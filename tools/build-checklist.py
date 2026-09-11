#!/usr/bin/env python3
"""Render tools/field-checklist.html to SOP/Parametrix-MX60-Field-Checklist.pdf.

Uses headless Chromium via Playwright. LibreOffice and pandoc are not usable in
every environment; Chromium is preinstalled at /opt/pw-browsers.

    pip install playwright pypdfium2
    python tools/build-checklist.py
"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO / "tools/field-checklist.html"
LOGO = REPO / "brand/parametrix-wordmark.png"
OUT = REPO / "SOP/Parametrix-MX60-Field-Checklist.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

FOOTER = (
    '<div style="font-size:7pt;color:#9A9A93;width:100%;padding:0 0.5in;'
    'font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between;">'
    '<span>Parametrix &middot; Trimble MX60 Mobile Mapping SOP &middot; Appendix A</span>'
    '<span>DRAFT — not approved for use &nbsp;&middot;&nbsp; '
    '<span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
)

html = SRC.read_text().replace(
    "LOGO", "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
)
tmp = REPO / "tools/.checklist-rendered.html"
tmp.write_text(html)

try:
    with sync_playwright() as p:
        kw = {"args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        if pathlib.Path(CHROME).exists():
            kw["executable_path"] = CHROME
        b = p.chromium.launch(**kw)
        pg = b.new_page()
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(600)
        pg.pdf(path=str(OUT), format="Letter", print_background=True,
               display_header_footer=True, header_template="<span></span>",
               footer_template=FOOTER,
               margin={"top": "0.45in", "bottom": "0.6in", "left": "0.5in", "right": "0.5in"})
        b.close()
finally:
    tmp.unlink(missing_ok=True)

print(f"wrote {OUT}")
