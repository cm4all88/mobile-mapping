# 16. Acceptance and Approval

## 16.1 What acceptance is

**Acceptance is the point at which the data becomes the deliverable.** It is a decision by a named
person, recorded, that a dataset meets the project's stated accuracy requirement (§6.1).

Acceptance is always **against a requirement**. A dataset is not accepted because it looks good, or
because the residuals are small, or because the schedule has run out.

## 16.2 The criterion is not established

> **PARAMETRIX DECISION REQUIRED · D-13 · P1 · blocks operation**
>
> **What constitutes an acceptable registration, and an acceptable point cloud?**
>
> **This SOP states no numerical acceptance tolerance, and one has not been invented.**
>
> | | |
> |---|---|
> | Trimble publishes **no acceptance tolerance** for the MX60 | The published figures are instrument performance under stated conditions, not deliverable acceptance criteria |
> | Trimble publishes **no attitude error budget** for the point cloud | So a useful range for a given tolerance cannot be calculated from the documentation *(Technical Manual §16.5)* |
> | The relationship between achieved accuracy and GNSS conditions on this system **has not been tested** | **T31** |
> | Which features are fit for horizontal or vertical control at MX60 density **has not been tested** | **T25** |
>
> Until D-13 is answered, **a Parametrix accuracy statement for an MX60 deliverable rests on the
> judgement of the person signing it**, supported by the evidence in §15 — and that should be
> understood by whoever signs it and whoever receives it.

> **A number here would be worse than the gap.** An invented tolerance would be quoted, relied on
> and eventually defended, and there is nothing behind it. The gap is visible; a fabricated
> threshold would not be.

## 16.3 What acceptance requires regardless

Even without D-13, five things are required before a dataset is accepted. These are structural and
do not depend on the number.

| # | Requirement | State |
|---|---|---|
| 1 | The project's **accuracy requirement is stated in writing** (§6.1) | **PROPOSED — D-13** |
| 2 | **Independent check points exist**, were designated before registration, and took no part in any adjustment (§7.3) | **PROPOSED — D-15** |
| 3 | **Residuals on those check points are recorded**, by component (§15.4) | **PROPOSED — D-29** |
| 4 | **The visual inspection was performed and recorded** (§15.5) | **PROPOSED — D-27** |
| 5 | **Update Scans was run**, and the accepted cloud is the registered one (§13.4) | **PROPOSED — D-36** |

> **Requirement 2 is the one that cannot be recovered afterwards.** If no point was held out, the
> dataset cannot be checked later without re-surveying, because every point it might be checked
> against helped produce it.

## 16.4 What acceptance shall not rest on

| | Why |
|---|---|
| **RMS alone** | A good RMS does not prove success; Trimble says so twice (§15.1) |
| **Residuals on control points used in the adjustment** | They measure the fit of the adjustment to observations it was given |
| **A clean-looking point cloud** | Mobile mapping data does not look wrong when it is wrong *(Technical Manual §3.2)* |
| **Agreement between two passes** | Two passes can agree with each other and both be displaced, if the trajectory was drifting through the stretch |

## 16.5 Who accepts

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> Who may accept a registration, and who signs an accuracy statement. Proposed at §4.2: the
> Project Surveyor, and not the person who computed the registration.

## 16.6 The accuracy statement

An accuracy statement issued to a client states:

| | |
|---|---|
| The accuracy requirement it was assessed against | |
| **The evidence** — residuals on independent check points, by component | |
| **The basis of the check** — how many points, where, in which GNSS environments | |
| The extent it applies to | Accuracy is not uniform along a corridor *(Technical Manual §3)* |
| Any segment excluded, and why | §8.6, §21 |

> **Accuracy varies along the corridor.** A single figure for a whole corridor implies a uniformity
> the method does not have. Where the statement is a single figure, the extent and the conditions
> it applies to are stated with it.

## 16.7 Records this section requires

| Record | State |
|---|---|
| Acceptance decision — dataset, by whom, date, against what requirement | **D-3, D-13** |
| The evidence the decision rested on | **D-29** |
| The accuracy statement issued | **D-29** |
