# 3. Definitions

**Technical Manual §6 is the authoritative glossary for all four documents.** Trajectory, SBET,
boresight, lever arm, registration, target, GCP, validation point, Update Scans, Cleanup and the
rest are defined there and are not repeated here.

This section defines only the words that carry **procedural force in this document** — the words
that decide whether a clause has been complied with.

## 3.1 Workflow stage names

The nineteen workflow stages are named identically in all four documents and in every checklist and
form. They are listed, with the synonyms that are not used, in **Technical Manual §4** and in
`deliverables/_control/workflow-stage-names.md`.

**A stage is not a command.** *Registration* is the stage; *Register a Run* is one of three
commands that perform it.

## 3.2 Obligation

| Term | Meaning |
|---|---|
| **shall** | A requirement that binds now. Departure is a non-conformance and is handled under §22 |
| **shall not** | A prohibition that binds now. The same applies |
| **should** | A recommendation. Departure is permitted and, where it affects the deliverable, is recorded |
| **may** | A permission. No obligation either way |

### Which clauses bind, and on whose authority

A requirement does not become binding only by Parametrix adopting it. **Trimble's instructions and
the equipment's limits bind regardless**, because their authority is the manufacturer's and does
not wait for a company decision.

Every clause in this procedure that carries procedural force therefore carries an **authority
label**:

| Label | Binding now? | Verb used |
|---|---|---|
| **TRIMBLE REQUIREMENT** | **Yes** | shall · do not |
| **EQUIPMENT LIMIT** | **Yes** | shall · do not |
| **PARAMETRIX REQUIREMENT (ADOPTED)** | **Yes** — recorded in Appendix A | shall |
| **TRIMBLE DOCUMENTED PROCEDURE** | No — Trimble documents the method without requiring it | **should** |
| **PARAMETRIX PROCEDURE (PROPOSED)** | No — a recommendation from this project | **should** |
| **PARAMETRIX DECISION REQUIRED** | No — the answer is not set | *no imperative* |
| **TESTING REQUIRED** | No — nobody has the answer yet | *no imperative, or a stated interim posture* |

> **`shall` is reserved for the three authorities that bind now.** A proposed Parametrix practice
> uses **should**. When Parametrix adopts it, the label changes to **(ADOPTED)** and the verb
> changes to **shall** — one edit, recorded in Appendix A.

> **A documented procedure is not a requirement.** Trimble publishes a great deal of method and
> requires comparatively little of it. Where Trimble writes *"must"*, or the software refuses, or
> a stated limit exists, the label is **TRIMBLE REQUIREMENT**. Where Trimble documents how to do
> something — including where it writes *"should"*, *"it is advised"*, or heads a list *"Proposal
> of a checklist"* — the label is **TRIMBLE DOCUMENTED PROCEDURE** and the verb is **should**.
>
> **This procedure does not promote Trimble's methods into Trimble's requirements**, which would
> borrow the manufacturer's authority for a rule the manufacturer did not make.

> **CAUTION**
>
> **At this revision no clause carries PARAMETRIX REQUIREMENT (ADOPTED).** Every `shall` in this
> procedure rests on a **Trimble requirement** or on an **equipment limit**. None of them is a
> Parametrix policy decision, and none may be described to a client as one.
>
> **Parametrix-originated requirements adopted: 0.** The `shall` clauses that remain are
> externally binding — they would bind an MX60 operator at any company, working from no SOP at
> all. They are listed in full at **§2.4**.

The full model, including why it is built this way, is
`deliverables/_control/authority-model.md`.

## 3.3 Terms with procedural force

| Term | Meaning in this procedure |
|---|---|
| **Approved** | A named person with the authority in §4 has recorded a decision, with a date. An approval that is not recorded did not occur |
| **In writing** | Recorded in the project record in a form that survives the project and identifies its author and date. An instant message is not in writing |
| **Recorded** | Written into the project record at the time, not reconstructed afterwards |
| **The project record** | The durable record of the project, in the location §20 requires. Not a processor's local machine |
| **Independent check** | An observation that **took no part in any adjustment** applied to the data it is checking, and whose designation was fixed **before** that adjustment was computed (§7.3) |
| **Accepted** | The person with acceptance authority under §4 has recorded that the dataset meets the project's stated accuracy requirement. Acceptance is against a requirement, never against a feeling |
| **Delivered** | Released outside Parametrix, or relied on by another discipline as final |
| **Destructive operation** | An operation that removes data or history and cannot be undone within the software. §18 governs these |
| **Re-collection** | Returning to site to collect again. The remedy of last resort, and the only remedy for a field error |

## 3.4 Two words this procedure avoids

| | |
|---|---|
| **"Verified"**, unqualified | Verified against what, by whom? The procedure names the comparison every time |
| **"QC'd"** | §16 defines what a quality control activity consists of. The abbreviation hides whether anything was inspected |
