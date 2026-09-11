# 11. LiDAR QC

## 11.1 What it is, and what it costs to run

**LiDAR QC Processing** uses the scan data itself as an aiding sensor to improve the trajectory
where GNSS is poor — similar in principle to SLAM *(TBC 28972)*. It is the only documented remedy
for degraded GNSS that needs **neither POSPac nor additional ground control** (§27).

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

> **Open Parametrix decision — D-11.** Stated and tracked in the **SOP §13**; see also the master register.

> **VENDOR CLARIFICATION REQUIRED · V-9**
>
> **Does LiDAR QC have its own POSPac dependency?** Trimble does not state one, but it is an
> Applanix technology and the topic directs configuration questions to the **Applanix Support
> Team** *(TBC 28972)*. *(Appendix E)*

## 11.2 What it actually computes

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 28972)*
>
> "LiDAR QC is an advanced trajectory processing technology that, **similar to LiDAR SLAM**, is
> using scan data as an aiding sensor to improve georeferencing accuracies in areas of poor GNSS
> coverage or in areas where overlapping scans are not perfectly matching. Based on a robust and
> iterative least square adjustment, LiDAR QC generates 3D Voxels that are matched in overlap
> scan regions. The result of this iterative process is solving the constant IMU boresight angles
> and making corrections to the post-processed trajectory (position and orientation)."

Enabled by the **LiDAR QC (Refine with scans)** checkbox in Process Raw Trajectory Data, which
adds a LiDAR QC tab. Requires **MATLAB Runtime R2024b (24.2)** and a substantial workstation
(§11.1).

## 11.3 Settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60**; 10 mm for MX9/MX90 |
| **Lasers** | Left · Right · All | **All** |

> **FIELD TESTING REQUIRED · T13, T13**
>
> **T13 — the 3–100 m range.** The MX60's useful range and the range over which scan geometry
> usefully aids a trajectory solution are different questions. 100 m may include returns too noisy
> to help.
>
> **T13 — Lasers = All.** Trimble's own text beside the setting says using both "can increase
> computation time without significantly improving the accuracy, as it compares the left versus
> right laser of isolated runs." **The default contradicts the guidance printed next to it.**
> *(Appendix E)*

## 11.4 Running it

Select runs from the Project Tree **with overlap — parallel runs, or crossing runs** — click
**Add**, set the parameters, **Compute** *(TBC 28972)*.

## 11.5 The acquisition geometry it needs

Trimble prescribes a specific acquisition geometry for LiDAR QC:

| Element | Requirement |
|---|---|
| **Area** | "a structured scene such as a residential area with detached houses and objects within the LiDAR sensor's maximum range"; "open sky terrain for good GNSS satellite visibility" |
| **Strips** | "two perpendicular strips. **Each strip will consist of two runs (one in each direction)**" |
| **Strip length** | **250–300 m** |

*(TBC 28972)*

> This is materially the same geometry the laser scanner calibration requires (§20.3) — four runs,
> two orthogonal pairs, both directions. **One site can serve both**, which matters because
> establishing a calibration site is a real piece of work (the **SOP §15**).

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We looked at a way of improving the trajectory using the scan data itself.
> Instead of relying only on GNSS and the inertial sensor, LiDAR QC matches overlapping scans to
> each other and works backwards to a better path — the same idea a SLAM system uses, applied
> after the fact to data you already have.
>
> **Why it matters.** It is the only remedy for poor GNSS that needs neither a POSPac licence nor
> additional surveyed control (§27). If you have overlapping runs — and the recommended pass
> pattern gives you overlapping runs anyway — the information needed to improve the solution is
> already sitting in the dataset.
>
> **What can go wrong.** It is not free. The hardware requirement is a serious workstation, not a
> good laptop: 128 GB of RAM at minimum, 256 GB recommended, plus a separate MATLAB runtime. If
> the machine cannot meet that, the capability does not exist for us regardless of what the
> checkbox says. And it needs genuine overlap — running it on isolated passes that do not see the
> same ground gives it nothing to match.
>
> **What good looks like.** Overlapping runs, a structured scene with buildings and hard edges
> rather than open field, and a machine that can hold the problem in memory. Note that the
> acquisition geometry LiDAR QC wants is nearly the same one the laser scanner calibration wants
> (§20), so one site can serve both purposes.
