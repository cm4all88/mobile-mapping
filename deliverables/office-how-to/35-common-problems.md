# 35. Common Problems — What to Check First

| Symptom | First check | Then |
|---|---|---|
| **A registration command is dimmed** | Does the run have at least one **generated scan**? | §11 |
| **GAMS or DMI settings are dimmed** in Process Raw Trajectory Data | The sensor was **disabled during acquisition** and logged nothing. Not a software problem | §9 of the Field How To; field record |
| **The trajectory is NAV, not SBET** | Is `POS_1/raw/` present? Is a POSPac licence available? | §2, §9 |
| **Picked targets have vanished** | Was a reload prompt answered **"No"**? `Targets.csv` is emptied permanently | §19, W-06 |
| **Residuals got worse after a second registration** | You registered twice. Adjustments stack — use **Edit** | §19 |
| **The exported cloud is not the registered one** | Was **Update Scans** run? Do the stations carry `_reg_####`? | §21, §31 |
| **Two passes are offset in the cutting plane** | Is rendering set to **Scan Color**? Without it, two surfaces read as one | §22 |
| **A surface looks thick and the numbers were fine** | Attitude error or calibration. Check whether thickening grows with range | §13, §22 |
| **Side camera images export black** | Corrupted imagery. It is **silent** — assume there are others | §23 |
| **Imagery colour sits beside feature edges** | Camera boresight | §13.2 |
| **Nothing exported to TopoDot** | Scans not generated; or run views not closed | §30 |
| **`Extract Classified Point Cloud` produced nothing** | Run it before **Export to LAS (Trajectory Split)**, not after | §30 |
| **The whole trajectory is degraded** | Antenna model — must read **`Trimble 112735`** | §8 |
| **A height bias across the whole job** | Antenna model, geoid, or base station coordinate | §8, §5 |
| **The RMS colouring has gaps** | Registered segments render as **"Undefined RMS"**. Not a fault | §10, §27 |
| **`No overlap` rows in run-to-run results** | Information, not noise. The two runs do not overlap there | §18 |
| **LiDAR QC will not produce a useful result** | Do the runs actually overlap? Does the machine have 128 GB of RAM? | §24 |
| **MTA / GPU driver documentation** | **Not applicable to the MX60.** That is the MX9 and MX90 path | §11 |
| **TBC sign-in asks for an emailed code** | From TBC 2026.10, Trimble ID requires two-step verification | §30 |

### 35.1 When the answer is "re-collect"

Some of these are not office problems. Missing coverage, missing overlap, a mission with no closing
sequence and a sensor that logged nothing are all field problems, and the only remedy is a
mobilisation *(SOP §22.3)*.

**Raise it. Do not absorb it.** A non-conformance fixed quietly leaves no trace that the workflow
failed, which means it happens again to somebody else on a job where it costs more.
