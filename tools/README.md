# tools

## build-sop.js

Builds `SOP/Parametrix-MX60-Mobile-Mapping-SOP.docx` from
`SOP/MX60-SOP-COMPLETE.md`.

Converts markdown headings, tables, blockquote callouts, code blocks and lists into
Word equivalents, and adds a Parametrix cover page and a table of contents.

Callouts are styled by their leading label — CAUTION, IMPORTANT, FIELD TIP,
WHY THIS MATTERS, PARAMETRIX DECISION REQUIRED, ADVANCED — each getting a coloured
left rule and tinted background.

### Running it

```bash
npm install docx          # not preinstalled in every environment
node tools/build-sop.js
```

Re-run after any change to the markdown sections. Regenerate the assembled markdown
first if individual section files were edited.

### Note on verification

This environment has no working LibreOffice, pandoc or pdftoppm, so the output could
not be rendered and visually checked. It passes OOXML XSD validation and structural
checks (parts, relationships, content types, image references), but **open it in Word
and look at it before issuing**.


## build-checklist.py

Renders `tools/field-checklist.html` to `SOP/Parametrix-MX60-Field-Checklist.pdf` —
the four-page vehicle quick reference, a condensed form of Appendix A.

```bash
pip install playwright pypdfium2
python tools/build-checklist.py
```

Uses headless Chromium (preinstalled at `/opt/pw-browsers`) rather than LibreOffice,
which does not work in this environment. Edit the HTML to change the checklist; the
layout is plain CSS with `@page` print rules.

Output was rendered to images and visually checked — all four pages verified.


## build-sop-page.py

Builds `SOP/sop-page.html` — the browsable single-page version of the SOP, published as
an Artifact.

```bash
python tools/build-sop-page.py
```

Reads the section markdown files in the order set by `ORDER` in the script, converts
each to HTML (headings, tables, callouts, code, lists, inline emphasis, and Trimble page
citations), and injects them into `tools/sop-page-template.html` along with the sidebar
navigation and a per-section search index.

Edit the template for design changes and the markdown sections for content. Re-run after
either, then republish the artifact from the same file path to keep its URL.

**Watch the cascade.** The nav list items use `nv-sec` / `nv-app` classes specifically to
avoid colliding with the `.sec` section rule, which carries large padding and a border.
An earlier version used `sec` for both and the navigation rendered with ~195px gaps.

## Consistency checks

`tools/check-all.py` runs every cross-document check and exits non-zero on any failure.
**Run it before any issue.**

| Check | Tool |
|---|---|
| The externally binding requirements table and every count of them match the register | `build-binding-table.py --check` |
| Every built page carries the current Working Version, the Living Draft status, the print layer and its documented accent | `check-style.py` |
| Registered warnings appear **verbatim** in their owner document, and wherever the register says | `check-warnings.py` |
| No forbidden workflow stage-name synonyms | `check-stage-names.py` |
| The derived control artefacts still match the documents | `sync-control.py --check` |
| The shared circulation blocks are identical in all four front matters | `sync-circulation.py --check` |
| Every Office How To task step carries its section number | `number-subsections.py --check` |
| **No `shall` rests on anything but a binding authority** | `check-authority.py` |
| Every cross-reference resolves, in all four documents | `check-all.py` |
| Every register identifier cited exists, and every register item is raised somewhere | `check-all.py` |
| The page renderer leaves no unrendered emphasis | `check-all.py` |

`sync-control.py` without `--check` re-derives the control artefacts that *describe* the
documents — the register's `affected_documents` column, the ownership matrix's ref / — columns and
the register README's current-state table. Everything else in those files is judgement and is set
by hand.

## The living-draft circulation blocks

`sync-circulation.py` writes three blocks into all four front matters from one source in
`deliverables/_control/circulation/`:

| Block | What it is |
|---|---|
| `banner.md` | The **LIVING DRAFT — INTERNAL REVIEW** status notice |
| `how-to-review.md` | The four reviewer questions, the reviewer roles, and how to cite a section |
| `working-revision.md` | The temporary working revision block — **not** a Parametrix convention |

**No copy is hand-edited.** Edit the source and re-run, or `check-all.py` fails. The working draft
label and the circulation date are set at the top of the script.

## check-authority.py

Classifies every labelled block in all four documents and fails any `shall` that does not rest on
**TRIMBLE REQUIREMENT**, **EQUIPMENT LIMIT** or **PARAMETRIX REQUIREMENT (ADOPTED)**.

`-v` prints the classification table — the authority audit. A **TRIMBLE DOCUMENTED METHOD** is
deliberately *not* a binding authority: Trimble documenting a method is not Trimble requiring it,
and `deliverables/_control/authority-model.md` explains why that distinction is enforced.

## number-subsections.py

Numbers the Office How To's task steps — `### 16.5 Stop if` — so a reviewer can cite one. The
step names repeat in every section, so the name alone is not an address. Idempotent.


## Building the circulation package

Order matters only in that the derived artefacts come first.

```bash
python3 tools/sync-control.py            # register + ownership matrix + register README
python3 tools/sync-circulation.py        # the shared front-matter blocks
python3 tools/build-binding-table.py     # SOP §2.4 and its counts
python3 tools/build-register-views.py    # SOP Appendix A, Manual Appendix E/F, _control views
python3 tools/build-records-index.py     # SOP Appendix B
for d in manual sop office field; do
  python3 tools/build-doc.py "$d"        # assembled markdown
  python3 tools/build-doc-page.py "$d"   # the browsable page
done
python3 tools/build-field-sheets.py      # the four standalone printable sheets
python3 tools/build-index.py             # deliverables/index.html, the landing page
python3 tools/check-all.py               # the gate. Nine checks
python3 tools/build-pdfs.py              # PDFs, through the print layer
```

**The Working Version is set in one place** — `DRAFT` at the top of `sync-circulation.py`. Every
page, sheet, PDF header and footer reads it from there, and `check-style.py` fails any built page
that still carries an older one.

## build-pdfs.py

Renders the nine circulation pages to PDF through the print layer in
`tools/doc-page-template.html`, with a running header carrying the Working Version and the Living
Draft status, and `Page n of m` in the footer.

**These are not controlled PDFs**, and every page says so. They exist because some reviewers would
rather read on paper; the HTML remains the living implementation.

Uses the preinstalled Chromium at `/opt/pw-browsers`. There is no LibreOffice or pdftoppm in this
environment, so do not add a pipeline that assumes one.
