# 4. The Workflow, End to End

Every stage, in order, with what it produces and where it is. **Read this once and the rest of
the document has a shape.**

| | Stage | What it produces | § |
|---|---|---|---|
| **Plan** | Project setup and control | A CRS, a control network that brackets the job, designated check points | 5 |
| | Mission planning | A route, a pass pattern, mapped GNSS-hostile stretches and a mitigation for each | 6 |
| **Field** | Preparation and preflight | A mounted, calibrated, measured system | 7 |
| | Acquisition | A mission: raw scanner, imagery and navigation data | 8 |
| | Field QC | Confirmation the data **exists and is complete** — not that it is good | 9 |
| | Transfer | A verified copy, in two places | 10 |
| **Office** | Import | An **index** in TBC. Still no point cloud | 11 |
| | **Trajectory processing** | The **SBET** — the computed path. *The accuracy ceiling is set here* | 12 |
| | **Generate Scans** | The point cloud, by applying the trajectory to the raw scanner data | 13 |
| | *(Calibration)* | Sensor boresight angles. **Periodic — most projects skip this** | 14 |
| | **Registration** | A **better trajectory**, fitted to surveyed control. *The cloud has not moved* | 15, 16 |
| | **Update Scans** | A **new point cloud**, on the registered trajectory. **Without this the registration reaches nothing** | 13.6 |
| | QC | Residuals, independent checks, and a visual inspection | 17, 18, 19 |
| | *(Degraded GNSS)* | A branch, if QC fails — and two of its three remedies had to be arranged in the field | 20 |
| | *(Cleanup)* | A light project with one answer. **Destructive and not undoable** | 21 |
| **Deliver** | Export | The deliverable — which may not identify the trajectory that produced it | 22, 23 |
| | Final QA/QC | Ten layers of verification, before it leaves | 24 |
| | Archive | The records that let the work be defended later | 25 |

Three things to carry out of that table:

1. **The trajectory is computed once and improved twice** — at §17, then at §21. Everything
   else either applies it or checks it.
2. **Registration and Update Scans are two steps.** Doing the first without the second leaves the
   deliverable unadjusted, and it looks identical.
3. **Bracketed stages are conditional.** Calibration is periodic. The degraded-GNSS branch and
   Cleanup happen only when the job calls for them.


## 4.1 Frozen stage names

The stage names in the table above are **frozen**. They are used identically in this manual, the
SOP, both How To guides, every checklist and form, and future training material.

| | |
|---|---|
| Project setup · Mission planning · Field preparation · Acquisition · Field QC · Transfer | |
| Intake · Trajectory processing · Scan generation · Calibration · Registration · Update Scans | |
| QC · Degraded-GNSS handling · Cleanup · Export · Final QA/QC · Archive | |
| **Provenance** — cross-cutting rather than a stage | |

> **A stage is not a command.** *Registration* is the stage; **Register a Run**, **Register a
> Mission** and **Register Run to Run** are three commands that perform it (§21). **Update Scans**
> is unusual in being both a stage name and a command name, and that is Trimble's doing.

The authoritative list, with the synonyms that are not to be used, is
the glossary at **§6**.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We laid out every stage from planning to archive on one page, with what
> each produces.
>
> **Why it matters.** Read once, it gives the rest of the manual a shape. The three things worth
> carrying away are in the table's closing notes: the trajectory is computed once and improved
> twice; registration and Update Scans are two separate steps; and several stages are conditional
> rather than routine.
>
> **What can go wrong.** Treating the conditional stages as routine, or the routine ones as
> optional. Calibration is periodic — most projects skip it. Cleanup is destructive — some projects
> should skip it. Update Scans is neither, and skipping it silently undoes a registration.
>
> **What good looks like.** Anyone on the team using the same word for the same stage. That sounds
> trivial until two people are discussing "registration" and one means the adjustment while the
> other means the whole office process.
