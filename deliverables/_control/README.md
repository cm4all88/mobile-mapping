# Project control documents

These four files are **shared infrastructure**. They are not deliverables and are not issued.
They exist so the four documents cannot drift apart.

| File | What it governs |
|---|---|
| **`master-register.csv`** | **The single authoritative backlog.** All 74 D, T and V items |
| **`warning-register.md`** | Authoritative wording for every warning quoted in more than one document |
| **`ownership-matrix.md`** | Which document owns each topic, and which merely reference it |
| **`workflow-stage-names.md`** | **Frozen** stage names, used identically everywhere |

---

## 1. The master register

`master-register.csv` — **the only place an item's status lives.**

| Column | Values / meaning |
|---|---|
| `id` | `D-n` decision · `T-n` test · `V-n` vendor question |
| `type` | `decision` · `test` · `vendor` |
| `status` | `open` · `in_progress` · `resolved` · `superseded` |
| `priority` | `P1` · `P2` · `P3` |
| `blocks` | **What this item actually prevents**, precisely: `nothing` · `collection` · `processing` · `formal acceptance` · `delivery for a stated accuracy purpose` · `one workflow branch`. Most items block **nothing** — they leave a question open, not the work |
| `owner` | Person or role, once assigned. Empty until *D-3* |
| `question` | The question, stated once |
| `why_it_matters` | The consequence of leaving it open |
| `source_evidence` | Trimble topics, manual pages, or `—` where it is purely a Parametrix choice |
| `affected_documents` | `Manual` · `SOP` · `Field` · `Office`, semicolon-separated |
| `affected_stage` | A frozen stage name from `workflow-stage-names.md` |
| `resolution` | What was decided or found. Empty while open |
| `date_resolved` | ISO date. Empty while open |

### Current state

| | Items | P1 | Blocking |
|---|---|---|---|
| Decisions | 35 | 20 | 9 |
| Tests | 25 | 6 | 0 |
| Vendor questions | 16 | 5 | 1 |
| **Total** | **76** | **31** | **10 rows, 9 distinct** |

> `D-2` and `V-4` are the same question — *which system do we own* — asked of Parametrix and of
> the vendor. They are kept as two rows because they have different owners and close
> independently, but they are one blocker.

### The circulation blocks

`circulation/` holds the three blocks that appear identically in all four front matters — the
**LIVING DRAFT — INTERNAL REVIEW** banner, the *How to review this draft* panel, and the temporary
working revision block. They are written into the documents by `tools/sync-circulation.py` and are
**never hand-edited in a document**, for the same reason the register is not: four copies of a
statement drift, and a status that differs between two documents is worse than no status at all.

### Views, not copies

The documents contain **filtered views** generated from this file. **No document is permitted to
carry an item's status independently.**

| View | Filter |
|---|---|
| **SOP Appendix A** | `type=decision` AND (`status≠resolved` OR resolved within the current revision) |
| **Manual Appendix E** | `type IN (test, vendor)` AND `status≠resolved` |
| **Manual Appendix F** | `type=test` AND `status=resolved` — the results |
| Field / Office How To | Inline `⚠ D-n` markers only, with no status text |

Regenerate with `tools/build-register-views.py`. **A view is never hand-edited.** If a view is
wrong, the CSV is wrong.

### Changing an item

1. Edit the CSV row — never a view
2. Regenerate the views
3. Check `affected_documents` and review each one named

---

## 2. Provisional identifiers

> **No Parametrix document numbers, revision conventions, approval-block wording, effective-date
> format, owner terminology or controlled-copy language have been assigned.**
>
> Parametrix's actual document-control convention has not been confirmed. Until it is, the four
> documents use **temporary descriptive identifiers only**:

| Document | Temporary identifier |
|---|---|
| Technical Manual | working draft `2026-09-11-a` |
| SOP | working draft `2026-09-11-a` |
| Field How To | working draft `2026-09-11-a` |
| Office How To | working draft `2026-09-11-a` |

Each carries a **document control block with the fields present but the conventions unset**, so
the real scheme can be dropped in without restructuring. The three supporting documents state
which SOP draft they support; the Manual states its evidence revision.

---

## 3. Status of this folder

Working infrastructure. Kept under version control with the deliverables, not issued with them.
