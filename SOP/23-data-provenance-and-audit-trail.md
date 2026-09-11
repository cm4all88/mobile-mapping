# 23. Data Provenance and Audit Trail

## 23.1 The question this section answers

> *A client, a reviewer, or opposing counsel is looking at a point cloud Parametrix delivered
> three years ago. They ask: how do we know this is the adjusted version, and which adjustment
> was it?*

That question is ordinary in survey work. A conventional adjustment produces a report naming its
observations, its constraints and its residuals, and the report travels with the deliverable.
Mobile mapping does not work that way, and this section sets out precisely what can and cannot be
demonstrated.

## 23.2 Four things that are related and not interchangeable

Conflating these is the most common error in discussing mobile mapping provenance, and it leads
people to believe a question has been answered when it has not.

| | What it establishes | What it does **not** establish |
|---|---|---|
| **Spatial reference metadata** | Which coordinate system and scale the coordinates belong to | Which trajectory produced them |
| **Trajectory information** | The sensor path through space and time | Which *version* of that path this is |
| **Registration history** | What adjustments were applied after the original trajectory solution | — |
| **Data provenance** | Where the data came from and how it was processed, end to end | — |

Stated as plainly as possible:

> **A coordinate system does not prove which trajectory produced the points.**
>
> **GPS Time does not prove which registration was applied.**
>
> **Trajectory geometry without trajectory identity does not necessarily reconstruct the
> processing lineage.**

That last one deserves a sentence of its own, because it is the subtlest. The TMX export and
Publish to TRCPS both carry **trajectory geometry** out of TBC (§22). A recipient therefore holds
a path through space. What they do not hold is a statement of **which** path it is — the imported
one, the first registration, or the fourth — and on a project where several existed, geometry
alone may not distinguish them, particularly where a registration made a small correction.

## 23.3 The provenance chain

Each transition, with what exists at that point, what Cleanup can remove, and what survives
export.

### Legend

**In TBC** = a project object · **On disk** = a file in the project or raw data folder ·
**Cleanup** = may be removed by §21 · **Export** = documented as surviving export

---

### 1 · Raw MX60 mission → imported mission

| | |
|---|---|
| **In TBC** | Mission node; runs; Capture Devices; start/stop, duration, **covered distance**, active trajectory file *(TBC 22499)* |
| **On disk** | The `.mxdb`, raw POS data, raw scanner and camera data, `Extcal.json`, mission logs *(TBC 25943)* |
| **Cleanup** | The raw data is outside the project and unaffected |
| **Export** | Not applicable |
| **Parametrix record** | **The field record** — conditions, incidents, what was not collected. No software artefact exists (§9) |

### 2 · Imported mission → trajectory

| | |
|---|---|
| **In TBC** | The trajectory node under each run; RMS colouring from `smrmsg_xxx.out` *(TBC 27248)* |
| **On disk** | `sbet_[mission].out` **or** `sbet_[mission]_[frame].out` in `NAVPROC/Export/`; the processing report in `NAVPROC/Report/`; with **Backup SBET Next to MXDB**, a copy **and a log of the frame and epoch used** beside the `.mxdb` *(TBC 25943)* |
| **Cleanup** | Keeps the trajectory "consistent with the latest version of navigation and trajectory information file (SBET or NAV)" *(TBC 26466)* |
| **Export** | Trajectory **geometry** on TMX and TRCPS; **identity not documented** |
| **Parametrix record** | Which computation mode, which base station, which settings — **no single artefact captures these** (§12.3) |

> **The frame-and-epoch log written by Backup SBET Next to MXDB is the only artefact found in the
> whole workflow that records the frame a trajectory was computed in, and it lives with the raw
> data rather than inside the project.** That is why enabling the option is proposed in §12.4.

### 3 · Trajectory → generated scans

| | |
|---|---|
| **In TBC** | Scan nodes **nested beneath the trajectory that produced them** *(TBC 22638)*; the **Results of Scan Generation** dialog recording filters, range and colorization per run *(TBC 22499)* |
| **On disk** | RWCX point cloud data in the project |
| **Cleanup** | Scans associated with removed registrations are removed *(TBC 26466)* |
| **Export** | The cloud itself. **Filter and colorization settings are not documented as travelling** |
| **Parametrix record** | **Capture the Results of Scan Generation** — proposed §13.5 |

### 4 · Calibration state

| | |
|---|---|
| **In TBC** | Camera and sensor properties: **Boresight installation** vs **Boresight refinement**, lever arm installation vs refinement *(TBC 24868)* |
| **On disk** | `Extcal.json` with the raw data; an exported calibration JSON containing the **Installation Matrix** and **Refinement Matrix** for each sensor *(TBC 22920)* |
| **Cleanup** | Not addressed by Trimble's description |
| **Export** | **Not documented as travelling with any deliverable** |
| **Parametrix record** | The **Mission Report** carries per-sensor boresight and lever-arm calibration **with a date of calibration** *(TBC 24868)* — the only dated calibration record found |

### 5 · Registration → adjusted trajectory

| | |
|---|---|
| **In TBC** | The adjusted trajectory node with properties **`Origin: Registration result`**, **`Input trajectory`**, **`Registration type`** *(TBC 22905, 26473)*; picked and updated targets named for the registration; registered segments rendered in the **"Undefined RMS"** colour *(TBC 27248)* |
| **On disk** | **`sbet_<date>_reg_####.out`**, incrementing per registration, in the project folder *(TBC 22905)*; **`Targets.csv`** holding the picked targets, when Registration Auto-Saving is on *(TBC 22905)* |
| **Cleanup** | **Keeps only the most recent registration.** Earlier trajectories and their scans are removed. **Whether the numbered SBET files are deleted from disk is untested — T28** |
| **Export** | **No export path is documented as identifying the registration result** (§22.7) |
| **Parametrix record** | **Which points were control and which were checks, and the residuals on each** — TBC is not documented as reporting this after the fact (§17.6) |

### 6 · Update Scans → final point cloud state

| | |
|---|---|
| **In TBC** | New scan nodes beneath the adjusted trajectory; stations carrying a **`_reg_####`** suffix *(TBC 22638)* |
| **On disk** | RWCX data in the project |
| **Cleanup** | Scans of removed registrations are removed |
| **Export** | The cloud. **The `_reg_####` suffix is a station name inside TBC and is not documented as appearing in exported filenames** |
| **Parametrix record** | Confirmation that Update Scans was performed before export (§22.2) |

### 7 · Export → delivered dataset

| | |
|---|---|
| **Travels** | Coordinate system and scale factor (`.txt`, grid); project global CRS (ECEF); GPS Time per point; image position and orientation in some paths; image EXIF naming TBC; **trajectory geometry on TMX and TRCPS** |
| **Not documented as travelling** | Trajectory name or ID; SBET filename; registration result; registration type; `_reg_####` sequence; source run or mission identifier within the data; calibration identity |
| **Cleanup** | Not applicable — but what Cleanup removed is no longer available to be recorded |
| **Parametrix record** | **The delivery record** — what was exported, from which node, on what date, by whom |

---

## 23.4 The limitation, stated precisely

> **IMPORTANT PROVENANCE LIMITATION**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**

### What this does and does not mean

| It does **not** mean | It **does** mean |
|---|---|
| That exports carry no metadata | That the metadata they carry answers *where are these coordinates*, not *how were they produced* |
| That the trajectory never leaves TBC | That where it does leave (TMX, TRCPS), **which** trajectory it is is not documented |
| That provenance is impossible | That it depends on the TBC project and on Parametrix's own records, not on the deliverable |
| That Trimble's software lacks the information | That **Trimble's documentation does not establish it**, and does not enumerate LAS headers or VLR content — so something undocumented may be written (T22) |

> **The practical concern is therefore not "no history."** It is:
>
> **The deliverable may not contain enough documented provenance to reconstruct its processing
> history independently of the TBC project and Parametrix records.**

### Classification

> **PARTLY CONFIRMED.**
>
> **This no longer represents missing documentation.** All known MX60 export and publish paths
> have been reviewed (§22.6). The remaining uncertainty is about **software behaviour Trimble does
> not document**, resolvable by test (T18–T23), not by further reading.

## 23.5 Cleanup and provenance, combined

> Cleanup reduces the registration history available in the project.
>
> Export is not documented as providing unique registration lineage.
>
> **Therefore performing Cleanup before preserving the appropriate project evidence may reduce
> Parametrix's ability to reconstruct the processing history later.**

That is a finding, not a prohibition.

> **PARAMETRIX DECISION REQUIRED**
>
> This is precisely why the Cleanup policy (§21.4) remains open. **This document does not prohibit
> Cleanup and does not require it.** The combined finding above is the reason the decision matters
> more than it appears to, and it is the input Parametrix needs in order to make it.
> *(Register item 35)*

### T28 — why it is high priority here

> **FIELD TESTING REQUIRED · T28 — high priority**
>
> **Does Cleanup delete the `sbet_*_reg_####.out` files physically from storage, or only remove
> the corresponding project objects and references?**
>
> **Until tested, distinguish two things and do not assume one implies the other:**
>
> | **Project object retention** | **Underlying file retention** |
> |---|---|
> | Whether the trajectory node still appears in Project Explorer | Whether the `.out` file still exists in the project folder |
>
> The registered SBETs are written to the project folder on disk, not inside the TBC database
> *(TBC 22905, 26473)*. Removing a project object does not necessarily delete the file it points
> at, and Trimble does not address this.
>
> **The result materially changes what must be archived before Cleanup.** If the files survive,
> they are a partial lineage record that outlives the operation. If they do not, that record must
> be copied out beforehand or it is gone. *(Appendix E; §21.6, §25)*

## 23.6 What Parametrix would need to record

Stated as a gap analysis, not as policy.

> **PARAMETRIX DECISION REQUIRED**
>
> **What provenance record must accompany a mobile mapping deliverable, and where does it live?**
>
> Six facts cannot be reconstructed from the deliverable on current evidence. Each is cheap to
> record at the time and effectively unrecoverable later:
>
> | Fact | Why it is not in the deliverable |
> |---|---|
> | Which trajectory the delivered cloud was built on | §23.4 |
> | Which registration was applied, and which of several | §23.4 |
> | Which points were control and which were independent checks | TBC not documented as reporting it (§17.6) |
> | The residuals on each | Live in a dialog; the report question is open (§17.6) |
> | The calibration state at processing | In the Mission Report, if run (§14.6) |
> | Whether Cleanup was run, and what was archived first | No artefact (§21) |
>
> **This document does not establish a recordkeeping policy.** It establishes that without one,
> the six facts above are lost. *(Register item 29)*

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Not adopted.** A minimal record that would close the gap, offered for decision:
>
> - **A one-page delivery record** per dataset: mission ID, trajectory node name, SBET filename
>   including its `_reg_####` number, registration type, export path and date, exported by whom
> - **The Mission Report**, run before Cleanup (§21.6)
> - **The control/check table** — point ID, Use XY, Use Z, As Check, residual (§17.6)
> - **The calibration JSON** in force (§14.5)
> - **`Targets.csv`** (§21.6)
>
> Five artefacts, four of them small files that already exist. *(Register item 29)*

## 23.7 Reconstruction paths that do exist

Where a delivered dataset must be tied back after the fact, two routes exist on current evidence.
**Both are reconstruction, not provenance, and both depend on Parametrix having retained
something.**

**Timestamp matching.** LAS point records carry GPS Time *(TBC 23339, 22501)*, and a retained SBET
is a time series. A point's timestamp can be matched to an epoch in a specific SBET. This
identifies *a* trajectory only if the candidate SBETs differ measurably at that epoch, and it
requires the SBETs to have been kept.

**Trajectory geometry comparison.** A TMX or TRCPS delivery contains trajectory geometry
(§22.6.2, §22.6.6), which could be compared against retained `sbet_*_reg_####.out` files. Same
caveat: it requires retention, and it distinguishes candidates only where they differ.

> **FIELD TESTING REQUIRED · T30** — establish whether either reconstruction path works in
> practice on a real dataset with two candidate trajectories. Neither has been attempted.
> *(Appendix E)*

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We traced the data from the raw mission to the delivered file and asked, at
> every step, what record exists of what was done — inside TBC, on disk, and in the file the client
> receives.
>
> **Why it matters.** In conventional survey work, an adjustment comes with a report. It names the
> observations, the constraints and the residuals, and it goes out with the job. If somebody
> queries the result in five years, you open the report. Mobile mapping does not produce that
> document. The evidence exists — it is genuinely good inside the TBC project — but it is spread
> across node names, file suffixes, a dialog and a colour, and the documentation does not establish
> that any of it reaches the delivered file.
>
> **What can go wrong.** Be careful about what the problem actually is, because it is easy to
> overstate. The exported file is not empty of information: it knows its coordinate system, it may
> carry a scale factor sidecar, its points may be timestamped, and on two of the six paths the
> trajectory itself travels with it. What it does not do, as far as Trimble's documentation
> establishes, is say *which* trajectory — the original, or the first registration, or the fourth.
> So a delivered cloud can tell you where its coordinates belong and not how they were arrived at.
>
> The practical failure is a client query three years on, a project file that was cleaned up, and a
> processor who has left. The data is fine. Nobody can demonstrate that it is fine.
>
> **What good looks like.** The deliverable is not the record — the project and a short written
> note are. A page per dataset naming the trajectory, the registration and its number, which points
> were control and which were checks, what the residuals were, and what was archived before the
> project was tidied up. Five minutes at the end of a job, and the difference between "we are
> confident in it" and "here is why."
