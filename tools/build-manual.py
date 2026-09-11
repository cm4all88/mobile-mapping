#!/usr/bin/env python3
"""Assemble the Technical Manual into one document, with part dividers."""
import glob, os, re

SRC = 'deliverables/technical-manual'
OUT = os.path.join(SRC, 'MX60-TECHNICAL-MANUAL.md')

PARTS = {1: ('Part I', 'Principles'), 7: ('Part II', 'The System'),
         13: ('Part III', 'Acquisition, Explained'), 17: ('Part IV', 'Processing, Explained')}

def divider(label, title):
    return f'\n---\n\n# {label} — {title}\n\n---\n'

chunks = [open(os.path.join(SRC, '00-front-matter.md')).read().rstrip()]
for f in sorted(glob.glob(os.path.join(SRC, '[0-3][0-9]-*.md'))):
    n = int(os.path.basename(f)[:2])
    if n == 0: continue
    if n in PARTS: chunks.append(divider(*PARTS[n]))
    chunks.append(open(f).read().rstrip())
chunks.append(divider('Part V', 'Evidence'))
for f in sorted(glob.glob(os.path.join(SRC, 'appendix-*.md'))):
    chunks.append(open(f).read().rstrip())

doc = '\n\n---\n\n'.join(chunks)
doc = re.sub(r'\n{4,}', '\n\n\n', doc)
open(OUT, 'w').write(doc + '\n')
print(f'{OUT}: {len(doc.split()):,} words, {doc.count(chr(10)):,} lines')
