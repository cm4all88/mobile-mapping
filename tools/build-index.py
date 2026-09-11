#!/usr/bin/env python3
"""Build deliverables/index.html -- the internal-review landing page.

One entry point, so a reviewer does not have to hunt through folders. The content
is deliverables/README.md; this only renders it in the shared visual system.

    python3 tools/build-index.py
"""
import base64, html, pathlib, re, runpy, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
_argv = sys.argv[:]
sys.argv = ['build-doc-page.py', 'sop']
mod = runpy.run_path(str(REPO / 'tools/build-doc-page.py'))
sys.argv = _argv
render, WORKVER = mod['render'], mod['WORKING_VERSION']

TPL = (REPO / 'tools/doc-page-template.html').read_text()
STYLE = TPL[TPL.index('<style>'):TPL.index('</style>') + len('</style>')]
LOGO = base64.b64encode((REPO / 'brand/logo/parametrix-logo-primary.png').read_bytes()).decode()
LOGO_KO = base64.b64encode((REPO / 'brand/logo/parametrix-logo-knockout.png').read_bytes()).decode()

CSS = """
<style>
body{background:var(--ground);color:var(--ink);margin:0}
.wrap{max-width:920px;margin:0 auto;padding:34px 22px 70px}
.ix-head{display:flex;align-items:flex-start;gap:16px;margin-bottom:6px}
.ix-head img{height:30px;width:auto}
:root:not([data-theme="light"]) .ix-head .mark-light{display:none}
:root:not([data-theme="light"]) .ix-head .mark-dark{display:block}
:root[data-theme="light"] .ix-head .mark-light{display:block}
:root[data-theme="light"] .ix-head .mark-dark{display:none}
.ix-head .mark-dark{display:none}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]) .ix-head .mark-light{display:block}
  :root:not([data-theme="dark"]) .ix-head .mark-dark{display:none}}
.ix-k{font:600 10.5px/1.4 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
h1.ix-n{font:700 30px/1.15 var(--sans);margin:4px 0 8px;color:var(--ink)}
.ix-badge{display:inline-block;font:600 10px/1.6 var(--sans);letter-spacing:.1em;
  text-transform:uppercase;background:var(--brand-calm-orange);color:var(--brand-charcoal);
  padding:3px 10px;border-radius:2px}
.ix-rule{height:3px;background:linear-gradient(90deg,var(--brand-blue) 0 25%,var(--brand-orange) 25% 50%,
  var(--brand-green) 50% 75%,var(--brand-yellow) 75% 100%);margin:16px 0 28px;border-radius:2px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(212px,1fr));gap:12px;margin:22px 0 8px}
.card{display:block;text-decoration:none;border:1px solid var(--rule);border-radius:4px;
  padding:14px 15px;background:var(--panel);border-top:3px solid var(--c)}
.card:hover{border-color:var(--c)}
.card b{display:block;font:700 15px/1.3 var(--sans);color:var(--ink);margin-bottom:4px}
.card span{font:500 12.5px/1.5 var(--sans);color:var(--muted)}
.ix-foot{margin-top:40px;padding-top:12px;border-top:1px solid var(--rule);
  font:500 11.5px/1.6 var(--sans);color:var(--muted)}
#theme{position:fixed;top:12px;right:12px;font:600 10.5px/1 var(--sans);letter-spacing:.08em;
  text-transform:uppercase;background:var(--panel);color:var(--ink);border:1px solid var(--rule);
  border-radius:3px;padding:7px 10px;cursor:pointer}
@media print{#theme,.cards{display:none}.wrap{max-width:none;padding:0}}
@media (max-width:520px){.wrap{padding:20px 14px 50px}h1.ix-n{font-size:24px}}
</style>
"""

CARDS = [
    ('technical-manual/technical-manual.html', 'Technical Manual', 'Why it works this way, and the evidence', 'var(--brand-blue)'),
    ('sop/sop.html', 'SOP', 'What is required, and on whose authority', 'var(--brand-orange)'),
    ('field-how-to/field-how-to.html', 'Field How To', 'How to run it in the vehicle', 'var(--brand-green)'),
    ('office-how-to/office-how-to.html', 'Office How To', 'How to process it in TBC', 'var(--brand-yellow)'),
]
SHEETS = [
    ('field-how-to/sheets/a-preflight-checklist.html', 'Preflight Checklist', 'Field How To Appendix A'),
    ('field-how-to/sheets/b-end-of-mission-checklist.html', 'End-of-Mission Checklist', 'Field How To Appendix B'),
    ('field-how-to/sheets/c-field-record-form.html', 'Field Record Form', 'Field How To Appendix C'),
    ('field-how-to/sheets/e-quick-card.html', 'Quick Card', 'Field How To Appendix E'),
]

md = (REPO / 'deliverables/README.md').read_text()
md = md.split('\n', 1)[1]                      # the shell carries the title
body = render(md, 'ix')

cards = '<div class="cards">' + ''.join(
    f'<a class="card" href="{h}" style="--c:{c}"><b>{html.escape(n)}</b><span>{html.escape(d)}</span></a>'
    for h, n, d, c in CARDS) + '</div>'
sheets = '<div class="cards">' + ''.join(
    f'<a class="card" href="{h}" style="--c:var(--brand-green)"><b>{html.escape(n)}</b>'
    f'<span>{html.escape(d)} · prints on its own</span></a>' for h, n, d in SHEETS) + '</div>'

# put the document cards under the "The documents" heading, the sheets under "Print on its own"
body = body.replace('<h3 id="ix-the-documents">The documents</h3>',
                    '<h3 id="ix-the-documents">The documents</h3>' + cards, 1)
body = body.replace('<h4 id="ix-print-on-its-own">Print on its own</h4>',
                    '<h4 id="ix-print-on-its-own">Print on its own</h4>' + sheets, 1)

out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Parametrix MX60 Mobile Mapping — Internal Review</title>
{STYLE}
{CSS}
</head>
<body style="--doc-accent:var(--brand-charcoal);--doc-accent-on:#fff">
<button id="theme" type="button">Theme</button>
<div class="wrap">
  <header class="ix-head">
    <img class="mark-light" src="data:image/png;base64,{LOGO}" alt="Parametrix">
    <img class="mark-dark" src="data:image/png;base64,{LOGO_KO}" alt="Parametrix">
    <div>
      <div class="ix-k">MX60 Mobile Mapping</div>
      <h1 class="ix-n">Internal Review</h1>
      <span class="ix-badge">Living Draft — Internal Review · Working Version {WORKVER}</span>
    </div>
  </header>
  <div class="ix-rule"></div>
  {body}
  <footer class="ix-foot">Parametrix · MX60 Mobile Mapping documentation set ·
    Working Version {WORKVER} · <b>not issued, not approved</b></footer>
</div>
<script>
(function(){{
  var root=document.documentElement;
  try{{var t=localStorage.getItem('pmx-theme'); if(t) root.setAttribute('data-theme',t);}}catch(e){{}}
  document.getElementById('theme').addEventListener('click',function(){{
    var dark=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')
      && matchMedia('(prefers-color-scheme:dark)').matches);
    var n=dark?'light':'dark'; root.setAttribute('data-theme',n);
    try{{localStorage.setItem('pmx-theme',n);}}catch(e){{}}
  }});
}})();
</script>
</body>
</html>
"""
p = REPO / 'deliverables/index.html'
p.write_text(out)
print(f'  {p.relative_to(REPO)}  {len(out)//1024} KB  ·  Working Version {WORKVER}')
