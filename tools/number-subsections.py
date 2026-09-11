#!/usr/bin/env python3
"""Number the Office How To's task steps, so every one can be pointed at.

The Office How To subdivides each numbered section into named steps — Do, Look
at, Expect, Stop if, Record. The names repeat in every section, so "Stop if" is
not an address: a reviewer cannot cite it and a cross-reference cannot resolve
to it. This numbers them §n.1, §n.2 … from the section number in the filename,
leaving the names intact.

Idempotent: a step that already carries its correct number is left alone.

    python3 tools/number-subsections.py [--check]
"""
import glob, os, re, sys

check = '--check' in sys.argv
changed = []
for f in sorted(glob.glob('deliverables/office-how-to/[0-3][0-9]-*.md')):
    if os.path.basename(f).startswith('00-'): continue   # front matter carries shared blocks
    sec = int(os.path.basename(f)[:2])
    lines = open(f).read().split('\n')
    n, out, hit = 0, [], False
    for line in lines:
        m = re.match(r'^### (?:\d+\.\d+ )?(.*)$', line)
        if m:
            n += 1
            new = f'### {sec}.{n} {m.group(1)}'
            hit |= new != line
            out.append(new)
        else:
            out.append(line)
    if hit:
        changed.append(os.path.basename(f))
        if not check: open(f, 'w').write('\n'.join(out))

for c in changed: print(f'  {c}')
print(f'office subsections: {"renumbered " + str(len(changed)) + " file(s)" if changed else "in sync"}')
sys.exit(1 if (check and changed) else 0)
