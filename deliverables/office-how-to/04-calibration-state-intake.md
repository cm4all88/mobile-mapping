# 4. Calibration-State Intake

**Do this at intake, not later.** A later project cleanup (§29) removes the objects that would
produce the report.

### Do

1. **Copy `Extcal.json` out of the raw mission folder** into the project record, named with the
   system serial number and the mission date
2. Run the **Mission Report** — *(TBC 23991_1)*
3. Archive the report into the project record

### Look at

The report's **Capture devices** table. It carries per-sensor **boresight installation** and
**boresight refinement**, and a **date of calibration**.

### Expect

A date of calibration you can point at, for each sensor.

### Stop if

- **The calibration date cannot be established.** Which calibration a mission was processed
  against is a question somebody will ask later, and the answer has to exist now
- The calibration date is older than whatever interval Parametrix has set

> **PARAMETRIX DECISION REQUIRED · D-26**
>
> The recalibration interval and its triggers — including whether daily removal of the Sensor Unit
> counts as disturbing the calibration *(SOP §14.2)*.

> **That dated record is the only one found anywhere in the workflow** *(Technical Manual §30)*.
> There is no other place the software tells you when the system was last calibrated.

### Record

`Extcal.json` and the Mission Report, both in the project record. Which calibration this mission
was processed against.
