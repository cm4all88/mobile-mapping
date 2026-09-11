#!/usr/bin/env python3
"""Run every consistency check across the four documents. Exit 1 on any failure.

    python3 tools/check-all.py

  1  registered warnings appear verbatim in their owner, and wherever the register says
  2  no forbidden workflow stage-name synonyms
  3  the derived control artefacts match the documents
  3b every `shall` rests on an authority that binds now
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
run('circulation blocks',     ['tools/sync-circulation.py', '--check'])
run('subsection numbering',   ['tools/number-subsections.py', '--check'])
run('binding requirements',   ['tools/build-binding-table.py', '--check'])
run('style and build',        ['tools/check-style.py'])
run('authority of shall',     ['tools/check-authority.py'])

DIRS = {'Manual':'technical-manual','SOP':'sop','Office':'office-how-to','Field':'field-how-to'}
def heads(d):
    s,u = set(),set()
    for f in sorted(glob.glob(f'deliverables/{DIRS[d]}/[0-3][0-9]-*.md')):
        for l in open(f):
            m = re.match(r'^# (\d+)\.', l)
            if m: s.add(m.group(1))
            m = re.match(r'^#{2,3} (\d+\.\d+) ', l)
            if m: u.add(m.group(1))
    return s,u
P = {d: heads(d) for d in DIRS}
bad = 0
for d in DIRS:
    for f in sorted(glob.glob(f'deliverables/{DIRS[d]}/*.md')):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md': continue
        # scan paragraph-wise: a reference and its "Technical Manual" prefix are
        # routinely split by a soft line break, and a line-wise scan misreads those
        raw = open(f).read()
        for para in re.split(r'\n\s*\n', raw):
            line0 = raw[:raw.index(para)].count('\n') + 1 if para in raw else 0
            flat = re.sub(r'\s+', ' ', re.sub(r'^>\s?', '', para, flags=re.M))
            for m in re.finditer(r'§(\d+(?:\.\d+)?)', flat):
                pre = flat[max(0, m.start()-70):m.start()]
                # a table cell or a new sentence starts a fresh context: an earlier
                # "Technical Manual" in the same paragraph does not own this reference
                pre = re.split(r'\|| \u00b7 |(?<=[a-z0-9)])\. ', pre)[-1]
                # a section of a Trimble document is not a reference into this set
                if re.search(r'QSG|User Guide|UG Rev|TBC|TMI|Brand Guide|Spec ?Sheet', pre): continue
                pool = P['Manual'] if 'Technical Manual' in pre else (P['SOP'] if 'SOP' in pre else P[d])
                t = m.group(1)
                if t not in (pool[1] if '.' in t else pool[0]):
                    print(f'      {d} {b} ~line {line0}: §{t}  |  {flat[max(0,m.start()-60):m.start()+10]}'); bad += 1
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
