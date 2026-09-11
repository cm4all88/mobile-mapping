#!/usr/bin/env python3
"""Re-derive the control artefacts that describe the documents, from the documents.

Two columns were written before the four deliverables existed and have drifted:

  master-register.csv  affected_documents   where each open item is actually raised
  ownership-matrix.md  the ref / — columns  which documents reference each topic

Both are *descriptions* of the documents, so both are derived here rather than
maintained by hand. What is NOT derived: the ● column of the ownership matrix,
which is a design decision about where a statement belongs, and every other
column of the register, which is judgement.

    python3 tools/sync-control.py [--check]

--check reports drift and exits 1 without writing, for use before an issue.
"""
import csv, glob, os, re, sys

REG   = 'deliverables/_control/master-register.csv'
MATRIX = 'deliverables/_control/ownership-matrix.md'
DOCS = {'Manual': 'deliverables/technical-manual/*.md',
        'SOP':    'deliverables/sop/*.md',
        'Field':  'deliverables/field-how-to/*.md',
        'Office': 'deliverables/office-how-to/*.md'}
ORDER = ['Manual', 'SOP', 'Field', 'Office']

def body(doc):
    """Every authored file of a document — not the assembled copy or the README."""
    for f in sorted(glob.glob(DOCS[doc])):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        yield f, open(f).read()

# ---- where is each register item actually raised? -------------------------
ids = {r['id'] for r in csv.DictReader(open(REG))}
raised = {i: set() for i in ids}
for doc in DOCS:
    for f, s in body(doc):
        for m in re.finditer(r'\b([DV]-\d+|T\d{1,2})\b', s):
            if m.group(1) in raised: raised[m.group(1)].add(doc)

# ---- which documents reference each Manual section? -----------------------
refs = {}                                   # manual section -> set of documents
for doc in DOCS:
    if doc == 'Manual': continue
    for f, s in body(doc):
        for m in re.finditer(r'Technical Manual\s+§(\d+(?:\.\d+)?)((?:,\s*§\d+(?:\.\d+)?)*)', s):
            for t in [m.group(1)] + re.findall(r'§(\d+(?:\.\d+)?)', m.group(2) or ''):
                refs.setdefault(t.split('.')[0], set()).add(doc)

check = '--check' in sys.argv
drift = 0

# ---- register ------------------------------------------------------------
rows = list(csv.DictReader(open(REG)))
fields = list(rows[0].keys())
for r in rows:
    now = '; '.join(d for d in ORDER if d in raised[r['id']]) or '—'
    if r['affected_documents'].strip() != now:
        drift += 1
        if check: print(f'  register {r["id"]:5} was "{r["affected_documents"]}" -> "{now}"')
        else: r['affected_documents'] = now
if not check:
    with open(REG, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

# ---- ownership matrix ----------------------------------------------------
txt = open(MATRIX).read()
out, changed = [], 0
for line in txt.split('\n'):
    m = re.match(r'^\| (.*?) \| (.*?) \| (●|ref|—) \| (●|ref|—) \| (●|ref|—) \| (●|ref|—) \|$', line)
    if not m:
        out.append(line); continue
    topic, owner = m.group(1), m.group(2)
    cells = dict(zip(ORDER, m.group(3, 4, 5, 6)))
    sec = re.search(r'Manual\s+§(\d+)', owner)
    if sec:
        seen = refs.get(sec.group(1), set())
        for d in ORDER:
            if cells[d] == '●': continue
            cells[d] = 'ref' if d in seen else '—'
    new = f'| {topic} | {owner} | ' + ' | '.join(cells[d] for d in ORDER) + ' |'
    if new != line:
        changed += 1
        if check: print(f'  matrix   {topic[:56]}')
    out.append(new)
if not check:
    open(MATRIX, 'w').write('\n'.join(out))

print(f'register rows re-derived: {drift}')
print(f'matrix rows re-derived:   {changed}')
if check and (drift or changed): sys.exit(1)
