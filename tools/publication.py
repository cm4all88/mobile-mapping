#!/usr/bin/env python3
"""The publication layer: what the reader sees, and what stays behind the build.

The source markdown carries the project's own machinery -- authority labels,
register identifiers, decision and testing callouts, document-control sections,
circulation blocks. All of it is real and all of it stays in the repository,
where the gates check it and the registers track it.

None of it belongs in a document handed to an employee. A reader opening the
Field How To should find a Parametrix guide, not the editorial state of one.

This module is the single place that decides the difference. It is imported by
tools/build-doc-page.py and tools/build-field-sheets.py; nothing here edits a
source file.

  WHAT IS REMOVED          circulation and status blocks, document-control and
                           approval sections, the decision and open-question
                           registers, every D-/T-/V-/W- identifier, the
                           editorial state columns of requirement tables, and
                           prose about revisions, adoption or the build.

  WHAT IS KEPT, RELABELLED a statement's source of authority. "Trimble requires
                           this" and "Parametrix recommends this" are different
                           facts for a surveyor, not document control -- so the
                           distinction survives in plain words. The reader is
                           never told a recommendation is company policy.
"""
import pathlib, re

OVERRIDES = pathlib.Path(__file__).resolve().parent.parent / 'deliverables/_control/publication'

# ---------------------------------------------------------------- files ----
# Sections and appendices that exist only to describe the document's own state.
DROP_FILES = {
    'manual': {'00-front-matter',
               'appendix-C-figures',                  # a production list, not reader material
               'appendix-E-open-technical-questions',  # the open-item register
               'appendix-F-test-results'},             # empty until tests are run
    'sop':    {'00-front-matter',
               'appendix-A-decision-register',
               'appendix-C-approval-and-revision-history'},
    'field':  {'00-front-matter'},
    'office': {'00-front-matter'},
}

# Appendices are lettered, so dropping one leaves a gap. Published letters are
# reassigned in order and every "Appendix X" reference in the text follows.
APPENDIX_KEEP = {
    'manual': ['appendix-A-trimble-source-index', 'appendix-B-reference-dataset',
               'appendix-D-observed-software-behaviour', 'appendix-G-source-conflicts'],
    'sop':    ['appendix-B-records-index'],
    'field':  ['appendix-A-preflight-checklist', 'appendix-B-end-of-mission-checklist',
               'appendix-C-field-record-form', 'appendix-D-tmi-status-reference',
               'appendix-E-quick-card'],
    'office': ['appendix-A-office-processing-checklist', 'appendix-B-registration-checklist',
               'appendix-C-qc-checklist', 'appendix-D-export-and-delivery-checklist',
               'appendix-E-archive-and-cleanup-checklist', 'appendix-F-record-templates'],
}

def appendix_map(doc):
    """old letter -> published letter, for the appendices that survive."""
    out, letter = {}, ord('A')
    for fn in APPENDIX_KEEP[doc]:
        out[fn.split('-')[1]] = chr(letter); letter += 1
    return out

# --------------------------------------------------------------- labels ----
# The left-hand side is the project's authority vocabulary. The right-hand side
# is what it means to somebody using the equipment.
RELABEL = [
    ('PARAMETRIX REQUIREMENT (ADOPTED)',   'PARAMETRIX REQUIREMENT'),
    ('PARAMETRIX PROCEDURE (PROPOSED)',    'RECOMMENDED PRACTICE'),
    ('PARAMETRIX DECISION REQUIRED',       'SET BY THE PROJECT'),
    ('Open Parametrix decision —',          'Set by the project:'),
    ('Proposed at §',                       'Recommended at §'),
    ('proposed at §',                       'recommended at §'),
    ('Open Parametrix decision',            'Set by the project'),
    ('open Parametrix decision',            'set by the project'),
    ('FIELD TESTING / VENDOR CLARIFICATION REQUIRED', 'NOT ESTABLISHED'),
    ('VENDOR CLARIFICATION REQUIRED',      'NOT DOCUMENTED BY TRIMBLE'),
    ('Vendor clarification required',      'Not documented by Trimble'),
    ('FIELD TESTING REQUIRED',             'NO PUBLISHED FIGURE'),
    ('TESTING REQUIRED',                   'NO PUBLISHED FIGURE'),
    ('TRIMBLE DOCUMENTED METHOD',          'TRIMBLE METHOD'),
    ('TRIMBLE REQUIREMENT',                'TRIMBLE REQUIREMENT'),
    ('OBSERVED SOFTWARE BEHAVIOR',         'OBSERVED IN THE SOFTWARE'),
    ('PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED',
     'SCREENING METHOD — NOT VALIDATED'),
    ('EQUIPMENT LIMIT',                    'EQUIPMENT LIMIT'),
]
# the short inline forms used in the two How To guides
INLINE_MARKS = [
    (r'\[TRIMBLE METHOD\]', '[TRIMBLE METHOD]'),
    (r'\[TRIMBLE\]',        '[TRIMBLE]'),
    (r'\[EQUIPMENT\]',      '[EQUIPMENT]'),
    (r'\[PROPOSED\s*·\s*(SOP §\d+(?:\.\d+)?)[^\]]*\]', r'[\1]'),
    (r'\[PROPOSED[^\]]*\]',  '[RECOMMENDED]'),
    (r'\[TESTING · T\d+\]', '[NO PUBLISHED FIGURE]'),
    (r'\[TESTING\]',        '[NO PUBLISHED FIGURE]'),
    (r'\[DECISION · D-\d+\]', '[SET BY THE PROJECT]'),
    (r'\[DECISION\]',       '[SET BY THE PROJECT]'),
    (r'\[SOP §(\d+(?:\.\d+)?)\]', r'[SOP §\1]'),
]

ID = r'(?:[DV]-\d+|T\d{1,2}|W-\d+)'

# register metadata that rides along in a callout header
META = re.compile(r'\s*·\s*(?:P[123]|blocks (?:operation|collection|processing|'
                  r'formal acceptance|delivery[^*·|]*|one workflow branch))(?=\s*[·*|]|$)')

def strip_ids(s):
    """Remove every register identifier, and the punctuation left holding it."""
    s = META.sub('', s)
    # a labelled callout header: "**LABEL · D-43**" / "**LABEL — D-15, D-3**"
    s = re.sub(rf'\s*[·—-]\s*{ID}(?:\s*,\s*{ID})*(?=\*\*)', '', s)
    # "**CAUTION · W-08**" in a heading line, and "· W-11" anywhere
    s = re.sub(rf'\s*[·—]\s*\*\*{ID}\*\*', '', s)
    # a parenthetical or trailing reference: "(§7.2, **W-08**)" -> "(§7.2)"
    s = re.sub(rf',?\s*\*\*{ID}\*\*(?=\s*\))', '', s)
    s = re.sub(rf'\(\s*\*\*{ID}\*\*\s*\)', '', s)
    # a table cell that is only identifiers
    s = re.sub(rf'\|\s*\*\*{ID}(?:\s*[,·]\s*{ID})*\*\*\s*(?=\|)', '| ', s)
    s = re.sub(rf'\|\s*{ID}(?:\s*[,·]\s*{ID})*\s*(?=\|)', '| ', s)
    # anything left, bold or bare
    s = re.sub(rf'\*\*{ID}(?:\s*(?:,|·|and)\s*{ID})*\*\*', '', s)
    s = re.sub(rf'(?<![\w-]){ID}(?![\w-])', '', s)
    # tidy the punctuation the identifier used to be attached to
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    # collapse runs of spaces inside a line only -- the leading run is markdown
    # structure (blockquote marker, list indent) and changing it reflows the text
    s = re.sub(r'(?m)^([ \t]*(?:>[ \t]*)?(?:[-*+][ \t]+|\d+\.[ \t]+)?)(.*)$',
               lambda m: m.group(1) + re.sub(r'[ \t]{2,}', ' ', m.group(2)), s)
    s = re.sub(r'\*?\(\s*[,;·]?\s*\)\*?', '', s)
    s = re.sub(r'\s*·\s*(?=[|\n])', '', s)
    s = re.sub(r',\s*(?=\))', '', s)
    s = re.sub(r'\*\*\s*\*\*', '', s)
    s = re.sub(r'·\s*(?:·\s*)+', '· ', s)
    s = re.sub(r'\*\*([A-Z][A-Z .()]+?)\s*·\s*\*\*', r'**\1**', s)
    s = re.sub(r'\s*·\s*\*\*', '**', s)
    s = re.sub(r'\[SOP §(\d+(?:\.\d+)?)\s*·\s*PROPOSED\]', r'[SOP §\1]', s)
    s = re.sub(r'\s*·\s*PROPOSED\]', ']', s)
    s = re.sub(r'(?m)^(\s*>?\s*)[·—,]\s*$', r'\1', s)
    return s

# ------------------------------------------------------------ paragraphs ----
# Whole blocks that exist only to describe the document's editorial state. Each
# is matched on a distinctive opening so a rewrite upstream fails loudly rather
# than silently publishing the block.
# whole lines that describe how the file was produced, or the project's own
# document-control vocabulary
DROP_LINES = [
    re.compile(r'^\*\*Generated view — do not edit by hand\.\*\*.*$', re.M),
    re.compile(r'^\| Parametrix document-control vocabulary.*$', re.M),
    re.compile(r'^\*\*\d+ entries\.\*\* Last generated [\d-]+\.\s*$', re.M),
    re.compile(r'^\*\*Last generated\*\*.*$', re.M),
    re.compile(r'^.*Last generated [\d-]+\..*$', re.M),
    # the records index lists §2's document-control records; §2 is not published
    re.compile(r'^\| 2 \| Document Control and Related Documents \|.*$', re.M),
    re.compile(r'^\| Evidence revision \|.*$', re.M),
    re.compile(r'^\| Structured reference records \|.*$', re.M),
    re.compile(r'^## A5 · Analysis record\s*$', re.M),
    re.compile(r'^\| `analysis/[^`]+` \|.*$', re.M),
    re.compile(r'^\|\s*\|\s*\|\s*(?:Which supporting revisions were issued with this one|'
               r'Distribution and receipt)\s*\|.*$', re.M),
]

DROP_BLOCKS = [
    'At this revision no clause carries PARAMETRIX REQUIREMENT',
    'Parametrix-originated requirements adopted: 0',
    'shall` is reserved for the three authorities that bind now',
    'A documented method is not a requirement.',
    'This procedure does not promote Trimble',
    'A marker never softens a Trimble instruction',
    'and are not the same thing',
    'This SOP does not choose between A, B and C',
    'What this SOP requires of Parametrix today',
    'This is not primarily a copy-editing exercise',
    'Who owns this procedure, who approves a revision',
    'decision against it, with a date and an owner, in the SOP',
    'the highest-priority test in the register',
    'The source ingestion and classification that produced this SOP',
    'Decided by Parametrix, with a date and owner in Appendix',
    'analysis/STAGE-1-SOURCE-ANALYSIS.md',
    'Read the State column',
    'Records this section requires* table at the end of each section',
    'records**, across',
    'B2 · Where the state stands',
    'Records required by an **adopted** clause',
    'Every record in this index is currently',
]

def drop_state_column(md):
    """Remove the editorial "State" column from a requirement table.

    Several tables carry a column whose only content is which decision governs
    the row. With the identifiers gone the column is empty, so the column goes.
    """
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        l = lines[i]
        if (l.strip().startswith('|') and i + 1 < len(lines)
                and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip())):
            blk = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                blk.append(lines[i]); i += 1
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in blk]
            hdr = rows[0]
            kill = [j for j, h in enumerate(hdr) if h.strip('* ').lower() == 'state']
            # also drop any column left entirely blank once identifiers are gone
            width = len(hdr)
            for j in range(width):
                if j in kill: continue
                if all(len(r) > j and not r[j].strip() for r in rows[2:]) and rows[2:]:
                    kill.append(j)
            if kill and width - len(kill) >= 1:
                for r in rows:
                    for j in sorted(kill, reverse=True):
                        if len(r) > j: del r[j]
            # a table reduced to one column is a list, and sets better as one:
            # a single-column table strands rows across page breaks
            if len(rows[0]) == 1:
                head = rows[0][0].strip().strip('*')
                if out and out[-1].strip(): out.append('')
                if head and head.lower() not in ('record', 'records', 'requirement', ''):
                    out += [f'**{head}**', '']
                out += [f'- {r[0]}' for r in rows[2:] if r[0].strip()]
                out.append('')
                continue
            out += ['| ' + ' | '.join(r) + ' |' for r in rows]
            continue
        out.append(l); i += 1
    return '\n'.join(out)

def publish(doc, stem, md):
    """Return the reader-facing markdown for one source file, or None to drop it.

    A few sections are *about* the document's editorial state -- the acceptance
    criterion, the authority key, document control. Stripping identifiers out of
    those leaves holes, so each has a hand-written reader-facing version in
    deliverables/_control/publication/. The source keeps the full version.
    """
    if stem in DROP_FILES.get(doc, ()):
        return None
    ov = OVERRIDES / doc / f'{stem}.md'
    if ov.exists():
        return ov.read_text()
    md = re.sub(r'(?m)^<!-- /?(?:circulation|derived).*?-->\n?', '', md)

    # drop the editorial-state blocks, each a blockquote or a paragraph
    for key in DROP_BLOCKS:
        md = _drop_para(md, key)

    for pat in DROP_LINES:
        md = pat.sub('', md)
    md = re.sub(r'\n(?:[ \t]*\n)+(?=\|)', '\n', md)   # a deleted row must not split a table
    for old, new in RELABEL:
        if old == new:
            continue
        # a label can be wrapped across lines inside a blockquote, so match the
        # words with any run of whitespace and quote markers between them
        pat = r'[\s>]+'.join(re.escape(w) for w in old.split())
        md = re.sub(pat, new, md)
        md = re.sub(r'[\s>]+'.join(re.escape(w) for w in old.title().split()),
                    new.title(), md)
    md = strip_ids(md)
    for pat, rep in INLINE_MARKS:
        md = re.sub(pat, rep, md)

    amap = appendix_map(doc)
    # a reference to an appendix that is not published is removed, not left
    # pointing at nothing
    gone = [c for c in 'ABCDEFG' if c not in amap]
    if gone:
        g = '|'.join(gone)
        md = re.sub(rf'\s*\*?\(Appendix ({g})\)\*?', '', md)
        md = re.sub(rf'\*\*Appendix ({g})\*\*', '', md)
        md = re.sub(rf'\(Appendix ({g})[;,]\s*', '(', md)
        md = re.sub(rf',?\s*Appendix ({g})\b', '', md)
    def remap(m):
        return 'Appendix ' + amap.get(m.group(1), m.group(1))
    md = re.sub(r'\bAppendix ([A-G])\b', remap, md)
    md = re.sub(r'\s*\*?\(\s*[,;·]?\s*\)\*?', '', md)
    # sub-headings inside an appendix carry its letter: "## B1 · By section"
    md = re.sub(r'(?m)^(#{2,4} )([A-G])(\d+)\b',
                lambda m: m.group(1) + amap.get(m.group(2), m.group(2)) + m.group(3), md)

    md = re.sub(r'\|\s*\*\*PROPOSED\*\*\s*(?=\|)', '| ', md)
    md = drop_state_column(md)
    # collapse the blank lines the removals leave behind
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'(?m)^>\s*\n(?=>\s*\n)', '', md)
    md = re.sub(r'(?m)^(>\s*\n)+(?=\n|\Z)', '', md)
    md = re.sub(r'(?m)^---\n+(?=---$)', '', md)
    return md.strip() + '\n'

def _drop_para(md, key):
    """Remove the paragraph or blockquote containing `key`."""
    paras = re.split(r'\n\s*\n', md)
    return '\n\n'.join(p for p in paras if key not in p)
