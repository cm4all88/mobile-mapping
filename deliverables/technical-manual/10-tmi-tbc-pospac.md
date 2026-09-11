# 10. TMI, TBC and POSPac — and the Licensing Gates

## 10.1 Trimble Mobile Imaging — the field software

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

> **VENDOR CLARIFICATION REQUIRED · V-2**
>
> **Which TMI version is on the Parametrix system, and how are firmware updates distributed?**
> One documented behaviour differs between versions: the Quick Start Guide describes two separate
> MX60 laser controls (*Measurement Prog* and *Line Speed*), where TMI Rev L describes a single
> combined **Laser Mode** *(MX60 QSG p.10; TMI UG Rev L p.29)*. *(Appendix E; `CONFLICT-005`)*

## 10.2 Trimble Business Center — the office software

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
> *(TBC 11769)*. §29 covers the distinction. Choosing the wrong tab is an easy and consequential
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

## 10.3 POSPac MMS — and the licence gate that shapes the whole workflow

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

> **Open Parametrix decision — D-10.** *Does Parametrix hold a POSPac MMS 8.6+ licence, and where is it installed?* Stated and tracked in the **SOP §13**; see also the master register.

## 10.4 Trimble Connect and TRCPS

**Publish to TRCPS** uploads point cloud data, trajectories and images from TBC to a **Trimble
Connect** project, through the **Trimble Desktop Utility (TDU)** installed alongside TBC. It
requires a Trimble ID, and uploads consume the account's Trimble Connect storage quota
*(TBC 29527)*.

It matters to this document for a reason beyond delivery convenience: **it is one of only two
paths that carries the trajectory out of TBC with the data** (§29, §30).

## 10.5 Reference documents

The full list is §1.6. Two gaps:

> **VENDOR CLARIFICATION REQUIRED · V-5, V-5**
>
> **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* and
> **Trimble DMI Installation & Operation Manual** *(referenced MX60 UG p.42)* are both needed to
> complete the lever-arm procedure (§7.6, and the **Field How To**), **if those accessories are fitted**. Neither is held.
>
> Note that the MX60 User Guide requires millimetre-level GAMS offsets and a **≥ 2.0 m baseline**
> where navigation data will be post-processed *(p.68)* — which is all survey-grade work.
> *(Appendix E)*

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
> one of them was selected with any awareness of which data it was taking. §29 comes back to
> this.
>
> **What good looks like.** Before the first production job, someone should be able to state, on
> one page: the configuration and serial number, whether GAMS and DMI are fitted, which rack is
> on the vehicle, the TMI version, the TBC version, and whether a POSPac licence exists and where
> it lives. None of that is known today. All of it is a phone call to the dealer.
