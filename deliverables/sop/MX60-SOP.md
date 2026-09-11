# MX60 Mobile Mapping Standard Operating Procedure

**Trimble MX60 · Trimble Business Center 2026.10**

> **LIVING DRAFT — INTERNAL REVIEW**
>
> **This document is a living draft for internal Parametrix review, training, testing and workflow
> development.** It is not an issued Parametrix standard, and it does not replace professional
> judgement, project requirements, safety procedures or approved company policy.
>
> **Items marked Parametrix Decision Required, Proposed, Testing Required or Vendor Clarification
> Required are unresolved.** There are a lot of them, and that is deliberate — an open question is
> shown as an open question rather than filled in with a guess.

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

---

## Document control

> **Provisional.** Parametrix's document-control convention has not been established, and the
> *Parametrix Brand Guide* settles visual identity only — it does not settle numbering, revision
> conventions, approval authorities, effective dates, retention or controlled-copy terminology.
> The block below is a temporary working scheme for this review only (**D-1**).

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

---


---

# Part I — The Procedure and Who Runs It

---


---

# 1. Purpose, Scope and Application

## 1.1 Purpose

This procedure governs the acquisition, processing, quality control, acceptance, delivery and
retention of **mobile mapping data collected with the Trimble MX60**.

Its purpose is that a Parametrix mobile mapping deliverable can be relied on, and can account for
itself afterwards: what was collected, how it was processed, what it was checked against, who
accepted it, and on what basis.

## 1.2 Scope

**This procedure applies to** all Parametrix work in which the MX60 is used to collect data that
will be delivered, measured from, or relied on — including work where the mobile mapping data is
an input to another deliverable rather than the deliverable itself.

**It applies from** the decision to use mobile mapping on a project **through** archive of the
project record.

## 1.3 What it does not govern

| | Where it belongs |
|---|---|
| Conventional survey practice — control networks, datums, adjustment, check observations | Existing Parametrix survey practice. This procedure assumes it |
| Establishing the control network itself | Existing Parametrix survey practice. §7 states only what mobile mapping additionally requires of it |
| Terrestrial or airborne scanning | Not this procedure |
| The client's own specification | Where a client specification is stricter, **it governs.** Where it is less strict, this procedure governs |

> The brand guide makes the same point for visual identity: a project deliverable prepared for a
> client may follow the client's guidelines *(Parametrix Brand Guide, p.22)*. The same logic
> applies to technical requirements.

## 1.4 Application

This procedure applies to every person performing any activity within its scope, in the roles
defined in §4.

Where a requirement cannot be met on a particular project, §22 states what happens. **A
requirement is not waived by being inconvenient on the day.**

## 1.5 Related documents

| Document | Relationship |
|---|---|
| **MX60 Mobile Mapping Technical Manual** | The technical basis. Every explanatory reference in this SOP points to it |
| **MX60 Field How To** | The field method. Carries the checklists |
| **MX60 Office How To** | The processing method in Trimble Business Center |
| `reference/mx60-reference-data.csv` | The authority for manufacturer values. Technical Manual, Appendix B |
| Master register | The single register of open decisions, tests and vendor questions. Appendix A is this SOP's **view** of it |

> **The master register is one register.** Appendix A and the Technical Manual's Appendix E are
> filtered views of the same file, generated. An item cannot carry one status here and a different
> status there.

## 1.6 Review

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> **Who owns this procedure, who approves a revision, and on what review cycle?**
>
> A review trigger that is not optional: **Trimble Business Center is on an annual release cycle,
> and releases have changed mobile mapping behaviour.** This revision documents **TBC 2026.10**.
> A TBC upgrade is a reason to review this procedure, not merely an IT event.

---

# 2. Document Control and Related Documents

## 2.1 What this section is for

A procedure that cannot say which revision of itself was in force on a given date cannot support a
deliverable produced on that date. This section reserves the machinery. **It does not invent it.**

## 2.2 What is not established

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> None of the following is established, and none is invented here:
>
> | | |
> |---|---|
> | **Document identifier** | The scheme, and this document's number |
> | **Revision convention** | Letters, numbers, draft-versus-issued, and how a revision is incremented |
> | **Approval authority** | Who approves an issue, and whether technical and procedural approval are separate |
> | **Effective date rule** | When a revision takes effect relative to its approval, and what happens to work in progress |
> | **Controlled-copy terminology** | Whether copies are controlled, how, and what an uncontrolled copy is called |
> | **Distribution** | Who receives a revision, and how receipt is recorded |
>
> **The Parametrix Brand Guide does not settle these.** It is authoritative for visual identity —
> colour, typography, logo, layout — and says nothing about document control. The two should not be
> confused: applying the brand to this document does not make it a controlled document.

Until D-1 is answered, this procedure carries a **temporary working draft label** on its front
matter — a circulation date, not a revision — and the status **LIVING DRAFT — INTERNAL REVIEW**.
The working label exists so that two reviewers can tell whether they are reading the same text. It
is not a revision convention and does not become one by being used.

## 2.3 The document family

Four documents, issued as a set.

| Document | Role | Changes when |
|---|---|---|
| **SOP** *(this document)* | What Parametrix requires | A requirement changes, or a decision is adopted |
| **Technical Manual** | Why the system behaves as it does, and the evidence | The evidence changes — a TBC release, a test result, a vendor answer |
| **Field How To** | Field method and checklists | A field method changes |
| **Office How To** | Processing method | A processing method changes, or TBC changes |

### The rule between them

**This SOP is the governing document.** The other three are issued in support of a stated revision
of it.

| Change | Triggers |
|---|---|
| A change to this SOP | Review of all three supporting documents |
| A change to the Technical Manual | Review of this SOP **only where the change touches a requirement** |
| A change to a How To | No review of this SOP. A How To may not create a requirement |

> **A How To cannot create a requirement.** If a How To states something that must be done and
> this SOP does not require it, one of the two is wrong. Resolve it here, not there.

## 2.4 What binds while this procedure is a draft

Two different things are easily confused, and this procedure keeps them apart.

| | Count at this revision |
|---|---|
| **Parametrix-originated requirements adopted** | **0** |
| **Externally binding requirements restated here** | **7** |

**Parametrix has adopted nothing.** Every Parametrix-originated clause in this procedure is a
proposal, carries **PARAMETRIX PROCEDURE (PROPOSED)**, and uses **should**. Nothing in this
document becomes company policy by being written down here.

**The externally binding requirements are not Parametrix's and do not wait for Parametrix.** They
are restated here because an operator needs them in one place, not because this procedure creates
them. They would bind an MX60 operator at any company, working from no SOP at all:

| # | Requirement | Authority | Clause |
|---|---|---|---|
| 1 | Navigation alignment complete before data logging — *"must be done first before data logging is allowed"* | Trimble, stated · system-enforced | §9.2 |
| 2 | Minimum mission length **30 minutes** — *"is required"* | Trimble, stated | §9.2 |
| 3 | A GCP and its picked target no more than **30 m** apart | Trimble · TBC rejects the pair | §14.5 |
| 4 | Data outside the outermost control point not described as registered to it | Trimble, stated limitation | §7.2, §14.5 |
| 5 | A calibration not accepted on RMS alone — *"a visual check is needed"* | Trimble, stated | §15.4 |
| 6 | A registration not judged on residuals alone — same instruction, same wording | Trimble, stated | §14.9, §16.7 |
| 7 | Equipment and power limits — speed, voltage, Battery Protect, load | Manufacturer limits | §9.4 |

> **CAUTION**
>
> **A documented Trimble method is not in this table.** Trimble's initialization sequence, its
> closing sequence and its in-field checklist are documented method — Trimble writes *"should"*,
> *"it is advised"*, and *"Proposal of a checklist for system operation"*. They carry
> **TRIMBLE DOCUMENTED PROCEDURE** and **should**, and whether Parametrix makes them mandatory is
> **D-56**.
>
> Presenting a manufacturer's method as a manufacturer's requirement borrows an authority the
> manufacturer did not grant. It also makes the real requirements harder to see.

> **This procedure does not authorise an accuracy statement.** It restates what Trimble and the
> equipment require, and it proposes how Parametrix might work. It sets no accuracy tolerance, no
> error budget, and no acceptance threshold, and **D-13** is unresolved. Whoever signs an accuracy
> statement for MX60 work today signs on their own professional judgement (§17.2).

## 2.5 Evidence revision

The Technical Manual carries an **evidence revision** alongside its document revision, recording
the state of the source material rather than the state of the prose: which TBC version, how many
help topics, how many manuals, how many structured reference records.

**This SOP states which evidence revision it was written against** — on the front matter — because
a requirement derived from evidence is only as current as that evidence.

## 2.6 Records this section requires

| Record | Held by | State |
|---|---|---|
| Revision history of this procedure | Appendix C | **D-1** |
| Which supporting revisions were issued with this one | Front matter | **D-1** |
| Distribution and receipt | — | **D-1** |

---

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

---

# 4. Roles, Responsibilities and Authorities

## 4.1 Why this section exists first

Three activities in this workflow change what the deliverable is, and two of them are invisible
afterwards:

- **Designating which control points are held as independent checks** — because if the person
  computing the adjustment also chooses what it is measured against, the check is not independent
- **Accepting a registration** — because acceptance is the point at which the data becomes the
  deliverable
- **Running a destructive operation** — because it cannot be undone (§18)

TBC makes the first of these a checkbox *(Technical Manual §22.2)*, which makes it easy to change
quietly. That is the reason this SOP treats authority as a control and not as an organisation chart.

## 4.2 The decision

> **PARAMETRIX DECISION REQUIRED · D-3 · P1 · blocks operation**
>
> **Who may operate the system, who may register, who may accept a registration, who may run
> Cleanup, and who signs an accuracy statement?**
>
> Until this is answered, every clause in this procedure that names a role — *the Project
> Surveyor*, *the Processor*, *the System Owner* — is naming something nobody holds. That is why
> those clauses are **proposed** rather than binding, and why §18 cannot require an authorisation
> from a person who has not been appointed.

### The structure proposed, for decision

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted. Offered so that D-3 has something concrete
> to react to.*
>
> | Activity | Performed by | Reviewed or approved by |
> |---|---|---|
> | Mission planning | Processor or Project Surveyor | Project Surveyor |
> | Control network design | Project Surveyor | — |
> | Field acquisition | Field Technician | — |
> | Field quality checks and close-out | Field Technician | — |
> | Trajectory processing | Processor | — |
> | Calibration | Processor | System Owner |
> | **Registration** | **Processor** | **Project Surveyor** |
> | **Designating control versus independent check** | **Project Surveyor** | — |
> | Point cloud and imagery QC | Processor | Project Surveyor |
> | **Cleanup Mobile Mapping Mission** | **Processor** | **Project Surveyor, in writing** |
> | Export and delivery | Processor | Project Surveyor |
> | Accuracy statement | Project Surveyor | — |
> | Archive | Processor | Project Manager |
>
> The three rows in bold are the ones where the reviewer genuinely matters. The rest could
> reasonably collapse onto fewer people on a small job.

## 4.3 The one separation this procedure treats as structural

> **PARAMETRIX PROCEDURE (PROPOSED) · D-15**
>
> **The person who designates control versus independent check should not be the person who
> computes the registration.**
>
> If both are the same person, the residuals on the check points measure the fit of an adjustment
> to observations that person was free to choose. That is not an independent check, whatever the
> numbers say.
>
> On a job small enough that one person does both, the designation is **recorded before the
> registration is computed** and is not changed afterwards (§7.3).

## 4.4 Responsibilities that attach to any assignment

Whoever holds a role, these attach to it:

| | |
|---|---|
| **Stand-down authority** | The Field Technician may stop or decline collection on safety or data-quality grounds without seeking approval first. The decision and its reason are recorded. **This authority is not conditional on being right** |
| **Escalation** | Anyone who finds that a delivered dataset may not be what it was believed to be escalates it. To whom is part of **D-3** |
| **Competence** | Nobody performs an activity they are not qualified for under §5, whatever the schedule says |

## 4.5 What the record must answer

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Whatever Parametrix decides about roles, the project record **should** be able to answer, for any
> dataset, years later:
>
> 1. Who collected it, when, and in what conditions
> 2. **Which trajectory the delivered data was built on** *(Technical Manual §30 — this one is
>    genuinely hard)*
> 3. Which points were used as control and which were held as independent checks
> 4. What the residuals were, on both
> 5. Who accepted it, on what date, against what accuracy requirement
> 6. Whether a destructive operation was run, by whom, and what was archived first
>
> Six facts. None is onerous to record at the time. All are effectively unrecoverable later.
> *(D-29)*

## 4.6 Records this section requires

| Record | State |
|---|---|
| Who holds each role on a given project | **D-3** |
| Who designated control versus independent check, and when | **D-15** |
| Any exercise of stand-down authority, and its reason | **D-43** |

---

# 5. Competence and Training

## 5.1 The principle

Mobile mapping fails quietly. A weak trajectory produces a clean, dense, internally consistent
point cloud in the wrong place *(Technical Manual §3.2)*. There is no visual tell, so the
protection is a person who knows what to check and is required to check it.

**Competence here is not "has operated the system." It is "knows what the system cannot tell
you."**

## 5.2 What qualification covers

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Three qualifications are distinguished. Who holds each, how it is obtained and how it is
> evidenced is part of D-3.

| Qualification | Covers |
|---|---|
| **Qualified to operate** | Installation and pre-flight; initialization and the closing sequence, and why each exists; operating limits and stand-down authority; field quality checks and the field record |
| **Qualified to process and register** | The data chain and what regenerates from what; trajectory processing; scan generation; registration and the three commands; **what RMS can and cannot prove**; the layered QC in §16 |
| **Qualified to accept** | All of the above, plus the accuracy framework in §17 and the authority under §4 |

## 5.3 The five things a qualified person is expected to know

Not a training syllabus — a list of the misconceptions that have actual consequences. Each is
covered in the Technical Manual at the reference given.

| | | Where |
|---|---|---|
| 1 | **The trajectory is the job.** Every point inherits its error, and an attitude error grows with range | Technical Manual §2, §3 |
| 2 | **A good RMS does not prove success. A bad RMS proves failure.** Trimble states this in identical words in two places | Technical Manual §23 |
| 3 | **Registration does not move points.** The cloud is unchanged until Update Scans runs | Technical Manual §19 |
| 4 | **A Local adjustment does not extrapolate** beyond the outermost control point, and nothing shows where it stopped | Technical Manual §21 |
| 5 | **Cleanup cannot be undone** | Technical Manual §28 |

> **The In Plain English boxes in the Technical Manual are the intended route to this.** Read end
> to end with nothing else, they describe the whole workflow in ordinary language.

## 5.4 Currency

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Whether a qualification lapses, and what refreshes it. One trigger is not discretionary: **a TBC
> release can change mobile mapping behaviour** (§2.3), and a processor working from a prior
> release's understanding is working from a stale procedure.

## 5.5 Records this section requires

| Record | State |
|---|---|
| Who holds which qualification, and from when | **D-3** |
| Training delivered, and against which document revision | **D-3** |

---


---

# Part II — Before and During Collection

---


---

# 6. Project Setup Requirements

## 6.1 Before any data is collected

Four things **should** exist in writing before mobilisation. None is onerous, and the failures
they prevent are expensive.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *the practice of recording them.* **What** each one says is
> a separate open decision, named in the table.

| # | Requirement | State |
|---|---|---|
| 1 | **The accuracy requirement**, stated in writing, with the client agreement or scope it derives from | **PARAMETRIX DECISION REQUIRED — D-13.** The requirement to state one is not in doubt; what constitutes meeting it is §17 |
| 2 | **The coordinate reference system, datum, epoch and geoid model**, stated in writing and matching the control network | **PARAMETRIX DECISION REQUIRED — D-21** |
| 3 | **Grid or ground**, agreed with the client in writing | **PARAMETRIX DECISION REQUIRED — D-38** |
| 4 | **The system configuration and fitment** the work assumes | **PARAMETRIX DECISION REQUIRED — D-2 · blocks operation** |

## 6.2 The coordinate reference system

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

> **PARAMETRIX DECISION REQUIRED · D-21 · P1 · blocks operation**
>
> **Which datum and epoch does Parametrix work in, who sets it, and who checks it?**
>
> Epoch carries more weight here than in conventional work, because the trajectory's reference
> frame and the project's control may be realised at different epochs *(Technical Manual §12.4)*.
> TBC 2026.10 allows working at a non-default epoch and warns that the feature "is intended for
> experienced users, as incorrect settings may lead to inaccurate results" *(TBC RN 2026.10)*.

### The frame the trajectory is computed in

The trajectory is produced by POSPac, which has its own view of the project's coordinate system and
may compute in ITRF00 and then transform. The only outward sign is the SBET filename
*(Technical Manual §12.3, §17.4)*.

> **PARAMETRIX DECISION REQUIRED · D-19 · P1 · blocks operation**
>
> **IN-Fusion+ Single Base or PP-RTX?** The two differ in whether a local base station must be
> occupied on every mission, and in the reference frame the solution is computed in. It interacts
> with **D-42** (§8) and with D-21 above.

> **TESTING REQUIRED · T10**
>
> Which of Parametrix's normal coordinate systems POSPac recognises directly, and which trigger
> the ITRF00 path. Answerable once, then known.

## 6.3 Grid and ground

> **IMPORTANT**
>
> A **ground**-scaled export **does not record the scale factor it used**. A **grid** export writes
> a sidecar naming the coordinate system and scale factor *(TBC 11769; Technical Manual §12.5)*.
>
> The recipient of a ground-scaled file cannot recover the scale factor from the file. Agree it in
> writing, and make sure the delivery can say what it is (§19).

> **PARAMETRIX DECISION REQUIRED · D-38**
>
> Deliverable specification — standard formats, which export path produces each, and the default
> scaling.

## 6.4 The system this work assumes

> **PARAMETRIX DECISION REQUIRED · D-2 / V-4 · P1 · blocks operation**
>
> **Which MX60 configuration is the Parametrix system — Core, Pro or Premium? Are GAMS and DMI
> fitted? Which mounting rack?**
>
> This is the single decision that unblocks the most others. It changes every imagery resolution
> statement, the attitude accuracy underlying every accuracy statement, whether the initialization
> manoeuvres are required or merely advisable, and whether DMI settings appear in trajectory
> processing *(Technical Manual §7.7, §9)*. **The vendor can confirm it from the serial number.**

## 6.5 Records this section requires

| Record | Where | State |
|---|---|---|
| Accuracy requirement, and its source | Project record | **D-13** |
| CRS, datum, epoch, geoid — and who set them | Project record | **D-21** |
| Grid or ground, as agreed | Project record and client agreement | **D-38** |
| Configuration and fitment assumed | Project record | **D-2** |

---

# 7. Control Requirements

This section states only what **mobile mapping** additionally requires of a control network.
Establishing the network is ordinary Parametrix survey practice and is not governed here (§1.3).

## 7.1 Control has to be findable in a point cloud

A mobile mapping control point must be identifiable in the point cloud at the density and incidence
angle the vehicle produced. **That is a different requirement from occupiable with a prism**
*(Technical Manual §22.5)*.

| Works | Works poorly |
|---|---|
| Painted stop-bar and lane-line corners — crisp intensity edges | A survey nail in asphalt: a few millimetres across, below cloud resolution |
| Target panels for which TBC holds templates | Small features at grazing incidence |
| Painted arrow and legend corners | Anything that moves, is repainted, or is worn |

Horizontal and vertical suitability are separate. A painted stop-bar corner is an excellent
horizontal target and a poor vertical one, and TBC allows a point to participate in one component
and not the other *(Technical Manual §22.2, §22.3)*.

> **TESTING REQUIRED · T25**
>
> Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle. **This will shape control design more than any software setting.**

## 7.2 Control and the delivered extent

> **CAUTION · W-08**
>
> **Local does not extrapolate.** Trimble states it is *"not for systematic error along the run or
> for adjusting outside the ground control points set"* *(TBC 22905)*.
>
> Beyond the first and last control point the trajectory is not adjusted, **and nothing indicates
> where the adjustment stopped.** Control must bracket the extent you intend to deliver.

> **TRIMBLE REQUIREMENT** — *binding now, on Trimble's authority, not Parametrix's*
>
> The limitation itself is Trimble's and is not open to local interpretation. Data outside the
> outermost control point **shall not** be described as registered to that control, because it was
> not adjusted.

> **PARAMETRIX PROCEDURE (PROPOSED) · D-56**
>
> What follows from the limitation is a design rule, and the design rule is ours: control
> **should** bracket the extent to be delivered.
>
> Trimble states a limitation, not a control-design requirement. It does not say control must
> bracket anything; it says the adjustment stops. This procedure draws the practical consequence
> and proposes it — it does not present it as a manufacturer instruction.

Bracketing, not merely falling within. The ends of a corridor are also where the trajectory
smoother had data on one side only *(Technical Manual §14.4)*, which makes them simultaneously the
weakest data and the place registration helps least.

## 7.3 Independent checks are designated before registration

> **PARAMETRIX PROCEDURE (PROPOSED) · D-15, D-3**
>
> 1. **Independent check points are designated by the Project Surveyor before registration begins**
> 2. **A point's As Check status is not changed during processing.** If a designation was wrong, it
>    is changed by the Project Surveyor, **recorded**, and the registration is recomputed from the
>    imported trajectory using **Edit** — not layered on top of the previous one
>    *(Technical Manual §21.8)*
> 3. **The designation is recorded in the project record** and travels with the accuracy statement

> **The failure this prevents.** A conscientious processor registers a mission, finds one check
> point with a residual larger than expected, and adds it to the adjustment to bring it in. Every
> step is well intentioned. The result is an adjustment with no independent check at all, and a set
> of residuals that now measure nothing *(Technical Manual §22.4)*.

## 7.4 How much control, and where

> **PARAMETRIX DECISION REQUIRED · D-16 · P1 · blocks operation**
>
> **How many control points, at what spacing, how many held as independent checks, and does density
> vary with predicted GNSS conditions?**
>
> **No Trimble source states a minimum, a spacing or a ratio.** TBC's software minimum is one
> control pair — a mathematical floor with no bearing on survey adequacy *(Technical Manual
> §21.6)*.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *a structure for the decision, not the decision*
>
> - Control **bracketing** each end of the delivered extent, outside it where the corridor allows
> - Control along the corridor at an interval set from the project accuracy requirement, and
>   **tightened where GNSS is predicted to be degraded** (§8)
> - **Independent check points distributed, not clustered**, including at least one in each distinct
>   GNSS environment — open sky, tree cover, urban canyon
> - **A check point near each end of the delivered extent**
>
> **No counts, spacings or ratios appear here deliberately.** Those are the content of D-16.

> Two indications of scale exist, and neither is a specification. Trimble's Target-Bundle
> Adjustment operates at **250 m** intervals when checked and **70 m** when unchecked
> *(Technical Manual §21.7)*. The Queensland TMR mobile laser scanning guideline is an example of
> how another agency answered this question, cited in the Technical Manual §22.6 **as an example
> and not as a standard**.

## 7.5 Records this section requires

| Record | State |
|---|---|
| Control network, with coordinates and their source | Existing practice |
| **Which points are control and which are independent checks, fixed before registration** | **D-15** |
| Who designated them, and when | **D-3** |

---

# 8. Mission Planning Requirements

## 8.1 What planning must produce

A mission plan, in the project record, before mobilisation. It states the route, the passes, the
GNSS assessment, the initialization locations, and — explicitly — **what mobile mapping will not
get**.

## 8.2 Passes and overlap

> **PARAMETRIX DECISION REQUIRED · D-41 · P1 · blocks operation**
>
> **How many passes, in what pattern, by roadway type?**
>
> No Trimble source specifies a pass pattern. The v1 Parametrix draft stated a minimum of three
> passes on the pavement; **that figure is not traceable to any source in the evidence set** and is
> recorded here so it is not lost, not because it is established.

Two facts constrain the answer, and both are in the Technical Manual:

- **A second pass in the opposite direction improves a dataset more than any setting change**,
  because it converts grazing incidence into direct incidence and long range into short range for
  the far side of the corridor *(Technical Manual §16.3)*
- **Overlap is what makes the office remedies possible.** LiDAR QC and run-to-run registration both
  require overlapping runs *(Technical Manual §11.5, §21.11)*

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

## 8.3 GNSS assessment

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> The plan **should** identify GNSS-hostile stretches **before mobilising**, and for each state the
> expected duration at realistic collection speed.

> **Duration, not length.** Inertial drift is a function of time. A 300 m tunnel at 80 km/h is 13
> seconds; the same tunnel at 20 km/h in traffic is nearly a minute *(Technical Manual §15.1)*.
> The time of day is part of the assessment.

> **IMPORTANT**
>
> Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
> nothing beyond *(MX60 UG Rev B, p.56; Technical Manual §15.2)*.
>
> **Outages materially longer than 60 seconds are a planning problem, not a driving problem.**
> Beyond the published figure, any expectation is an extrapolation past the manufacturer's stated
> envelope.

For each hostile stretch the plan states the mitigation: additional control, planned overlap for
LiDAR QC, or a different acquisition method — **because two of the three have to be arranged
before the crew leaves.**

> **TESTING REQUIRED · T31**
>
> Whether predicted GNSS conditions correlate with achieved trajectory RMS on this system. Until
> that is established, the assessment is judgement rather than estimate.

## 8.4 Initialization locations

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> The plan identifies a **primary and a backup** initialization location, each of which is:
>
> - open sky, away from buildings and canopy
> - somewhere the vehicle can safely sit still for two to three minutes
> - with room afterwards to drive straight and perform dynamic manoeuvres
>
> Scout them on imagery before mobilising. A lot that turns out to be fenced, occupied or under
> trees costs twenty minutes at the worst moment of the day. *(Technical Manual §13)*

## 8.5 Base station strategy

> **PARAMETRIX DECISION REQUIRED · D-42 · P1 · blocks operation**
>
> **Own base on project control, VRS, RTX, or CORS post-processing — and what maximum baseline?**
>
> It interacts with **D-19** (§6.2): Single Base requires a local base station on every mission,
> PP-RTX does not. The decision determines field logistics on every job.

## 8.6 What mobile mapping will not get

> **PARAMETRIX PROCEDURE (PROPOSED) · D-34**
>
> Record in the project file **before mobilising**: the segments where mobile mapping is expected
> to be marginal, the mitigation chosen for each, and the segments where another method is
> proposed.

> **This is the clause people avoid**, and the reason it is a requirement rather than a
> recommendation. What it costs to discover the same thing in the office instead is set out in
> **Technical Manual §15.5**.

> **PARAMETRIX DECISION REQUIRED · D-34**
>
> The decision rule when a corridor produces an unacceptable trajectory: who decides, against what,
> and what the client is told.

## 8.7 Records this section requires

| Record | State |
|---|---|
| The mission plan — route, passes, direction, overlap | **D-41** |
| GNSS assessment, with duration estimates and mitigations | **D-41, D-42** |
| Initialization locations, primary and backup | **PROPOSED** |
| Segments mobile mapping will not serve, and what is proposed instead | **D-34** |

---

# 9. Field Acquisition Requirements

The method is in the **Field How To**. This section states what shall be done, and what shall not.

## 9.1 Before the vehicle moves

| # | Requirement | State |
|---|---|---|
| 1 | The installation configuration, lever arms and Vehicle Preset are as recorded, and have not changed since | **PARAMETRIX DECISION REQUIRED — D-46** |
| 2 | Where GAMS or DMI are fitted, **each is activated in Vehicle Settings** — not merely installed | **PROPOSED** |
| 3 | The mission plan (§8) is on board and understood | **PROPOSED** |
| 4 | Storage has capacity for the planned collection | **PROPOSED** |

> **CAUTION**
>
> An aiding sensor that is installed and wired but **not activated in Vehicle Settings logs
> nothing**, and nothing looks wrong *(TMI UG Rev L, p.21; Technical Manual §9.3)*. The office
> symptom appears days later as a dimmed settings pane, by which time the mission is collected.

> **PARAMETRIX DECISION REQUIRED · D-46**
>
> **Where are the lever arms, the Vehicle Preset and the installation configuration recorded, and
> who verifies them?** These values are entered once and used on every mission afterwards. An
> error in them is systematic, invisible, and persists until somebody re-measures.

## 9.2 Initialization

> **TRIMBLE REQUIREMENT** — *(MX60 QSG Rev B, §5.3, p.11)*
>
> **Navigation alignment shall be complete before data logging begins.** Trimble states it in
> mandatory terms and the system enforces it: *"Navigation alignment must be done first before data
> logging is allowed!"* It is not a matter of operator discipline.

> **TRIMBLE REQUIREMENT** — *(MX60 QSG Rev B, §5.4, p.13)*
>
> **A mission shall be at least 30 minutes long.** *"Important! A minimum mission time of ≥30 min is
> required."*

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 QSG Rev B, §5.3, p.11; §6, p.14)*
>
> Trimble documents an initialization sequence — static logging, a straight run, then dynamic
> manoeuvres — and it **should** be performed at the start of every mission, in the order given.
>
> **Trimble does not state this sequence as a requirement**, and this procedure does not claim it
> is one. Trimble writes *"Mobile Mapping Mission **should** be started in a static mode"*, and
> heads the in-field list *"Proposal of a checklist for system operation"*. Whether Parametrix makes
> the sequence mandatory is **D-56**.

> **IMPORTANT**
>
> **Green is not finished.** The navigation status turning green means the solution met its
> accuracy thresholds, not that it has converged. Trimble asks for **up to ten further minutes**
> before recording anything that matters *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.**

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> That data **should not** be spent on the most important part of the corridor. Trimble asks for the
> settling time; how the crew spends it is Parametrix's to decide.

The sequence and its rationale are in **Technical Manual §13**; the steps are in the **Field How
To**.

## 9.3 The closing sequence

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 QSG Rev B, §5.5, p.13)*
>
> Trimble documents a closing sequence and instructs that the mission be finalized *"according to
> the following sequence"* — dynamic manoeuvres, varying speed, then 2–3 minutes static — and it
> **should** be performed at the end of every mission, before the mission is closed in TMI.
>
> **Trimble states the reason, not an obligation.** Its note says symmetrical start and end
> procedures *"supports forward and reverse processing modes in the office software"*. That is a
> strong technical reason and a weak instruction; the strength of the rule is Parametrix's to set,
> and it is **D-56**.

> **CAUTION**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and then
> driving to open sky achieves nothing. *(Technical Manual §14.2)*

It takes about five minutes and it is the cheapest quality improvement in the workflow. It cannot
be added later — a crew returning the next day cannot append it, because a new mission is a new
trajectory *(Technical Manual §14.3)*.

## 9.4 Operating limits

| Limit | Value | Source |
|---|---|---|
| **Recommended maximum speed with the system operating** | **80 km/h (50 mph)** | MX60 UG Rev B |
| Absolute maximum, operating or not | 110 km/h (68 mph) | MX60 UG Rev B |
| **Direct sun, stationary or below 10 km/h** | **Outside the rated operating envelope** | MX60 UG Rev B, p.53 |

> **CAUTION · W-11**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*: an audible warning below **10.5 V for longer than
> 12 seconds**, power cut below **10.5 V for more than 90 seconds**, recovery if voltage rises
> above **12.0 V** within that time.
>
> **An interrupted run loses the closing sequence with it.** Treat the audible warning as an
> instruction to restore charge, not as information.

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **Field operating rules** — wet-weather go/no-go with operator stand-down authority, night
> collection, and collection speed by deliverable type. Trimble publishes a recommended maximum and
> an absolute maximum and **no guidance relating speed to deliverable quality**
> *(Technical Manual §16.2)*.

## 9.5 Stand-down authority

**The Field Technician may stop or decline collection on safety or data-quality grounds without
seeking approval first.** The decision and its reason are recorded. This authority is not
conditional on the decision later proving correct (§4.4).

## 9.6 The field record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-49**
>
> Recorded per mission, at the time: date, operator, vehicle, mission ID; capture settings; the
> initialization location and time; each run with start and end and any incident; **GNSS conditions
> observed**; weather; traffic and occlusion events; **anything not collected and why**; the closing
> sequence performed; disk and free space at the end.

> **This is the one record in the whole workflow with no software artefact behind it.** Nothing in
> TBC knows that a truck occluded the near lane for 200 m, or that the corridor was collected in
> rain. If the crew does not write it down, it is gone *(Technical Manual §30)*.

## 9.7 Records this section requires

| Record | State |
|---|---|
| Pre-flight confirmation, including aiding-sensor activation where fitted | **D-46** |
| The field record, per §9.6 | **D-49** |
| Any exercise of stand-down authority, and its reason | **D-43** |
| Operating-limit exceedance, if any, and what was done | **D-43** |

---

# 10. Field Close-out and Handoff

## 10.1 Why close-out is a separate requirement

Everything in this section is cheap on site and impossible afterwards. A gap discovered in the
office costs a mobilisation; the same gap discovered before the vehicle leaves costs twenty
minutes.

**The field stage is the only stage in the workflow with no office remedy**
*(Technical Manual §5.5)*.

## 10.2 Coverage verification, before leaving site

> **PARAMETRIX PROCEDURE (PROPOSED) · D-49**
>
> Confirmed against the mission plan (§8) before the vehicle leaves:
>
> 1. Every planned pass was driven, **in the planned direction**
> 2. The corridor was driven end to end, including any extent beyond the deliverable needed to
>    bracket control (§7.2)
> 3. **Planned overlap was actually collected** — this is the one that removes office options if
>    missed (§8.2, W-10)
> 4. Sections not collected, and why, are recorded
> 5. The closing sequence was performed (§9.3)

## 10.3 What accompanies the data

> **PARAMETRIX PROCEDURE (PROPOSED) · D-49**
>
> A mission is handed to the office with:
>
> | | |
> |---|---|
> | The complete mission folder | Not the `.mxdb` alone — that is an index, not the data *(Technical Manual §5.2)* |
> | The field record | §9.6 |
> | Base station data | If a local base was occupied |
> | Any deviation from the plan, and its reason | §8, §22 |

## 10.4 Handoff is a transfer of responsibility

Until the office has confirmed a verified copy (§11), **the field holds the only copy of an
unrepeatable measurement.** Close-out is not complete when the vehicle is packed; it is complete
when §11.2 has been satisfied.

## 10.5 Records this section requires

| Record | State |
|---|---|
| Coverage verification, performed and by whom | **D-49** |
| Deviations from the mission plan | **D-49** |
| Handoff — what was transferred, to whom, when | **D-52, D-54** |

---


---

# Part III — Office and Delivery

---


---

# 11. Data Transfer and Custody

## 11.1 The one irreplaceable thing

`POS_1/raw/` holds the raw GNSS and inertial observations. **Every trajectory the office ever
computes derives from those files, and nothing can recompute them** *(Technical Manual §5.2)*. The
picked registration targets are the other irreplaceable item, and that comes later (§13).

Everything else in the chain is reproducible. These two are not.

## 11.2 Offload and verification

> **PARAMETRIX PROCEDURE (PROPOSED) · D-52**
>
> 1. **Copy, do not move.** The source disk remains the source until a verified copy exists in two
>    locations
> 2. **Verify the copy** — file count and total size at minimum, a checksum comparison where the
>    tooling allows
> 3. **Confirm the `.mxdb` opens.** Importing into a scratch TBC project is the definitive test
> 4. **Confirm `POS_1/raw/` is present and non-empty.** Without it there is no post-processed
>    trajectory and the mission is NAV-only *(Technical Manual §17.2)*
> 5. **Confirm base station data** is present if a local base was occupied
> 6. **Only then** is the source disk available for reuse

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

## 11.3 Backup before processing

> **PARAMETRIX PROCEDURE (PROPOSED) · D-52**
>
> **The raw-data backup is taken before any processing begins**, not after.
>
> Processing writes into the project and, with **Backup SBET Next to MXDB** enabled (§13.2), into
> the raw data folder alongside the `.mxdb`. A backup taken after processing has begun is a backup
> of a partly processed state — usually fine, and occasionally exactly the wrong thing to have.

## 11.4 Structure, naming and location

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> **Folder structure, naming convention and storage location.**

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Two constraints are proposed as non-discretionary whatever else D-53 decides: the project record
> **should not** live on a processor's local machine (§3.3), and raw mission data **should** be
> distinguishable from processed products without opening them.

## 11.5 Chain of custody

> **PARAMETRIX DECISION REQUIRED · D-54**
>
> **Is a chain-of-custody record required?** For most survey work the answer is probably no. For
> work that may be used in a dispute, a claim or a proceeding, it is a different question, and it
> has to be decided **before** the data is collected rather than when it is asked for.

## 11.6 Records this section requires

| Record | State |
|---|---|
| Offload performed, verified how, by whom, when | **D-52** |
| Location of the raw-data backup | **D-52, D-55** |
| Custody, where required | **D-54** |

---

# 12. Office Intake Requirements

## 12.1 The principle

Everything checked at intake is cheap; everything discovered later is not. Intake is also the last
point at which re-collection is still a small decision.

## 12.2 What is verified at import

> **PARAMETRIX PROCEDURE (PROPOSED) · D-18**
>
> Before any processing:
>
> | # | Check | Why |
> |---|---|---|
> | 1 | **Project coordinate system** matches the control network and the client requirement | Changing it afterwards is irreversible in practice (§6.2, W-05) |
> | 2 | **Covered distance** is consistent with the field record | |
> | 3 | **Run count** matches the field record | Fewer runs than the crew logged means data was lost in transfer |
> | 4 | **The active trajectory** is the intended one, and is **SBET rather than NAV** unless there is a recorded reason | *(Technical Manual §17.2)* |
> | 5 | **Capture Devices** lists the sensors expected for the configuration | A missing camera or laser means a sensor was disabled or failed in the field (§9.1) |
> | 6 | **Base station data** is present if the trajectory will be processed in house | |
> | 7 | **The calibration state the mission was collected under is recorded** | See §12.3 |
>
> Seven checks, none taking more than a minute.

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

## 12.3 Capture the calibration state

`Extcal.json` travels with the raw mission data, and the **Mission Report** carries per-sensor
boresight and lever-arm calibration **with a date of calibration** *(TBC 24868)*.

> **That dated calibration record is the only one found anywhere in the workflow**
> *(Technical Manual §30)*. It is captured at intake because a later Cleanup can remove the
> objects that would have produced it (§18).

## 12.4 What intake does not do

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Intake should not correct anything.** If a check fails, it is recorded and raised (§22).

A processor who quietly fixes a coordinate system mismatch at intake has removed the evidence that
the field and office disagreed — which is the reason the practice is proposed, and the reason it
matters more than it looks.

## 12.5 Records this section requires

| Record | State |
|---|---|
| Intake checks performed, by whom, with the result of each | **D-18** |
| Calibration state at collection — `Extcal.json` and the Mission Report | **D-55** |
| Any intake check that failed, and what was done | **D-18, §22** |

---

# 13. Processing Requirements

**What shall be done, not how.** The method is in the Office How To; the explanation is in the
Technical Manual §§17–21.

## 13.1 Trajectory

| # | Requirement | State |
|---|---|---|
| 1 | Survey deliverables are produced from a **post-processed SBET**, not the real-time NAV solution. Where NAV is used, the reason is recorded and the deliverable is qualified | **PROPOSED** |
| 2 | The **antenna model** is confirmed before computing. The MX60 requires **Trimble 112735** | **PROPOSED** |
| 3 | The frame and epoch the trajectory was computed in is recorded | **PROPOSED · D-55** |

> **IMPORTANT**
>
> The antenna model is read automatically from the RINEX, which means it can be read **wrongly**.
> An incorrect model introduces a **systematic antenna-height and reference error** into the
> trajectory *(TBC 25943; Technical Manual §17.3)*. It is one field nobody looks at, upstream of
> everything.

> **PARAMETRIX DECISION REQUIRED · D-10 · P1 · blocks operation**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?** Without it,
> trajectory processing inside TBC and the PFIX route are both unavailable, which removes one of
> the three degraded-GNSS remedies *(Technical Manual §10.3, §27)*.

> **PARAMETRIX DECISION REQUIRED · D-19**
>
> Computation mode — Single Base or PP-RTX. Stated at §6.2 because it is a project-setup decision
> as much as a processing one.

> **PARAMETRIX DECISION REQUIRED · D-11**
>
> **Is LiDAR QC a capability Parametrix intends to have?** It is the only degraded-GNSS remedy
> needing neither a POSPac licence nor additional control, and it needs a workstation with 128 GB
> of RAM at minimum *(Technical Manual §11.1)*. The answer is a procurement decision, not a
> processing one.

> **TESTING REQUIRED · T11, T12, T13**
>
> Three trajectory-processing defaults are untested against Parametrix conditions: the **Multipath**
> default of Medium on open-sky corridors, the **DMI scale factor standard deviation** default of
> 5 % where the wheel may never have been measured, and the **LiDAR QC** range and laser defaults.
> Trimble's own guidance beside the LiDAR QC laser setting contradicts its default
> *(Technical Manual §11.3)*.

## 13.2 Preserve what records the trajectory

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Enable Backup SBET Next to MXDB.** That log is the only artefact found anywhere in the workflow
> that records the frame and epoch a trajectory was computed in, and it lives with the raw data
> rather than inside a TBC project that may later be cleaned up (§18) or lost.

## 13.3 Scan generation

| # | Requirement | State |
|---|---|---|
| 1 | **The filters applied are recorded.** Filter choice is a defensible-or-not decision a reviewer may need to see years later | **PROPOSED · D-55** |
| 2 | Colorization is applied or not applied by decision, not by default | **PARAMETRIX DECISION REQUIRED — D-22** |

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Capture the Results of Scan Generation into the project record.** It is the only artefact that
> states which filters produced a given cloud.

> **TESTING REQUIRED · T1, T3**
>
> Filter defaults are untested. **T3 in particular:** whether the **Reflective Panels** filter
> removes legitimate retro-reflective returns from signs and line marking — on sign and
> retroreflectivity work, those returns are the deliverable *(Technical Manual §18.3)*.

## 13.4 Registration

**Registration has its own section: §14.** It is not a processing step like the others — it is the
step that decides whether the deliverable sits where it is supposed to, and it carries its own
authority, designation, command-selection and record requirements.

## 13.5 Records this section requires

| Record | State |
|---|---|
| Trajectory processing settings, and the frame and epoch log | **D-55** |
| Results of Scan Generation | **D-55** |

*Registration records are §14.10.*

---

# 14. Registration Requirements

Registration is the step that decides whether the deliverable sits where it is supposed to. It is
also the step with the most ways to produce a confident, defensible-looking, wrong result — which
is why it has a section of its own rather than a subsection of processing.

**This section states what is required.** The three commands and their click sequences are the
**Office How To §§16–21**; why registration behaves as it does is **Technical Manual §21**.

## 14.1 When registration is required

| | State |
|---|---|
| A dataset that will be **measured from, delivered, or relied on** is registered to surveyed control | **PARAMETRIX DECISION REQUIRED — D-12, D-16** |
| A dataset used only to look at, internally, may not need it | **PARAMETRIX DECISION REQUIRED — D-13** (§17.2) |

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Registration to surveyed control **should** be performed on every dataset for which an accuracy
> statement will be issued. A trajectory that has never been fitted to control has no independent
> evidence of its absolute position at all — the processing was internally consistent and nothing
> more *(Technical Manual §8.5)*.

## 14.2 Authority

> **PARAMETRIX DECISION REQUIRED · D-3 · P1 · blocks formal acceptance**
>
> **Who may perform a registration, and who may accept one?** Proposed at §4.2: performed by the
> Processor, reviewed by the Project Surveyor.

> **PARAMETRIX PROCEDURE (PROPOSED) · D-15, D-3**
>
> **The person who designates control versus independent check should not be the person who
> computes the registration** (§4.3). Where one person must do both on a small job, the designation
> is recorded **before** the registration is computed, and is not changed afterwards.

## 14.3 Control and independent check designation

The requirement is §7.3 and is not restated here. Two consequences belong to registration:

| | State |
|---|---|
| The designation is **fixed before** registration begins | **PROPOSED — D-15** |
| A point's **As Check** state is **not changed during** processing. If a designation was wrong, it is changed by the person with the authority, recorded, and the registration recomputed from the imported trajectory | **PROPOSED — D-15** |

> **The failure this prevents.** A processor registers, finds one check point with a larger
> residual than expected, and adds it to the adjustment to bring it in. Every step is well
> intentioned. The result is an adjustment with no independent check at all, and a set of residuals
> that now measure nothing *(Technical Manual §22.4)*.

## 14.4 Command selection

Three commands perform registration and they are not interchangeable *(Technical Manual §21)*.

| Command | Uses surveyed control? | Scope |
|---|---|---|
| **Register a Run** | Yes | One run |
| **Register a Mission** | Yes — **each GCP reusable across runs** | A set of runs |
| **Register Run to Run** | **No — cloud-to-cloud against a fixed Reference Run** | A pair, batched |

> **PARAMETRIX DECISION REQUIRED · D-12**
>
> **Is Register a Mission the corridor default**, with Register a Run reserved for single-run cases
> and for repairing one run in an otherwise accepted mission? **And where does run-to-run sit?**
>
> The decision also has to say what happens to a mission registration when one run is later
> re-collected.

> **TESTING REQUIRED · T15, T9, T24**
>
> Which registration **type** — Global, Local, Global-then-Local — and when; whether Target-Bundle
> Adjustment should be checked; and how much run overlap run-to-run actually needs. No selection
> rule is published for any of the three.

## 14.5 Use of surveyed control

> **TRIMBLE REQUIREMENT** — *binding now, on Trimble's authority*
>
> A **Local** registration does not adjust beyond the outermost control point, and nothing
> indicates where the adjustment stopped. Data outside that bracket **shall not** be described as
> registered to the control (§7.2, **W-08**).

> **PARAMETRIX PROCEDURE (PROPOSED) · D-56**
>
> Control **should** bracket the extent to be delivered. The limitation is Trimble's; the control
> design rule that follows from it is this project's proposal, not a manufacturer instruction
> (§7.2).

> **TRIMBLE REQUIREMENT** — *an enforced software limit, not advice*
>
> A GCP and its picked target **shall not** be more than **30 m** apart. TBC rejects the pair
> beyond that distance — the limit cannot be exceeded, only worked around *(TBC 22905)*.

## 14.6 Run-to-run — what it cannot do

> **PARAMETRIX PROCEDURE (PROPOSED) · D-12**
>
> Run-to-run registration improves **relative** agreement between passes. It uses no surveyed
> control and cannot establish absolute position. It **should** therefore be used only in this
> order:
>
> 1. Register to surveyed control first
> 2. Assess against independent check points and visually (§16)
> 3. **Only then**, if overlapping passes still disagree, use run-to-run — choosing as **Reference
>    Run** the pass with the better GNSS conditions and the better residuals against control
> 4. **Re-check against the independent check points afterwards**, because the Run to Adjust has
>    moved
>
> **Step 4 is the one that gets skipped**, and it is why the sequence matters: adjusting one run to
> match another changes its residuals against control, and if the Reference Run was itself
> displaced, run-to-run propagates that displacement faithfully into the run you adjusted.

## 14.7 Re-registration, Edit and Reset

> **CAUTION · W-07**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

> **PARAMETRIX PROCEDURE (PROPOSED) · D-12**
>
> A registration that needs changing **should** be recomputed from the **imported** trajectory
> using **Edit**, never layered on a previous result.

> **CAUTION · W-06**
>
> Picked targets are written to **`Targets.csv`** when Registration Auto-Saving is on. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

> **TESTING REQUIRED · T7** — whether Registration Auto-Saving is on by default.

## 14.8 Update Scans

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **PARAMETRIX PROCEDURE (PROPOSED) · D-36**
>
> **Update Scans should be run before a registration result is inspected, accepted or exported.**
> The confirmation that it was run is the export gate at §19.2.

## 14.9 Review after registration

| # | | State |
|---|---|---|
| 1 | Residuals on **independent check points** are read and recorded, by component | **PROPOSED — D-29** |
| 2 | The **visual check** is performed against the registered cloud, not the unregistered one | **PROPOSED — D-27** (§16.5) |
| 3 | Where run-to-run was used, check points are re-read **after** it | **PROPOSED — D-12** (§14.6) |

> **TRIMBLE REQUIREMENT**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> A registration **shall not** be judged on its residuals alone. The visual check is Trimble's
> instruction and does not wait on a Parametrix decision.

## 14.10 Records this section requires

| Record | State |
|---|---|
| Registration name, type, and the runs included | **D-29** |
| The trajectory node produced, and its SBET filename **with its `_reg_####` number** | **D-29** |
| **Control and check designation, with the residual on each point, by component** | **D-29** — *no software artefact exists* |
| Confirmation that **Update Scans** was run | **D-36** |
| `Targets.csv`, archived | **D-55** |
| That the visual check was performed, by whom, over what extent | **D-27** — *no software artefact exists* |

## 14.11 Acceptance of a registration

A registration is **accepted** under §17, against the project's stated accuracy requirement, by the
person with the authority under §4. **Acceptance is not the registrant's** (§17.5).

> **PARAMETRIX DECISION REQUIRED · D-13 · P1**
>
> **What constitutes an acceptable registration is not established** (§17.2). Until it is,
> acceptance rests on documented professional judgement supported by the evidence above — and the
> decision at §17.2 is whether that is permitted at all.

---

# 15. Calibration Control

## 15.1 What calibration is, in one line

TBC's laser scanner calibration estimates the **angular** offsets between sensors. Lever arms are
**measured, not estimated** *(Technical Manual §7.6, §20.2)*. A wrong lever arm cannot be
calibrated out, because the adjustment has no parameter for it.

An angular error acts through range: the same error is ten times larger at 100 m than at 10 m
*(Technical Manual §3.1)*.

## 15.2 Currency

> **PARAMETRIX DECISION REQUIRED · D-26 · P1**
>
> **What is the recalibration interval, and what triggers a recalibration outside it?**
>
> The specific question that has to be answered explicitly: **does daily removal and refitting of
> the Sensor Unit count as disturbing the calibration?** If the unit comes off the vehicle between
> jobs, the answer determines whether calibration is an annual event or a per-mobilisation one.

> **PARAMETRIX PROCEDURE (PROPOSED) · D-26**
>
> **No mission should be processed against a calibration whose currency cannot be established.**

The calibration state in force is captured at intake (§12.3), which is what makes this checkable.
The proposal is not controversial; what makes it undecided is that **the interval it would be
checked against does not exist yet.**

## 15.3 The calibration site

> **PARAMETRIX DECISION REQUIRED · D-24**
>
> **Where is the calibration site, and who maintains it?**

Trimble specifies the geometry, and two different procedures need compatible sites:

| | Requirement | Source |
|---|---|---|
| **Laser scanner calibration** | Two streets crossing at **90° ± 30°**, at least **20 m** usable on each side and ideally **80 m** total, façades in each direction, little vegetation | TBC 24886 |
| **LiDAR QC** | Two perpendicular strips, each **250–300 m**, each driven in both directions; structured scene; open sky | TBC 28972 |

> **PARAMETRIX PROCEDURE (PROPOSED) · D-24**
>
> **Establish one site that satisfies both** — two streets crossing near 90°, façades on all four
> approaches, little vegetation, **125–150 m of usable street on each arm**, open sky, drivable in
> both directions without traffic-control complications.
>
> The two requirements are compatible and the stricter one should govern. Establishing such a site
> is real work — reconnaissance, a traffic plan, possibly permission — and doing it once, well,
> before it is needed under schedule pressure is worth more than the procedure it supports.

## 15.4 Judging a calibration

> **CAUTION**
>
> Trimble states, in identical words in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

> **TRIMBLE REQUIREMENT** — *binding now.* Trimble does not recommend the visual check; it states
> that one **is needed**, in identical words in two topics.
>
> **A calibration shall not be accepted on RMS alone.** The visual check is part of the acceptance,
> not an optional extra *(Technical Manual §23.1, §25)*.

## 15.5 The calibration record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Export the calibration JSON after every calibration and archive it outside the TBC project**,
> named with the system serial number and the calibration date.
>
> It is the complete calibration state of the system in one small file, it can be imported into any
> subsequent project, and it is the only portable record of what the system's angles were on a
> given date. Cleanup (§18) or a lost workstation should not take it with them.

## 15.6 Periodic system verification

Distinct from per-project QC: the check that the **instrument** is still performing.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, p.7)*
>
> Scan approximately **eight flat retro-reflecting targets** at varied distances over more than
> **180° horizontally**, previously surveyed by total station. The system passes if residuals fall
> within the specified accuracy. Trimble recommends doing this "regularly" and "especially before
> starting an extensive data acquisition campaign" — and **gives no interval**.

> **PARAMETRIX DECISION REQUIRED · D-28**
>
> **Is this the periodic verification Parametrix adopts, and at what interval?**

> **TESTING REQUIRED · V-14**
>
> Whether Trimble or the dealer expects this check specifically, and at what period.

## 15.7 Records this section requires

| Record | State |
|---|---|
| Calibration performed — date, site, who, and the result including the visual check | **D-26** |
| The calibration JSON, archived outside the project | **D-55** |
| Which calibration each mission was processed against | **D-55** |
| Periodic verification, when performed | **D-28** |

---

# 16. Quality Control Requirements

## 16.1 The principle this section rests on

> **CAUTION**
>
> Trimble states, in identical words in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

**A number can prove failure. A number cannot prove success.** Only two things can suggest success:
observations that took no part in the adjustment, and looking at the data
*(Technical Manual §23)*.

Everything in this section follows from that, and it is why QC here is **layered** rather than a
single test. A residual measures how well an adjustment fitted the observations it was given. That
is a narrower question than the one that matters.

## 16.2 The layers

Each layer catches something the others cannot. **None of them is optional because another was
performed.**

| # | Layer | Catches | Artefact |
|---|---|---|---|
| 1 | **Field coverage verification** (§10.2) | Missing passes, missing overlap | Field record |
| 2 | **Intake checks** (§12.2) | Transfer loss, wrong CRS, missing sensors | Intake record |
| 3 | **Trajectory RMS review** | Where the solution was weak — **before any point cloud exists** | Screen capture |
| 4 | **Residuals on control** | A broken adjustment | Targets pane |
| 5 | **Residuals on independent check points** | An adjustment that fits its own observations and is still wrong | **Recorded manually** |
| 6 | **Visual inspection of the point cloud** | Doubled surfaces, thickening at range, systematic tilt | **No software artefact** |
| 7 | **Imagery inspection** | Coverage gaps, exposure, blur, corrupted images | **No software artefact** |
| 8 | **Export-state confirmation** (§19.2) | Delivering the unregistered cloud | Screen capture |

> **Two of the eight layers produce no software artefact at all.** If a reviewer asks whether the
> visual check was performed and over what extent, the only possible answer is a record somebody
> wrote.

## 16.3 Trajectory RMS review

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **The trajectory should be reviewed in RMS colouring before the point cloud is inspected.**

It is available before any point cloud exists, it costs seconds, and it says where the solution
degraded, for how long, and whether the degradation is at the ends of the mission
*(Technical Manual §24)*. That determines where to look in every later layer.

## 16.4 Residuals

| | |
|---|---|
| Residuals on **control** points used in the adjustment are recorded, by component | |
| Residuals on **independent check points** are recorded, by component | These are the ones that mean something (§7.3) |
| **Which points were control and which were checks is recorded manually** | **TBC does not report it** *(Technical Manual §22.7)* |

> **TESTING REQUIRED · T21, V-11**
>
> TBC 2025.21 states that signed residuals are "included in the report" without naming it, and the
> only mobile mapping report topic does not mention residuals. **Whether the residuals can be
> produced as a report, or must be transcribed by hand, determines how this record is kept.**
> Answerable in ten minutes with the software open.

## 16.5 Visual inspection

> **PARAMETRIX PROCEDURE (PROPOSED) · D-27**
>
> A visual QC pass over a registered mission covers:
>
> | Check | Looking for |
> |---|---|
> | **Overlapping passes in Cutting Plane View**, dragged the full length | Doubled surfaces |
> | **Flat surfaces at range** — a wall, a building face | Thickening with distance: attitude error or a calibration issue |
> | **The ends of the corridor** | Where a Local adjustment stopped; where the smoother was weakest |
> | **The degraded stretches identified at layer 3** | Whether the registration actually fixed them |
> | **Vertical surfaces against horizontal** | Systematic tilt |
> | **Features near control versus far from control** | Residual growth with distance from constraint |

> **IMPORTANT**
>
> **Set the rendering to Scan Color for this.** Without it, two offset surfaces read as one thick
> one and the defect the check exists to find is invisible *(Technical Manual §25)*.

> **TESTING REQUIRED · T16**
>
> The working cutting-plane thickness for these checks.

> **The constraint the decision has to satisfy.** Mobile mapping error is **localised** — it
> arrives in stretches, not as scatter *(Technical Manual §3.2)*. **An inspection strategy must
> therefore be capable of finding localised degradation, which means traversing the corridor rather
> than sampling it.** A sampling scheme that inspects ten places will find a problem that affects
> the whole job and miss the one that affects 300 m.

> **PARAMETRIX DECISION REQUIRED · D-39**
>
> **The corridor continuity inspection method and its coverage** — how much of a corridor is
> inspected, and how that is decided.

## 16.6 Imagery inspection

> **PARAMETRIX PROCEDURE (PROPOSED) · D-27**
>
> | Check | Looking for |
> |---|---|
> | **Coverage** | Gaps where a camera stopped, or a run was not colorized |
> | **Exposure** | Blown highlights, blocked shadows under canopy and in underpasses — both unrecoverable |
> | **Motion blur** | Speed too high for the light available |
> | **Obstruction** | Aerials, a following vehicle, a smear on the dome |
> | **Focus and contamination** | Rain, dust, insects on the optical surface |
> | **Corrupted images** | **These are silent** — a corrupted side camera image exports as black |
> | **Alignment with the point cloud** | Colour in the wrong place at feature edges indicates a camera boresight issue |

> **PARAMETRIX DECISION REQUIRED · D-31**
>
> Whether the proposed **file-size scan** for detecting silently corrupted imagery is adopted. It is
> a screening method proposed by this project and **not validated** *(Technical Manual §26)*.

## 16.7 What QC does not do

> **TRIMBLE REQUIREMENT** — *the visual check is Trimble's instruction, not ours*
>
> Good residuals **shall not** be treated as removing the need for visual inspection. Trimble does
> not recommend the check; it states that one **is needed**, and says so in identical words in two
> topics (§16.1).

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> More generally, **a QC layer should not be substituted by another.** Each catches something the
> others cannot, and which layers Parametrix requires is **D-27** and **D-39**.

## 16.8 Records this section requires

> **PARAMETRIX PROCEDURE (PROPOSED) · D-29**
>
> For each registered mission:
>
> | Record | Source |
> |---|---|
> | Residuals on control points used, by component | Targets pane |
> | Residuals on independent check points, by component | Same |
> | **Which points were control and which were checks** | **Manual — TBC does not report it** |
> | Run-to-run RMS statistics, if used | Results tab |
> | Trajectory RMS picture | Screen capture |
> | **Visual check performed, by whom, covering what extent** | **No software artefact exists** |
> | **Imagery check performed, by whom** | **No software artefact exists** |
> | Results of Scan Generation | §13.3 |
> | Mission Report | §18.3 |

---

# 17. Acceptance and Approval

## 17.1 What acceptance is

**Acceptance is the point at which the data becomes the deliverable.** It is a decision by a named
person, recorded, that a dataset meets the project's stated accuracy requirement (§6.1).

Acceptance is always **against a requirement**. A dataset is not accepted because it looks good, or
because the residuals are small, or because the schedule has run out.

## 17.2 The criterion is not established — and the decision that follows from it

> **PARAMETRIX DECISION REQUIRED · D-13 · P1 · blocks formal acceptance**
>
> **What constitutes an acceptable registration, and an acceptable point cloud?**
>
> **This SOP states no numerical acceptance tolerance, and one has not been invented.**

### What is established

| | |
|---|---|
| Trimble publishes **no acceptance tolerance** for the MX60 | Its published figures are **instrument performance under stated conditions**, which is not a project acceptance criterion |
| Trimble publishes **no attitude error budget** for the point cloud | A useful range for a given tolerance therefore cannot be calculated from the documentation *(Technical Manual §16.5)* |
| **A good RMS does not prove success** | Trimble states it twice, in identical words. Only observations held out of the adjustment, and looking at the data, can suggest success *(Technical Manual §23)* |
| The relationship between achieved accuracy and GNSS conditions on this system **has not been tested** | **T31** |
| Which features are fit for horizontal or vertical control at MX60 density **has not been tested** | **T25** |

> **A number here would be worse than the gap.** An invented tolerance would be quoted, relied on
> and eventually defended, and there would be nothing behind it. The gap is visible; a fabricated
> threshold would not be.

### The decision Parametrix has to make

The absence of a general standard does not by itself say whether work may proceed. **That is a
separate question, and it is the one that is actually blocking:**

> ### Until a general Parametrix acceptance standard exists, may MX60 work be accepted against a **project-specific written accuracy requirement**, using independent check evidence, visual QC and documented professional judgement?

| | Outcome | What it means in practice |
|---|---|---|
| **A** | **No.** | MX60 survey-grade delivery is **blocked** until a corporate acceptance framework is adopted. The system may still be used for work where no accuracy claim is made |
| **B** | **Yes, project by project.** | Interim acceptance is permitted where the accuracy requirement is **stated in writing before collection** and the acceptance evidence at §17.3 is documented. Each acceptance stands on its own project record, not on a company standard |
| **C** | **Another Parametrix-approved interim framework.** | For example a tiered scheme, an approver-limited scheme, or acceptance restricted to named clients or work types |

> **This SOP does not choose between A, B and C, and no other document in the set implies a
> choice.** The decision is Parametrix's, it is recorded in Appendix A, and it changes §17.3 from
> proposed to adopted the day it is made.

### What is true under every outcome

**D-13 blocks formal acceptance, and nothing else.** Stated as plainly as it can be:

| With D-13 open | |
|---|---|
| **Collecting data** | **Permitted.** Nothing in D-13 touches field operation |
| **Processing, registering and inspecting it** | **Permitted.** Including exploratory and trial processing, and processing to learn the system |
| **Testing the system against known control** | **Permitted, and needed** — several register items (T25, T31) cannot close without it |
| **Delivering data with no accuracy claim attached** | **Permitted**, where the deliverable says so |
| **Formal acceptance under §17.1** | **Blocked** |
| **An accuracy claim resting on a Parametrix standard** | **Blocked**, because no such standard exists to rest on |

**Nor does this SOP authorise an accuracy statement.** It is a draft, no Parametrix requirement in
it is adopted (§2.4), and it sets no tolerance. A person may still sign an accuracy statement for
MX60 work — but they sign it on their own professional judgement and the project's own evidence,
not on the authority of this document.

> **Whoever signs an accuracy statement today is signing on their own professional judgement,
> supported by the evidence in §16 — not on a Parametrix standard, because there is not one.**
> That should be understood by the person signing and by whoever receives it.

## 17.3 What acceptance requires regardless

Even without D-13, five things are required before a dataset is accepted. These are structural and
do not depend on the number.

| # | Requirement | State |
|---|---|---|
| 1 | The project's **accuracy requirement is stated in writing** (§6.1) | **PROPOSED — D-13** |
| 2 | **Independent check points exist**, were designated before registration, and took no part in any adjustment (§7.3) | **PROPOSED — D-15** |
| 3 | **Residuals on those check points are recorded**, by component (§16.4) | **PROPOSED — D-29** |
| 4 | **The visual inspection was performed and recorded** (§16.5) | **PROPOSED — D-27** |
| 5 | **Update Scans was run**, and the accepted cloud is the registered one (§13.4) | **PROPOSED — D-36** |

> **Requirement 2 is the one that cannot be recovered afterwards.** If no point was held out, the
> dataset cannot be checked later without re-surveying, because every point it might be checked
> against helped produce it.

## 17.4 What acceptance does not rest on

| | Why |
|---|---|
| **RMS alone** | **TRIMBLE REQUIREMENT** — a visual check is needed. Trimble says so twice, in identical words (§16.1) |
| **Residuals on control points used in the adjustment** | They measure the fit of the adjustment to observations it was given |
| **A clean-looking point cloud** | Mobile mapping data does not look wrong when it is wrong *(Technical Manual §3.2)* |
| **Agreement between two passes** | Two passes can agree with each other and both be displaced, if the trajectory was drifting through the stretch |

## 17.5 Who accepts

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Who may accept a registration, and who signs an accuracy statement. Proposed at §4.2: the
> Project Surveyor, and not the person who computed the registration.

## 17.6 The accuracy statement

An accuracy statement issued to a client states:

| | |
|---|---|
| The accuracy requirement it was assessed against | |
| **The evidence** — residuals on independent check points, by component | |
| **The basis of the check** — how many points, where, in which GNSS environments | |
| The extent it applies to | Accuracy is not uniform along a corridor *(Technical Manual §3)* |
| Any segment excluded, and why | §8.6, §22 |

> **Accuracy varies along the corridor.** A single figure for a whole corridor implies a uniformity
> the method does not have. Where the statement is a single figure, the extent and the conditions
> it applies to are stated with it.

## 17.7 Records this section requires

| Record | State |
|---|---|
| Acceptance decision — dataset, by whom, date, against what requirement | **D-3, D-13** |
| The evidence the decision rested on | **D-29** |
| The accuracy statement issued | **D-29** |

---

# 18. Destructive Operation Controls

## 18.1 What this section governs

An operation that removes data or history and cannot be undone within the software. In the MX60
workflow, one command is in this class.

> **CAUTION · W-01**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

Clearing a data disk before a verified copy exists (§11.2) and deleting raw mission data (§21) are
destructive in the same sense, and are governed by the same principle: **authorisation, and the
record made before the act, not after.**

## 18.2 Authorisation

> **PARAMETRIX DECISION REQUIRED · D-35 · P1 · blocks operation**
>
> **When may Cleanup be performed, by whom, and what must be archived first?**

> **PARAMETRIX PROCEDURE (PROPOSED) · D-3, D-35**
>
> **Cleanup should not be run without written authorisation** from the person with the authority
> under §4 — proposed there as the Project Surveyor. "In writing" carries the meaning in §3.3.
>
> **The verb is *should* because the authority does not exist yet.** D-35 blocks this operation:
> until Parametrix names who may authorise a Cleanup, there is nobody for the clause to name.

## 18.3 What is archived first

> **PARAMETRIX PROCEDURE (PROPOSED) · D-35**
>
> A sequence in which Cleanup destroys nothing that matters:
>
> | # | Step | Why in this order |
> |---|---|---|
> | 1 | **Complete and accept QC** (§16, §17) | Cleanup is an end-of-preparation step. Running it before acceptance removes the alternatives you might need to go back to |
> | 2 | **Run the Mission Report and archive it** | It records capture devices, runs, trajectories, generated scans, and per-sensor calibration with date *(TBC 23991_1, 24868)*. **Run it before Cleanup** — afterwards it can only report what survives |
> | 3 | **Record the registration evidence** (§16.8) | Control/check designation and residuals. TBC does not appear to report these |
> | 4 | **Archive `Targets.csv`** *(TBC 22905)* | The picked registration observations — the registration's field book, and not recoverable |
> | 5 | **Archive the numbered SBET files** `sbet_<date>_reg_####.out` | Pending **T28**, assume Cleanup removes them |
> | 6 | **Archive the calibration JSON** (§15.5) | The system state the mission was processed under |
> | 7 | **Take the project backup Trimble asks for**, to a location that is part of the project archive (§21) | A backup nobody can find is not a backup. Not a local copy on the processor's machine |
> | 8 | **Obtain the authorisation** §18.2 requires | |
> | 9 | **Run Cleanup** | |
> | 10 | **Record that it was run** — by whom, on what date, and what was archived first | Otherwise the absence of history is itself unexplained |
>
> Steps 2 to 6 are small files. The whole set is a few megabytes beside a project of tens of
> gigabytes, and they are the difference between a deliverable that can account for itself and one
> that cannot.

> **TESTING REQUIRED · T28**
>
> **Does Cleanup delete `sbet_*_reg_####.out` from storage, or only remove the project objects?**
> The answer determines what step 5 has to cover. Until it is known, assume the worse case.

## 18.4 Why this matters more here than elsewhere

Cleanup removes the evidence of how a deliverable was produced, and MX60 provenance is already the
hardest part of this workflow *(Technical Manual §30)*. A project that has been cleaned up can no
longer show which of several trajectories a delivered cloud was built on, because the alternatives
are gone along with the record of which one was chosen.

**That is not an argument against running Cleanup.** It is the argument for §18.3.

## 18.5 Records this section requires

| Record | State |
|---|---|
| Authorisation — who, when, for which mission | **D-35** |
| What was archived before, and where it is | **D-35, D-55** |
| That Cleanup was run, by whom, on what date | **D-35** |

---

# 19. Export and Delivery Controls

## 19.1 The release gate

**Export is the last point at which a mistake is still internal.** This section is a gate, not a
procedure: the method is in the Office How To.

## 19.2 Before any export

> **PARAMETRIX PROCEDURE (PROPOSED) · D-36**
>
> **Before any export from a registered mission, confirm in Project Explorer that the scan nodes
> selected for export sit beneath the intended registered trajectory, and that their stations carry
> the `_reg_####` suffix.**

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **PARAMETRIX DECISION REQUIRED · D-36 · P1**
>
> **Is the pre-export trajectory-node confirmation mandatory, and may export be performed without
> it?** This is the single cheapest control in the procedure and the one that prevents the most
> expensive failure.

> **TESTING REQUIRED · T29, T23**
>
> The reliable export-state verification method for each export path, and what happens when a
> Point Cloud tab selection is drawn across scans belonging to two different trajectories. Neither
> is documented.

## 19.3 Export timestamps

> **CAUTION · W-03**
>
> With **Export timestamps** set to **Yes**, Trimble states that *"the exported scans are
> **reprocessed from the raw data**"* rather than being the scans processed with Generate Scans
> *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated.** Until this is established, the
> exported data may not be the data that was registered and checked.

> **TESTING REQUIRED · T18 · the highest-priority test in the register**
>
> Export the same registered run twice, timestamps off and on, and compare point geometry.
>
> **TESTING REQUIRED · T18 — and an interim posture until it is answered**
>
> **An export with timestamps enabled should be treated as unverified** against the checked
> dataset, and the option **should not** be enabled on a delivered dataset without a recorded
> reason.
>
> This is an interim posture, not a Parametrix rule and not a Trimble one. It exists because
> Trimble documents a behaviour whose consequence it does not state, and it is withdrawn the day
> T18 is answered — in either direction.

## 19.4 What the delivery carries

| | Requirement | State |
|---|---|---|
| Grid or ground, as agreed (§6.3) | A ground-scaled export **does not record the scale factor it used**; a grid export writes a sidecar | **D-38** |
| The coordinate reference system, datum and epoch | Stated in the delivery, not only in the file | **D-38** |
| The delivery record (§20) | | **D-29** |
| The accuracy statement (§17.6) | Where accuracy is relied on | **D-13** |

> **PARAMETRIX DECISION REQUIRED · D-38**
>
> **Deliverable specification** — standard formats, which export path produces each, and the
> default scaling.

## 19.5 Provenance limitation, stated plainly

> **IMPORTANT**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**
>
> That is why the delivery record in §20 exists, and why it is not optional.

> **TESTING REQUIRED · T19, T22, T26, T30**
>
> Which trajectory travels with a publish or an export; what a LAS file actually carries in its
> header, VLRs and sidecar; whether exported imagery reflects a registration; and whether a
> delivered dataset can be matched back to its trajectory after the fact.

## 19.6 Imagery

> **PARAMETRIX DECISION REQUIRED · D-32 · P1**
>
> **What is Parametrix's position on imagery privacy?** Are unblurred originals retained, and for
> how long? Mobile mapping imagery captures faces, number plates and private property as a matter
> of course. **The decision is made before collection, not on request.**

## 19.7 Records this section requires

| Record | State |
|---|---|
| Export-state confirmation, before export | **D-36** |
| The delivery record — §20 | **D-29** |
| What was delivered, to whom, when, in what format and scaling | **D-38** |

---


---

# Part IV — Records, Retention and Departure

---


---

# 20. Documentation and Records

## 20.1 Why the record carries unusual weight here

In conventional survey work the observations are the record: field notes, raw files, an adjustment
report. In mobile mapping, several of the things that determine whether a deliverable is correct
**produce no software artefact at all**.

| Fact | Software artefact |
|---|---|
| Which points were control and which were independent checks | **None** — TBC does not report it *(Technical Manual §22.7)* |
| That the visual inspection was performed, and over what extent | **None** |
| That the imagery inspection was performed | **None** |
| The conditions at collection — occlusion, weather, traffic | **None** |
| Which trajectory a delivered cloud was built on | **Partial, and not conclusive** *(Technical Manual §30)* |

**Those five facts are either written down at the time or lost.**

## 20.2 The record package

> **PARAMETRIX DECISION REQUIRED · D-29 · P1**
>
> **What provenance record accompanies a deliverable, where does it live, and who produces it?**

> **PARAMETRIX PROCEDURE (PROPOSED) · D-29**
>
> A minimal package that closes the gap:
>
> | # | Artefact | Size |
> |---|---|---|
> | 1 | **A one-page delivery record** per dataset: mission ID, trajectory node name, SBET filename including its `_reg_####` number, registration type, export path and date, exported by whom | kB |
> | 2 | **The control and check table** — point ID, Use XY, Use Z, As Check, and the residual on each | kB |
> | 3 | **The Mission Report**, run **before** Cleanup (§18.3) | kB |
> | 4 | **The calibration JSON** in force (§15.5) | kB |
> | 5 | **`Targets.csv`** (§18.3) | kB |
> | 6 | **The field record** (§9.6) | kB |
> | 7 | **The QC record** (§16.8), including the two layers with no software artefact | kB |
>
> Seven artefacts. Five of them are small files that already exist; two are written by a person.
> **The whole package is a few hundred kilobytes.**

## 20.3 Where records live

**In the project record** (§3.3) — durable, not on a processor's local machine, and findable by
someone who was not involved.

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> Folder structure, naming and storage location (§11.4).

## 20.4 When they are made

**At the time.** A record reconstructed later is a reconstruction, and the facts most worth having
are exactly the ones that cannot be reconstructed.

## 20.5 Index of records this procedure requires

The full index, section by section, is **Appendix B**.

## 20.6 What a record is for

Not compliance. Three specific uses, each of which has happened to somebody:

| | |
|---|---|
| **A question about a deliverable, years later** | "Which trajectory was this built on, and what was it checked against?" |
| **A test result that changes what a past deliverable means** | **T18** and **T19** both have this shape. If either returns a result meaning a past export was not what it was believed to be, the record is what identifies which deliverables are affected |
| **Improving the work** | The relationship between GNSS conditions, control density and achieved accuracy on Parametrix corridors is not published anywhere and cannot be, because it is specific to this system and these roads. It can only be learned from a record of what was done and what came out |

## 20.7 Records this section requires

| Record | State |
|---|---|
| The delivery record, per §20.2 | **D-29** |
| The control and check table, with residuals | **D-29** |
| Where the record package lives for a given project | **D-53** |

---

# 21. Retention and Archive

## 21.1 What has to survive, and for how long

> **PARAMETRIX DECISION REQUIRED · D-55 · P1**
>
> **What is retained, where, for how long, and by whom?**

The decision is genuinely a decision — storage cost against the ability to reprocess — but it
divides cleanly, because the artefacts fall into three tiers of very different size.

## 21.2 The three tiers

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**

### Tier 1 — small, irreplaceable, and the basis of any later defence

| Artefact | Size |
|---|---|
| Field record | kB |
| Control and check designation table, with residuals | kB |
| Mission Report, run **before** Cleanup | kB |
| Calibration JSON in force at processing | kB |
| Results of Scan Generation | kB |
| Delivery record (§20.2) | kB |
| QC record (§16.8) | kB |
| The accuracy statement issued to the client | kB |

> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against
> retaining it indefinitely, and every one of these is unrecoverable.

### Tier 2 — retained for a defined period

| Artefact | Size |
|---|---|
| SBET, its processing report, and the frame and epoch log | MB |
| Numbered registered SBETs `sbet_*_reg_####.out` | MB |
| `Targets.csv` | kB |
| Base station data | MB |
| The delivered files | GB |

### Tier 3 — retained per the decision

| Artefact | Size | Note |
|---|---|---|
| **Raw mission folder** | **Tens to hundreds of GB** | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved — only re-collected |
| TBC project | Tens to hundreds of GB | The provenance record *(Technical Manual §30)* |

> **The Tier 3 decision is the expensive one and it is a real trade.** Keeping raw data means a
> better trajectory later is possible — from better base data, a POSPac upgrade, or LiDAR QC.
> Discarding it means the deliverable is final in a way it need not have been.

## 21.3 What is not discarded on one person's judgement

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **`POS_1/raw/` and `Targets.csv` should not be deleted by an individual acting alone.**

Both are irreplaceable, and the reason is a fact about the data rather than a policy: one cannot be
recomputed from anything, and the other was picked by a person and would be different if picked
again *(Technical Manual §5.4)*. **What the proposal needs from Parametrix is who else has to
agree**, which is part of D-55.

## 21.4 The archive record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> One page per project, in the archive, stating: what was archived, where, when and by whom; the
> retention tier applied; whether Cleanup was run and what was archived first; and where the raw
> mission data is, if it is held elsewhere.
>
> **Without it, the archive is a folder somebody has to reverse-engineer.**

## 21.5 Records this section requires

| Record | State |
|---|---|
| The archive record | **D-55** |
| Retention tier applied, and the date the period runs from | **D-55** |
| Disposal, where it occurs — what, when, authorised by whom | **D-55** |

---

# 22. Non-conformance and Re-collection

## 22.1 What counts

A non-conformance is a departure from a **shall** in this procedure, or a dataset that does not
meet the project's accuracy requirement (§17).

It is not a non-conformance to be unable to meet a requirement that has not been adopted. At this
revision that covers most of this document, which is a reason to answer the decisions rather than a
reason to relax.

## 22.2 Raise it, do not absorb it

**Anyone who identifies a non-conformance raises it.** The person who finds it is frequently the
person who caused it, and the procedure is designed so that raising it is the normal thing to do.

> **A non-conformance that is fixed quietly leaves no trace that the workflow failed** — which
> means it will happen again, to somebody else, on a job where it costs more.

## 22.3 The two categories

| | |
|---|---|
| **Recoverable in the office** | Reprocess the trajectory, regenerate scans, re-register, re-export. Costs hours. **Requires that the raw data was retained** (§21) |
| **Recoverable only in the field** | Missing coverage, missing overlap, a mission with no closing sequence, a weak initialization. Costs a mobilisation |

The second category is why §10 exists: **the field stage is the only stage with no office remedy**
*(Technical Manual §5.5)*.

## 22.4 Re-collection

> **PARAMETRIX DECISION REQUIRED · D-3, D-34**
>
> **Who decides that a dataset is rejected and that re-collection is required, and who bears it?**
>
> The decision is uncomfortable and is therefore the one most likely to be deferred until it is
> more expensive. Naming the decision-maker in advance is most of the control.

## 22.5 When a segment cannot be served

Where a corridor segment produces an unacceptable trajectory and no remedy applies, the honest
finding is that **mobile mapping may not be the appropriate acquisition method for that segment**.

> **PARAMETRIX DECISION REQUIRED · D-34**
>
> The decision rule: who decides, against what, and what the client is told. The planning-stage
> counterpart is §8.6 — identifying such segments before mobilising is much cheaper than finding
> them afterwards.

## 22.6 When a test result changes what a past deliverable means

Two open tests have this shape: **T18** (whether exporting with timestamps substitutes reprocessed
data) and **T19** (which trajectory travels with an export or publish).

> **CAUTION**
>
> If either test returns a result meaning a past deliverable was not what it was believed to be,
> **that is not a documentation problem.** It is recorded in the Technical Manual Appendix F and
> escalated.
>
> **The decision about what a client is told is not the tester's to make**, and it is not specified
> here. Who it escalates to is part of **D-3**.

## 22.7 Records this section requires

| Record | State |
|---|---|
| The non-conformance — what, when, found by whom | **D-3** |
| Disposition — accepted with qualification, reprocessed, re-collected, or rejected | **D-3** |
| Where re-collection occurred, what changed | **D-3** |
| Any deliverable affected, and what was done about it | **D-29** |

---


---

# Appendices — Decisions, Records and Approval

---


---

# Appendix A — Parametrix Decision Register

**35 items.** Generated from `deliverables/_control/master-register.csv` on 2026-09-11. **Do not edit this file** — edit the register and re-run `tools/build-register-views.py`.

This appendix is the SOP's **view** of the project's single master register. It shows the questions
that are **Parametrix's to answer** — the ones no test and no vendor can settle. The questions
answerable by evidence are the Technical Manual's Appendix E, and are not repeated here.

| | Count |
|---|---|
| Decisions open | **35** |
| **Adopted** | **0** |
| Priority P1 | 20 |
| Blocking something | 9 |

> **CAUTION**
>
> **No decision has been adopted.**
> A clause in this SOP whose decision appears below as open is **not a Parametrix requirement**. It
> is a proposal from this project, and it may not be quoted to a client, a reviewer or a regulator
> as an existing Parametrix standard.

## A1 · The adoption record

A decision becomes binding when it appears here with an answer, a date and an approver — and when
the register is updated and the views regenerated. **Editing this appendix by hand does not adopt
anything**, because it is regenerated from the register.

| ID | Decision taken | Date | Approved by |
|---|---|---|---|
| — | *No decision has been adopted at this revision.* | — | — |


## A2 · Decisions that block something

9 of the 35 decisions block something. **"Blocking" is not one thing** —
an item that stops a crew leaving the yard and an item that stops a signature at the end are both
blockers, and treating them alike hides which have to be answered first.

**Nothing here blocks operating the MX60 or inspecting what it collects.** What these items prevent
is a defensible accuracy claim and a formal acceptance.

| ID | What is blocked | Decision | SOP § |
|---|---|---|---|
| **D-2** | delivery for a stated accuracy purpose | Which MX60 configuration is ours - Core, Pro or Premium? Are GAMS and DMI fitted? Which rack? | §6.4 |
| **D-10** | processing | Do we hold a POSPac MMS 8.6+ licence, and where is it installed? | §13.1 |
| **D-13** | formal acceptance | What constitutes an acceptable registration and an acceptable point cloud? | §14.11, §17.2 |
| **D-16** | delivery for a stated accuracy purpose | Control design - how many control points, at what spacing, how many independent checks, and does density vary with predicted GNSS conditions? | §7.4 |
| **D-19** | collection | IN-Fusion+ Single Base or PP-RTX? | §6.2, §13.1 |
| **D-21** | processing | Which datum and epoch do we work in, who sets it, who checks it? | §6.2 |
| **D-35** | one workflow branch | When may Cleanup be performed, by whom, and what must be archived first? | §18.2 |
| **D-41** | collection | How many passes, in what pattern, by roadway type? | §8.2 |
| **D-42** | collection | Base station strategy and maximum baseline? | §8.5 |

## A3 · The full register

### D-1 · Who owns this SOP, who approves revisions, on what review cycle? · SOP §1.6, §2.2

**P2** · open

**Why it matters.** TBC is on an annual release cycle and each release has changed mobile mapping behaviour

*Stage: document control · Documents: Manual; SOP; Field; Office*

### D-2 · Which MX60 configuration is ours - Core, Pro or Premium? Are GAMS and DMI fitted? Which rack? · SOP §6.4

**P1** · open · **blocks delivery for a stated accuracy purpose**

**Why it matters.** Panoramic imagery is 8192x4096 on Core and 12288x6144 on Pro/Premium. Changes every imagery and accuracy statement

**Evidence.** TBC 22501; TBC 23888; MX60 UG Rev B p.12

*Stage: system · Documents: Manual; SOP; Field; Office*

### D-3 · Roles and authorities - who may operate, register, accept a registration, run Cleanup, sign the accuracy statement, own calibration currency · SOP §4.2, §5.2, §5.4, §14.2, §17.5, §22.4

**P1** · open

**Why it matters.** The accepting person should not be the person who performed the adjustment

*Stage: all · Documents: Manual; SOP; Field*

### D-10 · Do we hold a POSPac MMS 8.6+ licence, and where is it installed? · SOP §13.1

**P1** · open · **blocks processing**

**Why it matters.** Determines whether trajectory processing and PFIX are available at all, and removes one of three degraded-GNSS remedies

**Evidence.** TBC 25943; TBC 24460

*Stage: trajectory processing · Documents: Manual; SOP; Office*

### D-11 · Is LiDAR QC a capability we intend to have? · SOP §13.1

**P2** · open

**Why it matters.** 128-256 GB RAM, dedicated SSDs, MATLAB Runtime. Urgent only when it is too late

**Evidence.** TBC 28972

*Stage: trajectory processing · Documents: Manual; SOP*

### D-12 · Registration command selection - is Register a Mission the corridor default, and where does run-to-run sit? · SOP §14.4

**P2** · open

**Why it matters.** The three commands are not interchangeable. Run-to-run uses no control and propagates the reference run absolute error

**Evidence.** TBC 22905; TBC 26473; TBC 25096

*Stage: registration · Documents: Manual; SOP; Office*

### D-13 · What constitutes an acceptable registration and an acceptable point cloud? · SOP §14.11, §17.2

**P1** · open · **blocks formal acceptance**

**Why it matters.** No Trimble source provides a threshold. Must combine residuals, independent checks, visual inspection and the project accuracy requirement

**Evidence.** TBC 24886; TBC 25096

*Stage: QC · Documents: Manual; SOP; Field; Office*

### D-15 · Is the control/check designation fixed before registration and unchangeable during it? · SOP §4.3

**P1** · open

**Why it matters.** Guards the failure that looks like diligence - a processor who dislikes a check residual and ticks the point into the adjustment

**Evidence.** TBC 22905

*Stage: registration · Documents: Manual; SOP; Office*

### D-16 · Control design - how many control points, at what spacing, how many independent checks, and does density vary with predicted GNSS conditions? · SOP §7.4

**P1** · open · **blocks delivery for a stated accuracy purpose**

**Why it matters.** No Trimble source states any. TBC minimum of one pair is a mathematical floor. Local does not extrapolate

**Evidence.** TBC 22905

*Stage: project setup · Documents: Manual; SOP*

### D-18 · What is verified at import, and by whom? · SOP §12.2

**P3** · open

**Why it matters.** Seven checks, each cheaper now than later

**Evidence.** TBC 22499

*Stage: intake · Documents: SOP; Office*

### D-19 · IN-Fusion+ Single Base or PP-RTX? · SOP §6.2, §13.1

**P1** · open · **blocks collection**

**Why it matters.** Determines whether a base station is occupied every mission, and the reference frame the solution is computed in

**Evidence.** TBC 25943

*Stage: trajectory processing · Documents: Manual; SOP; Field*

### D-21 · Which datum and epoch do we work in, who sets it, who checks it? · SOP §6.2

**P1** · open · **blocks processing**

**Why it matters.** A silent failure mode (the ITRF00 path) plus a user-settable epoch control Trimble flags as risky

**Evidence.** TBC 25943; TBC RN 2026.10

*Stage: project setup · Documents: Manual; SOP; Office*

### D-22 · Are scans generated coloured by default? · SOP §13.3

**P3** · open

**Why it matters.** Discovering later that colour was wanted means regenerating the mission

**Evidence.** TBC 22499; TBC 23339

*Stage: scan generation · Documents: Manual; SOP; Office*

### D-24 · Where is the calibration site, and who maintains it? · SOP §15.3

**P2** · open

**Why it matters.** Establishing one is a morning of work; finding one under schedule pressure is not

**Evidence.** TBC 24886; TBC 28972

*Stage: calibration · Documents: Manual; SOP; Office*

### D-26 · Recalibration interval and triggers - does daily removal of the Sensor Unit count as disturbing it? What happens to data collected on a stale calibration? · SOP §15.2

**P1** · open

**Why it matters.** If the head comes off nightly, calibration is routine rather than periodic

**Evidence.** MX60 UG Rev B p.7

*Stage: calibration · Documents: Manual; SOP; Field; Office*

### D-27 · QC inspection content - what does a visual point-cloud QC pass cover, and an imagery QC pass? · SOP §14.9

**P2** · open

**Why it matters.** Two QC layers produce no software artefact at all

**Evidence.** TBC 24886; TBC 25096

*Stage: QC · Documents: Manual; SOP; Office*

### D-28 · Is the retro-reflective target check our periodic verification, and at what interval? · SOP §15.6

**P2** · open

**Why it matters.** The only independent check on the instrument in any source

**Evidence.** MX60 UG Rev B p.7

*Stage: calibration · Documents: Manual; SOP*

### D-29 · The record package - what provenance record accompanies a deliverable, where does it live, and where is the control/check designation and its residuals recorded? · SOP §20.2

**P1** · open

**Why it matters.** Six facts cannot be reconstructed from the deliverable; TBC is not documented as reporting the designation

**Evidence.** TBC 22905; TBC 23991_1

*Stage: provenance · Documents: Manual; SOP; Office*

### D-31 · Is the imagery file-size scan adopted? · SOP §16.6

**P3** · open

**Why it matters.** Validation required first - file size alone cannot establish image validity

**Evidence.** TBC 23339; TBC 22501

*Stage: QC · Documents: Manual; SOP; Office*

### D-32 · What is our position on imagery privacy? Are unblurred originals retained, and for how long? · SOP §19.6

**P1** · open

**Why it matters.** Legal and reputational dimensions outside the SOP. Blurring is irreversible in the delivered product

**Evidence.** TBC 29527

*Stage: export · Documents: Manual; SOP; Office*

### D-34 · Handling segments mobile mapping cannot serve - the decision rule when a corridor produces an unacceptable trajectory, and whether marginal segments are recorded before mobilising · SOP §8.6, §22.4, §22.5

**P2** · open

**Why it matters.** Includes the legitimate professional answer that another method would be more defensible

*Stage: mission planning · Documents: Manual; SOP; Field; Office*

### D-35 · When may Cleanup be performed, by whom, and what must be archived first? · SOP §18.2

**P1** · open · **blocks one workflow branch**

**Why it matters.** Destructive, not undoable, reduces registration history at the moment the project is handed on

**Evidence.** TBC 26466

*Stage: cleanup · Documents: Manual; SOP; Office*

### D-36 · The export release gate - is the pre-export trajectory-node confirmation mandatory, and may exports be made with Export timestamps enabled before T18 resolves? · SOP §19.2

**P1** · open

**Why it matters.** Registration does not reach the cloud until Update Scans runs; a documented export option may substitute reprocessed data

**Evidence.** TBC 22638; TBC 23339; TBC 22501

*Stage: export · Documents: Manual; SOP; Office*

### D-38 · Deliverable specification - standard formats, which export path produces each, and default scaling · SOP §6.3, §19.4

**P2** · open

**Why it matters.** Ground scaling does not record its own scale factor; grid writes a sidecar that does

**Evidence.** TBC 11769; TBC 27279

*Stage: export · Documents: Manual; SOP; Office*

### D-39 · What is the corridor continuity inspection method and coverage? · SOP §16.5

**P1** · open

**Why it matters.** Must detect a degraded stretch shorter than the sampling interval, which rules out sparse spot checks

*Stage: QC · Documents: SOP; Office*

### D-41 · How many passes, in what pattern, by roadway type? · SOP §8.2

**P1** · open · **blocks collection**

**Why it matters.** Two of three degraded-GNSS remedies require overlap collected on the day

**Evidence.** TBC 25096; TBC 28972

*Stage: mission planning · Documents: SOP; Field*

### D-42 · Base station strategy and maximum baseline? · SOP §8.5

**P1** · open · **blocks collection**

**Why it matters.** Field logistics on every mission. Interacts with D-19

**Evidence.** TBC 25943

*Stage: mission planning · Documents: Manual; SOP; Field*

### D-43 · Field operating rules - wet-weather go/no-go with operator stand-down authority, night collection, collection speed by deliverable type, free-space margin · SOP §9.4

**P2** · open

**Why it matters.** An operator who must phone for permission will drive. Trimble publishes speed maxima and no relation to deliverable quality

**Evidence.** MX60 UG Rev B p.49,53; TMR 9.1

*Stage: acquisition · Documents: Manual; SOP; Field*

### D-46 · Where are lever arms, the Vehicle Preset and the installation configuration recorded and verified? · SOP §9.1

**P1** · open

**Why it matters.** Entered once, used every mission. An error is systematic, invisible, and persists until someone re-measures

**Evidence.** MX60 UG Rev B p.68; TBC 25943

*Stage: field preparation · Documents: SOP; Field*

### D-49 · Field close-out - what the mission field record contains, what coverage verification happens before leaving site, what triggers a re-drive and who decides · SOP §9.6

**P1** · open

**Why it matters.** No software produces the field record. Missed overlap removes office options irrecoverably

*Stage: field QC · Documents: SOP; Field*

### D-52 · Offload, verification and backup procedure · SOP §10.5

**P1** · open

**Why it matters.** The only irreversible step in the workflow

**Evidence.** MX60 UG Rev B p.10

*Stage: transfer · Documents: SOP; Field; Office*

### D-53 · Folder structure, naming and storage location · SOP §11.4, §20.3

**P2** · open

**Why it matters.** Several provenance artefacts are small files loose in a project folder

**Evidence.** TBC 25943; TBC 22905

*Stage: transfer · Documents: SOP; Field; Office*

### D-54 · Is a chain-of-custody record required? · SOP §11.5

**P3** · open

**Why it matters.** The deliverable may not be able to speak for itself

*Stage: transfer · Documents: SOP; Field*

### D-55 · Capture and retention - what is retained, where, for how long, by whom, including Backup SBET Next to MXDB, Results of Scan Generation, and the calibration JSON · SOP §21.1

**P1** · open

**Why it matters.** Tier 1 is a few hundred kilobytes. Tier 3 is hundreds of GB and determines whether reprocessing is ever possible

**Evidence.** TBC 25943; TBC 22499; TBC 22920

*Stage: archive · Documents: Manual; SOP; Office*

### D-56 · Does Parametrix adopt Trimble's documented initialization sequence, closing sequence and control-bracketing design rule as mandatory Parametrix requirements? · SOP §2.4

**P2** · open

**Why it matters.** Trimble documents these methods but does not state them as requirements - it writes 'should', 'it is advised', and 'Proposal of a checklist for system operation'. They carry TRIMBLE DOCUMENTED PROCEDURE and 'should' until Parametrix decides. Nothing else makes them mandatory.

**Evidence.** MX60 QSG Rev B sec 5.3 p.11, sec 5.5 p.13, sec 6 p.14; TBC 22905

*Stage: Field · Documents: SOP; Field*

---

## A4 · How a decision is adopted

1. Parametrix decides
2. The decision, its date and its approver are written into
   `deliverables/_control/master-register.csv` — `status`, `resolution`, `date_resolved`, `owner`
3. `python3 tools/build-register-views.py` regenerates this appendix and every other view
4. The SOP clause changes state from **PARAMETRIX DECISION REQUIRED** to **ADOPTED**, and its
   *should* becomes *shall*

**There is one register.** A decision cannot be adopted in one document and open in another.

---

# Appendix B — Index of Required Records

**Generated view — do not edit by hand.** Produced by `tools/build-records-index.py` from the
*Records this section requires* table at the end of each section. Edit the section; regenerate this.

**72 records**, across 20 sections.
Last generated 2026-09-11.

> **Read the State column.** A record whose state names a **D-** identifier is required by a clause
> that has not been adopted. It is proposed, not mandatory, and the identifier is where the decision
> is tracked (Appendix A).

> **Five of these records have no software artefact behind them** — the control and check
> designation, the visual inspection, the imagery inspection, the field conditions, and the
> disposition of a non-conformance. They are written by a person or they do not exist (§20.1).

---

## B1 · By section

| § | Section | Record | State |
|---|---|---|---|
| 2 | Document Control and Related Documents | Revision history of this procedure | **D-1** |
|  |  | Which supporting revisions were issued with this one | **D-1** |
|  |  | Distribution and receipt | **D-1** |
| 4 | Roles, Responsibilities and Authorities | Who holds each role on a given project | **D-3** |
|  |  | Who designated control versus independent check, and when | **D-15** |
|  |  | Any exercise of stand-down authority, and its reason | **D-43** |
| 5 | Competence and Training | Who holds which qualification, and from when | **D-3** |
|  |  | Training delivered, and against which document revision | **D-3** |
| 6 | Project Setup Requirements | Accuracy requirement, and its source | **D-13** |
|  |  | CRS, datum, epoch, geoid — and who set them | **D-21** |
|  |  | Grid or ground, as agreed | **D-38** |
|  |  | Configuration and fitment assumed | **D-2** |
| 7 | Control Requirements | Control network, with coordinates and their source | Existing practice |
|  |  | **Which points are control and which are independent checks, fixed before registration** | **D-15** |
|  |  | Who designated them, and when | **D-3** |
| 8 | Mission Planning Requirements | The mission plan — route, passes, direction, overlap | **D-41** |
|  |  | GNSS assessment, with duration estimates and mitigations | **D-41, D-42** |
|  |  | Initialization locations, primary and backup | **PROPOSED** |
|  |  | Segments mobile mapping will not serve, and what is proposed instead | **D-34** |
| 9 | Field Acquisition Requirements | Pre-flight confirmation, including aiding-sensor activation where fitted | **D-46** |
|  |  | The field record, per §9.6 | **D-49** |
|  |  | Any exercise of stand-down authority, and its reason | **D-43** |
|  |  | Operating-limit exceedance, if any, and what was done | **D-43** |
| 10 | Field Close-out and Handoff | Coverage verification, performed and by whom | **D-49** |
|  |  | Deviations from the mission plan | **D-49** |
|  |  | Handoff — what was transferred, to whom, when | **D-52, D-54** |
| 11 | Data Transfer and Custody | Offload performed, verified how, by whom, when | **D-52** |
|  |  | Location of the raw-data backup | **D-52, D-55** |
|  |  | Custody, where required | **D-54** |
| 12 | Office Intake Requirements | Intake checks performed, by whom, with the result of each | **D-18** |
|  |  | Calibration state at collection — `Extcal.json` and the Mission Report | **D-55** |
|  |  | Any intake check that failed, and what was done | **D-18, §22** |
| 13 | Processing Requirements | Trajectory processing settings, and the frame and epoch log | **D-55** |
|  |  | Results of Scan Generation | **D-55** |
| 14 | Registration Requirements | Registration name, type, and the runs included | **D-29** |
|  |  | The trajectory node produced, and its SBET filename **with its `_reg_####` number** | **D-29** |
|  |  | **Control and check designation, with the residual on each point, by component** | **D-29** — *no software artefact exists* |
|  |  | Confirmation that **Update Scans** was run | **D-36** |
|  |  | `Targets.csv`, archived | **D-55** |
|  |  | That the visual check was performed, by whom, over what extent | **D-27** — *no software artefact exists* |
| 15 | Calibration Control | Calibration performed — date, site, who, and the result including the visual check | **D-26** |
|  |  | The calibration JSON, archived outside the project | **D-55** |
|  |  | Which calibration each mission was processed against | **D-55** |
|  |  | Periodic verification, when performed | **D-28** |
| 16 | Quality Control Requirements | Residuals on control points used, by component | Targets pane |
|  |  | Residuals on independent check points, by component | Same |
|  |  | **Which points were control and which were checks** | **Manual — TBC does not report it** |
|  |  | Run-to-run RMS statistics, if used | Results tab |
|  |  | Trajectory RMS picture | Screen capture |
|  |  | **Visual check performed, by whom, covering what extent** | **No software artefact exists** |
|  |  | **Imagery check performed, by whom** | **No software artefact exists** |
|  |  | Results of Scan Generation | §13.3 |
|  |  | Mission Report | §18.3 |
| 17 | Acceptance and Approval | Acceptance decision — dataset, by whom, date, against what requirement | **D-3, D-13** |
|  |  | The evidence the decision rested on | **D-29** |
|  |  | The accuracy statement issued | **D-29** |
| 18 | Destructive Operation Controls | Authorisation — who, when, for which mission | **D-35** |
|  |  | What was archived before, and where it is | **D-35, D-55** |
|  |  | That Cleanup was run, by whom, on what date | **D-35** |
| 19 | Export and Delivery Controls | Export-state confirmation, before export | **D-36** |
|  |  | The delivery record — §20 | **D-29** |
|  |  | What was delivered, to whom, when, in what format and scaling | **D-38** |
| 20 | Documentation and Records | The delivery record, per §20.2 | **D-29** |
|  |  | The control and check table, with residuals | **D-29** |
|  |  | Where the record package lives for a given project | **D-53** |
| 21 | Retention and Archive | The archive record | **D-55** |
|  |  | Retention tier applied, and the date the period runs from | **D-55** |
|  |  | Disposal, where it occurs — what, when, authorised by whom | **D-55** |
| 22 | Non-conformance and Re-collection | The non-conformance — what, when, found by whom | **D-3** |
|  |  | Disposition — accepted with qualification, reprocessed, re-collected, or rejected | **D-3** |
|  |  | Where re-collection occurred, what changed | **D-3** |
|  |  | Any deliverable affected, and what was done about it | **D-29** |

## B2 · Where the state stands

| | |
|---|---|
| Records required by an **adopted** clause | **0** |
| Records required by a clause awaiting a decision | **72** |
| Distinct decisions they depend on | **24** — D-1, D-2, D-3, D-13, D-15, D-18, D-21, D-26, D-27, D-28, D-29, D-34, D-35, D-36, D-38, D-41, D-42, D-43, D-46, D-49, D-52, D-53, D-54, D-55 |

**Every record in this index is currently proposed.** That follows from no clause having been
adopted, not from any doubt about whether the records are worth keeping.

## B3 · The records with no software artefact

These are the ones that get lost, because nothing in the software produces them and nothing
complains when they are absent.

| Record | Section | Why nothing produces it |
|---|---|---|
| **Which points were control and which were independent checks** | §7.3, §14.10, §16.4 | TBC shows the state while the command is open and reloads it on Edit, but no report of it has been found *(Technical Manual §22.7)* |
| **That the visual inspection was performed, and over what extent** | §16.5 | It is a human act in a viewer |
| **That the imagery inspection was performed** | §16.6 | The same |
| **Conditions at collection** — occlusion, weather, traffic, what was not collected and why | §9.6 | Nothing in the vehicle records them |
| **Disposition of a non-conformance** | §22.7 | — |

## B4 · The smallest package that would satisfy the record

§20.2 proposes seven artefacts totalling a few hundred kilobytes. **Five of the seven already exist
as files** and need only to be copied out of the project before it is cleaned up (§18.3). Two are
written by a person.

---

# Appendix C — Approval and Revision History

## C1 · Status

> **CAUTION**
>
> **This procedure is a draft and has not been issued.** No clause is adopted, no approver is
> assigned, and the document-control convention it would be issued under does not exist yet
> (**D-1**, §2.2).
>
> It may be read, reviewed and worked from as a proposal. **It may not be cited as a Parametrix
> standard**, quoted to a client, or attached to a deliverable as evidence of procedure.

## C2 · What has to exist before this can be issued

| # | | State |
|---|---|---|
| 1 | A document-control convention — identifier, revision scheme, effective date, controlled copies | **D-1** |
| 2 | An owner and an approver | **D-1**, **D-3** |
| 3 | Roles assigned, so that the clauses naming a role name somebody | **D-3** |
| 4 | The nine decisions that **block operation** answered, or the clauses depending on them removed from scope | Appendix A, §A2 |
| 5 | The acceptance criterion, or an explicit statement that acceptance rests on documented professional judgement | **D-13**, §17.2 |

> Item 5 is the one that cannot be deferred silently. A procedure that governs acceptance without
> saying what acceptance means is incomplete in a way the reader must be told about, which is why
> §17.2 says it rather than hiding it.

## C3 · Approval

Reserved. The fields below are the ones a controlled document would carry; **the convention that
governs them is not established** and they are not filled in.

| Role | Name | Signature | Date |
|---|---|---|---|
| Prepared by | | | |
| Technical review | | | |
| Approved by | | | |

> **PARAMETRIX DECISION REQUIRED · D-1**
>
> Whether technical review and procedural approval are separate, and who holds each.

## C4 · Revision history

| Revision | Date | Issued with | Summary of change | Approved |
|---|---|---|---|---|
| `2026-09-11-a` | 2026-09-11 | Technical Manual `2026-09-11-a` / Evidence revision E1 | First draft circulated for internal review. 22 sections, three appendices. **No Parametrix clause adopted**; seven externally binding requirements restated (§2.4) | *Not approved — living draft* |

## C5 · What triggers a review

| Trigger | Why |
|---|---|
| **A TBC release** | TBC is on an annual cycle and releases have changed mobile mapping behaviour. This revision documents **2026.10** |
| **A decision adopted** | The clause changes state, and its *should* becomes *shall* |
| **A test result** | Technical Manual Appendix F. **T18** and **T19** could change what §19 requires |
| **A vendor answer** | Especially **V-4** — the system configuration, which nine other items depend on |
| A change to the system — reconfiguration, a fitted sensor, a new vehicle | §6.4, §9.1 |
| A non-conformance that the procedure did not prevent | §22 |

## C6 · How this appendix relates to the register

Appendix A is generated from the master register and is the authoritative list of decisions. **This
appendix is written by hand** and records approval events, which have no representation in the
register.

If the two ever disagree about whether something is adopted, **Appendix A is correct**, because it
is generated from the file that the adoption is recorded in.
