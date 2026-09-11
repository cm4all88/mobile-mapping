#!/usr/bin/env python3
"""Run every consistency check across the four documents. Exit 1 on any failure.

    python3 tools/check-all.py

  1  registered warnings appear verbatim in their owner, and wherever the register says
  2  no forbidden workflow stage-name synonyms
  3  the derived control artefacts match the documents
  4  every cross-reference resolves, in all four documents
  5  every register identifier cited exists; every register item is cited somewhere
  6  the page renderer leaves no unrendered emphasis
"""
import re, glob, os, sys, csv, subprocess

fail = []
def run(name, argv):
    r = subprocess.run([sys.executable] + argv, capture_output=True, text=True)
    ok = r.returncode == 0
    print(f'{"ok  " if ok else "FAIL"}  {name}')
    if not ok:
        fail.append(name); print('      ' + '\n      '.join(r.stdout.strip().split('\n')[-8:]))

run('warnings verbatim',      ['tools/check-warnings.py'])
run('stage names',            ['tools/check-stage-names.py'])
run('control artefacts fresh',['tools/sync-control.py', '--check'])

DIRS = {'Manual':'technical-manual','SOP':'sop','Office':'office-how-to','Field':'field-how-to'}
def heads(d):
    s,u = set(),set()
    for f in sorted(glob.glob(f'deliverables/{DIRS[d]}/[0-3][0-9]-*.md')):
        for l in open(f):
            m = re.match(r'^# (\d+)\.', l)
            if m: s.add(m.group(1))
            m = re.match(r'^## (\d+\.\d+) ', l)
            if m: u.add(m.group(1))
    return s,u
P = {d: heads(d) for d in DIRS}
bad = 0
for d in DIRS:
    for f in sorted(glob.glob(f'deliverables/{DIRS[d]}/*.md')):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        for i, l in enumerate(open(f), 1):
            for m in re.finditer(r'(Technical Manual\s+|SOP\s+)?§(\d+(?:\.\d+)?)', l):
                pre = (m.group(1) or '') + l[max(0, m.start()-70):m.start()]
                pool = P['Manual'] if 'Technical Manual' in pre else (P['SOP'] if 'SOP' in pre else P[d])
                t = m.group(2)
                if t not in (pool[1] if '.' in t else pool[0]):
                    print(f'      {d} {b} line {i}: §{t}'); bad += 1
print(f'{"ok  " if not bad else "FAIL"}  cross-references resolve')
if bad: fail.append('cross-references')

reg = {r['id'] for r in csv.DictReader(open('deliverables/_control/master-register.csv'))}
cited, unknown = set(), set()
for d in DIRS:
    for f in sorted(glob.glob(f'deliverables/{DIRS[d]}/*.md')):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        s = open(f).read()
        s = re.sub(r'P/N T\d+', '', s)                       # Trimble part numbers
        for m in re.finditer(r'\b([DV]-\d+|T\d{1,2})\b', s):
            (cited if m.group(1) in reg else unknown).add(m.group(1))
miss = reg - cited
ok = not unknown and not miss
print(f'{"ok  " if ok else "FAIL"}  register identifiers ({len(cited)}/{len(reg)} cited)')
if unknown: print('      unknown:', sorted(unknown))
if miss:    print('      never cited:', sorted(miss))
if not ok:  fail.append('register identifiers')

lit = 0
for f in glob.glob('deliverables/*/[a-z]*.html'):
    h = open(f).read()
    lit += len([m for m in re.finditer(r'.{40}\*\*.{20}', h) if m.group(0).lower() != m.group(0)])
print(f'{"ok  " if not lit else "FAIL"}  rendered emphasis ({lit} unrendered)')
if lit: fail.append('rendered emphasis')

print()
print('all checks pass' if not fail else f'{len(fail)} FAILED: {", ".join(fail)}')
sys.exit(1 if fail else 0)
