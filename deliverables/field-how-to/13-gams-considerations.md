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

> **PROPOSED INTERIM PRACTICE — deliberately more conservative than Trimble's GAMS statement**
>
> **Perform the full sequence either way** (§12) while this is a living draft. Trimble documents
> that GAMS eliminates the special driving manoeuvres; this draft is **not** claiming otherwise.
> The extra manoeuvres are being retained as an interim Parametrix practice because they cost little,
> the static period still matters, and the delivered GAMS fitment has not yet been confirmed.
>
> Once the actual system configuration and first controlled missions are validated, this paragraph
> is either adopted as Parametrix practice or simplified to match the confirmed configuration.

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
