# 26. Troubleshooting

Symptom first. Each entry gives the likely cause, what to check, and where the procedure is.

## 26.1 Field — before and during collection

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **System will not power up** | Supply, battery, or hold duration | Supply live; hold the Control Unit button **≥ 15 s**; battery above the Battery Protect threshold | 7.5 |
| **Audible alarm during operation** | **Battery Protect** — power cut in **78–90 s** | Restore charge immediately. Do not continue | 7.5, 8.6 |
| **TMI will not load** | Browser, network, or system not ready | Use **Chrome**; `http://tmi.mx-scan.net`; allow the startup sequence to complete | 7.6 |
| **Navigation will not reach ready** | Poor sky view, insufficient manoeuvres, or a heading problem | Move to genuinely open sky; repeat the dynamic manoeuvres; ask TMI which parameter is holding it | 8.2 |
| **Navigation degrades mid-run** | GNSS obstruction | Note it and continue if brief; if sustained, this is a §20 planning problem, not a driving one | 8.6, 20 |
| **A sensor stops reporting** | Cable, power, or sensor fault | Stop. A run collected with a sensor down is incomplete and may need re-driving | 9.4 |
| **Storage filling faster than expected** | Settings, or a longer corridor than planned | Reassess before the disk fills mid-run — an interrupted run loses the closing sequence | 7.8, 8.7 |
| **Imagery obviously degraded** | Contamination, precipitation, low sun | Clean the optics. Weather is a go/no-go decision, not a driving adjustment | 6.5, 19.3 |
| **Vehicle stationary in direct sun** | Outside the rated envelope below 10 km/h | Move, or shut down. A queue on a hot day is a real risk | 8.5 |

## 26.2 Office — import and trajectory

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Covered distance shorter than expected** | A run is missing, or a transfer was incomplete | Compare against the field record. **Catch this at import** | 11.4 |
| **Fewer runs than the crew logged** | Incomplete transfer | Re-verify the offload before processing | 10.3 |
| **Process Raw Trajectory Data unavailable** | **POSPac MMS 8.6+ with a valid licence not installed** | §4.4. Without it the trajectory must be produced elsewhere | 12.1 |
| **Base station data not recognised** | Ephemeris imported instead of observation, or not imported before running | Import **only** the `.YYo`. **Do not import `.YYn` or `.YYg`** | 12.2 |
| **Antenna model wrong** | Read automatically from the RINEX | **Must read `Trimble 112735`** for the MX60. Verify before computing | 12.3 |
| **SBET named `sbet_<mission>_<frame>.out`** | POSPac did not recognise the datum and epoch; computed in ITRF00 then transformed | A **processing-path indicator**, not a verdict. Direct scrutiny to the CRS and epoch setup | 12.4, 24 L3 |
| **Trajectory Plots greyed out** | No SBET computed yet, or no mission | Plots open once after computation; this command reopens them | 12.5 |
| **Plots vanished after computing** | They open only once | Use **Mobile Mapping ▸ Reports ▸ Trajectory Plots** — do **not** recompute | 12.5 |
| **LiDAR QC tab unavailable** | MATLAB Runtime R2024b not installed | §4.5 | 12.7 |

## 26.3 Office — scans and calibration

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Scans did not appear after generation** | Display setting, or generation not complete | Check beneath the trajectory node in Project Explorer | 13.2 |
| **Scan generation failed or was interrupted** | Various | **Recover Mobile Mapping Scans** *(TBC 28155)* | 13.7 |
| **Expected returns missing — signs, line marking** | A filter removed them | Review the filters applied. **Reflective Panels is the suspect** — T3 | 13.3 |
| **Point cloud not coloured** | Generated with colour off | Colour must be on at generation; it propagates to export | 13.4, 19.5 |
| **MTA configuration guidance appears not to apply** | It does not — **the MX60 has no MTA stage** | Ignore MTA topics; they are MX9/MX90 | 13.1 |
| **Calibration RMS good but data still disagrees** | **Good RMS does not prove success** | Perform the visual check, on **both** run pairs | 14.3, 18.1 |
| **Calibration will not compute** | Run geometry does not meet the pattern | Four runs, two roads crossing near 90° ± 30°, ≥ 20 m each side, façades present | 14.3 |
| **Camera imagery misaligned with the cloud** | Camera boresight | Manual Camera Calibration; colour fringing at edges is the symptom | 14.4, 19.5 |

## 26.4 Office — registration

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Register a Run dimmed** | No generated scan on the run | Generate scans first | 15.3 |
| **Error: all points set As Check** | The adjustment requires at least one control point | TBC enforces this. Reconsider the designation with the Project Surveyor | 17.2 |
| **Pair rejected** | GCP-to-target separation exceeds **30 m** | The wrong feature was picked | 15.6 |
| **Warning: not a 3D point / not in this run's scan** | Pick landed off the scan or with no Z | Pick again | 15.6 |
| **Warning: not the most recent scan** | Pick landed on a **superseded** scan set | Pick again. Consider whether superseded sets should still be in the project | 15.6, 21 |
| **Picked targets lost on reopening** | Registration Auto-Saving, and the reload prompt | Answering "No" **empties `Targets.csv` permanently** | 15.3 |
| **Residuals improve each time you register** | **Adjustments are stacking** | Use **Edit**, which starts from the imported trajectory and supports **Reset** | 15.8 |
| **Ends of the corridor still misaligned** | **Local does not extrapolate** | Control must bracket the extent | 15.5, 5.6 |
| **Run-to-run Results mostly `No overlap`** | Insufficient overlap between the pair | The adjustment is based on a small fraction of the run | 16.6 |
| **Run-to-run made absolute accuracy worse** | The reference run carried absolute error, and it propagated | Choose the reference deliberately; re-check against control afterwards | 16.2 |

## 26.5 Office — QC, export and delivery

| Symptom | Likely cause | Check | § |
|---|---|---|---|
| **Surfaces look thick rather than doubled** | **Rendering is not set to Scan Color** | One colour per scan, or two offset surfaces read as one thick one | 18.5, 24 L6 |
| **Everything passes but the client finds an error** | **Spot-checking** — error arrives in stretches, not speckles | Traverse the corridor rather than sampling it | 18.5, 24 L7 |
| **Exported cloud does not reflect the registration** | **Update Scans was not run** | Confirm scans sit under the registered trajectory and stations carry `_reg_####` | 22.2, 13.6 |
| **Exported data differs from what was QC'd** | **Export timestamps = Yes reprocesses from raw** | Unresolved — **T18 / vendor**. Record the setting used | 22.3 |
| **Scale factor unknown in a delivered file** | Ground scaling does not expose it | Export to grid to obtain the `.txt` sidecar, or use ECEF | 22.5 |
| **Re-imported cloud is wrongly scaled** | **Double-scaling** on re-import of a grid-scaled export | Trimble's own warning | 22.5 |
| **Some delivered images are black** | **Corrupted side camera images export as black** — silently | Screen by file size, then open the flagged ones | 19.4 |
| **Nothing exported to TopoDot** | Scans not generated, or run views open | Generate first; close all run views | 22.6.3 |
| **Cannot determine which trajectory produced a delivered cloud** | **The documented provenance limitation** | §23. Reconstruct from retained SBETs if they exist; record it next time | 23 |

## 26.6 When the answer is "this segment is not suitable for mobile mapping"

> **IMPORTANT · a legitimate outcome, not a failure**
>
> Where GNSS degradation is severe, no remedy is available, and the accuracy requirement cannot be
> met, **the correct professional answer may be that mobile mapping is not the appropriate
> acquisition method for that segment** (§6.8, §20.7).
>
> Conventional survey, static scanning or total station work may produce a more defensible result.
> Saying so — early, in writing, to the client — is better practice than delivering a weak segment
> mixed in with a good corridor.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We put the common failures in one place, organised by what you actually
> see rather than by what causes it.
>
> **Why it matters.** Most of these have a cheap fix if caught at the right moment and an expensive
> one if caught later. A missing run found at import is a transfer problem; found at delivery it is
> a mobilisation.
>
> **What can go wrong.** The entries worth memorising are the silent ones — they do not produce an
> error and you only find them by looking: exporting before Update Scans, surfaces that look thick
> because the rendering is wrong, black images in a delivery that counted correctly, and residuals
> that improve every time you re-register because the adjustments are stacking.
>
> **What good looks like.** Most of this table never gets used, because the checks in §9, §18 and
> §24 catch things while they are still cheap. When you do need it, you look up the symptom, not
> the cause.
