#!/usr/bin/env python3
"""Check that every built page agrees with the style system.

Built HTML is derived, so it drifts silently when a source changes and a build is
not re-run. This catches the three ways that shows up:

  * a page whose document accent does not match the style system
  * a page built before the print layer existed
  * a page still carrying anything about how it was produced

    python3 tools/check-style.py
"""
import re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
ACCENTS = {                      # _control/style/style-system.md is the authority
    'deliverables/technical-manual/technical-manual.html': 'brand-blue',
    'deliverables/sop/sop.html':                           'brand-orange',
    'deliverables/field-how-to/field-how-to.html':         'brand-green',
    'deliverables/office-how-to/office-how-to.html':       'brand-yellow',
}
SHEETS = sorted(str(p.relative_to(REPO)) for p in
                (REPO / 'deliverables/field-how-to/sheets').glob('*.html'))
ALL = list(ACCENTS) + SHEETS
# nothing about how the document was produced may reach a built page
STALE = ('Draft A', 'Not issued', 'Living Draft', 'LIVING DRAFT', 'Working Version',
         'Internal Review', 'INTERNAL REVIEW', 'TRIMBLE DOCUMENTED PROCEDURE',
         'PARAMETRIX DECISION REQUIRED', 'not adopted', 'controlled document',
         '2026-09-11-a', '_control/')

bad = []
for rel in ALL:
    p = REPO / rel
    if not p.exists():
        bad.append(f'{rel}: not built'); continue
    h = p.read_text()
    if 'Parametrix' not in h:
        bad.append(f'{rel}: does not carry the Parametrix name')
    if '@media print' not in h:
        bad.append(f'{rel}: no print layer')
    for t in STALE:
        if t in h:
            bad.append(f'{rel}: carries stale string "{t}"')
    a = ACCENTS.get(rel)
    if a and f'--doc-accent:var(--{a})' not in h.replace(' ', ''):
        bad.append(f'{rel}: document accent is not {a}')

# the style system names the same four accents
sysdoc = (REPO / 'deliverables/_control/style/style-system.md').read_text().lower()
for rel, a in ACCENTS.items():
    word = a.split('-')[1]
    if word not in sysdoc:
        bad.append(f'style-system.md does not name the {word} accent')

for b in bad: print('  ' + b)
print(f'{len(bad)} style/build inconsistencies' if bad
      else f'{len(ALL)} built pages agree with the style system')
sys.exit(1 if bad else 0)
