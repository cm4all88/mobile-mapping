#!/usr/bin/env python3
"""Verify the documents' equipment numbers against the register that is their authority.

    python3 tools/check-numbers.py [-v]

`reference/mx60-reference-data.csv` is declared throughout this project as the
authority for every number: the CSV row changes and the prose usually does not.
Nothing enforced that. Until 2026-09-19 a figure could be edited in the register,
or in a document, and the two would disagree silently — which is precisely the
failure the arrangement exists to prevent.

WHAT IT CHECKS

Every equipment quantity stated anywhere in the four documents must appear in the
register. That catches all three ways the two can part company:

  a number invented in prose        — not in the register
  a register value edited alone     — the prose figure is no longer in the register
  a prose figure edited alone       — the edited figure is not in the register

WHAT IT DOES NOT CHECK, AND WHY THAT IS STATED HERE

It does not require every register row to be quoted. Most rows are reference
detail no document states, and the register is wider than the documents by design.

It checks membership, not correspondence: a document figure is accepted if it
appears anywhere in the register, not if it matches the particular row it came
from. So it catches a figure that exists nowhere in the register — invented,
mistyped, or orphaned when a register edit removed the last copy — and it does
not catch a figure swapped for another value the register happens to hold.
Closing that gap would mean every document figure naming its register row, which
is a bigger change than this gate.

Verified by mutation on 2026-09-19: 4096 px -> 4098 px and 28 kg -> 29 kg are
both caught; an invented "0.4 mm precision" is caught.

Units are restricted to those that identify an equipment specification. Bare
metres and seconds are excluded: they appear constantly in ordinary prose
("within 30 m of the control point") and would bury a real disagreement.
"""
import csv, re, glob, os, sys

REG = 'reference/mx60-reference-data.csv'
DOCS = {'Manual': 'deliverables/technical-manual', 'SOP': 'deliverables/sop',
        'Field': 'deliverables/field-how-to', 'Office': 'deliverables/office-how-to'}
VERBOSE = '-v' in sys.argv

# Units that only ever denote an equipment specification. Degrees are excluded on
# purpose: the documents state angles that are equipment specs (0.0025 deg roll)
# and angles that are TBC method or interface values (a 90 deg crossing angle, a
# 0.001 deg nudge key), and only the first kind belongs to the register.
UNIT = r'(?:mm|kHz|MHz|MP|px|fps|TB|GB|kg|W)'
# A number and its unit, with at most one space. "(?![\w-])" keeps a warning
# identifier out: the W of "W-10" is not a watt.
QTY = re.compile(r'(\d[\d,]*\.?\d*)\s?(' + UNIT + r')(?![\w-])')


def pairs(text):
    return {(v.replace(',', ''), u.lower()) for v, u in QTY.findall(text)}


# Read the register through the csv module: a raw scan trips over values that sit
# immediately after a comma, which in a CSV is all of them.
known = set()
for row in csv.DictReader(open(REG, encoding='utf-8')):
    known |= pairs(' ; '.join(row.values()))
if not known:
    sys.exit(f'no quantities found in {REG} — check the file')

seen = unknown = 0
problems = []
for doc, d in DOCS.items():
    for f in sorted(glob.glob(os.path.join(d, '*.md'))):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md':
            continue
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            for v, u in QTY.findall(line):
                key = (v.replace(',', ''), u.lower())
                seen += 1
                if key in known:
                    if VERBOSE:
                        print(f'  ok  {v} {u:4} {b}:{i}')
                else:
                    unknown += 1
                    problems.append((f'{v} {u}', doc, f'{b}:{i}', line.strip()[:84]))

for q, doc, where, line in problems:
    print(f'  {q} in {doc} {where} is not in {REG}')
    print(f'     {line}')

print(f'{seen} equipment quantities in the documents, {unknown} not in the register')
sys.exit(1 if unknown else 0)
