# 13. Generate Scans

## 13.1 What it does

**Generate Scans** applies the trajectory to the raw scanner data and produces the point cloud.

```
   TMX                 Generate Scans                RWCX
   polar scan data  ──────────────────────────►   point cloud
   ranges + angles      + the trajectory           XYZ, intensity, colour, normals
   sensor-relative                                 georeferenced
```

> **This is where the trajectory meets the measurements.** Before it, the scanner data is a set
> of ranges and angles relative to a sensor that was moving. After it, every return has a
> coordinate. Change the trajectory and the same raw data produces a different cloud — which is
> the whole basis of registration (§15) and of Update Scans (§13.6).

### The MX60 has no MTA stage

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22503)*
>
> MX50 and MX60 convert **TMX → RWCX in one step**. MX9 and MX90 go RXP → TMX → RWCX in two, and
> the intermediate stage requires **MTA** (Multiple Times Around) range-ambiguity correction.

> **The MX60 workflow has no MTA configuration and no MTA failures.** If you encounter TBC
> documentation about configuring a GPU driver for MTA correction *(TBC 23856)*, it does not
> apply to this system. Mentioned because it is prominent in the TBC help and causes confusion.

## 13.2 Running it

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

Select a run or a mission in **Project Explorer** and choose **Generate Scans** from the context
menu. Scans appear beneath the trajectory node they were computed from.

Generating at mission level processes all runs. Generating at run level processes one — useful
when a single run has been re-collected or when testing filter settings before committing to a
full mission.

## 13.3 Filters

The Filters pane is where most of the judgement in this command lives, and where most of the
untested defaults are.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*

| Filter | What Trimble says it does |
|---|---|
| **Range Min / Max** | Discards returns outside the distance window |
| **Isolated Points** | Removes points with too few neighbours |
| **Fog** | Removes returns caused by fog |
| **Sun** | Removes returns caused by direct sunlight on the sensor |
| **Reflective Panels** | "Removes the noise before and after a target" |
| **Dust** | Removes airborne dust returns *(Product Bulletin, January 2025)* |

Two presets are offered — **Default** and **High Quality** — where High Quality enables Fog, Sun
and Reflective Panels.

> **FIELD TESTING REQUIRED · T1–T5**
>
> **The filter defaults are the largest block of untested settings in the workflow.** Each removes
> real returns under conditions that may or may not have occurred.
>
> **T1 — Default vs High Quality.** Trimble states what each preset contains and gives no
> selection criteria. High Quality enables three filters unconditionally, including on data
> collected in conditions where none of them applies.
>
> **T2 — Isolated Points.** Trimble's own text contradicts itself: the prose says the filter is
> on, the Restore Default Values behaviour says off.
>
> **T3 — Reflective Panels.** "Removes the noise before and after a target." **Does it also
> remove legitimate retro-reflective returns from signs and line marking?** This bears directly on
> sign inventory and retroreflectivity work, where those returns are the deliverable.
>
> **T4 — Range Max.** The MX60 default matches the scanner's maximum range at the lower pulse
> rate. The User Guide separately warns that real-world range is shorter in bright sunlight and at
> oblique incidence *(MX60 UG Rev B)*, so points may be retained well beyond useful range.
>
> **T5 — Fog and Sun.** Both remove real returns under defined conditions. Applying them when
> those conditions did not occur removes valid data.
>
> *(Appendix E)*

> **CAUTION**
>
> **Filtering is not reversible within a scan set.** A filtered return is not flagged, it is
> absent. Recovering it means regenerating the scans with different settings — which is cheap in
> effort and expensive in time on a large mission, and impossible once the raw data has been
> archived and the project cleaned up (§21).
>
> **Generate one representative run with the intended settings and look at the result before
> committing a whole mission.**

## 13.4 Colorization

Scans can be generated with colour from the imagery, or without.

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)* — so the decision made here propagates all the way to the deliverable.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule.
> *(Appendix E)*

> **PARAMETRIX DECISION REQUIRED**
>
> **Are scans generated coloured by default?** Colorization costs processing time and disk, and
> is not needed for every deliverable — but generating without it and discovering later that the
> client wanted coloured points means regenerating the mission. *(Register item 22)*

## 13.5 The Results record

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22499)*
>
> A **Results of Scan Generation** dialog records, per run: the **filters applied**, the **range**,
> and whether **colorization** was on.

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> **Capture the Results of Scan Generation into the project record.** It is the only artefact that
> states which filters produced a given cloud, and filter choice is a defensible-or-not decision
> that a reviewer may need to see years later.
>
> **Not adopted.** *(Register item 23; §23, §25)*

## 13.6 Update Scans — switching a cloud onto a different trajectory

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22638)*

**Update Scans** regenerates scans against a different trajectory. It is how a registration (§15)
reaches the point cloud.

| | **Generate Scans** | **Update Scans** |
|---|---|---|
| Purpose | Create scans from raw data | **Switch existing scans to a different trajectory** |
| Filters pane | Yes | **No** |
| Trajectory choice | The run's current trajectory | **Switches between the imported trajectory and an adjusted one** |

Updated scan stations carry a **`_reg_####`** suffix — for example
`Run_14_Laser Right_reg_0001 (S3)`.

> **IMPORTANT**
>
> **Registration alone changes nothing about the point cloud.**
>
> A registration produces a new trajectory node. The scans sitting under the old trajectory are
> still the old scans, in the old positions. Until Update Scans is run, **the cloud you would
> export is the unregistered one.**
>
> This is the most consequential sequencing fact in the office workflow, and the mistake it
> guards against is invisible: the project contains a registration, the residuals were good, the
> processor moved on — and the delivered cloud never received the adjustment.

Update Scans works in **both directions**: it switches between imported and adjusted, so it is
also the mechanism for reverting.

> **The exception.** **Register Run to Run** has an **Update Scans** checkbox inside the command,
> which regenerates the Run to Adjust's scans inline *(TBC 25096; §16.5)*. That is the only place
> where the two steps merge.

## 13.7 Recovering failed scans

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 28155)*
>
> **Recover Mobile Mapping Scans** exists for scan generation that failed or was interrupted.
> Treated as a recovery procedure in §26.

## 13.8 A hazard that lives in §22 but starts here

> **CAUTION · cross-reference to §22.3**
>
> Some TBC export paths do **not** export the scans this command produced.
>
> Trimble states, identically in two export topics: with **Export timestamps = No**, "the exported
> scans are the ones processed with the Generate Scans feature"; with **Export timestamps = Yes**,
> "the exported scans are **reprocessed from the raw data** and directly written to the LAS format
> files" *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated by Trimble.** Both readings are
> consistent with the text.
>
> The consequence for this section: the filters you chose here, the colorization decision you
> made, and — critically — the registration you applied through Update Scans may or may not be
> present in an export made with timestamps enabled.
>
> **FIELD TESTING REQUIRED · T18 — the highest-priority test in this document.** See §22.3 and
> Appendix E.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We combined the vehicle's computed path with the raw scanner measurements
> to produce an actual point cloud — the first time in the workflow that the data has coordinates.
> We also chose which returns to keep and whether to colour them from the imagery.
>
> **Why it matters.** Up to now the project has been an index and a line on a map. This is the
> data. It is also the first point at which the job becomes expensive to redo: regenerating a
> large mission with different filters is hours of processing, and on a corridor job it can be
> overnight.
>
> **What can go wrong.** The filters are the quiet problem. Several of them remove genuine
> returns under conditions that may not have applied on the day — a fog filter on a clear morning
> is throwing away data to solve a problem you did not have. And there is a specific worry for
> anyone doing sign or line-marking work: the Reflective Panels filter is described as removing
> noise around a target, and nobody has established whether it also removes the retro-reflective
> returns that *are* the deliverable. Nothing warns you; the points are simply not there.
>
> The bigger trap is sequencing, and it comes later in the job. Registering a mission does not
> change the point cloud. It produces a better path and leaves the cloud where it was. If nobody
> runs Update Scans, the project contains a perfectly good registration with good residuals, and
> the data you export is the unregistered version. It looks identical. It is centimetres out.
>
> **What good looks like.** Generate one run first, look at it, and only then commit the mission.
> A good result has the noise you expected removed and the features you care about still present —
> check the signs, check the line marking, check a wall at range. And when a registration is
> applied later, the scans sitting under the registered trajectory carry a `_reg_` suffix. If you
> cannot see that suffix, the adjustment has not reached the data.
