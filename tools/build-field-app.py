#!/usr/bin/env python3
"""Build the tablet preflight checklist from Appendix A.

    python3 tools/build-field-app.py            # write both targets
    python3 tools/build-field-app.py --check    # fail if either is stale

WHY IT IS BUILT AND NOT WRITTEN

`deliverables/field-how-to/appendix-A-preflight-checklist.md` is the checklist.
A second hand-written copy of it inside an HTML file is a copy that drifts, and
this project already carries the scar: `tools/build-checklist.py` produced a PDF
whose Appendix A source was rewritten underneath it. So every item, every
section reference and the two header lines are read out of the markdown here,
and `--check` is a gate in `tools/check-all.py`.

WHAT IS DERIVED, AND WHAT IS DECLARED

  derived    the seven groups and their titles; all thirty-four items with their
             emphasis; the section references beside each one, resolved to the
             Field How To heading they point at; the Date/Operator/Vehicle header
             and the Signed footer; which items read "if fitted", which are the
             only ones the operator may mark N/A.

  declared   `deliverables/_control/field-app-fields.csv` — the few items whose
             own text asks for a value rather than a tick ("time recorded",
             "which presentation you saw recorded"). Each row must match exactly
             one item or the build fails, so an edit to Appendix A cannot leave a
             stale override behind.

TWO TARGETS, ONE SOURCE

  file       `field-app/MX60-preflight.html`, self-contained, for the iPad. It
             works with no signal and it prints.
  artifact   a copy for review through a claude.ai link. The artifact frame
             blocks `window.print()` and the page is fetched over the network, so
             that copy offers the record on screen instead of a Print button and
             says plainly that it is the review copy.
"""
import base64, csv, hashlib, html, json, pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
FIELD = REPO / 'deliverables/field-how-to'
SRC = FIELD / 'appendix-A-preflight-checklist.md'
FIELDS = REPO / 'deliverables/_control/field-app-fields.csv'
TPL = pathlib.Path(__file__).with_name('field-app-template.html')
OUT_FILE = REPO / 'field-app/MX60-preflight.html'
OUT_ART = REPO / 'field-app/review-copy/MX60-preflight.html'

WORKING_VERSION = re.search(r"^DRAFT = '([^']+)'",
                            (REPO / 'tools/sync-circulation.py').read_text(),
                            re.M).group(1)


def inline(t):
    """The item text as the markdown writes it: bold and code survive, nothing else."""
    t = html.escape(t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


# ---- the Field How To's own headings, so a section reference can name itself ----
def headings():
    out = {}
    for f in sorted(FIELD.glob('[0-2][0-9]-*.md')):
        for line in f.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^#{1,3} (\d+(?:\.\d+)?)\.? +(.+)$', line)
            if m:
                out[m.group(1)] = m.group(2).strip()
    return out


SECTIONS = headings()

# ---- Appendix A ----
raw = SRC.read_text(encoding='utf-8')
meta, groups, group = [], [], None

for line in raw.splitlines():
    s = line.strip()
    if not s:
        continue
    m = re.match(r'^## (A\d+) · (.+)$', s)
    if m:
        group = {'id': m.group(1), 'title': m.group(2).strip(), 'items': []}
        groups.append(group)
        continue
    # the header line: **Date** ____ **Operator** ____ **Vehicle** ____
    if s.startswith('**Date**'):
        meta = [{'id': lbl.lower(), 'label': lbl,
                 'type': 'date' if lbl == 'Date' else 'text'}
                for lbl in re.findall(r'\*\*([A-Z][a-z]+)\*\*', s)]
        continue
    if s.startswith('**Signed**'):
        continue
    cells = [c.strip() for c in s.split('|')[1:-1]] if s.startswith('|') else []
    if len(cells) == 3 and cells[0] == '☐' and cells[1] and cells[1] != '':
        text, refs = cells[1], cells[2]
        if group is None:
            sys.exit(f'{SRC.name}: an item appears before any group heading')
        group['items'].append({
            'id': f'{group["id"]}-{len(group["items"]) + 1}',
            'html': inline(text),
            'text': re.sub(r'[*`]', '', text),
            'refs': [{'n': n, 'title': SECTIONS.get(n, '')}
                     for n in re.findall(r'\d+(?:\.\d+)?', refs)],
            # Only an item whose own text says "if fitted" may be marked N/A.
            # Every other item is a tick or an unfinished checklist.
            'na': bool(re.search(r'if fitted', text, re.I)),
            'field': None,
        })

items = [it for g in groups for it in g['items']]
if not groups or not items:
    sys.exit(f'{SRC.name}: parsed {len(groups)} groups and {len(items)} items — check the file')
if not meta:
    sys.exit(f'{SRC.name}: no Date/Operator/Vehicle header line found')

missing = sorted({r['n'] for it in items for r in it['refs'] if not r['title']})
if missing:
    sys.exit(f'{SRC.name}: section reference(s) with no Field How To heading: {missing}')

# ---- the declared value-bearing items ----
for row in csv.DictReader(FIELDS.open(encoding='utf-8')):
    hits = [it for it in items if row['match'] in it['text']]
    if len(hits) != 1:
        sys.exit(f'{FIELDS.name}: "{row["match"]}" matches {len(hits)} items, expected 1')
    hits[0]['field'] = {'type': row['type'], 'label': row['label']}

DATA = {
    'doc': 'Field How To', 'appendix': 'Appendix A', 'name': 'Preflight Checklist',
    'system': 'Trimble MX60 Premium', 'version': WORKING_VERSION,
    # Deliberately no build date. The page is dated by the Working Version and
    # the source hash, both of which come from the documents; a date taken from
    # the clock would differ on every machine and turn --check red on its own
    # the day after a build.
    'source': SRC.name,
    'sourceHash': 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()[:16],
    'meta': meta, 'sign': 'Signed',
    'count': len(items), 'groups': groups,
}


def b64(rel):
    return base64.b64encode((REPO / rel).read_bytes()).decode()


TOKENS = (REPO / 'deliverables/_control/style/brand-tokens.css').read_text()
# the tokens file carries the spacer-arrow rules for a printed document; the app
# does not use them, and a rule with no element is noise in a field file
TOKENS = TOKENS[:TOKENS.index('/* --- the spacer arrow')].rstrip() + '\n'

SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Preflight">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px)}
html,body{margin:0}
body{font:14px/1.4 system-ui,-apple-system,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
{{PAGE}}
</body>
</html>
"""


def build(target):
    page = (TPL.read_text()
            .replace('{{TOKENS}}', TOKENS)
            .replace('{{DATA}}', json.dumps(DATA, ensure_ascii=False))
            .replace('{{TARGET}}', target)
            .replace('{{LOGO}}', b64('brand/logo/parametrix-logo-primary.png'))
            .replace('{{LOGO_KO}}', b64('brand/logo/parametrix-logo-knockout.png')))
    if '{{' in page:
        sys.exit('unreplaced placeholder: ' + str(re.findall(r'\{\{\w+\}\}', page)))
    return SKELETON.replace('{{PAGE}}', page) if target == 'file' else page


OUTS = [(OUT_FILE, 'file'), (OUT_ART, 'artifact')]

if '--check' in sys.argv:
    stale = [str(p.relative_to(REPO)) for p, t in OUTS
             if not p.exists() or p.read_text() != build(t)]
    if stale:
        print(f'the tablet checklist is stale against {SRC.name}: {", ".join(stale)}')
        print('  rebuild: python3 tools/build-field-app.py')
        sys.exit(1)
    print(f'tablet checklist current ({len(items)} items, '
          f'{sum(1 for i in items if i["na"])} may be N/A, '
          f'{sum(1 for i in items if i["field"])} take a value)')
    sys.exit(0)

for p, t in OUTS:
    p.parent.mkdir(parents=True, exist_ok=True)
    page = build(t)
    p.write_text(page)
    print(f'{t:9} -> {p.relative_to(REPO)}  {len(page) / 1024:.0f} KB')
print(f'{len(groups)} groups · {len(items)} items · '
      f'{sum(1 for i in items if i["na"])} may be N/A · '
      f'{sum(1 for i in items if i["field"])} take a value · '
      f'{len({r["n"] for i in items for r in i["refs"]})} sections referenced')
