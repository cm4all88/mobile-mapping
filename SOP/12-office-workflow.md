# 12. OFFICE WORKFLOW

> **IMPORTANT — read this before relying on the section**
>
> The only TBC mobile mapping document available to Parametrix is *TBC Technical Notes:
> For Mobile Mapping*, **October 2022**. It is a capability brochure, not a procedure
> manual, and it predates the MX60 — it lists raw import from "MX7, MX50, or MX9" only
> *(TBC Technical Notes, p.3)*. MX60 support reached TMI in **December 2024**
> *(TMI UG Rev L, p.2)*.
>
> This section therefore describes the **shape** of the workflow and Trimble's own
> terminology for it. It is not a step-by-step procedure, and the specific commands,
> dialogs, and settings must come from current TBC documentation before this section is
> used to train anyone.

## 12.1 The workflow in one line

```
Import mxdb → Process trajectory → Generate scans → Register to control
   → Colorize → Classify → Extract → QC → Deliver → Archive
```

## 12.2 The stages

### 1. Import

Import raw mobile mapping data by **pointing at the project database file (`mxdb`)**
created by TMI in the field.

The `mxdb` "maintains your data integrity between trajectory, LiDAR data, and panoramic
images," and "full synchronization between original sensor data is maintained for data
runs as collected in the field" *(TBC Technical Notes, p.3)*.

> **WHY THIS MATTERS**
>
> You import a *mission*, not a pile of files. The database is what preserves the timing
> relationship between the trajectory and every laser and camera observation — which, per
> Section 2, is the thing that makes the data georeferenced at all. This is why Section 11
> insists the two SSDs stay together and the mission folder stays intact.

### 2. Vehicle trajectory processing

Two routes:

| Route | Notes |
|---|---|
| **In TBC** | Requires the TBC Mobile Mapping subscription licence. Load raw trajectory and base station data directly; process without leaving TBC; run trajectory reports and QA/QC in TBC |
| **Standalone Applanix POSPac MMS** | Still supported |

*(TBC Technical Notes, pp.2–3)*

This is where the GNSS and IMU data become the trajectory that everything else depends on.
Section 13 covers what to look for in the result.

> **ADVANCED — forward and reverse processing**
>
> This is the step that consumes the symmetry you built in the field. The processor runs
> the solution forward from the start and backward from the end and blends them — which is
> exactly why Trimble asks for a good initialization at **both** ends *(QSG Rev B, p.13)*.
> A mission with a strong start and a skipped finalize sequence produces a visibly weaker
> reverse pass.

> **ADVANCED — lever arms will not match what you measured**
>
> The MX60 System Reference Frame origin differs from the External Reference Point. TMI
> adds internal vectors, so POSPac displays corrected lever arms that differ from your
> mechanical measurements. **This is correct.** *(MX60 UG Rev B, p.47)*

### 3. Generate scans

Use the finished trajectory to generate scans, for individual runs or all runs in the
project.

Available at this stage *(TBC Technical Notes, p.3)*:

- **Filters for sun and fog**
- A **masking template** for point cloud colorization

### 4. Register point clouds

Register mobile mapping runs to fixed control points — Trimble's stated purpose is to
"reduce, or eliminate, **IMU drift**" *(TBC Technical Notes, p.4)*.

| Capability | Detail |
|---|---|
| Registration to control | TBC **smart picking tool** plus the integrated **POSPac PFix engine** |
| **Batch registration** | Register several runs together "to minimize anomalies between common runs in the same geographical location from one mission or from multiple ones" |
| Scan update | Update scans based on registration constraints |

*(TBC Technical Notes, p.4)*

> **IMPORTANT**
>
> Batch registration across runs is how run-to-run disagreement gets resolved. Section 13
> explains why that disagreement is also your best free QC measure — and why you should
> **look at it before you remove it**.

### 5. Colorize

Colorize point clouds using **RGB from the 360° imagery**
*(TBC Technical Notes, p.3)*.

Intensity colouring is the alternative and is the more common delivery for engineering
use. TMR requires delivered intensity data to be normalised to a **16-bit range, 0
(black) to 65535 (white)** *(TMR MLS Guideline §9.2.2, p.11)*.

### 6. Classify and extract

TBC's automated classification creates extraction regions
*(TBC Technical Notes, p.4)*:

| Region | Typical use |
|---|---|
| **Ground** | Surface and corridor deliverables, digital surface models |
| **Buildings** | Context, clearance |
| **High Vegetation** | Vegetation clearance, landscape management |
| **Poles** and **Signs** | Asset inventory |
| **Power Lines** | Power line and pole extraction |

From there: CAD and drafting, surfaces and volumes, alignments and corridors, utility
modelling *(TBC Technical Notes, pp.5–6)*.

### 7. Review imagery

360° panoramic images can be navigated **synchronised with the point cloud 3D view**, with
point clouds overlaid on images for feature verification and object inspection
*(TBC Technical Notes, p.4)*.

> **FIELD TIP**
>
> This is the office's equivalent of walking the site. When a point cloud feature is
> ambiguous — is that a sign or a mailbox, is that curb or a shadow — the synchronised
> panorama resolves it in seconds.

### 8. QC, deliver, archive

Section 13 covers quality control. Delivery formats and archive policy are Parametrix
decisions recorded in Section 11.

## 12.3 Boresight calibration

### What is actually being calibrated

A system calibration estimates where each sensor sits and how it is oriented relative to
an internal virtual reference point inside the sensor head. Each sensor has two sets of
offsets:

| Offset | What it is | Estimated? |
|---|---|---|
| **Lever arms** | Translation — X forward, Y right, **Z down** | **No — known for all sensors** |
| **Boresight angles** | Rotation about those axes — roll, pitch, heading | **Yes — this is what calibration solves** |

*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*

> **WHY THIS MATTERS**
>
> This is the point that makes the whole subject tractable. **You never measure the
> scanners' positions** — Trimble knows where they are inside the head. What drifts, and
> what calibration recovers, is the tiny **angular** misalignment between each scanner and
> the inertial system.
>
> And per Section 13, angular error is the one that multiplies with range. A boresight
> error of a few hundredths of a degree is invisible at the curb line and significant at
> 50 m.

Do not confuse these with the **vehicle** lever arms in Section 6. Those describe where
GAMS and the DMI sit relative to the External Reference Point, and you do measure them.
The sensor lever arms discussed here are internal to the head.

### Where it happens

**In TBC.** Trimble states that "up to the 5.21 version, laser scanners are calibrated out
of the application and the calibration values are imported into TBC from a JSON format
file," and that the *Calibrate Laser Scanners* feature now allows calibration inside TBC
*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*. The feature therefore arrived after
5.21; the exact release is not stated.

> **IMPORTANT**
>
> Both routes still exist, and which one applies depends on your TBC version:
>
> - **TBC after 5.21** — calibrate in TBC using *Calibrate Laser Scanners*, then **Apply**
> - **TBC 5.21 and earlier** — calibrate outside TBC, then import the JSON via
>   `Settings → Calibration Import` in TMI, from a USB stick in the **USB1** socket
>   *(TMI UG Rev L, p.18)*
>
> Confirm which TBC version Parametrix runs before writing this into procedure.

**This is office work.** Nothing is returned to Trimble and nothing is dismantled.

### The calibration mission — what the field crew must collect

This is the part that lands on the field crew, and it is a specific drive, not a normal
collection.

**Four runs over one crossroad:**

| Run | Direction |
|---|---|
| Run_0 | Along the first road, forward |
| Run_1 | Along the first road, backward |
| Run_2 | Along the crossing road, forward |
| Run_3 | Along the crossing road, backward |

**Site requirements** *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*:

| Requirement | Detail |
|---|---|
| **Crossing angle** | As close to **90°** as possible, within **±30°** |
| **Run length** | At least **20 m each side** of the crossing. **Ideally 80 m long — 40 m each side** |
| **Overlap** | Enough overlap between runs |
| **Façades** | **Present in each direction, in sufficient quantity** |
| **Vegetation** | **Few or none, ideally** |

> **WHY THIS MATTERS — why façades and why a crossing**
>
> Boresight angles are solved by comparing the same surfaces seen from different
> directions. Flat vertical surfaces seen from two opposing passes make an angular error
> show up as a visible gap between the two point clouds; pavement alone, viewed at a
> grazing angle, barely constrains it.
>
> The orthogonal pair matters for the same reason in the other axis. A single road only
> constrains the rotations that road's geometry is sensitive to — the crossing supplies
> the rest.
>
> And vegetation is excluded because it gives soft, inconsistent returns that do not
> repeat between passes, so it adds noise to exactly the comparison the solver depends on.

> **FIELD TIP**
>
> Scout the calibration site once and reuse it. A quiet crossroad with buildings on all
> four approaches, minimal trees, and room for 40 m of clean run each way is not common —
> having a known good one saves an hour every time.

### The TBC procedure

1. Create a VCE project; set the coordinate system to match the mobile mapping data
2. Import the `.mxdb`
3. In **Project Explorer**, select a laser scanner under **Capture Devices**
4. From the pop-up menu, choose **Calibrate Laser Scanners**
5. Select the **four runs** (Run_0 – Run_3) of the same crossroad
   — *fewer than four raises an error*
6. Optionally **Toggle Active Trajectory** to see which runs intersect
7. Optionally check **Open Cutting Plane View**
8. Press **Compute** — this may take a while
9. Review the results (below), and **perform the visual check**
10. In the dialog, switch to **Run_2 <-> Run_3** and check that pair too
11. Press **Apply**

*(TBC Help: Calibrate Mobile Mapping Laser Scanners)*

### Reading the result

The dialog reports:

| Output | Meaning |
|---|---|
| **Computed calibration values** | Heading, pitch and roll per laser scanner |
| **Overall Overlap** | Percentage of points used against total points generated |
| **Overall RMS** | Average of the RMS values between used scans |
| **Per-pair Timestamps + 3 RMS values** | For each set of two parallel runs, over a 20 m section around the crossing |

The three RMS directions are **Tangential**, **Orthogonal** and **Vertical** — how closely
the parallel runs agree in each.

> **CAUTION — the asymmetry that matters**
>
> **Good RMS values do not mean the calibration succeeded. A visual check is needed.**
> Bad RMS values do mean it failed, and a visual check will confirm that.
> *(TBC Help: Calibrate Mobile Mapping Laser Scanners)*
>
> So the numbers can only tell you when you have failed. They cannot tell you that you
> have passed. **Never press Apply on RMS alone.**

### The visual check

With **Open Cutting Plane View** checked, a plane named *Mobile Mapping Cutting Plane*
appears as a yellow plane in the 3D View at the start of the first run pair, and points
intersecting it show as a profile in the Cutting Plane View tab.

To use it well:

- Set **rendering to Scan Color** so each scan draws in its own colour — this is what
  makes a gap between passes obvious
- Increase **Point Size** so thin surfaces read clearly
- Adjust **cutting plane thickness** to control which points appear
- **Drag the slider** along the run pair and watch the gap between the two scans at
  several positions, not just one

Then repeat for **Run_2 <-> Run_3**.

> **FIELD TIP**
>
> You are looking for the two colours to sit on top of each other on flat surfaces —
> especially building façades, which is why the site needs them. A consistent offset that
> grows with distance from the vehicle is the signature of a residual angular error.

### How often

No Trimble document in our set states a frequency for the MX60. Queensland TMR, writing
for any MLS system, requires calibration immediately before **and** again at the end of
every project, plus any time the system is disturbed or reassembled
*(TMR MLS Guideline §6, p.7)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Set the boresight calibration policy: frequency, who performs it, what triggers an
> unscheduled calibration, and how the calibration in force is recorded against each
> mission.
>
> *Recommended practice:* calibrate on a defined interval and after any event that could
> have disturbed the sensor head or rack. Record the calibration date and values in the
> field protocol so any mission can be traced to the calibration it was collected under.
> Establish one standard calibration site meeting the crossing requirements above.
>
> Two questions this needs answered first:
>
> - **Which TBC version** does Parametrix run? Versions after 5.21 calibrate in TBC;
>   5.21 and earlier require the external-then-import route.
> - **Does daily removal of the Sensor Unit count as "disturbed"?** If Parametrix follows
>   Trimble's assumption and cases the head each night (Section 3), a literal reading of
>   TMR would require calibration every day, which is not practical. A sensible position
>   is that the fast-lock mount is repeatable and only rack disturbance or a suspected
>   problem triggers recalibration — but that position should be tested against a
>   calibration check, not assumed.

## 12.4 What this section still needs

| Needed | To write |
|---|---|
| Current TBC mobile mapping documentation covering MX60 | Step-by-step import, trajectory processing, registration, export |
| TBC trajectory report interpretation | Section 13 acceptance criteria |
| MX60 boresight calibration procedure | §12.3 policy and the procedure itself |
| POSPac MMS documentation | Trajectory processing detail, forward/reverse settings |

---

## References — Section 12

| Source | Pages |
|---|---|
| Trimble Business Center Technical Notes: For Mobile Mapping, October 2022 | 2–6 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 2, 18, 20 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 47 |
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 13 |

## Other References — Section 12

| Source | Section |
|---|---|
| Queensland TMR, *Mobile Laser Scanning Technical Guideline*, March 2023 (CC BY 4.0) | §6 p.7; §9.2.2 p.11 |
