# Appendix C — QC Checklist

**Eight layers. Each catches something the others cannot.** None is optional because another one
looked fine.

| ☐ | # | Layer | Evidence produced | § |
|---|---|---|---|---|
| ☐ | 1 | Field coverage verification | Field record | 2 |
| ☐ | 2 | Intake checks — seven | Intake record | 3 |
| ☐ | 3 | **Trajectory RMS review** | Screen capture | 10 |
| ☐ | 4 | Residuals on control points used | Targets pane | 20 |
| ☐ | 5 | **Residuals on independent check points** | **Written by you** | 20 |
| ☐ | 6 | **Visual inspection — Cutting Plane View, Scan Color** | **Written by you** | 22 |
| ☐ | 7 | **Imagery inspection** | **Written by you** | 23 |
| ☐ | 8 | Export-state confirmation | Screen capture | 31 |

## C1 · Layer 6 in detail

| ☐ | Check | Looking for |
|---|---|---|
| ☐ | Rendering set to **Scan Color** | Without it the check does not work |
| ☐ | Overlapping passes, plane dragged full length | Doubled surfaces |
| ☐ | Flat surfaces at range | Thickening with distance |
| ☐ | The ends of the corridor | Where a Local adjustment stopped |
| ☐ | The degraded stretches from layer 3 | Whether registration fixed them |
| ☐ | Vertical against horizontal | Systematic tilt |
| ☐ | Near control versus far from control | Residual growth with distance |

## C2 · Layer 7 in detail

| ☐ | Check |
|---|---|
| ☐ | Coverage — gaps where a camera stopped or a run was not colorized |
| ☐ | Exposure — blown highlights, blocked shadows. Both unrecoverable |
| ☐ | Motion blur |
| ☐ | Obstruction — aerials, following vehicle, smear on the dome |
| ☐ | Focus and contamination |
| ☐ | **Corrupted images — silent, export as black** |
| ☐ | Alignment with the point cloud at feature edges |

## C3 · Before you call it done

| ☐ | |
|---|---|
| ☐ | **As Check residuals exist and are recorded** |
| ☐ | No layer was skipped |
| ☐ | Layers 6 and 7 were written down — **nothing else records them** |
| ☐ | Nothing is being accepted on RMS alone |
| ☐ | **No acceptance tolerance has been invented or quoted** — D-13 is open |
