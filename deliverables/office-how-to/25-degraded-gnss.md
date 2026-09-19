# 25. Degraded GNSS — Choosing and Applying a Remedy

You are here because §10 showed a degraded stretch. **Four remedies, and they are not
interchangeable.**

### 25.1 Look at — what each costs and what it needs

| Remedy | Acts on | Needs | Section |
|---|---|---|---|
| **Reprocess with better base data or settings** | The GNSS side of the solution | Raw data intact; better corrections available | §8 |
| **LiDAR QC** | Adds scan data as a third aiding sensor | **Overlapping runs**, and a very large workstation | §24 |
| **PFIX** | Injects surveyed control into a **second POSPac pass** | **POSPac licence**, surveyed control, picked targets | §26 |
| **Registration to control** | Bends the finished trajectory to fit control | Surveyed control | §16, §17 |

> **The first three improve the *solution*. Registration improves the *fit*.** That distinction
> matters: a registered trajectory has been adjusted to agree with the control it was given, so its
> agreement with that control is no longer evidence of anything *(Technical Manual §8.5)*.

### 25.2 Do

1. Establish how long the degraded stretch is **in time**, not in metres
2. Check what you actually have: overlap? control bracketing it? a POSPac licence?
3. Choose. Prefer a remedy that improves the solution over one that improves the fit
4. Apply it, then **re-check against independent check points** (§20)

### 25.3 Expect

Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
nothing beyond *(MX60 UG Rev B, p.56)*:

| | Core / Pro | **Premium — ours** |
|---|---|---|
| No outage | X,Y < 0.01 m · Z 0.01 m | X,Y < 0.01 m · Z 0.01 m |
| **After 60 s outage** | X,Y **0.12 m** · Z **0.1 m** | X,Y **0.1 m** · Z **0.07 m** |

**Use the Premium column.** The no-outage row assumes a DMI, which this system may not carry.

### 25.4 Stop if

- **The outage is materially longer than 60 seconds.** Beyond the published figure you are
  extrapolating past the manufacturer's stated envelope. Inertial drift is not linear
- **No remedy applies** — no overlap, no bracketing control, no licence. Then the honest finding is
  that **mobile mapping may not be the appropriate acquisition method for that segment**, and that
  goes up, not into the deliverable

> **PARAMETRIX DECISION REQUIRED · D-34** — the decision rule when a corridor produces an
> unacceptable trajectory: who decides, against what, and what the client is told *(SOP §22.5)*.

> **The remedies that need something from the field cannot be arranged now.** Overlap for LiDAR QC
> and control bracketing a hostile stretch are mission-planning decisions *(SOP §8)*. If they were
> not made, the option does not exist today.

### 25.5 Record

Which remedy, why, and the check-point residuals before and after.


> **IN PLAIN LANGUAGE**
>
> **What this section means.** What you can and cannot do about a stretch where the satellites were
> blocked and the trajectory drifted.
>
> **Why it matters.** Only some remedies actually add information. Control in the affected stretch
> adds real, independent information. Registering the bad pass to a good one adds consistency but no
> new truth. Knowing which is which keeps you from making a dataset look better without making it
> better.
>
> **Remember this.** If there is no overlap, no control bracketing the stretch and no reprocessing
> option, the honest outcome is to say the stretch does not meet the requirement — not to smooth it
> until it looks acceptable.
>
> **If this is skipped.** A degraded stretch is delivered inside an otherwise good dataset, carrying
> the same accuracy statement as the rest of it.
