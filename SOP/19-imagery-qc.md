# 19. Imagery QC

## 19.1 What the MX60 imagery is for

| Camera | Output | Typical use |
|---|---|---|
| **360° spherical** | Panoramic images along the corridor | Feature identification, asset attribution, virtual site visits, client review |
| **Rear-downward** | Pavement-facing imagery | Pavement condition, orthomosaics, line-marking work |

Imagery is positioned from the trajectory, exactly as the point cloud is. It inherits the same
errors and improves — or does not — in the same way.

> **OBSERVED SOFTWARE BEHAVIOR · unverified**
>
> **Whether imagery positions inherit a registration is not documented.** Registration produces a
> new trajectory and Update Scans recomputes the point cloud from it (§13.6). No captured Trimble
> topic states whether station positions and panorama orientations are recomputed too.
>
> It is plausible that they are, since imagery is positioned from the trajectory. **It is not
> stated, and must not be assumed.**
>
> **FIELD TESTING REQUIRED · T26** — compare a station's position before and after a registration.
> This is answerable in minutes and nobody has done it. *(Appendix I)*

## 19.2 Resolution depends on the configuration

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 22501, 23888)*

| Image | MX60 **Core** | MX60 **Pro** / **Premium** |
|---|---|---|
| Panoramic | **8192 × 4096 px** | **12288 × 6144 px** |
| Side / planar | 4096 × 3008 px | 4096 × 3008 px |

> **IMPORTANT**
>
> **Core delivers a quarter of the panoramic pixels of Pro and Premium.** Any commitment to a
> client about imagery deliverable quality — legibility of sign text, identification of small
> assets, orthomosaic ground sample distance — depends on which configuration is on the roof, and
> Parametrix does not currently know which that is (§4.1).
>
> *(D-2; Appendix I)*

### A configuration note about side cameras

> **OBSERVED SOFTWARE BEHAVIOR**
>
> Trimble's export folder-structure examples show the MX60 tree containing **Camera 3 Back Down**
> and **Camera 4 360°**, with per-face `.cal` files for the 360° camera (Front, Rear, Left, Right,
> Top, Bottom). The MX9 and MX50 trees additionally show **Planar 1** and **Planar 2** side
> cameras; **the MX60 tree does not** *(TBC 23339, 22501)*.
>
> This suggests the **Export side images** option has nothing to export on an MX60. **Trimble does
> not state this**, and the option remains present in the dialog.
>
> **FIELD TESTING / VENDOR CLARIFICATION REQUIRED · T27** — **what imagery streams actually
> exist on the MX60, and which are exposed through TBC export?** Run an export with side images
> enabled and see what appears; confirm with the vendor what the MX60 camera complement is.
>
> **Do not write MX9 or MX90 camera behaviour into MX60 procedure on the strength of a shared
> dialog.** The option's presence in the export pane is not evidence that the sensor exists.
> *(Appendix I; V-8)*

## 19.3 What to check

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> | Check | Looking for |
> |---|---|
> | **Coverage** — is there imagery for the full corridor? | Gaps where a camera stopped, or where a run was not colorized |
> | **Exposure** | Blown highlights on bright surfaces, blocked shadows under tree cover and in underpasses — both are unrecoverable |
> | **Motion blur** | Speed too high for the light available |
> | **Obstruction** | The survey vehicle's own aerials, a following vehicle, a smear on the dome |
> | **Focus and contamination** | Rain, dust, insects on the optical surface |
> | **Corrupted images** | See §19.4 — these are **silent** |
> | **Alignment with the point cloud** | Colorized points in the wrong colour at feature edges indicates a camera boresight issue (§14.4) |
>
> **Not adopted.** *(D-27)*

## 19.4 Corrupted side camera images are exported as black

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "**Corrupted side camera images are exported as black images.**" *(TBC 23339, 22501)*

> **CAUTION**
>
> **This is a silent failure.** The export completes. The file count is right. The images are
> there. Some of them are black.
>
> Nothing in TBC reports it, and a deliverable can pass every automated check with a proportion of
> its imagery blank. **The only detection is looking at the imagery**, which on a corridor job
> means sampling systematically rather than opening the first few.

> **PROPOSED PARAMETRIX QC AUTOMATION — VALIDATION REQUIRED**
>
> **This is not a Trimble procedure. It is a screening method proposed by this document and not
> yet validated.**
>
> Include a **file-size scan** of the exported imagery in the delivery check (§24). The logic: a
> uniformly black JPEG typically compresses far smaller than a valid image, so **anomalously small
> files are a useful screening flag** and a sorted file listing surfaces candidates without
> opening a single image.
>
> **File size alone cannot establish image validity.** It is a screening method, not proof. A
> small file may be a legitimately low-detail frame — a plain sky, a blank wall, an unlit tunnel —
> and a corrupted image is not guaranteed to be small. Anything the scan flags must be opened and
> looked at; anything it does not flag is not thereby verified.
>
> **Validation required** before adoption: run it against a known-good export and a known-bad one
> and establish whether a usable threshold exists for MX60 imagery.
>
> *(D-31)*

## 19.5 Colorized point clouds

Colour on the point cloud comes from the imagery, at scan generation (§13.4).

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> Colour is exported "if the scans have been generated with the color option set to on"
> *(TBC 23339, 22501)*.

Two failure modes worth checking specifically:

**Colour fringing at feature edges** — points on a kerb taking the colour of the road, or points
on a pole taking the colour of the sky behind it. Small amounts are inherent: the camera and the
scanner are at different positions and see slightly different things. Large or systematic
fringing indicates a **camera boresight problem** (§14.4), and is one of the few places where a
calibration issue is directly visible.

**Colour from the wrong exposure** — a stretch of cloud markedly darker or lighter than its
neighbours, where the camera's automatic exposure changed between passes.

> **FIELD TESTING REQUIRED · T6**
>
> The colouriser offers a forward versus backward camera preference with no stated selection rule
> *(§13.4)*. Its effect on fringing is untested. *(Appendix I)*

## 19.6 Privacy and blurring

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> **Blur people** and **Blur vehicles** options exist on the **Publish to TRCPS** command
> *(TBC 29527)*, and the export commands cross-reference a **Blur Exported Images** topic
> *(TBC 23339, 23888, 22501, 20927_1, 21713_1)*.
>
> On Publish to TRCPS, the blur options are **greyed out until an images option is selected**, and
> blurring prompts to use **GPU (if compatible) or CPU** *(TBC 29527)*.

> **The Blur Exported Images topic has not been captured.** It is the one remaining Trimble topic
> identified as worth collecting, and it should be captured before imagery privacy becomes a
> requirement on a live job. It is not a gap in the technical workflow — blurring is a delivery
> option, not a processing stage.

> **PARAMETRIX DECISION REQUIRED**
>
> **What is Parametrix's position on imagery privacy?**
>
> Mobile mapping imagery routinely captures pedestrians, vehicle licence plates, private property
> and building interiors visible through windows. This is not a Trimble question and no Trimble
> setting answers it.
>
> The decision needs to cover:
>
> - Whether blurring is applied by default, on request, or by jurisdiction
> - Whether **unblurred originals are retained** after a blurred deliverable is issued, and for
>   how long (§25)
> - What the client is told about what was captured
> - Whether any client or jurisdiction imposes a requirement Parametrix must meet
>
> Blurring is irreversible in the delivered product and the decision has legal and reputational
> dimensions that sit well outside this SOP. *(D-32)*

## 19.7 Imagery in the delivered dataset

Where imagery travels, and what travels with it:

| Path | Imagery | GPS attributes in the image file |
|---|---|---|
| **Export to TMX** | Panoramic, side, back-facing | Optional — latitude, longitude, altitude, acquisition time |
| **Export to TopoDot** | Panoramic, side, back-facing, as cubical images | Optional |
| **Export to Solv3D** | Panoramic | Optional |
| **Publish to TRCPS** | Panoramic, side, back-facing — each optional | — |

*(TBC 22501, 23339, 23888, 29527)*

> **OBSERVED SOFTWARE BEHAVIOR**
>
> An exported panoramic image's file properties show **`Program name: Trimble Business Center`**
> *(TBC 21713_1)*. Software provenance does reach the imagery, in EXIF. **It names the software,
> not the trajectory** (§23).

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We checked the photographs: that they cover the whole route, that they are
> properly exposed and sharp, that nothing is blocking the lens, and that where the imagery has
> been draped onto the point cloud the colours land on the right points.
>
> **Why it matters.** Imagery is often what the client actually looks at. A project manager who
> will never open a point cloud will click through panoramas, and an asset inventory job may
> depend entirely on being able to read a sign face. It is also the part of the deliverable where
> defects are most obvious to a non-specialist, which cuts both ways — easy to catch, and
> embarrassing if you do not.
>
> **What can go wrong.** Two things stand out. First, resolution is not a property of the MX60; it
> is a property of *which MX60*. Core panoramas are a quarter of the pixels of Pro and Premium,
> which is the difference between reading a sign at 20 m and guessing at it. Promising imagery
> quality without knowing which unit is on the roof is promising blind.
>
> Second, Trimble states that corrupted side camera images are exported as black. Not flagged,
> not reported, not missing — present, and black. The export succeeds, the file count is right,
> and a client opens image 4,712 to find nothing there. Sorting the exported files by size takes
> two minutes and finds every one of them, because a black JPEG is tiny.
>
> **What good looks like.** Continuous coverage with no unexplained gaps. Exposure that holds
> through the shaded stretches as well as the open ones. Colour on the point cloud that lands
> cleanly on feature edges — a kerb coloured like a kerb, not like the road beside it, because
> that fringing is the visible symptom of a camera boresight problem. And a systematic sample of
> the imagery actually opened and looked at, not just counted.
