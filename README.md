# Parametrix MX60 Mobile Mapping documentation

Trimble MX60 Premium · Trimble Business Center 2026.10

**Start here: [`deliverables/`](deliverables/README.md).** That is the live set. Everything else in
this repository either feeds it, checks it, or has been superseded by it.

> **Nothing here is an issued Parametrix standard.** Every Parametrix procedure is marked
> **PROPOSED**, every acceptance threshold is marked **PARAMETRIX DECISION REQUIRED**, and the
> adoption record is empty. **Parametrix-originated requirements adopted: 0.** Some requirements
> bind anyway, because their authority is Trimble's or the equipment's rather than Parametrix's;
> those are listed with their sources at SOP §2.4.

## What is where

| | |
|---|---|
| **[`deliverables/`](deliverables/README.md)** | **The live set.** Four documents — Technical Manual, SOP, Field How To, Office How To — plus the control layer that governs them |
| [`reference/`](reference/) | `mx60-reference-data.csv`, **the authority for every number** in the set |
| [`sources/`](sources/) | TBC help captures and extracted source text |
| [`analysis/`](analysis/) | Build records: how the sources were ingested and classified |
| [`tools/`](tools/README.md) | The builders and the twelve gates. `python3 tools/check-all.py` |
| [`brand/`](brand/README.md) | Logo assets and brand extractions |
| [`marketing/`](marketing/README.md) | **The only outward-facing material.** Governed separately — see its README |
| `SOP/` | **Superseded.** The single-document generation |
| `SOP-v1-superseded/` | **Superseded.** The first draft |
| Root `*.pdf` | The source documents. What each one is, and whether anything rests on it, is in Technical Manual Appendix A |

## The four documents, and why there are four

Each carries one kind of content. The test for where something belongs: if you removed it, which
question becomes unanswerable?

| Document | Answers | Content |
|---|---|---|
| **Technical Manual** | *Why does it work, and how do we know?* | Explanation and evidence. Every statement traceable to a Trimble topic or manual page |
| **SOP** | *What must I do?* | Requirements only. It states what is required and points to the manual for explanation |
| **Field How To** | *How, in the field?* | Task steps, checklists, stop-if conditions |
| **Office How To** | *How, in TBC?* | Task steps, command sequences, checklists |

A click sequence belongs in a How To and nowhere else. An explanation belongs in the Manual and
nowhere else. A requirement belongs in the SOP. Where the same thing is maintained in two places it
drifts, and the audit of 2026-09-19 removed the instances that had.

## Before editing anything

1. Read [`deliverables/00-DELIVERABLE-ARCHITECTURE.md`](deliverables/00-DELIVERABLE-ARCHITECTURE.md).
2. Numbers change in `reference/mx60-reference-data.csv` first, never in prose.
3. Open items change in `deliverables/_control/master-register.csv` first, then
   `python3 tools/build-register-views.py`. **There is one register.** An item cannot be open in one
   document and closed in another.
4. Run `python3 tools/check-all.py` before committing. Twelve gates, all of which must pass.

## Building

```bash
npm install                      # node_modules is not tracked
python3 tools/check-all.py       # the gates
python3 tools/build-doc.py manual|sop|field|office
python3 tools/build-register-views.py
python3 tools/sync-control.py
```

## Open items

The current count and the list of what each one blocks are generated into
`deliverables/_control/views/blocking.md` — read it there rather than from a number typed into
prose. The suggested order for working through them is in the Technical Manual Appendix E and SOP
Appendix A.
