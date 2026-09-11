# 30. Export — by Path

**Six documented MX60 paths.** No preference between them is expressed here; format choice is a
project and client matter Parametrix has not decided *(SOP §19.4, **D-38**)*.

**Do §31 first.** Every path below assumes the pre-export check has passed.

### 30.1 The paths

| Path | Where | Carries the trajectory? |
|---|---|---|
| **Export to LAS (Trajectory Split)** | Mobile Mapping tab | **No**, despite the name |
| **Export to TMX** | Mobile Mapping tab | **Yes** — one trajectory file for all devices, in a folder under the Mission folder |
| **Export to TopoDot** | Mobile Mapping tab | The `.lst` carries image position and orientation |
| **Export to Solv3D** | Mobile Mapping tab | Sidecar `reference.csv` |
| **Generic Point Cloud Export** | **Point Cloud tab** | **No** |
| **Publish to TRCPS** | Home ▸ Data Exchange ▸ Publish to TRCPS | **Yes** — point cloud and trajectories are exported by default |

### 30.2 Do — Export to LAS (Trajectory Split)

1. **Run Extract Classified Point Cloud first** — *Point Clouds ▸ Regions*. Without it there is
   nothing to export
2. **Home ▸ Data Exchange ▸ Export ▸ Mobile Mapping tab**
3. Set **Splitting distance** — "a value in meter multiple of 250"
4. Choose lasers: merged into one file, or left and right independently. **At least one must be
   selected**
5. Set **Format** — LAS 1.2 or 1.4 — and **Export unit**

*(TBC 27279)*

> **TESTING REQUIRED · T17**
>
> **Sample points performs *random* sampling to a fixed point count.** On a survey deliverable that
> is destructive thinning with no documented spatial rule — no minimum spacing, no preservation of
> edges or breaklines. Its default state is not stated. **Check it before exporting.**

### 30.3 Do — Export to TMX

1. **Mobile Mapping tab ▸ Export to TMX**
2. Decide the **Export timestamps** setting — **read §31 first**
3. Export

Produces panoramic images, side camera images, laser point clouds **and the trajectory**, plus a
`reference.csv` *(TBC 22501)*.

### 30.4 Do — Export to TopoDot

1. **Generate scans first.** "Otherwise, nothing will be exported"
2. **Close all run views.** "Otherwise, a warning message will pop up"
3. Export

Produces LAS 1.4, one couple per run *(TBC 23339)*.

### 30.5 Do — Export to Solv3D

1. **Mobile Mapping tab ▸ Export to Solv3D**
2. Trimble recommends **disabling timestamps** on this path

Produces a mission-named folder with `Lasers` and `Panorama` sub-folders, LAS 1.4 *(TBC 23888)*.

> On this path the recommended setting is also the safe one: timestamps off means the **generated**
> scans are exported rather than reprocessed ones (§31).

### 30.6 Do — Generic Point Cloud Export

1. **Home ▸ Data Exchange ▸ Export ▸ Point Cloud tab**
2. **This tab selects by region or a drawn rectangle — not by run** *(TBC 11769)*
3. Set **Scaling**: **Grid** or **Ground**, or **ECEF**

| Option | Behaviour |
|---|---|
| **Grid** | Current projected CRS with the combined scale factor. **Writes a `.txt` sidecar naming the coordinate system and scale factor.** Trimble warns re-importing it "may cause some inconsistencies due to a double-scaling effect" |
| **Ground** | Ground coordinates scaled from the 0,0 origin. **"The scale factor is not exposed during export"** |
| **ECEF** | LAS or LAZ in ground-based scaling, "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not record the scale factor it used.** The recipient cannot recover
> it from the file. Agree grid or ground in writing, and make sure the delivery can say which
> *(SOP §6.3)*.

> **This is the path most likely to be used for an ordinary LAS deliverable, and it is the one with
> the least documented provenance and no run awareness.**
>
> **TESTING REQUIRED · T23** — what happens when a Point Cloud tab selection is drawn across scans
> belonging to two different trajectories. Not documented.

### 30.7 Do — Publish to TRCPS

1. **Home ▸ Data Exchange ▸ Publish to TRCPS ▸ Mobile Mapping tab**
2. Requires a **Trimble ID**; uploads via the **Trimble Desktop Utility**, installed with TBC
3. **Point cloud and trajectories are exported by default** — the publishing options govern
   imagery only *(TBC 29527)*

> **VENDOR CLARIFICATION REQUIRED · V-10 · TESTING REQUIRED · T19**
>
> **Which trajectory is published when several exist under a run is not documented.**

> **From TBC 2026.10, Trimble ID sign-in requires two-step verification** — a code by email each
> time. Worth knowing before it stops a session.

### 30.8 Record

Export path, date, by whom, format, scaling — into the delivery record (§28, Appendix F).
