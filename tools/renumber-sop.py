#!/usr/bin/env python3
"""Shift SOP sections N..21 up by one to make room for a new section, and repair
   every reference to them in all four documents.

    python3 tools/renumber-sop.py <first-section-to-shift>

Only SOP-internal references and explicit "SOP §n" references elsewhere are
touched. Technical Manual references are left alone.
"""
import re, glob, os, sys, shutil

FIRST = int(sys.argv[1])
SOP = 'deliverables/sop'
files = sorted(glob.glob(f'{SOP}/[0-2][0-9]-*.md'))

# old -> new for the sections being shifted, highest first so renames don't collide
shift = {n: n+1 for n in range(FIRST, 22)}

# 1. rename the files
for n in sorted(shift, reverse=True):
    for f in files:
        b = os.path.basename(f)
        if b.startswith(f'{n:02d}-'):
            new = f'{SOP}/{shift[n]:02d}-' + b.split('-', 1)[1]
            shutil.move(f, new); print(f'  {b} -> {os.path.basename(new)}')

# 2. renumber headings inside the shifted files
for n in sorted(shift, reverse=True):
    for f in sorted(glob.glob(f'{SOP}/{shift[n]:02d}-*.md')):
        s = open(f).read()
        s = re.sub(rf'^# {n}\. ', f'# {shift[n]}. ', s, flags=re.M)
        s = re.sub(rf'^(#+) {n}\.(\d+) ', lambda m: f'{m.group(1)} {shift[n]}.{m.group(2)} ', s, flags=re.M)
        open(f, 'w').write(s)

# 3. repair references, in every document
def remap(txt, sop_context):
    def sub(m):
        pre, num = m.group(1) or '', m.group(2)
        head = int(num.split('.')[0])
        if head in shift:
            num = str(shift[head]) + (('.' + num.split('.')[1]) if '.' in num else '')
        return f'{pre}§{num}'
    # explicit "SOP §n" anywhere
    txt = re.sub(r'(SOP\s+)§(\d+(?:\.\d+)?)', sub, txt)
    if sop_context:
        # bare §n inside the SOP, but never one introduced by "Technical Manual"
        out, i = [], 0
        for m in re.finditer(r'§(\d+(?:\.\d+)?)', txt):
            out.append(txt[i:m.start()])
            ctx = txt[max(0, m.start()-70):m.start()]
            out.append(m.group(0) if 'Technical Manual' in ctx or 'SOP ' in ctx[-6:]
                       else sub(re.match(r'()§(\d+(?:\.\d+)?)', m.group(0))))
            i = m.end()
        out.append(txt[i:]); txt = ''.join(out)
    return txt

n = 0
for doc in ('sop', 'technical-manual', 'office-how-to', 'field-how-to'):
    for f in sorted(glob.glob(f'deliverables/{doc}/*.md')):
        b = os.path.basename(f)
        if b.startswith('MX60-'): continue
        s = open(f).read()
        t = remap(s, doc == 'sop')
        if t != s: open(f, 'w').write(t); n += 1
print(f'{n} files had references repaired')
