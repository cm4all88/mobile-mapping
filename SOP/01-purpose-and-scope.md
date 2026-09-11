# 1. Purpose and Scope

## 1.1 Purpose

This standard operating procedure covers mobile mapping production at Parametrix using the
**Trimble MX60** vehicle-mounted laser scanning and imaging system, and **Trimble Business
Center (TBC)** for office processing.

It exists to make three things possible:

1. **Repeatable acquisition.** Two crews on two days should collect data the same way, and a
   third person should be able to tell from the record that they did.
2. **Defensible processing.** Every adjustment applied to the data should be traceable to a
   decision someone made deliberately, with evidence of why it was acceptable.
3. **Transferable competence.** A surveyor who has never operated an MX60 should be able to
   read this document and understand what the crew did, what the office did, and where the
   result could have gone wrong.

## 1.2 What this document assumes, and what it does not

**It assumes** the reader is a competent survey professional. Control networks, datums,
geoids, residuals, least squares adjustment, check points and accuracy statements are taken as
known. This document does not teach them and does not restate them.

**It does not assume** any prior mobile mapping experience. Trajectories, SBETs, GNSS/INS
integration, boresight calibration, scan generation, registration and mobile LiDAR quality
control are explained from the beginning.

Where conventional survey practice and mobile mapping differ, the difference is explained **at
the point where it matters** rather than in a preamble. Most of those differences come down to
one thing, and §2 is about it: in mobile mapping, the instrument is never stationary, so
everything the system measures is referenced to a computed path through space rather than to an
occupied point.

## 1.3 Scope

**In scope**

- MX60 field acquisition: planning, installation, initialization, collection, field checks
- Data transfer and project organisation
- TBC office processing: import, trajectory processing, scan generation, calibration,
  registration, QC, cleanup and export
- Quality control at every stage, and the records that demonstrate it
- The decisions Parametrix must make before this becomes binding procedure

**Out of scope**

- Basic land surveying practice
- Establishing the control network the mobile mapping data will be registered to — that is
  conventional survey work and is governed by Parametrix's existing survey procedures
- Feature extraction, CAD production and deliverable drafting downstream of the point cloud
- Static terrestrial scanning, UAS and aerial workflows, except where TBC behaviour is shared
- Vehicle operation, traffic control and site safety, which are governed by Parametrix's health
  and safety procedures and by the client's requirements

## 1.4 How to read this

The document is sequential — it follows the production workflow from planning to archive — but
almost nobody needs all of it.

| If you are… | Start here | Then read |
|---|---|---|
| **A surveyor new to mobile mapping** | §2, *Mobile Mapping in Plain Terms* | §5, §12, §15, §17, §18 — and every **In Plain English** box, in order |
| **A field technician** | §4, *Equipment and Software* | §6–§10, then Appendices A–C |
| **An office technician** | §11, *Import into TBC* | §11–§22 in order, then Appendix C |
| **A project surveyor** | §17, *Control and Independent Check Points* | §5, §15, §18, §23, §24 |
| **A project manager** | §1 and §3 | §23, §24, §25 — and the **In Plain English** boxes on their own |

> **The In Plain English boxes are a complete document in themselves.** Read end to end, with
> nothing else, they describe the whole workflow in ordinary language. That is deliberate: a PM
> or a reviewer should be able to get a true picture without working through the technical
> detail.

## 1.5 How to read the evidence tags

Every instruction in this document carries a tag saying where its authority comes from. This
matters more here than in most procedures, because the MX60 workflow is new to Parametrix and
much of what looks like established practice is in fact a software default that nobody has yet
examined.

| Tag | What it means |
|---|---|
| **TRIMBLE DOCUMENTED PROCEDURE** | Trimble states this, in the cited topic or manual page |
| **OBSERVED SOFTWARE BEHAVIOR** | Seen in the software, but Trimble does not state it as procedure |
| **PARAMETRIX PROCEDURE (PROPOSED)** | This document recommends it. **It is not company policy** |
| **PARAMETRIX PROCEDURE (ADOPTED)** | Decided by Parametrix, with a date and an owner in Appendix D |
| **PARAMETRIX DECISION REQUIRED** | A choice only Parametrix can make. The question is stated; the answer is not |
| **FIELD TESTING REQUIRED** | Answerable by testing, not by reading. See Appendix E |
| **VENDOR CLARIFICATION REQUIRED** | Answerable only by Trimble. See Appendix F |

### The state of this document on first issue

> **CAUTION**
>
> **On first issue, this SOP contains no PARAMETRIX PROCEDURE (ADOPTED) entries at all.**
>
> Every Parametrix procedure in it is marked **PROPOSED**. Every acceptance threshold is marked
> **PARAMETRIX DECISION REQUIRED**. Nothing in this document is yet binding company policy, and
> nothing in it should be quoted to a client as an existing Parametrix standard.
>
> That is the correct state, not an oversight. The technical content is complete and evidenced;
> the company decisions on top of it have not been made. **Appendix D lists all of them, in
> priority order, and eleven of them should be settled before the first production job.**

## 1.6 What this document is built from

| Source | Revision | Used for |
|---|---|---|
| Trimble MX60 User Guide | Rev B, May 2025 | Hardware, installation, specifications, safety |
| Trimble MX60 Quick Start Guide | Rev B, March 2025 | Field sequence |
| Trimble Mobile Imaging (TMI) Software User Guide | Rev L, April 2026 | Field software |
| Trimble MX60 Spec Sheet | PN 022516-737C | Specifications |
| Trimble MX Shock Absorbing Mounting Rack User Guide | Rev B, May 2025 | Vehicle installation |
| Product Bulletin: Enabling the Dust Filter in TMI for MX60 | January 2025 | Laser settings |
| **Trimble Business Center help portal** | **TBC 2026.10** | **All office processing** |
| TBC Release Notes 2025.21 and 2026.10 | — | Version-dependent behaviour |

Thirty-eight TBC help topics were captured, read and classified before this document was
drafted. The full assessment is in `analysis/`, the structured data in
`reference/mx60-reference-data.csv` (402 records), and the cited topic index in **Appendix G**.

> **The CSV is the authority for numbers.** This document explains what they mean. When a
> Trimble revision changes a value, the CSV row is updated and the prose usually is not.

### A note on version

The captured TBC help documents **TBC 2026.10**, confirmed by cross-reference: a registration
feature listed as new in the 2026.10 release notes is present in the captured help topic
*(TBC RN 2026.10; TBC 22905)*.

> **VENDOR CLARIFICATION REQUIRED**
>
> **Which TBC version is installed on the Parametrix processing workstation?** Two behaviours
> in this document depend on it, and both are legacy: calibrating outside TBC (versions up to
> 5.21) and a prompt for a missing RMS file (projects saved before 5.80). Both boundaries
> predate 5.70, the oldest release Trimble still publishes notes for, so any recent
> installation is unaffected — but this should be confirmed rather than assumed. *(Appendix F)*

## 1.7 Revision and ownership

> **PARAMETRIX DECISION REQUIRED**
>
> **Who owns this document, who approves revisions, and on what cycle is it reviewed?**
>
> Nothing in this SOP establishes an owner, an approver or a review interval, because no such
> assignment has been made. A procedure with no owner decays quietly — the software changes
> underneath it and nobody is responsible for noticing.
>
> Two things make this more pressing than usual. TBC is now on an annual release cycle
> (2023.10 through 2026.10), and each release has changed mobile mapping behaviour. And the
> MX60 itself is recent — TMI support arrived in December 2024 *(TMI UG Rev L, p.2)* — so the
> documentation underneath this SOP is still moving.
>
> *Register item 1. See Appendix D.*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set out what this document covers, who it is for, and — most
> importantly — how to tell the difference between something Trimble says, something the
> software does, and something Parametrix has decided. Right now that last category is empty.
>
> **Why it matters.** Mobile mapping produces enormous, convincing-looking datasets very
> quickly. A point cloud with a hundred million points looks authoritative whether or not the
> trajectory underneath it was ever checked. The only thing standing between "looks right" and
> "is right" is a procedure that says what was done and what was verified — and a reader who
> can tell which parts of that procedure someone actually thought about.
>
> **What can go wrong.** The most likely failure with a new SOP is not that somebody ignores
> it. It is that somebody reads a software default in it, assumes it was chosen deliberately,
> and defends it to a client. That is why the tags exist and why nothing in this document is
> yet marked as adopted. If you find yourself citing this SOP as a Parametrix standard, check
> the tag first.
>
> **What good looks like.** You should be able to open any page of this document, point at any
> instruction, and answer in one sentence: *who says so?* If you cannot, the tag is missing and
> the document has a defect worth reporting.
