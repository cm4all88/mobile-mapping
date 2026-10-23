#!/usr/bin/env python3
"""Build the MX60 Field Tools app from the eight source appendices.

    python3 tools/build-field-app.py            # write both targets
    python3 tools/build-field-app.py --check    # fail if either is stale
    python3 tools/build-field-app.py --dump KEY # print one parsed form as JSON

WHY IT IS BUILT AND NOT WRITTEN

The eight forms are appendices of the Field How To and the Office How To. A
second hand-written copy of any of them inside an HTML file is a copy that
drifts, and this project already carries the scar: `tools/build-checklist.py`
produced a PDF whose Appendix A source was rewritten underneath it. So every
item, field, section reference and callout is read out of the markdown here, and
`--check` is a gate in `tools/check-all.py`.

WHAT IS DERIVED

  structure  the groups and their titles; every checklist item with its emphasis
             and its step number; every field of the Field Record Form with its
             choices, blanks and repeating tables; the callouts; the prose that
             introduces a form or qualifies a group.

  authority  the section references beside each item, resolved to the heading
             they point at -- in this form's own document, or in the SOP or the
             Technical Manual where the cell names one.

  what binds which checklist items may be marked N/A (their own text reads "if
             fitted"), and which fields of the Field Record Form are required
             (the document sets them in bold; see CONDITIONAL ITEMS

An item may be marked N/A only where the document makes it conditional -- its
own text reads "if fitted" or opens with "If ...", or its group is qualified,
as "Run-to-run, if used" is. Fourteen of the two hundred and twenty items
qualify. Nothing else can be set aside.

REQUIRED BY EMPHASIS below).

WHAT IS DECLARED

  `deliverables/_control/field-app-fields.csv` -- the few checklist items whose
  own text asks for a value rather than a tick. Each row must match exactly one
  item of the form it names, or the build fails, so an edit to a source cannot
  leave a stale override behind.

CONDITIONAL ITEMS

An item may be marked N/A only where the document makes it conditional -- its
own text reads "if fitted" or opens with "If ...", or its group is qualified,
as "Run-to-run, if used" is. Fourteen of the two hundred and twenty items
qualify. Nothing else can be set aside.

REQUIRED BY EMPHASIS

The Field Record Form has fifty-odd fields and requiring all of them would make
the form unusable and the requirement a lie -- "Weather changes during" is
blank on most missions. The document already says which ones matter: it sets
them in bold. Mission ID, the capture settings, the presentation shown, the two
times, the closing sequence, the run count, POS_1/raw and the disk-cleared
question are bold in the source and required in the app. Nothing is added to
that list here.

TWO TARGETS, ONE SOURCE

  file       `field-app/MX60-Field-Tools.html`, self-contained, for the iPad. It
             works with no signal, it prints, and it writes PDFs.
  review     a copy for a claude.ai link. The artifact frame blocks
             `window.print()`, so that copy says so and offers the record on
             screen instead.
"""
import base64, csv, hashlib, html, json, pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DELIV = REPO / 'deliverables'
FIELDS = DELIV / '_control/field-app-fields.csv'
TPL = pathlib.Path(__file__).with_name('field-app-template.html')
OUT_FILE = REPO / 'field-app/MX60-Field-Tools.html'
OUT_REVIEW = REPO / 'field-app/review-copy/MX60-Field-Tools.html'
JSPDF = REPO / 'vendor/jspdf.umd.min.js'

WORKING_VERSION = re.search(r"^DRAFT = '([^']+)'",
                            (REPO / 'tools/sync-circulation.py').read_text(),
                            re.M).group(1)

DOCS = {'field':  ('field-how-to',     'Field How To'),
        'office': ('office-how-to',    'Office How To'),
        'sop':    ('sop',              'SOP'),
        'manual': ('technical-manual', 'Technical Manual')}

# The eight forms, in the order a mission actually goes through them.
FORMS = [
    dict(key='preflight',   doc='field',  kind='checklist', stage='Field',
         src='appendix-A-preflight-checklist.md', code='PF',
         short='Preflight', blurb='Before the vehicle leaves the yard.'),
    dict(key='field-record', doc='field', kind='form', stage='Field',
         src='appendix-C-field-record-form.md', code='FR',
         short='Field Record', blurb='The only record of what the office cannot see.'),
    dict(key='end-of-mission', doc='field', kind='checklist', stage='Field',
         src='appendix-B-end-of-mission-checklist.md', code='EM',
         short='End of Mission', blurb='Before the vehicle leaves the corridor.'),
    dict(key='office-processing', doc='office', kind='checklist', stage='Office',
         src='appendix-A-office-processing-checklist.md', code='OP',
         short='Office Processing', blurb='Intake to delivery.'),
    dict(key='registration', doc='office', kind='checklist', stage='Office',
         src='appendix-B-registration-checklist.md', code='RG',
         short='Registration', blurb='Control, picks and the adjusted trajectory.'),
    dict(key='qc', doc='office', kind='checklist', stage='Office',
         src='appendix-C-qc-checklist.md', code='QC',
         short='QC', blurb='Eight layers. None is optional.'),
    dict(key='export-delivery', doc='office', kind='checklist', stage='Office',
         src='appendix-D-export-and-delivery-checklist.md', code='ED',
         short='Export and Delivery', blurb='The gate, the export and what goes with it.'),
    dict(key='archive-cleanup', doc='office', kind='checklist', stage='Office',
         src='appendix-E-archive-and-cleanup-checklist.md', code='AC',
         short='Archive and Cleanup', blurb='Archive first. Cleanup cannot be undone.'),
]

# Job fields carried between every form, so nothing is typed twice.
JOB = [
    dict(id='project',  label='Project number', type='text',   always=True),
    dict(id='task',     label='Task number',    type='text',   always=True),
    dict(id='date',     label='Date',           type='date',   always=True),
    dict(id='operator', label='Operator',       type='text',   always=True),
    dict(id='vehicle',  label='Vehicle',        type='text',   always=False),  # Field only
]
JOB_LABELS = {j['label'].lower(): j['id'] for j in JOB}
# How a source document names a job field, where it names it differently.
JOB_LABELS['project'] = 'project'
JOB_LABELS['task'] = 'task'
JOB_LABELS['mission id'] = None          # a form-level field, not a job field


# --------------------------------------------------------------- inline ----
def inline(t):
    """Markdown as the source writes it: bold, italic and code survive."""
    t = html.escape(t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\w])\*([^*]+)\*(?!\w)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def plain(t):
    return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', t)).strip()


# ------------------------------------------------------------- headings ----
def headings(folder):
    out = {}
    for f in sorted((DELIV / folder).glob('[0-3][0-9]-*.md')):
        for line in f.read_text(encoding='utf-8').splitlines():
            m = re.match(r'^#{1,3} (\d+(?:\.\d+)?)\.? +(.+)$', line)
            if m:
                out[m.group(1)] = plain(m.group(2))
    return out


SECTIONS = {k: headings(v[0]) for k, v in DOCS.items()}
DOCWORD = {'sop': 'sop', 'technical manual': 'manual', 'office how to': 'office',
           'field how to': 'field'}


def refs(cell, home):
    """The § column -> [{n, title, doc}]. A cell may name another document."""
    out, doc = [], home
    for m in re.finditer(r'(SOP|Technical Manual|Office How To|Field How To)?'
                         r'\s*&?§?\s*(\d+(?:\.\d+)?)', cell):
        if m.group(1):
            doc = DOCWORD[m.group(1).lower()]
        n = m.group(2)
        title = SECTIONS[doc].get(n)
        if title is None:
            sys.exit(f'section reference with no heading: {DOCS[doc][1]} §{n}  '
                     f'(from "{cell.strip()}")')
        out.append({'n': n, 'title': title,
                    'doc': DOCS[doc][1] if doc != home else ''})
    return out


# --------------------------------------------------------------- tables ----
def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def is_rule(line):
    return bool(re.match(r'^\|[\s:|-]+\|$', line.strip()))


# ------------------------------------------------------ the record form ----
BLANK = '______'


def parse_spec(spec):
    """One value cell of the Field Record Form -> the controls it asks for.

    The form writes its controls in plain marks, and each one means something
    specific:

      (empty)                     a line to write on            -> text
      '☐'                         one box to tick               -> check
      '______ min'                a blank with its unit          -> text, hinted
      '☐ a ☐ b ☐ c'               pick one of these             -> choice
      '☐ yes — time: ______'      pick one, then say which/when -> choice + text
      '☐ yes, received from:'     an option that asks for a name  -> choice + text
      'a · b'                     two controls in one cell      -> two parts
    """
    parts = []
    for seg in re.split(r'\s+·\s+', spec):
        seg = seg.strip()
        if not seg:
            continue
        boxes = seg.count('☐')
        lead = seg.split('☐')[0].strip() if boxes else ''
        if boxes == 0:
            hint = ''
            m = re.search(re.escape(BLANK) + r'\s*(\S+)?', seg)
            if m:
                hint = (m.group(1) or '').strip()
            parts.append({'kind': 'text', 'label': plain(re.sub(
                re.escape(BLANK) + r'.*$', '', seg)), 'hint': hint})
        elif boxes == 1 and not re.sub(r'☐', '', seg).strip():
            parts.append({'kind': 'check', 'label': lead})
        elif boxes == 1:
            parts.append({'kind': 'check', 'label': plain(seg.replace('☐', ''))})
        else:
            opts = []
            for raw in [o.strip() for o in seg.split('☐')[1:]]:
                # "yes — time: ______" is one option plus the thing it asks for
                m = re.match(r'^(.*?)\s*—\s*(.+)$', raw)
                follow = ''
                if m and (BLANK in m.group(2) or m.group(2).rstrip().endswith(':')):
                    raw, follow = m.group(1), re.sub(
                        re.escape(BLANK), '', m.group(2)).strip().rstrip(':')
                elif raw.rstrip().endswith(':'):
                    # "yes, confirmation received from:" asks for the name
                    raw = follow = raw.rstrip().rstrip(':')
                opts.append({'t': plain(raw), 'html': inline(raw),
                             'follow': plain(follow)})
            parts.append({'kind': 'choice', 'label': plain(lead), 'options': opts})
    return parts or [{'kind': 'text', 'label': '', 'hint': ''}]


def parse_record_form(lines, form):
    """Appendix C: groups of labelled fields, plus the repeating tables."""
    groups, g, intro, i = [], None, [], 0
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        m = re.match(r'^## ([A-Z]\d+) · (.+)$', s)
        if m:
            g = {'id': m.group(1), 'title': plain(m.group(2)), 'note': None,
                 'pointer': None, 'items': [], 'fields': [], 'table': None}
            groups.append(g)
            i += 1
            continue
        if s.startswith('**Signed**'):
            form['sign'] = 'Signed'
            i += 1
            continue
        if s.startswith('|') and i + 1 < len(lines) and is_rule(lines[i + 1]):
            head = cells(s)
            body = []
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                body.append(cells(lines[j].strip()))
                j += 1
            if len(head) == 2 and not any(head):
                for row in body:
                    if not row[0]:
                        continue
                    label = plain(row[0])
                    job = JOB_LABELS.get(label.lower())
                    g['fields'].append({
                        'id': f'{g["id"]}-{len(g["fields"]) + 1}',
                        'label': label, 'labelHtml': inline(row[0]),
                        # the document sets the fields it will not do without in
                        # bold; that emphasis is the requirement, not a new rule
                        'required': '**' in row[0] or bool(job),
                        # a field the job header already carries is shown filled
                        # in from the job, never typed a second time
                        'job': job,
                        'parts': [] if job else parse_spec(row[1])})
            else:
                tmpl = body[0] if body else [''] * len(head)
                g['table'] = {
                    'id': g['id'],
                    'cols': [{'name': plain(h),
                              'parts': parse_spec(tmpl[k] if k < len(tmpl) else '')}
                             for k, h in enumerate(head)],
                    'rows': max(1, len(body))}
            i = j
            continue
        if s.startswith('>'):
            block, j = [], i
            while j < len(lines) and (lines[j].strip().startswith('>')
                                      or (block and not lines[j].strip())):
                if lines[j].strip().startswith('>'):
                    block.append(re.sub(r'^>\s?', '', lines[j].strip()))
                j += 1
            note = inline('\n'.join(block)).replace('\n', '<br>')
            if g:
                g['note'] = ((g['note'] + '<br>') if g['note'] else '') + note
            else:
                intro.append(note)
            i = j
            continue
        if s and not s.startswith('#') and s != '---':
            if g is None:
                intro.append(inline(s))
            elif not g['fields'] and not g['table']:
                g['pointer'] = inline(s)
            else:
                g['note'] = ((g['note'] + '<br>') if g['note'] else '') + inline(s)
        i += 1
    form['intro'] = ' '.join(intro)
    return groups


# -------------------------------------------------------- the checklists ----
def parse_checklist(lines, form):
    """Any of the seven checklists, whatever its table is shaped like.

    The tables are not one shape. The first column is always the box; the last
    is the § column only when the header says §; a '#' column is a step number;
    and whatever is left is the item, with any further column kept as a labelled
    second line rather than thrown away -- "Looking for", "Evidence produced".
    """
    groups, g, intro, i = [], None, [], 0
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        m = re.match(r'^## ([A-Z]\d+) · (.+)$', s)
        if m:
            g = {'id': m.group(1), 'title': plain(m.group(2)), 'note': None,
                 'pointer': None, 'items': [], 'fields': [], 'table': None}
            groups.append(g)
            i += 1
            continue
        if s.startswith('**Signed**'):
            form['sign'] = 'Signed'
            i += 1
            continue
        if '________' in s and s.startswith('**'):
            form['_header'] = re.findall(r'\*\*([^*]+)\*\*', s)
            i += 1
            continue
        if s.startswith('|') and i + 1 < len(lines) and is_rule(lines[i + 1]):
            head = cells(s)
            has_ref = head[-1] in ('§',)
            num_col = head.index('#') if '#' in head else None
            text_cols = [k for k in range(1, len(head))
                         if k != num_col and not (has_ref and k == len(head) - 1)]
            if g is None:                     # a table before any group heading
                g = {'id': form['appendix'].replace('Appendix ', '') + '0',
                     'title': form['name'], 'note': None, 'pointer': None,
                     'items': [], 'fields': [], 'table': None}
                groups.append(g)
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                row = cells(lines[j].strip())
                j += 1
                if not row or row[0] != '☐' or len(row) < 2:
                    continue
                body = [row[k] for k in text_cols if k < len(row)]
                if not any(body):
                    continue
                text = body[0]
                sub = [{'label': plain(head[text_cols[k]]), 'html': inline(body[k])}
                       for k in range(1, len(body)) if body[k]]
                g['items'].append({
                    'id': f'{g["id"]}-{len(g["items"]) + 1}',
                    'n': row[num_col].strip() if num_col is not None
                         and num_col < len(row) else '',
                    'html': inline(text), 'text': plain(text), 'sub': sub,
                    'refs': refs(row[-1], form['doc']) if has_ref else [],
                    # Only a conditional item may be marked N/A: one whose own
                    # text says "if fitted" or opens with "If ...", or one in a
                    # group the document itself qualifies ("Run-to-run, if
                    # used"). Every other item is a tick or an unfinished
                    # checklist; a gate that cannot be satisfied honestly is a
                    # gate crews learn to tick through.
                    'na': bool(re.search(r'if fitted|, if |^If ', text))
                          or bool(re.search(r', if \w', g['title'])),
                    'field': None})
            i = j
            continue
        if s.startswith('>'):
            block, j = [], i
            while j < len(lines) and (lines[j].strip().startswith('>')
                                      or (block and not lines[j].strip())):
                if lines[j].strip().startswith('>'):
                    block.append(re.sub(r'^>\s?', '', lines[j].strip()))
                j += 1
            note = inline('\n'.join(block)).replace('\n', '<br>')
            if g:
                g['note'] = ((g['note'] + '<br>') if g['note'] else '') + note
            else:
                intro.append(note)
            i = j
            continue
        if s and not s.startswith('#') and s != '---':
            if g is None:
                intro.append(inline(s))
            elif not g['items']:
                g['pointer'] = inline(s)
            else:
                g['note'] = ((g['note'] + '<br>') if g['note'] else '') + inline(s)
        i += 1
    form['intro'] = ' '.join(intro)
    return groups


# ------------------------------------------------------------- assemble ----
def build_form(spec):
    path = DELIV / DOCS[spec['doc']][0] / spec['src']
    raw = path.read_text(encoding='utf-8')
    title = re.match(r'^# (Appendix [A-Z]) — (.+)$', raw.splitlines()[0])
    if not title:
        sys.exit(f'{spec["src"]}: the first line is not "# Appendix X — Name"')
    form = dict(spec)
    form.pop('src')
    form.update({'appendix': title.group(1), 'name': plain(title.group(2)),
                 'docName': DOCS[spec['doc']][1], 'source': spec['src'],
                 'sourceHash': 'sha256:' + hashlib.sha256(raw.encode()).hexdigest()[:16],
                 'sign': None, 'meta': [], 'intro': '', '_header': []})
    lines = raw.splitlines()[1:]
    parse = parse_record_form if spec['kind'] == 'form' else parse_checklist
    form['groups'] = parse(lines, form)
    # a header name the job already carries is not asked for twice
    for lbl in form.pop('_header'):
        if JOB_LABELS.get(lbl.lower(), 'x') is None:
            form['meta'].append({'id': re.sub(r'\W+', '', lbl.lower()),
                                 'label': lbl, 'type': 'text'})
        elif lbl.lower() not in JOB_LABELS:
            sys.exit(f'{spec["src"]}: header field "{lbl}" is neither a job field '
                     f'nor a known form field — add it to JOB or JOB_LABELS')
    # The Field Record Form names Mission ID in its own C1 table, so the header
    # does not need to ask for it a second time.
    if spec['kind'] == 'form':
        form['meta'] = []
    form['items'] = [it for g in form['groups'] for it in g['items']]
    form['count'] = len(form['items']) if spec['kind'] == 'checklist' else \
        sum(1 for g in form['groups'] for f in g['fields'] if f['required'])
    form['fieldCount'] = sum(len(g['fields']) for g in form['groups'])
    return form


FORMSET = {f['key']: build_form(f) for f in FORMS}

# ---- the declared value-bearing checklist items ----
for row in csv.DictReader(FIELDS.open(encoding='utf-8')):
    f = FORMSET.get(row['form'])
    if f is None:
        sys.exit(f'{FIELDS.name}: unknown form "{row["form"]}"')
    hits = [it for it in f['items'] if row['match'] in it['text']]
    if len(hits) != 1:
        sys.exit(f'{FIELDS.name}: "{row["match"]}" matches {len(hits)} items of '
                 f'{row["form"]}, expected 1')
    hits[0]['field'] = {'type': row['type'], 'label': row['label']}

for f in FORMSET.values():
    f.pop('items')
    for g in f['groups']:
        if f['kind'] == 'checklist':
            g.pop('fields'); g.pop('table')
        else:
            g.pop('items')

if '--dump' in sys.argv:
    print(json.dumps(FORMSET[sys.argv[sys.argv.index('--dump') + 1]],
                     indent=1, ensure_ascii=False))
    sys.exit(0)

DATA = {
    'app': 'MX60 Field Tools', 'system': 'Trimble MX60 Premium',
    'version': WORKING_VERSION, 'job': JOB,
    'order': [f['key'] for f in FORMS],
    'forms': FORMSET,
}


def b64(rel):
    return base64.b64encode((REPO / rel).read_bytes()).decode()


TOKENS = (REPO / 'deliverables/_control/style/brand-tokens.css').read_text()
TOKENS = TOKENS[:TOKENS.index('/* --- the spacer arrow')].rstrip() + '\n'

SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="MX60 Field">
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
            .replace('{{JSPDF}}', JSPDF.read_text())
            .replace('{{DATA}}', json.dumps(DATA, ensure_ascii=False))
            .replace('{{TARGET}}', target)
            .replace('{{LOGO}}', b64('brand/logo/parametrix-logo-primary.png'))
            .replace('{{LOGO_KO}}', b64('brand/logo/parametrix-logo-knockout.png')))
    left = re.findall(r'\{\{\w+\}\}', page)
    if left:
        sys.exit('unreplaced placeholder: ' + str(sorted(set(left))))
    return SKELETON.replace('{{PAGE}}', page) if target == 'file' else page


OUTS = [(OUT_FILE, 'file'), (OUT_REVIEW, 'review')]

if '--check' in sys.argv:
    stale = [str(p.relative_to(REPO)) for p, t in OUTS
             if not p.exists() or p.read_text() != build(t)]
    if stale:
        print('the Field Tools app is stale against its sources: ' + ', '.join(stale))
        print('  rebuild: python3 tools/build-field-app.py')
        sys.exit(1)
    print(f'Field Tools app current ({len(FORMS)} forms)')
    sys.exit(0)

for p, t in OUTS:
    p.parent.mkdir(parents=True, exist_ok=True)
    page = build(t)
    p.write_text(page)
    print(f'{t:7} -> {p.relative_to(REPO)}  {len(page) / 1024:.0f} KB')
print()
for f in FORMS:
    d = FORMSET[f['key']]
    n = sum(len(g['items']) for g in d['groups']) if d['kind'] == 'checklist' \
        else d['fieldCount']
    na = sum(1 for g in d['groups'] for i in g.get('items', []) if i['na'])
    val = sum(1 for g in d['groups'] for i in g.get('items', []) if i['field'])
    req = d['count'] if d['kind'] == 'form' else n
    tab = sum(1 for g in d['groups'] if g.get('table'))
    print(f'  {d["docName"]:13} {d["appendix"]:11} {d["name"][:30]:32} '
          f'{d["kind"]:9} {n:3} {"items" if d["kind"] == "checklist" else "fields"}'
          f' · {req} required'
          + (f' · {na} may be N/A' if na else '')
          + (f' · {val} take a value' if val else '')
          + (f' · {tab} tables' if tab else ''))
