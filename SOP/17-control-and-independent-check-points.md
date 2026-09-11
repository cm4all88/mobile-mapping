# 17. Control and Independent Check Points

## 17.1 Why this section is separate

Every accuracy claim Parametrix makes about a mobile mapping deliverable rests on this section.

Registration (§15) is the mechanism. This section is about the **survey decision** underneath it:
which surveyed points participate in the adjustment, which are held back to measure it, and who
decides. TBC reduces that decision to three checkboxes, which makes it easy to make
inadvertently.

> A surveyor needs no explanation of why check points matter. What needs explaining is how TBC
> expresses the idea, and where its expression differs from the conventional one.

## 17.2 How control participates — three independent choices per point

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*
>
> In the **Control Points** list, each point carries three checkboxes:
>
> | Column | Effect |
> |---|---|
> | **Use XY** | The **horizontal** coordinates of this point are used to optimise the trajectory |
> | **Use Z** | The **vertical** coordinate is used |
> | **As Check** | The point is a **validation point**. Its residuals are computed and reported but **are not taken into account in the registration** |
>
> "For the selected ground control point (GCP), choose to optimize only the XY coordinates (Use
> XY), or only the Z coordinate (Use Z), or both by checking the corresponding check box(es)."

### The validation point definition, in full

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "A validation point (VP) (As Check) is a ground control point (GCP) that is used **only for
> measuring the quality of the registration**. In the same manner as a normal ground control
> point (GCP), **you need to pair a validation point (VP) with a picked target**. The resulting
> XYZ residual values **will not be taken into account in the registration**, which is why all
> the selected ground control points (GCPs) cannot be set as validation points (VPs). If you set
> all the selected ground control points (GCPs) as validation points (VPs), **an error will
> pop-up** and will prompt you to have at least one ground control point (GCP) for the
> calculation." *(TBC 22905, 26473)*

Three consequences worth stating plainly:

1. **A check point still has to be picked.** Holding a point out of the adjustment does not save
   the operator any work — the target must be identified in the cloud exactly as for a control
   point, and picked with the same care. A carelessly picked check point produces a bad residual
   that says nothing about the data.
2. **TBC does not permit every point to be a check point**, because the adjustment still requires
   control. The software enforces a minimum of one. **That is a mathematical floor, not a survey
   standard.**
3. **The split is per component.** A point can be horizontal control and vertical check, or the
   reverse, by combining the checkboxes. This is genuinely useful where the horizontal control is
   strong and the vertical is the question — or where a feature is well defined in plan and
   poorly defined in height, which describes most painted road markings.

## 17.3 Horizontal and vertical are separable, and usually should be considered separately

> **WHY THIS MATTERS**
>
> A painted stop-bar corner is an excellent horizontal target — a crisp intensity edge the cloud
> resolves well. It is a poor vertical one: it lies in the road surface, the scan hits it at a
> grazing angle, and the height of the picked point depends on exactly which return the operator
> snapped to.
>
> Checking **Use XY** and leaving **Use Z** unchecked on such a point uses it for what it is good
> at and keeps it out of the vertical solution. TBC supports this directly. A processor who
> checks both boxes on every point because that is the default has made a survey decision without
> noticing.

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** This is answerable empirically on a test site with a variety of
> features surveyed conventionally, and the answer will shape control design (§6) far more than
> any software setting. *(Appendix E)*

## 17.4 The independence requirement

This is the part the software cannot enforce.

> **IMPORTANT**
>
> **A check point is only meaningful if it was designated before the adjustment and did not
> change.**
>
> Residuals on points that took part in the adjustment measure how well the adjustment fits the
> observations that shaped it. They are a measure of internal consistency. They tend to look good
> and they are not evidence of accuracy.
>
> Residuals on points held out of the adjustment measure something entirely different: whether
> the adjusted trajectory predicts a position it was never told about. **That is the only
> numerical evidence of accuracy this workflow produces.**

### The failure mode to design against

A conscientious processor registers a mission, inspects the residuals, finds one check point with
a residual larger than they expected, and adds it to the adjustment to bring it in. Every step is
well intentioned. The result is an adjustment with no independent check at all, and a set of
residuals that now measure nothing.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> - **Check points are designated by the Project Surveyor before registration begins** (§3.4)
> - **A point's As Check status is not changed during processing.** If the designation was wrong,
>   it is changed by the Project Surveyor, recorded, and the registration is redone from the
>   imported trajectory using **Edit** (§15.8) — not layered on top
> - **The designation is recorded in the project record** and travels with the accuracy statement
>
> **Not adopted.** *(Register item 15; §3.3 D-3.3)*

## 17.5 How much control, and where

> **PARAMETRIX DECISION REQUIRED**
>
> **How many control points, at what spacing, and how many held as independent checks?**
>
> **No Trimble source states a minimum, a spacing, or a ratio.** TBC's software minimum is one
> control pair and one check point, which is a mathematical floor and has no bearing on survey
> adequacy.
>
> The decision must account for:
>
> - **Corridor length and the project accuracy requirement**
> - **The registration method.** A **Local** adjustment interpolates between control points and
>   **does not extrapolate beyond them** *(TBC 22905)*, so control must **bracket** the delivered
>   extent, not merely fall within it (§15.5)
> - **The bundle adjustment interval** — 250 m checked, 70 m unchecked *(§15.7)* — which is
>   Trimble's own indication of the scale at which control density matters
> - **GNSS conditions along the corridor.** Control is most valuable where the trajectory is
>   weakest, which is precisely where it is hardest to survey conventionally
> - **Redundancy.** Enough that removing any single point would not materially change the result
>
> *(Register item 16)*

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **A structure for the decision, not the decision:**
>
> - Control **bracketing** each end of the delivered extent, outside it where the corridor allows
> - Control at intervals along the corridor, with the interval set from the project accuracy
>   requirement and tightened where GNSS is degraded
> - **Independent check points distributed across the corridor, not clustered**, and including at
>   least one in each distinct GNSS environment — open sky, tree cover, urban canyon
> - **A check point near each end**, because that is where a Local adjustment stops working and
>   where the smoother has data on one side only (§2.2)
>
> **Not adopted.** No counts, no spacings and no ratios appear here deliberately — those are the
> content of the decision above. *(Register item 16)*

## 17.6 What TBC reports, and what it does not

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Per pick, live in the **Validate Picking** window and in the **Targets** pane: **Easting
> residual**, **Northing residual**, **Elevation residual**, "with their corresponding directional
> signs" *(TBC 22905)*.
>
> From TBC 2025.21: those residuals "are now **signed** and included in **the report**"
> *(TBC RN 2025.21)*.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which report?** The 2025.21 release note says the signed residuals are included in "the
> report" without naming it. The only mobile mapping report topic — *Run a Mission Report*
> *(TBC 23991_1)* — describes the report as showing "capture devices, runs, trajectories and
> generated scans" and **does not mention residuals at all**.
>
> This matters because the residuals on check points are the primary numerical evidence in the
> accuracy statement, and whether they can be produced as a report — rather than transcribed by
> hand from a dialog — determines how the record is kept (§23, §25). *(Appendix F)*

> **FIELD TESTING REQUIRED · T21**
>
> Register a mission, run a Mission Report, and look. This is answerable in ten minutes with the
> software in front of you. *(Appendix E)*

### What TBC does not report

❌ TBC does not produce, in any captured topic, a statement of **which points were used as
control and which as checks** in a registration that has already been applied. The Use XY / Use Z
/ As Check state is visible while the command is open and reloaded by **Edit** *(TBC 25362,
26578)* — but no report of it has been found.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Record the control/check designation outside TBC**, in the project record, at the time of
> registration: point ID, Use XY, Use Z, As Check, and the resulting residual on each.
>
> This is the single most important record in the whole workflow and the software does not appear
> to produce it. Six columns in a spreadsheet, written once. **Not adopted.**
> *(Register item 17; §23)*

## 17.7 Control for calibration is a different thing

A brief warning against a natural confusion.

The calibration procedures in §14 use a specific **run geometry** — four runs, two orthogonal
pairs, each driven in both directions, 250–300 m per strip *(TBC 24886, 28972)* — and derive
boresight angles from **scan-to-scan agreement**, not from control. Surveyed control plays no
part in TBC's laser scanner calibration.

Control and check points are for registration. They do not validate a calibration, and a
calibration does not substitute for them.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We separated the surveyed points into two groups: ones the adjustment is
> allowed to use, and ones it is not allowed to see. TBC does this with three checkboxes per
> point — horizontal, vertical, and *hold this one back as a check* — and it lets you split a
> single point between the groups, using it horizontally while holding its height back.
>
> **Why it matters.** This is the difference between an accuracy statement and an opinion. If
> every surveyed point went into the adjustment, then the residuals you report are just telling
> you how well the maths fitted the numbers you gave it. Of course it fitted. The only figure
> that means anything to a client is the residual on a point the adjustment never saw — that is
> the one that says "the system predicted a position it was not told about, and it was right to
> within this much."
>
> **What can go wrong.** The dangerous failure is not carelessness, it is diligence pointed the
> wrong way. A processor sees a check point with a residual bigger than they hoped, ticks it into
> the adjustment, and re-runs. The number improves. The check has been destroyed, and nothing in
> the software records that it ever existed. This is why the designation should be made by
> somebody other than the person doing the adjustment, and why it should be written down outside
> TBC — because TBC does not appear to report it afterwards.
>
> **What good looks like.** Points held out of the adjustment, chosen before it ran, spread along
> the corridor rather than clustered, with at least one in each kind of GNSS environment and one
> near each end. Their residuals in the same range as the control points that were used — not
> much worse, which would mean the adjustment is only fitting locally, and not suspiciously
> better either. And a written record of which was which, because in two years the project file
> will not tell you.
