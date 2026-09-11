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


> **IN PLAIN LANGUAGE**
>
> **What this section means.** Mobile mapping still needs surveyed ground control, and it needs two
> different kinds of it: points the adjustment is allowed to use, and points deliberately held back so
> they can be used to check the result.
>
> **Why it matters.** The adjustment will fit whatever you give it. Residuals on points it used tell
> you how well it fitted them, not whether the cloud is in the right place. Only a point it never saw
> can tell you that.
>
> **Remember this.** Decide which points are control and which are checks **before** registration
> starts, write it down, and do not change it afterwards to make a number look better. Control has to
> bracket the extent you intend to deliver — beyond the outermost point the trajectory is not adjusted
> at all, and nothing on screen shows where that happened.
>
> **If this is skipped.** You end up with a dataset that cannot be checked without going back out and
> surveying more, and with a set of residuals that measure nothing. That usually surfaces when a
> client asks how the accuracy figure was arrived at.
