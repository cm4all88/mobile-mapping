# 5. Coordinate Systems, Control, and Project Setup

## 5.1 What this section does and does not cover

The reader is a survey professional. Projections, datums, geoids, epochs, grid and ground
coordinates, and the design of a control network are taken as known.

**This section covers only what mobile mapping does differently** — and there are five things:

1. The trajectory is computed in a frame that may not be the project's (§5.3)
2. Epoch handling has a silent failure mode and a new user-settable control (§5.4)
3. Control must be **findable in a point cloud**, which is a different requirement from
   occupiable (§5.5)
4. Control must **bracket** the delivered extent, because one adjustment method does not
   extrapolate (§5.6)
5. Grid and ground are decided at export, and one of the two options withholds its scale factor
   (§5.7)

## 5.2 Set the project coordinate system before importing

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> "Create a VCE project and if necessary, change the coordinate system so that it matches the
> coordinate system for the mobile mapping data to import." *(TBC 24886, 24460)*

> **IMPORTANT**
>
> Changing the CRS after import is possible in TBC generally, but by then every derived product —
> scans, registrations, exports — was computed in the previous frame. **Treat it as irreversible
> in practice** (§11.2).

### The database

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> The **Coordinate System Database v115** ships with TBC 2026.10. Selecting a predefined geoid
> model now enters the vertical datum name automatically *(TBC RN 2026.10)*.
>
> Two v115 entries relevant to US work: a grid transformation from **CSRN2025 (NAD83 2011) to
> CA SRS Epoch 2017.50** for California zones 1–6, and a **beta** Canadian **NATRF2022(CSRS)**
> with SGEOID2022-beta2.

## 5.3 The frame the trajectory is computed in

The trajectory is produced by POSPac, not by TBC (§12), and POSPac has its own view of the
project's coordinate system.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 25943)*
>
> | Condition | SBET filename |
> |---|---|
> | Datum and epoch **known** by POSPac | `sbet_[mission name].out` |
> | Datum and epoch **unknown** by POSPac | `sbet_[mission name]_[frame].out` — computed "first in ITRF00 and then in the datum and epoch of the project" |

> **The filename is a processing-path indicator and nothing more** (§12.4, §24 Layer 3). It tells
> you an additional transformation occurred. It does not tell you the parameters were right, that
> the project CRS is set up correctly, or that the result is accurate. The plain form is equally
> not proof of correctness.

> **FIELD TESTING REQUIRED · T10**
>
> **Establish which of Parametrix's normal coordinate systems POSPac recognises directly, and
> which trigger the ITRF00 path.** Answerable once, then known — and it determines whether an
> extra transformation is routine on Parametrix work or exceptional. *(Appendix I)*

### Computation mode and the reference frame

> **PARAMETRIX DECISION REQUIRED · D-19**
>
> **IN-Fusion+ Single Base or IN-Fusion+ PP-RTX?** *(TBC 25943; §12.3)*
>
> Single Base uses a local base station; PP-RTX uses Trimble's RTX corrections and needs no local
> base. The choice determines whether a base station must be occupied for every mission **and**
> the reference frame the solution is computed in — which feeds directly into §5.3.

## 5.4 Epoch

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> From TBC 2026.10: "When working with a time-dependent datum, you can now work at a specific
> epoch that is not the default reference epoch for the selected datum… **Note that this feature
> is intended for experienced users, as incorrect settings may lead to inaccurate results.**"
> *(TBC RN 2026.10)*

> **PARAMETRIX DECISION REQUIRED · D-21**
>
> **Which datum and epoch does Parametrix work in for mobile mapping, who sets it, and who checks
> it?**
>
> Epoch handling is not abstract in this workflow. It has a silent failure mode (§5.3) and now a
> user-settable control that Trimble itself flags as capable of producing inaccurate results.

## 5.5 Control that works for mobile mapping

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **GCP** is "an accurately surveyed coordinate location for a physical feature that can be
> identified on the ground, e.g., **a corner on the pavement markings**." A **target** is "a point
> extracted from the acquired scan data." *(TBC 22905)*

> **IMPORTANT · this changes control design**
>
> A mobile mapping GCP must be **findable in a point cloud** at the density and incidence angle
> the vehicle produced. That is a different requirement from occupiable with a prism.
>
> | Works well | Works poorly |
> |---|---|
> | Painted stop-bar and lane-line corners — crisp intensity edges | A survey nail in asphalt — a few millimetres across, below cloud resolution |
> | Checkerboard, diamond, rectangular and L-shape (GV) target panels, for which TBC has templates *(TBC 22905)* | Small features at grazing incidence |
> | Painted arrow and legend corners | Anything that moves, is repainted, or is worn |

### Horizontal and vertical are separable

TBC lets a point participate as **Use XY**, **Use Z**, or both — independently (§17.2).

> A painted stop-bar corner is an excellent horizontal target and a poor vertical one: it lies in
> the road surface, the scan hits it at a grazing angle, and the picked height depends on which
> return the operator snapped to. **Use it for what it is good at.**

> **FIELD TESTING REQUIRED · T25**
>
> **Which feature types are fit for horizontal control, vertical control, or both, at MX60 point
> density and incidence angle?** Answerable on a test site with features surveyed conventionally,
> and the answer will shape control design more than any software setting. *(Appendix I)*

## 5.6 Control layout

### The constraint that drives it

> **TRIMBLE DOCUMENTED PROCEDURE**
>
> A **Local** registration is "suitable for a local adjustment of a run, **not for systematic
> error along the run or for adjusting outside the ground control points set**." *(TBC 22905)*

> **CAUTION**
>
> **Local does not extrapolate.** Beyond the outermost control point the trajectory is not
> adjusted, and nothing indicates where the adjustment stopped. **Control must bracket the extent
> you intend to deliver, not merely fall within it.**

### The other scale indication Trimble gives

**Target-Bundle Adjustment** operates at **250 m** intervals when checked and **70 m** when
unchecked *(TBC 22905; §15.7)*. That is Trimble's own indication of the scale at which control
density matters.

### A structure for the decision

> **PARAMETRIX DECISION REQUIRED · D-16**
>
> **How many control points, at what spacing, and how many held as independent checks?**
>
> **No Trimble source states a minimum, a spacing, or a ratio.** TBC's software minimum is one
> control pair — a mathematical floor with no bearing on survey adequacy (§15.6).

> **PARAMETRIX PROCEDURE (PROPOSED)** — *not adopted*
>
> - Control **bracketing** each end of the delivered extent, outside it where the corridor allows
> - Control along the corridor at an interval set from the project accuracy requirement, and
>   **tightened where GNSS is predicted to be degraded** (§6.3)
> - **Independent check points distributed, not clustered**, including at least one in each
>   distinct GNSS environment — open sky, tree cover, urban canyon
> - **A check point near each end**, where a Local adjustment stops working and where the smoother
>   had data on one side only (§2.2)
>
> No counts, spacings or ratios appear here deliberately. Those are the content of D-16.

### Reference practice, for information only

> **EXTERNAL REFERENCE — NOT PARAMETRIX PROCEDURE**
>
> The Queensland TMR *Mobile Laser Scanning Technical Guideline* (March 2023, CC BY 4.0) is a
> published transport-agency specification in the source set. It defines survey-grade,
> engineering-grade and asset-grade tiers, and for its higher tiers specifies control adjacent to
> the start and end of the project and at intersections of controlled roads *(TMR §11)*.
>
> **It is cited as an example of how another agency has answered D-16, not as a Parametrix
> standard and not as a Trimble requirement.** Parametrix's own accuracy tiers, if it adopts any,
> are D-16.

## 5.7 Grid, ground, and what the deliverable carries

Decided at export (§22.5), but it belongs in project setup because the client agreement depends
on it.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(TBC 11769, 27279)*
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

> **PARAMETRIX DECISION REQUIRED · D-40**
>
> **What is Parametrix's default deliverable scaling, and what accompanies it?** *(§22)*

## 5.8 Project setup checklist

Full version in **Appendix C**.

| ☐ | Item |
|---|---|
| ☐ | Project CRS, vertical datum and geoid set and confirmed against the client requirement |
| ☐ | Epoch confirmed where a time-dependent datum is in use |
| ☐ | Control network computed and adjusted in the project CRS |
| ☐ | Control points selected for **findability in a point cloud**, not just occupiability |
| ☐ | Control **brackets** the delivered extent at both ends |
| ☐ | **Independent check points designated in writing, by the Project Surveyor, before processing** (§17.4) |
| ☐ | Grid or ground deliverable agreed with the client |
| ☐ | Accuracy requirement stated, in writing, per component |

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We set up the project frame and planned the control — with two twists that
> do not arise in conventional work. The control has to be *visible in a point cloud*, not just
> occupiable, and it has to sit at both ends of the job rather than merely inside it.
>
> **Why it matters.** Control is what ties a mobile mapping dataset to the ground. Without it you
> have an internally consistent shape floating on whatever the satellites managed that day. And
> unlike a traverse, you cannot add a point later by going back and occupying it — the target has
> to be visible in data that was already collected.
>
> **What can go wrong.** Two things specific to this workflow. A survey nail is an excellent
> control point and a useless mobile mapping target: it is millimetres across and the cloud simply
> does not resolve it. Pick painted markings, panel targets, things with an edge. And if you set
> control inside the corridor rather than bracketing it, one of TBC's adjustment methods will
> quietly leave the ends unadjusted — the cloud there looks exactly like the rest and is on the
> original trajectory.
>
> **What good looks like.** Control at both ends, outside the delivered extent where you can
> manage it. Features you can actually point at in a cloud. Points held back as independent checks
> — chosen and written down before anyone processes anything, spread along the corridor and
> including the difficult stretches. And a clear agreement about grid or ground, because one of
> the export options does not tell the recipient which scale factor it used.
