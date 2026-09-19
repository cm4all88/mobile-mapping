# tools

Everything that builds or checks the document set. **`deliverables/` is the live set**; two builders
here serve the superseded `SOP/` directory and are marked as such, and three scripts are spent
migrations kept only as a record.

Rewritten 2026-09-19. The previous version documented six tools of the twenty-five present, led with
the superseded single-document builder, and described a `build-sop-page.py` that does not exist.

## The gate

```bash
python3 tools/check-all.py
```

Fourteen checks. Everything else in this file exists to keep them passing.

| Check | What it proves | Script |
|---|---|---|
| warnings verbatim | Every registered warning appears word for word in the document that owns it, **and** every `W-` cited anywhere exists in the register | `check-warnings.py` |
| stage names | No forbidden stage-name synonym. Terms are **derived** from `workflow-stage-names.md`, never restated | `check-stage-names.py` |
| control artefacts fresh | The derived control files still match the documents | `sync-control.py --check` |
| circulation blocks | The living-draft blocks are identical in all four documents | `sync-circulation.py --check` |
| subsection numbering | Every subsection is numbered and in sequence | `number-subsections.py --check` |
| binding requirements | SOP §2.4 and every count match `binding-requirements.csv` | `build-binding-table.py --check` |
| style and build | The style system is honoured and the pages build | `check-style.py` |
| publication layer | No build machinery leaked into a published document | `check-publication.py` |
| authority of shall | Every `shall` rests on an authority that binds now | `check-authority.py` |
| numbers match register | Every equipment quantity in the documents exists in `reference/mx60-reference-data.csv` | `check-numbers.py` |
| cross-references resolve | Every `§n` points at a section that exists | in `check-all.py` |
| register identifiers | Every `D-`/`T`/`V-` cited exists, and every register item is cited | in `check-all.py` |
| rendered emphasis | No unrendered `**` in the built pages — **and the pages are newer than their markdown**, so the check is not reading stale output | in `check-all.py` |

> **Every gate was mutation-tested on 2026-09-19**: a violation was introduced for each and the suite
> confirmed to fail. Three did not catch theirs and were fixed. A gate that has never been seen to
> fail has not been tested.

## The live pipeline

Run after editing, in this order. Most are idempotent; all are safe to re-run.

```bash
python3 tools/build-register-views.py      # master-register.csv  -> Manual App. E, SOP App. A, views
python3 tools/build-records-index.py       # section record tables -> SOP Appendix B
python3 tools/build-binding-table.py       # binding-requirements.csv -> SOP §2.4
python3 tools/sync-control.py              # re-derive the control artefacts from the documents
python3 tools/sync-circulation.py          # push the circulation blocks into all four front matters
python3 tools/number-subsections.py        # renumber subsections
python3 tools/build-doc.py manual|sop|field|office     # assemble MX60-*.md
python3 tools/build-doc-page.py manual|sop|field|office # render the browsable .html
python3 tools/build-index.py               # deliverables/README.md and the review index
```

| Also | |
|---|---|
| `build-field-sheets.py` | The Field How To's standalone sheets |
| `build-pdfs.py` | PDFs of the pages and sheets |
| `build-observed-behaviour.py` | Technical Manual Appendix D, from the observed-behaviour entries |
| `publication.py` | **A library, not a script.** The single place deciding what the publication layer strips. Imported by the page and sheet builders |

## Superseded — they build into `SOP/`, not `deliverables/`

`SOP/` is the earlier single-document generation. See `SOP/SUPERSEDED.md`.

| | |
|---|---|
| `build-sop.js` | The `.docx` of the single-document SOP. `npm install docx` first |
| `build-checklist.py` | The four-page field checklist PDF. **Its Appendix A source has been rewritten since**, so the PDF in `SOP-v1-superseded/` does not match the live Field How To. Regenerating it against the live set is outstanding work, not a re-run |

Both still reference `brand/parametrix-wordmark.png`, which is why that superseded asset is kept.

## Spent migrations — kept as a record, not to be re-run

They performed the split from the single document into four and are recorded here so nobody mistakes
them for part of the pipeline.

| | |
|---|---|
| `rehome.py` | Moved a section from the single-document draft into the Technical Manual |
| `slice_rehome.py` | Sliced named subsections out of an SOP file and re-homed them |
| `renumber-sop.py` | Shifted SOP sections to make room for a new one. **Its range is hard-coded to the 21-section SOP; the SOP now has 22.** Fix the range before ever using it again |

## Note on verification

This environment has no working LibreOffice, pandoc or `pdftoppm`. `build-sop.js` output passes OOXML
structural validation but **has never been rendered and looked at** — open it in Word before issuing
anything. The same applies to `marketing/`.
