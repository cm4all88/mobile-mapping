# 15. Registration

This is the section the rest of the office workflow exists to support. Read §2 and §13 first.

## 15.1 What registration is, in this system

**Registration adjusts the trajectory.** It does not move points.

TBC takes surveyed ground control points, pairs each with a point the operator picks in the
point cloud, and computes a correction to the trajectory that reduces the difference between
the pairs. The output is a **new trajectory**, stored beside the imported one. The existing
point cloud is untouched until you deliberately recompute it (§13.6).

> **This is the single most important structural fact about TBC registration, and it surprises
> people from a static scanning background.** In static work, registration moves scans. Here it
> produces a better path, and the points follow only when you ask them to.

### The three commands

They are **not interchangeable**. Each solves a different problem with a different kind of
observation.

| Command | What constrains it | Scope | Section |
|---|---|---|---|
| **Register a Run** | Surveyed GCPs ↔ targets picked in the cloud | One run | §15.3 |
| **Register a Mission** | The same, with each GCP reusable across runs and passes | A set of runs at once | §15.4 |
| **Register Run to Run** | **Cloud-to-cloud overlap** against a fixed reference run | Pairs, batched | **§16** |

> **IMPORTANT**
>
> Register Run to Run uses **no surveyed control at all**. It makes two runs agree with each
> other. Two runs can agree perfectly and both be in the wrong place. It is a relative tool, and
> §16 explains where it belongs in a controlled workflow.

## 15.2 What TBC means by "target"

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **ground control point (GCP)** is "an accurately surveyed coordinate location for a physical
> feature that can be identified on the ground, e.g., a corner on the pavement markings."
>
> A **target** is "a point extracted from the acquired scan data." *(TBC 22905)*

The target is **not** a physical panel. It is a point the operator picks in the point cloud,
which TBC then pairs with a surveyed GCP. A painted road-marking corner is as legitimate a GCP
as a checkerboard panel — and in corridor work, far more common.

> **FIELD TIP**
>
> This shapes control design (§6). A GCP for mobile mapping registration has to be something you
> can *find in a point cloud* at the density and incidence angle the vehicle produced — which is
> a different requirement from something you can occupy with a prism. A painted stop-bar corner
> is excellent. A survey nail in asphalt is nearly useless: it is a few millimetres across, and
> the cloud will not resolve it.

## 15.3 Register a Run

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*

### Prerequisites

- **At least one generated scan on the run.** The command is dimmed otherwise
- **A GCP file imported into the project** — Shape, ASCII or CSV. Imported points appear in Plan
  View and under the **Points** node

### The sequence

1. In **Project Explorer**, select a run
2. Generate its scans if not already done (§13)
3. Import the GCP file
4. **Mobile Mapping ▸ Processing ▸ Register a Run**
5. Accept the default **Registration Name** (*RunName* Trajectory) or enter one. **This name is
   given to the computed trajectory** — it is what you will be identifying months later (§23)
6. Choose a **Registration Type** (§15.5)
7. Select a GCP under the **Points** node and click **Add Selection to Control Points**
8. Set **Use XY**, **Use Z**, **As Check** for that point (§17)
9. Optionally enable **Activate Limit Box** — a flat box in Plan View or a 3D box in 3D View that
   hides everything outside it, "to remove potential parasitic points over the target"
10. Optionally set **Activate Target-Bundle Adjustment** (§15.7)
11. Select the point in the **Control Points** list. It centres in Plan View and **Point Cloud
    Smart Picking** opens
12. Pick the target, read the residuals, and **Validate** (§15.6)
13. Repeat for further points, or adjust an existing pick
14. **Compute**. The adjusted trajectory draws in **blue**; the original stays **green**
15. Add or modify pairs and recompute as needed
16. **Apply**

### What Apply produces

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*
>
> - An **adjusted trajectory node** nested beneath the run, beside `Sbet`
> - A new **SBET file on disk**: `sbet_<date>_reg_####.out`, in the project folder,
>   **incrementing** with each registration — `_reg_0001`, `_reg_0002`, and so on
> - Picked targets renamed *RunName TrajectoryGCPName*; the updated targets carry a trailing `*`
> - Trajectory properties carrying **`Origin: Registration result`**, **`Input trajectory:
>   Imported trajectory`**, and **`Registration type:`** the method used

> **Those four properties and the numbered SBET file are your provenance record.** They are the
> strongest evidence available that a given point cloud was built on a given adjustment. §23 is
> about how far that evidence travels — and it does not travel as far as you would like.

### A note for single-scanner acquisition

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "In case of a single head configuration (one high-end laser scanner acquisition), it does not
> matter which scan is used (left or right) for the registration." *(TBC 22905)*

## 15.4 Register a Mission

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 26473)*

Register a Mission registers "a set of runs at the same time" rather than sequentially, and —
this is the point of it — **lets every GCP be used more than once**, with different run point
clouds or different passes of the same run.

### How it differs from Register a Run

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP *instance*** |
| Instances | — | TBC creates one per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left, right, or both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | *RunName TrajectoryGCPName* | ***RegistrationName*_*GCPName*_*RunName*** |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |
| Unused instances | — | "All unused instances are removed from the Control Points list" |

### Why this is probably the normal case

Consider an ordinary corridor: driven in both directions, perhaps twice, with control set along
it. A single painted mark is visible in four passes. Under Register a Run it constrains one of
them. Under Register a Mission it constrains all four **simultaneously**, and the four runs come
out mutually consistent because they were adjusted against the same observation.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Register a Mission should be the default for corridor work, with Register a Run reserved for
> single-run situations and for repairing one run within an otherwise accepted mission.**
>
> **Not adopted.** The reasoning is above and follows from Trimble's description, but it is a
> production convention and Parametrix should decide it deliberately — including whether a
> mission registration should be redone from scratch when one run is later re-collected.
> *(Register item 12)*

## 15.5 Registration Type — and the one that does not extrapolate

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*

| Method | What it does | Trimble's stated use |
|---|---|---|
| **Global** | A shift of the whole trajectory, **without rotation**. No local adjustment near control | "situations where there are consistent differences between the laser data and the ground control points. A situation in which the data can be corrected with a simple shift" |
| **Local** | Local adjustment **with interpolation between** control points | "suitable for a local adjustment of a run, **not for systematic error along the run or for adjusting outside the ground control points set**" |
| **Global, and then Local** | Global first, then Local | *No separate guidance given* |

> **CAUTION**
>
> **Local does not extrapolate.** Trimble says so directly: it is not for "adjusting outside the
> ground control points set."
>
> Beyond the first and last control point along a run, a Local adjustment does not correct the
> trajectory. The cloud at the ends of the corridor is left on the imported trajectory while the
> middle is adjusted — and there is no visual indication of where the adjustment stopped.
>
> **The practical consequence for control design:** control must bracket the extent you intend
> to deliver, not merely fall within it. A GCP 200 m inside each end of a 3 km corridor leaves
> 400 m unadjusted at the tails. §6 and §17 return to this.

> **FIELD TESTING REQUIRED · T15**
>
> **Which registration type, when?** Trimble describes the mechanism of each and gives no
> selection rule beyond "consistent differences." **Global, and then Local** receives no guidance
> at all, and is the method shown in every screenshot Trimble publishes.
>
> Do not adopt a default from the screenshots. Test the three methods on a representative
> corridor with independent check points and compare. *(Appendix E)*

## 15.6 Target picking, and reading residuals before you commit

This is where the operator's judgement enters the adjustment, and TBC gives real help.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905)*

### Picking types

| Type | Use |
|---|---|
| **Default** | Snap to a cloud point near the GCP. Not for road marks or plane intersections |
| **Intersected Plane** | Fits a plane near the rough pick and projects the pick onto it |
| **Road Mark** | Picks a point on a **pavement marking edge line** |

Within **Intersected Plane**, a target template may be applied:

| Template | Predefined dimension |
|---|---|
| Single Pick | — |
| Checkerboard | 0.500 m middle line |
| Diamond | 0.400 m edge length |
| Rectangular | 0.500 × 0.500 m |
| GV Target (L-shape) | 0.080 m bolt |

### The Validate Picking window

Each pick opens **Validate Picking**, which shows:

- An overhead view of the projected point
- A **side view perpendicular to the trajectory**
- The 3D coordinates of the pick
- The **RMS of the fitted plane**
- **Direct residuals to the GCP**, updating live as the template is adjusted

> **IMPORTANT**
>
> **The residuals are shown before you commit the pick, and they update as you nudge it.**
>
> That changes the working method. This is not "pick everything, compute, then discover the
> problem." It is *pick, read the residual, adjust, then validate* — and the operator should be
> forming a judgement about each observation as they make it, exactly as they would reject a bad
> total station shot at the instrument rather than in the office.
>
> Live residuals update when the target centre moves (by picking a new centre, or with the
> keyboard arrows, including fine adjustment with **Shift**) or when the GV Target bolt size
> changes *(TBC 22905; TBC RN 2026.10)*.

Rendering can be changed to **Gray-Scale Intensity**, **Color-Coded Intensity** or **Color By
Distance to Plane**, and for Intersected Plane an **Intensity** slider reduces contrast on
targets with reflective parts.

### Two warnings TBC raises

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> One icon means "the picked point is not a 3D point (no Z coordinate) and/or does not belong to
> the scan of the run to register."
>
> The other means "the picked point **does not belong to the most recent scan** of the run to
> register."
>
> "In both cases, pick again a new target." *(TBC 22905)*

> **The second warning deserves attention.** It means the pick landed on a superseded scan — an
> earlier generation, or one built on a different trajectory. Registering against it would be
> adjusting a trajectory to fit a cloud produced by a different trajectory. TBC catches it. It is
> a good illustration of why superseded scan sets are a hazard worth managing (§21, §23).

### The 30 m rule

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "The distance in a pair of points cannot exceed the allowed maximum distance of **30 meters (or
> 100 feet)**." *(TBC 22905, 26473)*

A pair exceeding it is rejected. In practice this is a sanity limit, not a working tolerance — a
GCP and its picked target should be a few centimetres apart, not tens of metres. Hitting this
limit means the wrong feature was picked.

### Minimum observations

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "A pair of a ground control point (GCP) and a picked target is **enough to perform the
> registration**." *(TBC 22905)*

> **CAUTION**
>
> **One pair is enough for TBC. It is nowhere near enough for survey work.**
>
> A single pair gives a shift with no redundancy, no residual to inspect and nothing to check it
> against. TBC will compute it, apply it, and report residuals of zero — because with one
> observation and three unknowns the fit is exact and meaningless.
>
> **How many pairs are required, at what spacing, is PARAMETRIX DECISION REQUIRED** and is
> treated in §17. Do not infer a Parametrix minimum from Trimble's software minimum.

## 15.7 Target-Bundle Adjustment — the option whose name reads backwards

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22905, 26473)*

| State | Bundle adjustment interval | Trimble's stated fit |
|---|---|---|
| **Checked** | **250 m** acquisition intervals | "few GCPs… accuracy of the GCPs is moderate… precision in target picking is less stringent" |
| **Unchecked** | **70 m** acquisition intervals | "more GCPs available… accuracy of the GCPs is high and precise target picking is necessary" |

> **IMPORTANT**
>
> **Checking the box makes the adjustment coarser, not finer.** The name implies you are turning
> something on that will improve the result. What you are turning on is a longer averaging
> interval, appropriate when you have few or moderate-quality control points.
>
> For survey-grade work with dense, well-surveyed control and careful picking, **unchecked** is
> what Trimble's own description points to. This document does not adopt that as a rule.

> **FIELD TESTING REQUIRED · T9**
>
> Trimble ties the choice to three conditions at once — GCP density, GCP accuracy, and picking
> precision — which will rarely all point the same way. The default state is not stated.
>
> Test both states on a representative dataset with independent check points. *(Appendix E)*

## 15.8 Editing a registration — not the same as registering again

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25362, 26578)*

**Edit a Run** and **Edit a Mission** reopen an existing registration and improve it "not by
incrementing each time the adjusted trajectory but by **editing the same (imported)
trajectory**."

Re-running Register on an already-registered run stacks a new adjustment and creates a new
numbered trajectory. **Edit** reloads the original registration's parameters — registration type,
each GCP's Use XY / Use Z / As Check choices, and the paired targets — and lets you add, remove
or re-pick pairs, then recompute **from the imported trajectory**.

| | Register (again) | **Edit** |
|---|---|---|
| Starts from | The current trajectory | **The imported trajectory** |
| Output | A further incremented trajectory | *RunName*_Trajectory2 |
| **Reset available?** | **No** — "There is no restoration when you register the trajectory of a run but only when you edit it" | **Yes** — restores modified targets to their initial picked position, restores deleted pairs, removes added pairs, and restores the original Use XY / Use Z / As Check choices |

> **CAUTION**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

## 15.9 Judging the result

Covered fully in §18, but the governing principle belongs here because it is where the temptation
to shortcut is greatest.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Trimble's position, in identical wording in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

> **The asymmetry is the whole point. A number can prove failure. A number cannot prove
> success.**
>
> That is not a quirk of Trimble's software — it follows from what a residual is. A residual
> measures the fit between the adjustment and the observations that shaped it. An adjustment with
> few observations, or with a systematic error common to all of them, will fit beautifully and be
> wrong. Only observations that took no part in the adjustment (§17) and a direct look at the
> data (§18) can distinguish the two.

> **PARAMETRIX DECISION REQUIRED**
>
> **What constitutes an acceptable registration at Parametrix?**
>
> **No numerical threshold appears anywhere in this document, because none exists in any Trimble
> source and inventing one would be indefensible.**
>
> The acceptance framework should combine four things, and a rule built on any one alone will
> fail:
>
> 1. **Numerical residuals** on the control used in the adjustment
> 2. **Independent check information** — residuals on points held out of it (§17)
> 3. **Visual inspection** — Cutting Plane View across overlapping runs (§18)
> 4. **The project accuracy requirement**, which is set per job and is the only thing that makes
>    any threshold meaningful
>
> **Under no circumstances should this SOP acquire a statement of the form "RMS below X equals
> pass."** *(Register item 13; §18, §24)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took surveyed control points, found each one in the point cloud by
> eye, and told TBC to bend the vehicle's computed path so the cloud lands where the control says
> it should. The output is a new path — a new trajectory — sitting next to the original one. The
> point cloud has not moved yet.
>
> **Why it matters.** This is the step that ties a mobile mapping dataset to the ground. Before
> it, the cloud is an internally consistent shape floating on whatever the GNSS and inertial
> solution managed on the day. After it, the shape has been fitted to points a surveyor actually
> occupied. Everything a client relies on — that a curb is where you say it is, that a clearance
> is what you measured — rests on this and on the control network underneath it.
>
> **What can go wrong.** Three things, in order of how often they bite.
>
> First, **too little control and too much confidence**. TBC computes a registration from one
> pair and reports a residual of zero. That zero means the arithmetic worked, not that the data
> is good. Second, **registering twice instead of editing** — the residuals improve each time
> while the trajectory gets bent further against the same handful of points. Third, and least
> visible: **choosing Local and expecting it to fix the ends of the corridor.** It does not
> extrapolate. The last 400 m sit on the unadjusted trajectory and look identical to the rest.
>
> **What good looks like.** Control distributed along the whole extent you intend to deliver,
> bracketing both ends rather than sitting inside them. Enough pairs that removing any one would
> not change the answer much. Residuals that do not grow systematically as you move away from
> control. Some points deliberately held out of the adjustment, with residuals on them in the
> same range as the ones that were used. And a cutting plane through two overlapping passes
> showing the same wall in the same place. A small RMS on its own is not a result — it is one of
> four things you need, and it is the only one the software hands you for free.
