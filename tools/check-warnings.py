#!/usr/bin/env python3
"""Verify the warning register and the documents agree, in both directions.

Forward:  every registered warning appears verbatim in the document that owns it.
Reverse:  every W- identifier cited anywhere in the four documents exists in the
          register. Without this a typo -- W-99 for W-09 -- reads as a real
          warning, cites an authority that does not exist, and passes silently.
          The D-/T-/V- gate has checked both directions from the start; warnings
          are the highest-severity content in the set and were checked one way
          until 2026-09-19.

The warning register (deliverables/_control/warning-register.md) holds the authoritative
wording. A warning is quoted, never paraphrased. This checks the owner document for each
one, and reports the documents that are listed under "Quoted in" but do not exist yet.

Exit code 1 if an owned warning is missing or altered.

    python3 tools/check-warnings.py
"""
import re, os, sys, glob

REG = 'deliverables/_control/warning-register.md'
DOCS = {'Technical Manual': 'deliverables/technical-manual',
        'SOP': 'deliverables/sop',
        'Field How To': 'deliverables/field-how-to',
        'Office How To': 'deliverables/office-how-to'}

def norm(t):
    """Compare on words alone: line wrapping is not part of the wording."""
    return re.sub(r'\s+', ' ', re.sub(r'^>\s?', '', t, flags=re.M)).strip()

def corpus(path):
    if not os.path.isdir(path): return None
    out = []
    for f in sorted(glob.glob(os.path.join(path, '*.md'))):
        if os.path.basename(f).startswith('MX60-'): continue   # the assembled copy
        out.append(open(f).read())
    return norm('\n'.join(out))

reg = open(REG).read()
entries = re.split(r'\n### (W-\d+) · ', reg)[1:]
pairs = list(zip(entries[0::2], entries[1::2]))

cache = {k: corpus(v) for k, v in DOCS.items()}
missing, pending = [], []

for wid, body in pairs:
    title = body.split('\n', 1)[0].strip()
    m = re.search(r'\*\*Owner:\*\*\s*([^·\n]+)', body)
    owner = m.group(1).strip() if m else ''
    owner_doc = next((d for d in DOCS if owner.startswith(d)), None)
    m = re.search(r'\*\*Quoted in:\*\*\s*([^\n]+)', body)
    quoted = m.group(1).strip() if m else ''

    # the quoted block: from the first '> **CAUTION**' / '> **IMPORTANT**' to the blank line
    qb = re.search(r'((?:^>.*\n)+)', body, re.M)
    text = norm(qb.group(1)) if qb else ''
    # the distinctive sentence: the first bolded full line inside the block
    key = re.search(r'\*\*([^*]{25,})\*\*', text)
    key = key.group(1).strip() if key else text[:80]

    if owner_doc is None:
        missing.append((wid, title, f'owner "{owner}" is not one of the four documents'))
        continue
    hay = cache.get(owner_doc)
    if hay is None:
        pending.append((wid, title, f'{owner_doc} not built yet'))
        continue
    if key not in hay:
        missing.append((wid, title, f'not found verbatim in {owner_doc}: "{key[:60]}…"'))

    for d in DOCS:
        if d in quoted and cache.get(d) is None:
            pending.append((wid, title, f'quoted in {d}, which is not built yet'))

# ---- reverse: every W- cited in a document must exist in the register ---------
known = {wid for wid, _ in pairs}
unknown = []
for d, path in DOCS.items():
    if not os.path.isdir(path):
        continue
    for f in sorted(glob.glob(os.path.join(path, '*.md'))):
        if os.path.basename(f).startswith('MX60-'):
            continue
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            for m in re.finditer(r'\bW-\d+\b', line):
                if m.group(0) not in known:
                    unknown.append((m.group(0), os.path.basename(f), i, line.strip()[:70]))

print(f'{len(pairs)} warnings in the register')
for wid, title, why in pending:
    print(f'  pending  {wid} · {why}')
for wid, title, why in missing:
    print(f'  MISSING  {wid} {title}\n           {why}')
print(f'\n{len(pairs) - len(missing)} verified in their owner document, '
      f'{len(missing)} missing, {len(pending)} pending a document not yet built')
for wid, f, i, line in unknown:
    print(f'  UNKNOWN  {wid} cited in {f}:{i} but not in the register\n           {line}')
if unknown:
    print(f'{len(unknown)} citations of a warning identifier that does not exist')
sys.exit(1 if (missing or unknown) else 0)
