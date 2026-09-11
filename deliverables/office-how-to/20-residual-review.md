# 20. Residual Review

### Do

1. Read the residuals in the **Targets** pane and in the **Validate Picking** window
2. Separate them: **residuals on points used in the adjustment** and **residuals on points held As
   Check**
3. Write both into the control-and-check table (Appendix F)
4. Read the three-axis breakdown where you have one

### Look at — what TBC gives you, at four levels

| Level | Indicator | Where |
|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, **signed**; RMS of the fitted plane | Validate Picking, Targets pane *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in tangential / orthogonal / vertical; `No overlap` | Results tab, Register Run to Run *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair three-axis | Calibrate Laser Scanners *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation, velocity RMS after smoothing | Plan View colouring (§10) |

### Look at — the three axes, when you have them

| Dominant component | Points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor and time synchronisation |
| **Orthogonal** — across travel | **Heading.** The hardest component, and the one a single direction of travel cannot resolve |
| **Vertical** | Pitch, or the height component. Check the antenna model (§8) and the geoid |

Three similar-sized components mean random disagreement, which is what good data looks like. **One
much larger than the other two is the solution telling you which part of itself is struggling**
*(Technical Manual §23.3)*.

### Expect

Residuals on the **used** points to be small. That is not evidence of anything — an adjustment with
few observations fits them exactly, and one whose observations share a systematic error fits them
beautifully and carries the error straight through.

### Stop if

> **CAUTION**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*
>
> **A number can prove failure. A number cannot prove success.**

Stop if:

- **There are no As Check residuals.** Nothing is measuring the result
- A check-point residual is much larger than the used-point residuals, and you are about to promote
  it into the adjustment. **Do not.** Read §15 again
- One three-axis component dominates. Diagnose it before accepting

> **What TBC does not report.** No captured topic produces a statement of **which points were used
> as control and which as checks** in a registration already applied. The state is visible while
> the command is open and reloads on **Edit** *(TBC 25362, 26578)* — but no report of it has been
> found.
>
> **TESTING REQUIRED · T21, V-11.** TBC 2025.21 says signed residuals are "included in the report"
> without naming it, and the only mobile mapping report topic does not mention residuals. Ten
> minutes with the software answers it.

### Record

The control-and-check table: point ID, Use XY, Use Z, As Check, and the residual on each. **Six
columns, written once.** It is the single most important record in the workflow and the software
does not produce it (§28, SOP §19).
