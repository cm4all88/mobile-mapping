# 15. GCP and Check Point Configuration

**Three independent choices per point.** This is the most consequential configuration in the
office workflow and it is three checkboxes.

### 15.1 Do

For each point, in the **Control Points** list of a registration command:

| Setting | Meaning |
|---|---|
| **Use XY** | The point constrains the adjustment horizontally |
| **Use Z** | The point constrains the adjustment vertically |
| **As Check** | The point is paired and measured, **but excluded from the adjustment** |

They are per-point and per-component. A point can be **Use XY** and **As Check** in Z — used
horizontally, held out vertically.

### 15.2 Look at

The designation you were given (§14), and set it. **Do not decide it here.**

### 15.3 Expect

A mixture. A painted road-surface mark is usually Use XY and not Use Z. A point held out entirely
is a validation point.

### 15.4 Stop if

- **Every point is set As Check.** TBC will not compute — the adjustment has nothing to fit
- **No point is set As Check.** Then nothing measures the result, and the residuals you are about
  to read measure only how well the adjustment fitted observations it was given *(§20)*
- **You are about to change an As Check setting during processing.** Stop. That designation was
  fixed before registration began, and changing it is a Project Surveyor decision that gets
  recorded and requires the registration to be recomputed from the imported trajectory using
  **Edit** (§19) — not layered on top *(SOP §7.3)*

> **PARAMETRIX DECISION REQUIRED · D-15**
>
> **Is the control/check designation fixed before registration and unchangeable during it?**
> Recommended at **SOP §7.3**.

> **The failure this prevents.** A conscientious processor registers a mission, finds one check
> point with a larger residual than expected, and adds it to the adjustment to bring it in. Every
> step is well intentioned. The result is an adjustment with **no independent check at all**, and a
> set of residuals that now measure nothing *(Technical Manual §22.4)*.

### 15.5 Record

Point ID, Use XY, Use Z, As Check — for every point, **outside TBC**. The software does not
appear to report it (§20, §28).
