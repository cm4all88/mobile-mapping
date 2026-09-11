# 21. Retention and Archive

## 21.1 What has to survive, and for how long

> **PARAMETRIX DECISION REQUIRED · D-55 · P1**
>
> **What is retained, where, for how long, and by whom?**

The decision is genuinely a decision — storage cost against the ability to reprocess — but it
divides cleanly, because the artefacts fall into three tiers of very different size.

## 21.2 The three tiers

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**

### Tier 1 — small, irreplaceable, and the basis of any later defence

| Artefact | Size |
|---|---|
| Field record | kB |
| Control and check designation table, with residuals | kB |
| Mission Report, run **before** Cleanup | kB |
| Calibration JSON in force at processing | kB |
| Results of Scan Generation | kB |
| Delivery record (§20.2) | kB |
| QC record (§16.8) | kB |
| The accuracy statement issued to the client | kB |

> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against
> retaining it indefinitely, and every one of these is unrecoverable.

### Tier 2 — retained for a defined period

| Artefact | Size |
|---|---|
| SBET, its processing report, and the frame and epoch log | MB |
| Numbered registered SBETs `sbet_*_reg_####.out` | MB |
| `Targets.csv` | kB |
| Base station data | MB |
| The delivered files | GB |

### Tier 3 — retained per the decision

| Artefact | Size | Note |
|---|---|---|
| **Raw mission folder** | **Tens to hundreds of GB** | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved — only re-collected |
| TBC project | Tens to hundreds of GB | The provenance record *(Technical Manual §30)* |

> **The Tier 3 decision is the expensive one and it is a real trade.** Keeping raw data means a
> better trajectory later is possible — from better base data, a POSPac upgrade, or LiDAR QC.
> Discarding it means the deliverable is final in a way it need not have been.

## 21.3 What is not discarded on one person's judgement

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> **`POS_1/raw/` and `Targets.csv` should not be deleted by an individual acting alone.**

Both are irreplaceable, and the reason is a fact about the data rather than a policy: one cannot be
recomputed from anything, and the other was picked by a person and would be different if picked
again *(Technical Manual §5.4)*. **What the proposal needs from Parametrix is who else has to
agree**, which is part of D-55.

## 21.4 The archive record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-55**
>
> One page per project, in the archive, stating: what was archived, where, when and by whom; the
> retention tier applied; whether Cleanup was run and what was archived first; and where the raw
> mission data is, if it is held elsewhere.
>
> **Without it, the archive is a folder somebody has to reverse-engineer.**

## 21.5 Records this section requires

| Record | State |
|---|---|
| The archive record | **D-55** |
| Retention tier applied, and the date the period runs from | **D-55** |
| Disposal, where it occurs — what, when, authorised by whom | **D-55** |
