# 25. Visual QC

## 25.1 The visual check

Trimble requires it and does not describe how to do it thoroughly. What follows assembles the
mechanics Trimble does give *(TBC 24886, 25096)* into a method.

### Cutting Plane View — checking agreement between overlapping data

The tool for the question *do two passes of the same feature land in the same place?*

1. **Point Clouds ▸ View ▸ Cutting Plane View** (it opens automatically after calibration or
   run-to-run registration if the option was checked)
2. Set rendering to **Scan Color** — one colour per scan, so the two data sets are
   distinguishable. **This is the step that makes the check possible**; in a single colour, two
   offset surfaces read as one thick surface
3. Increase **Point Size**
4. Set **Cutting plane thickness** (§25.2)
5. In Project Explorer, **check only the scans in the pair** and uncheck everything else
6. **Drag the slider along the run**, watching the gap
7. Optionally **Show surface-plane intersection** where a surface exists

What you are looking for: **one wall, one kerb, one pole.** Two of anything is a disagreement,
and its size in the profile is its size in the data.

> **FIELD TIP**
>
> Drag the slider through the **whole** run, not a representative sample. Trajectory error is
> correlated in time (§3), so disagreement is concentrated in stretches rather than scattered.
> A pass that is perfect for 2 km and 5 cm out for 300 m will look perfect at every point you
> spot-check and be unacceptable where it matters.

### What else to look at, and what nothing automates

> **This manual states no Parametrix procedure.** A practice covering this is proposed in the **SOP §13** (D-27); it is not decided here.

## 25.2 Cutting plane thickness

> **FIELD TESTING REQUIRED · T16**
>
> Trimble's screenshots show **0.030** in the calibration topic *(TBC 24886)* and **5.000** in the
> run-to-run topic *(TBC 25096)*, with no stated basis for either.
>
> The value determines what the check can see. Too thin and the profile is empty. Too thick and a
> real 3 cm offset is buried inside a 5 m band of points collected from either side of the plane.
>
> Establish working values for the checks in §25.1 and record them. *(Appendix E)*


---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We went and looked at the point cloud — specifically at places where two
> passes should agree — using a profile view with one colour per scan, dragged along the whole
> corridor rather than sampled at a few spots.
>
> **Why it matters.** This is the half of QC that no number can do. Trimble requires it and does
> not describe how to do it thoroughly, which is why this section assembles the mechanics into a
> method. What you are looking for is simple: one wall, one kerb, one pole. Two of anything is a
> disagreement, and its size in the profile is its size in the data.
>
> **What can go wrong.** Two things, and both are about how you set the view up rather than what
> you are looking at. If the rendering is left in a single colour, **two surfaces four centimetres
> apart look exactly like one surface four centimetres thick** — you will stare straight at the
> defect and not see it. And if the cutting plane is too thick, a real offset is buried inside a
> band of points collected from either side of the plane.
>
> The third failure is sampling. Mobile mapping error arrives in stretches, not speckles, because
> it is driven by a filter that changes smoothly over minutes. A corridor that is flawless for two
> kilometres and five centimetres out for three hundred metres will pass every spot check you take.
>
> **What good looks like.** Scan Color on, point size up, a sensible plane thickness, and the
> slider dragged the full length of every overlap — showing one of everything. Flat surfaces that
> are as thin at fifty metres as at ten. And the ends of the corridor checked specifically, because
> that is where a Local adjustment stops working and where the trajectory smoother had data on one
> side only.
