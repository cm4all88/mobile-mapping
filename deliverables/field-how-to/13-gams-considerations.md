# 13. GAMS Considerations

**Only if GAMS is fitted.** Whether it is on this system is an open question — **D-2** *(SOP §6.4)*.

## 13.1 What it changes

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.67)*
>
> GAMS **reduces initialization time and eliminates the special driving manoeuvres** otherwise
> required.

> **Read the second half.** By implication, **the manoeuvres are required when GAMS is not
> fitted.** Trimble says the same from the other direction: **straight driving is more important
> if a GAMS antenna is not used** *(MX60 QSG Rev B, p.12)*.

## 13.2 What to do

**Perform the full sequence either way** (§12). It costs a few minutes, the static period does work
GAMS does not replace, and whether this system has GAMS is not yet established.

## 13.3 If GAMS is fitted — the installation requirements

| | Value |
|---|---|
| Offset accuracy, **collection only** | 10 cm or better |
| Offset accuracy, **post-processing** | **A few millimetres** |
| Minimum baseline | **2.0 m** between primary and secondary antennas |
| Antenna matching | **Must be the same type as the primary.** Do not mix |
| Measured to | The **L1 antenna phase centre** of the secondary antenna |
| **Re-measure** | **Every time GAMS is re-installed on the roof for a new mission** |

*(MX60 UG Rev B, pp.67–68)*

> **All Parametrix mobile mapping is post-processed, so the requirement is millimetres, not
> centimetres.** An offset good enough to navigate with is not good enough to survey with.

## 13.4 Stop if

- GAMS is fitted but not activated in Vehicle Settings (§10.1) — **it will log nothing**
- The published rack corner offsets are being used and you are not certain which rack is fitted.
  Those offsets apply to the **standard Trimble Roof Rack only** *(MX60 UG Rev B, p.68)*

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** is not held. It is needed to
> complete the installation procedure if GAMS is fitted.
