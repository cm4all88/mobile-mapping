#!/usr/bin/env python3
"""Render the employee-facing documents to PDF, through the print layer.

The reader gets a Parametrix publication: a running header and footer carrying
the company and the document, and a page number. Nothing about how the file was
produced reaches the page.

    pip install playwright
    python3 tools/build-pdfs.py
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / 'deliverables/pdf'
# The employee-facing package. The internal review page is deliberately not here.
PAGES = [
    ('deliverables/technical-manual/technical-manual.html', 'Parametrix-MX60-Technical-Manual',
     'MX60 Mobile Mapping Technical Manual'),
    ('deliverables/sop/sop.html', 'Parametrix-MX60-SOP',
     'MX60 Mobile Mapping Standard Operating Procedure'),
    ('deliverables/field-how-to/field-how-to.html', 'Parametrix-MX60-Field-How-To',
     'MX60 Field How To'),
    ('deliverables/office-how-to/office-how-to.html', 'Parametrix-MX60-Office-How-To',
     'MX60 Office How To'),
    ('deliverables/field-how-to/sheets/a-preflight-checklist.html',
     'Parametrix-MX60-Preflight-Checklist', 'MX60 Field How To — Preflight Checklist'),
    ('deliverables/field-how-to/sheets/b-end-of-mission-checklist.html',
     'Parametrix-MX60-End-of-Mission-Checklist', 'MX60 Field How To — End-of-Mission Checklist'),
    ('deliverables/field-how-to/sheets/c-field-record-form.html',
     'Parametrix-MX60-Field-Record-Form', 'MX60 Field How To — Field Record Form'),
    ('deliverables/field-how-to/sheets/e-quick-card.html',
     'Parametrix-MX60-Quick-Card', 'MX60 Field How To — Quick Card'),
]

def furniture(title):
    hdr = ('<div style="font:600 6.5pt system-ui;color:#B3B4B5;width:100%;padding:0 16mm;'
           'letter-spacing:.08em;text-transform:uppercase">'
           f'Parametrix &nbsp;|&nbsp; {title}</div>')
    ftr = ('<div style="font:500 7.5pt system-ui;color:#939598;width:100%;padding:0 16mm;'
           'display:flex;justify-content:space-between">'
           f'<span>Parametrix &nbsp;|&nbsp; {title}</span>'
           '<span>Page <span class="pageNumber"></span></span></div>')
    return hdr, ftr

OUT.mkdir(exist_ok=True)
made = []
with sync_playwright() as pw:
    exe = next((str(x) for x in [
        pathlib.Path('/opt/pw-browsers/chromium-1194/chrome-linux/chrome'),
    ] if x.exists()), None)
    b = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
    pg = b.new_page()
    for rel, name, title in PAGES:
        src = REPO / rel
        if not src.exists():
            print(f'  MISSING {rel}'); sys.exit(1)
        pg.goto(src.as_uri(), wait_until='load')
        pg.emulate_media(media='print')
        hdr, ftr = furniture(title)
        dst = OUT / f'{name}.pdf'
        pg.pdf(path=str(dst), format='A4', print_background=True,
               display_header_footer=True, header_template=hdr, footer_template=ftr,
               margin={'top': '17mm', 'bottom': '16mm', 'left': '0mm', 'right': '0mm'})
        made.append(dst)
        print(f'  {dst.relative_to(REPO)}  {dst.stat().st_size // 1024} KB')
    b.close()
print(f'{len(made)} PDFs')
