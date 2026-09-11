# Appendix G — Figure List and Placeholders

Figures identified during source ingestion, to be cropped from the Trimble help captures held in
`sources/`. **No figure has been cropped or placed yet** — this is the production list.

> **Crops, not whole pages.** A full help-portal screenshot carries Trimble's navigation, header
> and footer, which would make the SOP look like a Trimble document (§1, branding requirement).
> Each entry below names the specific element to crop.

## G1 · Captions and attribution

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> Every figure carries: a Parametrix-style caption stating what the reader should see; the source
> citation; and a note that the interface shown is **TBC 2026.10** *(§1.6)*.
>
> Trimble screenshots are preserved as technical evidence and are **not** redrawn or paraphrased
> away. Trimble's page layout, typography and iconography are **not** carried over.

## G2 · The list

### Field and system

| # | Figure | Source | § |
|---|---|---|---|
| F01 | MX60 sensor layout — two scanners, 360° camera, back-down camera | MX60 UG Rev B | 4.1 |
| F02 | Vehicle frame axes — **+X forward, +Y right, +Z down** | TBC 24886 / 25943 | 7.3 |
| F03 | Lever arm vs boresight, on a vehicle | TBC 24886 | 14.2 |
| F04 | TMI status display with colour indications | TMI UG Rev L | App. B |
| F05 | Initialization manoeuvre profile — **speed against time** | *To be drawn — Parametrix original* | 8.2 |

### Trajectory and scans

| # | Figure | Source | § |
|---|---|---|---|
| F06 | Raw mission folder tree — `POS_1/raw`, `Base`, `Camera_*`, `Laser_*`, `Extcal.json`, `.mxdb` | TBC 25943 | 10.1 |
| F07 | Process Raw Trajectory Data settings pane | TBC 25943 | 12.3 |
| F08 | **Trajectory coloured by RMS in Plan View** — the single most useful QC view | TBC 25943 / 27248 | 12.4 |
| F09 | The data chain — TMX → RWCX, one step on MX60 | *To be drawn — Parametrix original* | 2.5, 13.1 |
| F10 | Generate Scans filter pane | TBC 22499 | 13.3 |
| F11 | Results of Scan Generation dialog | TBC 22499 | 13.5 |
| F12 | Project Explorer showing scans nested beneath their trajectory | TBC 22638 | 11.3, 22.2 |

### Calibration

| # | Figure | Source | § |
|---|---|---|---|
| F13 | Calibration site geometry — two roads crossing, four runs, 90° ± 30° | *To be drawn from TBC 24886 values* | 6.7, 14.3 |
| F14 | Calibration results — Overall Overlap, Overall RMS, per-pair three-axis RMS | TBC 24886 | 14.3 |
| F15 | **Mission Report Capture devices table** — boresight installation vs calibration, **date of calibration** | TBC 24868 | 14.6 |
| F16 | Camera properties — Boresight installation vs Boresight refinement | TBC 24868 | 14.4 |

### Registration

| # | Figure | Source | § |
|---|---|---|---|
| F17 | Control Points grid — **Use XY / Use Z / As Check / Target** columns | TBC 22905 | 17.2 |
| F18 | Targets pane with signed E / N / Elev residuals populated | TBC 22905 | 15.6, 17.6 |
| F19 | **Validate Picking** — overhead view, perpendicular side view, RMS of plane | TBC 22905 | 15.6 |
| F20 | Project Explorer — `Unnamed Run 0 › Sbet` / `Reg. Trajectory` | TBC 22905 | 15.3 |
| F21 | **Trajectory properties** — `Origin: Registration result`, Input trajectory, Registration type | TBC 22905 / 26473 | 15.3, 23.3 |
| F22 | Project folder listing `sbet_…_reg_0001…0004.out` | TBC 22905 | 15.3, 23.3 |
| F23 | Mission control list — one GCP, five instances, one per run | TBC 26473 | 15.4 |
| F24 | Project Explorer after mission registration — `RegTrajectory` under each run | TBC 26473 | 15.4 |
| F25 | **Tangential / Orthogonal / Vertical** axes on a curved trajectory | TBC 25096 | 16.6, 18.3 |
| F26 | Run-to-run **Results tab** — RMS statistics with `No overlap` rows | TBC 25096 | 16.6 |
| F27 | **Cutting Plane View** profile across two runs | TBC 25096 | 16.7, 18.5 |
| F28 | Plan View — Run to Adjust green, Reference Run red | TBC 25096 | 16.4 |

### Export and delivery

| # | Figure | Source | § |
|---|---|---|---|
| F29 | **MX60** export folder tree — Camera 3 Back Down, Camera 4 360° with six `.cal` faces | TBC 23339 | 19.2, 22.6.3 |
| F30 | **TMX MX60 tree showing the `trajectory` sub-folder** beside `laser` and `panorama` | TBC 22501 | 22.6.2, 23.3 |
| F31 | Classified LAS Settings pane — splitting distance, per-laser, Format, Export unit | TBC 27279 | 22.6.1 |
| F32 | Solv3D output tree with `reference.csv` | TBC 23888 | 22.6.4 |
| F33 | Export Point Cloud Files Settings — Scaling, ECEF, Split | TBC 11769 | 22.5, 22.6.5 |
| F34 | **Publish to TRCPS** — "point cloud and trajectories will be automatically exported" | TBC 29527 | 22.6.6 |
| F35 | Trimble Connect 3D+ view — colorized cloud with **trajectory and camera markers** | TBC 29527 | 22.6.6 |

### Parametrix originals to be drawn

| # | Figure | § |
|---|---|---|
| F36 | **The workflow at a glance** — field to delivery, one page | 2.6, 4 |
| F37 | **The degraded-GNSS branch diagram** — showing the two backward loops | 20.1 |
| F38 | **The provenance chain** — seven transitions, what survives each | 23.3 |
| F39 | **The ten QA/QC layers** | 24.2 |

## G3 · Source availability

| Batch | Held as files? |
|---|---|
| TBC help batch 2 — 17 topics | ✅ `sources/tbc-help-captures/` |
| TBC help batch 4 — 15 topics | ✅ `sources/tbc-help-captures-batch4/` |
| TBC help batch 7 — 7 topics | ✅ `sources/tbc-help-captures-batch7/` |
| **TBC help batch 6 — 4 export topics** (27279, 22501, 23339, 23888) | ❌ **Arrived inline; not archived** |
| MX60 / TMI / QSG manuals | ✅ repository root |

> **F29–F32 cannot be cropped until the batch 6 pages are supplied as files.** Their content is
> recorded and cited in §22; only the images are missing. This blocks figure production, not
> drafting.

## G4 · Branding

> **PARAMETRIX BRANDING — PLACEHOLDER**
>
> The document is **unstyled**. Branding is applied once, at the end, when content and structure
> are stable *(`analysis/GUIDE-REQUIREMENTS.md` §1)*.
>
> **Held:** `brand/parametrix-wordmark.png`, `brand/parametrix-x-mark.png`; sampled colours
> **charcoal `#343433`** and **red `#EB2A2B`**.
>
> **Still needed:** vector logo (SVG/EPS), a reversed variant for dark backgrounds, and whatever
> template, example and brand-standard material exists.
>
> **Note for capture consistency:** TBC 2026.10 introduced a **dark theme** *(TBC RN 2026.10)*.
> **All screenshots must be captured in one theme** — light, matching every existing capture.
> Mixed light and dark TBC screenshots in a Parametrix manual read as an error.
