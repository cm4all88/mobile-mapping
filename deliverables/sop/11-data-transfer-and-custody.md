# 11. Data Transfer and Custody

## 11.1 The one irreplaceable thing

`POS_1/raw/` holds the raw GNSS and inertial observations. **Every trajectory the office ever
computes derives from those files, and nothing can recompute them** *(Technical Manual §5.2)*. The
picked registration targets are the other irreplaceable item, and that comes later (§13).

Everything else in the chain is reproducible. These two are not.

## 11.2 Transfer and verification

> **PARAMETRIX PROCEDURE (PROPOSED) · D-52**
>
> 1. **Copy, do not move.** The source disk remains the source until a verified copy exists in two
>    locations
> 2. **Verify the copy** — file count and total size at minimum, a checksum comparison where the
>    tooling allows
> 3. **Confirm the `.mxdb` opens.** Importing into a scratch TBC project is the definitive test
> 4. **Confirm `POS_1/raw/` is present and non-empty.** Without it there is no post-processed
>    trajectory and the mission is NAV-only *(Technical Manual §17.2)*
> 5. **Confirm base station data** is present if a local base was occupied
> 6. **Only then** is the source disk available for reuse

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

## 11.3 Backup before processing

> **PARAMETRIX PROCEDURE (PROPOSED) · D-52**
>
> **The raw-data backup is taken before any processing begins**, not after.
>
> Processing writes into the project and, with **Backup SBET Next to MXDB** enabled (§13.2), into
> the raw data folder alongside the `.mxdb`. A backup taken after processing has begun is a backup
> of a partly processed state — usually fine, and occasionally exactly the wrong thing to have.

## 11.4 Structure, naming and location

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> **Folder structure, naming convention and storage location.**

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> Two constraints are proposed as non-discretionary whatever else D-53 decides: the project record
> **should not** live on a processor's local machine (§3.3), and raw mission data **should** be
> distinguishable from processed products without opening them.

## 11.5 Chain of custody

> **PARAMETRIX DECISION REQUIRED · D-54**
>
> **Is a chain-of-custody record required?** For most survey work the answer is probably no. For
> work that may be used in a dispute, a claim or a proceeding, it is a different question, and it
> has to be decided **before** the data is collected rather than when it is asked for.

## 11.6 Records this section requires

| Record | State |
|---|---|
| Transfer performed, verified how, by whom, when | **D-52** |
| Location of the raw-data backup | **D-52, D-55** |
| Custody, where required | **D-54** |
