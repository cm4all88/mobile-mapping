# Figure production register

**Cross-document. Project material, not reader material** — it was Technical Manual Appendix C and
was moved here, because a reader-facing appendix should not carry a production backlog.

Figures identified during source ingestion, to be cropped from the Trimble help captures held in
`sources/`. **No figure has been cropped or placed yet** — this is the production list, and it
serves **all four deliverables**.

The **Manual §** column gives the section each figure supports where that section exists in this
manual. Figures that belong in the **Field How To** or the **Office How To** are marked as such;
their final placement is settled when those documents are built, and this list is the single place
where figure production is tracked.

> **Crops, not whole pages.** A full help-portal screenshot carries Trimble's navigation, header
> and footer, which would make a Parametrix document look like a Trimble one (§1).
> Each entry below names the specific element to crop.

## C1 · Captions and attribution

> **PROPOSED — not adopted**
>
> Every figure carries: a Parametrix-style caption stating what the reader should see; the source
> citation; and a note that the interface shown is **TBC 2026.10** *(§1.6)*.
>
> Trimble screenshots are preserved as technical evidence and are **not** redrawn or paraphrased
> away. Trimble's page layout, typography and iconography are **not** carried over.

## C2 · The list

### Field and system

| # | Figure | Source | Manual § |
|---|---|---|---|
| F01 | MX60 sensor layout — two scanners, 360° camera, back-down camera | MX60 UG Rev B | 7.1 |
| F02 | Vehicle frame axes — **+X forward, +Y right, +Z down** | TBC 24886 / 25943 | 7.5 |
| F03 | Lever arm vs boresight, on a vehicle | TBC 24886 | 7.6 |
| F04 | TMI status display with colour indications | TMI UG Rev L | *Field How To* |
| F05 | Initialization manoeuvre profile — **speed against time** | *To be drawn — Parametrix original* | 13.1 |

### Trajectory and scans

| # | Figure | Source | Manual § |
|---|---|---|---|
| F06 | Raw mission folder tree — `POS_1/raw`, `Base`, `Camera_*`, `Laser_*`, `Extcal.json`, `.mxdb` | TBC 25943 | 5.2 |
| F07 | Process Raw Trajectory Data settings pane | TBC 25943 | 17.3 |
| F08 | **Trajectory coloured by RMS in Plan View** — the single most useful QC view | TBC 25943 / 27248 | 17.4 |
| F09 | The data chain — TMX → RWCX, one step on MX60 | *To be drawn — Parametrix original* | 5.1, 18.1 |
| F10 | Generate Scans filter pane | TBC 22499 | 18.3 |
| F11 | Results of Scan Generation dialog | TBC 22499 | 18.5 |
| F12 | Project Explorer showing scans nested beneath their trajectory | TBC 22638 | 5.3, 29.2 |

### Calibration

| # | Figure | Source | Manual § |
|---|---|---|---|
| F13 | Calibration site geometry — two roads crossing, four runs, 90° ± 30° | *To be drawn from TBC 24886 values* | 20.3 |
| F14 | Calibration results — Overall Overlap, Overall RMS, per-pair three-axis RMS | TBC 24886 | 20.3 |
| F15 | **Mission Report Capture devices table** — boresight installation vs calibration, **date of calibration** | TBC 24868 | 20.6 |
| F16 | Camera properties — Boresight installation vs Boresight refinement | TBC 24868 | 20.4 |

### Registration

| # | Figure | Source | Manual § |
|---|---|---|---|
| F17 | Control Points grid — **Use XY / Use Z / As Check / Target** columns | TBC 22905 | 22.2 |
| F18 | Targets pane with signed E / N / Elev residuals populated | TBC 22905 | 21.6, 22.7 |
| F19 | **Validate Picking** — overhead view, perpendicular side view, RMS of plane | TBC 22905 | 21.6 |
| F20 | Project Explorer — `Unnamed Run 0 › Sbet` / `Reg. Trajectory` | TBC 22905 | 21.3 |
| F21 | **Trajectory properties** — `Origin: Registration result`, Input trajectory, Registration type | TBC 22905 / 26473 | 21.3, 30.3 |
| F22 | Project folder listing `sbet_…_reg_0001…0004.out` | TBC 22905 | 21.3, 30.3 |
| F23 | Mission control list — one GCP, five instances, one per run | TBC 26473 | 21.4 |
| F24 | Project Explorer after mission registration — `RegTrajectory` under each run | TBC 26473 | 21.4 |
| F25 | **Tangential / Orthogonal / Vertical** axes on a curved trajectory | TBC 25096 | 21.15, 23.3 |
| F26 | Run-to-run **Results tab** — RMS statistics with `No overlap` rows | TBC 25096 | 21.15 |
| F27 | **Cutting Plane View** profile across two runs | TBC 25096 | 21.16, 25.1 |
| F28 | Plan View — Run to Adjust green, Reference Run red | TBC 25096 | 21.13 |

### Export and delivery

| # | Figure | Source | Manual § |
|---|---|---|---|
| F29 | **MX60** export folder tree — Camera 3 Back Down, Camera 4 360° with six `.cal` faces | TBC 23339 | 26.2, 29.6 |
| F30 | **TMX MX60 tree showing the `trajectory` sub-folder** beside `laser` and `panorama` | TBC 22501 | 29.6, 30.3 |
| F31 | Classified LAS Settings pane — splitting distance, per-laser, Format, Export unit | TBC 27279 | 29.6 |
| F32 | Solv3D output tree with `reference.csv` | TBC 23888 | 29.6 |
| F33 | Export Point Cloud Files Settings — Scaling, ECEF, Split | TBC 11769 | 29.5, 29.6 |
| F34 | **Publish to TRCPS** — "point cloud and trajectories will be automatically exported" | TBC 29527 | 29.6 |
| F35 | Trimble Connect 3D+ view — colorized cloud with **trajectory and camera markers** | TBC 29527 | 29.6 |

### Parametrix originals to be drawn

| # | Figure | Manual § |
|---|---|---|
| F36 | **The workflow at a glance** — field to delivery, one page | 2.3, 4 |
| F37 | **The degraded-GNSS branch diagram** — showing the two backward loops | 27.1 |
| F38 | **The provenance chain** — seven transitions, what survives each | 30.3 |
| F39 | **The ten QA/QC layers** | *SOP §16* |

## C3 · Source availability

| Batch | Held as files? |
|---|---|
| TBC help batch 2 — 17 topics | ✅ `sources/tbc-help-captures/` |
| TBC help batch 4 — 15 topics | ✅ `sources/tbc-help-captures-batch4/` |
| TBC help batch 7 — 7 topics | ✅ `sources/tbc-help-captures-batch7/` |
| **TBC help batch 6 — 4 export topics** (27279, 22501, 23339, 23888) | ❌ **Arrived inline; not archived** |
| MX60 / TMI / QSG manuals | ✅ repository root |

> **F29–F32 cannot be cropped until the batch 6 pages are supplied as files.** Their content is
> recorded and cited in §29; only the images are missing. This blocks figure production, not
> drafting.

## C4 · Branding

Settled. The **Parametrix Brand Guide v6, November 2023** governs, and the visual system built from
it is specified in `deliverables/_control/style/style-system.md`.

| | |
|---|---|
| Figure captions | Franklin Gothic 13.5 px, Medium Gray, `Figure n` in weight 600, then the caption, then the source citation |
| Screenshot crops | Crops, never whole help-portal pages. Trimble's navigation, header and footer are excluded |
| Frames | 1 px Light Gray 3 rule, square corners. No shadows |
| Callouts on figures | Parametrix Red, matching the CAUTION treatment, used only to mark the element the caption names |
| Parametrix originals | Charcoal and the document accent; Parametrix Red reserved for the element that carries the warning. The **spacer arrow** is the divider in any diagram that needs one |

> **The logo does not appear on figures.** It appears once in the running header and once in the
> footer, as the ix formation *(brand guide pp.13, 23)*. Adding it to a figure would breach the
> clear-space and no-added-elements rules of pp.13–14.
