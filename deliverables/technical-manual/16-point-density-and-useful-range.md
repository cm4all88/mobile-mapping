# 16. What Determines Point Density and Useful Range

Two questions come up on every project — *how dense will the cloud be?* and *how far out is it
good for?* — and they have different answers from different parts of the system. Density is
geometry and settings. Useful range is trajectory quality.

## 16.1 The instrument's own numbers

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, pp.54–55)*
>
> | | Value |
> |---|---|
> | Laser pulse repetition rate, **per scanner** | **500 kHz / 1000 kHz** selectable |
> | Scan speed, profiles per second, **per scanner** | **120 Hz / 200 Hz** selectable |
> | Maximum measurement range | **150 m** at the lower rate · **120 m** at the higher rate |
> | Minimum range | **0.6 m** |
> | Range accuracy | **2 mm**, one sigma under test conditions |

> **CAUTION · two ways of quoting the same instrument**
>
> The MX60 specification sheet quotes **1000 / 2000 kHz** and **240 / 400** profiles per second.
> Those are **system totals across both scanners**. The User Guide figures above are **per
> scanner**, and TMI's own **Measurement Prog** and **Line Speed** settings use the per-scanner
> labelling *(`SPEC-004`, `SPEC-005`, `SPEC-011`; QSG-008, QSG-009)*.
>
> **Do not put the system-total figures into a field instruction.** A crew told to set 2000 kHz
> will not find it on the screen.

> **The higher rate costs range.** 1000 kHz per scanner gets 120 m; 500 kHz gets 150 m. That is a
> direct trade, made at the instrument, and it is the first of the three levers below.

## 16.2 The three levers on density

Point density along a corridor is set by three things, and only three:

| Lever | Effect | Where it is set |
|---|---|---|
| **Pulse repetition rate** | More pulses per second → more points, **at the cost of maximum range** | TMI, field |
| **Scan speed (profiles/s)** | More profiles per second → profiles closer together along the direction of travel | TMI, field |
| **Vehicle speed** | Slower → profiles closer together along the corridor | The driver |

Vehicle speed is the lever that changes most between projects and the one with the least
guidance attached to it.

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B)*
>
> | | Value |
> |---|---|
> | **Recommended maximum with the system operating** | **80 km/h (50 mph)** |
> | Absolute maximum, operating or not | 110 km/h (68 mph) |

> **Open Parametrix decision — D-43.** *What collection speed, by deliverable type?* Trimble
> publishes a recommended maximum and an absolute maximum and **no guidance relating speed to
> deliverable quality**. Stated and tracked in the **SOP §9**; see also the master register.

Imagery follows the same logic on its own clock: the spherical camera captures at up to **10 fps**
and the down camera at up to **9 fps**, by distance or by time *(MX60 Spec Sheet, p.2)*. Capture
by distance decouples image spacing from vehicle speed; capture by time does not.

> **VENDOR CLARIFICATION REQUIRED · V-7**
>
> **Does the Lateral Range Limit affect accuracy, or is it purely a data-volume tool?** TMI offers
> a lateral range limit at acquisition. If it only discards returns beyond a distance, it is a file
> size control and nothing else. If it changes what the scanner does, it belongs in this section as
> a fourth lever. The documentation held does not say which. *(Appendix E)*

## 16.3 Geometry does more than settings

Two effects change density more than any setting, and neither is adjustable.

**Density falls with range.** The angular spacing between pulses is fixed, so the distance
between adjacent returns grows with range. A façade at 60 m is sampled far more coarsely than the
road surface at 6 m, on the same pass with the same settings.

**Density falls with incidence angle.** A surface hit obliquely is sampled across a stretched
footprint. Road markings ahead of and behind the vehicle are hit at a grazing angle, which is why
a painted stop-bar corner is a good horizontal target and a poor vertical one (§22.3).

> These two effects are why *a second pass in the opposite direction* improves a dataset more
> than any setting change: it converts grazing incidence into direct incidence and long range into
> short range for the far side of the corridor.

## 16.4 The range specification is a laboratory figure

> **TRIMBLE DOCUMENTED PROCEDURE** — *(MX60 UG Rev B, p.55)*
>
> The maximum range figures apply to **flat targets larger than the beam diameter, at
> perpendicular incidence, with 23 km atmospheric visibility**. Range is **shorter in bright
> sunlight than under overcast**.

Every one of those conditions is optimistic relative to a corridor survey. Real targets are small,
oblique, and frequently wet or dark. The published maximum is the ceiling, not the working
distance.

## 16.5 Useful range is a different question, with a different answer

The scanner can return a point at 150 m. Whether that point is good enough to measure from is a
question about the **trajectory**, not the scanner.

From §3.1: an attitude error displaces a point by the range multiplied by the angular error in
radians. Range accuracy is 2 mm and does not change with distance. Attitude error does not change
with distance either — but its *effect* does, in direct proportion.

| | At 10 m | At 50 m | At 100 m |
|---|---|---|---|
| Range error contribution | 2 mm | 2 mm | 2 mm |
| Attitude error contribution | ×1 | ×5 | ×10 |

> **This is arithmetic, not a specification.** **No Trimble source in the set publishes an
> attitude error budget for the MX60 point cloud.** The published attitude figures — roll and
> pitch 0.005° Core/Pro, 0.0025° Premium, heading 0.015° with GAMS *(MX60 UG Rev B, p.56)* — are
> trajectory accuracies under stated conditions, not point cloud accuracies at range. Converting
> one into the other requires assumptions this manual does not make.

> **WHY THIS MATTERS**
>
> **Useful range is not a property of the instrument. It is a property of the job.** Two clouds
> collected on the same day with the same instrument and the same settings have different useful
> ranges if one was collected under open sky and the other in an urban canyon, because the
> attitude solution was better in one than the other. That is why there is no single number to
> publish, and why the honest answer to "how far out is this good for?" begins with looking at the
> trajectory RMS for that stretch (§24).

> **FIELD TESTING REQUIRED · T1**
>
> **Establishing a working useful range for Parametrix deliverables is a test, not a calculation.**
> Survey features conventionally at a spread of ranges from the vehicle path, collect over them
> under known GNSS conditions, and compare. The result would give a defensible range statement for
> each deliverable class — which is currently the largest gap between what this manual can say and
> what a project manager needs to promise a client.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We separated two questions that get asked as if they were one: how many
> points you get, and how far out you can trust them.
>
> **Why it matters.** Density you control — pulse rate, scan speed, how fast you drive. Faster
> pulses give more points but less range; driving slower puts the profiles closer together. None
> of that is subtle and all of it is decided before or during collection. Useful range is a
> different animal. The scanner will happily return a point at 150 m. Whether that point is where
> it says it is depends on how well the system knew which way it was pointing at that instant, and
> a pointing error acts through distance — the same error that is invisible at 10 m is ten times
> as large at 100 m.
>
> **What can go wrong.** Quoting the maximum range as if it were a working range. The published
> figure assumes flat targets bigger than the beam, hit square on, in clear air, and says range is
> shorter in bright sun. A wet oblique kerb line at 120 m is none of those things. The other trap
> is the specification sheet's system-total pulse rates, which are double the numbers the crew will
> see on the screen in TMI.
>
> **What good looks like.** Nobody promises a range figure without knowing what the trajectory was
> doing over that stretch. A second pass in the opposite direction, which fixes the far side of the
> corridor better than any setting will. And eventually a tested range statement per deliverable
> class, because right now that number is the biggest thing this manual cannot give you.
