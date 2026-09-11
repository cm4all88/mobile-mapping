# 25. Data Transfer and Handoff

## 25.1 Removing the disk

1. Confirm the mission is closed and the **power button light is out** (§22)
2. Remove the exchangeable data disk
3. **Never connect the USB cable while the disk is inside the Control Unit** *(MX60 UG Rev B,
   p.10)*

## 25.2 What goes to the office

**The complete mission folder — not the `.mxdb` alone.**

```
TMX<serial>-<mission id>/
  ├── Base/                 base RINEX, if collected
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── POS_1/raw/            ← the one that cannot be recovered
  ├── Extcal.json           the calibration file
  └── <mission>.mxdb        an index, not the data
```

> **The `.mxdb` is a table of contents.** Copying it alone copies nothing useful
> *(Technical Manual §5.2)*.

Plus: the **field record** (§26), base station data if a local base was occupied, and any deviation
from the plan with its reason.

## 25.3 The disk rule

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

**Not on a promise, not on a message, not because the disk is needed tomorrow.** The office
confirms it, in writing *(SOP §11.2)*.

## 25.4 Handoff is a transfer of responsibility

Until the office has confirmed that verified copy, **the field holds the only copy of an
unrepeatable measurement**. Close-out is not complete when the vehicle is packed; it is complete
when the office confirms.

## 25.5 Record

What was transferred, to whom, when.

> **PARAMETRIX DECISION REQUIRED · D-52, D-53, D-54** — the offload and verification procedure,
> the folder structure and naming, and whether a chain-of-custody record is required *(SOP §11)*.
