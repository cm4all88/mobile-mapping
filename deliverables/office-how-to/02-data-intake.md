# 2. Data Intake

**Before anything else happens.** Nothing in this section involves TBC.

### 2.1 Do

1. **Copy, do not move.** The source disk stays the source until a verified copy exists in two
   places
2. **Verify the copy** — file count and total size at minimum; a checksum comparison if your
   tooling allows
3. **Open the `.mxdb`** in a scratch TBC project — this is the definitive test that the copy
   worked. **A file count can look right, the copy can seem fine, and the `.mxdb` still be
   truncated**
4. **Confirm `POS_1/raw/` is present and non-empty**
5. **Confirm base station data** is in `Base/`, if a local base was occupied
6. **Take the raw-data backup now**, before any processing
7. Only then is the source disk available for reuse

### 2.2 Look at

The mission folder, which should look like this:

```
TMX<serial>-<mission id>/
  ├── Base/                 .YYo .YYn .YYg      base RINEX, if collected
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── POS_1/raw/            posl_*.000, .001 …  ← the irreplaceable one
  ├── Extcal.json           the calibration file
  ├── <mission>.mxdb        the file you import
  └── <mission>_*.log
```

### 2.3 Expect

Tens to hundreds of gigabytes. `POS_1/raw/` holds a numbered series of `posl_*` files, not one
file. `Extcal.json` is small and is there.

### 2.4 Stop if

- **`POS_1/raw/` is missing or empty.** There is no post-processed trajectory without it and the
  mission is NAV-only. Raise it now, while re-collection is still a small decision
- The copy does not verify
- The mission folder has arrived without the field record

> **PARAMETRIX DECISION REQUIRED · D-52**
>
> **The offload, verification and backup procedure** — the six steps above are this guide's
> recommendation *(SOP §11.2)*.

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

> **Take the backup before processing, not after.** Processing writes into the project and, with
> **Backup SBET Next to MXDB** enabled (§8), into the raw data folder beside the `.mxdb`. A backup
> taken afterwards is a backup of a partly processed state *(SOP §11.3)*.

### 2.5 Record

Offload performed, verified how, by whom, when. Where the backup is.
