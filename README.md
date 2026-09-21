# Parametrix MX60 Mobile Mapping documentation

Trimble MX60 Premium · Trimble Business Center 2026.10

**Start here: [`deliverables/`](deliverables/README.md).** That is the live set. Everything else in
this repository either feeds it, checks it, or has been superseded by it.

## Purpose of the set

This package is for **survey staff who already understand basic surveying but may have little or no
MX60 Premium experience**. It is intended to let them operate the system, process the data,
recognize when something is wrong, troubleshoot common problems, and know when to stop and raise
an issue.

It is **not a land surveying course**. Control networks, datums, adjustments, check observations
and professional survey judgement are assumed. The documents teach the MX60 Premium and its
workflow, not surveying itself.

A new MX60 user should normally start in the **Field How To** or **Office How To**. The Technical
Manual is a reference for why the system behaves as it does and for abnormal or unfamiliar cases.
The SOP defines what is required and who has authority.

Because this is a **living document set**, some items are intentionally deferred until the actual
Parametrix MX60 and software build can be inspected. Those are not filled with generic screenshots
or guessed configuration values. They are tracked in
[`deliverables/_control/equipment-arrival-validation-checklist.md`](deliverables/_control/equipment-arrival-validation-checklist.md)
and are replaced with unit-specific evidence when the equipment is available.

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
| [`tools/`](tools/README.md) | The builders and the QA gates. `python3 tools/check-all.py` |
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
| **Technical Manual** | *Why is the MX60 or TBC behaving this way?* | Technical reference and evidence. Used for explanation, troubleshooting depth and unusual conditions |
| **SOP** | *What is required, and who has authority?* | The controlled operating rules. It does not teach surveying or replace the How To guides |
| **Field How To** | *How do I operate and troubleshoot the MX60 in the field?* | **Primary field training and operating guide**. Task steps, normal indications, stop conditions and troubleshooting |
| **Office How To** | *How do I process and troubleshoot MX60 data in TBC?* | **Primary office training and processing guide**. Click paths, expected results, stop conditions and troubleshooting |

The two How To guides are the normal learning path for someone new to the MX60. A click sequence,
screen check, normal indication, first troubleshooting action or stop condition belongs there. The
Technical Manual carries the deeper explanation and evidence. A requirement belongs in the SOP.
Basic survey instruction belongs in none of them.

## Before editing anything

1. Read [`deliverables/00-DELIVERABLE-ARCHITECTURE.md`](deliverables/00-DELIVERABLE-ARCHITECTURE.md).
2. Numbers change in `reference/mx60-reference-data.csv` first, never in prose.
3. Open items change in `deliverables/_control/master-register.csv` first, then
   `python3 tools/build-register-views.py`. **There is one register.** An item cannot be open in one
   document and closed in another.
4. Run `python3 tools/check-all.py` before committing. Every gate must pass.

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
