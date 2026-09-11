# Topic ownership matrix

**The most operationally useful document in this folder.** It answers: *when one technical fact
changes, which documents need review?*

| | |
|---|---|
| **●** | **Owns it.** The authoritative statement lives here and changes here first |
| **ref** | References it. Carries a cross-reference, not a copy. **Review when the owner changes** |
| **—** | Does not mention it. No review needed |

> **Rule: exactly one ● per row.** If a topic needs two owners it is two topics.

> **The ● column is a design decision and is set by hand. The ref / — columns are derived** from
> the documents by `tools/sync-control.py`, which reads every *Technical Manual §n* reference each
> document actually makes. Do not edit them: they describe the documents rather than instructing
> them, and a hand-edited value drifts the moment anyone writes a cross-reference.
>
> Rows whose owner is not a Manual section cannot be derived this way, and their ref / — cells are
> still set by hand.
>
> Run `python3 tools/sync-control.py --check` before an issue. It exits non-zero on drift.

---

## Principles and concepts

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| What a trajectory is; why everything depends on it | Manual §2 | ● | ref | — | — |
| How mobile mapping error behaves — range, correlation in time | Manual §3 | ● | ref | — | ref |
| The workflow end to end | Manual §4 | ● | ref | — | — |
| The data chain — `.mxdb`, SBET, TMX, RWCX; no MTA on MX60 | Manual §5 | ● | ref | ref | ref |
| **Terminology and glossary** | **Manual §6** | ● | ref | ref | ref |
| GNSS/INS integration | Manual §8 | ● | ref | — | ref |
| GAMS and DMI — what each contributes | Manual §9 | ● | ref | ref | — |
| Coordinate systems, datums, epochs as mobile mapping uses them | Manual §12 | ● | ref | — | ref |

## System

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| MX60 architecture, sensors, configurations | Manual §7 | ● | ref | ref | — |
| TMI, TBC, POSPac and the licensing gates | Manual §10 | ● | ref | — | — |
| LiDAR QC — what it is and needs | Manual §11 | ● | ref | — | ref |
| Battery Protect behaviour | Manual §7 | ● | ref | ref | — |
| **What to do when the Battery Protect alarm sounds** | **Field §7** | ref | — | ● | — |

## Acquisition

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| Why initialization works — what the static period and manoeuvres solve | Manual §13 | ● | ref | ref | — |
| **How to initialize** | **Field §12** | ref | ref | ● | — |
| **That initialization is required** | **SOP §9** | — | ● | ref | — |
| Why the closing sequence exists | Manual §14 | ● | ref | ref | ref |
| **How to perform the closing sequence** | **Field §21** | ref | ref | ● | — |
| GNSS environment and outage duration | Manual §15 | ● | ref | ref | — |
| Point density and useful range | Manual §16 | ● | ref | ref | — |
| **Operating limits — speed, weather, stand-down** | **SOP §9** | ref | ● | ref | — |
| **Field record contents** | **SOP §9** | — | ● | ref | ref |
| **The field record form** | **Field App. C** | — | ref | ● | — |

## Processing

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| Trajectory processing — settings, SBET naming, ITRF00 path | Manual §17 | ● | ref | — | ref |
| **How to process a trajectory** | **Office §8–10** | ref | ref | — | ● |
| Scan generation — filters, colorization, what each removes | Manual §18 | ● | ref | — | — |
| **Which filters to use** | **SOP §13** *(pending D)* | ref | ● | — | ref |
| **How to generate scans** | **Office §11–12** | ref | ref | — | ● |
| **Update Scans — why registration does not move points** | **Manual §19** | ● | ref | — | — |
| Calibration theory, site geometry | Manual §20 | ● | ref | — | — |
| **Calibration interval, triggers, currency** | **SOP §14** | ref | ● | ref | ref |
| **How to calibrate** | **Office §13** | ref | ref | — | ● |
| Registration theory; the three commands | Manual §21 | ● | ref | — | — |
| **Who may register; who accepts** | **SOP §4** | — | ● | — | ref |
| **How to register** | **Office §16–19** | ref | ref | — | ● |
| Control vs check; why independence matters | Manual §22 | ● | ref | — | ref |
| **Control density, bracketing, designation rule** | **SOP §7** | ref | ● | ref | ref |
| **How to configure control and checks in TBC** | **Office §15** | ref | ref | — | ● |
| The RMS asymmetry | Manual §23 | ● | ref | — | ref |
| Reading trajectory RMS colouring | Manual §24 | ● | ref | — | — |
| Visual QC — Cutting Plane View, Scan Color | Manual §25 | ● | ref | — | ref |
| **How to perform visual QC** | **Office §22** | ref | ref | — | ● |
| **What QC must be performed and recorded** | **SOP §15** | ref | ● | ref | ref |
| **Acceptance criteria** | **SOP §16** *(pending D-13)* | ref | ● | — | ref |
| Imagery — resolution, colorization, failure modes | Manual §26 | ● | ref | — | ref |
| Degraded GNSS — three remedies and what each costs | Manual §27 | ● | ref | — | ref |
| **How to apply a degraded-GNSS remedy** | **Office §24–26** | ref | ref | — | ● |
| Periodic system verification | Manual §31 | ● | — | — | — |

## Delivery and control

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| Cleanup — what it destroys | Manual §28 | ● | ref | — | — |
| **Cleanup authorisation and prerequisites** | **SOP §17** | ref | ● | — | ref |
| **How to run Cleanup safely** | **Office §29** | ref | ref | — | ● |
| Export paths — what each carries | Manual §29 | ● | — | — | — |
| **Export release gate** | **SOP §18** | ref | ● | — | ref |
| **How to export** | **Office §30–31** | ref | ref | — | ● |
| Provenance chain and the limitation | Manual §30 | ● | ref | ref | ref |
| **Required provenance records** | **SOP §19** | ref | ● | ref | ref |
| **Retention tiers and periods** | **SOP §20** | ref | ● | — | ref |
| **How to archive** | **Office §33** | ref | ref | — | ● |
| **Transfer and custody requirements** | **SOP §11** | — | ● | ref | ref |
| **How to transfer data** | **Field §25** | — | ref | ● | ref |
| **Non-conformance and re-collection** | **SOP §21** | — | ● | ref | ref |

## Registers and control

| Topic | Owner | Manual | SOP | Field | Office |
|---|---|---|---|---|---|
| **Master register** | **`_control/master-register.csv`** | view | view | marker | marker |
| Decision view | SOP App. A | ref | ● | ref | ref |
| Test and vendor view | Manual App. E | ● | ref | ref | ref |
| Test results | Manual App. F | ● | ref | — | ref |
| **Warning register** | **`_control/warning-register.md`** | ● source | quote | quote | quote |
| **Stage names** | **`_control/workflow-stage-names.md`** | use | use | use | use |
| Trimble source index | Manual App. A | ● | ref | — | ref |
| Reference dataset (402 records) | Manual App. B | ● | ref | ref | ref |
| Figures and screenshots | Manual App. C | ● | ref | ref | ref |
| Field checklists | Field App. A–B | — | ref | ● | — |
| Office checklists | Office App. A–E | — | ref | — | ● |

---

## How to use this when something changes

| If this changes… | Review |
|---|---|
| A **Trimble behaviour** | The owning Manual section, then every document marked `ref` on that row |
| A **Parametrix decision** | The SOP clause, then every `ref` — and regenerate the register views |
| A **test result** | Manual App. E → F, the owning Manual section, then the SOP clause it gated |
| A **TBC version** | Manual App. A first, then any row whose evidence cites a changed topic |
| A **warning's wording** | The warning register, then every document under *Quoted in* |
| A **stage name** | `workflow-stage-names.md`, then all four documents, checklists and forms |

> **A change that touches no row in this matrix is a change to something nobody owns.** That is
> worth noticing.
