# Source Inventory — Batch 3: chain model tested, registration gap identified

**Prepared:** 2026-09-11
**Status:** Ingestion continued. **No rewrite performed.**

---

## 0. No new documentation arrived with this instruction

The only upload in this session remains the batch 2 archive, already ingested. Nothing new
was attached, and the live help portal is unreachable from this environment (egress to
`help.fieldsystems.trimble.com` is blocked).

So this entry does two things that do not require new material:

1. **Tests the proposed processing chain** against everything ingested so far, and proposes
   corrections
2. **Identifies exactly which Trimble help topics answer the eight questions**, by reading
   the help portal's own navigation tree out of the batch 2 captures

The second is the more useful result.

---

## 1. THE GAP — the three topics you need were not in batch 2

The left-hand navigation of the captured pages enumerates the complete **Mobile Mapping**
topic tree. Batch 2 captured one branch of it almost completely, and none of the others.

| # | Top-level topic | Status |
|---|---|---|
| 1 | Understanding Mobile Mapping | ✅ have |
| 2 | Mobile Mapping System Data Structure | ✅ have |
| 3 | Mobile Mapping Options | ✅ have |
| 4 | Import, View and Process Mobile Mapping Data | ✅ have — 14 of its 15 sub-topics |
| 5 | **Register Mobile Mapping Trajectories** | ❌ **MISSING — the priority topic** |
| 6 | **Perform Mobile Mapping Calibrations** | ❌ **MISSING** |
| 7 | **Cleanup Mobile Mapping Mission** | ❌ **MISSING** |
| 8 | Export Mobile Mapping Data | ❌ missing |
| 9 | **Blur Exported Images** | ❌ missing — bears on SOP §13 imagery privacy |
| 10 | Run a Batch Command | ❌ missing |
| 11 | Create CAD Entities on Mobile Mapping Data | ❌ missing |
| 12 | **Create Orthomosaics from a Trimble Back-Camera Mobile Mapping System** | ❌ missing — MX60 has this camera |
| 13 | Import Ortho Lane Images | ❌ missing |
| 14 | Inspect Pavement Condition | ❌ missing |
| 15 | Import and Export Road Segments in AgileAssets | ❌ missing |
| 16 | Run a Boeing Bump Index (BBI) Report | ❌ missing |

Also missing from branch 4: **Display Mobile Mapping Run Views** (the 15th sub-topic).

> **Your eight questions are, almost without exception, answered by topics 5, 6 and 7 —
> none of which were captured.** Batch 2 documented everything *around* registration
> without documenting registration itself.

**Capture priority for the next batch**

| Priority | Topic | Answers |
|---|---|---|
| 1 | **Register Mobile Mapping Trajectories** (and all sub-topics) | Q1–Q6, Q8 |
| 2 | **Cleanup Mobile Mapping Mission** | validation and cleanup |
| 3 | **Perform Mobile Mapping Calibrations** | confirms/extends §12.3 |
| 4 | Export Mobile Mapping Data | proving what was delivered |
| 5 | Blur Exported Images | SOP §13 privacy decision |
| 6 | Create Orthomosaics from Back-Camera | MX60-specific capability |
| 7 | Display Mobile Mapping Run Views | completes branch 4 |

Expand each section in the help tree before capturing — topics 5, 6 and 7 are parents and
will have sub-topics that the collapsed nav does not show.

---

## 2. The proposed chain, tested

**Your model:**

```
Raw MX60 data → imported trajectory → initial scan generation
  → trajectory registration/adjustment → Update Scans using adjusted trajectory
  → QC → extraction/delivery
```

**Verdict: directionally correct, and it is the right spine for the guide.** Five
corrections are supported by evidence already ingested.

### Correction 1 — the imported trajectory is a decision, not an inheritance

At import, *"if there is an SBET file included in your data set, it is, by default, used
and its file path is displayed in the Refine trajectory list"* *(TBC 20736-1)*.

The default is adopted **silently**. Every downstream product inherits it. The chain should
show this as a checkpoint, not a passive step.

Trajectory can also be changed later, before generation, via mission properties →
**Active trajectory file** → *Select Trajectory* dialog *(TBC 22499)*.

### Correction 2 — calibration is a prerequisite loop, not a later stage

Boresight calibration **consumes generated scans** — *Calibrate Laser Scanners* requires
four runs of a crossroad that have been imported and processed *(TBC 20716)*. But its
result must be applied **before** production scans are generated, or every production cloud
carries the old boresight.

So calibration is a **separate, earlier mini-chain**:

```
calibration mission → import → generate scans → Calibrate Laser Scanners
  → visual check → Apply  ──► then production work begins
```

The main chain should show calibration as an input state, with an explicit "calibration in
force" that gets recorded per mission.

### Correction 3 — filters are locked at Generate; Update cannot change them

**Update Scans has no Filters pane** *(TBC 22638)*. Its panes are Runs / Scan Configuration
only.

Therefore the chain is not a one-way street. A wrong filter choice forces a return to
**Generate**, not Update:

```
              ┌──────────────── filter wrong? ────────────────┐
              ▼                                               │
  Generate Scans ──► registration ──► Update Scans ──► QC ────┘
                                          ▲
                       trajectory wrong? ─┘
```

**The distinction matters operationally:** a trajectory problem is cheap (Update); a filter
problem is expensive (regenerate from raw).

### Correction 4 — the chain is additive, not replacing

Registration does **not** overwrite the imported trajectory. After Update Scans, the project
holds:

```
Run
├── Sbet                          ← imported trajectory
│   ├── Scan Right (G1)           ← original scans
│   └── Scan Left  (G2)
└── Reg. Trajectory               ← adjusted trajectory
    ├── Scan Right (G5)           ← updated scans
    └── Scan Left  (G6)
```

*(TBC 22638)*

Both persist. **Nothing in the tree marks which one is the deliverable.** This is the single
largest defensibility hazard identified so far — see Q7.

### Correction 5 — QC is distributed, not terminal

There are at least four distinct QC moments, each with its own artifact:

| After | Check | Artifact |
|---|---|---|
| Calibration | Cutting Plane visual check | RMS + Overall Overlap *(TBC 20716)* |
| Scan generation | Settings actually applied | **Results of Scan Generation** dialog *(TBC 22499)* |
| Registration | *unknown* | *unknown — needs topic 5* |
| Update Scans | Correct trajectory used | *no known artifact — see Q7* |

### Proposed corrected chain

```
  ┌─ CALIBRATION (periodic) ────────────────────────────────┐
  │  calib mission → import → generate → calibrate → Apply  │
  └──────────────────────────┬──────────────────────────────┘
                             ▼  calibration in force
  raw .mxdb
      │
      ▼
  IMPORT ──────────────► trajectory selected  ◄── CHECKPOINT: is this the right SBET?
      │
      ▼
  GENERATE SCANS ──────► filters locked here  ◄── CHECKPOINT: Results dialog
      │                                            SAVE THE VCE PROJECT
      ▼
  REGISTER TRAJECTORY ─► creates Reg. Trajectory  [MECHANISM UNKNOWN]
      │                  (original retained)
      ▼
  UPDATE SCANS ────────► scans under Reg. Trajectory
      │                  (original scans retained)
      │                  SAVE THE VCE PROJECT
      ▼
  QC ──────────────────► against independent check points
      │
      ▼
  EXTRACTION / DELIVERY ◄── CHECKPOINT: which scan set is being delivered?
```

---

## 3. The eight questions — what is answered, what is not

> **Verified Trimble behaviour** is marked ✅. **Inference** is marked ⚠ and is not fact.
> **Unknown** is marked ❌ and must not be filled in from assumption.

### Q1 — How is an adjusted or Registration Trajectory created?

❌ **Unknown.** No captured topic documents the registration command.

⚠ **Inferred, for testing only:**
- The output node is named **"Reg. Trajectory"** and sits as a sibling of `Sbet` under the
  Run ✅ *(TBC 22638)*
- Updated scans carry a **`_reg_####`** suffix — e.g. `Run_14_Laser Right_reg_0001 (S3)` ✅
  *(TBC 22638)*, implying registrations are **numbered and repeatable**, so multiple
  registration versions of one run can coexist
- TBC registers *"mobile mapping runs to fixed control points"* using the **smart picking
  tool** and the **integrated POSPac PFix engine**, and can **batch register** several runs
  *(TBC Technical Notes 2022, p.4)* — but that document predates MX60 support

**Needs:** topic 5.

### Q2 — What observations or control can constrain it?

⚠ **Partially inferred.** The strongest evidence is an options entry, not a registration
topic:

> **Registration auto-saving** — *"Allow to automatically save the **targets that have been
> picked** during a **run** or **mission** registration, ensuring that they are not lost and
> can be easily retrieved later."* ✅ *(TBC 21243-1)*

Three things follow:

1. Registration observations are **picked targets** — a manual, operator-driven act
2. There are **two scopes**: **run registration** and **mission registration**
3. Picked targets are **losable** unless this option is enabled

> **Flag for testing, not procedure:** whether "targets" means surveyed control points,
> cloud-to-cloud tie points, or both, is **not established**. Do not write either into the
> guide.

**Needs:** topic 5.

### Q3 — What quality indicators does TBC provide?

❌ **Unknown for registration.**

✅ **Known for calibration** *(TBC 20716)* — and worth noting because the eventual
registration report may follow the same pattern:
- Overall Overlap (% of points used vs. generated)
- Overall RMS (average of RMS between used scans)
- Per-pair RMS in **Tangential, Orthogonal, Vertical**

✅ **Known for scan generation** *(TBC 22499)* — the Results dialog records filters, range
and colorization per run.

**Needs:** topic 5.

### Q4 — Acceptable versus unacceptable result?

❌ **Unknown, and Trimble may not state it.**

✅ What Trimble does state, for calibration, is a **rule about the logic of the test**
rather than a threshold:

> *"Good RMS values do not mean that the calibration succeeded. A visual check is needed.
> On the other side, bad RMS values mean that the calibration failed."* *(TBC 20716)*

> **Carry this asymmetry forward as a working hypothesis for registration:** numeric
> indicators may be able to prove failure without proving success. If topic 5 repeats this
> pattern, any Parametrix acceptance rule must pair a numeric threshold with a mandatory
> visual check — a number alone would not be defensible.

**Parametrix tolerances remain undefined and unproposed.** SOP §13 already records that no
source in the set provides them.

### Q5 — Does registration change the trajectory only, or other mission objects?

✅ **Partially answered — and the answer is "trajectory only, until you act."**

Registration produces a **new trajectory node**; the existing scans are **not** altered.
Scans change only when **Update Scans** is run *(TBC 22638)*. That is precisely why Update
Scans exists as a separate command.

❌ **Unknown:** whether registration also touches station positions, camera positions or
imagery georeferencing. Imagery is positioned from the trajectory, so it is plausible that
station imagery inherits the adjustment — **but this is not documented and must not be
assumed.**

> **Flag for testing:** after a registration, compare a station's panoramic position before
> and after. This is a question Parametrix can answer empirically without Trimble.

### Q6 — Exactly when is Update Scans required after registration?

✅ **Answered by structure.** Update Scans is required **whenever the registered trajectory
must be reflected in the point cloud** — which is every time a registration is intended to
improve a deliverable.

Without it, the registration exists only as a trajectory node and **the delivered cloud
still sits on the imported trajectory**.

✅ **Also required** when switching *back* — the dialog switches *between* the imported and
adjusted trajectory *(TBC 22638)*, so it is the mechanism in both directions.

⚠ **Not required** for anything that reads the trajectory directly rather than the cloud.
Which operations those are is **not established**.

### Q7 — How can the processor prove final scans use the intended trajectory?

**This is the weakest point in the entire documented workflow, and it deserves its own
Parametrix control.**

✅ What the software gives you:
- Scans sit **beneath their trajectory node** in Project Explorer — scans under
  `Reg. Trajectory` were computed against it *(TBC 22638)*
- Updated stations carry the **`_reg_####`** suffix *(TBC 22638)*
- **Mission Report** reports *"capture devices, runs, trajectories and generated scans"*
  *(TBC 23991)*

❌ What is not established:
- Whether any **export** carries the trajectory identity with it
- Whether the **Mission Report** explicitly states which trajectory each scan used
- Whether there is any **scan-level property** naming its source trajectory

> **This is the proof gap.** Tree position and a filename suffix are the only evidence
> found so far, and neither survives export.

> **PROPOSED PARAMETRIX PRACTICE — not Trimble behaviour, not adopted:**
> Before extraction or export, record in the project file (a) which trajectory node the
> delivered scans sit beneath, (b) the `_reg_` version number, (c) a Mission Report run
> after the final Update Scans. Consider deleting or clearly renaming superseded scan sets
> so the wrong one cannot be exported by accident. **This needs testing against topic 5 and
> the Export topic before it becomes procedure.**

### Q8 — What reports or records should be retained?

✅ **Available and verified today:**

| Record | Source | Captures |
|---|---|---|
| **Mission Report** | TBC 23991 | Capture devices, runs, trajectories, generated scans |
| **Results of Scan Generation** | TBC 22499 | Per run: filters, range, colorization on/off |
| **Calibration results** | TBC 20716 | Computed angles, Overall Overlap, Overall RMS, per-pair RMS |
| Mission properties | TBC 22499 | Start/stop, duration, **covered distance**, active trajectory file |

❌ **Not established:** whether a registration report exists at all.

> **FLAGGED, not adopted.** SOP §E1 already flags Mission Report as a candidate Parametrix
> QC requirement. The natural package — Mission Report + Results of Scan Generation +
> calibration record + trajectory identity — is a **proposal for testing**, not policy.

---

## 4. Defaults and filters flagged for testing, not adoption

Per instruction, none of these is converted into procedure.

| # | Item | Why it needs testing before adoption |
|---|---|---|
| T1 | **Default vs High Quality** filter preset | Trimble states contents, never selection criteria. High Quality enables Fog, Sun and Reflective Panels unconditionally |
| T2 | **Isolated Points default state** | Trimble's own text contradicts itself — prose says On, Restore Default Values says Off *(TBC 22499)* |
| T3 | **Reflective Panels filter** | *"Removes the noise before and after a target."* Does it also remove legitimate retro-reflective returns from signs and line marking? Directly affects asset extraction and retroreflectivity work |
| T4 | **Range Max 150 m (MX60 default)** | Matches the scanner's 150 m maximum at the lower rate, but the MX60 UG warns real-world range is shorter in bright sunlight and at oblique incidence. Points may be retained beyond useful range |
| T5 | **Fog / Sun filters** | Both remove real returns under defined conditions. Applying them when conditions did not occur may remove valid data |
| T6 | **Colouriser settings** — forward vs backward preference | No selection rule given |
| T7 | **Registration auto-saving** | Appears to default off. Given picked targets are the registration observations, losing them may mean redoing the registration |
| T8 | **Show scans after generation** | Cosmetic, but its default explains the common "my scans did not appear" report |

> **A general caution for the guide:** every filter in the Generate Scans dialog **removes
> points permanently from the generated cloud**. There is no post-hoc "unfilter" — recovery
> requires regenerating from raw. For survey-grade work the conservative default is to
> filter as little as the conditions require, not as much as the preset allows. **This is a
> proposed Parametrix position, not Trimble guidance.**

---

## 5. Register of new open questions

Added to the seven in batch 2:

| # | Question | Resolved by |
|---|---|---|
| 8 | How is a Registration Trajectory created, and what commands invoke it? | Topic 5 |
| 9 | What are registration "targets" — surveyed control, cloud tie points, or both? | Topic 5 |
| 10 | What is the difference between **run** registration and **mission** registration? | Topic 5 |
| 11 | Does a registration report exist, and what does it contain? | Topic 5 |
| 12 | Does registration move station and imagery positions, or only the trajectory? | Topic 5 + empirical test |
| 13 | Can multiple registration versions coexist, and how is the active one chosen? | Topic 5 |
| 14 | What does **Cleanup Mobile Mapping Mission** remove, and is it reversible? | Topic 7 |
| 15 | Does export carry trajectory identity? | Export topic |
| 16 | Does **Blur Exported Images** satisfy the SOP §13 privacy requirement? | Blur topic |

---

## 6. Figures to add to the batch 2 list

Extending §H of the batch 2 inventory:

| # | Source | Crop | Demonstrates |
|---|---|---|---|
| F17 | 22499 nav sidebar | The full Mobile Mapping topic tree | The scope of TBC mobile mapping functionality — useful orientation early in the guide |

And, once topics 5–7 are captured, the figures most likely to be needed are the registration
dialog, its observation list, its residual output, and the Cleanup dialog. **Do not crop
these blind — identify them from the captures.**

---

*No SOP section has been rewritten. Section 12 still reflects the earlier source set. This
document extends `SOURCE-INVENTORY-TBC-BATCH-2.md` and is input for the eventual
restructure.*
