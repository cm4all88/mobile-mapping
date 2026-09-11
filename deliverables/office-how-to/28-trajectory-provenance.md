# 28. Trajectory Provenance — What to Record Before You Go Further

### The limitation, stated plainly

> **IMPORTANT**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**

Inside the project, §27 gives you four layers of evidence. **Outside it, you have what you wrote
down.**

### Do

Record these, now, before Cleanup (§29) and before export (§30):

| # | Artefact | Where it comes from |
|---|---|---|
| 1 | **The delivery record** — mission ID, trajectory node name, SBET filename including `_reg_####`, registration type, export path and date, exported by whom | Written by you. Appendix F |
| 2 | **The control-and-check table** — point ID, Use XY, Use Z, As Check, residual on each | Written by you (§20). Appendix F |
| 3 | **The Mission Report**, run **before** Cleanup | *(TBC 23991_1)* |
| 4 | **The calibration JSON** in force | §13.3 |
| 5 | **`Targets.csv`** | The project folder |
| 6 | **The field record** | It came with the data (§2) |
| 7 | **The QC record** — including the visual and imagery checks | Written by you (§22, §23) |

*(SOP §20.2)*

### Expect

**Five of the seven already exist as files.** Two are written by a person. The whole package is a
few hundred kilobytes beside a project of tens of gigabytes.

### Stop if

- You are about to run Cleanup and any of items 3 to 5 is not archived
- You are about to export and item 1 does not exist

> **PARAMETRIX DECISION REQUIRED · D-29** — what provenance record accompanies a deliverable, where
> it lives, and who produces it *(SOP §20.2)*.

> **TESTING REQUIRED · T19, T22, T30** — which trajectory travels with a publish or an export; what
> a LAS file actually carries in its header, VLRs and sidecar; and whether a delivered dataset can
> be matched back to its trajectory after the fact.
