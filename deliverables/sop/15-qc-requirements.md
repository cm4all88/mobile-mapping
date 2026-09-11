# 15. Quality Control Requirements

## 15.1 The principle this section rests on

> **CAUTION**
>
> Trimble states, in identical words in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

**A number can prove failure. A number cannot prove success.** Only two things can suggest success:
observations that took no part in the adjustment, and looking at the data
*(Technical Manual §23)*.

Everything in this section follows from that, and it is why QC here is **layered** rather than a
single test. A residual measures how well an adjustment fitted the observations it was given. That
is a narrower question than the one that matters.

## 15.2 The layers

Each layer catches something the others cannot. **None of them is optional because another was
performed.**

| # | Layer | Catches | Artefact |
|---|---|---|---|
| 1 | **Field coverage verification** (§10.2) | Missing passes, missing overlap | Field record |
| 2 | **Intake checks** (§12.2) | Transfer loss, wrong CRS, missing sensors | Intake record |
| 3 | **Trajectory RMS review** | Where the solution was weak — **before any point cloud exists** | Screen capture |
| 4 | **Residuals on control** | A broken adjustment | Targets pane |
| 5 | **Residuals on independent check points** | An adjustment that fits its own observations and is still wrong | **Recorded manually** |
| 6 | **Visual inspection of the point cloud** | Doubled surfaces, thickening at range, systematic tilt | **No software artefact** |
| 7 | **Imagery inspection** | Coverage gaps, exposure, blur, corrupted images | **No software artefact** |
| 8 | **Export-state confirmation** (§18.2) | Delivering the unregistered cloud | Screen capture |

> **Two of the eight layers produce no software artefact at all.** If a reviewer asks whether the
> visual check was performed and over what extent, the only possible answer is a record somebody
> wrote.

## 15.3 Trajectory RMS review

**The trajectory shall be reviewed in RMS colouring before the point cloud is inspected.**

It is available before any point cloud exists, it costs seconds, and it says where the solution
degraded, for how long, and whether the degradation is at the ends of the mission
*(Technical Manual §24)*. That determines where to look in every later layer.

## 15.4 Residuals

| | |
|---|---|
| Residuals on **control** points used in the adjustment are recorded, by component | |
| Residuals on **independent check points** are recorded, by component | These are the ones that mean something (§7.3) |
| **Which points were control and which were checks is recorded manually** | **TBC does not report it** *(Technical Manual §22.7)* |

> **TESTING REQUIRED · T21, V-11**
>
> TBC 2025.21 states that signed residuals are "included in the report" without naming it, and the
> only mobile mapping report topic does not mention residuals. **Whether the residuals can be
> produced as a report, or must be transcribed by hand, determines how this record is kept.**
> Answerable in ten minutes with the software open.

## 15.5 Visual inspection

> **PARAMETRIX PROCEDURE (PROPOSED) · D-27**
>
> A visual QC pass over a registered mission covers:
>
> | Check | Looking for |
> |---|---|
> | **Overlapping passes in Cutting Plane View**, dragged the full length | Doubled surfaces |
> | **Flat surfaces at range** — a wall, a building face | Thickening with distance: attitude error or a calibration issue |
> | **The ends of the corridor** | Where a Local adjustment stopped; where the smoother was weakest |
> | **The degraded stretches identified at layer 3** | Whether the registration actually fixed them |
> | **Vertical surfaces against horizontal** | Systematic tilt |
> | **Features near control versus far from control** | Residual growth with distance from constraint |

> **IMPORTANT**
>
> **Set the rendering to Scan Color for this.** Without it, two offset surfaces read as one thick
> one and the defect the check exists to find is invisible *(Technical Manual §25)*.

> **TESTING REQUIRED · T16**
>
> The working cutting-plane thickness for these checks.

> **PARAMETRIX DECISION REQUIRED · D-39**
>
> **The corridor continuity inspection method and its coverage** — how much of a corridor is
> inspected, and how that is decided.

## 15.6 Imagery inspection

> **PARAMETRIX PROCEDURE (PROPOSED) · D-27**
>
> | Check | Looking for |
> |---|---|
> | **Coverage** | Gaps where a camera stopped, or a run was not colorized |
> | **Exposure** | Blown highlights, blocked shadows under canopy and in underpasses — both unrecoverable |
> | **Motion blur** | Speed too high for the light available |
> | **Obstruction** | Aerials, a following vehicle, a smear on the dome |
> | **Focus and contamination** | Rain, dust, insects on the optical surface |
> | **Corrupted images** | **These are silent** — a corrupted side camera image exports as black |
> | **Alignment with the point cloud** | Colour in the wrong place at feature edges indicates a camera boresight issue |

> **PARAMETRIX DECISION REQUIRED · D-31**
>
> Whether the proposed **file-size scan** for detecting silently corrupted imagery is adopted. It is
> a screening method proposed by this project and **not validated** *(Technical Manual §26)*.

## 15.7 What QC shall not do

**A QC layer shall not be substituted by another.** In particular, good residuals do not remove the
requirement for visual inspection, for the reason in §15.1.

## 15.8 Records this section requires

> **PARAMETRIX PROCEDURE (PROPOSED) · D-29**
>
> For each registered mission:
>
> | Record | Source |
> |---|---|
> | Residuals on control points used, by component | Targets pane |
> | Residuals on independent check points, by component | Same |
> | **Which points were control and which were checks** | **Manual — TBC does not report it** |
> | Run-to-run RMS statistics, if used | Results tab |
> | Trajectory RMS picture | Screen capture |
> | **Visual check performed, by whom, covering what extent** | **No software artefact exists** |
> | **Imagery check performed, by whom** | **No software artefact exists** |
> | Results of Scan Generation | §13.3 |
> | Mission Report | §17.3 |
