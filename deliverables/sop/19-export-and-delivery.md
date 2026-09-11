# 19. Export and Delivery Controls

## 19.1 The release gate

**Export is the last point at which a mistake is still internal.** This section is a gate, not a
procedure: the method is in the Office How To.

## 19.2 Before any export

> **PARAMETRIX PROCEDURE (PROPOSED) · D-36**
>
> **Before any export from a registered mission, confirm in Project Explorer that the scan nodes
> selected for export sit beneath the intended registered trajectory, and that their stations carry
> the `_reg_####` suffix.**

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **PARAMETRIX DECISION REQUIRED · D-36 · P1**
>
> **Is the pre-export trajectory-node confirmation mandatory, and may export be performed without
> it?** This is the single cheapest control in the procedure and the one that prevents the most
> expensive failure.

> **TESTING REQUIRED · T29, T23**
>
> The reliable export-state verification method for each export path, and what happens when a
> Point Cloud tab selection is drawn across scans belonging to two different trajectories. Neither
> is documented.

## 19.3 Export timestamps

> **CAUTION · W-03**
>
> With **Export timestamps** set to **Yes**, Trimble states that *"the exported scans are
> **reprocessed from the raw data**"* rather than being the scans processed with Generate Scans
> *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated.** Until this is established, the
> exported data may not be the data that was registered and checked.

> **TESTING REQUIRED · T18 · the highest-priority test in the register**
>
> Export the same registered run twice, timestamps off and on, and compare point geometry.
>
> **TESTING REQUIRED · T18 — and an interim posture until it is answered**
>
> **An export with timestamps enabled should be treated as unverified** against the checked
> dataset, and the option **should not** be enabled on a delivered dataset without a recorded
> reason.
>
> This is an interim posture, not a Parametrix rule and not a Trimble one. It exists because
> Trimble documents a behaviour whose consequence it does not state, and it is withdrawn the day
> T18 is answered — in either direction.

## 19.4 What the delivery carries

| | Requirement | State |
|---|---|---|
| Grid or ground, as agreed (§6.3) | A ground-scaled export **does not record the scale factor it used**; a grid export writes a sidecar | **D-38** |
| The coordinate reference system, datum and epoch | Stated in the delivery, not only in the file | **D-38** |
| The delivery record (§20) | | **D-29** |
| The accuracy statement (§17.6) | Where accuracy is relied on | **D-13** |

> **PARAMETRIX DECISION REQUIRED · D-38**
>
> **Deliverable specification** — standard formats, which export path produces each, and the
> default scaling.

## 19.5 Provenance limitation, stated plainly

> **IMPORTANT**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**
>
> That is why the delivery record in §20 exists, and why it is not optional.

> **TESTING REQUIRED · T19, T22, T26, T30**
>
> Which trajectory travels with a publish or an export; what a LAS file actually carries in its
> header, VLRs and sidecar; whether exported imagery reflects a registration; and whether a
> delivered dataset can be matched back to its trajectory after the fact.

## 19.6 Imagery

> **PARAMETRIX DECISION REQUIRED · D-32 · P1**
>
> **What is Parametrix's position on imagery privacy?** Are unblurred originals retained, and for
> how long? Mobile mapping imagery captures faces, number plates and private property as a matter
> of course. **The decision is made before collection, not on request.**

## 19.7 Records this section requires

| Record | State |
|---|---|
| Export-state confirmation, before export | **D-36** |
| The delivery record — §20 | **D-29** |
| What was delivered, to whom, when, in what format and scaling | **D-38** |


> **IN PLAIN LANGUAGE**
>
> **What this section means.** What has to be true before data leaves Parametrix, and what has to
> travel with it.
>
> **Why it matters.** An export is the point at which the data stops being ours and becomes something
> somebody else relies on. Once it is out, the receiving party has no way to tell which trajectory
> produced it, whether it was registered, or what accuracy it was checked to — unless we say so.
>
> **Remember this.** Confirm the cloud being exported is the registered one before exporting, not
> after. State the coordinate system, the epoch and the scaling explicitly rather than assuming the
> file carries them, and say what extent any accuracy statement applies to.
>
> **If this is skipped.** A file goes out that looks authoritative and cannot be traced back to how it
> was made. If it is later questioned, there is no record to answer with.
