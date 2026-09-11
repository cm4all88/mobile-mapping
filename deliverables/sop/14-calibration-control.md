# 14. Calibration Control

## 14.1 What calibration is, in one line

TBC's laser scanner calibration estimates the **angular** offsets between sensors. Lever arms are
**measured, not estimated** *(Technical Manual §7.6, §20.2)*. A wrong lever arm cannot be
calibrated out, because the adjustment has no parameter for it.

An angular error acts through range: the same error is ten times larger at 100 m than at 10 m
*(Technical Manual §3.1)*.

## 14.2 Currency

> **PARAMETRIX DECISION REQUIRED · D-26 · P1**
>
> **What is the recalibration interval, and what triggers a recalibration outside it?**
>
> The specific question that has to be answered explicitly: **does daily removal and refitting of
> the Sensor Unit count as disturbing the calibration?** If the unit comes off the vehicle between
> jobs, the answer determines whether calibration is an annual event or a per-mobilisation one.

**No mission shall be processed against a calibration whose currency cannot be established.** The
calibration state in force is captured at intake (§12.3), which is what makes this checkable.

## 14.3 The calibration site

> **PARAMETRIX DECISION REQUIRED · D-24**
>
> **Where is the calibration site, and who maintains it?**

Trimble specifies the geometry, and two different procedures need compatible sites:

| | Requirement | Source |
|---|---|---|
| **Laser scanner calibration** | Two streets crossing at **90° ± 30°**, at least **20 m** usable on each side and ideally **80 m** total, façades in each direction, little vegetation | TBC 24886 |
| **LiDAR QC** | Two perpendicular strips, each **250–300 m**, each driven in both directions; structured scene; open sky | TBC 28972 |

> **PARAMETRIX PROCEDURE (PROPOSED) · D-24**
>
> **Establish one site that satisfies both** — two streets crossing near 90°, façades on all four
> approaches, little vegetation, **125–150 m of usable street on each arm**, open sky, drivable in
> both directions without traffic-control complications.
>
> The two requirements are compatible and the stricter one should govern. Establishing such a site
> is real work — reconnaissance, a traffic plan, possibly permission — and doing it once, well,
> before it is needed under schedule pressure is worth more than the procedure it supports.

## 14.4 Judging a calibration

> **CAUTION**
>
> Trimble states, in identical words in two separate topics:
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **A calibration shall not be accepted on RMS alone.** The visual check is part of the
> acceptance, not an optional extra *(Technical Manual §23.1, §25)*.

## 14.5 The calibration record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **Export the calibration JSON after every calibration and archive it outside the TBC project**,
> named with the system serial number and the calibration date.
>
> It is the complete calibration state of the system in one small file, it can be imported into any
> subsequent project, and it is the only portable record of what the system's angles were on a
> given date. Cleanup (§17) or a lost workstation should not take it with them.

## 14.6 Periodic system verification

Distinct from per-project QC: the check that the **instrument** is still performing.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, p.7)*
>
> Scan approximately **eight flat retro-reflecting targets** at varied distances over more than
> **180° horizontally**, previously surveyed by total station. The system passes if residuals fall
> within the specified accuracy. Trimble recommends doing this "regularly" and "especially before
> starting an extensive data acquisition campaign" — and **gives no interval**.

> **PARAMETRIX DECISION REQUIRED · D-28**
>
> **Is this the periodic verification Parametrix adopts, and at what interval?**

> **TESTING REQUIRED · V-14**
>
> Whether Trimble or the dealer expects this check specifically, and at what period.

## 14.7 Records this section requires

| Record | State |
|---|---|
| Calibration performed — date, site, who, and the result including the visual check | **D-26** |
| The calibration JSON, archived outside the project | **D-55** |
| Which calibration each mission was processed against | **D-55** |
| Periodic verification, when performed | **D-28** |
