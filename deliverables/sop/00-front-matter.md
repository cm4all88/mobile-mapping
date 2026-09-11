# MX60 Mobile Mapping Standard Operating Procedure

**Trimble MX60 · Trimble Business Center 2026.10**

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
<!-- /circulation -->

> **What this SOP requires of Parametrix today: nothing.**
>
> | | |
> |---|---|
> | **Parametrix-originated requirements adopted** | **0** |
> | **Externally binding requirements restated here** | **7** — Trimble's and the equipment's, listed at **§2.4** |
>
> The seven are not Parametrix policy. They would bind an MX60 operator at any company, working
> from no SOP at all. **This draft does not authorise an MX60 accuracy statement** — it sets no
> tolerance, and **D-13** is open (§17.2).

---

<!-- circulation:how-to-review -->
## How to review this draft

**This is not primarily a copy-editing exercise.** Typos and awkward sentences are worth reporting,
but they are not what this draft needs. Four questions are:

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

**When commenting, identify the document and the section.** For example: **`SOP §14.5`**, or
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

> *"The registration part is confusing"* cannot be acted on. *"`SOP §14.5` is confusing"* can.
<!-- /circulation -->

---

## Document control

> **Provisional.** Parametrix's document-control convention has not been established, and the
> *Parametrix Brand Guide* settles visual identity only — it does not settle numbering, revision
> conventions, approval authorities, effective dates, retention or controlled-copy terminology.
> The block below is a temporary working scheme for this review only (**D-1**).

<!-- circulation:working-revision -->
### Working revision — internal draft only

> **This is a temporary working revision scheme, used only while the set is in internal review.**
> It is deliberately **not** a revision letter or number, so it cannot be mistaken for the
> Parametrix document-control convention that **D-1** will establish. When D-1 is answered, this
> block is replaced by the real one.

| | |
|---|---|
| **Document** | **MX60 Mobile Mapping Standard Operating Procedure** |
| **Working draft** | `2026-09-11-a` — date of circulation, plus a letter for same-day reissues |
| **Supersedes** | — first circulated draft |
| **Status** | **LIVING DRAFT — INTERNAL REVIEW.** Not issued, not approved |
| **Circulated for** | Internal review, training, testing and workflow development |
| **Prepared by** | MX60 mobile mapping documentation project |
| **Document identifier** | *Not assigned* — **D-1** |
| **Formal revision** | *Not assigned* — **D-1** |
| **Owner** | *Not assigned* — **D-1** |
| **Approved by** | **Nobody.** This draft is not approved and not issued |
| **Comments to** | *Not assigned* |
| **Set circulated together** | Technical Manual · SOP · Field How To · Office How To, all at `2026-09-11-a` |
<!-- /circulation -->

---

## What this SOP is

**It states what Parametrix requires.** It does not explain why, and it does not say which button
to press.

| Question | Document |
|---|---|
| **Must I?** | **This SOP** |
| Why does it work this way? | Technical Manual |
| How do I do it in the field? | Field How To |
| How do I do it in the office? | Office How To |

It is short on purpose. Where a requirement needs justification, the justification is a reference
to the Technical Manual, not a paragraph reproduced here. Where a requirement needs a method, the
method is in a How To.

---

## Whose authority each clause rests on

**Every clause with procedural force carries a label naming its authority.** The label is part of
the clause and is not decoration. **§3.2** is the full key; this is the short version.

| Label | Binds today? |
|---|---|
| **TRIMBLE REQUIREMENT** · **EQUIPMENT LIMIT** | **Yes** — the manufacturer's, not Parametrix's |
| **PARAMETRIX REQUIREMENT (ADOPTED)** | **Yes** — recorded in Appendix A. **None exists at this draft** |
| **TRIMBLE DOCUMENTED PROCEDURE** | No — Trimble documents the method without requiring it |
| **PARAMETRIX PROCEDURE (PROPOSED)** | No — a recommendation from this project |
| **PARAMETRIX DECISION REQUIRED** · **TESTING REQUIRED** | No — the answer is not set, or nobody has it yet |

> **CAUTION**
>
> **At this draft, no clause is ADOPTED.** Appendix A is empty of adoptions, and that is correct
> for a document under review rather than an oversight.
>
> **Nothing in this document may be quoted to a client, to a reviewer or to a regulator as an
> existing Parametrix standard.** A proposed requirement is a recommendation from this project. It
> becomes a requirement when Parametrix records a decision against it.
>
> **The reverse also holds.** The seven externally binding requirements at **§2.4** bind whether or
> not this draft is ever adopted, because their authority is Trimble's and the equipment's. This
> document restates them; it does not create them, and it cannot suspend them.

---

## What this SOP does not contain

| | Why |
|---|---|
| **Numerical acceptance tolerances** | Trimble publishes no acceptance tolerance for the MX60, and none has been established by test. Inventing one would be worse than leaving it open. See §17 and **D-13** |
| **Explanation** | Technical Manual |
| **Step-by-step method** | Field How To · Office How To |
| **Terminology** | Technical Manual **§6** is the authoritative glossary for all four documents. §3 below defines only the terms that carry procedural force in this SOP |

---

## Visual identity

This SOP follows the **Parametrix Brand Guide v6, November 2023**, through the shared style system
in `deliverables/_control/style/`. Its document accent is **Progress Orange**.
