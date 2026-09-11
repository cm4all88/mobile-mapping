# 16. Run to Run Registration

## 16.1 What it is, and what it is not

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
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
> **absolute** accuracy. It cannot replace registration to control (§15), and a dataset that has
> only been run-to-run registered has not been tied to the ground at all.

## 16.2 Where it belongs

Run-to-run registration solves a specific problem: two passes down the same corridor that are
each individually acceptable against control, but that do not sit on top of each other.

That mismatch is real and visible — a doubled curb line, a wall with two faces 4 cm apart — and
it is the thing a client notices first in a delivered cloud. It arises because the two passes
were collected at different times with different GNSS conditions, and each carries its own
trajectory error.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Where run-to-run registration fits in a controlled workflow:**
>
> 1. Register the mission to surveyed control first (§15). This establishes absolute position
> 2. Assess the result against independent check points (§17) and visually (§18)
> 3. **Only then**, if overlapping passes still disagree, use run-to-run to reconcile them —
>    choosing as **Reference Run** the pass with the better GNSS conditions and the better
>    residuals against control
> 4. Re-check against the independent check points afterwards, because the Run to Adjust has
>    moved
>
> **Not adopted.** Step 4 is the part most likely to be skipped and is the reason this sequence
> matters: adjusting a run to match another run will change its residuals against control, and
> if the reference run was itself slightly off, run-to-run will faithfully propagate that error
> into the run you adjusted. *(Register item 14)*

> **The choice of which run is the Reference is a survey decision, not a processing convenience.**
> Whatever the Reference Run's absolute error is, the Run to Adjust inherits it.

## 16.3 Prerequisites

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> In a pair, the two runs need to have:
>
> - **At least one scan**, whatever the scan (left or right)
> - **Enough overlapping scan data** along the trajectories

### A useful exception

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> *"Missing TMX Files for 'Runname_X and Runname_X+1'" in the Status column means that no scan
> data has been generated… "Missing TMX files" does not prevent you from launching the Register
> Run to Run directly, and you do not need to generate the scans first, **TMX files will be
> generated on the fly**.* *(TBC 25096)*

This is the only registration command that does not require pre-generated scans. Every other one
is dimmed without them.

## 16.4 The sequence

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*

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
9. Set the **Update Scans** option (§16.5)
10. Check **Open Cutting Plane View** to inspect visually
11. **Compute**

### What Compute produces

- A new trajectory nested beneath the **Run to Adjust**, named
  `GivenName: Runname_X To Runname_X+1`
- **RMS statistics in the Results tab** (§16.6)
- If **Update Scans** was checked, new Scan nodes beneath the created trajectory
- A cutting plane named `MissionID Last Two Digits - Run to Adjust`, one per pair

## 16.5 Update Scans is an option inside this command

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
>
> - **Unchecked** — do not generate the scan data after the registration
> - **Checked** — generate the scan data for the **Run to Adjust** on the adjusted trajectory,
>   and enable the **Open Cutting Plane View** option

> **This is the one place in TBC where Update Scans is not a separate step.** Everywhere else,
> registration produces a trajectory and the cloud is recomputed later and deliberately (§13.6).
> Here it can happen inline.
>
> The consequence for provenance is worth noting: a run-to-run registration with Update Scans
> checked produces a new scan set immediately, and the previous scan set remains in the project.
> Which one is delivered becomes a question of which node is selected at export (§22, §23).

## 16.6 The result — and TBC's most informative QC output

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*
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
trajectories" — the prerequisite in §16.3. The registration may still compute, on the few
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

## 16.7 The visual check

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25096)*

Checking **Open Cutting Plane View** creates, per pair, a plane named *MissionID Last Two Digits
- Run to Adjust*, appearing as:

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

## 16.8 Improving a run-to-run result

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "You can use the **Register a Run** command to improve the trajectory resulting from
> registering two runs together. The improvement can be done by editing the same (run_to_run)
> trajectory." *(TBC 25362)*

So a run-to-run result can subsequently be adjusted against surveyed control through Edit — which
supports the sequencing in §16.2, in reverse order, for situations where the relative fit was
addressed first.

---

> **IN PLAIN ENGLISH**
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
