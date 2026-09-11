# 6. Project Setup Requirements

## 6.1 Before any data is collected

Four things **should** exist in writing before mobilisation. None is onerous, and the failures
they prevent are expensive.

> **PARAMETRIX PROCEDURE (PROPOSED)** — *the practice of recording them.* **What** each one says is
> a separate open decision, named in the table.

| # | Requirement | State |
|---|---|---|
| 1 | **The accuracy requirement**, stated in writing, with the client agreement or scope it derives from | **PARAMETRIX DECISION REQUIRED — D-13.** The requirement to state one is not in doubt; what constitutes meeting it is §17 |
| 2 | **The coordinate reference system, datum, epoch and geoid model**, stated in writing and matching the control network | **PARAMETRIX DECISION REQUIRED — D-21** |
| 3 | **Grid or ground**, agreed with the client in writing | **PARAMETRIX DECISION REQUIRED — D-38** |
| 4 | **The system configuration and fitment** the work assumes | **PARAMETRIX DECISION REQUIRED — D-2 · blocks operation** |

## 6.2 The coordinate reference system

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

> **PARAMETRIX DECISION REQUIRED · D-21 · P1 · blocks operation**
>
> **Which datum and epoch does Parametrix work in, who sets it, and who checks it?**
>
> Epoch carries more weight here than in conventional work, because the trajectory's reference
> frame and the project's control may be realised at different epochs *(Technical Manual §12.4)*.
> TBC 2026.10 allows working at a non-default epoch and warns that the feature "is intended for
> experienced users, as incorrect settings may lead to inaccurate results" *(TBC RN 2026.10)*.

### The frame the trajectory is computed in

The trajectory is produced by POSPac, which has its own view of the project's coordinate system and
may compute in ITRF00 and then transform. The only outward sign is the SBET filename
*(Technical Manual §12.3, §17.4)*.

> **PARAMETRIX DECISION REQUIRED · D-19 · P1 · blocks operation**
>
> **IN-Fusion+ Single Base or PP-RTX?** The two differ in whether a local base station must be
> occupied on every mission, and in the reference frame the solution is computed in. It interacts
> with **D-42** (§8) and with D-21 above.

> **TESTING REQUIRED · T10**
>
> Which of Parametrix's normal coordinate systems POSPac recognises directly, and which trigger
> the ITRF00 path. Answerable once, then known.

## 6.3 Grid and ground

> **IMPORTANT**
>
> A **ground**-scaled export **does not record the scale factor it used**. A **grid** export writes
> a sidecar naming the coordinate system and scale factor *(TBC 11769; Technical Manual §12.5)*.
>
> The recipient of a ground-scaled file cannot recover the scale factor from the file. Agree it in
> writing, and make sure the delivery can say what it is (§19).

> **PARAMETRIX DECISION REQUIRED · D-38**
>
> Deliverable specification — standard formats, which export path produces each, and the default
> scaling.

## 6.4 The system this work assumes

> **PARAMETRIX DECISION REQUIRED · D-2 / V-4 · P1 · blocks operation**
>
> **Which MX60 configuration is the Parametrix system — Core, Pro or Premium? Are GAMS and DMI
> fitted? Which mounting rack?**
>
> This is the single decision that unblocks the most others. It changes every imagery resolution
> statement, the attitude accuracy underlying every accuracy statement, whether the initialization
> manoeuvres are required or merely advisable, and whether DMI settings appear in trajectory
> processing *(Technical Manual §7.7, §9)*. **The vendor can confirm it from the serial number.**

## 6.5 Records this section requires

| Record | Where | State |
|---|---|---|
| Accuracy requirement, and its source | Project record | **D-13** |
| CRS, datum, epoch, geoid — and who set them | Project record | **D-21** |
| Grid or ground, as agreed | Project record and client agreement | **D-38** |
| Configuration and fitment assumed | Project record | **D-2** |
