# 12. Coordinate Systems, Datums and Epochs

## 12.1 What this section covers

Coordinate systems, datums, projections and geoid models are ordinary survey knowledge and this
manual does not teach them. What it does cover is the handful of places where **mobile mapping
uses them differently from conventional survey work**, and where that difference has caused real
errors:

- The project coordinate system must be set **before** the mission is imported, not after (§12.2)
- The trajectory is computed in a frame chosen by POSPac, which may not be the project's, and the
  only outward sign is a filename (§12.3)
- Epoch matters more than usual, because the trajectory's reference frame and the project's
  control may be realised at different epochs (§12.4)
- Grid and ground scaling behave asymmetrically at export — one writes down what it did, the
  other does not (§12.5)

Everything else about datums and projections is assumed.

## 12.2 Set the project coordinate system before importing

> **TRIMBLE DOCUMENTED METHOD**
>
> "Create a VCE project and if necessary, change the coordinate system so that it matches the
> coordinate system for the mobile mapping data to import." *(TBC 24886, 24460)*

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

### The database

> **TRIMBLE DOCUMENTED METHOD**
>
> The **Coordinate System Database v115** ships with TBC 2026.10. Selecting a predefined geoid
> model now enters the vertical datum name automatically *(TBC RN 2026.10)*.
>
> Two v115 entries relevant to US work: a grid transformation from **CSRN2025 (NAD83 2011) to
> CA SRS Epoch 2017.50** for California zones 1–6, and a **beta** Canadian **NATRF2022(CSRS)**
> with SGEOID2022-beta2.

## 12.3 The frame the trajectory is computed in

The trajectory is produced by POSPac, not by TBC (§17), and POSPac has its own view of the
project's coordinate system.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> | Condition | SBET filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — computed "first in ITRF00 and then in the datum and epoch of the project" |

> **The filename is a processing-path indicator and nothing more** (§17.4, and Layer 3 of the layered verification — the **SOP §16**). It tells
> you an additional transformation occurred. It does not tell you the parameters were right, that
> the project CRS is set up correctly, or that the result is accurate. The plain form is equally
> not proof of correctness.

> **FIELD TESTING REQUIRED · T10**
>
> **Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and
> which trigger the ITRF00 path.** Answerable once, then known — and it determines whether an
> extra transformation is routine on Parametrix work or exceptional. *(Appendix E)*

### Computation mode and the reference frame

> **Open Parametrix decision — D-19.** Stated and tracked in the **SOP §6**; see also the master register.

## 12.4 Epoch

> **TRIMBLE DOCUMENTED METHOD**
>
> From TBC 2026.10: "When working with a time-dependent datum, you can now work at a specific
> epoch that is not the default reference epoch for the selected datum… **Note that this feature
> is intended for experienced users, as incorrect settings may lead to inaccurate results.**"
> *(TBC RN 2026.10)*

> **Open Parametrix decision — D-21.** Stated and tracked in the **SOP §6**; see also the master register.

## 12.5 Grid, ground, and what the deliverable carries

Decided at export (§29.5), but it belongs in project setup because the client agreement depends
on it.

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 11769, 27279)*
>
> | Option | Behaviour |
> |---|---|
> | **Scaling: Grid** | Points in the current projected CRS with the combined scale factor. **An associated `.txt` file specifies the coordinate system and scale factor used.** Trimble warns that re-importing it "may cause some inconsistencies due to a **double-scaling effect**" |
> | **Scaling: Ground** | Ground coordinates scaled from the 0,0 origin by the average combined scale factor. **"The scale factor is not exposed during export"** |
> | **ECEF export** | LAS or LAZ in ground-based scaling "that includes the project's global coordinate system information" |

> **IMPORTANT**
>
> **A ground-scaled export does not record the scale factor it used.** The recipient cannot
> convert without being told. Grid writes a sidecar; ECEF embeds the global CRS. Agree with the
> client which they are receiving, and make sure the file can say so.

> **Open Parametrix decision — D-38.** Stated and tracked in the **SOP §6**; see also the master register.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We went through the four places where mobile mapping treats coordinate
> systems differently from a conventional survey: when the CRS has to be set, what frame the
> trajectory was actually computed in, why epoch matters, and what a grid or ground export
> carries with it.
>
> **Why it matters.** In conventional work the coordinate system is something you can change your
> mind about — the observations are raw and the reductions are repeatable. Here the coordinate
> system is baked into everything downstream the moment the mission is imported, because the
> trajectory, the scans, the registration and the exports are all computed products. Change the
> CRS afterwards and you have not reprojected your data; you have orphaned it.
>
> **What can go wrong.** The one that is hardest to catch is the trajectory frame. POSPac may not
> recognise the project's datum and epoch, in which case it computes in ITRF00 and then transforms
> — and the only thing that tells you so is an extra word in the SBET filename. That is not an
> error, and the result may be perfectly correct. But it means an extra transformation happened
> that nobody chose, and if the parameters were wrong it will look like a small systematic shift
> rather than like a mistake.
>
> **What good looks like.** The CRS, datum, epoch and geoid are set and written down before the
> first mission is imported. Somebody has looked at the SBET filename and knows which path it
> took. And the client agreement says grid or ground in writing, because a ground-scaled export
> does not record the scale factor it used and the recipient cannot recover it from the file.
