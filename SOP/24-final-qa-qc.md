# 24. Final QA/QC

## 24.1 What this section is

The point where every earlier check converges, performed once, before the data leaves Parametrix.

> **IMPORTANT**
>
> **Final QA/QC is not a single RMS number and cannot be reduced to one.**
>
> Trimble's own position, stated in two separate topics: **bad RMS can demonstrate failure; good
> RMS does not by itself demonstrate success** *(TBC 24886, 25096)*. A final check built on one
> number would pass exactly the datasets most likely to be wrong — those with sparse control, or
> with a systematic error common to every observation (§18.1).
>
> What follows is a **layered verification**. No layer is sufficient alone; the confidence comes
> from their agreement.

## 24.2 The ten layers

| # | Layer | Answers |
|---|---|---|
| 1 | **Mission completeness** | Did we collect what we said we would? |
| 2 | **Trajectory quality** | Where was the navigation solution weak? |
| 3 | **Coordinate system verification** | Do the coordinates belong where we think? |
| 4 | **Control usage** | Were the checks genuinely independent? |
| 5 | **Registration results** | Did the adjustment work? |
| 6 | **Point cloud visual QC** | Does the data look right where numbers cannot reach? |
| 7 | **Corridor continuity** | Is it right *everywhere*, not just where we looked? |
| 8 | **Imagery QC** | Is the imagery complete and usable? |
| 9 | **Export state verification** | Is the exported file the data we checked? |
| 10 | **Deliverable review** | Is the package correct and openable? |

---

### Layer 1 · Mission completeness

Was all intended corridor coverage actually collected?

| Check | Evidence |
|---|---|
| **Covered distance** against the planned extent and the field record | Mission properties *(TBC 22499)* |
| **Run count** against the field record | Project Explorer |
| **Coverage in plan** — drive the trajectory in Plan View against the project extent | Plan View |
| Gaps, aborted runs and re-drives noted in the field record | §9, §10 |

> Trimble provides covered distance and run count. **The planned extent and the field record are
> Parametrix artefacts** — this layer only works if §9 produced them.

### Layer 2 · Trajectory quality

Review the trajectory solution rather than treating the mission as uniformly good or bad.

| Check | Evidence |
|---|---|
| **RMS colouring** of the trajectory in Plan View | *(TBC 25943, 27248; §12.4, §18.4)* |
| **Trajectory Plots** from the SBET computation | *(TBC 27415)* |
| **Suspect stretches identified and listed**, not averaged away | — |

> **The purpose of this layer is to produce a list, not a verdict.** A mission is not "good" or
> "bad"; it has stretches. Identifying them directs Layers 5, 6 and 7 to where they matter, and
> tells a reviewer where the residual risk sits.

> **Note the limit.** Registered segments render in the **"Undefined RMS"** colour *(TBC 27248)*,
> so a registered trajectory no longer shows its original RMS in those stretches. Where possible,
> review the RMS picture **before** registration as well as after.

### Layer 3 · Coordinate system verification

| Check | Evidence |
|---|---|
| **Project CRS** matches the control network and the client requirement | Project settings; §5 |
| **Vertical datum and geoid** as specified | Project settings |
| **Epoch**, where a time-dependent datum is in use | *(TBC RN 2026.10; §12.6)* |
| **SBET filename** — `sbet_[mission].out` or `sbet_[mission]_[frame].out` | *(TBC 25943; §12.4)* |
| **Scale factor handling at export** — grid or ground, sidecar present | *(TBC 11769, 27279; §22.5)* |

> **IMPORTANT · read the SBET filename correctly**
>
> The `_[frame]` form is a **documented indicator that POSPac used the frame-transformation
> workflow** — it computed in ITRF00 and then transformed. That is all it is.
>
> | It tells you | It does **not** tell you |
> |---|---|
> | That an additional transformation occurred | That the transformation parameters were right |
> | Where to direct scrutiny | That the project CRS is set up correctly |
> | | That the final point cloud is accurate |
>
> **The plain filename is equally not proof of correctness** — it means only that POSPac
> recognised the datum and epoch it was given, which may still be the wrong ones. Treat either
> form as a flag for review, never as a verdict.

### Layer 4 · Control usage

Confirm that the checks were genuinely independent.

| Check | Evidence |
|---|---|
| **Which points were Use XY, Use Z, As Check** | *(TBC 22905, 26473)*. **Reloadable via Edit a Run / Edit a Mission** *(TBC 25362, 26578)* — TBC is not documented as reporting it otherwise (§17.6) |
| **Check points were designated before the adjustment and not changed during it** | Parametrix record (§17.4) |
| **At least one point was not a check** — TBC enforces this, but the near-miss is invisible | *(TBC 22905)* |
| **Check point distribution** — along the corridor, in each GNSS environment, near each end | §17.5 |

> **CAUTION**
>
> **Confirm that check points were not allowed to drive the adjustment.** The failure this guards
> against is a processor who saw a check residual they disliked and ticked the point into the
> adjustment. Every step of that is well intentioned; the result is an adjustment measured against
> itself.
>
> On current evidence the only way to confirm this after the fact is to **reload the registration
> through Edit**, which restores the original Use XY / Use Z / As Check choices *(TBC 25362,
> 26578)*, and compare against the designation recorded before processing began.

### Layer 5 · Registration results

| Check | Evidence |
|---|---|
| **Numerical residuals on control used**, by component | Targets pane; signed in the report from 2025.21 *(TBC RN 2025.21; §17.6)* |
| **Residuals on independent check points** | Same |
| **Run-to-run RMS statistics**, where used — three axes, every 20 m, `No overlap` rows read | *(TBC 25096; §16.6)* |
| **Registration type used, and whether it suited the error** | *(TBC 22905; §15.5)* |
| **For a Local adjustment: was the delivered extent bracketed by control?** | §15.5 — it does not extrapolate |
| **Visual alignment** | Layer 6 |

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **Bad RMS can demonstrate failure. Good RMS does not by itself demonstrate success.** This layer
> is not complete without Layers 6 and 7.

### Layer 6 · Point cloud visual QC

| Check | Method |
|---|---|
| **Overlapping passes** | Cutting Plane View, **rendering set to Scan Color**, point size increased, plane dragged along the run *(TBC 25096, 24886; §18.5)* |
| **Flat surfaces at range** | Thickening with distance |
| **Ends of the corridor** | Where a Local adjustment stopped; where the smoother had data on one side only |
| **The suspect stretches from Layer 2** | Did the registration actually fix them? |
| **Features near control vs far from control** | Residual growth with distance from constraint |

> **IMPORTANT · the rendering setting is part of the check**
>
> **Set rendering to Scan Color — one colour per scan — before looking for misalignment.**
>
> In a single colour, **two surfaces 4 cm apart look exactly like one surface 4 cm thick.** You
> will look directly at the defect and not see it. The visualisation setting is not a display
> preference here; it is what makes the check possible.

### Layer 7 · Corridor continuity

> **CAUTION**
>
> **Do not rely solely on isolated spot checks.**
>
> Mobile mapping error is **correlated in time, not scattered** (§2.3). It arrives in stretches
> because it is driven by a filter that evolves smoothly over seconds and minutes. A corridor that
> is excellent for 2 km and 5 cm out for 300 m **will pass every spot check you take** and fail at
> the one place the client happens to measure.
>
> The inspection strategy must be capable of identifying **localised** degradation, which means
> traversing the corridor rather than sampling it.

> **PARAMETRIX DECISION REQUIRED**
>
> **What is the corridor continuity inspection method, and at what interval or coverage?**
>
> No Trimble source prescribes one. The method must be able to detect a degraded stretch shorter
> than the sampling interval, which rules out sparse spot checks. Candidate approaches — dragging
> the cutting plane continuously, a systematic interval tied to the Layer 2 suspect list,
> deviation analysis against a reference surface — have different costs and different detection
> limits.
>
> *(Register item 39)*

### Layer 8 · Imagery QC

| Check | Evidence |
|---|---|
| **Coverage** for the full corridor | §19.3 |
| **Exposure, blur, obstruction, contamination** | §19.3 |
| **Corrupted images** — exported as **black**, silently | *(TBC 23339, 22501; §19.4)* |
| **Colour fringing at feature edges** on colorized clouds | §19.5 — indicates camera boresight (§14.4) |
| **Blur applied where required** | §19.6 |

> **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED**
>
> A **file-size scan** of exported imagery as a screening method for black images. **Not a Trimble
> procedure and not yet validated** — see §19.4 for the logic and its limits. **File size alone
> cannot establish image validity.**
>
> **This is not mandatory and should not be treated as a required step until validated.**
> *(Register item 31)*

### Layer 9 · Export state verification

> **CAUTION · carry this from §22.2**
>
> **Confirm that the exported point cloud represents the intended final trajectory and
> registration state, to the extent TBC permits that to be verified.**
>
> **Registration does not modify the point cloud until Update Scans is performed** (§13.6). An
> operator can complete a registration, obtain good residuals, pass Layer 5 — and export data that
> still reflects the pre-registration trajectory.

| Check | Evidence |
|---|---|
| **Scan nodes selected for export sit beneath the intended registered trajectory** | *(TBC 22638, 22905, 26473)* |
| **Stations carry the `_reg_####` suffix** | *(TBC 22638)* |
| **The trajectory's properties** read `Origin: Registration result`, with the expected `Input trajectory` and `Registration type` | *(TBC 22905, 26473)* |
| **Export timestamps setting recorded** — and §22.3 understood | *(TBC 23339, 22501)* |
| **Scaling recorded** — grid or ground; sidecar present if grid | *(TBC 11769, 27279)* |

> **FIELD TESTING REQUIRED · T29** — the reliable verification method **for each export path** is
> not established; how an export dialog resolves its selection is undocumented (§22.2). Until
> tested, the project-side checks above, performed immediately before export and recorded, are the
> only defensible verification. *(Appendix E)*

### Layer 10 · Deliverable review

Performed on the exported files, not in TBC.

| Check |
|---|
| **Expected files exist** — the full set, named as agreed |
| **Expected extents are present** — open the data and compare against the project extent |
| **Coordinate system is correct** |
| **Units are correct** |
| **Each file opens successfully** in software other than the one that wrote it |
| **Point count and file size are plausible** for the extent and density |
| **Imagery exists where required**, and a systematic sample has been opened and looked at |
| **Sidecars exist where required** — the scaling `.txt`, `reference.csv`, `.lst`, `.cal`, per §22.6 |
| **No obviously corrupted output** |
| **Project-specific deliverable requirements are met** |

> **No acceptance limits are stated here.** Point count, file size and extent are checked for
> **plausibility against the project**, not against any figure in this document. Project-specific
> acceptance limits are set per job and are not invented here.

---

## 24.3 Acceptance

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes acceptance of a mobile mapping deliverable at Parametrix, who signs it, and
> against what?**
>
> **No numerical acceptance criterion appears anywhere in this document. No Trimble source in the
> set provides one, and inventing one would be indefensible.**
>
> The framework must combine four things, and a rule built on any one alone will fail:
>
> | Component | Why necessary | Why not sufficient |
> |---|---|---|
> | **Numerical residuals** on control used | Objective, repeatable | Measures fit to its own observations (§18.1) |
> | **Independent check information** | The only numerical evidence of accuracy | Sparse — a handful of points cannot characterise a corridor |
> | **Visual inspection** | Catches what no number reports | Subjective, and dependent on who looked and how |
> | **Project accuracy requirement** | The only thing that makes a threshold meaningful | Varies per job; not a property of the system |
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."**
>
> *(Register item 13; §15.9, §18.9)*

## 24.4 The record

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted.** A final QA/QC record covering the ten layers, naming who performed each and
> when, plus the provenance record proposed in §23.6.
>
> Two layers — 6 and 7 — produce **no software artefact whatsoever**. If a reviewer asks whether
> the visual check was performed and over what extent, the only possible answer is a record
> somebody wrote. *(Register item 29)*

## 24.5 Blocked pending resolution

These should be settled before a final QA/QC procedure is signed off:

| Item | Why it blocks |
|---|---|
| **T18** — Export timestamps and reprocessing | Layer 9 cannot be completed while it is unknown whether a documented export option substitutes different data |
| **T29** — per-path export verification | Layer 9's method is not established |
| **T28** — Cleanup and the SBET files | Determines what must be archived before the project is tidied (§21, §23.5) |
| **Register item 39** — continuity method | Layer 7 has no defined method |
| **Register item 13** — acceptance framework | Layers 5 and 10 have no threshold |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We ran a single, structured check over the whole job before it left the
> building — ten layers, from "did we collect the whole corridor" through to "does the file the
> client gets actually open."
>
> **Why it matters.** Every layer catches something the others cannot. The numbers catch a broken
> adjustment. The independent check points catch an adjustment that fitted its own observations
> beautifully and is still in the wrong place. The visual check catches what neither number
> reports. And the last two layers catch the case where all the analysis was right and the wrong
> file went out.
>
> **What can go wrong.** Three things, and they are the same three throughout this document.
>
> **Trusting a good number.** Trimble says it plainly, twice: a bad RMS proves failure, a good one
> proves nothing on its own. If the only evidence is a small residual, you have not checked the
> work — you have checked the arithmetic.
>
> **Spot-checking a corridor.** The error comes in stretches. Two kilometres perfect and three
> hundred metres out will pass every sample you take, and the client will measure in the three
> hundred.
>
> **Exporting before updating the scans.** The adjustment lives on the trajectory until somebody
> runs Update Scans. Skip it and you deliver the version from before the registration — same file
> size, same extents, opens fine, centimetres out.
>
> **What good looks like.** The covered distance matches the plan. The trajectory picture shows
> short degraded stretches where you expected them, and you have a list of them. Points the
> adjustment never saw come back in the same range as the ones it used. A cutting plane dragged
> the length of every overlap — in scan colour — shows one wall, not two. The imagery has been
> opened, not counted. The exported scans sit under the registered trajectory. And somebody has
> written down that all of that happened, because two of these checks leave no trace in the
> software at all.
