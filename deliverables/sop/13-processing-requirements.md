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
> rather than inside a TBC project that may later be cleaned up (§18) or lost.

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

**Registration has its own section: §14.** It is not a processing step like the others — it is the
step that decides whether the deliverable sits where it is supposed to, and it carries its own
authority, designation, command-selection and record requirements.

## 13.5 Records this section requires

| Record | State |
|---|---|
| Trajectory processing settings, and the frame and epoch log | **D-55** |
| Results of Scan Generation | **D-55** |

*Registration records are §14.10.*


> **IN PLAIN LANGUAGE**
>
> **What this section means.** Turning what the vehicle recorded into something you can measure: post-
> process the trajectory, generate scans from it, and keep track of which trajectory produced which
> point cloud.
>
> **Why it matters.** Every point in the cloud is placed relative to the trajectory. If you generate
> scans from the wrong trajectory — or from the real-time one when a post-processed one exists — the
> cloud is consistently, invisibly wrong. It will still look perfectly normal.
>
> **Remember this.** The post-processed trajectory (the SBET) is the normal input for survey work; the
> real-time one (NAV) is a fallback and should be recorded as such when it is used. Scan generation is
> not a formality — it is the step that commits the cloud to a particular trajectory.
>
> **If this is skipped.** Work proceeds on a cloud built from the wrong trajectory, and the error is
> uniform enough that no visual check catches it. It is found, if at all, when independent check
> points disagree by an amount nobody can explain.
