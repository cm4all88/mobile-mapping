# Appendix F — Record Templates

Five templates for the records that **have no software artefact**. Each is small. Each is
unrecoverable if it is not written at the time.

---

## F1 · Control and check table

**The single most important record in the workflow**, and TBC does not produce it (§20).

| Project | | Mission | | Registration name | |
|---|---|---|---|---|---|
| Designated by | | Date designated | | Registered by | |

| Point ID | Use XY | Use Z | As Check | Residual E | Residual N | Residual Elev | Notes |
|---|---|---|---|---|---|---|---|
| | ☐ | ☐ | ☐ | | | | |
| | ☐ | ☐ | ☐ | | | | |
| | ☐ | ☐ | ☐ | | | | |

> **Designation is fixed before registration and is not changed during it** (§15, SOP §7.3). If it
> changes, the Project Surveyor decides, it is recorded here with a date, and the registration is
> recomputed using **Edit** — not layered on top.

---

## F2 · Delivery record

One page per delivered dataset.

| | |
|---|---|
| Project | |
| Mission ID | |
| **Trajectory node name** | |
| **SBET filename, including `_reg_####`** | |
| Registration type | Global · Local · Global then Local · Run to Run |
| Update Scans confirmed | ☐ stations carry `_reg_####` |
| Export path | |
| **Export timestamps** | ☐ No ☐ Yes — *if Yes, state the recorded reason* |
| Scaling | ☐ Grid ☐ Ground ☐ ECEF · scale factor communicated: ☐ |
| Coordinate system, datum, epoch | |
| Export date | | 
| Exported by | |
| Delivered to | |

---

## F3 · QA/QC record

| Layer | Performed by | Date | Extent covered | Result |
|---|---|---|---|---|
| 1 Field coverage verification | | | | |
| 2 Intake checks | | | | |
| 3 Trajectory RMS review | | | | |
| 4 Residuals on control | | | | |
| 5 **Residuals on independent checks** | | | | |
| 6 **Visual inspection** | | | | |
| 7 **Imagery inspection** | | | | |
| 8 Export-state confirmation | | | | |

| | |
|---|---|
| Accuracy requirement assessed against | |
| Accepted by | |
| Acceptance date | |

> **Acceptance is not the processor's.** It is a decision by the person with the authority under
> SOP §4, against the requirement stated at project setup.

---

## F4 · Cleanup authorisation and archive-first record

| | |
|---|---|
| Project · Mission | |
| **Authorised by** | |
| Authorisation date | |
| Mission Report archived | ☐ · location: |
| Registration evidence recorded | ☐ |
| `Targets.csv` archived | ☐ · location: |
| Numbered SBET files archived | ☐ · location: |
| Calibration JSON archived | ☐ · location: |
| Project backup taken | ☐ · location: |
| **Cleanup run by** | |
| **Date run** | |

---

## F5 · Archive record

One page per project.

| | |
|---|---|
| Project | |
| Archived by · date | |
| What was archived | |
| Where it is | |
| **Retention tier applied** | ☐ Tier 1 ☐ Tier 2 ☐ Tier 3 |
| Retention period runs from | |
| Cleanup run? | ☐ No ☐ Yes — see F4 |
| **Where the raw mission data is**, if held elsewhere | |
| Disposal, if any — what, when, authorised by | |

> **Without this, the archive is a folder somebody has to reverse-engineer.**
