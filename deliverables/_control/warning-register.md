# Warning register

**Authoritative wording for every warning that appears in more than one document.**

A warning in the register is **quoted verbatim** wherever it appears. It is never paraphrased,
never shortened, never "adapted for the audience." If the wording is wrong, it is fixed here and
then everywhere.

## What qualifies as a warning

> **Warnings must mean something.** An ordinary note is not a warning.

A **CAUTION** is justified only where the consequence is one of:

| Consequence | |
|---|---|
| **Data loss** | Irrecoverable, or recoverable only by re-collection |
| **Irreversible operation** | Cannot be undone within the software |
| **Loss of registration history** | Evidence of how a result was produced is destroyed |
| **Overwriting or replacing a result** | A good result is silently replaced by a worse one |
| **Incorrect coordinate or reference system** | Everything downstream is wrong and looks right |
| **Requires re-collection or reprocessing** | Costs a mobilisation or a processing run |
| **Safety** | Injury or equipment damage |

An **IMPORTANT** marks something that gets the job wrong if ignored but does not meet the above.

Everything else is body text.

---

## The register

Eleven warnings. **W-01 to W-05 are the protected set** — data loss, irreversibility, lost
history, silent replacement, wrong reference frame.

---

### W-01 · Cleanup is destructive and cannot be undone

**Owner:** Technical Manual §28 · **Quoted in:** SOP §17 · Office How To §29 · Checklists

> **CAUTION**
>
> **Cleanup Mobile Mapping Mission is destructive and cannot be undone.**
>
> It permanently removes registrations, trajectories and scan sets from the project, keeping only
> the most recent. Trimble states: *"Please, have a backup copy of your project prior performing
> the operation, it cannot be undone."* *(TBC 26466)*

**Consequence class:** irreversible · loss of registration history
**Evidence:** TBC 26466 · **Related:** D-35, T28

---

### W-02 · Registration does not reach the point cloud until Update Scans is run

**Owner:** Technical Manual §19 · **Quoted in:** SOP §13, §18 · Office How To §21, §31 · Checklists

> **CAUTION**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

**Consequence class:** overwriting or replacing a result · requires reprocessing
**Evidence:** TBC 22638 · **Related:** D-36

---

### W-03 · Export timestamps may substitute reprocessed data

**Owner:** Technical Manual §29 · **Quoted in:** SOP §18 · Office How To §30–31

> **CAUTION**
>
> With **Export timestamps** set to **Yes**, Trimble states that *"the exported scans are
> **reprocessed from the raw data**"* rather than being the scans processed with Generate Scans
> *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated.** Until this is established, the
> exported data may not be the data that was registered and checked.

**Consequence class:** overwriting or replacing a result
**Evidence:** TBC 23339, 22501 · **Related:** T18, V-1, D-36

---

### W-04 · Do not clear a data disk until the copy is verified

**Owner:** Technical Manual §5 *(data chain)* · **Quoted in:** SOP §11 · Field How To §25 · Office How To §2

> **CAUTION**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

**Consequence class:** data loss · requires re-collection
**Evidence:** MX60 UG Rev B p.10 · **Related:** D-52

---

### W-05 · Set the project coordinate system before importing

**Owner:** Technical Manual §12 · **Quoted in:** SOP §6, §12 · Office How To §5

> **CAUTION**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

**Consequence class:** incorrect coordinate or reference system · requires reprocessing
**Evidence:** TBC 24886, 24460 · **Related:** D-21

---

### W-06 · Targets.csv is emptied permanently by declining the reload prompt

**Owner:** Technical Manual §21 · **Quoted in:** SOP §13 · Office How To §16

> **CAUTION**
>
> If Registration Auto-Saving is on, picked targets are written to **`Targets.csv`**. Reopening
> the command prompts to reload them, and *"if you choose 'No', they will be emptied from the
> Targets.csv file and you will not be able to retrieve them"* *(TBC 22905)*.
>
> `Targets.csv` holds the registration's observations. **Answering "No" discards the field book.**

**Consequence class:** data loss · loss of registration history
**Evidence:** TBC 22905 · **Related:** T7

---

### W-07 · Registering again stacks adjustments — use Edit

**Owner:** Technical Manual §21 · **Quoted in:** SOP §13 · Office How To §19

> **CAUTION**
>
> **Getting this wrong stacks adjustments on adjustments.** A processor who registers, dislikes
> the residuals, and registers again has applied a second correction on top of the first. The
> residuals will look better. The trajectory has been bent twice against the same control.
>
> **To improve a registration, use Edit.** To start over, edit and Reset.

**Consequence class:** overwriting or replacing a result
**Evidence:** TBC 22905, 25362, 26578

---

### W-08 · Local registration does not extrapolate

**Owner:** Technical Manual §21 · **Quoted in:** SOP §7 · Office How To §16–17

> **CAUTION**
>
> **Local does not extrapolate.** Trimble states it is *"not for systematic error along the run or
> for adjusting outside the ground control points set"* *(TBC 22905)*.
>
> Beyond the first and last control point the trajectory is not adjusted, **and nothing indicates
> where the adjustment stopped.** Control must bracket the extent you intend to deliver.

**Consequence class:** overwriting or replacing a result · requires reprocessing
**Evidence:** TBC 22905 · **Related:** D-16, T15

---

### W-09 · The closing sequence cannot be added later

**Owner:** Technical Manual §14 · **Quoted in:** Field How To §21 · Checklists

> **CAUTION**
>
> The post-processed trajectory is computed **forward and backward** and merged. A degraded stretch
> mid-mission is bracketed by good data on both sides. **A degraded stretch at the end has good
> data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

**Consequence class:** requires re-collection
**Evidence:** MX60 QSG Rev B p.13 · **Related:** D-49

---

### W-10 · Missed overlap removes office remedies

**Owner:** Technical Manual §27 · **Quoted in:** SOP §8 · Field How To §23

> **CAUTION**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

**Consequence class:** requires re-collection
**Evidence:** TBC 25096, 28972 · **Related:** D-41, D-49

---

### W-11 · Battery Protect

**Owner:** Technical Manual §7 · **Quoted in:** Field How To §7 · Office How To *(not used)*

> **CAUTION**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*:
>
> | Event | Trigger |
> |---|---|
> | Audible warning | Supply below **10.5 V for longer than 12 seconds** |
> | Power cut | Supply below **10.5 V for more than 90 seconds** |
> | Recovery | Voltage rises above **12.0 V within that 90 seconds** |
>
> The alarm leaves roughly **78 seconds** to restore charge — that figure is the arithmetic of the
> two sourced timings, not a separately published one.
>
> An interrupted run loses the closing sequence with it.

**Consequence class:** data loss · requires re-collection
**Evidence:** MX60 UG Rev B p.27 · **Related:** W-09

---

## Deliberately *not* warnings

Recorded so they are not promoted by a later editor.

| Statement | Why it is not a warning |
|---|---|
| Good RMS does not prove success | A **principle**, stated as body text and as an evidence-tagged quotation. Making it a CAUTION would weaken the eleven above by inflation |
| Corrupted side camera images export as black | **IMPORTANT.** A silent defect, but it costs a re-export, not a re-collection |
| Checking Target-Bundle Adjustment makes the adjustment coarser | **IMPORTANT.** Counter-intuitive, not destructive |
| Ground scaling does not expose its scale factor | **IMPORTANT.** Recoverable by exporting to grid |
| The SBET `_frame` filename | A **note**. It is an indicator, not a failure |
| TBC 2026.10 requires two-step verification | A **note** |

---

## Verification

Before any issue, confirm each registered warning appears **verbatim** in every document listed
under *Quoted in*, and nowhere in a paraphrased form.

`tools/check-warnings.py` performs this check.
