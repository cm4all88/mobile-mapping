# 27. Degraded GNSS Conditions

## 27.1 This section is a branch, not a stage

Everything from §17 to §26 describes one path through the workflow. This section describes what
to do when that path does not produce an acceptable trajectory — and **two of its three remedies
loop backwards** into earlier stages.

```
                        §17  Trajectory processing
                               │
                               ├──────────── LiDAR QC ──────────┐   inside §17
                               │                                 │   needs a large workstation
                               ▼                                 │
                        §18  Generate scans                      │
                               │                                 │
                               ▼                                 │
                        §21  Register to control ────────────────┤   needs more control
                               │                                 │
                               ▼                                 │
                        §23  QC  ── not acceptable ──────────────┤
                               │                                 │
                               │            PFIX ────────────────┘   needs POSPac
                               │            loops back to §17, second pass
                               ▼
                             accept
```

Read it after the normal path is understood. Placing it in sequence would imply it happens after
QC, which is true only in the sense that QC is where you discover you need it.

## 27.2 Why GNSS degradation is the dominant risk

From §3: the point cloud inherits the trajectory's error, attitude error multiplies with range,
and **error is correlated in time rather than scattered**. GNSS degradation is the principal cause
of all three.

When GNSS is obstructed, the inertial solution carries on alone and drifts. The drift is smooth,
so the cloud stays crisp and internally consistent — it simply moves. Under tree cover, in an
urban canyon, beneath a structure, the data looks exactly as good as the rest of the corridor and
is not.

> **The environments that degrade GNSS are also the environments clients most often want
> surveyed**: downtown corridors, treed arterials, under-bridge inspections, tunnel approaches.
> This is not an edge case.

### Seeing it before it costs you

The trajectory RMS colouring (§17.4, §24) shows degraded stretches **in plan, before any point
cloud exists**. That is the earliest and cheapest warning available, and it should be looked at
on every mission.

## 27.3 The three remedies

| | **More control** | **PFIX** | **LiDAR QC** |
|---|---|---|---|
| What it is | Register to additional surveyed GCPs | POSPac position fixes from GCP/target offsets | Scan data as an aiding sensor in the solution |
| Where it acts | **After** the navigation solution | **Inside** the navigation solution | **Inside** the navigation solution |
| Needs POSPac | No | **Yes** | Not stated |
| Needs extra field control | **Yes** | **Yes** | **No** |
| Needs a large workstation | No | No | **Yes** — 128–256 GB RAM (§11.1) |
| Passes | One | **Two** | One |
| Section | §15, §17 | §27.5 | §27.6 |

> **Without a POSPac licence, Parametrix has two remedies, not three: place more control, or buy a
> much larger workstation.** That is a procurement consequence of a licensing decision, and it is
> worth knowing before quoting a job through a difficult corridor. *(§10.3, D-10)*

## 27.4 Remedy one — more control

The conventional answer, and the one that needs no software Parametrix may not have.

Registration to surveyed GCPs (§21) corrects the trajectory **after** the navigation solution.
Where GNSS was poor, the trajectory has drifted, and control in that stretch pulls it back.

Two constraints from §21 govern how control must be placed for this to work:

- **A Local adjustment does not extrapolate** beyond the outermost control point *(TBC 22905)*.
  Control must **bracket** the degraded stretch, not sit in the middle of it
- **Target-Bundle Adjustment** operates at 250 m or 70 m intervals (§21.7), which is Trimble's own
  indication of the scale at which control density matters

> **The difficulty is practical rather than technical.** The stretches that most need control are
> the ones where conventional survey is hardest — under the canopy, between the buildings, where
> the GNSS you would use to establish the control is as obstructed as the vehicle's was. Control
> there has to be carried in by traverse or total station, which is the real cost of this remedy.

> **Open Parametrix decision — D-16.** Stated and tracked in the **SOP §8**; see also the master register.

## 27.5 Remedy two — Generate POSPac Position Fixes (PFIX)

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> "**Generate POSPac Position Fixes** is a method that lets you improve the trajectories of a
> mission in the Applanix's POSPac MMS software **where there is no GNSS coverage or the coverage
> is extremely poor**. At these locations, trajectories are corrected by measuring the distance
> between ground control points (GCPs) collected in the field and targets extracted from the
> acquired scan data. The results of these measurements are **Offset values that are projected
> back to the trajectories**. New positions of the modified trajectories are then exported to a
> text file, which is used by the POSPac MMS software to do a **second-pass on the trajectory
> data**."

### The distinction from registration — and why it matters

> Registration corrects **the answer**. PFIX corrects **the computation**.
>
> Registration takes a finished trajectory and bends it to fit control. PFIX takes the same
> control observations and feeds them back into the navigation solver as position fixes, so the
> filter re-solves with that information available. The difference is that PFIX's corrections are
> propagated by the filter's own model of how the system behaves, rather than by interpolation
> between control points.
>
> ⚠ *That framing is this document's, inferred from Trimble's descriptions of the two commands.
> Trimble never states the contrast directly.* **VENDOR CLARIFICATION REQUIRED · V-16** — when should
> PFIX be preferred over registration? *(Appendix E)*

### Prerequisites

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> - **POSPac MMS installed, with a valid licence** for the IN-Fusion processing methods
> - An SBET processed in POSPac, or the real-time NAV trajectory "in case of POSPac processing not
>   possible"
> - A VCE project whose coordinate system matches the data
> - The `.mxdb` imported with that trajectory applied
> - **Scan data generated from at least one run**
> - A GCP file imported in the project coordinate system

### The procedure

1. Right-click the **Mission** node ▸ **Generate Pospac Position Fixes**. *The command does not
   open if the mission has no generated scan*
2. Select a GCP under **Points** ▸ **Add Selection to Control Points**
3. Pick the target in the cloud — **the same Point Cloud Smart Picking tool as registration**
   (§21.6), with the same live residuals and the same **30 m** maximum pair separation
4. **Validate**. Easting, Northing and Elevation residuals display
5. Add further pairs — one pair is sufficient for TBC, and §21.6's caution applies equally
6. **Compute.** "The computation consists in reducing the global error between the ground control
   point(s) (GCPs) and their corresponding targets"
   - Updated targets are named `Mission_Name-PFIX-GCP_Name`
   - **A `custom_events.txt` file is generated in a `PFIX` folder under the TBC project folder**
7. Close the dialog

### The second pass, in POSPac

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> 1. Start POSPac MMS, create and save a project
> 2. Import the POS logged files from `POS_1/raw`
> 3. **Copy the `custom_events.txt` from TBC into the `Extract` folder of the POSPac project**
> 4. Open the **GNSS-Inertial Processor**
> 5. Optionally open **Position Fixes and Satellite Events** to inspect the fixes
> 6. Select the IN-Fusion processing mode
> 7. **All Processings**. A new SBET appears in the `Proc` folder

### Bringing it back

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 24460)*
>
> 1. Select the mission in Project Explorer and display its properties
> 2. **Replace the initial trajectory file with the new SBET** computed with PFIXes
> 3. **Update the scan data with the Update Scans command** (§19)

> **IMPORTANT**
>
> Step 3 is the one that is skipped. A PFIX pass that produces a better SBET but never reaches the
> point cloud has cost a day and changed nothing in the deliverable (§19).

## 27.6 Remedy three — LiDAR QC

Covered in §11, because it runs **inside** trajectory processing rather than after it.

In summary: it uses the scan data as an aiding sensor, generating 3D voxels matched in overlap
regions, solving the constant IMU boresight angles and correcting the post-processed trajectory in
position and orientation *(TBC 28972)*.

**What makes it distinctive:** it is the only remedy that needs **no additional field control**.
The information comes from the overlap in the data already collected.

**What makes it expensive:** 128 GB RAM minimum, 256 GB recommended, dedicated SSDs, a paging file
at six times installed RAM, and the MATLAB Runtime (§11.1).

> **It requires overlap.** "Select the runs from the Project Tree **with overlap** (parallel runs,
> or crossing runs)" *(TBC 28972)*. A single pass down a difficult corridor gives it nothing to
> work with — which is a **planning** consequence (§15), not a processing one. If a corridor is
> known to be GNSS-hostile and LiDAR QC is a possible remedy, the overlap has to be collected on
> the day.

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

## 27.7 Choosing

> **Open Parametrix decision — D-34.** *What is the decision rule when a corridor produces an unacceptable trajectory?* Stated and tracked in the **SOP §8**; see also the master register.

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §8** (D-16); it is not decided here.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set out what to do when the satellites were not visible enough for long
> enough, and the computed path drifted. There are three fixes: put in more surveyed control and
> pull the path back onto it; feed the control measurements back into the navigation solver and
> re-solve from scratch; or let the software use the overlapping scan data itself as a substitute
> for satellites.
>
> **Why it matters.** The places where GNSS fails are the places clients most want surveyed —
> downtown streets, tree-lined arterials, under bridges. This is not an unusual case to plan for;
> on many corridors it is most of the job. And because the failure is invisible in the data, the
> only thing standing between a drifted stretch and a delivered deliverable is somebody having
> looked.
>
> **What can go wrong.** Two of the three fixes have to be set up *before* you drive. More control
> means surveying points in exactly the places where conventional survey is hardest, because the
> sky is just as obstructed for your control crew as it was for the vehicle. LiDAR QC needs
> overlapping passes, which means driving the corridor more than once — and if you did not, the
> remedy is not available in the office no matter how large the workstation. Discovering at QC that
> you needed overlap you did not collect means going back.
>
> The third failure is subtler: doing a PFIX pass properly, producing a genuinely better path, and
> then forgetting to run Update Scans. The trajectory improves, the point cloud does not, and the
> file you deliver is the one you started with.
>
> **What good looks like.** The hostile stretches were identified from a desk review before anyone
> drove, the mitigation was chosen then, and the field work was planned around it. After
> processing, the trajectory RMS picture shows short degraded stretches where you expected them.
> Independent check points in those stretches — and there should be some, specifically there — come
> back in the same range as the ones in the open. And if none of that could be arranged, somebody
> said so early enough that the client could choose a different approach for that 400 m rather
> than receiving it quietly mixed in with the rest.
