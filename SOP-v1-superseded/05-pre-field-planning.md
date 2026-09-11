# 5. PRE-FIELD PLANNING

This section covers only what is different about planning a *mobile mapping* job. It
assumes you already know how to plan a survey.

The short version: **you are planning a drive, not a set of setups.** Almost every
decision here is about where the vehicle goes, when, and how many times.

## 5.1 Route and passes

### How many passes

Trimble's documents do not specify a pass count. Queensland TMR's guideline does, and it
is the most defensible standard available:

> A minimum of **three passes** shall be run on the pavement.
> *(TMR MLS Guideline §8, p.8)*

The reasoning matters more than the number:

- **Redundancy** — three observations of the same surface let you detect a bad one
- **Changing constellation** — passes separated in time see a different GNSS geometry,
  which reduces the effect of multipath
- **Shadowing** — a truck blocking the curb on pass 1 is somewhere else on pass 3

> **IMPORTANT**
>
> TMR is explicit that a **multi-scanner system does not escape this**. Two scanners
> capturing simultaneously share one GNSS constellation and one trajectory, so they
> provide coverage redundancy but **not positional redundancy**:
>
> > "On MLS vehicles using multiple scanners to give the multiple aspect coverage in one
> > pass by capturing two or more scans at the one time, these scans do not use
> > independent GNSS constellations. In this case, a minimum of three independent passes
> > are still generally required."
> > *(TMR MLS Guideline §8, p.8)*
>
> The MX60 has two scanners. Plan passes as though it had one.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the Parametrix minimum pass standard, and who may authorise fewer.
>
> *Recommended practice:* adopt three passes as standard for survey-grade work. TMR
> permits fewer only by prior agreement and warns that "extreme caution should be
> exercised and is NOT a recommended practice" *(§8, p.8)*. Allow reduction only with
> written approval from the project surveyor, recorded in the survey report.

### Pass patterns by roadway type

| Roadway | Minimum pattern |
|---|---|
| **Single carriageway, multiple lanes** | One pass each direction, plus a third in either direction |
| **Single carriageway, divided lanes** | If scans from each direction don't fully overlap, three passes per direction |
| **Dual carriageway** | If carriageways don't fully overlap, three passes each; at least one run in the left-hand through lane of each carriageway |
| **Any lane not fully overlapped by the adjacent lane's scan** | Three passes of that lane |

*(TMR MLS Guideline §8.1, pp.9–10)*

### Direction of travel

Plan it, and record it. The field protocol requires the **order and direction of runs**
*(QSG Rev B, p.14)*.

Direction matters because the sensor's view is asymmetric in practice — a curb, a sign
face, or a barrier is seen well from one direction and poorly from the other. Two-way
coverage is what fills those shadows.

> **FIELD TIP**
>
> Drive the lane closest to what you care about. If the deliverable is curb-and-gutter,
> the outside lane gives you a much better look at it than the inside lane does.

## 5.2 GNSS planning

This is the one piece of conventional survey planning that changes materially.

### Check the almanac

Trimble builds this into their own office checklist:

> Check satellite almanac (`www.gnssplanning.com/#/charts`)
> *(QSG Rev B, p.14)*

You are looking for windows of good satellite count and low PDOP over your corridor,
and — just as importantly — **avoiding** windows where the constellation is weak.

> **WHY THIS MATTERS**
>
> In static GNSS work a poor window costs you time. In mobile mapping it costs you the
> whole run, because you cannot go back and reoccupy — the vehicle has already driven
> the corridor and everything it collected inherited that geometry.

### Identify initialization locations

You need **open sky at both ends of the mission** — one to initialize, one to finalize.

Requirements *(QSG Rev B, pp.11, 14)*:

- Good GNSS visibility and PDOP
- Away from high buildings and obstructions that reduce reception and increase multipath
- Somewhere you can **safely sit still for 2–3 minutes**
- Room to drive straight ~20 m and perform 2–3 dynamic turns

Good candidates: large parking lots, wide intersections in open areas, rural road ends,
highway rest areas.

> **FIELD TIP**
>
> Scout initialization points on aerial imagery before you mobilise, and pick two —
> primary and backup. Discovering that your chosen lot is fenced, occupied, or under a
> canopy of trees costs 20 minutes at the worst moment of the day.

### Map the GNSS-hostile stretches

Walk the route on imagery and mark:

- Tunnels and long underpasses
- Urban canyon — tall buildings both sides
- Heavy tree canopy
- Deep cuts and overhead structures

For each, estimate **how long the vehicle will be under it at collection speed.** That
duration is the number that matters, not the length.

| Outage duration | Expectation |
|---|---|
| Brief (seconds) | IMU bridges it comfortably |
| **60 seconds** | Trimble publishes degraded but specified performance: X,Y 0.10–0.12 m, Z 0.07–0.10 m *(MX60 UG Rev B, p.56)* |
| Well beyond 60 s | Outside published specification — treat as a planning problem, not a driving problem |

> **IMPORTANT**
>
> Trimble specifies positioning performance at no outage and at a **60-second** outage.
> They publish nothing beyond that. A two-minute tunnel is not "twice as bad as one
> minute" — IMU drift is not linear, and you are extrapolating past the manufacturer's
> stated envelope.
>
> Plan long outages deliberately: a DMI, extra passes from both directions, or
> conventional survey supplementation. Section 13 covers the consequences.

TMR places responsibility squarely on the operator here:

> "It is the responsibility of the MLS contractor to increase the number of passes or
> implement other strategies in poor GNSS environments. These areas shall be reported to
> the project manager and noted in the survey report."
> *(TMR MLS Guideline §8.2, p.10)*

## 5.3 Timing

Three separate clocks constrain when you collect.

| Constraint | Window | Source |
|---|---|---|
| **Satellite geometry** | Whenever PDOP is good | QSG p.14 |
| **Imagery lighting** | Avoid early morning and late afternoon — **8am–4pm usually ideal** | TMR §10, p.15 |
| **Traffic** | Whenever the road is least occluded | — |

These frequently conflict. A good GNSS window at 7am is useless if the imagery is a
deliverable.

> **FIELD TIP**
>
> If imagery is not a deliverable and shadowing is the main problem, **night collection**
> is a legitimate tool. TMR explicitly permits it for parked-vehicle occlusion:
>
> > "If there is a problem with parked vehicles in urban areas, then consideration should
> > be given to scanning at night when parked vehicles may be absent."
> > *(TMR MLS Guideline §9.3, p.12)*
>
> LiDAR does not need daylight. Cameras do.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix position on night collection: when it is permitted, what
> additional safety measures apply, and how the loss of usable imagery is handled with
> the client.
>
> *Recommended practice:* permit night collection where imagery is not a deliverable and
> parked-vehicle occlusion would otherwise force recollection. Require it to be agreed
> with the client in advance, because the imagery *will* be unusable for interpretation.

## 5.4 Weather

Weather is a go/no-go decision, not a driving adjustment.

| Condition | Guidance | Source |
|---|---|---|
| **Rain or mist** | **Avoid operating the system** | MX60 UG Rev B, p.49 |
| Wet pavement | Degrades laser returns; standing water may give no return at all | TMR §9.1, p.11 |
| Heavy dew | Affects point cloud quality | TMR §9.1, p.11 |
| Wet conditions for imagery | Make a considered effort not to capture; water on the lens is grounds for rejection | TMR §10, p.15 |
| Extreme dust | Dust filter available — unpaved roads and mine sites only | Dust Filter Bulletin, p.1 |
| Direct sun, stationary or <10 km/h | Outside the rated operating envelope | MX60 UG Rev B, p.53 |

> **CAUTION**
>
> The Control Unit and Power Unit are **IP30** — not waterproof. They live inside the
> vehicle for a reason. *(MX60 UG Rev B, p.53)*

> **PARAMETRIX DECISION REQUIRED**
>
> Write one clear wet-weather rule. Trimble says avoid operating in rain or mist; TMR
> says don't capture imagery in wet conditions; neither defines "wet."
>
> *Recommended practice:* no collection during active precipitation. After rain, wait
> until the pavement is visibly dry before collecting, and note conditions in the field
> protocol. Give the operator explicit authority to stand down without seeking approval.

## 5.5 Access, traffic and safety

Mobile mapping removes the crew from the roadway, but it does not remove the vehicle.

**Plan for:**

- **Legal and physical access** to every part of the corridor — gated roads, private
  drives, restricted areas
- **Turnarounds** — cul-de-sacs, medians, where a U-turn is legal
- **Traffic control**, if any pass requires an unusual manoeuvre or speed
- **Total vehicle height.** The system adds height, and the driver must know the new
  clearance *(MX60 UG Rev B, p.9)*
- **Safe stopping locations**, for initialization and for problems

> **CAUTION**
>
> The system adds significant height to the vehicle. Check clearances on the planned
> route — low bridges, parking structures, drive-throughs, and the shop door at the
> office. *(MX60 UG Rev B, p.9)*

> **PARAMETRIX DECISION REQUIRED**
>
> Define traffic control requirements by roadway class, and the go/no-go criteria for
> collecting without it.
>
> *Recommended practice:* no traffic control needed where the vehicle travels at or near
> the prevailing speed in a normal lane. Require a traffic control plan wherever the
> collection speed would be materially below prevailing traffic, or where a pass requires
> stopping, reversing, or occupying a shoulder.

## 5.6 Control planning

Detail is in Section 13. At the planning stage you need to decide two things.

**1. What service level is this?**

TMR distinguishes two, and conflating them is expensive:

| Service level | Control approach |
|---|---|
| **Survey-grade** | Full project reference frame, base stations, ground control points, check points |
| **Asset-grade** | A "GNSS only solution" — appropriate "where asset information is the primary objective," minimising initial control cost while keeping enough rigour to post-control later if needed *(TMR §11, p.17)* |

**2. Where does control go?**

TMR requires, at minimum:

- A ground control point **adjacent to the start and end** of the project
- A ground control point at **all intersections of state-controlled roads** within the
  project area, so future collections match

*(TMR MLS Guideline, Appendix E, p.31)*

Short baselines between base station and vehicle give the best positional outcome
*(TMR §5.2, p.6; §7.2, p.8)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the Parametrix control standard for mobile mapping: base station strategy
> (own base, VRS, RTX, or CORS post-processing), maximum baseline length, control point
> spacing, and independent check point density.
>
> *Recommended practice:* own base stations on project control, with baselines kept
> short. Control at both project ends and at every significant intersection. Independent
> check points at a spacing set per project, placed in **both good and poor GNSS
> environments** — TMR's stated intent is "to gather an understanding of the accuracies
> achieved in areas of both good and poor GNSS coverage" *(Appendix F, p.32)*, which is
> exactly what you need to know.

## 5.7 The calibration site

Boresight calibration needs a **specific drive**, not a normal collection, and the site
has to meet real geometric requirements. Plan it once and reuse it.

**What the crew must collect** — four runs over one crossroad:

| Run | Direction |
|---|---|
| Run_0 / Run_1 | Along the first road, forward and backward |
| Run_2 / Run_3 | Along the crossing road, forward and backward |

**Site requirements** *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*:

| Requirement | Value |
|---|---|
| Crossing angle | As near **90°** as possible, within **±30°** |
| Run length | ≥ **20 m each side** of the crossing; ideally **80 m total, 40 m each side** |
| Overlap | Sufficient between runs |
| **Façades** | Present **in each direction**, in sufficient quantity |
| Vegetation | **Few or none** |

> **WHY THIS MATTERS**
>
> Boresight angles are solved by comparing the same surfaces seen from opposing
> directions. Flat façades make an angular error show up as a visible gap between two
> point clouds; pavement viewed at a grazing angle barely constrains it. The orthogonal
> pair supplies the axes a single road cannot. Vegetation is excluded because soft,
> non-repeating returns add noise to exactly that comparison.

> **FIELD TIP**
>
> A quiet crossroad with buildings on all four approaches, few trees, and room for 40 m of
> clean run each way is not common. Find one, record it, and use it every time.

Section 12.3 covers what happens to the data afterwards.

> **PARAMETRIX DECISION REQUIRED**
>
> Identify and record a standard Parametrix calibration site meeting the requirements
> above.
>
> *Recommended practice:* scout one near the office, document it with an aerial image and
> the four run lines, and note it in the field protocol whenever a calibration mission is
> driven.

## 5.8 Identify what mobile mapping will not get

Do this at planning, not at delivery.

Walk the corridor on imagery and mark anything that will need conventional survey:

- Features behind barriers, walls, or dense vegetation
- Drainage structures — invert elevations, pipe sizes, anything inside a structure
- Deep ditches and steep side slopes below the sensor's line of sight
- Anything under permanently parked vehicles
- Monuments and boundary evidence
- Areas the vehicle cannot reach

> **WHY THIS MATTERS**
>
> This list is not a shortcoming to be hidden. It is a scope item to be priced. A project
> that discovers it needs conventional supplementation *after* the mobile mapping crew has
> demobilised pays for two mobilisations.

Section 13 covers the full picture of what the system can and cannot see.

## 5.9 Planning checklist

| ☐ | Item |
|---|---|
| ☐ | Project limits defined and mapped |
| ☐ | Route, pass count, and direction of travel planned per pass |
| ☐ | Satellite almanac checked for the collection window |
| ☐ | Two initialization locations identified — primary and backup, both ends |
| ☐ | GNSS-hostile stretches mapped, with estimated outage duration |
| ☐ | Strategy for each long outage — passes, DMI, or supplementation |
| ☐ | Collection window reconciled against lighting and traffic |
| ☐ | Weather forecast checked; stand-down criteria understood |
| ☐ | Access confirmed; turnarounds identified |
| ☐ | Vehicle height clearances checked on route |
| ☐ | Traffic control decided |
| ☐ | Service level agreed — survey-grade or asset-grade |
| ☐ | Control and check point plan set |
| ☐ | Conventional supplementation identified and scoped |
| ☐ | Calibration site identified, if a calibration mission is due |

---

## References — Section 5

| Source | Pages |
|---|---|
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 9, 49, 53, 56 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 11, 14 |
| Trimble Business Center Help: *Calibrate Mobile Mapping Laser Scanners* | help.fieldsystems.trimble.com/tbc/20716.htm |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60, January 2025 | 1 |
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §5.2 p.6; §7.2 p.8; §8 p.8; §8.1 pp.9–10; §8.2 p.10; §9.1 p.11; §9.3 p.12; §10 p.15; §11 p.17; App E p.31; App F p.32 |
