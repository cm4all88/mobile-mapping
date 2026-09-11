# 4. Equipment and Software

## 4.1 The MX60 system

The MX60 is a vehicle-roof-mounted mobile mapping system. Its components, as they appear in
this document and in TMI:

| Component | Function |
|---|---|
| **Sensor Unit** | The roof-mounted head: scanners, cameras, GNSS antenna, IMU |
| **Control Unit** | In-vehicle computer, data storage, power management |
| **Exchangeable data disk** | Removable storage inside the Control Unit |
| **Mounting rack** | Attaches the Sensor Unit to the vehicle |
| **GAMS antenna** *(optional)* | Second GNSS antenna for direct heading |
| **DMI** *(optional)* | Wheel-mounted distance measuring indicator |

### Sensors

| Sensor | Count | Notes |
|---|---|---|
| Laser scanner | **2** | One per side, mounted at opposing oblique angles |
| Spherical camera | 1 | 360° panoramic |
| Rear-downward camera | 1 | Pavement-facing |

> **The two-scanner arrangement is the reason Register Run to Run can work on a single run**, and
> the reason most exports produce a pair of files — *Laser Left* and *Laser Right* — rather than
> one *(TBC 22501, 23339)*.

### Configurations

Three: **Core**, **Pro**, **Premium** *(MX60 UG Rev B, p.12)*. They differ in the 360° camera
and in the GNSS/IMU grade.

| | Core | Pro | Premium |
|---|---|---|---|
| Panoramic image size | **8192 × 4096 px** | **12288 × 6144 px** | **12288 × 6144 px** |
| Side / planar image size | 4096 × 3008 px | 4096 × 3008 px | 4096 × 3008 px |

*(TBC 22501, 23888 — the panorama figures; these are the sizes TBC writes at export)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Which configuration is the Parametrix system, and is it fitted with GAMS and DMI?**
>
> This changes: every imagery accuracy and resolution statement in §19; the attitude accuracy
> that underlies every point cloud accuracy statement; whether GAMS-assisted initialization is
> available (§8); and whether DMI settings appear in trajectory processing (§12).
>
> The vendor can confirm from the serial number. *(D-2; Appendix I)*

### Specification discrepancies to be aware of

Two unresolved conflicts sit in the source documents. Neither blocks work, but neither should be
quoted to a client without checking.

| | Source A | Source B | Status |
|---|---|---|---|
| Scanner field of view | ~346° beam deflection *(MX60 UG Rev B, p.54)* | Full 360° *(Spec sheet, p.2)* | **VENDOR CLARIFICATION REQUIRED** — matters for occlusion geometry |
| Mounting rack | MX SCAN Roof Rack, 18 kg | MX Shock Absorbing Mounting Rack, 28 kg | **PARAMETRIX DECISION REQUIRED** — which is fitted. The published GAMS corner offsets apply to the standard rack **only** *(MX60 UG Rev B, p.68)* |

*(Recorded as `CONFLICT-002` and `CONFLICT-003` in `reference/mx60-reference-data.csv`.)*

## 4.2 Trimble Mobile Imaging — the field software

**TMI** is the browser-based field software. It runs in **Chrome** against the Control Unit.

| | |
|---|---|
| Capture interface | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture, TMI.AI |

*(TMI UG Rev L)*

> **TMI is a web application served by the vehicle, not a cloud service.** It does not need
> internet access, and the addresses above resolve only on the Control Unit's network.

MX60 support arrived in TMI in **December 2024** *(TMI UG Rev L, p.2)*, which is why documents
older than that — including the TBC Technical Notes of October 2022 — do not mention the MX60 at
all.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which TMI version is on the Parametrix system, and how are firmware updates distributed?**
> One documented behaviour differs between versions: the Quick Start Guide describes two separate
> MX60 laser controls (*Measurement Prog* and *Line Speed*), where TMI Rev L describes a single
> combined **Laser Mode** *(MX60 QSG p.10; TMI UG Rev L p.29)*. *(Appendix I; `CONFLICT-005`)*

## 4.3 Trimble Business Center — the office software

TBC with the **mobile mapping module**. The captured documentation is **TBC 2026.10** (§1.6).

### Where the mobile mapping commands live

| Ribbon location | Commands |
|---|---|
| **Mobile Mapping ▸ Processing** | Register a Run, Register a Mission, Register Run to Run |
| **Mobile Mapping ▸ Reports** | Mobile Mapping Report, Trajectory Plots |
| **Mission node context menu** | Generate Scans, Update Scans, Process Raw Trajectory Data, Generate POSPac Position Fixes, Import/Export Calibration, **Cleanup Mobile Mapping Mission** |
| **Capture Devices node context menu** | Manual Camera Calibration |
| **Point Clouds ▸ Regions** | Extract Classified Point Cloud |
| **Point Clouds ▸ View** | Cutting Plane View |
| **Home ▸ Data Exchange ▸ Export** | **Mobile Mapping** tab and **Point Cloud** tab — different exporters |
| **Home ▸ Data Exchange** | Publish to TRCPS |

*(TBC 22905, 26473, 25096, 23991_1, 27415, 26466, 25943, 24460, 22920, 20728, 27279, 11769, 29527)*

> **IMPORTANT**
>
> **The Export dialog has two tabs that both export point clouds, and they behave differently.**
> The **Mobile Mapping** tab holds the run-aware exporters; the **Point Cloud** tab holds the
> generic ones, which select by region or by a rectangle drawn in a view rather than by run
> *(TBC 11769)*. §22 covers the distinction. Choosing the wrong tab is an easy and consequential
> mistake.

### Version-dependent behaviour

Two behaviours in this document depend on TBC version. Both are legacy.

| Behaviour | Boundary | Relevance |
|---|---|---|
| Laser scanners and cameras calibrated **outside** TBC and imported as JSON | "up to the 5.21 version" *(TBC 24886, 24868)* | 5.21 predates 5.70, the oldest release Trimble publishes notes for. **Any recent installation calibrates in TBC** |
| **Select RMS File** prompt on a registration with no RMS file | "typically a project saved in TBC prior to version 5.80" *(TBC 27248)* | Affects **inherited legacy projects** only |

TBC renumbered from `5.x` to `YYYY.MM` after 5.90.1; releases run 2023.10 through 2026.10
*(TBC RN 2025.21)*.

### Licensing

| Release | Requires warranty or subscription valid to |
|---|---|
| 2025.21 | 1 November 2025 or later |
| 2026.10 | **1 June 2026 or later** |

*(TBC RN 2025.21, 2026.10)*. Visible at **Support ▸ License Manager**.

> **OBSERVED SOFTWARE BEHAVIOR**
>
> From TBC 2026.10, **Trimble ID sign-in requires two-step verification** — a code by email each
> time *(TBC RN 2026.10)*. Anyone signing in to TBC or Trimble Connect needs access to the
> account's email at that moment. Worth knowing before it stops a session.

## 4.4 POSPac MMS — and the licence gate that shapes the whole workflow

**Applanix POSPac MMS** computes the SBET from raw GNSS and inertial observations. Whether
Parametrix holds a licence determines which office workflow is even available.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> TBC's **Process Raw Trajectory Data** command computes an SBET inside TBC — but "the
> requirement to run the feature is to have the Applanix's POSPac MMS application (**from version
> 8.6 and a valid license**) installed alongside TBC" *(TBC 25943)*.
>
> **Generate POSPac Position Fixes** — the documented remedy for corridors with no usable GNSS —
> also requires POSPac, and a second processing pass in it *(TBC 24460)*.

| Function | Needs POSPac 8.6+ and a licence? |
|---|---|
| Import `.mxdb`, apply SBET or NAV | No |
| Generate Scans · Update Scans | No |
| Register a Run / Mission / Run-to-Run | No |
| Calibrate laser scanners and cameras | No |
| Cleanup, Mission Report, Trajectory Plots | No |
| Export and Publish | No |
| **Process Raw Trajectory Data** | **Yes** |
| **Generate POSPac Position Fixes (PFIX)** | **Yes** |
| **LiDAR QC Processing** | Not stated — see below |

> **PARAMETRIX DECISION REQUIRED**
>
> **Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?**
>
> Without it, the trajectory must be produced wherever POSPac lives — a subcontractor, a partner
> office, or not at all — and **one of the three documented remedies for degraded GNSS becomes
> unavailable** (§20).
>
> This is the single decision that most changes the shape of the office workflow.
> *(D-10; Appendix I)*

## 4.5 LiDAR QC — a capability decision, not a setting

**LiDAR QC Processing** uses the scan data itself as an aiding sensor to improve the trajectory
where GNSS is poor — similar in principle to SLAM *(TBC 28972)*. It is the only documented remedy
for degraded GNSS that needs **neither POSPac nor additional ground control** (§20).

It needs a workstation well beyond an ordinary one.

| | Minimum | Recommended |
|---|---|---|
| CPU | Intel Core i7 or i9 | Intel XEON |
| RAM | **128 GB** | **256 GB** |
| TEMP storage | 1 TB SSD on the PCI bus | 2 TB SSD M.2 on the PCI bus |
| Virtual memory | +1 TB SSD always available | +2 TB SSD M.2, or 4 TB combined |
| Paging file | — | initial = installed RAM, **maximum = 6 × installed RAM** |
| Also required | **MATLAB Runtime R2024b (24.2)**, installed after TBC | |

*(TBC 28972)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Is LiDAR QC a capability Parametrix intends to have?** It is a procurement question, not a
> software setting, and it only becomes urgent on a job with a genuinely bad GNSS corridor — at
> which point it is too late to buy a workstation. *(D-11)*

> **VENDOR CLARIFICATION REQUIRED**
>
> **Does LiDAR QC have its own POSPac dependency?** Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the **Applanix Support
> Team** *(TBC 28972)*. *(Appendix I)*

## 4.6 Trimble Connect and TRCPS

**Publish to TRCPS** uploads point cloud data, trajectories and images from TBC to a **Trimble
Connect** project, through the **Trimble Desktop Utility (TDU)** installed alongside TBC. It
requires a Trimble ID, and uploads consume the account's Trimble Connect storage quota
*(TBC 29527)*.

It matters to this document for a reason beyond delivery convenience: **it is one of only two
paths that carries the trajectory out of TBC with the data** (§22, §23).

## 4.7 Reference documents

The full list is §1.6. Two gaps:

> **VENDOR CLARIFICATION REQUIRED**
>
> **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* and
> **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* are both needed to
> complete the lever-arm procedure in §7, **if those accessories are fitted**. Neither is held.
>
> Note that the MX60 User Guide requires millimetre-level GAMS offsets and a **≥ 2.0 m baseline**
> where navigation data will be post-processed *(p.68)* — which is all survey-grade work.
> *(Appendix I)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We inventoried the hardware and the three pieces of software, and
> identified the two questions that decide what the office workflow can even look like: which
> configuration of MX60 this is, and whether Parametrix has a POSPac licence.
>
> **Why it matters.** Most equipment sections are reference material you never read twice. This
> one contains a fork in the road. If there is no POSPac licence, the trajectory has to be
> computed somewhere else and one of the three fixes for bad GNSS is simply unavailable — and
> you want to know that before you quote a job through a tree-lined corridor, not during it. The
> configuration question is similar: Core and Premium differ by a factor of four in image
> resolution, so a promise about imagery deliverables made without knowing which one is on the
> roof is a promise made blind.
>
> **What can go wrong.** The quiet failure here is the Export dialog having two tabs that both
> produce point clouds. The Mobile Mapping tab knows about runs; the Point Cloud tab does not,
> and lets you export a rectangle drawn across a view. Both produce a plausible LAS file. Only
> one of them was selected with any awareness of which data it was taking. §22 comes back to
> this.
>
> **What good looks like.** Before the first production job, someone should be able to state, on
> one page: the configuration and serial number, whether GAMS and DMI are fitted, which rack is
> on the vehicle, the TMI version, the TBC version, and whether a POSPac licence exists and where
> it lives. None of that is known today. All of it is a phone call to the dealer.
