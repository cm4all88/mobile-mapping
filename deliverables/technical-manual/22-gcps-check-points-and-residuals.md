# 22. GCPs, Check Points and Residuals

## 22.1 Why this section is separate

Every accuracy claim Parametrix makes about a mobile mapping deliverable rests on this section.

Registration (§21) is the mechanism. This section is about the **survey decision** underneath it:
which surveyed points participate in the adjustment, which are held back to measure it, and who
decides. TBC reduces that decision to three checkboxes, which makes it easy to make
inadvertently.

> A surveyor needs no explanation of why check points matter. What needs explaining is how TBC
> expresses the idea, and where its expression differs from the conventional one.

## 22.2 How control participates — three independent choices per point

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

## 22.3 Horizontal and vertical are separable, and usually should be considered separately

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
> features surveyed conventionally, and the answer will shape control design (§22.6) far more than
> any software setting. *(Appendix E)*

## 22.4 The independence requirement

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

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-15, D-3); it is not decided here.

## 22.5 What makes a feature usable as a mobile mapping GCP

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*
>
> A **GCP** is "an accurately surveyed coordinate location for a physical feature that can be
> identified on the ground, e.g., **a corner on the pavement markings**." A **target** is "a point
> extracted from the acquired scan data."

> **IMPORTANT · this changes control design**
>
> A mobile mapping GCP must be **findable in a point cloud** at the density and incidence angle
> the vehicle produced. That is a different requirement from *occupiable with a prism*, and it is
> the requirement that governs.
>
> | Works well | Works poorly |
> |---|---|
> | Painted stop-bar and lane-line corners — crisp intensity edges | A survey nail in asphalt — a few millimetres across, below cloud resolution |
> | Checkerboard, diamond, rectangular and L-shape (GV) target panels, for which TBC has templates *(TBC 22905)* | Small features at grazing incidence (§21.12) |
> | Painted arrow and legend corners | Anything that moves, is repainted, or is worn |

A painted stop-bar corner is an excellent **horizontal** target and a poor **vertical** one: it
lies in the road surface, the scan hits it at a grazing angle, and the picked height depends on
which return the operator snapped to. TBC's per-component control (§22.2) exists precisely so that
a feature can be used for what it is good at.

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** Answerable on a test site with features surveyed conventionally,
> and the answer will shape control design more than any software setting.

## 22.6 How much control, and where

No Trimble source states a minimum, a spacing, or a ratio. TBC's software minimum is one control
pair — a mathematical floor with no bearing on survey adequacy (§28.6). What Trimble does give is
two indications of the **scale** at which control matters, and one hard constraint.

### The constraint: Local does not extrapolate

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*
>
> A **Local** registration is "suitable for a local adjustment of a run, **not for systematic error
> along the run or for adjusting outside the ground control points set**."

> **CAUTION · W-08**
>
> **Local does not extrapolate.** Beyond the outermost control point the trajectory is not
> adjusted, and nothing in the software indicates where the adjustment stopped. **Control must
> bracket the extent you intend to deliver, not merely fall within it.**
>
> The trajectory RMS colouring makes the boundary visible after the fact — adjusted segments render
> as *Undefined RMS* (§24) — but that is a check, not a substitute for designing the control layout
> correctly.

### The scale indication

**Target-Bundle Adjustment** operates at **250 m** intervals when checked and **70 m** when
unchecked *(TBC 22905; §28.7)*. That is Trimble's own indication of the scale at which control
density matters, and the two figures differ by more than a factor of three.

The second indication is §20.4: the ends of a mission are where the smoother had one anchor rather
than two, so control and checks at the ends are worth more than control in the middle.

> **Open Parametrix decision — D-16.** *How many control points, at what spacing, and how many held
> as independent checks?* Stated and tracked in the **SOP §7**; see also the master register.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-16); it is not decided here.

> **EXTERNAL REFERENCE — NOT PARAMETRIX PROCEDURE**
>
> The Queensland TMR *Mobile Laser Scanning Technical Guideline* (March 2023, CC BY 4.0) is a
> published transport-agency specification in the source set. It defines survey-grade,
> engineering-grade and asset-grade tiers, and for its higher tiers specifies control adjacent to
> the start and end of the project and at intersections of controlled roads *(TMR §11)*.
>
> **It is cited as an example of how another agency has answered D-16 — not as a Parametrix
> standard and not as a Trimble requirement.** Parametrix's own accuracy tiers, if it adopts any,
> are D-16.

## 22.7 What TBC reports, and what it does not

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Per pick, live in the **Validate Picking** window and in the **Targets** pane: **Easting
> residual**, **Northing residual**, **Elevation residual**, "with their corresponding directional
> signs" *(TBC 22905)*.
>
> From TBC 2025.21: those residuals "are now **signed** and included in **the report**"
> *(TBC RN 2025.21)*.

> **VENDOR CLARIFICATION REQUIRED · V-11**
>
> **Which report?** The 2025.21 release note says the signed residuals are included in "the
> report" without naming it. The only mobile mapping report topic — *Run a Mission Report*
> *(TBC 23991_1)* — describes the report as showing "capture devices, runs, trajectories and
> generated scans" and **does not mention residuals at all**.
>
> This matters because the residuals on check points are the primary numerical evidence in the
> accuracy statement, and whether they can be produced as a report — rather than transcribed by
> hand from a dialog — determines how the record is kept (§30, and the **SOP §20**). *(Appendix E)*

> **FIELD TESTING REQUIRED · T21**
>
> Register a mission, run a Mission Report, and look. This is answerable in ten minutes with the
> software in front of you. *(Appendix E)*

### What TBC does not report

❌ TBC does not produce, in any captured topic, a statement of **which points were used as
control and which as checks** in a registration that has already been applied. The Use XY / Use Z
/ As Check state is visible while the command is open and reloaded by **Edit** *(TBC 25362,
26578)* — but no report of it has been found.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §7** (D-29); it is not decided here.

## 22.8 Control for calibration is a different thing

A brief warning against a natural confusion.

The calibration procedures in §20 use a specific **run geometry** — four runs, two orthogonal
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
