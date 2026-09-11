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
