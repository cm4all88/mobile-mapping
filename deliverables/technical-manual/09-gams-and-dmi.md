# 9. GAMS and DMI

Both are optional. Both change what the system is capable of, and both change the field
procedure. Whether this system has them is an open item (**D-2 / V-4**, §7.7).

## 9.1 GAMS — a second antenna, and therefore a heading

**GAMS** is the GNSS Azimuth Measurement System: a second GNSS antenna mounted a known distance
from the primary one. Two antennas a known distance apart give a **direct heading measurement**.

That matters because heading is the hardest attitude component to determine. Roll and pitch are
anchored by gravity — an accelerometer knows which way is down. Nothing anchors heading. Without
a second antenna, heading has to be solved out of the vehicle's motion, which requires the
vehicle to move in ways that make it observable (§13).

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.67)*
>
> GAMS **reduces initialization time and eliminates the special driving manoeuvres** otherwise
> required.

> **Read the second half of that sentence.** It says, by implication, that **the manoeuvres are
> required when GAMS is not fitted.** Trimble's Quick Start Guide states the same thing from the
> other direction: **straight driving is more important if a GAMS antenna is not used**
> *(MX60 QSG Rev B, p.12)*. The field procedure is therefore not the same on a system with GAMS
> and a system without, and knowing which one this is precedes writing it down (§13).

### What GAMS requires to work

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, pp.67–68)*
>
> | Requirement | Value |
> |---|---|
> | Offset accuracy, **collection only** | 10 cm or better |
> | Offset accuracy, **post-processing** | **on the order of a few millimetres** |
> | Minimum baseline, post-processing | **2.0 m** between primary and secondary antennas |
> | Antenna matching | Primary and secondary **must be the same type**. Do not mix |
> | Measured to | The **L1 antenna phase centre** of the secondary antenna |
> | Re-measure | **Every time GAMS is re-installed** on the roof for a new mission |

> **The two accuracy figures are two orders of magnitude apart, and survey work is on the tight
> one.** All Parametrix mobile mapping is post-processed, so the requirement is millimetres, not
> centimetres. A GAMS offset good enough to navigate with is not good enough to survey with.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.68)*
>
> Known offsets from the **top-left front corner of the standard Trimble Roof Rack** to the
> external reference point: **X +1.006 m · Y −0.469 m · Z +0.025 m**.

> **CAUTION**
>
> Those published offsets apply to the **standard roof rack only** — not to the shock-absorbing
> mounting rack. Which rack is fitted is an open conflict in the source documents
> (`CONFLICT-003`, §7.4). Using the published corner offsets on the wrong rack puts a fixed,
> systematic error into the GAMS baseline and therefore into heading.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** *(referenced MX60 UG p.43)* is
> not held. It is needed to complete the installation procedure if GAMS is fitted.

### What GAMS is worth

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.56)*
>
> Heading accuracy, all configurations: **0.015°**, with the GAMS option and a 2 m baseline.

Apply §3.1 to that figure to see what it means in the cloud: an angular error acts through range,
so the same heading error produces a proportionally larger position error the further the feature
is from the vehicle.

## 9.2 DMI — an independent measure of distance travelled

A **DMI** (Distance Measuring Indicator) is a wheel-mounted sensor giving an independent
along-track distance. It constrains the inertial solution when GNSS is poor: the IMU can drift in
along-track scale, and the DMI does not.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.46; TMI UG Rev L, p.21)*
>
> - The DMI wheel must be a **non-steering** wheel
> - The lever arm is measured to **the centre of the tread where the DMI wheel contacts the road**
> - TMI requires the lever arm in metres, the **mounting position — left or right, taking the
>   driving direction as reference** — and the **wheel diameter**, which is to be measured "with
>   great care"

### Two signs that point in opposite directions

This is the single most error-prone detail in the installation, and it is worth setting out
side by side because both quantities are entered by hand, both depend on the mounting side, and
they carry **opposite** signs.

| Quantity | Mounted **left** | Mounted **right** | Source |
|---|---|---|---|
| **Lever arm Y** (vehicle frame: +Y is right) | **negative** | positive | *(MX60 UG Rev B, p.46)* |
| **Scale factor** (trajectory processing, §17.3) | **positive** | negative | *(TBC 25943)* |

> **CAUTION**
>
> A left-mounted DMI has a **negative Y lever arm** and a **positive scale factor**. They are
> different quantities describing different things — one is a position, one is a correction to a
> measured distance — and their signs are not related. Anyone who reasons "it's on the left, so
> both are the same sign" will get one of them wrong.
>
> The lever arm is entered in the field, in TMI. The scale factor is entered in the office, in
> TBC. **Record which side the DMI is on at installation**, because the processor cannot see the
> vehicle.

### The 5 % that is an assumption, not a measurement

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 25943)*
>
> DMI scale factor standard deviation: **default 5 %**. "Increase the setting if the scale factor
> is not known with 5% accuracy, and **set it to 100% if it is not known at all**."

> **FIELD TESTING REQUIRED · T12**
>
> **The 5 % default is only correct if the wheel diameter was actually measured.** If the value
> came out of a manual for a nominal tyre, 5 % is an assertion of accuracy that nobody verified,
> and the filter is weighting the DMI accordingly. Trimble provides the honest escape hatch — set
> it to 100 % if unknown. Determine which case applies before trusting the default.

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble MX Distance Measuring Indicator Installation & Operation Manual** *(referenced
> MX60 UG p.42)* is not held. It contains the scale-factor value for the measured wheel diameter,
> which trajectory processing needs (§17.3).

## 9.3 The failure mode both share

> **OBSERVED SOFTWARE BEHAVIOR / TRIMBLE DOCUMENTED METHOD** — *(TMI UG Rev L, p.21)*
>
> "If an aiding navigation sensor is not activated in Vehicle Settings its data will **not** be
> logged — even though all connections may have been made properly."

> **CAUTION**
>
> This applies to both DMI and GAMS. The hardware can be correctly installed, correctly wired and
> physically present, and log nothing, because a checkbox in Vehicle Settings is off. There is no
> cabling fault to find and nothing looks wrong.
>
> In the office the symptom is the corresponding pane in **Process Raw Trajectory Data** appearing
> **dimmed** — TBC dims the GAMS and DMI settings when the sensor was disabled during acquisition
> *(TBC 25943; §17.3)*. By then the mission is collected.

Two consequences: the preflight check on a system with either sensor fitted has to confirm
activation and not merely presence, and the office intake check has to look at whether those
panes are dimmed and say so, while a re-collection is still cheap.

## 9.4 Summary — what each contributes

| | **GAMS** | **DMI** |
|---|---|---|
| Gives the filter | A direct **heading** observation | An independent **along-track distance** |
| Most valuable | At initialization, and wherever heading is weakly determined | Through GNSS outages, where inertial along-track scale drifts |
| Without it | Heading is solved from motion; straight driving and manoeuvres matter more *(QSG p.12)* | The inertial solution carries outages unaided |
| Configured | In TMI Vehicle Settings, field | Lever arm in TMI, field; scale factor in TBC, office |
| Silent failure | Not activated in Vehicle Settings → not logged | Not activated → not logged; or scale factor from a nominal, unmeasured wheel |

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at the two optional sensors: a second GNSS antenna that measures
> heading directly, and a wheel sensor that measures how far the vehicle actually travelled.
>
> **Why it matters.** Heading is the attitude component nothing else pins down. Gravity tells the
> system which way is down, so roll and pitch have an anchor; nothing tells it which way is north.
> With a second antenna it gets that directly. Without one it has to work it out from how the
> vehicle moves, which is why the driving manoeuvres at the start of a mission exist and why
> Trimble says straight driving matters *more* when GAMS is absent. The DMI does a different job:
> it keeps the along-track scale honest through a tunnel or under tree cover, where the inertial
> sensor alone will quietly stretch or compress the distance travelled.
>
> **What can go wrong.** Three things, all of them silent. A sensor that is installed but not
> activated in Vehicle Settings logs nothing at all. A DMI scale factor taken from a manual rather
> than a measured wheel is a guess wearing a 5 % accuracy label. And the DMI's two signs run
> opposite ways — left-side mounting means a negative lever-arm Y and a positive scale factor —
> which catches people who assume the two must agree.
>
> **What good looks like.** Somebody knows which sensors are fitted, the offsets were measured to
> millimetres rather than centimetres because this is post-processed survey work, the activation
> was confirmed before driving, and the mounting side is written down somewhere the office can
> find it.
