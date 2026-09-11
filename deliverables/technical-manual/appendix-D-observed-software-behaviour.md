# Appendix D — Observed Software Behaviour

**Generated view — do not edit by hand.** Produced by `tools/build-observed-behaviour.py` from the
**OBSERVED SOFTWARE BEHAVIOR** blocks in the body of this manual. Edit the section; regenerate
this.

An entry here is something seen in the software, or stated in a release note, that Trimble does
**not** document as procedure. It is weaker evidence than a **TRIMBLE DOCUMENTED PROCEDURE** block
and stronger than an inference. Where behaviour of this kind carries a real consequence, it also
appears in the warning register.

**9 entries.** Last generated 2026-09-11.

---

### §9.3 · The failure mode both share

"If an aiding navigation sensor is not activated in Vehicle Settings its data will **not** be
logged — even though all connections may have been made properly."

### §10.2 · Trimble Business Center — the office software

From TBC 2026.10, **Trimble ID sign-in requires two-step verification** — a code by email each
time *(TBC RN 2026.10)*. Anyone signing in to TBC or Trimble Connect needs access to the
account's email at that moment. Worth knowing before it stops a session.

### §17.4 · Outputs, and a filename that means something

A registered trajectory no longer matches its `smrmsg` file, so adjusted stretches lose their
RMS colour and render as **Undefined RMS** *(TBC 27248)*. **§24 quotes the behaviour in full and
makes a QC technique out of that side effect.**

### §24 · Reading Trajectory RMS Colouring

"If the mission contains some registrations then the modified segments will be colorized with
the **'Undefined RMS' color**" *(TBC 27248)*. A registered trajectory no longer matches the
`smrmsg` file, so adjusted stretches lose their RMS colour.

**Incidentally useful:** this makes the extent of a registration visible in plan. A **Local**
registration that stopped adjusting beyond the outermost control point (§21.5) shows the
boundary directly.

### §26.1 · What the MX60 imagery is for

**Whether imagery positions inherit a registration is not documented.** Registration produces a
new trajectory and Update Scans recomputes the point cloud from it (§19). No captured Trimble
topic states whether station positions and panorama orientations are recomputed too.

It is plausible that they are, since imagery is positioned from the trajectory. **It is not
stated, and must not be assumed.**

**FIELD TESTING REQUIRED · T26** — compare a station's position before and after a registration.
This is answerable in minutes and nobody has done it. *(Appendix E)*

### §26.2 · Resolution depends on the configuration

Trimble's export folder-structure examples show the MX60 tree containing **Camera 3 Back Down**
and **Camera 4 360°**, with per-face `.cal` files for the 360° camera (Front, Rear, Left, Right,
Top, Bottom). The MX9 and MX50 trees additionally show **Planar 1** and **Planar 2** side
cameras; **the MX60 tree does not** *(TBC 23339, 22501)*.

This suggests the **Export side images** option has nothing to export on an MX60. **Trimble does
not state this**, and the option remains present in the dialog.

**FIELD TESTING / VENDOR CLARIFICATION REQUIRED · T27** — **what imagery streams actually
exist on the MX60, and which are exposed through TBC export?** Run an export with side images
enabled and see what appears; confirm with the vendor what the MX60 camera complement is.

**Do not write MX9 or MX90 camera behaviour into MX60 procedure on the strength of a shared
dialog.** The option's presence in the export pane is not evidence that the sensor exists.
*(Appendix E; V-8)*

### §26.7 · Imagery in the delivered dataset

An exported panoramic image's file properties show **`Program name: Trimble Business Center`**
*(TBC 21713_1)*. Software provenance does reach the imagery, in EXIF. **It names the software,
not the trajectory** (§30).

### §28.3 · What it removes, and why that matters

The registered SBETs are written **to the project folder on disk**, not inside the TBC database
*(TBC 22905, 26473)*. Trimble does not state whether Cleanup deletes them or only removes the
project's references to them.

**FIELD TESTING REQUIRED · T28** — list the project folder before and after Cleanup and
compare. If the files survive, they are a partial audit trail that outlives the operation; if
they do not, the record is gone entirely. **This materially changes what must be archived
first.** *(Appendix E)*

### §29.6 · The MX60 export paths

Publish to TRCPS and Trimble Mobile Mapping data *(TBC RN 2026.10)*. Not applicable to
Parametrix, but it confirms Publish to TRCPS is a Connected Workspace function.
