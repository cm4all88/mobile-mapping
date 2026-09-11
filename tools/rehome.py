#!/usr/bin/env python3
"""Re-home a section from the single-document draft into the Technical Manual.

Rule, applied mechanically so nothing is lost by accident:
  KEEP   TRIMBLE DOCUMENTED METHOD, OBSERVED SOFTWARE BEHAVIOR,
         FIELD TESTING REQUIRED, VENDOR CLARIFICATION REQUIRED,
         CAUTION, IMPORTANT, FIELD TIP, WHY THIS MATTERS, ADVANCED,
         IN PLAIN ENGLISH, and all body text, tables and citations.
  MOVE   PARAMETRIX PROCEDURE (PROPOSED)  -> SOP. Replaced by a pointer.
  REDUCE PARAMETRIX DECISION REQUIRED     -> named, one line, pointing at the SOP.

Trimble's documented procedures stay: they are evidence of what the software does,
which is what the Manual is for. Parametrix's operational steps are not here --
they belong in the How To guides.
"""
import re, sys

def blocks(md):
    """Yield ('quote'|'text', lines) preserving order."""
    out, buf, inq = [], [], False
    for ln in md.split('\n'):
        q = ln.strip().startswith('>')
        if q != inq:
            if buf: out.append(('quote' if inq else 'text', buf))
            buf, inq = [], q
        buf.append(ln)
    if buf: out.append(('quote' if inq else 'text', buf))
    return out

def label(qlines):
    first = re.sub(r'[>*_]', '', qlines[0]).strip().upper()
    for name in ('PARAMETRIX PROCEDURE (PROPOSED)', 'PARAMETRIX PROCEDURE (ADOPTED)',
                 'PARAMETRIX DECISION REQUIRED'):
        if first.startswith(name): return name
    return None

def ids(qlines):
    return sorted(set(re.findall(r'\bD-\d+\b', '\n'.join(qlines))))

def transform(md, sop_ref):
    out = []
    for kind, lines in blocks(md):
        if kind == 'text':
            out.extend(lines); continue
        lab = label(lines)
        if lab == 'PARAMETRIX PROCEDURE (PROPOSED)':
            d = ids(lines)
            tag = f" ({', '.join(d)})" if d else ''
            out.append(f'> **This manual states no Parametrix procedure.** A practice covering '
                       f'this is proposed in the **SOP{sop_ref}**{tag}; it is not decided here.')
        elif lab == 'PARAMETRIX DECISION REQUIRED':
            d = ids(lines)
            # keep the question line so the reader knows what is open
            qline = ''
            for ln in lines[1:]:
                t = re.sub(r'^>\s?', '', ln).strip()
                if t.startswith('**') and t.endswith('**') and len(t) > 8:
                    qline = t.strip('*'); break
            tag = ', '.join(d) if d else 'a Parametrix decision'
            out.append(f'> **Open Parametrix decision — {tag}.** '
                       + (f'*{qline}* ' if qline else '')
                       + f'Stated and tracked in the **SOP{sop_ref}**; see also the master register.')
        else:
            out.extend(lines)
    txt = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', txt)

if __name__ == '__main__':
    src, dst, newnum, newtitle, sopref = sys.argv[1:6]
    md = open(src).read()
    md = transform(md, sopref)
    md = re.sub(r'^# \d+\.\s*.*$', f'# {newnum}. {newtitle}', md, count=1, flags=re.M)
    open(dst, 'w').write(md)
    print(f'  {src.split("/")[-1]:52} -> M§{newnum} {newtitle}')
