# 13. Processing Requirements

**What shall be done, not how.** The method is in the Office How To; the explanation is in the
Technical Manual §§17–21.

## 13.1 Trajectory

| # | Requirement | State |
|---|---|---|
| 1 | Survey deliverables are produced from a **post-processed SBET**, not the real-time NAV solution. Where NAV is used, the reason is recorded and the deliverable is qualified | **PROPOSED** |
| 2 | The **antenna model** is confirmed before computing. The MX60 requires **Trimble 112735** | **PROPOSED** |
| 3 | The frame and epoch the trajectory was computed in is recorded | **PROPOSED · D-55** |

> **IMPORTANT**
>
> The antenna model is read automatically from the RINEX, which means it can be read **wrongly**.
> An incorrect model introduces a **systematic antenna-height and reference error** into the
> trajectory *(TBC 25943; Technical Manual §17.3)*. It is one field nobody looks at, upstream of
> everything.

> **PARAMETRIX DECISION REQUIRED · D-10 · P1 · blocks operation**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?** Without it,
> trajectory processing inside TBC and the PFIX route are both unavailable, which removes one of
> the three degraded-GNSS remedies *(Technical Manual §10.3, §27)*.

> **PARAMETRIX DECISION REQUIRED · D-19**
>
> Computation mode — Single Base or PP-RTX. Stated at §6.2 because it is a project-setup decision
> as much as a processing one.

> **PARAMETRIX DECISION REQUIRED · D-11**
>
> **Is LiDAR QC a capability Parametrix intends to have?** It is the only degraded-GNSS remedy
> needing neither a POSPac licence nor additional control, and it needs a workstation with 128 GB
> of RAM at minimum *(Technical Manual §11.1)*. The answer is a procurement decision, not a
> processing one.

> **TESTING REQUIRED · T11, T12, T13**
>
> Three trajectory-processing defaults are untested against Parametrix conditions: the **Multipath**
> default of Medium on open-sky corridors, the **DMI scale factor standard deviation** default of
> 5 % where the wheel may never have been measured, and the **LiDAR QC** range and laser defaults.
> Trimble's own guidance beside the LiDAR QC laser setting contradicts its default
> *(Technical Manual §11.3)*.

## 13.2 Preserve what records the trajectory

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Enable Backup SBET Next to MXDB.** That log is the only artefact found anywhere in the workflow
> that records the frame and epoch a trajectory was computed in, and it lives with the raw data
> rather than inside a TBC project that may later be cleaned up (§17) or lost.

## 13.3 Scan generation

| # | Requirement | State |
|---|---|---|
| 1 | **The filters applied are recorded.** Filter choice is a defensible-or-not decision a reviewer may need to see years later | **PROPOSED · D-55** |
| 2 | Colorization is applied or not applied by decision, not by default | **PARAMETRIX DECISION REQUIRED — D-22** |

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Capture the Results of Scan Generation into the project record.** It is the only artefact that
> states which filters produced a given cloud.

> **TESTING REQUIRED · T1, T3**
>
> Filter defaults are untested. **T3 in particular:** whether the **Reflective Panels** filter
> removes legitimate retro-reflective returns from signs and line marking — on sign and
> retroreflectivity work, those returns are the deliverable *(Technical Manual §18.3)*.

## 13.4 Registration

| # | Requirement | State |
|---|---|---|
| 1 | The control/check designation is fixed **before** registration and is not changed during it | **PROPOSED — D-15** (§7.3) |
| 2 | A registration that needs changing is **recomputed from the imported trajectory using Edit**, not layered on a previous one | **PROPOSED — D-12** |
| 3 | **Update Scans is run before the result is inspected, accepted, or exported** | **PROPOSED — D-36** |
| 4 | Registration type, the trajectory node produced, and its SBET filename are recorded | **PROPOSED — D-29** |

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **CAUTION · W-07**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.
>
> *(Technical Manual §21.8)*

> **PARAMETRIX DECISION REQUIRED · D-12**
>
> **Registration command selection.** Is **Register a Mission** the corridor default, with Register
> a Run reserved for single-run cases and for repairing one run in an otherwise accepted mission?
> And where does **run-to-run** sit?

> **PARAMETRIX PROCEDURE (PROPOSED)** — *where run-to-run belongs*
>
> 1. Register the mission to surveyed control first. This establishes absolute position
> 2. Assess against independent check points and visually (§15)
> 3. **Only then**, if overlapping passes still disagree, use run-to-run — choosing as **Reference
>    Run** the pass with the better GNSS conditions and the better residuals against control
> 4. **Re-check against the independent check points afterwards**, because the Run to Adjust has
>    moved
>
> Step 4 is the one most likely to be skipped, and is why the sequence matters: adjusting a run to
> match another run changes its residuals against control, and if the reference run was itself
> slightly off, run-to-run propagates that error faithfully into the run you adjusted.

> **TESTING REQUIRED · T15, T9, T24, T7**
>
> Which registration type when; whether Target-Bundle Adjustment should be checked; how much
> overlap run-to-run needs; and whether Registration Auto-Saving is on by default.

> **CAUTION · W-06**
>
> Picked targets are written to **`Targets.csv`** when Registration Auto-Saving is on. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

## 13.5 Records this section requires

| Record | State |
|---|---|
| Trajectory processing settings, and the frame and epoch log | **D-55** |
| Results of Scan Generation | **D-55** |
| Registration type, trajectory node, SBET filename with its `_reg_####` number | **D-29** |
| Confirmation that Update Scans was run | **D-36** |
| `Targets.csv` | **D-55** |
