# 13. QUALITY, CONTROL AND LIMITS

The longest section, because it answers the question that matters: **is this data good
enough, and where isn't it?**

It is told once, in one place, because trajectory quality, point cloud quality, control
and QC are not four subjects — they are one subject seen from four angles.

---

## 13.1 Understanding the trajectory

### Why everything depends on it

From Section 2: every point inherits the trajectory's error at the instant it was
measured. The scanner's own accuracy — 2 mm, precision 2.5 mm at 30 m
*(MX60 UG Rev B, p.54)* — is a small contributor to your final number.

The trajectory has six components at every instant:

| Component | Comes from |
|---|---|
| **X, Y, Z position** | GNSS, bridged and smoothed by the IMU |
| **Roll, pitch** | IMU, referenced to gravity |
| **Heading** | IMU, inferred from motion — or directly from GAMS |

### How trajectory error becomes point error

**Position error** shifts points. A 10 cm position error moves every point collected at
that instant by 10 cm, in the same direction. This is the easy case: it is a translation,
and control can partly correct it.

**Attitude error rotates points, and the effect grows with range.** This is the case people
underestimate.

A small angular error at the sensor becomes a large positional error at distance. The
approximate lever is:

```
position error ≈ range × angular error (in radians)
```

Worked from Trimble's published figures *(MX60 UG Rev B, p.56)*:

| Angular error | At 10 m | At 30 m | At 100 m |
|---|---|---|---|
| 0.005° (Core/Pro roll-pitch) | 0.9 mm | 2.6 mm | 8.7 mm |
| 0.0025° (Premium roll-pitch) | 0.4 mm | 1.3 mm | 4.4 mm |
| 0.015° (heading, with GAMS) | 2.6 mm | 7.9 mm | 26 mm |

> **WHY THIS MATTERS**
>
> This table is the mathematical reason for the "useful range" concept in Section 2. The
> cloud is most accurate near the vehicle and degrades with distance — not because the
> laser gets worse, but because attitude error is multiplied by range.
>
> It is also why **attitude accuracy is the headline difference between Premium and
> Core/Pro**. At the roadway it barely matters. At 100 m it is a factor of two.

### GNSS outages and IMU bridging

When GNSS is lost, the IMU carries the solution alone. It does this well briefly and
badly eventually, because inertial errors accumulate — small biases integrate into
velocity error, which integrates into position error.

Trimble publishes two points on this curve *(MX60 UG Rev B, p.56)*:

| Condition | Core / Pro | Premium |
|---|---|---|
| **No outage** | X,Y <0.01 m · Z 0.01 m | X,Y <0.01 m · Z 0.01 m |
| **60-second outage** | X,Y 0.12 m · Z 0.10 m | X,Y 0.10 m · Z 0.07 m |

Note both are post-processed with POSPac and assume the **DMI option** and best
conditions.

> **IMPORTANT**
>
> Trimble publishes nothing beyond 60 seconds. Do not extrapolate — inertial drift is not
> linear, and a two-minute outage is not twice a one-minute outage. Beyond 60 seconds you
> are outside the manufacturer's stated envelope and into territory that must be verified
> by check points, not predicted.

**What helps during an outage:**

| Aid | Effect |
|---|---|
| **DMI** | Constrains distance travelled; supplies ZUPT information. This is what it is for *(MX60 UG Rev B, p.42)* |
| Smooth driving | Fewer unmodelled dynamics for the IMU to absorb |
| Short exposure | The only real fix — plan the route so outages are brief |
| Passes from both directions | The outage falls at a different point in each solution |

**What does not help:** driving faster to get through it sooner. You reduce the outage
duration but add dynamics at exactly the wrong moment.

### Reading the trajectory afterwards

TMR requires a trajectory string "attributed with RMSE values on each vertex... during
capture," plus an explicit statement of "how the IMU (and wheel encoder if fitted)
observations are applied during times of degraded, lost, or obstructed GNSS signal
reception" *(TMR MLS Guideline §14, p.25)*.

> **FIELD TIP**
>
> Plot the trajectory's reported accuracy against the route before you look at anything
> else. The spikes tell you where to concentrate your QC — and they will line up with the
> overpasses, canyons and canopy you mapped in Section 5.

---

## 13.2 Point cloud quality

### What degrades it, and how

The most useful distinction is **missing data vs. noisy data vs. wrong data**, because
they have different causes and different remedies.

| Cause | Effect | Remedy |
|---|---|---|
| **Occlusion** — traffic, parked cars, vegetation, barriers | **Missing** | More passes, other direction, night collection, conventional survey |
| **Beyond useful range** | **Wrong** (degraded accuracy, looks fine) | Understand and state useful range |
| **Wet surfaces, standing water** | **Missing** — no return | Do not collect wet |
| **Rain, mist, spray, snow** | **Noisy** — returns off airborne particles | Do not operate in rain or mist *(MX60 UG Rev B, p.49)* |
| **Dust** | **Noisy** | Dust filter, but only on unpaved roads and mine sites |
| **Glass, water, polished metal** | **Missing or wrong** — specular reflection | Expect gaps; verify by imagery |
| **Retro-reflective signs** | Blooming, saturated returns | Normal; usually still usable |
| **Grazing incidence** — far pavement, steep slopes | **Noisy and sparse** | Passes from both directions |
| **Excessive speed** | **Sparse** — lower point density | Reduce speed |
| **Moving vehicles** | **Wrong** — a car in the cloud that is not there | Cleansing, in the office |
| **Vehicle vibration, harsh manoeuvres** | **Noisy** | Drive smoothly |

### Range and reflectivity

Maximum range is **150 m at the lower measurement rate, 120 m at the higher**
*(MX60 UG Rev B, p.54)*. Those figures assume *(p.55)*:

- Flat targets larger than the beam diameter
- **Perpendicular** angle of incidence
- Atmospheric visibility of **23 km**
- And explicitly: **range is shorter in bright sunlight than under an overcast sky**

> **WHY THIS MATTERS**
>
> Every one of those conditions is optimistic relative to a real roadside. A dark, wet,
> obliquely-angled surface at 100 m in bright sun is nothing like the specification case.
> Treat published range as a ceiling, not an expectation.

### Density

Point density is set by measurement rate, line speed, range, and **vehicle speed**. TMR
notes speed is "a major factor affecting the final point density" *(§9.4.1, p.12)*.

TMR's approach is worth adopting: rather than specifying a density number, require a
**statement** of the density and pattern achieved at a stated speed, on defined surfaces
at defined distances *(§9.4.3, pp.12–13)*.

### Multiple passes and what they buy

Three things, per Section 5: redundancy, changed GNSS constellation, and shadow reduction.

But there is a subtlety worth knowing *(TMR Note 1, §9.4.3, p.14)*:

> "Multiple scans can achieve a higher overall density of points, but if there are any
> issues with aligning multiple Pointcloud scans together, the definition of features can
> become a problem if the point density is not high enough in each individual scan."

> **IMPORTANT**
>
> Passes are not a substitute for a good single pass. If each individual pass is sparse or
> poorly registered, stacking three of them produces a thicker, blurrier cloud — not a
> better one.

### Useful range — state it

TMR requires the contractor to state the width over which the cloud actually meets project
accuracy, noting a cloud may reach 200 m while the compliant portion is "considerably
less" *(§11.7, p.18)*.

Their worked example of an acceptable statement:

> "The MCPPC supplied meets or exceeds the accuracy requirements for this project between
> the edges of pavement."

> **IMPORTANT — the point scale factor trap**
>
> Laser scanners measure **plane** distances. Deliverables are usually **grid**
> coordinates. TMR warns of errors "of up to 40 mm / 100 m due entirely to Point Scale
> Factor," and says this must be considered in any useful range statement
> *(§11.7, p.19)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether Parametrix issues a useful range statement with every mobile mapping
> deliverable.
>
> *Recommended practice:* yes, on every project. It is a few lines in the survey report, it
> is defensible, and it prevents the most common and most expensive client
> misunderstanding — that everything visible in the cloud is surveyed to the same standard.

### Cleansing

Moving vehicles and other transient objects appear as real points.

> **IMPORTANT**
>
> TMR's rule is the right one: **reclassify, do not delete.**
>
> "It is recommended that data is not deleted but pushed to other files or classified in
> such a way so that it can be separated from the clean data. Care should be taken as
> removal of non-erroneous data during a cleansing process may result in the MLS
> contractor having to re-supply datasets."
> *(TMR §11.8.1, p.19)*

---

## 13.3 Imagery quality

Imagery fails differently from LiDAR, and it fails for reasons LiDAR does not care about.

| Factor | Effect |
|---|---|
| **Low sun angle** | Under- and over-exposure. TMR: avoid early morning and late afternoon; **8am–4pm usually ideal** *(§10, p.15)* |
| **Direct sun into lens** | Flare, blown highlights |
| **Deep shadow** | Unusable detail in shadowed areas |
| **Rain, water on lens** | **Grounds for rejection** *(TMR §10, p.15)* |
| **Dirty lens** | Haze across every frame from that camera |
| **Motion** | Blur — mitigated by the global shutter *(MX60 UG Rev B, p.53)* |
| **Traffic, pedestrians** | Occlusion, and privacy exposure |
| **Wrong exposure setting** | Correctable live in TMI — see below |

**Live exposure control** is available while driving *(TMI UG Rev L, pp.34–35)*: the
panoramic camera has an **Auto** button plus a slider mixing exposure time and gain; the
back-down camera has an exposure compensation slider. Left darker, right brighter.

> **FIELD TIP**
>
> Check the Camera view when lighting changes materially — entering a tree tunnel, turning
> into the sun, coming out of a cutting. An exposure set for open highway is wrong under
> canopy, and unlike LiDAR you cannot fix it afterwards.

**Focus is fixed, and the ranges matter** *(MX60 UG Rev B, pp.53–54)*:

| Camera | Sharp from |
|---|---|
| Spherical, Core | 0.7 m to infinity |
| Spherical, Pro/Premium | Calibrated 2.0 m to infinity |
| **Back-down camera** | **2.0 m to 9.0 m** |

That back-down range is why the vehicle needs a **minimum roof height of 1.60 m**
*(MX60 UG Rev B, p.59)*.

**Capture triggering** is by distance or by time, max 10 fps spherical, 9 fps back-down
*(MX60 Spec Sheet p.2)*. Distance-based gives even spatial coverage regardless of speed —
usually what you want.

> **IMPORTANT**
>
> Imagery must be captured **at the same time as the point cloud** to be a valid record of
> site conditions. TMR is explicit: capture at a different time does not meet the
> requirement, because conditions change *(§10, pp.14–15)*.

### Privacy

Mobile mapping imagery captures faces, licence plates, and private property incidentally.
No Trimble document addresses this.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the imagery privacy policy: whether faces and plates are blurred, who may
> access raw imagery, what is delivered to clients, retention period, and how requests for
> removal are handled.
>
> *Recommended practice:* treat raw imagery as internal and restricted. Where imagery is
> delivered or published, apply face and plate blurring. Set this before the first project
> that publishes imagery, not after.

---

## 13.4 Control and mobile mapping

This is not a section on control surveying. It covers only how control interacts with
mobile mapping.

### Two different jobs — do not confuse them

| | **Control points** | **Check points** |
|---|---|---|
| Purpose | **Improve** the solution | **Verify** the solution |
| Used in | Registration / adjustment | Independent testing only |
| If used for both | The test is meaningless | — |

> **IMPORTANT**
>
> A point used to register the cloud cannot then be used to verify it. It will fit,
> because you made it fit. Independent check points must be held out of the adjustment
> entirely.

### How control is used

TBC registers mobile mapping runs to fixed control points explicitly to "reduce, or
eliminate, IMU drift," using the smart picking tool and the POSPac PFix engine
*(TBC Technical Notes, p.4)*.

Control points must be **identifiable in the point cloud**. TMR calls these "Clearly
Defined Points" and gives examples *(App F, pp.32–33)*:

- Corners of concrete — bridge abutments, culverts
- Centres of light poles or posts
- Ends of line marking strings
- Guardrail posts
- Targets specifically placed for the purpose

### Where control goes

TMR's minimum *(App E, p.31)*:

- A ground control point **adjacent to the start and end** of the project
- A ground control point at **all intersections of state-controlled roads**, so future
  collections match

And for check sites, the stated intent is what makes them useful *(App F, p.32)*:

> "The intention of all the check sites is to gather an understanding of the accuracies
> achieved in areas of **both good and poor GNSS coverage** as well as close to and half
> way between [control marks]."

> **IMPORTANT**
>
> Check points only in open sky tell you the best case. Deliberately place them where you
> expect trouble — that is where you need to know.

### Base stations

Short baselines between base station and vehicle give the best positional outcome
*(TMR §5.2, p.6; §7.2, p.8)*. TMR requires 1-second epochs or better and dual-frequency
receivers *(§7.2, p.8)*.

> **ADVANCED — redundancy at the base is not redundancy at the vehicle**
>
> TMR makes a point worth absorbing:
>
> "If [base stations] are occupied simultaneously, there is only a redundancy in the GNSS
> observation at the [base marks], but generally **NO redundancy at the vehicle**.
> Therefore, concurrent base station observations only constitute a **partially
> independent** GNSS reading."
> *(§7.1, p.8)*
>
> Two base stations do not give you two independent measurements of where the vehicle was.
> Real redundancy at the vehicle comes from repeat passes at different times.

### Identifying systematic problems

| Symptom | Likely cause |
|---|---|
| Constant offset over a whole run | Base station coordinate error, or datum/epoch mismatch |
| Offset growing with distance from control | Trajectory drift between constraints |
| Vertical bias only | Geoid model, antenna height, or lever-arm Z error |
| Run-to-run disagreement, one direction consistently off | Boresight error |
| Disagreement worsening with range from vehicle | Attitude error — see §13.1 |
| Step at a run boundary | Registration issue; TMR: steps are "unacceptable" *(§8.3, p.10)* |

> **FIELD TIP**
>
> **Run-to-run disagreement is your best free QC measure.** Before you register the runs
> together, look at how far apart they are. That difference is a direct, independent
> measure of the system's internal consistency — and once you batch-register them, it is
> gone. Record it first.

---

## 13.5 The QC process

### Field QC — before leaving site

| ☐ | Check | Fail action |
|---|---|---|
| ☐ | NAV green throughout collection | Note stretches at orange or red |
| ☐ | **Thick blue line over every intended stretch** | Re-drive the missing run — now |
| ☐ | Camera and laser buttons green all mission | Investigate; the data may be incomplete |
| ☐ | Waterfall view showed sensible data | Investigate before leaving |
| ☐ | No disk Warning or Error | Do not reuse the disk |
| ☐ | Finalize sequence completed | Cannot be added later |
| ☐ | Field protocol complete | Complete it now |

### Office QC — after processing

| # | Question | How to answer |
|---|---|---|
| 1 | Did the system operate correctly? | System log, TMI Message Log (Alarm/Warning filter), field protocol |
| 2 | Is the trajectory acceptable? | Trajectory report; plot reported accuracy along the route; check both initializations |
| 3 | Is the point cloud complete? | Compare coverage against the project limits; look for gaps |
| 4 | Do the runs agree with each other? | **Run-to-run comparison, before registration** |
| 5 | Does independent control agree? | Check points held out of the adjustment |
| 6 | Are there areas of excessive noise? | Visual review; cross-sections through suspect areas |
| 7 | Are important features occluded? | Review against the deliverable list |
| 8 | Is imagery usable? | Review exposure, blur, lens cleanliness, coverage |
| 9 | Does anything need recollection? | See the decision table below |
| 10 | Does anything need conventional supplementation? | Compare against the Section 5 list |

### Acceptance categories

| Category | Meaning | Action |
|---|---|---|
| **ACCEPT** | Meets project requirements throughout the stated useful range | Proceed to delivery |
| **REVIEW** | Localised issues that may be acceptable depending on the deliverable | Project surveyor decides; document the decision |
| **SUPPLEMENT** | Data is sound but incomplete for the deliverable | Conventional survey fills the gaps |
| **RECOLLECT** | Trajectory or coverage failure over a material extent | Re-mobilise |

> **PARAMETRIX DECISION REQUIRED**
>
> Set the numerical tolerances that separate these categories.
>
> **No tolerances are proposed here**, because none of the Trimble documents provide them
> and TMR deliberately leaves its values as per-project variables — its uncertainty
> formulas appear as `(x) mm`, `(y) mm + (yy) ppm`, and so on, filled in by a project
> checklist that is not in our source set *(TMR App A–D, pp.27–30)*.
>
> *Recommended practice:* adopt a recognised US framework — ASPRS *Positional Accuracy
> Standards for Digital Geospatial Data* (2014) or NSSDA — and set default project
> tolerances against it, allowing per-project override. Adopt TMR's **structure** even if
> not its numbers, because the structure is sound:
>
> - **Horizontal survey uncertainty** — vector between a clearly defined point in the cloud
>   and the same point by independent means, at 95% *(App A, p.27)*
> - **Horizontal relative uncertainty** — distances within a sliding window of up to 200 m
>   agree to `(y) mm + (yy) ppm` *(App B, p.28)*
> - **Vertical survey uncertainty** — height difference on hard surfaces at 95%
>   *(App C, p.29)*
> - **Vertical relative uncertainty** — height differences within a 200 m sliding window
>   *(App D, p.30)*
>
> Absolute *and* relative matter. A cloud can be biased 5 cm and internally excellent —
> fine for volumes, wrong for tying to existing control. The reverse is also possible.

### Periodic system verification

Trimble's own recommended check, worth adopting as a scheduled procedure
*(MX60 UG Rev B, p.7)*:

> Register a scan position by scanning a number (e.g. 8) of flat retro-reflecting targets
> at different distances and at angles covering more than 180° horizontally, which have
> also been surveyed by a highly accurate total station. **The check is passed if the
> residual error is less than the instrument's specified accuracy.**

Trimble "strongly recommends" checking data quality regularly, "especially before starting
an extensive data acquisition campaign."

> **PARAMETRIX DECISION REQUIRED**
>
> Adopt this as a scheduled Parametrix verification, and set the interval.
>
> *Recommended practice:* establish a permanent target array at a Parametrix facility,
> surveyed conventionally. Run the check quarterly, before any major campaign, and after
> any event that could have disturbed the system. Retain results as a performance history —
> a trend is far more informative than a single pass/fail.

### QC deliverables

TMR's reporting list is a good starting template *(§14, p.25)*:

| ☐ | Item |
|---|---|
| ☐ | System reports — component calibration, alignment, self-tests |
| ☐ | Trajectory with accuracy values attributed along it |
| ☐ | Statement of how IMU (and DMI) observations are applied during degraded or lost GNSS |
| ☐ | Evidence of how scans from each scanner join |
| ☐ | Compliance report — cloud against control, horizontal and vertical |
| ☐ | **Useful range statement** |
| ☐ | Survey report, signed, including any areas where accuracy was not achieved |

> **IMPORTANT**
>
> TMR requires that "if there are areas where the contractor has not achieved the accuracy
> specified, the MLS contractor shall identify these areas in the Survey Report"
> *(§14, p.26)*.
>
> Disclose shortfalls. A documented limitation is a professional judgement. An undisclosed
> one discovered by the client is something else.

---

## 13.6 When mobile mapping does not work well

### What the system can and cannot see

**Can see:** anything with line of sight from a sensor about 2 m above the road, within
useful range, that reflects enough light, during the pass.

**Cannot see:**

| Cannot see | Why |
|---|---|
| Behind barriers, walls, dense vegetation | No line of sight |
| Under parked vehicles | Occluded |
| Inside structures — invert elevations, pipe conditions | No line of sight |
| Deep ditches, steep back slopes | Below the sensor's line of sight |
| Beneath water | No return |
| Through glass | Specular / transparent |
| Anything requiring physical contact or interpretation | Not a measurement problem |
| Monuments, boundary evidence | Requires professional judgement and recovery |
| Areas the vehicle cannot reach | Not driven |

### Environments that degrade or defeat it

| Environment | Problem | Mitigation |
|---|---|---|
| **Tunnel** | Total GNSS loss, potentially far beyond 60 s | DMI; short transit; control at both ends; verify with check points |
| **Underground parking** | Total loss, plus no initialization possible | Usually the wrong tool |
| **Urban canyon** | Multipath and partial loss — often worse than a clean outage | Multiple passes at different times; DMI; more check points |
| **Heavy canopy** | Intermittent loss, plus occlusion of everything above | Passes both directions; seasonal timing; supplementation |
| **Dense traffic** | Occlusion of curb and roadside | More passes; off-peak or night |
| **Standing water** | No return; hides the surface | Do not collect; return when dry |
| **Long GNSS outage** | Trajectory drift beyond published spec | See §13.1 |

> **WHY THIS MATTERS — multipath is worse than a clean outage**
>
> A total outage is honest: the system knows it has no GNSS and relies on the IMU, which
> is well characterised for about a minute.
>
> An urban canyon is not honest. The receiver still gets signals — reflected off buildings,
> arriving late, implying a position that is wrong. The filter may weight that bad
> observation as though it were good.
>
> This is why TMR requires extra passes at different times in poor GNSS environments
> *(§8.2, p.10)*: a different constellation gives a different, uncorrelated multipath
> pattern.

### Recollection decision

| Situation | Decision |
|---|---|
| A run was not recording | **Recollect** that run |
| NAV red across a material extent | **Recollect** |
| Trajectory failed check points over a material extent | **Recollect**, or supplement |
| Localised occlusion of a required feature | **Supplement** conventionally |
| Imagery unusable, LiDAR sound | Recollect **imagery** only, if imagery is a deliverable |
| Point density insufficient for the deliverable | **Recollect** at lower speed |
| Feature is fundamentally not visible from the road | **Supplement** — recollection will not help |

> **IMPORTANT**
>
> The last row is the one that gets missed. If a feature cannot be seen from the roadway,
> driving it again changes nothing. Recognise this at planning (Section 5), not after a
> second mobilisation.

> **PARAMETRIX DECISION REQUIRED**
>
> Define who authorises recollection and how remobilisation cost is handled — whether it
> falls to the project, to overhead, or is recoverable from the client depending on cause.
>
> *Recommended practice:* the project surveyor decides, with the project manager informed
> before mobilisation. Record the cause in the survey report — a pattern of recollections
> from the same cause is a training or equipment signal, not bad luck.

---

## References — Section 13

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 7, 42, 49, 53–56, 59 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 34–35 |
| Trimble MX60 Spec Sheet, PN 022516-737C (04/25) | 2 |
| Trimble Business Center Technical Notes: For Mobile Mapping, October 2022 | 4 |

## Other References — Section 13

| Source | Sections |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §5.2 p.6; §7.1–7.2 p.8; §8.2–8.3 p.10; §9.2.2 p.11; §9.4.1 p.12; §9.4.3 pp.12–14; §10 pp.14–15; §11.7 pp.18–19; §11.8.1 p.19; §14 pp.25–26; App A–D pp.27–30; App E p.31; App F pp.32–33 |
| NCHRP, *Practices for Collecting, Managing, and Using Lidar Data*, 2024 | Ch.5, Quality Assurance, pp.80–82 |
