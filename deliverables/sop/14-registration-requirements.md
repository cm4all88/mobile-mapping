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

> **TRIMBLE REQUIREMENT** — *an enforced software limit*
>
> **At least one control point in a registration shall not be a validation point.** Trimble states
> that if every selected GCP is set **As Check**, *"an error will pop-up and will prompt you to
> have at least one ground control point (GCP) for the calculation"* *(TBC 22905)*.
>
> It is worth knowing which way this cuts: TBC protects the *calculation*, not the *check*. It will
> stop you holding nothing back for the adjustment. **It will not stop you holding nothing back for
> the check**, which is the failure below.

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
