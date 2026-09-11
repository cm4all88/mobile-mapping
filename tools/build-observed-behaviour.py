#!/usr/bin/env python3
"""Generate the Technical Manual's Appendix D from the OBSERVED SOFTWARE BEHAVIOR blocks.

Appendix D is a VIEW. It is generated, never edited by hand: editing it would create a
second place where the same statement could drift. Change the section, re-run this.

    python3 tools/build-observed-behaviour.py
"""
import re, glob, os, datetime

SRC = 'deliverables/technical-manual'
OUT = os.path.join(SRC, 'appendix-D-observed-software-behaviour.md')

def sections():
    for f in sorted(glob.glob(os.path.join(SRC, '[0-3][0-9]-*.md'))):
        yield f, open(f).read()

def blocks(md):
    """Yield (heading_at_the_time, block_lines) for every quote block."""
    head = sub = None
    buf, inq = [], False
    for ln in md.split('\n'):
        m = re.match(r'^# (\d+)\. (.*)', ln)
        if m: head = (m.group(1), m.group(2)); sub = None
        m = re.match(r'^## (\d+\.\d+) (.*)', ln)
        if m: sub = (m.group(1), m.group(2))
        q = ln.strip().startswith('>')
        if q:
            buf.append(ln); inq = True
        else:
            if inq: yield head, sub, buf
            buf, inq = [], False
    if inq: yield head, sub, buf

def clean(lines):
    out = [re.sub(r'^>\s?', '', l).rstrip() for l in lines]
    while out and not out[0].strip(): out.pop(0)
    while out and not out[-1].strip(): out.pop()
    return out

rows = []
for f, md in sections():
    for head, sub, b in blocks(md):
        first = re.sub(r'[>*_\s]', '', b[0]).upper()
        if not first.startswith('OBSERVEDSOFTWAREBEHAVIOR'): continue
        body = clean(b[1:])
        ref = f'§{sub[0]}' if sub else (f'§{head[0]}' if head else '?')
        title = sub[1] if sub else (head[1] if head else '')
        rows.append((ref, title, '\n'.join(body)))

hdr = f"""# Appendix D — Observed Software Behaviour

**Generated view — do not edit by hand.** Produced by `tools/build-observed-behaviour.py` from the
**OBSERVED SOFTWARE BEHAVIOR** blocks in the body of this manual. Edit the section; regenerate
this.

An entry here is something seen in the software, or stated in a release note, that Trimble does
**not** document as procedure. It is weaker evidence than a **TRIMBLE DOCUMENTED PROCEDURE** block
and stronger than an inference. Where behaviour of this kind carries a real consequence, it also
appears in the warning register.

**{len(rows)} entries.** Last generated {datetime.date.today().isoformat()}.

---

"""
body = []
for ref, title, txt in rows:
    body.append(f'### {ref} · {title}\n\n{txt}\n')
open(OUT, 'w').write(hdr + '\n'.join(body))
print(f'{OUT}: {len(rows)} entries')
