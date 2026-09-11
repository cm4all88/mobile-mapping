#!/usr/bin/env python3
"""Write the shared circulation blocks into all four front matters, from one source.

The living-draft banner, the "How to review this draft" panel and the working
revision block are the same concept in all four documents, so they are held once
in deliverables/_control/circulation/ and inserted between markers here. No copy
is hand-edited — edit the source and re-run.

    python3 tools/sync-circulation.py [--check]

--check reports drift and exits 1 without writing, for use as a gate.
"""
import sys, os, re

SRC = 'deliverables/_control/circulation'
DRAFT = '2026-09-11-a'
SUPERSEDES = '— first circulated draft'

DOCS = {
    'technical-manual': dict(doc='MX60 Mobile Mapping Technical Manual',
                             example='Manual §21.4'),
    'sop':              dict(doc='MX60 Mobile Mapping Standard Operating Procedure',
                             example='SOP §14.5'),
    'field-how-to':     dict(doc='MX60 Field How To',
                             example='Field How To §17.3'),
    'office-how-to':    dict(doc='MX60 Office How To',
                             example='Office How To §16.4'),
}
BLOCKS = ('banner', 'working-revision', 'how-to-review')

def rendered(name, v):
    s = open(f'{SRC}/{name}.md').read().rstrip('\n')
    return (s.replace('{DOC}', v['doc']).replace('{EXAMPLE}', v['example'])
             .replace('{DRAFT}', DRAFT).replace('{SUPERSEDES}', SUPERSEDES))

check = '--check' in sys.argv
drift = []
for d, v in DOCS.items():
    p = f'deliverables/{d}/00-front-matter.md'
    s = open(p).read()
    out = s
    for name in BLOCKS:
        pat = re.compile(rf'(<!-- circulation:{name} -->\n).*?(\n<!-- /circulation -->)', re.S)
        if not pat.search(out):
            drift.append(f'  {d}: marker circulation:{name} is missing'); continue
        out = pat.sub(lambda m: m.group(1) + rendered(name, v) + m.group(2), out)
    if out != s:
        drift.append(f'  {d}: circulation blocks are stale')
        if not check: open(p, 'w').write(out)

for line in drift: print(line)
print(f'circulation blocks: {"drift in " + str(len(drift)) + " place(s)" if drift else "in sync"}')
sys.exit(1 if (check and drift) else 0)
