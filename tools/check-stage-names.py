#!/usr/bin/env python3
"""Flag forbidden stage-name synonyms across the four documents.

    python3 tools/check-stage-names.py [--coverage]

The forbidden terms are DERIVED from the Never column of
`deliverables/_control/workflow-stage-names.md`, which is the authority. They are
not restated here, because a second copy of a frozen list is a list that drifts —
and it had. Before 2026-09-19 this script carried its own hand-written copy
covering 18 of the table's 47 terms while reporting "no forbidden stage-name
synonyms", which reads as a clean bill of health rather than a partial check.

Two classes of term are deliberately not enforced, and both are named explicitly
below rather than silently dropped:

  ORDINARY   Words that are ordinary English outside their stage sense — setup,
             capture, survey, review, storage, import. Enforcing them would bury
             a real hit under false ones. The stage-names file makes the same
             point: the Never column forbids a word *as the name of the stage*,
             not the word itself.

  QUOTED     Source text reproduced as written. A Trimble quotation is not ours
             to reword. Quotations here often wrap across several lines, so the
             exemption tracks quote state across the block instead of looking for
             a quote character on each line — the bug that let a forbidden term
             sit inside a wrapped quotation in Technical Manual 11 unreported.
"""
import re, glob, os, sys

AUTHORITY = 'deliverables/_control/workflow-stage-names.md'

# Ordinary English outside its stage sense. Each is in the Never column and each
# is deliberately not enforced; the reason is the same for all of them.
ORDINARY = {
    'mobilisation', 'setup', 'capture', 'survey', 'the drive', 'import', 'receipt',
    'extraction', 'cal', 'adjustment', 'review', 'output', 'storage', 'retention',
    'filing', 'quality check', 'download', 'lineage', 'audit trail', 'field checks',
    'ingest', 'final check',
}


def forbidden_terms():
    """Read the Never column out of the authority. -> {term: frozen stage name}"""
    out = {}
    for line in open(AUTHORITY, encoding='utf-8'):
        m = re.match(r'^\|\s*\d+\s*\|\s*\*\*([^*]+)\*\*[^|]*\|[^|]*\|([^|]*)\|', line)
        if not m:
            continue
        stage = m.group(1).strip()
        for term in re.split(r'[,;]', m.group(2)):
            term = re.sub(r'\*|\(.*?\)|—.*$', '', term).strip()
            if term and term != '—':
                out[term.lower()] = stage
    return out


def quoted_lines(path):
    """Line numbers inside a quotation, tracking state across wrapped lines."""
    inside, marked = False, set()
    for i, line in enumerate(open(path, encoding='utf-8'), 1):
        opens = line.count('"') + line.count('“')
        closes = line.count('"') + line.count('”')
        if inside:
            marked.add(i)
        if line.count('"') % 2 or (opens and not closes):
            inside = not inside
            marked.add(i)
        elif opens or closes:
            marked.add(i)
        if line.strip() == '':
            inside = False
    return marked


DOCS = {'Manual': 'deliverables/technical-manual/*.md', 'SOP': 'deliverables/sop/*.md',
        'Office': 'deliverables/office-how-to/*.md', 'Field': 'deliverables/field-how-to/*.md'}

terms = forbidden_terms()
enforced = {t: s for t, s in terms.items() if t not in ORDINARY}

if '--coverage' in sys.argv:
    print(f'{len(terms)} forbidden terms in {AUTHORITY}')
    print(f'{len(enforced)} enforced, {len(terms) - len(enforced)} exempt as ordinary English\n')
    for t, s in sorted(terms.items()):
        print(f'  {"enforced" if t in enforced else "exempt  "}  {t:24} -> {s}')
    sys.exit(0)

bad = 0
for doc, pat in DOCS.items():
    for f in sorted(glob.glob(pat)):
        b = os.path.basename(f)
        if b.startswith('MX60-') or b == 'README.md':
            continue
        skip = quoted_lines(f)
        for i, l in enumerate(open(f, encoding='utf-8'), 1):
            if i in skip:
                continue
            for w, good in enforced.items():
                if re.search(r'\b' + re.escape(w) + r'\b', l, re.I):
                    print(f'  {doc:7} {b[:36]:38}{i:5}  "{w}" -> {good}')
                    print(f'          {l.strip()[:100]}')
                    bad += 1

print(f'{bad} forbidden stage-name synonyms' if bad
      else f'no forbidden stage-name synonyms ({len(enforced)} terms enforced, '
           f'{len(terms) - len(enforced)} exempt as ordinary English)')
sys.exit(1 if bad else 0)
