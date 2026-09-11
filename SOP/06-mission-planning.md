# 6. Mission Planning

## 6.1 The question this section answers

**What must be decided before anyone drives, so that the office has a defensible dataset to
process?**

Most of what goes wrong in the office cannot be fixed in the office. A GNSS-hostile stretch
driven once cannot be run-to-run registered. A corridor whose control sits inside the delivered
extent cannot be adjusted at the ends. Overlap that was not collected is not available.

## 6.2 Route and passes

### How many passes

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> The v1 draft stated a minimum of three passes on the pavement. **That figure is not traceable
> to a Trimble source in the current evidence set** and is carried here only so it is not lost.
> It must be confirmed, sourced or replaced before issue.

> **PARAMETRIX DECISION REQUIRED · D-41**
>
> **How many passes, and in what pattern, by roadway type?** The inputs are:
>
> - **Coverage and occlusion** — a single pass leaves the far side of parked vehicles, medians and
>   structures unmeasured
> - **Redundancy for run-to-run registration** (§16) — which needs "enough overlapping scan data
>   along the trajectories" *(TBC 25096)*
> - **LiDAR QC** (§12.7) — which needs runs "with overlap (parallel runs, or crossing runs)"
>   *(TBC 28972)*. **Without overlap, this remedy is unavailable in the office no matter what the
>   workstation can do**
> - Cost and road occupancy

> **IMPORTANT**
>
> **Two of the three degraded-GNSS remedies have to be arranged before you drive** (§20.3):
> control has to be surveyed, and overlap has to be collected. Discovering at QC that a corridor
> needed overlap you did not collect means going back.

### Direction of travel

Drive each pass in both directions where the corridor allows. It improves occlusion coverage, and
it is the geometry both the laser scanner calibration and LiDAR QC require (§14.3, §12.7).

## 6.3 GNSS planning

### Before mobilising

| Task | Why |
|---|---|
| **Check the almanac** for the planned window | Satellite geometry is knowable in advance; a poor window is avoidable |
| **Identify initialization locations** — a primary and a backup | §8.2 |
| **Map the GNSS-hostile stretches** | Below |

### Initialization locations need specific properties

> **EXISTING PARAMETRIX DRAFT PROCEDURE — CONFIRM BEFORE FINAL**
>
> - Open sky, away from buildings and canopy
> - Somewhere the vehicle can **safely sit still for 2–3 minutes**
> - Room to drive straight and perform dynamic manoeuvres afterwards (§8.2)

> **FIELD TIP**
>
> Scout them on aerial imagery before mobilising and pick two. Discovering that the chosen lot is
> fenced, occupied or under trees costs twenty minutes at the worst moment of the day.

### Map the hostile stretches, and estimate duration not length

Walk the route on imagery and mark tunnels, long underpasses, urban canyon, heavy canopy, deep
cuts and overhead structures.

> **For each, estimate how long the vehicle will be under it at collection speed.** That duration
> is the number that matters — a 300 m tunnel at 80 km/h is 13 seconds; the same tunnel at 20 km/h
> in traffic is nearly a minute.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Trimble publishes positioning performance at **no outage** and at a **60-second outage**
> *(MX60 UG Rev B, p.56)*.

> **IMPORTANT**
>
> **Trimble publishes nothing beyond 60 seconds.** A two-minute outage is not "twice as bad as one
> minute" — inertial drift is not linear, and beyond the published figure you are extrapolating
> past the manufacturer's stated envelope.
>
> Treat outages materially longer than 60 seconds as a **planning** problem, not a driving
> problem: additional control, planned overlap for LiDAR QC, DMI, or a different method for that
> segment (§20.7).

### Base station strategy

> **PARAMETRIX DECISION REQUIRED · D-42**
>
> **Own base on project control, VRS, RTX, or CORS post-processing — and what maximum baseline?**
>
> This interacts with D-19 (§5.3): **IN-Fusion+ Single Base** requires a local base station;
> **IN-Fusion+ PP-RTX** does not *(TBC 25943)*. The decision determines field logistics on every
> mission.

## 6.4 Timing

Three constraints that routinely conflict:

| Constraint | Wants |
|---|---|
| **GNSS geometry** | The best satellite window |
| **Imagery** | High sun, even light, no long shadows, dry surfaces |
| **Traffic** | Light traffic, so the corridor is not occluded by vehicles |

> **FIELD TIP**
>
> A good GNSS window at 07:00 is useless if the imagery is a wall of low-sun shadow, and an empty
> corridor at 05:00 is useless if it is dark. Where the three cannot be reconciled, decide which
> the deliverable actually depends on and say so in the project record.

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **Is night collection permitted, and under what conditions?** It solves the traffic-occlusion
> problem completely and makes the imagery unusable for interpretation. If it is permitted, the
> client must agree in advance and in writing.

## 6.5 Weather

Weather is a go/no-go decision, not a driving adjustment.

| Condition | Guidance | Source |
|---|---|---|
| **Rain or mist** | **Avoid operating the system** | *(MX60 UG Rev B, p.49)* |
| Wet pavement | Degrades laser returns; standing water may give no return at all | *(TMR §9.1)* |
| Heavy dew | Affects point cloud quality | *(TMR §9.1)* |
| Wet conditions, imagery | Water on the lens is grounds for rejection | *(TMR §10)* |
| Extreme dust | A dust filter is available — unpaved roads and mine sites *(Dust Filter Bulletin)* | |
| **Direct sun, stationary or < 10 km/h** | **Outside the rated operating envelope** | *(MX60 UG Rev B, p.53)* |

> **CAUTION**
>
> The Control Unit and Power Unit are **IP30 — not waterproof.** They live inside the vehicle for
> a reason. *(MX60 UG Rev B, p.53)*

> **PARAMETRIX DECISION REQUIRED · D-44**
>
> **One clear wet-weather rule.** Trimble says avoid operating in rain or mist; TMR says do not
> capture imagery in wet conditions; **neither defines "wet."**
>
> The rule should give the operator **explicit authority to stand down without seeking approval**.
> An operator who has to phone for permission will drive.

## 6.6 Access, traffic and safety

Mobile mapping removes the crew from the roadway. It does not remove the vehicle.

Plan for: road occupancy permits where required, the vehicle's behaviour in traffic at collection
speed (§8.5), locations where the vehicle must stop or turn, restricted or private access, and
any client or jurisdictional notification.

> **Vehicle operation, traffic control and site safety are governed by Parametrix's health and
> safety procedures and by the client's requirements. This SOP does not restate them and does not
> override them** (§1.3).

## 6.7 The calibration site

Plan it once and reuse it. Requirements are in **§14.3** and repeated here because they are a
planning task, not a processing one.

| Requirement | Value | Source |
|---|---|---|
| Four runs — two roads crossing, each driven both ways | | *(TBC 24886)* |
| **Crossing angle** | 90°, tolerance **± 30°** | *(TBC 24886)* |
| **Minimum run length** | ≥ **20 m each side** of the crossing | *(TBC 24886)* |
| **Ideal run length** | **80 m — 40 m each side** | *(TBC 24886)* |
| **Façades** present in each direction | | *(TBC 24886)* |
| **Vegetation** — few or none | | *(TBC 24886)* |
| For LiDAR QC as well: **250–300 m per strip**, structured scene, **open sky** | | *(TBC 28972)* |

> **FIELD TIP**
>
> A quiet crossroad with buildings on all four approaches, few trees, room for 125–150 m on each
> arm, and no traffic-control complications. Finding one is a morning's work. Finding one under
> schedule pressure, the week a calibration is overdue, is not.

> **PARAMETRIX DECISION REQUIRED · D-24**
>
> **Where is the Parametrix calibration site, and who maintains it?** *(§14.7)*

## 6.8 Identify what mobile mapping will not get

> **IMPORTANT · a professional judgement point**
>
> Part of planning is deciding what this method cannot deliver on this corridor:
>
> - Surfaces occluded from the roadway — behind walls, inside structures, beyond a crest
> - Detail finer than the point density at the achievable standoff
> - Features under a long GNSS outage where none of the §20 remedies is available
> - Anything requiring an accuracy the trajectory cannot support in that environment
>
> **Mobile mapping may not be the appropriate acquisition method for a particular segment.**
> Conventional survey, static scanning or total station work may produce a more defensible result
> there. Identifying that at planning is a professional judgement, and it is cheaper and more
> honest than delivering a weak segment mixed in with a good corridor.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Record, in the project file before mobilising: the segments where mobile mapping is expected to
> be marginal, the mitigation chosen for each, and the segments where another method is proposed.
> *(Register item 45)*

## 6.9 The planning record

Full checklist in **Appendix B**.

| ☐ | Item |
|---|---|
| ☐ | Corridor extent and pass pattern defined |
| ☐ | Control plan complete and bracketing the extent (§5.6) |
| ☐ | Independent check points designated in writing (§17.4) |
| ☐ | GNSS-hostile stretches mapped, with **outage duration** estimated |
| ☐ | Mitigation chosen for each — control, overlap, or another method |
| ☐ | Initialization locations identified, primary and backup |
| ☐ | Base station strategy fixed |
| ☐ | Collection window agreed against GNSS, imagery and traffic |
| ☐ | Weather go/no-go understood by the operator |
| ☐ | Calibration currency confirmed (§14.7) |
| ☐ | Segments unsuitable for mobile mapping identified and communicated |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We planned the drive: how many passes and in which directions, where to
> initialize, which stretches will lose satellites and for how long, when to collect, and what to
> do about the parts of the job this method will not handle well.
>
> **Why it matters.** Almost nothing here can be fixed later. If a tree-lined kilometre is driven
> once, the office cannot register it run-to-run, cannot refine it with LiDAR QC, and has only
> whatever control you happened to set. The decisions that determine whether the office has
> options are all made before anyone turns a key.
>
> **What can go wrong.** The one that costs a return visit is estimating obstruction by length
> instead of by time. A tunnel is not a distance problem; it is a duration problem, and the same
> tunnel in traffic can be four times the outage it is at speed. Trimble publishes performance at
> a sixty-second outage and nothing beyond, so anything longer is off the edge of the specification
> and needs a plan, not optimism.
>
> The other is quieter: planning a single pass because coverage looks adequate, and removing two of
> the three ways the office could have rescued a bad stretch.
>
> **What good looks like.** A route marked up with the hostile stretches and an estimated outage
> duration on each. A mitigation chosen for every one of them, before mobilisation. Two
> initialization spots, both scouted. Control that brackets the job. And an explicit note saying
> which parts of the corridor mobile mapping is not the right tool for — written down and sent to
> the client while there is still time to do something about it.
