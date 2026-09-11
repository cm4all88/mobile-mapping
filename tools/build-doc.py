#!/usr/bin/env python3
"""Assemble one of the four documents into a single markdown file.

    python3 tools/build-doc.py manual|sop|field|office
"""
import glob, os, re, sys

def strip_markers(s):
    """The circulation markers steer tools/sync-circulation.py. They are not content."""
    return re.sub(r'^<!-- /?circulation.*?-->\n?', '', s, flags=re.M)

DOCS = {
 'manual': ('deliverables/technical-manual', 'MX60-TECHNICAL-MANUAL.md',
            {1: ('Part I', 'Principles'), 7: ('Part II', 'The System'),
             13: ('Part III', 'Acquisition, Explained'), 17: ('Part IV', 'Processing, Explained')},
            ('Part V', 'Evidence')),
 'sop':    ('deliverables/sop', 'MX60-SOP.md',
            {1: ('Part I', 'The Procedure and Who Runs It'),
             6: ('Part II', 'Before and During Collection'),
             11: ('Part III', 'Office and Delivery'),
             20: ('Part IV', 'Records, Retention and Departure')},
            ('Appendices', 'Decisions, Records and Approval')),
 'field':  ('deliverables/field-how-to', 'MX60-FIELD-HOW-TO.md', {}, ('Appendices', '')),
 'office': ('deliverables/office-how-to', 'MX60-OFFICE-HOW-TO.md', {}, ('Appendices', '')),
}
KEY = sys.argv[1] if len(sys.argv) > 1 else 'manual'
SRC, OUTNAME, PARTS, LASTPART = DOCS[KEY]
OUT = os.path.join(SRC, OUTNAME)

def divider(label, title):
    return f'\n---\n\n# {label} — {title}\n\n---\n'

chunks = [strip_markers(open(os.path.join(SRC, '00-front-matter.md')).read()).rstrip()]
for f in sorted(glob.glob(os.path.join(SRC, '[0-3][0-9]-*.md'))):
    n = int(os.path.basename(f)[:2])
    if n == 0: continue
    if n in PARTS: chunks.append(divider(*PARTS[n]))
    chunks.append(strip_markers(open(f).read()).rstrip())
chunks.append(divider(*LASTPART))
for f in sorted(glob.glob(os.path.join(SRC, 'appendix-*.md'))):
    chunks.append(strip_markers(open(f).read()).rstrip())

doc = '\n\n---\n\n'.join(chunks)
doc = re.sub(r'\n{4,}', '\n\n\n', doc)
open(OUT, 'w').write(doc + '\n')
print(f'{OUT}: {len(doc.split()):,} words, {doc.count(chr(10)):,} lines')
