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

## 12.3 Boresight calibration and the JSON file

Boresight calibration is where office processing feeds back into the field system.

**The loop** *(TMI UG Rev L, pp.18, 20)*:

1. Orientation values in the system are "good start" values
2. They are refined in the office by a special processing called **boresight calibration**
3. The result is saved to a **JSON file**
4. That file is **imported back into the system** before the next missions:
   - Copy the JSON to a USB memory stick
   - Plug into the **USB1 socket** on the Control Unit
   - `Settings → Calibration Import` → press Import next to the file name

> **IMPORTANT**
>
> Until the JSON is imported, the system keeps using the old calibration. A boresight
> calibration computed and left in the office improves nothing.

**How often?** Trimble does not state a frequency for the MX60. Queensland TMR does, and
it is stricter than common practice:

> Boresight calibrations "shall occur immediately prior to any MLS capture for the
> project and be performed again at the end of the project to ensure that the calibration
> parameters have not changed during the project." If the system is disturbed or
> disassembled and reassembled, another calibration shall be performed before further
> capture.
> *(TMR MLS Guideline §6, p.7)*

> **PARAMETRIX DECISION REQUIRED**
>
> Establish the boresight calibration policy: frequency, who performs it, what triggers an
> unscheduled one, and how the JSON version in the system is tracked.
>
> *Recommended practice:* calibrate on a defined interval and after any disturbance to the
> Sensor Unit or rack. Record the JSON file version in the field protocol so every mission
> can be traced to the calibration it was collected under. Note that if Parametrix removes
> the Sensor Unit daily (Section 3), the question of what counts as "disturbed" needs an
> explicit answer.
>
> **This decision needs a procedure Parametrix does not currently have** — no document in
> the collection describes *how* to perform an MX60 boresight calibration. Obtain it from
> Trimble before adopting a policy that assumes it.

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
