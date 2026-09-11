# 8. INITIALIZATION

The most important twenty minutes of the day.

## 8.1 In plain language

Before the system can produce an accurate trajectory, the navigation solution has to
*converge* — it has to work out not just where the vehicle is, but exactly how it is
oriented, and how much its inertial sensors are drifting.

It cannot do that sitting still, and it cannot do it from GNSS alone. It needs to feel the
vehicle move in ways that reveal those unknowns.

**So you park in the open, sit still for a few minutes, drive straight, then deliberately
speed up, slow down and turn.** That's initialization. Do it at the start of every
mission, and again — in reverse — at the end.

## 8.2 The procedure

> **IMPORTANT**
>
> Navigation alignment must complete **before data logging is allowed**. This is the
> system protecting you, not an obstacle. *(QSG Rev B, p.11)*

### Step by step

1. **Park in an open-sky area** with good GNSS visibility and PDOP. Avoid high buildings
   and obstructions that reduce reception and increase multipath.
2. **Start the mission** — enter mission name and area name, select the Vehicle and
   Capture presets, press Next, then Start.
3. **Remain still for 2–3 minutes**, logging static data.
4. **Drive straight ahead for approximately 20 m**, with no large steering inputs.
   → NAV status switches **red → orange**.
5. **Vary speed and perform dynamic steering manoeuvres.** Typically **2–3 turns** are
   sufficient. Trimble's example speed profile:
   **0 → 50 → 20 → 50 → 20 km/h**
   → NAV status switches **orange → green**.
6. **Repeat until all navigation parameters are green.**
7. **Allow additional settling time — up to 10 minutes** — before logging data.

*(QSG Rev B, pp.11–12, 14)*

> **FIELD TIP — where to do it**
>
> You need room to sit still safely, drive straight ~20 m, and make 2–3 turns with speed
> changes. A large empty parking lot is ideal. Scout two locations before you mobilise;
> Section 5 covers this.

> **IMPORTANT — the settling time is not optional padding**
>
> "Depending on your working environment, the time period can vary for the system to
> resolve its ambiguities, so it is advised to add some time (up to 10 minutes) before
> logging data **to avoid poor results at the start of recording runs**."
> *(QSG Rev B, p.12)*
>
> Data logged immediately after the light turns green is the weakest data of the mission.
> If the first thing you record is the most important part of the corridor, you have put
> your worst solution on your most important asset.

### With GAMS fitted

GAMS changes this materially. With a second GNSS antenna the system can derive heading
directly from the baseline between antennas, so:

> "Using a GAMS, not only is the initialization time reduced but also **no special driving
> maneuvers are necessary** to complete initialization."
> *(MX60 UG Rev B, p.67)*

The Quick Start Guide is more measured: driving straight is "more important if a GAMS
antenna is not used," and the relevance of straight driving versus dynamic steering
"depends on the hardware used" *(QSG Rev B, p.12)*.

> **PARAMETRIX DECISION REQUIRED**
>
> Decide whether the full manoeuvre sequence is performed even when GAMS is fitted.
>
> *Recommended practice:* perform it anyway. It costs a few minutes, it is what the Quick
> Start Guide's checklist describes, and it gives the office a strong initialization at
> both ends regardless of GAMS status. Skipping it saves little and removes redundancy you
> cannot recover later.

## 8.3 Reading the status

| NAV colour | Meaning | Recording |
|---|---|---|
| **Red** | No valid solution, or navigation system failure | **Blocked** |
| **Orange** | A solution exists | Permitted by TMI |
| **Green** | Solution **meets your user accuracy figures** | Yes — this is the target |

*(TMI UG Rev L, pp.9, 25, 40)*

**Other things that tell you initialization is progressing:**

| Sign | Meaning |
|---|---|
| **Blue arrow** appears on the map | A valid position is available — navigation logging has already started |
| **UTC time** appears top-right | GNSS initialization complete *(TMI UG Rev L, p.33)* |
| **Thin blue line** on the map | Trajectory is being recorded |
| Camera / Laser buttons turn green | Those devices are time-synchronized |

> **IMPORTANT — navigation logging is not the same as recording**
>
> Three facts from the TMI guide *(pp.36, 40)* that operators consistently confuse:
>
> - Navigation logging **starts automatically** as soon as a valid position exists and the
>   blue arrow appears — **even if the NAV button is still red**
> - Navigation logging is **not affected** by the colour changing orange↔green
> - Navigation logging **stops immediately when the mission is closed**
>
> So the trajectory is being recorded long before you press Record, and it keeps recording
> between runs. Pressing Record starts and stops **laser and imagery only**.

### The Navigation View

Press the Nav button for detail: a **logarithmic-scale** display of each accuracy
parameter, plus status information and a **satellite skyplot**. The point at which each
bar turns from orange to green is the User Accuracy figure from Capture Settings
*(TMI UG Rev L, pp.35–36)*.

> **FIELD TIP**
>
> Watch which parameter is holding you at orange. If it is heading, you need more dynamic
> manoeuvres. If it is position, you likely have a sky-visibility problem and should move
> to a better location rather than driving more circles.

## 8.4 What the system is actually doing

> **ADVANCED — a new operator can skip this**

The MX60 blends GNSS and inertial data using Applanix IN-Fusion+ / ProPoint GNSS-Inertial
integration on a dedicated Inertial Engine board *(MX60 UG Rev B, p.56)*. Initialization
is the process of that blended filter resolving several unknowns at once.

**The static period (2–3 minutes)** does two things. It lets the GNSS receiver collect a
clean stretch of data for the post-processor to resolve carrier-phase ambiguities against
— Trimble says explicitly this "aids post-processing software in resolving ambiguities"
*(QSG Rev B, p.11)*. And with the vehicle known to be stationary, the IMU's output *is*
its own bias: anything it reports while parked is error, which the filter can measure and
remove.

**Driving straight** gives the filter a clean velocity vector. GNSS knows the direction of
travel; the IMU knows the vehicle's orientation. Comparing them starts to pin down heading
— the hardest of the three attitude angles.

**Why heading is hardest.** Roll and pitch are observable even at rest, because gravity
gives an absolute vertical reference the accelerometers can feel. There is no equivalent
absolute reference for heading. It has to be *inferred* from motion — which is why a
system without GAMS needs manoeuvres, and one with GAMS does not.

**Varying speed and turning** is what makes the remaining errors observable. Under
constant velocity, an accelerometer bias and a small attitude error look identical to the
filter — both produce the same steady signal, and it cannot tell which is which. Change
the speed and direction, and the two decouple: they affect the measurements differently,
so the filter can separate and estimate them. This is what "dynamic manoeuvres" are
buying — not motion for its own sake, but **observability**.

**The 10-minute settling advice** reflects that convergence is gradual. The light turns
green the moment thresholds are crossed; the solution continues improving after that.

**Why symmetry at the end matters.** Office software processes the trajectory forwards
*and* backwards and blends the two. A good initialization at both ends means both
directions start from strength, and the weakest part of the run — the middle — is solved
from two strong ends instead of one *(QSG Rev B, p.13)*. Section 10.

## 8.5 When initialization goes wrong

| Symptom | Likely cause | Action |
|---|---|---|
| NAV stays **red** | No valid solution — poor sky, obstruction, multipath | Move to a genuinely open location. Check the skyplot |
| NAV reaches orange, won't go green | Attitude/heading not converged | More dynamic manoeuvres — speed changes and turns |
| Green, then drops back to orange | Passing through obstruction, or a marginal solution | Return to open sky; repeat manoeuvres; consider a better site |
| Takes far longer than usual | Poor constellation, or a location worse than it looks | Check the almanac. Consider waiting or relocating |
| NAV never leaves red, sky is clearly open | Possible system fault | Check LEDs and Message Log. Section 14 |

### When to re-initialize

Trimble does not publish a re-initialization trigger list. Based on what the documents
*do* say, re-initialize when:

- The NAV solution degrades and does not recover in open sky
- You have completed a long GNSS outage and are about to collect critical data
- The mission has been closed — **closing a mission stops navigation logging**, so a new
  mission requires a new initialization *(TMI UG Rev L, pp.31, 42)*

> **FIELD TIP — the exception worth knowing**
>
> If you only need **different capture settings** — a dust preset, a different laser mode —
> use **mission re-configuration** rather than closing the mission. Navigation logging
> keeps running throughout, so **no new GNSS/IMU initialization is needed**
> *(TMI UG Rev L, p.41)*.
>
> Closing the mission to change a setting costs you a full re-initialization. Section 9.

> **PARAMETRIX DECISION REQUIRED**
>
> Define the Parametrix re-initialization triggers and record them on the field checklist.
>
> *Recommended practice:* re-initialize after any NAV degradation not recovered within a
> few minutes of open sky, after any GNSS outage materially longer than 60 seconds if
> critical data follows, and whenever a mission has been closed. Record every
> initialization — time and location — in the field protocol.

## 8.6 Initialization checklist

| ☐ | Step |
|---|---|
| ☐ | Parked in open sky, good PDOP, away from buildings |
| ☐ | Mission started; correct Vehicle and Capture presets confirmed |
| ☐ | **Still for 2–3 minutes** |
| ☐ | Blue arrow visible; UTC time showing |
| ☐ | Straight ~20 m → NAV **orange** |
| ☐ | Speed variation + 2–3 dynamic turns → NAV **green** |
| ☐ | All navigation parameters green in Nav View |
| ☐ | **Settling time allowed — up to 10 minutes** |
| ☐ | Camera and Laser buttons green |
| ☐ | Initialization time and location recorded in the field protocol |

---

## References — Section 8

| Source | Pages |
|---|---|
| Trimble MX60 Quick Start Guide, Rev B, March 2025 | 11–14 |
| Trimble Mobile Imaging Software User Guide, Rev L, April 2026 (P/N T001242) | 9, 25, 31, 33, 35–36, 40–42 |
| Trimble MX60 User Guide, Rev B, May 2025 (P/N T001983) | 56, 67 |
