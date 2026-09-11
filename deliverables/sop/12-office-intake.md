# 12. Office Intake Requirements

## 12.1 The principle

Everything checked at intake is cheap; everything discovered later is not. Intake is also the last
point at which re-collection is still a small decision.

## 12.2 What is verified at import

> **PARAMETRIX PROCEDURE (PROPOSED) · D-18**
>
> Before any processing:
>
> | # | Check | Why |
> |---|---|---|
> | 1 | **Project coordinate system** matches the control network and the client requirement | Changing it afterwards is irreversible in practice (§6.2, W-05) |
> | 2 | **Covered distance** is consistent with the field record | |
> | 3 | **Run count** matches the field record | Fewer runs than the crew logged means data was lost in transfer |
> | 4 | **The active trajectory** is the intended one, and is **SBET rather than NAV** unless there is a recorded reason | *(Technical Manual §17.2)* |
> | 5 | **Capture Devices** lists the sensors expected for the configuration | A missing camera or laser means a sensor was disabled or failed in the field (§9.1) |
> | 6 | **Base station data** is present if the trajectory will be processed in house | |
> | 7 | **The calibration state the mission was collected under is recorded** | See §12.3 |
>
> Seven checks, none taking more than a minute.

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

## 12.3 Capture the calibration state

`Extcal.json` travels with the raw mission data, and the **Mission Report** carries per-sensor
boresight and lever-arm calibration **with a date of calibration** *(TBC 24868)*.

> **That dated calibration record is the only one found anywhere in the workflow**
> *(Technical Manual §30)*. It is captured at intake because a later Cleanup can remove the
> objects that would have produced it (§18).

## 12.4 What intake does not do

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Intake should not correct anything.** If a check fails, it is recorded and raised (§22).

A processor who quietly fixes a coordinate system mismatch at intake has removed the evidence that
the field and office disagreed — which is the reason the practice is proposed, and the reason it
matters more than it looks.

## 12.5 Records this section requires

| Record | State |
|---|---|
| Intake checks performed, by whom, with the result of each | **D-18** |
| Calibration state at collection — `Extcal.json` and the Mission Report | **D-55** |
| Any intake check that failed, and what was done | **D-18, §22** |
