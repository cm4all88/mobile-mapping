#!/usr/bin/env python3
"""Check that procedural-force language carries an authority label.

The rule (deliverables/_control/authority-model.md): `shall` and `shall not` are
reserved for the three authorities that bind now — TRIMBLE REQUIREMENT, EQUIPMENT
LIMIT, and PARAMETRIX REQUIREMENT (ADOPTED). A proposed Parametrix practice uses
`should`.

    python3 tools/check-authority.py [-v]

-v also prints the classification of every labelled block, which is what the
authority audit reports.
"""
import re, glob, os, sys, collections

BINDING = ('TRIMBLE REQUIREMENT', 'EQUIPMENT LIMIT', 'PARAMETRIX REQUIREMENT (ADOPTED)')
PROPOSED = ('TRIMBLE DOCUMENTED METHOD', 'CAUTION', 'PARAMETRIX PROCEDURE (PROPOSED)',
            'PARAMETRIX DECISION REQUIRED', 'TESTING REQUIRED', 'FIELD TESTING REQUIRED',
            'VENDOR CLARIFICATION REQUIRED')
ALL = BINDING + PROPOSED
DIRS = {'Manual':'technical-manual','SOP':'sop','Office':'office-how-to','Field':'field-how-to'}

def blocks(md):
    """Yield (label or None, first line number, text) for each quote block, plus
       the running label context for plain text."""
    lines = md.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('>'):
            start, buf = i, []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(re.sub(r'^>\s?', '', lines[i])); i += 1
            first = re.sub(r'[*_\s]', ' ', buf[0]).strip().upper()
            lab = next((t for t in sorted(ALL, key=len, reverse=True) if first.startswith(t)), None)
            yield lab, start+1, '\n'.join(buf)
        else:
            yield None, i+1, lines[i]; i += 1

verbose = '-v' in sys.argv
counts = collections.Counter()
bad = []
for doc, dirn in DIRS.items():
    for f in sorted(glob.glob(f'deliverables/{dirn}/*.md')):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        md = open(f).read()
        if b == '03-definitions.md': continue           # defines the vocabulary
        for lab, ln, text in blocks(md):
            if lab: counts[(doc, lab)] += 1
            if not re.search(r'\bshall(\s+not)?\b', text): continue
            # a heading is not a clause, and neither is a line describing what the document does
            if text.lstrip().startswith('#'): continue
            if re.search(r'departure from a|\*should\* becomes|says \*the|clause in this procedure|'
                         r'This section states what|What shall be done, not how', text):
                continue
            if lab in BINDING: continue
            bad.append((doc, b, ln, lab or '(no label)', text.strip().split('\n')[0][:88]))

if verbose:
    print('Labelled blocks by document and authority\n')
    docs = sorted({d for d, _ in counts})
    labs = sorted({l for _, l in counts})
    print(f'  {"label":34}' + ''.join(f'{d:>9}' for d in docs))
    for l in labs:
        print(f'  {l:34}' + ''.join(f'{counts[(d,l)]:9}' for d in docs))
    print()

for d, b, ln, lab, t in bad:
    print(f'  {d:7} {b[:34]:36}{ln:5} shall under {lab}')
    print(f'          {t}')
print(f'{len(bad)} shall clauses without a binding authority' if bad
      else 'every shall rests on a binding authority')
sys.exit(1 if bad else 0)
