#!/usr/bin/env python3
"""Build the four Field sheets as standalone printable pages.

The Preflight Checklist, the End-of-Mission Checklist, the Field Record Form and
the Quick Card are used away from a screen. In the Field How To they are
appendices behind the navigation; here each becomes one self-contained HTML file
that prints on its own, carrying Parametrix, the document it came from, the sheet
name, the Working Version and the Living Draft status on the page itself.

The styling is the same style block as the four documents -- the sheets are not a
second visual system.

    python3 tools/build-field-sheets.py
"""
import base64, html, pathlib, re, runpy, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC  = REPO / 'deliverables/field-how-to'
OUT  = REPO / 'deliverables/field-how-to/sheets'

_argv = sys.argv[:]
sys.argv = ['build-doc-page.py', 'field']
mod = runpy.run_path(str(REPO / 'tools/build-doc-page.py'))
sys.argv = _argv
render, WORKVER = mod['render'], mod['WORKING_VERSION']

TPL = (REPO / 'tools/doc-page-template.html').read_text()
STYLE = TPL[TPL.index('<style>'):TPL.index('</style>') + len('</style>')]

SHEETS = [
    ('appendix-A-preflight-checklist',  'Appendix A', 'Preflight Checklist'),
    ('appendix-B-end-of-mission-checklist', 'Appendix B', 'End-of-Mission Checklist'),
    ('appendix-C-field-record-form',    'Appendix C', 'Field Record Form'),
    ('appendix-E-quick-card',           'Appendix E', 'Quick Card'),
]

SHEET_CSS = """
<style>
/* the sheet is a document, not an app: no rail, no search, no theme control */
body{background:var(--ground);color:var(--ink);margin:0}
.sheet{max-width:190mm;margin:0 auto;padding:14mm 12mm 18mm}
.sh-head{display:flex;align-items:flex-start;gap:14px;
  border-bottom:2px solid var(--doc-accent);padding-bottom:9px;margin-bottom:18px}
.sh-head img{height:26px;width:auto;flex:0 0 auto}
.sh-t{flex:1 1 auto;min-width:0}
.sh-k{font:600 10px/1.4 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.sh-n{font:700 22px/1.2 var(--sans);color:var(--ink);margin:2px 0 3px}
.sh-m{font:500 11px/1.5 var(--sans);color:var(--muted)}
.sh-status{display:inline-block;font:600 9.5px/1.5 var(--sans);letter-spacing:.1em;
  text-transform:uppercase;background:var(--doc-accent);color:var(--doc-accent-on);
  padding:2px 8px;border-radius:2px;margin-top:6px}
.sh-foot{margin-top:22px;padding-top:8px;border-top:1px solid var(--rule);
  font:500 10px/1.5 var(--sans);color:var(--muted);
  display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
@media print{
  .sheet{max-width:none;margin:0;padding:0}
  .sh-head{break-after:avoid-page;page-break-after:avoid}
  .sh-status{border:0.6pt solid #231F20 !important;background:#fff !important;color:#231F20 !important}
  .sh-foot{position:running(sheetfoot)}
  .sec{break-before:auto !important;page-break-before:auto !important}
  /* the sheets are meant to fit: tighter than the documents, on purpose */
  .sheet{font-size:9.6pt}
  .sheet table{font-size:8.7pt}
  .sheet td,.sheet th{padding:1.9mm 2.6mm !important}
  .sheet h3,.sheet h4{margin:5mm 0 2mm}
  .sheet .co{padding:2.4mm 3.2mm !important;margin:3mm 0 !important}
  .sheet p,.sheet li{margin:1.6mm 0}
}
@media (max-width:520px){ .sheet{padding:10mm 5mm} .sh-head{gap:9px} }
</style>
"""

def page(name, appx, title, body):
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Parametrix MX60 — {html.escape(title)}</title>
{STYLE}
{SHEET_CSS}
</head>
<body style="--doc-accent:var(--brand-green);--doc-accent-on:var(--brand-charcoal)">
<div class="sheet">
  <header class="sh-head">
    <img src="data:image/png;base64,{LOGO}" alt="Parametrix">
    <div class="sh-t">
      <div class="sh-k">MX60 Field How To · {html.escape(appx)}</div>
      <div class="sh-n">{html.escape(title)}</div>
      <div class="sh-m">Working Version {WORKVER} · Trimble MX60 · Trimble Mobile Imaging</div>
      <div class="sh-status">Living Draft — Internal Review</div>
    </div>
  </header>
  {body}
  <footer class="sh-foot">
    <span>Parametrix · MX60 Field How To · {html.escape(appx)} — {html.escape(title)}</span>
    <span>Working Version {WORKVER} · <b>not a controlled document</b></span>
  </footer>
</div>
</body>
</html>
"""

LOGO = base64.b64encode((REPO / 'brand/logo/parametrix-logo-primary.png').read_bytes()).decode()

OUT.mkdir(exist_ok=True)
for fn, appx, title in SHEETS:
    md = (SRC / f'{fn}.md').read_text()
    body = render(md, 'sh')
    out = OUT / f'{fn.replace("appendix-", "").lower()}.html'
    out.write_text(page(fn, appx, title, body))
    print(f'  {out.relative_to(REPO)}  {len(out.read_text())//1024} KB')
print(f'{len(SHEETS)} field sheets, Working Version {WORKVER}')
