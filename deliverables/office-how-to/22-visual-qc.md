# 22. Visual QC

**This is the layer that catches what numbers cannot.** It has no software artefact, so if you do
not record it, there is no evidence it happened.

### 22.1 Do

1. **Point Clouds ▸ View ▸ Cutting Plane View**
2. **Set rendering to Scan Color** — see below
3. **Drag the plane along the corridor, full length.** It is tedious, and the tedium is the
   check — error arrives in stretches, so a plane dropped in three places finds nothing
4. Work the checklist under **Look at**
5. Record what you covered, and by whom

### 22.2 The setting that makes or breaks this

> **IMPORTANT · [TRIMBLE]** — the visual check itself is Trimble's instruction (§20).
> **[PROPOSED · SOP §16.5 · D-27]** — what the pass covers is this project's checklist.
>
> **Set rendering to Scan Color** — one colour per scan. Without it, two offset surfaces read as
> one thick surface and the exact defect this check exists to find is invisible
> *(Technical Manual §25)*.
>
> It is part of the method, not a display preference.

### 22.3 Look at

| Check | Looking for |
|---|---|
| **Overlapping passes in the cutting plane, full length** | Doubled surfaces |
| **Flat surfaces at range** — a wall, a building face | Thickening with distance: attitude error or a calibration issue |
| **The ends of the corridor** | Where a **Local** adjustment stopped; where the smoother was weakest |
| **The degraded stretches you found in §10** | Whether the registration actually fixed them |
| **Vertical surfaces against horizontal** | Systematic tilt |
| **Features near control versus far from control** | Residual growth with distance from constraint |

*(SOP §16.5)*

### 22.4 Expect

Overlapping passes landing on each other. Flat surfaces that stay flat as range increases.

### 22.5 Stop if

- Two passes are visibly offset from each other anywhere
- A wall thickens with range
- The cloud is good near control and degrades between — that is the shape of an adjustment that
  fitted its constraints and nothing else

> **PARAMETRIX DECISION REQUIRED · D-27**
>
> **What does a visual point-cloud QC pass cover?** The checklist above is proposed, not adopted
> *(SOP §16.5)*.

> **TESTING REQUIRED · T16** — the working cutting-plane thickness for these checks.

> **PARAMETRIX DECISION REQUIRED · D-39** — how much of a corridor is inspected, and how that is
> decided *(SOP §16.5)*.

### 22.6 Record

**That the visual check was performed, by whom, and over what extent.** No software artefact
exists. This is the record.
