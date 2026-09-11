# APPENDIX D — PARAMETRIX DECISION REGISTER

Every **PARAMETRIX DECISION REQUIRED** item in this SOP, consolidated.

> **IMPORTANT**
>
> Nothing in this register is current Parametrix policy. Each row is an open question with
> a recommended answer. The recommendations are drawn from Trimble documentation, the
> Queensland TMR guideline, and NCHRP practice — they are **not** Parametrix standards
> until formally adopted.

**35 items.** Priority reflects what blocks first use of the system, not importance in the
abstract.

| Priority | Meaning |
|---|---|
| **P1** | Blocks first production collection |
| **P2** | Needed before delivering to a client |
| **P3** | Needed for a mature, repeatable programme |

---

## P1 — Blocks first production use

| # | § | Decision | Recommended |
|---|---|---|---|
| 1 | 1 | **Which MX60 configuration** — Core, Pro or Premium? Record serial number and accessories | Record in §1 and repeat on the field checklist. It sets imagery resolution, attitude accuracy and every spec table row |
| 2 | 1, 3 | **Are GAMS and DMI owned and fitted?** | Fit both. GAMS removes an initialization step the operator can get wrong; DMI protects the trajectory where mobile mapping is weakest |
| 3 | 1 | **Which mounting rack** — MX SCAN Roof Rack or MX Shock Absorbing? | Record it. Determines install procedure, and the published GAMS corner offsets apply to the standard rack **only** |
| 4 | 1 | **What does "trained" mean?** Required training, sign-off, supervised experience | Complete the Appendix E exercise, participate in one supervised production collection, sign-off by an experienced operator. Maintain a qualified-operator list |
| 5 | 6 | **Who measures lever arms**, by what method, recorded where, re-verified when | Trained-personnel task with a written record: date, who, method, values, vehicle condition. Re-verify after any disturbance to Sensor Unit, GAMS, DMI or rack |
| 6 | 6 | **Field protocol form** — Trimble requires order of runs, direction, date, mission, system S/N | One page capturing Trimble's fields plus operator, vehicle, weather, install height, preset names, initialization times and locations, and events |
| 7 | 7 | **Is recording at orange NAV ever permitted?** | Prohibit for survey-grade. Permit for asset-grade only with the project surveyor's approval, recorded in the field protocol |
| 8 | 9 | **Standard collection speed** and conditions for reducing it | At or near prevailing traffic up to 80 km/h. Reduce for high-detail extraction, dust, or density needs. Never exceed 80 km/h operating |
| 9 | 11 | **Backup standard** — copies, media, locations, retention | Three copies, two media types, one off-site. Raw data retained for project life plus records retention |
| 10 | 11 | **Raw data storage location and folder structure** | One project folder: `01-raw` (read-only once verified), `02-trajectory`, `03-pointcloud`, `04-imagery`, `05-control`, `06-qc`, `07-deliverables`, `08-field-records` |
| 11 | 11 | **Project and mission naming convention** | Keep TMI's automatic directory naming; carry the Parametrix project number in the mission name field, so it lands inside the mission database |

---

## P2 — Before client delivery

| # | § | Decision | Recommended |
|---|---|---|---|
| 12 | 5 | **Minimum pass count**, and who may authorise fewer | Three passes for survey-grade. TMR permits fewer only by agreement and warns against it. Written approval from the project surveyor, recorded in the survey report |
| 13 | 5 | **Control standard** — base strategy, max baseline, control spacing, check point density | Own base on project control, short baselines. Control at both project ends and at significant intersections. Check points in **both good and poor GNSS environments** |
| 14 | 5 | **Wet-weather rule.** Trimble says avoid rain and mist; TMR says no imagery in wet; neither defines "wet" | No collection during active precipitation. After rain, wait until pavement is visibly dry. Operator has explicit authority to stand down without approval |
| 15 | 5 | **Traffic control** by roadway class, and go/no-go without it | None needed where the vehicle travels at or near prevailing speed in a normal lane. Required where collection speed is materially below traffic, or where a pass requires stopping, reversing or occupying a shoulder |
| 16 | 13 | **Numerical tolerances** for accept / review / recollect | **None are proposed** — the sources contain none. Adopt ASPRS 2014 or NSSDA, and TMR's four-way structure: horizontal and vertical, absolute and relative, relative within a 200 m sliding window |
| 17 | 13 | **Useful range statement** with every deliverable? | Yes, every project. A few lines in the survey report; prevents the most common and expensive client misunderstanding |
| 18 | 13 | **Imagery privacy** — blurring, access, delivery, retention, removal requests | Raw imagery internal and restricted. Blur faces and plates on anything delivered or published. Decide before the first project that publishes imagery |
| 19 | 13 | **Who authorises recollection**, and how remobilisation cost is handled | Project surveyor decides, project manager informed before mobilising. Record the cause — a pattern is a training or equipment signal |
| 20 | 5, 12 | **Boresight calibration policy** — frequency, who performs it, what triggers an unscheduled one, and how the calibration in force is recorded | Defined interval plus after any event that could disturb the sensor head or rack. Record calibration date and values in the field protocol. Establish a standard calibration site (§5.7). **Two answers needed first: which TBC version Parametrix runs, and whether daily Sensor Unit removal counts as "disturbed"** |
| 21 | — | **Document control** — owner, number, approval authority, review cycle, controlled copy | Owner in the survey technology group; approval by a licensed professional surveyor; annual review or on any new Trimble revision |

---

## P3 — Programme maturity

| # | § | Decision | Recommended |
|---|---|---|---|
| 22 | 3 | **Is the Sensor Unit removed and cased daily?** | Yes — follow Trimble's assumption. Protects an expensive item from weather, theft and clearance accidents. Note this means GAMS comes off too, so its lever arm is re-measured each morning |
| 23 | 5 | **Standard calibration site** — identify and record one meeting the §12.3 crossing requirements | Scout one near the office; document with an aerial image and the four run lines; note it in the field protocol whenever a calibration mission is driven |
| 24 | 5 | **Night collection** — when permitted, safety measures, client handling | Permit where imagery is not a deliverable and parked-vehicle occlusion would otherwise force recollection. Agree with the client in advance — imagery **will** be unusable |
| 25 | 6 | **How second-person torque verification is recorded** | Dated sign-off on the installation record naming both people. Repeat after any disassembly |
| 26 | 7 | **Factory user-accuracy defaults, or Parametrix values?** Who may change them | Use factory defaults. Restrict changes to named trained personnel; record any change in the field protocol — a mission on altered thresholds is not comparable to one on defaults |
| 27 | 7 | **Standard capture presets and naming** | Build named presets in advance — corridor, dust, urban — and export to file as a backup and for replication to a second system |
| 28 | 7 | **Rule for proceeding past a disk Warning or Error** | Never start a production mission on Error. Treat Warning as grounds for swapping the disk before a long collection |
| 29 | 8 | **Full manoeuvre sequence even with GAMS fitted?** | Perform it anyway. Costs minutes, matches the Quick Start checklist, and gives the office strong initialization at both ends regardless |
| 30 | 8 | **Re-initialization triggers** | After NAV degradation not recovered in a few minutes of open sky; after any outage materially longer than 60 s if critical data follows; whenever a mission has been closed. Record every initialization |
| 31 | 11 | **Retention and archive policy** — who may authorise deletion of raw data | Never deleted by the project team. Deletion requires survey technology group owner sign-off after the retention period |
| 32 | 11 | **Chain of custody** — when formal handling applies | Standard projects: field protocol and dated backups suffice. Litigation or forensic work: documented chain from the moment disks leave the vehicle, with checksums |
| 33 | 11 | **How many SSD sets in circulation** | At least one spare. A single set means the crew cannot mobilise until the previous offload verifies — which is exactly the pressure that causes someone to skip verification |
| 34 | 13 | **Periodic system verification** using Trimble's retro-reflective target check | Permanent target array at a Parametrix facility, surveyed conventionally. Quarterly, before major campaigns, and after any disturbance. Retain results as a trend |
| 35 | 14 | **Field escalation path**, and who may grant Trimble remote access | Operator contacts the survey technology group owner, who decides on Trimble contact. Remote access needs that owner's approval after confirming no client-confidential data is on the system |

---

## Blocked pending Trimble documentation

One item remains blocked. **Boresight calibration is no longer among them** — the procedure
is documented at §12.3, sourced from TBC Help.

| Blocker | Needed |
|---|---|
| Section 12 office procedure | Current TBC mobile mapping documentation covering import, trajectory processing, registration and export for the MX60. The supplied Technical Notes is October 2022 and predates MX60 support |


---

## How to use this register

1. Work P1 first — those eleven items block the first production collection
2. Assign an owner and a date to each
3. When adopted, replace the **PARAMETRIX DECISION REQUIRED** callout in the relevant
   section with the decided standard, and note the decision date
4. Keep this register as the record of what was decided and when

> **PARAMETRIX DECISION REQUIRED**
>
> Nominate an owner for this register and a target date for closing the P1 items.
>
> *Recommended practice:* the survey technology group owner named under item 21, with P1
> closed before the first production collection and P2 before the first client delivery.
