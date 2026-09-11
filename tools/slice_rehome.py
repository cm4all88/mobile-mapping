#!/usr/bin/env python3
"""Slice named subsections out of a SOP file, re-home them, renumber.

  slice_rehome.py --out <file> --title "N. Title" --sop <sopref>
                  --take <sopfile>:<start>-<end> [--take ...]
                  --map <old>=<new> [...]

<start>/<end> are '## X.Y' subsection numbers; end is exclusive, '$' = to EOF.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rehome import transform

args = sys.argv[1:]
out = title = sopref = None
takes, maps = [], []
i = 0
while i < len(args):
    a = args[i]
    if a == '--out': out = args[i+1]; i += 2
    elif a == '--title': title = args[i+1]; i += 2
    elif a == '--sop': sopref = args[i+1]; i += 2
    elif a == '--take': takes.append(args[i+1]); i += 2
    elif a == '--map': maps.append(args[i+1]); i += 2
    else: raise SystemExit('bad arg ' + a)

chunks = []
for t in takes:
    f, rng = t.rsplit(':', 1)
    start, end = rng.split('-')
    md = open(f).read()
    lines = md.split('\n')
    si = next(i for i, l in enumerate(lines) if l.startswith('## ' + start + ' '))
    if end == '$':
        ei = len(lines)
    else:
        ei = next(i for i, l in enumerate(lines) if l.startswith('## ' + end + ' '))
    chunks.append('\n'.join(lines[si:ei]).rstrip())

body = '\n\n'.join(chunks)
body = transform(body, sopref)
for m in maps:
    o, n = m.split('=')
    body = re.sub(r'^## ' + re.escape(o) + r' ', '## ' + n + ' ', body, flags=re.M)
open(out, 'w').write('# ' + title + '\n\n' + body.strip() + '\n')
print(f'  -> {out}  ({len(body.split())} w)')
