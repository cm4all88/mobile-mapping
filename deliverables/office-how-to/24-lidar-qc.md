# 24. LiDAR QC

Uses the **scan data itself** as an aiding sensor to improve the trajectory — SLAM-like, run
inside trajectory processing. The only degraded-GNSS remedy that needs **neither POSPac nor
additional ground control**.

### Before you start — can this machine run it?

| | Minimum | Recommended |
|---|---|---|
| CPU | Intel Core i7 or i9 | Intel XEON |
| **RAM** | **128 GB** | **256 GB** |
| TEMP storage | 1 TB SSD on the PCI bus | 2 TB SSD M.2 |
| Virtual memory | +1 TB SSD always available | +2 TB M.2, or 4 TB combined |
| Paging file | — | initial = installed RAM, **maximum = 6 × installed RAM** |
| Also required | **MATLAB Runtime R2024b (24.2)**, installed **after** TBC | |

*(TBC 28972)*

### Do

1. Check **LiDAR QC (Refine with scans)** in **Process Raw Trajectory Data** (§8). A LiDAR QC tab
   appears
2. Select the runs from the Project Tree **with overlap** — parallel runs, or crossing runs
3. **Add**
4. Set the parameters
5. **Compute**

### Look at — the settings

| Setting | Values | Default |
|---|---|---|
| **Range** | Minimum and maximum LiDAR measurement distance used | **3 m to 100 m** |
| **Noise** | 5, 10, 50, 80, 100, 200 mm | **5 mm for MX50/MX60** |
| **Lasers** | Left · Right · All | **All** |

### Expect

A long computation. It solves the constant IMU boresight angles and corrects the post-processed
trajectory, position and orientation, from voxels matched in overlapping scan regions
*(TBC 28972)*.

### Stop if

- **The runs do not overlap.** It has nothing to match
- The machine does not meet the requirement above. It is not a setting you can push through

> **TESTING REQUIRED · T13**
>
> Two defaults are untested, and one of them contradicts Trimble's own guidance printed beside it:
> **Lasers = All**, where the note says using both "can increase computation time without
> significantly improving the accuracy, as it compares the left versus right laser of isolated
> runs." Also the **3–100 m** range: the MX60's useful range and the range over which scan geometry
> usefully aids a trajectory are different questions *(Technical Manual §11.3)*.

### The acquisition geometry it wants

| Element | Requirement |
|---|---|
| Area | A structured scene — detached houses, objects within sensor range; open sky |
| Strips | **Two perpendicular strips**, each consisting of **two runs, one in each direction** |
| Strip length | **250–300 m** |

*(TBC 28972)*

**That is materially the same geometry the laser scanner calibration wants (§13).** One site can
serve both, which matters because establishing one is real work *(SOP §14.3)*.

### Record

That LiDAR QC was run, on which runs, with which settings.
