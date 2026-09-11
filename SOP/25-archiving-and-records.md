# 25. Archiving and Records

## 25.1 Why this section carries more weight than usual

In most survey work the archive is a formality — the deliverable and its report tell the story,
and the archive is insurance.

In mobile mapping it is the primary evidence. §23 established that **the captured Trimble
documentation does not establish that an exported deliverable uniquely identifies the adjusted
trajectory or registration result used to create it.** The project and Parametrix's own records
are therefore where the processing history lives, and an archive that does not hold them holds a
point cloud and a coordinate system.

> **PARAMETRIX DECISION REQUIRED · D-55**
>
> **What is retained, where, for how long, and who is responsible?**
>
> **This document does not establish a retention policy.** What follows is a gap analysis and a
> proposal, so the decision has something concrete to react to.

## 25.2 What exists, and what is at risk

| Artefact | Where it is | At risk from |
|---|---|---|
| **Raw mission folder** — `.mxdb`, `POS_1/raw`, imagery, scanner data, `Extcal.json` | The offload location (§10) | Disk reuse; storage cost pressure |
| **Base station data** | `Base/` in the mission folder | Same |
| **SBET and its processing report** | `NAVPROC/Export/`, `NAVPROC/Report/` *(TBC 25943)* | Project deletion |
| **Frame and epoch log** — from **Backup SBET Next to MXDB** | Beside the `.mxdb` *(TBC 25943)* | **Only exists if the option was enabled** (§12.4) |
| **Numbered registered SBETs** `sbet_<date>_reg_####.out` | Project folder *(TBC 22905)* | **Cleanup — untested, T28** |
| **`Targets.csv`** — the picked registration observations | Project *(TBC 22905)* | Cleanup; a "No" answer to the reload prompt |
| **Calibration JSON** — Installation and Refinement matrices | Exported on demand *(TBC 22920)* | Never created unless someone exports it |
| **Mission Report** — devices, runs, trajectories, scans, **calibration with date** | Run on demand *(TBC 23991_1, 24868)* | **Only exists if run, and only reports what survives Cleanup** |
| **Results of Scan Generation** — filters, range, colorization | A dialog *(TBC 22499)* | Not persisted unless captured |
| **Run-to-run RMS statistics** | Results tab *(TBC 25096)* | Not persisted unless captured |
| **Control / check designation and residuals** | **Nowhere — TBC is not documented as reporting it** (§17.6) | Lost unless recorded manually |
| **Visual QC performed** | **Nowhere** (§24 Layers 6–7) | Lost unless recorded manually |
| **Field record** | **Nowhere — a Parametrix artefact** (§8.9) | Lost unless written |
| **The TBC project itself** | Storage | Size; Cleanup (§21) |
| **The delivered files** | Delivery location | — |

> **Four of those artefacts have no software home at all.** The control/check designation, the
> residuals on each, the visual QC record, and the field record exist only if a person writes them
> down.

## 25.3 A proposed retention framework

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted. Offered for D-55.*
>
> ### Tier 1 — retain for the life of the record
>
> Small, irreplaceable, and the basis of any later defence.
>
> | Artefact | Size |
> |---|---|
> | Field record | kB |
> | Control / check designation table with residuals | kB |
> | Mission Report, run **before** Cleanup | kB |
> | Calibration JSON in force at processing | kB |
> | Results of Scan Generation | kB |
> | Delivery record — §23.6 | kB |
> | Final QA/QC record — §24.4 | kB |
> | The accuracy statement issued to the client | kB |
>
> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against
> retaining it indefinitely.
>
> ### Tier 2 — retain for a defined period
>
> | Artefact | Size |
> |---|---|
> | SBET, its processing report, and the frame/epoch log | MB |
> | Numbered registered SBETs `sbet_*_reg_####.out` | MB |
> | `Targets.csv` | kB |
> | Base station data | MB |
> | The delivered files | GB |
>
> ### Tier 3 — retain per the decision
>
> | Artefact | Size | Note |
> |---|---|---|
> | Raw mission folder | **Tens to hundreds of GB** | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved, only re-collected |
> | TBC project | **Tens to hundreds of GB** | The provenance record (§23) |

> **The Tier 3 decision is the substantive one**, and it is a genuine trade-off. Raw data permits
> reprocessing when a better trajectory solution, a correction to a lever arm, or a client's
> changed requirement makes it worthwhile. It is also the largest single storage cost Parametrix
> will carry from this workflow.

## 25.4 Sequencing — archive before Cleanup

> **CAUTION**
>
> **Cleanup Mobile Mapping Mission is destructive and not undoable** (§21). Several Tier 1 and
> Tier 2 artefacts are produced from the project and **can only report what still exists**.
>
> The Mission Report in particular must be run **before** Cleanup, not after.

The ten-step sequence is in §21.6. It is a proposal, pending D-35.

> **FIELD TESTING REQUIRED · T28 — high priority**
>
> **Does Cleanup delete the `sbet_*_reg_####.out` files from storage, or only remove the
> corresponding project objects?** Distinguish **project object retention** from **underlying file
> retention**; do not assume one implies the other. The answer determines whether those files must
> be copied out beforehand. *(§23.5; Appendix I)*

## 25.5 Imagery and privacy retention

> **PARAMETRIX DECISION REQUIRED · D-32**
>
> **Are unblurred originals retained after a blurred deliverable is issued, and for how long?**
>
> Mobile mapping imagery routinely captures pedestrians, licence plates, private property and
> building interiors visible through windows (§19.6). Retaining the unblurred originals preserves
> the ability to re-derive a deliverable; it also retains the material the blurring existed to
> remove. This has legal and reputational dimensions outside the scope of this SOP and should not
> be settled by default.

## 25.6 The archive record

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> One page per project, in the archive, stating: what was archived, where, when, by whom; the
> retention tier applied; whether Cleanup was run and what was archived first; and where the raw
> mission data is, if retained elsewhere.
>
> **Without it, the archive is a folder somebody has to reverse-engineer.** *(D-55)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We worked out what has to be kept, and — more importantly — which of it
> exists only if somebody deliberately creates it.
>
> **Why it matters.** In ordinary survey work the archive is insurance you hope never to open. Here
> it is the primary evidence, because the delivered file does not carry its own processing history.
> If somebody queries a result in three years, the answer comes from the project and from what
> Parametrix wrote down, or it does not come at all.
>
> **What can go wrong.** Four of the most important records have no home in the software. Which
> points were control and which were checks, what the residuals were on each, whether the visual
> check was done and over what extent, and what the conditions were like in the field — TBC does
> not produce any of that. It exists if a person writes it down and it does not exist otherwise.
>
> The second failure is sequencing. Several of the records are produced *from* the project, so
> running the tidy-up command before generating them means they can only report what survived.
>
> **What good looks like.** A few hundred kilobytes per project that you keep forever — the field
> record, the control/check table with residuals, the mission report, the calibration file, the
> delivery note and the QA record. A clear decision about the big stuff: how long the raw mission
> data stays, knowing that once it goes the job can only be re-collected, never re-processed. And
> one page saying what was archived, where, and by whom — so the next person does not have to work
> it out from folder names.
