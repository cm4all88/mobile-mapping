# 23. Imagery QC

### Do

1. Step through the imagery along the corridor
2. Work the checklist
3. Check alignment against the point cloud at a feature edge

### Look at

| Check | Looking for |
|---|---|
| **Coverage** | Gaps where a camera stopped, or a run was not colorized |
| **Exposure** | Blown highlights; blocked shadows under canopy and in underpasses. **Both unrecoverable** |
| **Motion blur** | Speed too high for the light available |
| **Obstruction** | Aerials, a following vehicle, a smear on the dome |
| **Focus and contamination** | Rain, dust, insects on the optical surface |
| **Corrupted images** | **Silent** — see below |
| **Alignment with the cloud** | Colour in the wrong place at feature edges: a camera boresight issue (§13.2) |

*(SOP §16.6)*

### Expect

Resolution by configuration *(TBC 22501, 23888)*:

| | Core | Pro | Premium |
|---|---|---|---|
| Panoramic | **8192 × 4096** | **12288 × 6144** | **12288 × 6144** |
| Side / planar | 4096 × 3008 | 4096 × 3008 | 4096 × 3008 |

> **PARAMETRIX DECISION REQUIRED · D-2** — which configuration this system is. Every number above
> depends on it *(SOP §6.4)*.

### Stop if

- **A corrupted side camera image exports as black.** It is silent: nothing warns you, and the
  export succeeds. If you find one, assume there are others
- Coverage has a gap you cannot account for
- The imagery does not sit on the cloud

> **PARAMETRIX DECISION REQUIRED · D-31**
>
> Whether the proposed **file-size scan** for finding silently corrupted imagery is adopted. It is a
> screening method proposed by this project and **not validated** *(Technical Manual §26)*.

> **TESTING REQUIRED · T26, T27** — whether exported imagery reflects a registration at all, and
> which imagery streams the MX60 actually has and TBC exposes.

### Record

That the imagery check was performed and by whom. **No software artefact exists.**

> **PARAMETRIX DECISION REQUIRED · D-32** — imagery privacy. Whether unblurred originals are
> retained, and for how long. Decided before collection, not on request *(SOP §19.6)*.
