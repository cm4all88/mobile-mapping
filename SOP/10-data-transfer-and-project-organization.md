# 10. Data Transfer and Project Organization

## 10.1 What is on the disk

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*

```
TMX<serial>-<mission id>/
  ├── Backup/
  ├── Base/                 base station RINEX — .YYo observation, .YYn .YYg ephemeris
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── NavProc_01/           navigation processing outputs
  ├── POS_1/
  │     ├── raw/            raw IMU + GNSS — posl_*.000, .001, .002 …
  │     └── realtime/
  ├── Extcal.json           the calibration file
  ├── readme_*.txt
  ├── <mission>.mxdb        the mission database
  ├── <mission>.tridb
  └── <mission>_*.log
```

> **Everything the office can ever do derives from this folder.** The `.mxdb` is the index; the
> `POS_1/raw` files are the raw observations from which the trajectory is computed; `Extcal.json`
> is the calibration state the mission was collected under.

## 10.2 Removing the disk

> **CAUTION**
>
> - **Wait for the Control Unit power button light to go out** before removing the disk (§8.8)
> - **Never connect the USB cable while the exchangeable data disk is inside the Control Unit** —
>   remove the disk first *(MX60 UG Rev B, p.10)*

## 10.3 Offload and verify — before anything else happens

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> 1. **Copy, do not move.** The source disk remains the source until a verified copy exists in two
>    places
> 2. **Verify the copy** — file count and total size at minimum; a checksum comparison where the
>    tooling allows
> 3. **Confirm the `.mxdb` opens** — importing into a scratch TBC project is the definitive test
>    (§11)
> 4. **Confirm `POS_1/raw` is present and non-empty.** Without it there is no post-processed
>    trajectory and the mission is NAV-only (§11.2)
> 5. **Confirm base station data** is present if a local base was used
> 6. **Only then** consider the source disk available for reuse
>
> *(Register item 52)*

> **CAUTION**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.** A disk cleared for the next mission is not recoverable,
> and the mission is not re-drivable without a mobilisation.

## 10.4 Backup before processing

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> **Take the raw-data backup before any processing begins**, not after. Processing writes into the
> project and, with **Backup SBET Next to MXDB** enabled (§12.4), into the raw data folder
> alongside the `.mxdb`.
>
> A backup taken after processing has begun is a backup of a partly-processed state — which is
> usually fine and is occasionally exactly the wrong thing to have. *(Register item 52)*

## 10.5 Project organisation

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> **What is the Parametrix folder structure, naming convention and storage location for mobile
> mapping projects?**
>
> **No structure, path, server location or naming convention is proposed in this document**, and
> none should be inferred from the examples above — those are Trimble's own folder names as
> written by the system.
>
> The decision must cover at least:
>
> | Element | Why it matters here specifically |
> |---|---|
> | Where raw mission data lives, and for how long | Re-processing requires it; §25 |
> | Where the TBC project lives | It is large, and it is the provenance record (§23) |
> | Where **`NAVPROC/`** outputs live | The SBET, its report, and the frame/epoch log (§12.4) |
> | Where the **numbered `sbet_*_reg_####.out`** files live | The registration lineage (§23.3) |
> | Where **Parametrix records** live — control/check designation, residuals, delivery record | **None of these have a software home** (§23.6) |
> | Naming that survives a person leaving | — |
>
> *(Register item 53)*

> **The structure matters more in mobile mapping than in most survey work**, because several of
> the provenance artefacts identified in §23 are small files sitting loose in a project folder.
> A convention that keeps them together is the difference between an auditable job and a
> reconstruction exercise.

## 10.6 Chain of custody

> **PARAMETRIX DECISION REQUIRED · D-54**
>
> **Is a chain-of-custody record required for mobile mapping data, and in what form?**
>
> Relevant where data may be used in a dispute, where a client requires it, or where the
> deliverable supports a design decision with legal consequence. The provenance findings in §23
> mean that **the project and the Parametrix record are the evidence** — the deliverable may not
> be able to speak for itself.

## 10.7 Preparing for the next mission

| ☐ | Item |
|---|---|
| ☐ | Verified copy exists in two locations |
| ☐ | `.mxdb` confirmed to open |
| ☐ | Field record filed with the data |
| ☐ | Disk cleared **only after** the above |
| ☐ | Disk health checked; free space sufficient for the next mission |
| ☐ | System powered down correctly |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We got the data off the vehicle, proved the copy is good, and put it
> somewhere it can be found again.
>
> **Why it matters.** This is the only irreversible step in the whole workflow. Everything in the
> office can be redone — you can regenerate scans, redo a registration, re-export. You cannot
> un-erase a disk. And a mobile mapping mission is not re-drivable at reasonable cost: it means a
> vehicle, a crew, traffic control on some corridors, and the same GNSS and lighting conditions
> you had the first time.
>
> **What can go wrong.** The disk gets cleared for the next job before anyone has actually opened
> the mission. A file count looks right, the copy seems fine, and the `.mxdb` turns out to be
> truncated. Importing it into a scratch TBC project takes five minutes and is the only test that
> genuinely proves the data is there.
>
> The other one is `POS_1/raw`. Without those files there is no post-processed trajectory — the
> mission is stuck on the real-time solution, which is not survey grade. It is a folder nobody
> looks at because nothing opens it directly.
>
> **What good looks like.** Two verified copies before the source disk is touched. The mission
> opened once, in TBC, to prove it. The field record filed alongside the data rather than in
> somebody's notebook. And a folder structure someone else can navigate in three years, which
> matters here more than usual because several of the things that prove how the data was processed
> are small files sitting loose in a project folder.
