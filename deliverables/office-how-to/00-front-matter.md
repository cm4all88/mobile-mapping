# MX60 Office How To

**Trimble Business Center 2026.10 · Trimble MX60**

<!-- circulation:banner -->
> **LIVING DRAFT — INTERNAL REVIEW**
>
> **This document is a living draft for internal Parametrix review, training, testing and workflow
> development.** It is not an issued Parametrix standard, and it does not replace professional
> judgement, project requirements, safety procedures or approved company policy.
>
> **Items marked Parametrix Decision Required, Proposed, Testing Required or Vendor Clarification
> Required are unresolved.** There are a lot of them, and that is deliberate — an open question is
> shown as an open question rather than filled in with a guess.
>
> **Two things follow from that.** Some requirements here **bind anyway** — Trimble's and the
> equipment's, because their authority was never Parametrix's to grant or withhold; they are listed
> with their sources at **SOP §2.4**. And there is **no Parametrix MX60 acceptance standard** to
> claim, because **D-13** is open.
<!-- /circulation -->

---

<!-- circulation:how-to-review -->
## How to review this draft

**This is not primarily a copy-editing exercise.** Typos and awkward sentences are worth reporting,
but they are not what this draft needs. Four questions matter:

| | |
|---|---|
| **1** | **Is anything technically wrong?** |
| **2** | **Is anything impractical in actual field or office use?** |
| **3** | **Is anything presented more strongly than Parametrix has actually decided?** |
| **4** | **What would prevent you from performing the work using these documents?** |

**Question 3 is the one most likely to be missed.** Every statement with procedural force in this
set carries a label saying whose authority it rests on — Trimble's, the equipment's, or
Parametrix's — and **no Parametrix requirement is adopted at this draft.** If something reads as
settled company practice when it is not, that is a defect, and it is the kind this project is least
able to catch on its own.

**Question 4 is the one that finds gaps.** If you could not actually do the work from these
documents — because a step is missing, a decision is open, a tool is not available, or the
instruction assumes something you were never told — say so. A gap is more useful than a correction.

### Who is being asked

Reviewers are identified by role, because each role sees a different failure.

| Role | What this draft most needs from you |
|---|---|
| **Survey leadership and the responsible PLS** | **Question 3.** Where does this overstate what Parametrix has decided? And which of the open decisions are actually yours to make |
| **MX60 field operators** | **Question 2**, in the vehicle. Sequence, timing, what is realistic on a real shift, and anything the Field How To gets wrong about the machine |
| **TBC mobile mapping processors** | **Questions 1 and 2.** Whether the software behaves as described, in the version you are running, and whether the workflow order survives contact with a real project |
| **QA/QC reviewers** | **Question 1**, and the records. Whether the evidence a section asks for is evidence you could actually review, and whether anything is claimed that the evidence does not support |
| **Project managers who may scope or rely on mobile mapping** | **Question 4.** What you would need to know before scoping this work, pricing it, or promising it to a client — and whether you could find it here |
| **Survey staff with conventional experience and limited mobile mapping experience** | **Question 4, and you are the most important reviewer for it.** Where does this assume something nobody explained? An unexplained assumption is invisible to the people who wrote it, and obvious to you |

### How to point at something

**When commenting, identify the document and the section.** For example: **`Office How To §16.4`**, or
**`SOP D-13`**.

Every section and subsection is numbered, and every warning, open decision, test and vendor
question carries an identifier that is the same in all four documents:

| Identifier | Means |
|---|---|
| **§n.n** | A numbered subsection of the document named |
| **W-n** | A warning. Worded identically wherever it appears |
| **D-n** | An open Parametrix decision |
| **Tn** | An open test — something nobody has measured yet |
| **V-n** | An open question for Trimble |

> *"The registration part is confusing"* cannot be acted on. *"`Office How To §16.4` is confusing"* can.

**Comments go to the MX60 Internal Review Log.** That is the working channel until Parametrix
assigns a document owner and a review process under **D-1** — there is no named owner to send them
to, and inventing one would be worse than saying so.
<!-- /circulation -->

---

## Document control

> **Provisional.** Parametrix's document-control convention is not established (**D-1**). The
> block below is a temporary working scheme for this review only.

<!-- circulation:working-revision -->
### Working Version — internal circulation only

> **This is a temporary working identifier, used only while the set is in internal review.** It is
> deliberately **not** a revision letter or number, so it cannot be mistaken for the Parametrix
> document-control convention that **D-1** will establish. A second circulation package on the same
> date becomes `-b`, then `-c`. When D-1 is answered, this block is replaced by the real one.

| | |
|---|---|
| **Document** | **MX60 Office How To** |
| **Working Version** | `2026-09-11-a` |
| **Status** | **LIVING DRAFT — INTERNAL REVIEW** |
| **Supersedes** | — first circulated draft |
| **Formal revision** | *Not assigned* — **D-1** |
| **Document owner** | *Not assigned* — **D-1** |
| **Approval status** | **Not approved — Living Draft** |
| **Circulated for** | Internal review, training, testing and workflow development |
| **Prepared by** | MX60 mobile mapping documentation project |
| **Review comments** | Record in the **MX60 Internal Review Log** |
| **Set circulated together** | Technical Manual · SOP · Field How To · Office How To, all at Working Version `2026-09-11-a` |
<!-- /circulation -->

## What this guide is

**It shows you what to do in Trimble Business Center, in the order you do it.**

| Question | Document |
|---|---|
| Why does it work this way? | Technical Manual |
| Must I? | SOP |
| **How do I do it in the office?** | **This guide** |
| How do I do it in the field? | Field How To |

**This guide cannot create a requirement.** If it tells you to do something the SOP does not
require, one of the two is wrong — and the SOP is the one that governs.

## Abbreviations used here

Everything else is in **Technical Manual §6**, the authoritative glossary for all four documents.

| | |
|---|---|
| **TBC** | Trimble Business Center |
| **SBET** | The post-processed trajectory. The normal input for survey work |
| **NAV** | The real-time trajectory computed in the vehicle. A fallback |
| **GCP** | Ground control point — the surveyed coordinate |
| **Target** | In TBC's registration commands, **a point picked in the point cloud**. Not a physical panel |
| **RMS** | Root mean square — here, a residual statistic |

## Visual identity

Parametrix Brand Guide v6, November 2023, through the shared style system in
`deliverables/_control/style/`. Document accent: **Optimistic Yellow**.
