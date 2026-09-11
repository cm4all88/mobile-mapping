# Living Draft change log

**One log for all four documents.** They are circulated together at one Working Version, so they
change together and are recorded together.

> **This is not a revision history.** A revision history needs a revision convention, and
> Parametrix's is **D-1**. A Working Version is a circulation label — a date, plus a letter if more
> than one package goes out on the same date — and it exists so two reviewers can tell whether they
> are reading the same text.

## How to add an entry

One row per circulated package. A change that is made but not circulated does not get a row; it
goes in the next one. Name the documents and the sections, not the files.

| Field | |
|---|---|
| **Working Version** | `YYYY-MM-DD-x`, incrementing the letter within a date |
| **Supersedes** | The previous Working Version, or `—` for the first |
| **Documents** | Which of the four changed. All four carry the new Working Version whether or not they changed, because they are circulated as a set |
| **What changed** | In terms a reviewer would recognise |
| **Why** | The input that caused it: a review comment, a field test, a Parametrix decision, a vendor answer, or a defect found by the gates |
| **Register items closed** | `D-n`, `Tn`, `V-n` resolved by this change, or `—` |

## The log

### `2026-09-11-a` — first internal circulation

| | |
|---|---|
| **Supersedes** | — |
| **Documents** | All four. First circulation |
| **Register items closed** | — |

**What changed.** The set became circulatable: a shared **LIVING DRAFT — INTERNAL REVIEW** status,
a *How to review this draft* panel naming the four reviewer questions and six reviewer roles, a
Working Version block that is deliberately not a revision, numbered Office How To task steps so a
reviewer can cite one, and an internal-review landing page.

**Authority audit, at the same time.** Three clauses that read as Trimble requirements were
Trimble's *documented method* — the initialization sequence, the closing sequence and the
control-bracketing rule — and were corrected to **should** under **TRIMBLE DOCUMENTED METHOD** or
**PARAMETRIX PROCEDURE (PROPOSED)**, raising **D-56**. Two genuine requirements that were buried in
prose were promoted: navigation alignment before logging, and the 30-minute minimum mission. One
further requirement was found in the source and added: **at least one control point in a
registration must not be a validation point** *(TBC 22905)*. The externally binding requirements
are now a register with a source quotation per row, and the count — **10** — is generated from it.

**Why.** Internal review needed a status, a route for comments and an addressable structure; the
authority audit was the last correctness pass before circulation.

> **What did *not* change.** The four-document architecture, SOP §14 Registration, the Field How To
> and the Office How To operational content, and the Technical Manual's evidence base. **D-13 is
> exactly as unresolved as it was**, and A / B / C are all still on the table.
