# 18. Point Cloud QC

## 18.1 The governing principle

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

Stated by Trimble in identical wording in two separate topics — the laser scanner calibration
topic and the run-to-run registration topic. It is the single most important sentence in the
office workflow, and the whole of this section is built on it.

### Why the asymmetry is real and not a hedge

A residual measures the fit between an adjustment and **the observations that shaped it**.

An adjustment with few observations fits them exactly — with three unknowns and three
observations there is no redundancy and the residuals are zero by construction. An adjustment
whose observations all share a systematic error fits them beautifully and carries the error
through untouched. In both cases the numbers are excellent and the data is wrong.

The reverse does not hold. If an adjustment *cannot* fit its own observations, something is
genuinely broken — bad control coordinates, misidentified targets, a trajectory too poor to
correct, a calibration that has drifted.

> **A number can prove failure. A number cannot prove success.**
>
> Only two things can suggest success: **observations that took no part in the adjustment**
> (§17), and **looking at the data** (§18.5).

## 18.2 What TBC gives you, at four levels

| Level | Indicator | Where | Source |
|---|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, signed; **RMS of the fitted plane** | Validate Picking, Targets pane | *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in **Tangential, Orthogonal, Vertical**; `No overlap` where absent | Results tab, Register Run to Run | *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair RMS in three axes | Calibrate Laser Scanners | *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation and velocity RMS after smoothing, from `smrmsg_xxx.out` — rendered as **trajectory colour** | Plan View | *(TBC 25943, 27248)* |

Plus the visual check (§18.5) and the records in §18.8.

> **Note what is missing from that table: a single number that describes the quality of a
> registration.** There is no registration report equivalent to a least-squares adjustment
> summary. The evidence is distributed across a dialog, a results tab, a trajectory colour and
> the operator's eyes — which is why the recordkeeping in §18.8 and §23 matters more here than it
> would in a conventional adjustment.

## 18.3 Reading the three axes

Tangential, orthogonal and vertical appear in both calibration and run-to-run registration. They
diagnose, not just describe.

| Dominant component | What it points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor (§12.3) and the time synchronisation |
| **Orthogonal** — across travel, horizontal | Heading. The hardest attitude component, and the one a single direction of travel cannot resolve (§14.3) |
| **Vertical** | Pitch, or the height component of the trajectory. Check the antenna model (§12.3) and the geoid |

> **WHY THIS MATTERS**
>
> A combined RMS hides this. Three numbers of similar size mean random disagreement, which is
> what good data looks like. One number much larger than the other two means a specific,
> identifiable part of the solution is struggling — and tells you where to look rather than
> leaving you to regenerate everything and hope.

## 18.4 Reading the trajectory RMS colouring

Set at **Mobile Mapping ▸ Trajectory Settings ▸ Rendering Settings ▸ RMS values**, with
user-definable ranges and colours. Settings persist between projects *(TBC 27248)*.

> **This is the highest-value, lowest-effort QC view in the workflow**, and it is available
> before any point cloud exists (§12.4).

What to read from it:

- **Where the solution degraded** — and therefore where control is most valuable (§17) and where
  registration will struggle
- **How long each degraded stretch was.** A short gap bracketed by good data is bridged well by
  the smoother. A long one is not (§2.2)
- **Whether the degradation is at the ends of the mission**, where the smoother has data on one
  side only — the reason the closing sequence in §8 exists

> **OBSERVED SOFTWARE BEHAVIOR**
>
> "If the mission contains some registrations then the modified segments will be colorized with
> the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
> `smrmsg` file, so adjusted stretches lose their RMS colour.
>
> **Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
> registration that stopped adjusting beyond the outermost control point (§15.5) shows the
> boundary directly.

## 18.5 The visual check

Trimble requires it and does not describe how to do it thoroughly. What follows assembles the
mechanics Trimble does give *(TBC 24886, 25096)* into a method.

### Cutting Plane View — checking agreement between overlapping data

The tool for the question *do two passes of the same feature land in the same place?*

1. **Point Clouds ▸ View ▸ Cutting Plane View** (it opens automatically after calibration or
   run-to-run registration if the option was checked)
2. Set rendering to **Scan Color** — one colour per scan, so the two data sets are
   distinguishable. **This is the step that makes the check possible**; in a single colour, two
   offset surfaces read as one thick surface
3. Increase **Point Size**
4. Set **Cutting plane thickness** (§18.6)
5. In Project Explorer, **check only the scans in the pair** and uncheck everything else
6. **Drag the slider along the run**, watching the gap
7. Optionally **Show surface-plane intersection** where a surface exists

What you are looking for: **one wall, one kerb, one pole.** Two of anything is a disagreement,
and its size in the profile is its size in the data.

> **FIELD TIP**
>
> Drag the slider through the **whole** run, not a representative sample. Trajectory error is
> correlated in time (§2.3), so disagreement is concentrated in stretches rather than scattered.
> A pass that is perfect for 2 km and 5 cm out for 300 m will look perfect at every point you
> spot-check and be unacceptable where it matters.

### What else to look at, and what nothing automates

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> A visual QC pass over a registered mission should cover:
>
> | Check | Looking for |
> |---|---|
> | **Overlapping passes in Cutting Plane View**, dragged full length | Doubled surfaces |
> | **Flat surfaces at range** — a wall, a building face | Thickening with distance, which indicates attitude error or a calibration issue (§14.2) |
> | **The ends of the corridor** | Where a Local adjustment stopped; where the smoother was weakest |
> | **The degraded stretches identified in §18.4** | Whether the registration actually fixed them |
> | **Vertical surfaces against horizontal** | Systematic tilt |
> | **Features near control** versus **features far from control** | Residual growth with distance from constraint |
>
> **Not adopted.** *(D-27)*

## 18.6 Cutting plane thickness

> **FIELD TESTING REQUIRED · T16**
>
> Trimble's screenshots show **0.030** in the calibration topic *(TBC 24886)* and **5.000** in the
> run-to-run topic *(TBC 25096)*, with no stated basis for either.
>
> The value determines what the check can see. Too thin and the profile is empty. Too thick and a
> real 3 cm offset is buried inside a 5 m band of points collected from either side of the plane.
>
> Establish working values for the checks in §18.5 and record them. *(Appendix I)*

## 18.7 Periodic system verification

Distinct from per-project QC. This is the check that the **instrument** is still performing.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, p.7)*
>
> Scan approximately **eight flat retro-reflecting targets** at varied distances over **more than
> 180° horizontally**, previously surveyed by total station. The system passes if residuals fall
> within the specified accuracy.
>
> Trimble recommends doing this "regularly" and "especially before starting an extensive data
> acquisition campaign" — and **gives no interval**.

> **PARAMETRIX DECISION REQUIRED**
>
> **Is this the periodic verification Parametrix adopts, and at what interval?**
>
> It is the only independent check on the system in any source — the only one that compares the
> MX60 against conventionally surveyed truth rather than against itself. Calibration (§14) checks
> the system's internal consistency; this checks its accuracy.
>
> Needs: an interval, a site, a target specification, and a pass criterion tied to the
> manufacturer's specified accuracy for the configuration Parametrix owns (§4.1).
> *(D-28, V-14; Appendix I)*

## 18.8 What to record

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> For each registered mission:
>
> | Record | Source |
> |---|---|
> | Residuals on **control** points used, by component | Targets pane / the report *(§17.6)* |
> | Residuals on **independent check** points | Same |
> | **Which points were control and which were checks** | **Recorded manually — TBC does not report it** *(§17.6)* |
> | Run-to-run RMS statistics, if used | Results tab *(TBC 25096)* |
> | Trajectory RMS picture | Screen capture of the RMS-coloured trajectory |
> | Visual check performed, by whom, covering what | **No software artefact exists** |
> | Results of Scan Generation | *(TBC 22499; §13.5)* |
> | Mission Report | *(TBC 23991_1)* |
>
> Two of those eight have no software artefact at all. **Not adopted.** *(D-29; §23)*

## 18.9 Acceptance

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes an acceptable point cloud at Parametrix?**
>
> **No numerical acceptance criterion appears anywhere in this document. No Trimble source in the
> set provides one, and inventing one would be indefensible.**
>
> The framework must combine **numerical residuals**, **independent check information** (§17),
> **visual inspection** (§18.5) and **the project accuracy requirement**. **It is set out in full
> once, in §24.3**, with why each component is necessary and why none is sufficient alone.
>
> The reason no single component suffices is §18.1: residuals measure fit to the observations
> that shaped the adjustment, and an adjustment with few observations — or with a systematic
> error common to all of them — fits beautifully and is wrong.
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."** *(D-13; §15.9, §24.3)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We looked at the evidence the software produces about how good the data
> is — residuals on control, agreement between overlapping passes broken into three directions, a
> colour-coded picture of where the trajectory solution struggled — and then we went and looked at
> the actual point cloud, because the numbers cannot finish the job.
>
> **Why it matters.** Trimble says this outright, twice, in two unrelated parts of its
> documentation: a good RMS does not prove the work succeeded, though a bad one proves it failed.
> That is not corporate caution. A residual tells you how well the adjustment fitted the numbers
> you handed it. Hand it three points and it fits them perfectly. Hand it three points that share
> a common error and it fits those perfectly too, and passes the error straight through. The
> arithmetic is not lying to you; it is answering a narrower question than the one you care about.
>
> **What can go wrong.** The spot-check. Mobile mapping error comes in stretches, not speckles,
> because it is driven by a filter that changes smoothly over minutes. A corridor that is
> flawless for two kilometres and 5 cm out for three hundred metres will pass every sample you
> take and fail the one place the client happens to measure. Dragging the cutting plane along the
> whole run is tedious and it is the check.
>
> The other one is subtler: forgetting to set the rendering to one colour per scan. In a single
> colour, two surfaces 4 cm apart look exactly like one surface 4 cm thick. You will look straight
> at the defect and not see it.
>
> **What good looks like.** Residuals on points the adjustment never saw, in the same range as the
> ones it used. Three axes of similar size rather than one dominating. A trajectory that is mostly
> one colour with short, expected degraded stretches. A wall at 50 m that is as thin as a wall at
> 10 m. And a cutting plane dragged the length of every overlap showing one of everything. None of
> that is a number you can put in a spreadsheet, which is exactly why somebody has to look.
