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

### How the duties divide

> **PARAMETRIX PROCEDURE (PROPOSED)** — *how the duties divide*
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
