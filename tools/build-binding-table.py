#!/usr/bin/env python3
"""Derive the externally binding requirements table and count, from one register.

deliverables/_control/binding-requirements.csv is the record: for each
requirement, its authority type, the exact source, the SOP clause, whether
anything enforces it, and any qualification. SOP §2.4's table and every count of
"externally binding requirements" in the set are generated from it, so the number
cannot drift from the evidence behind it.

    python3 tools/build-binding-table.py [--check]
"""
import csv, re, sys

REG = 'deliverables/_control/binding-requirements.csv'
rows = list(csv.DictReader(open(REG)))
N = len(rows)
BY = {}
for r in rows: BY.setdefault(r['authority'], []).append(r)

def esc(s):
    return s.replace('|', '\\|')

def table():
    out = ['| # | Requirement | Authority | Source | SOP | Enforced by |',
           '|---|---|---|---|---|---|']
    for i, r in enumerate(rows, 1):
        cl = ', '.join('§' + c.strip() for c in r['sop_clause'].split(';'))
        out.append(f"| **{i}** | {esc(r['requirement'])} | {esc(r['authority'])} | "
                   f"{esc(r['source'])} | {cl} | {esc(r['enforced'])} |")
    out.append('')
    q = [r for r in rows if r['qualification'].strip()]
    if q:
        out += [f'**Qualifications.** {N - len(q)} of the {N} carry none. These do.', '',
                '| # | |', '|---|---|']
        for i, r in enumerate(rows, 1):
            if r['qualification'].strip():
                out.append(f"| **{i}** | {esc(r['qualification'])} |")
    return '\n'.join(out)

BLOCKS = {
    'binding-count': f'**{N}**',
    'binding-table': table(),
    'binding-enforced': (
        '> **' + str(sum(1 for r in rows if not r['enforced'].lower().startswith(('software', 'hardware'))))
        + f' of the {N} are enforced by nothing.** Software or hardware stops you breaking '
        + str(sum(1 for r in rows if r['enforced'].lower().startswith(('software', 'hardware'))))
        + ' of these. The rest are true whether or not anyone notices, which is the harder kind.'),
    'binding-summary': (
        f"| **Parametrix-originated requirements adopted** | **0** |\n"
        f"| **Externally binding requirements restated here** | **{N}** — "
        + ' · '.join(f"{len(v)} {k.lower()}" for k, v in BY.items()) + ' |'),
}

check = '--check' in sys.argv
FILES = ['deliverables/sop/02-document-control.md', 'deliverables/sop/00-front-matter.md',
         'deliverables/_control/authority-model.md']
drift = []
for p in FILES:
    s = open(p).read(); out = s
    for name, body in BLOCKS.items():
        pat = re.compile(rf'(<!-- derived:{name} -->\n)(?:.*\n)*?(<!-- /derived -->)')
        if pat.search(out):
            out = pat.sub(lambda m: m.group(1) + body + '\n' + m.group(2), out)
    if out != s:
        drift.append(p)
        if not check: open(p, 'w').write(out)

for d in drift: print(f'  {d}')
print(f'binding requirements: {N} ({"stale in " + str(len(drift)) if drift else "in sync"})')
sys.exit(1 if (check and drift) else 0)
