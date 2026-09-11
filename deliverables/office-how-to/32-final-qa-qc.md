# 32. Final QA/QC — Working the Layers

**Each layer catches something the others cannot.** None is optional because another was performed.

### 32.1 Do

Work them in order and record each.

| # | Layer | Catches | Where | Artefact |
|---|---|---|---|---|
| 1 | **Field coverage verification** | Missing passes, missing overlap | Field record | Field record |
| 2 | **Intake checks** | Transfer loss, wrong CRS, missing sensors | §3 | Intake record |
| 3 | **Trajectory RMS review** | Where the solution was weak — **before any cloud exists** | §10 | Screen capture |
| 4 | **Residuals on control** | A broken adjustment | §20 | Targets pane |
| 5 | **Residuals on independent checks** | An adjustment that fits its own observations and is still wrong | §20 | **Written by you** |
| 6 | **Visual inspection of the cloud** | Doubled surfaces, thickening at range, tilt | §22 | **No software artefact** |
| 7 | **Imagery inspection** | Coverage, exposure, blur, corruption | §23 | **No software artefact** |
| 8 | **Export-state confirmation** | Delivering the unregistered cloud | §31 | Screen capture |

*(SOP §16.2)*

### 32.2 Look at

Layer 5 especially. **Residuals on points that took no part in the adjustment are the only
numerical evidence that means anything**, and they exist only if somebody designated check points
before registration began (§15).

### 32.3 Expect

Layers 6 and 7 to produce nothing you can file unless you write it. **Two of the eight layers have
no software artefact at all.** If a reviewer asks whether the visual check was performed and over
what extent, the only possible answer is a record somebody wrote.

### 32.4 Stop if

- **There are no As Check residuals**
- Any layer was skipped because another one looked fine
- You are about to accept on RMS alone

> **CAUTION**
>
> **"Good RMS values do not mean that the calibration succeeded. A visual check is needed. On the
> other side, bad RMS values mean that the calibration failed."** *(TBC 24886, 25096)*

### 32.5 Acceptance is not yours

**Acceptance is a decision by the person with the authority under SOP §4**, recorded, against the
project's stated accuracy requirement. Your job is to produce the evidence, not to conclude.

> **PARAMETRIX DECISION REQUIRED · D-13 · blocks formal acceptance**
>
> **What constitutes an acceptable registration and an acceptable point cloud is not established.**
> Trimble publishes no acceptance tolerance for the MX60 and none has been set by test. **Do not
> invent one, and do not quote one.**
>
> **What is blocked is formal acceptance, not the work.** You can process, register and inspect a
> dataset with D-13 open — this section is how. What cannot happen is an acceptance resting on a
> Parametrix standard, because there is not one. Whoever signs is signing on their own documented
> judgement.
>
> The decision put to Parametrix — whether interim acceptance against a project-specific written
> requirement is permitted at all — is **SOP §17.2**.

### 32.6 Record

The QA/QC record: every layer, who performed it, when, and over what extent. Appendix C and
Appendix F.
