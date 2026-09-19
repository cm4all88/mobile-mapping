# 21. Registration

This is the section the rest of the office workflow exists to support. Read §2 and §18 first.

## 21.1 What registration is, in this system

**Registration adjusts the trajectory.** It does not move points.

TBC takes surveyed ground control points, pairs each with a point the operator picks in the
point cloud, and computes a correction to the trajectory that reduces the difference between
the pairs. The output is a **new trajectory**, stored beside the imported one. The existing
point cloud is untouched until you deliberately recompute it (§19).

> **This is the single most important structural fact about TBC registration, and it surprises
> people from a static scanning background.** In static work, registration moves scans. Here it
> produces a better path, and the points follow only when you ask them to.

### The three commands

They are **not interchangeable**. Each solves a different problem with a different kind of
observation.

| Command | What constrains it | Scope | Section |
|---|---|---|---|
| **Register a Run** | Surveyed GCPs ↔ targets picked in the cloud | One run | §21.3 |
| **Register a Mission** | The same, with each GCP reusable across runs and passes | A set of runs at once | §21.4 |
| **Register Run to Run** | **Cloud-to-cloud overlap** against a fixed reference run | Pairs, batched | **§21.10** |

> **IMPORTANT**
>
> Register Run to Run uses **no surveyed control at all**. It makes two runs agree with each
> other. Two runs can agree perfectly and both be in the wrong place. It is a relative tool, and
> §21.10 explains where it belongs in a controlled workflow.

## 21.2 What TBC means by "target"

> **TRIMBLE DOCUMENTED METHOD**
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
> This shapes control design (§22.5). A GCP for mobile mapping registration has to be something you
> can *find in a point cloud* at the density and incidence angle the vehicle produced — which is
> a different requirement from something you can occupy with a prism. A painted stop-bar corner
> is excellent. A survey nail in asphalt is nearly useless: it is a few millimetres across, and
> the cloud will not resolve it.

## 21.3 Register a Run

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*

### Prerequisites

- **At least one generated scan on the run.** The command is dimmed otherwise
- **A GCP file imported into the project** — Shape, ASCII or CSV. Imported points appear in Plan
  View and under the **Points** node

### What the command asks you for

Working through the dialog, the operator names the registration, chooses a **Registration Type**
(§21.5), pairs each imported GCP with a target picked in the cloud using **Point Cloud Smart
Picking** (§21.6), sets **Use XY**, **Use Z** and **As Check** per point (§22), optionally enables
a limit box or **Target-Bundle Adjustment** (§21.7), then computes and applies.

Three of those carry consequences this manual returns to: the **registration name** becomes the
name of the computed trajectory and is what identifies it months later (§30); the **As Check**
designation decides whether a point can test the result or only be fitted by it (§22); and
**Apply** does not reach the point cloud until Update Scans runs (§19).

**The click sequence is Office How To §16.** It is maintained there, once.

### What Apply produces

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*
>
> - An **adjusted trajectory node** nested beneath the run, beside `Sbet`
> - A new **SBET file on disk**: `sbet_<date>_reg_####.out`, in the project folder,
>   **incrementing** with each registration — `_reg_0001`, `_reg_0002`, and so on
> - Picked targets renamed *RunName TrajectoryGCPName*; the updated targets carry a trailing `*`
> - Trajectory properties carrying **`Origin: Registration result`**, **`Input trajectory:
>   Imported trajectory`**, and **`Registration type:`** the method used

> **Those four properties and the numbered SBET file are your provenance record.** They are the
> strongest evidence available that a given point cloud was built on a given adjustment. §30 is
> about how far that evidence travels — and it does not travel as far as you would like.

### A note for single-scanner acquisition

> **TRIMBLE DOCUMENTED METHOD**
>
> "In case of a single head configuration (one high-end laser scanner acquisition), it does not
> matter which scan is used (left or right) for the registration." *(TBC 22905)*

## 21.4 Register a Mission

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 26473)*

Register a Mission registers "a set of runs at the same time" rather than sequentially, and —
this is the point of it — **lets every GCP be used more than once**, with different run point
clouds or different passes of the same run.

### How it differs from Register a Run

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP `instance`** |
| Instances | — | TBC creates one per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left, right, or both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | `RunName TrajectoryGCPName` | `RegistrationName_GCPName_RunName` |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |
| Unused instances | — | "All unused instances are removed from the Control Points list" |

### Why this is probably the normal case

Consider an ordinary corridor: driven in both directions, perhaps twice, with control set along
it. A single painted mark is visible in four passes. Under Register a Run it constrains one of
them. Under Register a Mission it constrains all four **simultaneously**, and the four runs come
out mutually consistent because they were adjusted against the same observation.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-12); it is not decided here.

## 21.5 Registration Type — and the one that does not extrapolate

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905, 26473)*

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
> 400 m unadjusted at the tails. §22.6 and §22 return to this.

> **FIELD TESTING REQUIRED · T15**
>
> **Which registration type, when?** Trimble describes the mechanism of each and gives no
> selection rule beyond "consistent differences." **Global, and then Local** receives no guidance
> at all, and is the method shown in every screenshot Trimble publishes.
>
> Do not adopt a default from the screenshots. Test the three methods on a representative
> corridor with independent check points and compare. *(Appendix E)*

## 21.6 Target picking, and reading residuals before you commit

This is where the operator's judgement enters the adjustment, and TBC gives real help.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905)*

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

> **TRIMBLE DOCUMENTED METHOD**
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
> a good illustration of why superseded scan sets are a hazard worth managing (§28, §30).

### The 30 m rule

> **TRIMBLE DOCUMENTED METHOD**
>
> "The distance in a pair of points cannot exceed the allowed maximum distance of **30 meters (or
> 100 feet)**." *(TBC 22905, 26473)*

A pair exceeding it is rejected. In practice this is a sanity limit, not a working tolerance — a
GCP and its picked target should be a few centimetres apart, not tens of metres. Hitting this
limit means the wrong feature was picked.

### Minimum observations

> **TRIMBLE DOCUMENTED METHOD**
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

> **CAUTION · W-06**
>
> If Registration Auto-Saving is on, picked targets are written to **`Targets.csv`**. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

> **FIELD TESTING REQUIRED · T7**
>
> **Is Registration Auto-Saving on by default?** The consequence of the reload prompt depends on
> it, and the answer is a glance at the dialog. *(Appendix E)*

## 21.7 Target-Bundle Adjustment — the option whose name reads backwards

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22905, 26473)*

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

## 21.8 Editing a registration — not the same as registering again

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25362, 26578)*

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

## 21.9 Judging the result

Covered fully in §23, but the governing principle belongs here because it is where the temptation
to shortcut is greatest.

> **TRIMBLE DOCUMENTED METHOD**
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
> wrong. Only observations that took no part in the adjustment (§22) and a direct look at the
> data (§25) can distinguish the two.

> **Open Parametrix decision — D-13.** *What constitutes an acceptable registration at Parametrix?* Stated and tracked in the **SOP §13**; see also the master register.

---

## 21.10 Register Run to Run — the cloud-to-cloud path

## 21.11 What it is, and what it is not

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> **Register Run to Run** "provides a way to register a set of runs, two by two in batch mode,
> from the same mission or from different missions. In a pair of runs, one has to be defined as
> a **Reference Run**, meaning that its trajectory will not change, and the other as a **Run to
> Adjust**, its trajectory will be optimized with regards to the Reference Run's trajectory. As a
> result, a new trajectory will be created and the scan data of the Run to Adjust will be updated
> with this new trajectory so that the scan data of both runs will match well together."

The help topic is titled *Register Multiple Pairs of Runs*; the command in the ribbon is
**Register Run to Run**.

> **CAUTION**
>
> **This command uses no surveyed control.** It makes two clouds agree with each other.
>
> Two runs can agree perfectly and both be in the wrong place. Run-to-run registration improves
> **relative** accuracy — the internal consistency of the dataset — and does nothing whatever for
> **absolute** accuracy. It cannot replace registration to control (§21), and a dataset that has
> only been run-to-run registered has not been tied to the ground at all.

## 21.12 Where it belongs

Run-to-run registration solves a specific problem: two passes down the same corridor that are
each individually acceptable against control, but that do not sit on top of each other.

That mismatch is real and visible — a doubled curb line, a wall with two faces 4 cm apart — and
it is the thing a client notices first in a delivered cloud. It arises because the two passes
were collected at different times with different GNSS conditions, and each carries its own
trajectory error.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-12); it is not decided here.

> **The choice of which run is the Reference is a survey decision, not a processing convenience.**
> Whatever the Reference Run's absolute error is, the Run to Adjust inherits it.

## 21.13 Prerequisites

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> In a pair, the two runs need to have:
>
> - **At least one scan**, whatever the scan (left or right)
> - **Enough overlapping scan data** along the trajectories

### A useful exception

> **TRIMBLE DOCUMENTED METHOD**
>
> *"Missing TMX Files for 'Runname_X and Runname_X+1'" in the Status column means that no scan
> data has been generated… "Missing TMX files" does not prevent you from launching the Register
> Run to Run directly, and you do not need to generate the scans first, **TMX files will be
> generated on the fly**.* *(TBC 25096)*

This is the only registration command that does not require pre-generated scans. Every other one
is dimmed without them.

## 21.14 The sequence

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*

1. Import the missions into the TBC project
2. **Mobile Mapping ▸ Processing ▸ Register Run to Run**
3. Enter a **Registration Name**. "This name will be given to all computed trajectories"
4. Select a pair — one as **Run to Adjust**, one as **Reference Run**. They may come from the
   same mission or from different missions. In the pair selectors, runs are listed as
   `<mission ID last two digits> - Run <n>`
5. Optionally **Swap Runs** to invert the two
6. Click **+** to add the pair to the batch
7. In Plan View the **Run to Adjust draws green** and the **Reference Run draws red**
8. Repeat for further pairs. Pairs can be removed with **−**, or reordered with the up and down
   buttons — **TBC registers the pairs in the order given**
9. Set the **Update Scans** option (§21.15)
10. Check **Open Cutting Plane View** to inspect visually
11. **Compute**

### What Compute produces

- A new trajectory nested beneath the **Run to Adjust**, named
  `GivenName: Runname_X To Runname_X+1`
- **RMS statistics in the Results tab** (§21.16)
- If **Update Scans** was checked, new Scan nodes beneath the created trajectory
- A cutting plane named `MissionID Last Two Digits - Run to Adjust`, one per pair

## 21.15 Update Scans is an option inside this command

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> - **Unchecked** — do not generate the scan data after the registration
> - **Checked** — generate the scan data for the **Run to Adjust** on the adjusted trajectory,
>   and enable the **Open Cutting Plane View** option

> **This is the one place in TBC where Update Scans is not a separate step.** Everywhere else,
> registration produces a trajectory and the cloud is recomputed later and deliberately (§19).
> Here it can happen inline.
>
> The consequence for provenance is worth noting: a run-to-run registration with Update Scans
> checked produces a new scan set immediately, and the previous scan set remains in the project.
> Which one is delivered becomes a question of which node is selected at export (§29, §30).

## 21.16 The result — and TBC's most informative QC output

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*
>
> "TBC also computes some statistics and displays them in the **Results** tab. **Timestamps are
> computed every twenty meters depending on the speed of the vehicle.** For each Timestamp,
> **three RMS values are computed along three directions (Tangential, Orthogonal and
> Vertical)**."

| Direction | Meaning |
|---|---|
| **Tangential** | Along the direction of travel |
| **Orthogonal** | Across the direction of travel, horizontally |
| **Vertical** | Up and down |

Cells read **`No overlap`** where the two runs do not overlap at that timestamp, and a metric
value where they do.

> **This is the most detailed quality output anywhere in the mobile mapping workflow, and it is
> worth understanding why the three axes are separated.**
>
> An error that is large **tangentially** but small orthogonally and vertically is a *timing* or
> along-track scale problem. One that is large **orthogonally** is a heading or lateral position
> problem. One that is large **vertically** is a height or pitch problem. The three-axis
> breakdown tells you which part of the trajectory solution is struggling — information a single
> combined RMS would hide.
>
> The same three-axis convention appears in laser scanner calibration *(TBC 24886)*, so it is
> TBC's standard agreement metric for mobile mapping.

### The `No overlap` rows are information, not noise

A run pair with many `No overlap` timestamps did not have "enough overlapping scan data along the
trajectories" — the prerequisite in §21.13. The registration may still compute, on the few
timestamps that did overlap. **A pair that overlaps for 200 m of a 2 km run has been registered
on 10 % of its length and extrapolated across the rest.**

> **FIELD TESTING REQUIRED · T24**
>
> **How much overlap is enough?** Trimble states the requirement qualitatively — "enough
> overlapping scan data" — and gives no proportion, no minimum length and no distribution rule.
> The Results tab makes the actual overlap visible after the fact but offers no guidance on
> reading it.
>
> Test on a representative pair, varying overlap, and observe where the adjustment stops being
> trustworthy. *(Appendix E)*

## 21.17 The visual check

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25096)*

Checking **Open Cutting Plane View** creates, per pair, a plane named
`MissionID Last Two Digits - Run to Adjust`, appearing as:

- A plane node beneath the parent **Plane** node in Project Explorer
- A **yellow cutting plane** at the beginning of the Run to Adjust, visible in 3D View
- A profile in the **Cutting Plane View** tab, showing the points that intersect the plane

To read it:

- Change rendering to **Scan Color** — one colour per scan, so the two runs are distinguishable
- Increase **Point Size**
- Adjust **Cutting plane thickness** — "a wider thickness will typically result in additional
  points being displayed"
- Keep only the pair's Scan nodes checked in Project Explorer
- **Drag the slider at the bottom of the tab to move the plane along the Run to Adjust**, looking
  at the gap between the two clouds

> **This is the check Trimble says you cannot skip.** Good RMS values do not prove success
> *(TBC 24886, 25096)*. What you are looking for in the profile is one wall, one curb, one pole —
> not two of each, offset.

> **FIELD TESTING REQUIRED · T16**
>
> **Cutting plane thickness.** Trimble's screenshots show `5.000` in one topic and `0.030` in
> another, with no stated basis. Thickness determines what the visual check can actually see: too
> thin and there is nothing in the profile; too thick and a real offset is buried in a band of
> points from either side of the plane. *(Appendix E)*

## 21.18 Improving a run-to-run result

> **TRIMBLE DOCUMENTED METHOD**
>
> "You can use the **Register a Run** command to improve the trajectory resulting from
> registering two runs together. The improvement can be done by editing the same (run_to_run)
> trajectory." *(TBC 25362)*

So a run-to-run result can subsequently be adjusted against surveyed control through Edit — which
supports the sequencing in §21.12, in reverse order, for situations where the relative fit was
addressed first.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took two passes down the same stretch of road that did not quite line
> up, held one of them fixed, and bent the other until the two clouds sat on top of each other.
> No survey control was involved at all. TBC then told us how well they now agree, every 20 m,
> broken into along-track, across-track and vertical.
>
> **Why it matters.** A doubled curb line is the most visible defect in a delivered mobile mapping
> dataset. A client who cannot evaluate absolute accuracy can see two of something that should be
> one, immediately. Reconciling overlapping passes is what makes a dataset look — and be —
> internally coherent.
>
> **What can go wrong.** The trap is mistaking this for registration. It is not. Making two runs
> agree tells you nothing about whether either is in the right place, and it is entirely possible
> to take a well-controlled run and drag it off position by registering it to a poorly controlled
> reference. Whatever error the reference run carries, the adjusted run inherits. The second trap
> is overlap: the software will happily register a pair that only overlaps for a short stretch,
> and quietly extrapolate that correction along the whole run. The `No overlap` rows in the
> Results tab are how you catch it, and they are easy to scroll past.
>
> **What good looks like.** You choose as reference the pass with the better GNSS and the better
> residuals against control — deliberately, not by whichever was listed first. The Results tab
> shows real numbers across most of the run's length rather than a column of `No overlap`. The
> three axes are of similar size; one axis much larger than the other two is telling you
> something specific about which part of the solution is struggling. And when you drag the cutting
> plane along the corridor, you see one building face rather than two. Then you go back and
> re-check the run you moved against your independent control points, because you just moved it.

---

> **IN PLAIN LANGUAGE**
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
