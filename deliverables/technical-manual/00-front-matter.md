# MX60 Mobile Mapping Technical Manual

**Trimble MX60 · Trimble Business Center 2026.10**

---

## Document control

> **Provisional.** Parametrix's document-control convention has not been confirmed. The fields
> below are present so the real scheme can be applied without restructuring; **the values are
> placeholders and the conventions are unset.**

| Field | Value |
|---|---|
| Document | **MX60 Mobile Mapping Technical Manual** |
| Identifier | *`MX60 Technical Manual — Draft A`* — provisional |
| Revision | *Draft A* — convention not yet set |
| Date | 2026-09-11 |
| Owner | *Not assigned* — **D-1** |
| Reviewer / approver | *Not assigned* |
| Status | **Draft. Not issued.** |

### Evidence revision

This manual documents **the state of the evidence, not a version of the software alone.**

| | |
|---|---|
| **Software documented** | Trimble Business Center **2026.10** · Trimble Mobile Imaging **Rev L** |
| **Trimble help topics** | **38**, captured and classified |
| **Manuals and bulletins** | **7** |
| **Release notes** | 2025.21, 2026.10 |
| **Structured reference records** | **402** — `reference/mx60-reference-data.csv` |
| **Evidence revision** | **E1 — 2026-09-11** |

> The version cross-reference: a registration feature listed as new in the TBC 2026.10 release
> notes is present in the captured help topic *(TBC RN 2026.10; TBC 22905)*. The captured material
> is therefore current, not stale.

### Related documents

| Document | Relationship |
|---|---|
| **MX60 Mobile Mapping SOP** | States what Parametrix requires. **Cites this manual for technical basis** |
| **MX60 Field How To** | Field task instructions. Cites this manual for explanation |
| **MX60 Office How To** | Processing task instructions. Cites this manual for explanation |

---

## What this manual is

**It explains what the MX60 and Trimble Business Center are actually doing, and how we know.**

It is the technical reference from which the SOP and the two How To guides are derived. Where
those documents say *you must* or *click here*, this one says *because*.

| Question | Document |
|---|---|
| **Why does it work this way?** | **This manual** |
| Must I? | SOP |
| How do I do it in the field? | Field How To |
| How do I do it in the office? | Office How To |

### What it assumes

The reader is a competent survey professional. Control networks, datums, geoids, residuals, least
squares and check points are taken as known and are not taught here.

**No prior mobile mapping experience is assumed.** Trajectories, SBETs, GNSS/INS integration,
boresight calibration, scan generation, registration and mobile LiDAR quality control are
explained from the beginning.

### What it is not

**It is not a procedure.** Nothing in this manual is a Parametrix requirement. Where it describes
what Trimble's software does, that is a statement of fact about the software — not an instruction
to do it. **Requirements live in the SOP.**

---

## How to read the evidence tags

Every technical statement carries a tag saying where its authority comes from.

| Tag | Meaning |
|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in the cited topic or manual page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software or a captured screenshot; Trimble does not state it |
| **FIELD TESTING REQUIRED** | Answerable by test, not by reading. Appendix E |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble. Appendix E |

> **This manual contains no Parametrix procedure tags.** It does not decide anything. Where a
> Parametrix decision would resolve a question, the manual names the decision — **D-*n***, cross-
> referenced to the SOP — and moves on.

### Citations

`*(TBC 22905)*` a help topic · `*(MX60 UG Rev B, p.54)*` a manual page · `*(TBC RN 2025.21)*` a
release note. Every cited topic is indexed in **Appendix A** with the TBC version it was captured
from.

> **Appendix B — the reference dataset — is the authority for numbers.** This manual explains
> what they mean. When a Trimble revision changes a value, the dataset row changes and the prose
> usually does not.

---

## In Plain English

Every major technical section ends with a box addressed to **an experienced land surveyor who is
new to mobile mapping**, answering four questions:

1. **What we just did** · 2. **Why it matters** · 3. **What can go wrong** · 4. **What a good
result generally looks like**

They re-explain rather than summarise. **Read end to end, with nothing else, they describe the
whole workflow in ordinary language** — a reviewer or project manager can get a true picture from
them alone.

> The SOP and the How To guides do **not** repeat them. The How To guides carry short **Why This
> Matters** notes that point here.

**28 sections carry one.** Three do not, deliberately: **§6** is a glossary, and **§24** and
**§31** are short reference sections with nothing to re-explain. **§21** carries two, because
registration to control and registration run-to-run are different enough to need separate
treatment.

---

## Terminology

**§6 is the authoritative glossary for all four documents.** The SOP and the How To guides carry
only the handful of abbreviations needed to use each of them safely, and point here.

Workflow stage names are frozen and identical across all four documents — see §4.

---

## Contents

**Part I — Principles** · 1 Purpose and scope · 2 Mobile mapping in plain terms · 3 How error
behaves · 4 The workflow end to end · 5 The data chain · 6 Terminology

**Part II — The system** · 7 MX60 system architecture · 8 GNSS/INS integration · 9 GAMS and DMI ·
10 TMI, TBC and POSPac · 11 LiDAR QC · 12 Coordinate systems, datums and epochs

**Part III — Acquisition explained** · 13 Initialization · 14 The closing sequence ·
15 GNSS environment and outage duration · 16 Point density and useful range

**Part IV — Processing explained** · 17 Trajectory processing · 18 Scan generation ·
19 Update Scans · 20 Calibration · 21 Registration · 22 GCPs, check points and residuals ·
23 RMS and what it can prove · 24 Trajectory RMS colouring · 25 Visual QC · 26 Imagery ·
27 Degraded GNSS · 28 Cleanup · 29 Export · 30 Provenance · 31 Periodic system verification

**Part V — Evidence** · A Trimble source index · B Reference dataset · C Figures ·
D Observed software behaviour · E Open technical questions · F Test results · G Source conflicts

---

> **PARAMETRIX BRANDING — PLACEHOLDER**
>
> Unstyled. All four documents will share one visual system, applied once when content is stable
> and branding material is supplied.
