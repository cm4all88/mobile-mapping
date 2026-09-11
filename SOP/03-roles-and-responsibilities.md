# 3. Roles and Responsibilities

> **This entire section is PARAMETRIX DECISION REQUIRED.**
>
> No role assignment, approval authority, qualification requirement or sign-off has been made
> for mobile mapping at Parametrix. Everything below is a **structure for the decision**, not a
> record of one. Nothing in this section may be quoted as an existing Parametrix requirement.

## 3.1 Why this section is not optional

Most of the failure modes in this document are not technical. They are questions of who noticed
and who decided.

A registration that used the wrong trajectory, a Cleanup that destroyed the only record of an
earlier attempt, a deliverable exported with a setting nobody examined — none of these is a
software fault. Each is a place where a person made a choice, and the difference between a
defensible project and an indefensible one is whether the right person made it and whether
anyone can tell afterwards.

> **WHY THIS MATTERS**
>
> Mobile mapping compresses a great deal of judgement into a small number of dialog boxes. A
> processor clicking **Apply** in the Register a Run dialog is making an adjustment decision
> that, in conventional survey work, would have been a least-squares run reviewed by a licensed
> surveyor. The software does not care who clicks. The SOP has to.

## 3.2 The roles this document assumes

These are **functions, not job titles**. One person may hold several. On a small job the same
person may hold all of them — which is workable, provided it is recorded and provided the
independent checks in §17 and §24 are genuinely independent of the adjustment.

### Field Technician / Operator

Runs the system. Owns everything from vehicle preparation through to verified data transfer.

- Vehicle installation, sensor mounting, cabling, power (§7)
- Preflight checks and TMI configuration (§7, §8)
- Initialization, collection, monitoring, closing sequence (§8)
- Field quality checks before leaving site (§9)
- Data offload and integrity verification (§10)
- The field record: what was collected, in what conditions, what went wrong

> **The operator is the only person who will ever see the collection conditions.** GNSS quality,
> weather, traffic, obstructions, a manoeuvre that had to be abandoned — none of this survives
> into the data in a readable form. If the operator does not record it, it is gone, and the
> office will be inferring it from residuals three weeks later.

### Mobile Mapping Processor

Takes the raw mission to a QC'd, registered point cloud.

- Import and project setup (§11)
- Trajectory processing, or coordination with whoever holds the POSPac licence (§12)
- Scan generation and filter selection (§13)
- Registration to control (§15, §16)
- Point cloud and imagery QC (§18, §19)
- Export and delivery preparation (§22)
- The processing record (§23)

### Project Surveyor

Owns the accuracy statement. This is the role that must be independent of the adjustment.

- Control network design and adequacy for the corridor (§5, §6)
- **Designating which points are control and which are held as independent checks** (§17)
- Reviewing registration results against the project accuracy requirement (§15, §18)
- Accepting or rejecting the dataset (§24)
- Signing the accuracy statement that goes to the client

> **IMPORTANT**
>
> The person who performs a registration should not be the only person who judges whether it
> passed. This is ordinary survey practice and it applies here unchanged — but it is easier to
> lose in mobile mapping, because the adjustment and the assessment happen in the same
> software, in the same session, by the same person, minutes apart.

### Project Manager

Does not need to operate anything. Needs to be able to answer a client.

- Scope, schedule and the accuracy requirement agreed with the client (§5)
- Knowing what was collected and what was not
- Knowing whether the deliverable is defensible, and on what evidence (§23, §24)
- Records retention and archive (§25)

### System Owner

The role with no obvious home, and the one most likely to go unassigned.

- Calibration currency — when the system was last calibrated and whether it is still valid (§14)
- Firmware and software versions, and what changed in them (§4)
- Vendor relationship, support, open questions (Appendix I)
- **Maintaining this SOP** as TBC and TMI change

## 3.3 The decisions

> **PARAMETRIX DECISION REQUIRED**
>
> **D-3.1 · Who may operate the MX60?** Is there a qualification, a training requirement, a
> supervised-run count, or a sign-off before someone collects production data alone?
>
> **D-3.2 · Who may perform a registration?** Registration is an adjustment. Is it restricted,
> and if so to whom?
>
> **D-3.3 · Who accepts a registration?** Must the accepting person be someone other than the
> person who performed it? *(§17, §24)*
>
> **D-3.4 · Who may run Cleanup Mobile Mapping Mission?** It is destructive and not undoable.
> *(§21 — this is the sharpest single instance of the problem)*
>
> **D-3.5 · Who signs the accuracy statement?** Under what licensure, and against what evidence?
>
> **D-3.6 · Who owns calibration currency?** *(§14)*
>
> **D-3.7 · Who owns this SOP?** *(§1.7)*
>
> *D-3 to D-9. See Appendix I.*

## 3.4 A proposed structure, offered for decision

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted. Offered so the decisions in §3.3 have something concrete to react to.**
>
> | Activity | Performed by | Reviewed or approved by |
> |---|---|---|
> | Mission planning | Processor or Project Surveyor | Project Surveyor |
> | Control network design | Project Surveyor | — |
> | Field acquisition | Field Technician | — |
> | Field quality checks | Field Technician | — |
> | Trajectory processing | Processor | — |
> | Calibration | Processor | System Owner |
> | **Registration** | **Processor** | **Project Surveyor** |
> | **Designating control vs. check** | **Project Surveyor** | — |
> | Point cloud and imagery QC | Processor | Project Surveyor |
> | **Cleanup Mobile Mapping Mission** | **Processor** | **Project Surveyor, in writing** |
> | Export and delivery | Processor | Project Surveyor |
> | Accuracy statement | Project Surveyor | — |
> | Archive | Processor | Project Manager |
>
> The three rows in bold are the ones where the reviewer genuinely matters. The rest could
> reasonably collapse onto fewer people on a small job.
>
> **The rationale for control-versus-check sitting with the Project Surveyor and nobody else:**
> if the person performing the adjustment also chooses which points the adjustment is measured
> against, the check is not independent. That is true in conventional survey work and it is true
> here. TBC makes the choice a checkbox *(§17)*, which makes it easy to change quietly.

## 3.5 What must be recorded regardless of who does it

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Whatever Parametrix decides about roles, the project record should be able to answer, for any
> dataset, years later:
>
> - Who collected it, when, and in what conditions
> - Which trajectory the delivered data was built on *(§23 — this one is genuinely hard)*
> - Which points were used as control and which were held as independent checks
> - What the registration residuals were, on both
> - Who accepted it, on what date, against what accuracy requirement
> - Whether Cleanup was run, by whom, and what was archived first
>
> Six facts. None is onerous to record at the time and all are effectively unrecoverable later.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We listed the jobs that have to be done and the decisions about who does
> them — and were honest that Parametrix has not made those decisions yet. What is here is a
> proposal to argue with, not a rule to follow.
>
> **Why it matters.** In conventional survey work, the boundaries between roles are established
> by decades of practice and by licensure. Mobile mapping has none of that yet at Parametrix, and
> the software actively blurs the lines: the same person, in the same hour, in the same
> application, can adjust the data, decide what to measure the adjustment against, judge whether
> it passed, and export the result. Nothing stops them. Nothing records that they did.
>
> **What can go wrong.** The specific failure to worry about is not carelessness — it is a
> conscientious processor who adjusts, checks, finds a residual they do not like, adds a point to
> the adjustment to improve it, and re-checks. Every step is well intentioned. The result is an
> adjustment measured against itself, and a residual figure that means nothing. This is exactly
> the failure that separating "who adjusts" from "who decides what is a check" prevents.
>
> **What good looks like.** On a well-run job, the person who signs the accuracy statement can
> point to check points they designated before the adjustment ran, that took no part in it, and
> say what the residuals on those points were. If that sentence cannot be said, the accuracy
> statement is an opinion.
