#!/usr/bin/env python3
"""Render the circulation package to PDF, through the print layer.

These are NOT controlled PDFs. They are the HTML documents printed for people
who would rather read on paper, and each page says so -- the running header
carries the Working Version and the Living Draft status.

    pip install playwright
    python3 tools/build-pdfs.py
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / 'deliverables/pdf'
WORKVER = __import__('re').search(r"^DRAFT = '([^']+)'",
    (REPO / 'tools/sync-circulation.py').read_text(), 8).group(1)

PAGES = [
    ('deliverables/index.html',                        'MX60-Internal-Review'),
    ('deliverables/technical-manual/technical-manual.html', 'MX60-Technical-Manual'),
    ('deliverables/sop/sop.html',                      'MX60-SOP'),
    ('deliverables/field-how-to/field-how-to.html',    'MX60-Field-How-To'),
    ('deliverables/office-how-to/office-how-to.html',  'MX60-Office-How-To'),
    ('deliverables/field-how-to/sheets/a-preflight-checklist.html',     'MX60-Sheet-A-Preflight-Checklist'),
    ('deliverables/field-how-to/sheets/b-end-of-mission-checklist.html','MX60-Sheet-B-End-of-Mission-Checklist'),
    ('deliverables/field-how-to/sheets/c-field-record-form.html',       'MX60-Sheet-C-Field-Record-Form'),
    ('deliverables/field-how-to/sheets/e-quick-card.html',              'MX60-Sheet-E-Quick-Card'),
]

HDR = ('<div style="font:600 6.5pt system-ui;color:#939598;width:100%;padding:0 16mm;'
       'letter-spacing:.06em;text-transform:uppercase">PARAMETRIX &middot; MX60 MOBILE MAPPING '
       f'&middot; WORKING VERSION {WORKVER} &middot; LIVING DRAFT — INTERNAL REVIEW</div>')
FTR = ('<div style="font:500 6.5pt system-ui;color:#939598;width:100%;padding:0 16mm;'
       'display:flex;justify-content:space-between">'
       '<span>Not a controlled document. Not approved.</span>'
       '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')

OUT.mkdir(exist_ok=True)
made = []
with sync_playwright() as pw:
    exe = next((str(x) for x in [
        pathlib.Path('/opt/pw-browsers/chromium-1194/chrome-linux/chrome'),
    ] if x.exists()), None)
    b = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
    pg = b.new_page()
    for rel, name in PAGES:
        src = REPO / rel
        if not src.exists():
            print(f'  MISSING {rel}'); sys.exit(1)
        pg.goto(src.as_uri(), wait_until='load')
        pg.emulate_media(media='print')
        dst = OUT / f'{name}_{WORKVER}.pdf'
        pg.pdf(path=str(dst), format='A4', print_background=True,
               display_header_footer=True, header_template=HDR, footer_template=FTR,
               margin={'top': '17mm', 'bottom': '16mm', 'left': '0mm', 'right': '0mm'})
        made.append(dst)
        print(f'  {dst.relative_to(REPO)}  {dst.stat().st_size // 1024} KB')
    b.close()
print(f'{len(made)} PDFs at Working Version {WORKVER}')
