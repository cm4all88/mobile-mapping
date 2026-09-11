# 29. Export — What Each Path Carries

## 29.1 Export is a QA/QC step, not a file conversion

By the time a processor reaches this section the analytical work is done. It is tempting to treat
what follows as mechanical.

It is not. Export is the last point at which the project and the deliverable can diverge, and
several documented ways exist for them to do so silently:

- The scans exported may not be the registered ones (§29.2)
- The scans exported may not be the scans TBC generated at all (§29.3)
- Coordinates may be grid or ground, and one of those does not tell you its own scale factor
  (§29.5)
- Imagery may be present and black (§26.4)
- A selection drawn in a view may span scans built on different trajectories (§29.4)

**Every one of those produces a file that opens correctly, looks right, and is wrong.**

## 29.2 QC CHECK — CONFIRM SCANS WERE UPDATED AFTER REGISTRATION BEFORE EXPORT

> **CAUTION · the most consequential check in this section**
>
> **Registration does not modify the point cloud until Update Scans is performed** (§19, §21).
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> **export point cloud data that still reflects the pre-registration trajectory.** The export
> succeeds. The file is valid. The data is unregistered.
>
> Nothing in the export dialog references the registration state.

### How to verify, using documented evidence

> **TRIMBLE DOCUMENTED METHOD**
>
> | Evidence | What it shows | Source |
> |---|---|---|
> | **Scans are nested beneath the trajectory they were computed from** in Project Explorer | Scans under `Reg. Trajectory` / `RegTrajectory` were computed against it; scans under `Sbet` were not | *(TBC 22638, 22905, 26473)* |
> | **Updated scan stations carry a `_reg_####` suffix** — e.g. `Run_14_Laser Right_reg_0001 (S3)` | That station was produced by Update Scans against a registered trajectory | *(TBC 22638)* |
> | **The adjusted trajectory's properties** — `Origin: Registration result`, `Input trajectory`, `Registration type` | Which trajectory is the registered one | *(TBC 22905, 26473)* |
> | **Registered segments render in the "Undefined RMS" colour** | Which stretches of trajectory an adjustment actually affected | *(TBC 27248)* |

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §19** (D-36); it is not decided here.

> **FIELD TESTING REQUIRED · T29**
>
> **Establish the reliable verification method for each export path.** Tree position and the
> station suffix are evidence *inside the project*. What is **not** established is how an export
> dialog resolves its selection — in particular:
>
> - Whether the **Mobile Mapping tab** exporters, which select by run, take the currently active
>   trajectory or a specific one
> - Whether the **Point Cloud tab** exporters, which select by region or by a rectangle drawn in a
>   view (§29.4), can be made to respect a trajectory at all
>
> Until tested, the only defensible verification is the project-side one above, performed
> immediately before export and recorded. *(Appendix E)*

## 29.3 Export timestamps — an unresolved question about what is exported

> **TRIMBLE DOCUMENTED METHOD**
>
> Stated in identical wording in two export topics *(TBC 23339, 22501)*:
>
> "If the TIMESTAMP option has been set to **No**, the exported scans are **the ones processed
> with the Generate Scans feature**, and the color information will be exported if the generated
> scans have been processed with the color option set to on.
>
> If the TIMESTAMP option has been set to **Yes**, the exported scans are **reprocessed from the
> raw data** and directly written to the LAS format files, the color information will be exported
> in the LAS format files."

> **VENDOR CLARIFICATION REQUIRED · V-1**
>
> **When Export timestamps causes TBC to reprocess from the raw source data, which trajectory is
> used for that reprocessing?**
>
> **The captured documentation does not establish this.** Trimble states that reprocessing occurs
> and does not state what it reprocesses against. Both readings — the mission's currently applied
> trajectory, or the originally imported one — are consistent with the wording.
>
> **No speculation is offered here.** *(Appendix E)*

> **FIELD TESTING REQUIRED · T18 — the highest-priority test in this document**
>
> Export the same registered run twice, once with timestamps off and once on, and compare the
> point geometry.
>
> **Why it is the highest priority:** every quality step in the workflow — registration, Update
> Scans, filtering, colorization — acts on the **generated** scans. If reprocessing does not
> reflect the registered trajectory, then a documented, innocuous-sounding export option can
> deliver data that was never the data that was checked. *(Appendix E)*

Until T18 and the vendor question are resolved:

> **Open Parametrix decision — D-36.** *May exports be made with Export timestamps enabled before this behaviour is established?* Stated and tracked in the **SOP §19**; see also the master register.

## 29.4 Two export tabs that behave differently

> **TRIMBLE DOCUMENTED METHOD**
>
> Mobile mapping exporters: **Home ▸ Data Exchange ▸ Export ▸ Mobile Mapping tab.** "A list of
> available exporters displays" *(TBC 23339, 23888, 22501)*.
>
> Generic point cloud exporters: **Home ▸ Data Exchange ▸ Export ▸ Point Cloud tab**
> *(TBC 11769)*.

| | **Mobile Mapping tab** | **Point Cloud tab** |
|---|---|---|
| Selection | **By run**, from Project Explorer or Plan View | **By point cloud region**, or a **Rectangle / Polygon Select** drawn in a graphic view |
| Run-aware | Yes | **No** |
| Imagery | Yes, per exporter | No |

> **IMPORTANT**
>
> **The Point Cloud tab exporters do not select by run or by trajectory.** Trimble's step is to
> "select the region(s) you want to export in the Project Explorer or graphic view", or draw a
> rectangle or polygon *(TBC 11769)*.
>
> ⚠ **OBSERVED SOFTWARE BEHAVIOR — assessment, flagged** · Nothing in the command ties the export
> to a trajectory. A rectangle drawn across a view could, in principle, span scans generated from
> different trajectories. **Whether TBC prevents, warns about, or silently permits this is not
> stated.**
>
> **FIELD TESTING REQUIRED · T23** — draw a selection across scans from two trajectories and
> observe. *(Appendix E)*

## 29.5 Coordinate handling — common to the point cloud exporters

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 11769, 27279)*
>
> Identical wording appears in both the generic exporter and the classified-regions exporter, so
> this is TBC's standard point-cloud export behaviour rather than a mobile mapping special case.

| Setting | Behaviour |
|---|---|
| **Scaling: Grid** | Points expressed in the current projected coordinate system, with the current combined scale factor. **"An associated .txt file is also created to specify the coordinate system and scale factor used."** Trimble warns: *"re-importing this file into TBC may cause some inconsistencies due to a double-scaling effect"* |
| **Scaling: Ground** | Points exported as ground coordinates "as they were measured in the field, independent of the coordinate system used", scaled from the 0,0 origin by the average combined scale factor. **"The scale factor is not exposed during export when this option is selected"** — recoverable only by exporting to grid and reading the `.txt` |
| **Applicability** | Selectable for e57, LAS, LAZ, POD, PTS, RCP. **TDX and PTX are always ground-based** |
| **ECEF export** | LAS or LAZ in ground-based scaling "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not carry a record of the scale factor it used.** For a surveyor
> this is a familiar grid-versus-ground question with an unfamiliar wrinkle: the file cannot tell
> the recipient which it is, and one of the two options actively withholds the number needed to
> convert.
>
> The grid-scaled `.txt` sidecar and the ECEF option are the two documented ways to make an
> exported cloud self-describing about its coordinate frame. **Neither says anything about the
> trajectory** (§30).

## 29.6 The MX60 export paths

Six documented paths. **No preference between them is expressed or implied here — the choice of
deliverable format is a project and client matter that Parametrix has not decided.**

> **Open Parametrix decision — D-38.** Stated and tracked in the **SOP §19**; see also the master register.

### 29.6.1 Export to LAS (Trajectory Split) — classified point cloud regions

*(TBC 27279)* · **Mobile Mapping tab**

**Prerequisite:** run **Extract Classified Point Cloud** in *Point Clouds ▸ Regions* first.

| | |
|---|---|
| **What leaves TBC** | Classified point cloud regions of one run, as LAS. "The classification code is added to the exported points" |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Grid or ground per §29.5; `.txt` sidecar on grid |
| **Timing** | LAS point records per §29.7 |
| **Imagery** | None |
| **Sidecars** | The scaling `.txt` |

**Settings** *(TBC 27279)*:

| Setting | Behaviour |
|---|---|
| **Splitting distance** | "a value in meter multiple of 250" |
| **Export both lasers in the same file** | Yes merges left and right. "You need to select at least one laser to export" |
| **Export laser left / right** | Independent Yes/No |
| **Split into files** | Splits the LAS per the Splitting Distance |
| **Sample points** | "random sampling be performed on the exported point cloud regions", with a target **Number of points** |
| **Format** | LAS **1.2 or 1.4** |
| **Export unit** | Unit of distance in the file |
| **Use inspection colors** | Exports Scan Inspection heat-map colours instead of true colour |

> **FIELD TESTING REQUIRED · T17**
>
> **Sample points performs *random* sampling to a fixed point count.** On a survey deliverable
> that is a destructive thinning with no documented spatial rule — no minimum spacing, no
> preservation of edges or breaklines. Its default state is not stated. *(Appendix E)*

> **Provenance implication:** the exporter is named *Trajectory Split*, and splits by distance
> along the trajectory. Despite the name, **no trajectory information is documented as
> accompanying the output.**

### 29.6.2 Export to TMX

*(TBC 22501)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds **and trajectory** |
| **Trajectory geometry** | **YES** — "The trajectory file is created **once for all devices**. It resides in a folder under the Mission folder" |
| **Specific trajectory identified** | **Not documented** |
| **Coordinate system** | Per §29.5. **"For the MX9 Export to TMX, the user must use a coordinate system without Geoid"** — *stated for the MX9 only; whether it applies to the MX60 is not stated* |
| **Timing** | Export timestamps option — **see §29.3** |
| **Imagery** | Panoramic (Pano), side (Sideview, Planar 1/2), back-facing (Planar 3); optional GPS attributes in the image files |
| **Sidecars** | `reference.csv` |

Output structure: a **Mission folder** plus one folder per device, with `laser`, `panorama`,
`planar*` and **`trajectory`** sub-folders. The MX60 example is illustrated in Trimble's topic.

> **Provenance implication:** this is one of two paths on which **trajectory geometry accompanies
> the deliverable.** A run carrying both an imported `Sbet` and a registered trajectory has two
> candidates, and **the topic does not state which is written.**
>
> **VENDOR CLARIFICATION REQUIRED · V-10** — which trajectory does the TMX export write when
> several exist under a run? *(Appendix E)* · **FIELD TESTING REQUIRED · T19** *(Appendix E)*

### 29.6.3 Export to TopoDot

*(TBC 23339)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images, side camera images, laser point clouds — as a *Raw Project Data* folder with *Image Project* and *LAS Files* sub-folders |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5 |
| **Timing** | Export timestamps option — **see §29.3** |
| **Imagery** | Cubical images from the panoramic and side cameras, one set per camera per run |
| **Sidecars** | `.iprj` image project, `.lst` containing all image position and orientation, `.cal` camera models — one per camera |

**Prerequisites** *(TBC 23339)*: "You need to first generate scans from the raw data before
exporting them to the TopoDot software. Otherwise, nothing will be exported." And: **"You must
close all run views prior to export. Otherwise, a warning message will pop up."**

**LAS files:** "a couple of 1.4 LAS format files, one couple per run."

> **Provenance implication:** the `.lst` file carries **image position and orientation**, which is
> trajectory-derived information at the station level. **It is not documented as identifying the
> trajectory it came from.**

### 29.6.4 Export to Solv3D

*(TBC 23888)* · **Mobile Mapping tab**

| | |
|---|---|
| **What leaves TBC** | Panoramic images and laser point clouds |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5 |
| **Timing** | **Trimble recommends No** — "Solv3D does not need the Timestamps information. Trimble recommends turning this option to No" |
| **Imagery** | Panoramic only, in a `Panorama` folder; a `reference.csv` alongside "which contains Roll, Pitch and Yaw information and X, Y, Z as well" |
| **Sidecars** | `reference.csv` |

Output: a folder named for the mission, with `Lasers` and `Panorama` sub-folders. LAS 1.4, "one
couple per run in case of a single scanner system and two when a double laser system is used."

> **Note the interaction.** Trimble's recommendation to disable timestamps here has a second
> effect it does not mention: per §29.3, timestamps off means the **generated** scans are
> exported rather than reprocessed ones. On this path the recommended setting is also the one
> that preserves the processing you performed.

### 29.6.5 Generic Point Cloud Export

*(TBC 11769)* · **Point Cloud tab**

| | |
|---|---|
| **What leaves TBC** | Point cloud only, in `.e57` (plain or **structured**), `.las`, `.laz`, `.pod`, `.pts`, `.ptx`, `.rcp`, `.tdx` |
| **Trajectory geometry** | **No** |
| **Specific trajectory identified** | **No** |
| **Coordinate system** | Per §29.5, including the ECEF option |
| **Timing** | LAS point records per §29.7 |
| **Imagery** | None |
| **Sidecars** | The scaling `.txt` |
| **Split** | *By station* — a separate LAS per scan station; *None* — a single LAS from all stations |

> **This is the path most likely to be used for an ordinary LAS or E57 deliverable, and it is the
> one with the least documented provenance and no run awareness** (§29.4).

### 29.6.6 Publish to TRCPS

*(TBC 29527)* · **Home ▸ Data Exchange ▸ Publish to TRCPS**, then the **Mobile Mapping** tab

Uploads to a **Trimble Connect** project via the **Trimble Desktop Utility (TDU)**, installed with
TBC. Requires a **Trimble ID**; uploads consume the account's Trimble Connect storage quota.

| | |
|---|---|
| **What leaves TBC** | Point cloud, **trajectories**, and optionally imagery |
| **Trajectory geometry** | **YES, MANDATORY** — "By default, mobile mapping point cloud and trajectories will be **automatically exported**" |
| **Specific trajectory identified** | **Not documented** |
| **Selection** | **Run-aware** — an individual run, multiple runs (Shift/Ctrl+Click), or the entire mission (Ctrl+A). The selection must include scan data; if not, Trimble says run **Generate Scans** first |
| **Imagery** | Publish panoramic / side / back-facing images, each optional |
| **Privacy** | **Blur people**, **Blur vehicles** — greyed out until an images option is selected; prompts for **GPU (if compatible) or CPU** |
| **In the delivered dataset** | The **3D+ View** offers 3D, Map, Image and Panorama modes; in 3D and Panorama, **"trajectories and camera markers can be included or hidden as needed"** |

> **Provenance implication:** the trajectory is **not optional** on this path — the publishing
> options govern imagery only — and it is a first-class, viewable object in the delivered dataset.
> **Which trajectory is published when several exist under a run is not documented.**
>
> **VENDOR CLARIFICATION REQUIRED · V-10** *(Appendix E)* · **FIELD TESTING REQUIRED · T19** *(Appendix E)*

> **OBSERVED SOFTWARE BEHAVIOR** · Trimble Connect's **UK region** is currently unavailable for
> Publish to TRCPS and Trimble Mobile Mapping data *(TBC RN 2026.10)*. Not applicable to
> Parametrix, but it confirms Publish to TRCPS is a Connected Workspace function.

## 29.7 Summary — what is documented as leaving TBC

| Path | Trajectory geometry travels? | Specific trajectory identified? |
|---|---|---|
| Classified LAS, Trajectory Split | **No** | **No** |
| Export to TMX | **Yes** | **Not documented** |
| TopoDot | No | No |
| Solv3D | No | No |
| Generic Point Cloud Export | No | No |
| **Publish to TRCPS** | **Yes, mandatory** | **Not documented** |

### Metadata documented as travelling, where applicable

| Metadata | Where |
|---|---|
| **Coordinate system and scale factor**, in a `.txt` sidecar | Any grid-scaled point cloud export *(TBC 11769, 27279)* |
| **Project global coordinate system**, embedded | ECEF option, LAS/LAZ *(TBC 11769)* |
| **GPS Time per point** | LAS exports with timestamps on. "According to the ASPRS LAS 1.4 specification, the Timestamp information refers to the GPS Time in the point records, i.e., standard GPS Time (satellite GPS Time) minus 1 billion of seconds. The origin of standard GPS Time is defined as midnight of the morning of January 6, 1980" *(TBC 23339, 22501)* |
| **Image position and orientation** | TopoDot `.lst`; Solv3D `reference.csv` (Roll, Pitch, Yaw, X, Y, Z) |
| **Latitude, longitude, altitude, acquisition time** in image files | Where GPS attributes are enabled |
| **`Program name: Trimble Business Center`** in image EXIF | *(TBC 21713_1)* |
| **Trajectory geometry** | TMX export; Publish to TRCPS |

> **IMPORTANT PROVENANCE LIMITATION**
>
> **Exported mobile mapping data may retain coordinate, timing, and in some formats trajectory
> information, but the captured Trimble documentation does not establish that the output uniquely
> identifies the adjusted trajectory or registration result used to create it.**
>
> A further limit on that statement: **Trimble's help topics describe dialogs, options and output
> structures. They do not exhaustively enumerate LAS header fields or VLR content.** Something may
> be written that the documentation does not mention.
>
> This is therefore a **software-behaviour testing question**, not an unresolved documentation
> research question. All known MX60 export and publish paths have been reviewed.
> **FIELD TESTING REQUIRED · T22** — export and inspect the file directly. **VENDOR CLARIFICATION
> REQUIRED · V-12** — does any TBC export write the source trajectory into a LAS header, VLR or
> sidecar? *(Appendix E; §30)*

## 29.8 Known limitations and silent failures

| Limitation | Path | Source |
|---|---|---|
| **Corrupted side camera images are exported as black images** | TopoDot, TMX | *(TBC 23339, 22501)* |
| All run views must be closed before export | TopoDot | *(TBC 23339)* |
| Scans must be generated first or nothing is exported | TopoDot, Solv3D | *(TBC 23339, 23888)* |
| Ground scaling does not expose its scale factor | All point cloud exports | *(TBC 11769, 27279)* |
| Grid-scaled re-import may double-scale | All point cloud exports | *(TBC 11769, 27279)* |
| MX9 Export to TMX requires a coordinate system without Geoid | TMX — **MX60 applicability not stated · V-17** | *(TBC 22501)* |
| Random sampling with no spatial rule | Classified LAS | *(TBC 27279)* · T17 |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We wrote the finished data out of TBC in whatever format the client needs
> — a LAS file, a package for TopoDot or Solv3D, or a publication to Trimble Connect — and we
> looked carefully at what each of those paths actually carries with it.
>
> **Why it matters.** This is the last moment the project and the deliverable are the same thing.
> Everything after this, the client has; everything before this, you can still fix. And there are
> several documented ways for the two to quietly diverge here.
>
> **What can go wrong.** The one to burn into memory: **registering a mission does not change the
> point cloud.** If nobody ran Update Scans, the file you export is the unregistered data. It
> opens fine, it looks identical, the residuals in your notes were good — and the client has the
> version from before the adjustment. Check that the scans you are exporting sit under the
> registered trajectory and carry the `_reg_` suffix, every time.
>
> Two more. There is an innocuous-looking option called **Export timestamps** that, when switched
> on, makes TBC rebuild the cloud from the raw data instead of exporting the scans you processed.
> Trimble does not say what trajectory that rebuild uses. Until somebody tests it, treat that
> switch as a decision rather than a convenience. And if you export in ground coordinates, the
> file does not record the scale factor it used — the grid option writes a small text file beside
> the cloud that does.
>
> **What good looks like.** Before exporting: the scan nodes you have selected sit beneath the
> trajectory you intended, the stations carry the registration suffix, and you know whether you
> are writing grid or ground. After exporting: the file opens, the extents match the corridor, the
> point count is plausible, the sidecar is present if you expected one, and somebody has opened a
> sample of the imagery rather than counting it. That is ten minutes, and it is the difference
> between a delivery and a re-delivery.
