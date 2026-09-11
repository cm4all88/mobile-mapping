# 10. Mission Setup in TMI

## 10.1 Vehicle settings

> **CAUTION · [TRIMBLE]**
>
> **If an aiding navigation sensor is not activated in Vehicle Settings, its data will NOT be
> logged — even though all connections may have been made properly** *(TMI UG Rev L, p.21)*.
>
> This is Trimble stating how the system behaves. It is not a rule anybody can relax.
>
> This applies to **DMI and GAMS**. The hardware can be correctly installed, wired and present, and
> log nothing. There is no cabling fault to find and nothing looks wrong.

1. Open **Vehicle Settings**
2. **Confirm DMI is activated**, if fitted — and that its lever arm and **mounting position, left
   or right**, are set
3. **Confirm GAMS is activated**, if fitted — and that its lever arm is set
4. Confirm the **Install Height** preset is the one for this vehicle

> **The mounting side matters in the office.** The DMI's scale factor sign depends on it, and the
> processor cannot see the vehicle. **Record which side it is on** *(Technical Manual §9.2)*.

## 10.2 Capture settings

> **Expect either presentation, and record which you saw.**
>
> | Source | What the operator sees |
> |---|---|
> | MX60 Quick Start Guide Rev B, p.10 | Two controls — **Measurement Prog** `[500 kHz, 1000 kHz]` and **Line Speed** `[120 Hz, 200 Hz]` |
> | TMI User Guide Rev L, p.29 | A single combined **Laser Mode** |
>
> Which you get depends on the TMI version installed, which has not been confirmed
> *(**V-2**, `CONFLICT-005`)*.

| Setting | Range | Note |
|---|---|---|
| **Laser rate** | 500 / 1000 kHz per scanner | **The higher rate costs range**: 120 m instead of 150 m |
| **Line speed** | 120 / 200 Hz per scanner | More profiles per second = closer spacing along the corridor |
| **Lateral Range Limit** | 5–50 m | **V-7** — whether it affects accuracy or is purely a data-volume control is not documented |
| **Dust filter** | on/off | For **unpaved roads and mine sites** *(Product Bulletin, January 2025)* |

> The measurements-per-second values TMI displays are **rounded** *(TMI UG Rev L, pp.28–29)*.

> **The specification sheet's 1000/2000 kHz and 240/400 Hz are system totals across both
> scanners.** TMI uses the per-scanner numbering above. Do not go looking for 2000 kHz on the
> screen.

> **TESTING REQUIRED · T12**
>
> **The DMI scale factor's 5 % default assumes somebody measured the wheel.** If the value came
> from a manual for a nominal tyre, the office is weighting the DMI on an unverified claim. **If
> you know whether this wheel was measured, record it** *(SOP §13.1)*.

## 10.3 Record

Capture settings used, **and which presentation you saw**. Field record, Appendix C.

## 10.4 Stop if

- A fitted aiding sensor cannot be activated
- You cannot establish which capture settings are in force
