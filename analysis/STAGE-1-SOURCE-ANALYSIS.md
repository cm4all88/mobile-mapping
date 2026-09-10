# Stage 1 — Source Analysis for the Parametrix MX60 Mobile Mapping SOP

**Prepared:** 2026-09-10
**Status:** For review. No SOP drafting has begun.

---

## Headline finding

The uploaded collection totals **641 pages across 8 PDFs (5 distinct documents)**.

**Exactly 3 of those pages are Trimble MX60 / TMI operating documentation**, and they
cover one narrow feature — the field dust filter.

There is **no MX60 User Guide, no TMI software manual, no TBC mobile mapping
documentation, no datasheet, no installation guide, and no calibration procedure** in
the set. The single Trimble bulletin we do have explicitly refers the reader to the
"Trimble MX60 User Guide" for how to measure system installation height — a document
that is not in the collection.

The SOP as scoped cannot be written from this material. What *can* be written is
described in section 3 below, and it is a substantial and genuinely useful document —
but it is a mobile-laser-scanning practice manual, not an MX60 operating procedure.

---

## 1. Source inventory

### 1.1 — Product Bulletin: Enabling the Dust Filter in TMI for Trimble MX60

| Field | Value |
|---|---|
| Date / version | January 2025 (marked PUBLIC) |
| Publisher | Trimble Inc., Geospatial |
| Pages | 3 |
| Appears current | **Yes** — newest Trimble document in the set |

**Subject.** The field dust filter available in TMI for MX60: when to use it, how it
is enabled, and what must be true for it to work correctly.

**Relevant SOP sections.** 7 (installation height), 9 (TMI interface), 11 (collecting),
17 (point cloud quality), 22 (troubleshooting).

**What it actually gives us.** This is the only document in the entire collection that
describes the MX60 being operated. Specifically:

- The TMI UI path: **Mission Presets tab → Capture settings** (p.1)
- The **laser waterfall view** as the operator's live check on filter behaviour (p.3)
- Laser effective measurement rate settings of **500 kHz and 1000 kHz**, with 1000 kHz
  recommended in dusty conditions (p.3)
- **"Reconfigure mission"** as a mid-mission capability, with capture settings prepared
  in advance (p.3)
- System installation height must be measured **strictly vertically, perpendicular to
  the MX60 XY plane, to 2–3 cm**, to the **external reference cross on the right side
  of the mounting rack** (p.2)
- A documented failure mode: **installation height entered too high → filter mask
  touches ground → data loss**, visible immediately as gaps in the waterfall view (pp.2–3)
- Support contact: mx_support@trimble.com (p.3)
- Four figures (Pic 1–4) illustrating the filter box area, usable in the SOP

**Limitations.** Single-feature scope. Explicitly defers to the absent MX60 User Guide.
Says the filter is "not foreseen" for paved roads and urban canyons but does not state
the consequence of using it there anyway.

---

### 1.2 — "Mobile Mapping, Artificial Intelligence and Digital Data Optimize Road Infrastructure Management"

| Field | Value |
|---|---|
| Date / version | Smart Engineering Special Issue, © 2025 V1 Media |
| Author | Kevin Garcia, GM Civil Specialty Construction, Trimble |
| Pages | 2 |
| Appears current | Yes (2025) |

**Subject.** Trimble's six-phase road infrastructure management workflow, from mobile
mapping capture through TBC, Unity, Earthworks/Roadworks, to maintenance.

**Relevant SOP sections.** 1, 2, 15 — **context only**.

**Limitations — important.** This is **clearly labelled sponsored content**
("ENGINEERED SOLUTIONS — Sponsored by Trimble"). It contains no procedures, no
specifications, no settings, and no operating limits. It confirms only that the MX60
and MX90 exist, that the systems include a dedicated pavement-facing camera, and that
TBC offers AI point cloud classification and feature extraction. The Caltrans savings
figures it cites are promotional.

**This document must not be cited as technical authority anywhere in the SOP.**

---

### 1.3 — Mobile Laser Scanning Technical Guideline

| Field | Value |
|---|---|
| Date / version | March 2023 |
| Publisher | Queensland Department of Transport and Main Roads (TMR) |
| Pages | 65 |
| Licence | **CC BY 4.0** — free to adapt with attribution |
| Appears current | Yes for its jurisdiction |

**Subject.** A road authority's technical specification for MLS capture and delivery:
control framework, boresight calibration, pass requirements, point cloud variables,
imagery, uncertainty testing, classification, and QA reporting.

**Relevant SOP sections.** 5, 7, 11, 12, 16, 17, 18, 19, 20, 14, 27, 28.

**This is the strongest operational document in the collection.** Highlights:

- **Minimum three passes** on the pavement, and multi-scanner systems do **not** get to
  count simultaneous scans as independent passes (§8, p.8)
- **Boresight calibration immediately before *and* again at the end of each project**,
  and again any time the system is disturbed or reassembled (§6, p.7)
- Carriageway pass patterns for single/divided/dual carriageway (§8.1, pp.9–10)
- Contractor is responsible for **increasing passes in poor GNSS environments** and
  reporting those areas (§8.2, p.10)
- Horizontal/vertical **survey uncertainty** vs **relative uncertainty** within 200 m
  sliding windows (§11.2–11.5, App A–D)
- **Useful range statement** requirement — the honest admission that a cloud extending
  200 m is only accurate to project spec over a much shorter distance (§11.7, pp.18–19)
- Point scale factor caution: up to **40 mm per 100 m** error if plane distances are
  delivered as grid coordinates (§11.7, p.19)
- Imagery: avoid early morning and late afternoon, **8am–4pm usually ideal**; do not
  capture in wet conditions; both sides of double-sided signs (§10, p.15)
- Night capture as a mitigation for parked-vehicle occlusion (§9.3, p.12)
- Cleansing guidance: **do not delete, reclassify** (§11.8.1, p.19)
- Check point / check site regimes: ≥10 points per site, ≥10 m apart (App F)
- A complete **QA reporting deliverable list** (§14, p.25) including trajectory strings
  attributed with RMSE per vertex, and a required statement on how IMU and wheel encoder
  observations are applied during GNSS loss
- A ready-made **glossary** (§2, pp.1–4) directly usable for SOP Section 27

**Limitations.** Queensland-specific throughout: GDA94/GDA2020, AHD71, MGA zones 54–56,
AUSGeoid, ICSM SP1 v2.2 uncertainty framework, TMR Surveying Standards, Form 6 / PSM
registration with Department of Resources, and 12d Model `.12daz` deliverables. **None
of this transfers to Parametrix without substitution.**

Critically, **most numeric tolerances are left as variables** — (x), (y), (yy), (z),
(zz), (zzz) — to be filled in per project by the *MLS Technical Guideline Checklist*,
which is **not in the collection**. The guideline gives us the *framework* for
tolerances, not the tolerances.

Vendor-neutral: never mentions Trimble or the MX60.

---

### 1.4 — NCHRP Synthesis: Practices for Collecting, Managing, and Using Lidar Data

| Field | Value |
|---|---|
| Date / version | 2024 |
| Authors | Michael J. Olsen, Heidar Rastiveis (Oregon State); Gene V. Roe (MPN Components) |
| Publisher | Transportation Research Board / NCHRP (National Academies) |
| Pages | 211 |
| Appears current | Yes |

**Subject.** A synthesis of US state DOT practice in collecting, managing, and using
lidar data. Literature review, survey of all 50 states plus DC (100% response), and
five case-example interviews (Oregon, Tennessee, Wisconsin, Colorado, Texas).

**Relevant SOP sections.** 2, 3, 14, 19, 20, 21, 26.

**What it gives us.** Lidar data life cycle and governance, data formats, QA practice
across platforms, accuracy expectations by platform (**64.7% of DOTs target cm-level
for mobile lidar**, p.80), outsourcing patterns (**92.9% of DOTs outsource at least
some mobile lidar work**), and vehicle-mounted lidar strengths and challenges (pp.19–20,
including calibration maintenance, vibration, and data volume).

**Limitations.** **Descriptive, not prescriptive** — it documents what DOTs *do*, not
what an operator *must* do. Contains no MX60 content, no step-by-step procedures, and
no equipment operating instructions. Its accuracy figures are survey responses about
aspiration, **not achievable tolerances**, and must not be quoted as such.

Two disclosures worth noting in a document that cites it: the authors state ChatGPT 4/4o
was used to edit and organise the report (p.iv), and co-author Olsen declares a financial
interest in a lidar processing software company (p.iv).

**Copyright caution.** The report states it is owned by the National Academy of Sciences,
free for "personal and/or non-commercial academic use," and that **all other uses require
written permission**. An internal Parametrix commercial SOP is arguably outside that
grant. Brief cited quotation is normal practice; extensive reproduction is not. Flagged
for Parametrix decision.

---

### 1.5 — 3D Reconstruction and Mobile Mapping in Urban Environments Using Remote Sensing

| Field | Value |
|---|---|
| Date / version | 2024, MDPI *Remote Sensing* Special Issue reprint |
| Editors | San Jiang, Duojie Weng, Jianchen Liu, Wanshou Jiang |
| Pages | 360, split across **4 PDFs** |
| Licence | Articles CC BY; book as a whole CC BY-NC-ND |

**This is the "multiple PDFs of the same book."** I verified continuity by printed page
number: Part 1 = pp.2–95, Part 2 = pp.96–171, Part 3 = pp.172–265, Part 4 = pp.266–345.
**The set is complete with no gaps and no overlap.**

**Subject.** Fifteen peer-reviewed research papers on 3D reconstruction, SLAM, point
cloud registration, and urban mobile mapping.

**Relevant SOP sections.** 25 (Advanced) only, and thinly.

**Assessment.** The majority of the papers are off-topic for an MX60 operating procedure
— spherical image feature matching, UAV neural radiance field reconstruction of ancient
buildings, breakwater stability by RANSAC, satellite stereo building heights, InSAR point
cloud registration, ground penetrating radar. Roughly four papers touch the underlying
physics an advanced section might reference:

- *LVI-Fusion: A Robust Lidar-Visual-Inertial SLAM Scheme* (Part 2)
- *Enhanced SINS/LiDAR Tightly Integrated SLAM for Urban Structural Feature Weaken
  Occasions in Vehicular Platform* (Part 3) — relevant to GNSS-denied behaviour
- *Research on a Matching Method for Vehicle-Borne Laser Point Cloud and Panoramic
  Images Based on Occlusion Removal* (Part 3)
- *Image-Aided LiDAR Extraction, Classification, and Characterization of Lane Markings
  from Mobile Mapping Data* (Part 4)
- *High-Precision Map Construction in Degraded Long Tunnel Environments* (Part 3)

**Limitations.** Academic research, not operating guidance. No Trimble hardware, no TBC,
no procedures. Useful at most for a few "why this matters" explanations in Section 25.
**This book contributes very little to a field SOP** despite being 56% of the page count
you uploaded.

---

## 2. What is missing

Documents that the SOP scope requires and that are **not** in the collection:

| Missing document | Blocks SOP sections |
|---|---|
| **Trimble MX60 User Guide** (referenced by the dust filter bulletin, p.2) | 3, 6, 7, 8, 9, 10, 12, 13, 14, 22, 23, 28 |
| **TMI software manual / help** | 8, 9, 10, 12, 13, 22 |
| **MX60 datasheet / technical specifications** | 3, 16, 17, 18, 20 |
| **MX60 installation / vehicle mounting guide** | 7 |
| **Calibration documentation** (boresight, lever arm) | 7, 25 |
| **TBC mobile mapping module documentation** | 15, 16, 19, 25 |
| **Release notes / firmware / version history** | all |
| **Safety documentation** | 4, 6, 7 |
| **Data offload / storage media procedures** | 13, 14 |

---

## 3. Section-by-section feasibility against current sources

**Can be written well now (source-supported):**

- §2 Mobile mapping in plain language — NCHRP Ch.2
- §5 Pre-field planning — TMR §§8–10, NCHRP
- §11 Collecting data, *partially* — multi-pass strategy and lane selection (TMR §8),
  poor-GNSS strategy (TMR §8.2), reduced speed and no harsh manoeuvres in dust (bulletin p.3)
- §16 Understanding trajectory — TMR §14(b)(c), NCHRP, MDPI SINS/LiDAR paper
- §17 Point cloud quality — TMR §§9, 11.7, 11.8
- §18 Imagery quality — TMR §10
- §19 Control and mobile mapping — TMR §§5, 12, App E–F (reframed for US practice)
- §20 Quality control — TMR §§11, 14 + NCHRP QA chapter
- §21 When mobile mapping does not work well — TMR §9.3 shadowing, NCHRP
- §25 Advanced, *partially* — boresight rationale (TMR §6), MDPI papers
- §27 Glossary — TMR §2 is a ready-made starting point

**Cannot be written without more sources:**

- §3 System components — **no specifications exist in the set**
- §6 Equipment preparation — no Trimble checklist available
- §7 Vehicle installation — only the installation-height measurement survives
- §8 Starting the MX60 — **nothing**; no power sequence, boot, or connection procedure
- §9 TMI field interface — only four UI elements known
- §10 Initialization — **nothing**; no GNSS/IMU procedure, manoeuvres, speeds, or durations
- §12 Monitoring while driving — nothing beyond the waterfall view
- §13 Ending a collection — **nothing**
- §14 Data handling — nothing MX60-specific
- §15 TBC workflow — nothing beyond "TBC does AI feature extraction"
- §22 Troubleshooting — exactly one documented failure mode
- §23, §24, §28 — depend on the above

Sections 8, 10, and 13 are the operational heart of the SOP, and all three are
**completely unsourced**.

---

## 4. Proposed table of contents

Your 28-section structure is sound and I would carry it essentially intact. Three
structural changes I recommend, now informed by the sources:

1. **Move Trajectory (§16) ahead of the TBC workflow (§15).** A reader who understands
   what a trajectory is will follow trajectory processing far better than one meeting
   both at once.
2. **Split Vehicle Installation (§7)** into daily/every-project checks versus
   trained-personnel configuration work. TMR §6 makes boresight a formal, scheduled,
   consequence-bearing procedure — it does not belong beside a daily mount check.
3. **Merge §22 and Appendix G.** Keep the troubleshooting table authoritative in §22 and
   have the appendix reference it, so there is one place to maintain.

I also recommend adding, given what the sources emphasise:

- **A "service level" section early on** distinguishing survey-grade capture (full
  control framework) from asset-grade capture (TMR §11 explicitly permits a "GNSS only
  solution" where high accuracy is not needed). Conflating these is a common and
  expensive mistake, and the distinction drives control cost, pass count, and QC effort.

---

## 5. PARAMETRIX DECISION REQUIRED — foreseeable items

Items 1–16 are structural. Items 17–28 arise directly from the source documents.

| # | Decision | Section |
|---|---|---|
| 1 | Raw data storage location and project/mission folder structure | 14 |
| 2 | Project and mission naming convention | 14 |
| 3 | Backup policy — how many copies, where, retained how long | 14 |
| 4 | Raw source data retention and archive policy | 14, 20 |
| 5 | Who may perform calibration / lever-arm work; required training | 7, 25 |
| 6 | Operator qualification and sign-off before production work | 24 |
| 7 | Positional accuracy tolerances for accept / review / recollect | 20 |
| 8 | Independent check point density and distribution | 19, 20 |
| 9 | Who authorises a recollection; how remobilisation cost is handled | 20, 21 |
| 10 | GNSS correction source standard — own base, RTX, VRS, or CORS post-processing | 5 |
| 11 | Traffic control requirements and go/no-go by roadway class | 5 |
| 12 | Deliverable formats and coordinate conventions for clients | 15 |
| 13 | Imagery privacy and retention (faces, plates, private property) | 18 |
| 14 | QC documentation — what report per project, and who signs it | 20 |
| 15 | Equipment assignment, custody, and damage reporting | 6 |
| 16 | Escalation path when the operator hits a problem mid-collection | 22 |
| 17 | **Minimum pass count.** TMR requires 3 and refuses to count a multi-scanner system's simultaneous scans as independent. Does Parametrix adopt 3, or a project-driven rule? | 11 |
| 18 | **Boresight calibration frequency.** TMR requires it before *and* after every project, and after any disassembly. Adopt, relax, or defer to Trimble's (absent) procedure? | 7, 25 |
| 19 | **Uncertainty framework.** TMR uses ICSM SP1 (Australian). Parametrix needs a US equivalent — NSSDA, ASPRS 2014 Positional Accuracy Standards, or client-specified | 19, 20 |
| 20 | **Datum and epoch policy**, including the NATRF2022 / NAPGD2022 transition | 5, 15 |
| 21 | **Useful range statement.** Will Parametrix publish a per-project statement of the width over which the cloud actually meets spec? (TMR §11.7 requires it; it is good defensive practice) | 20 |
| 22 | **Intensity normalisation and bit depth** for delivered point clouds (TMR mandates 16-bit, 0–65535) | 15, 17 |
| 23 | **Pass identification in delivered LAS.** TMR encodes pass number in LAS classes 21, 22, 23, 24+. Non-standard but useful for QC. Adopt? | 15, 20 |
| 24 | **Imagery capture window** and wet-weather stand-down criteria (TMR: 8am–4pm, no wet capture) | 5, 18 |
| 25 | **Night collection policy** for parked-vehicle occlusion — permitted, and under what conditions? | 5, 11, 21 |
| 26 | **Point cloud cleansing policy** — TMR requires reclassify-not-delete. Adopt? | 15, 20 |
| 27 | **Service level definitions** — survey-grade versus asset-grade capture, and who decides which applies | 1, 5, 19 |
| 28 | **Third-party copyright use** — how much NCHRP material may be reproduced in an internal commercial SOP given its non-commercial licence terms | all |

---

## 6. Contradictions and unclear points in the sources

1. **Dust filter scope is asymmetric.** The bulletin says the filter is "not foreseen"
   for paved roads and urban canyons, but never states the consequence of enabling it
   there. Unclear whether it is harmful or merely pointless. (Bulletin p.1)

2. **Installation height error is only described in one direction.** Too high → mask
   touches ground → data loss. The effect of entering it too low is not stated.
   (Bulletin p.2)

3. **Laser rate guidance is dust-specific only.** 1000 kHz is recommended over 500 kHz
   *in dusty conditions*. No document explains the general trade-off — presumably range
   versus measurement rate — or what to use normally. (Bulletin p.3)

4. **Mid-mission reconfiguration is described but not explained.** "You can reconfigure
   mission using capture settings" with presets "prepared in advance," but the mechanism,
   and whether it breaks the mission into separate files, is not covered. (Bulletin p.3)

5. **Multi-scanner pass independence.** TMR explicitly rules that two scanners capturing
   simultaneously share one GNSS constellation and therefore do not provide redundancy,
   requiring three passes regardless. This sits in direct tension with the usual vendor
   position that a dual-head system needs fewer passes. Trimble's documentation is absent,
   so this cannot be resolved from the sources — but Parametrix will meet the argument on
   real projects. (TMR §8, p.8)

6. **Boresight before and after every project** is stricter than common industry practice,
   and we have no Trimble procedure describing how to perform one on an MX60. The
   requirement is stated; the method is unavailable. (TMR §6, p.7)

7. **Two service levels are easy to conflate.** TMR §11 permits a "GNSS only solution"
   where high accuracy is not required, alongside a full PRF control framework elsewhere
   in the same document. Read carelessly, this looks contradictory; it is actually two
   distinct service levels. The SOP must make this explicit.

8. **NCHRP accuracy figures are aspirations, not specifications.** "64.7% of state DOTs
   emphasise cm-level accuracy for mobile lidar" is a survey response about intent. It is
   not evidence that cm-level is achievable on a given corridor, and must not migrate into
   the SOP as a tolerance.

9. **No document in the collection states MX60 accuracy specifications at all** — not
   range accuracy, not precision, not trajectory performance. Any accuracy claim in the
   SOP would have to come from a source we do not have.

---

## 7. Recommendation

Obtain, at minimum:

1. **Trimble MX60 User Guide** — unblocks the largest number of sections
2. **TMI software documentation** — unblocks Sections 8–13
3. **MX60 datasheet / specifications** — unblocks Section 3 and every accuracy statement
4. **TBC mobile mapping workflow documentation** — unblocks Section 15

These are normally available through the Trimble Survey Partners portal
(https://surveypartners.trimble.com/), which the bulletin cites on every page, or from
the Trimble mobile mapping support team (mx_support@trimble.com, bulletin p.3).

If the Trimble documentation cannot be obtained, the honest alternative is to retitle
the deliverable as a **Parametrix Mobile Laser Scanning Practice Manual** — covering
planning, control, collection strategy, quality control, and limitations from the TMR
and NCHRP sources — and treat MX60-specific operation as a separate document to be
written when the manuals are in hand.
