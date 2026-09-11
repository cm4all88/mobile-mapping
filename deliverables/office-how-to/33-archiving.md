# 33. Archiving

### Do

1. Assemble the **record package** (§28) — seven artefacts, a few hundred kilobytes
2. Decide and apply the **retention tier** for everything else
3. Write the **archive record** — one page
4. Put it where somebody who was not involved can find it

### Look at — the three tiers

**Tier 1 — small, irreplaceable, keep indefinitely**

Field record · control-and-check table with residuals · Mission Report run **before** Cleanup ·
calibration JSON · Results of Scan Generation · delivery record · QA/QC record · the accuracy
statement issued.

> **The whole of Tier 1 is a few hundred kilobytes.** There is no storage argument against keeping
> it.

**Tier 2 — a defined period**

SBET and its processing report and the frame-and-epoch log · numbered registered SBETs ·
`Targets.csv` · base station data · the delivered files.

**Tier 3 — per the decision**

| | Size | Note |
|---|---|---|
| **Raw mission folder** | Tens to hundreds of GB | **The only thing that permits reprocessing.** Once gone, the deliverable cannot be improved, only re-collected |
| TBC project | Tens to hundreds of GB | The provenance record |

*(SOP §21.2)*

### Stop if

- **You are about to delete `POS_1/raw/` or `Targets.csv` on your own judgement.** Neither is
  recoverable: one cannot be recomputed, the other was picked by a person and would be different if
  picked again *(SOP §21.3)*
- The archive record does not exist

> **PARAMETRIX DECISION REQUIRED · D-55** — what is retained, where, for how long, by whom
> *(SOP §21.1)*.

> **PARAMETRIX DECISION REQUIRED · D-53** — folder structure, naming and storage location.

### The archive record

One page per project: what was archived, where, when, by whom; the retention tier applied; whether
Cleanup was run and what was archived first; and where the raw mission data is, if it is held
elsewhere.

**Without it, the archive is a folder somebody has to reverse-engineer.**

### Record

The archive record itself. Appendix F.
