# 23. RMS and What It Can Prove

## 23.1 The governing principle

> **TRIMBLE DOCUMENTED METHOD**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

Stated by Trimble in identical wording in two separate topics — the laser scanner calibration
topic and the run-to-run registration topic. It is the single most important sentence in the
office workflow, and the whole of this section is built on it.

### Why the asymmetry is real and not a hedge

A residual measures the fit between an adjustment and **the observations that shaped it**.

An adjustment with few observations fits them exactly — with three unknowns and three
observations there is no redundancy and the residuals are zero by construction. An adjustment
whose observations all share a systematic error fits them beautifully and carries the error
through untouched. In both cases the numbers are excellent and the data is wrong.

The reverse does not hold. If an adjustment *cannot* fit its own observations, something is
genuinely broken — bad control coordinates, misidentified targets, a trajectory too poor to
correct, a calibration that has drifted.

> **A number can prove failure. A number cannot prove success.**
>
> Only two things can suggest success: **observations that took no part in the adjustment**
> (§22), and **looking at the data** (§25.1).

## 23.2 What TBC gives you, at four levels

| Level | Indicator | Where | Source |
|---|---|---|---|
| **Per pick, live** | Easting, Northing, Elevation residual to the GCP, signed; **RMS of the fitted plane** | Validate Picking, Targets pane | *(TBC 22905)* |
| **Per run pair, every 20 m** | RMS in **Tangential, Orthogonal, Vertical**; `No overlap` where absent | Results tab, Register Run to Run | *(TBC 25096)* |
| **Whole calibration** | Overall Overlap %, Overall RMS, per-pair RMS in three axes | Calibrate Laser Scanners | *(TBC 24886)* |
| **Trajectory-wide** | Position, orientation and velocity RMS after smoothing, from `smrmsg_xxx.out` — rendered as **trajectory colour** | Plan View | *(TBC 25943, 27248)* |

Plus the visual check (§25.1) and the records in the **SOP §20**.

> **Note what is missing from that table: a single number that describes the quality of a
> registration.** There is no registration report equivalent to a least-squares adjustment
> summary. The evidence is distributed across a dialog, a results tab, a trajectory colour and
> the operator's eyes — which is why §30, the provenance problem, matters more here than it would
> in a conventional adjustment, and why the records the **SOP §20** requires are not a formality.

## 23.3 Reading the three axes

Tangential, orthogonal and vertical appear in both calibration and run-to-run registration. They
diagnose, not just describe.

| Dominant component | What it points at |
|---|---|
| **Tangential** — along travel | Timing, or along-track scale. Check the DMI scale factor (§17.3) and the time synchronisation |
| **Orthogonal** — across travel, horizontal | Heading. The hardest attitude component, and the one a single direction of travel cannot resolve (§20.3) |
| **Vertical** | Pitch, or the height component of the trajectory. Check the antenna model (§17.3) and the geoid |

> **WHY THIS MATTERS**
>
> A combined RMS hides this. Three numbers of similar size mean random disagreement, which is
> what good data looks like. One number much larger than the other two means a specific,
> identifiable part of the solution is struggling — and tells you where to look rather than
> leaving you to regenerate everything and hope.


---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at what a residual actually measures, and why Trimble says —
> twice, in two unrelated parts of its documentation — that a good RMS does not prove the work
> succeeded although a bad one proves it failed.
>
> **Why it matters.** A residual tells you how well the adjustment fitted the numbers you handed
> it. That is a narrower question than the one you care about. Hand it three points and it fits
> them perfectly, because with three observations and three unknowns there is nothing left over to
> disagree. Hand it three points that share a common error — a mis-keyed coordinate, a control
> network with a systematic bias — and it fits those perfectly too, and passes the error straight
> through into the deliverable. The arithmetic is not lying. It is answering the question it was
> asked.
>
> **What can go wrong.** Reporting a small residual as evidence of accuracy. It is evidence that
> the adjustment is internally consistent, which is a different claim and a much weaker one. The
> failure is most likely on a job with sparse control, because that is exactly where the residuals
> look best.
>
> **What good looks like.** Two things the numbers cannot give you on their own: residuals on
> points the adjustment never saw (§22), and a direct look at the data (§25). Where the three-axis
> breakdown is available, three components of similar size means random disagreement — which is
> what good data looks like. One component much larger than the other two is the solution telling
> you which part of itself is struggling.
