# 8. Trajectory Processing

Computes the SBET inside TBC, without going out to POSPac. **Requires a POSPac MMS 8.6+ licence**
— see §9 if you do not have one.

### Do

1. Import the base station `.YYo` first (§7)
2. Right-click the **Mission** node ▸ **Process Raw Trajectory Data**
3. TBC loads the raw POS data automatically and fills the settings from what the vehicle logged.
   **Check them — do not accept them unread.** Trimble's own instruction: *"Double check the
   settings values and if needed modify them"* *(TBC 25943)*
4. Set **Computation Mode** — **IN-Fusion+ Single Base** or **IN-Fusion+ PP-RTX**
5. **Verify the antenna model** — see below
6. Enable **Backup SBET Next to MXDB**
7. Consider **Generate QC Report**
8. **Compute**

### Look at — the settings, with Trimble's defaults

| Setting | Values | Default |
|---|---|---|
| **Computation Mode** | Single Base · PP-RTX | *none stated* |
| **Initialization Mode** | VNAV · **Gyro-compassing** · GAMS · GAMS and Gyro-compassing | Gyro-compassing |
| **Multipath** | Low · **Medium** · High | Medium |
| **Antenna Manufacturer / Type** | Read from the RINEX | — |
| **GAMS** | lever arm and standard deviation | *dimmed if GAMS was disabled at acquisition* |
| **DMI** | lever arm, SD, scale factor, scale factor SD | *dimmed if DMI was disabled at acquisition* |
| **LiDAR QC (Refine with scans)** | on/off | Off — see §24 |

*(TBC 25943)*

### The one field to check every time

> **CAUTION**
>
> **The antenna model must read `Trimble 112735`** for an MX60. `Tallysman/33-3970` is the MX9 and
> MX50 antenna *(TBC 25943)*.
>
> It is read automatically from the RINEX, **which means it can be read wrongly.** An incorrect
> antenna model puts a **systematic antenna-height and reference error** into the trajectory, and
> nothing downstream will attribute the symptom to its real cause.

### Expect

A trajectory that computes without error, and an SBET file in the project folder.

### Stop if

- **The antenna model is not `Trimble 112735`**
- **A GAMS or DMI pane is dimmed and you expected the sensor to be fitted.** Dimmed means the
  sensor was disabled during acquisition and logged nothing (§35). That is a field problem
- The DMI scale factor came from a manual rather than a measured wheel, and the standard deviation
  is still at the 5 % default. Trimble's escape hatch is to **set it to 100 % if the value is not
  known at all** *(TBC 25943)*

> **TESTING REQUIRED · T11, T12**
>
> Whether **Multipath = Medium** is right for open-sky Parametrix corridors, and whether the DMI
> 5 % default is an accuracy claim anybody verified *(SOP §13.1)*.

### Record

The settings used, the computation mode, and the frame-and-epoch log that **Backup SBET Next to
MXDB** writes. That log is the only artefact anywhere in the workflow that records the frame and
epoch a trajectory was computed in, and it lives beside the raw data rather than inside a project
that may later be cleaned up *(SOP §13.2)*.
