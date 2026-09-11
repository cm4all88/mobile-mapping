# 19. Documentation and Records

## 19.1 Why the record carries unusual weight here

In conventional survey work the observations are the record: field notes, raw files, an adjustment
report. In mobile mapping, several of the things that determine whether a deliverable is correct
**produce no software artefact at all**.

| Fact | Software artefact |
|---|---|
| Which points were control and which were independent checks | **None** — TBC does not report it *(Technical Manual §22.7)* |
| That the visual inspection was performed, and over what extent | **None** |
| That the imagery inspection was performed | **None** |
| The conditions at collection — occlusion, weather, traffic | **None** |
| Which trajectory a delivered cloud was built on | **Partial, and not conclusive** *(Technical Manual §30)* |

**Those five facts are either written down at the time or lost.**

## 19.2 The record package

> **PARAMETRIX DECISION REQUIRED · D-29 · P1**
>
> **What provenance record accompanies a deliverable, where does it live, and who produces it?**

> **PARAMETRIX PROCEDURE (PROPOSED) · D-29**
>
> A minimal package that closes the gap:
>
> | # | Artefact | Size |
> |---|---|---|
> | 1 | **A one-page delivery record** per dataset: mission ID, trajectory node name, SBET filename including its `_reg_####` number, registration type, export path and date, exported by whom | kB |
> | 2 | **The control and check table** — point ID, Use XY, Use Z, As Check, and the residual on each | kB |
> | 3 | **The Mission Report**, run **before** Cleanup (§17.3) | kB |
> | 4 | **The calibration JSON** in force (§14.5) | kB |
> | 5 | **`Targets.csv`** (§17.3) | kB |
> | 6 | **The field record** (§9.6) | kB |
> | 7 | **The QC record** (§15.8), including the two layers with no software artefact | kB |
>
> Seven artefacts. Five of them are small files that already exist; two are written by a person.
> **The whole package is a few hundred kilobytes.**

## 19.3 Where records live

**In the project record** (§3.2) — durable, not on a processor's local machine, and findable by
someone who was not involved.

> **PARAMETRIX DECISION REQUIRED · D-53**
>
> Folder structure, naming and storage location (§11.4).

## 19.4 When they are made

**At the time.** A record reconstructed later is a reconstruction, and the facts most worth having
are exactly the ones that cannot be reconstructed.

## 19.5 Index of records this procedure requires

The full index, section by section, is **Appendix B**.

## 19.6 What a record is for

Not compliance. Three specific uses, each of which has happened to somebody:

| | |
|---|---|
| **A question about a deliverable, years later** | "Which trajectory was this built on, and what was it checked against?" |
| **A test result that changes what a past deliverable means** | **T18** and **T19** both have this shape. If either returns a result meaning a past export was not what it was believed to be, the record is what identifies which deliverables are affected |
| **Improving the work** | The relationship between GNSS conditions, control density and achieved accuracy on Parametrix corridors is not published anywhere and cannot be, because it is specific to this system and these roads. It can only be learned from a record of what was done and what came out |

## 19.7 Records this section requires

| Record | State |
|---|---|
| The delivery record, per §19.2 | **D-29** |
| The control and check table, with residuals | **D-29** |
| Where the record package lives for a given project | **D-53** |
