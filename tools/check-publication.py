#!/usr/bin/env python3
"""Check that nothing from the build process reaches the reader.

Runs the publication layer over every source file and looks for two kinds of
failure: vocabulary that should never appear in a published document, and the
debris that stripping an identifier can leave behind.

    python3 tools/check-publication.py [-v]
"""
import glob, os, re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import publication as pub

DIRS = {'manual': 'technical-manual', 'sop': 'sop', 'field': 'field-how-to',
        'office': 'office-how-to'}

# words a reader should never have to interpret
FORBIDDEN = [
    (r'Living Draft', 'living-draft status'),
    (r'Working Version', 'working version'),
    (r'INTERNAL REVIEW', 'internal-review status'),
    (r'\bnot issued\b', 'issue status'),
    (r'\bnot adopted\b|\bno clause (?:is|has been) adopted\b|requirements adopted',
     'adoption status'),
    (r'\bPROPOSED\b|\bProposed\b', 'proposed marker'),
    (r'\badopt(?:ed|ion|s)\b', 'adoption language'),
    (r'At this revision|revision history|approves a revision|review cycle|'
     r'supporting revisions|Revision history', 'revision language'),
    (r'Last generated|Generated view|regenerate this', 'generation language'),
    (r'\bState column\b|\bthe register\b|register item', 'register language'),
    (r'\bD-\d+\b|\bV-\d+\b|\bW-\d+\b|(?<![A-Za-z])T\d{1,2}(?![\w.])', 'register identifier'),
    (r'PARAMETRIX DECISION REQUIRED|TESTING REQUIRED|VENDOR CLARIFICATION REQUIRED',
     'register callout label'),
    (r'master-register|_control/|check-all\.py|tools/[a-z-]+\.py|sync-control|build-doc', 'repository mechanics'),
    (r'\bthis (?:draft|revision)\b', 'draft language'),
    (r'controlled document|controlled copy|document control', 'document-control language'),
    (r'circulat(?:ed|ion)', 'circulation language'),
]
# debris an identifier leaves when it is removed
DEBRIS = [
    (r'·\s*·', 'doubled separator'),
    (r'\*\*[ \t]+\*\*', 'empty bold'),
    (r'\(\s*\)', 'empty parentheses'),
    (r'\|\s*\|\s*\|\s*\|\s*$', 'row of empty cells'),
    (r'(?m)^\s*[·—,]\s*$', 'orphaned separator'),
    (r'\s[,;]\s*(?=[|\n])', 'dangling punctuation'),
    (r'(?m)^#+\s*$', 'empty heading'),
    (r'VENDOR CLARIFICATION|FIELD TESTING', 'unrelabelled callout'),
    (r'§\s*(?![0-9§XnN])(?!\s*(?:\||column))', 'section mark with no number'),
]

verbose = '-v' in sys.argv
bad = []
for doc, d in DIRS.items():
    for f in sorted(glob.glob(f'deliverables/{d}/*.md')):
        stem = os.path.basename(f)[:-3]
        if stem.startswith('MX60-') or stem == 'README': continue
        out = pub.publish(doc, stem, open(f).read())
        if out is None: continue
        for pat, why in FORBIDDEN + DEBRIS:
            for m in re.finditer(pat, out):
                line = out[:m.start()].count('\n') + 1
                ctx = out.split('\n')[line - 1].strip()[:96]
                bad.append((doc, stem, line, why, ctx))

# every appendix reference in the published text must point at a published appendix
for doc, d in DIRS.items():
    have = set(pub.appendix_map(doc).values())
    for f in sorted(glob.glob(f'deliverables/{d}/*.md')):
        stem = os.path.basename(f)[:-3]
        if stem.startswith('MX60-') or stem == 'README': continue
        out = pub.publish(doc, stem, open(f).read())
        if out is None: continue
        for m in re.finditer(r'\bAppendix ([A-Z])\b', out):
            # a reference into another document of the set is that document's to resolve
            pre = out[max(0, m.start() - 90):m.start()]
            if re.search(r'Technical Manual|SOP|Field How To|Office How To', pre): continue
            if m.group(1) not in have:
                line = out[:m.start()].count('\n') + 1
                bad.append((doc, stem, line, f'reference to Appendix {m.group(1)}, which is not published',
                            out.split('\n')[line - 1].strip()[:96]))

for doc, stem, line, why, ctx in bad[:60 if not verbose else 10000]:
    print(f'  {doc:7} {stem[:38]:40}{line:5} {why}')
    print(f'          {ctx}')
print(f'{len(bad)} publication leaks' if bad else 'the published output carries nothing from the build')
sys.exit(1 if bad else 0)
