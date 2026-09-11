# 13. Initialization — What It Actually Solves

Initialization looks like a warm-up. It is not. It is a short observation campaign designed to
make quantities observable that are not observable at rest or at constant velocity, and the
quality of everything collected afterwards depends on it.

The operational step list lives in the **Field How To**. This section explains what each step is
for, so that a crew that has to improvise — a site with no open sky, a route that cannot be
driven straight for 20 m — knows which part of the sequence they are trading away.

## 13.1 The sequence Trimble documents

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, pp.13–14; MX60 UG Rev B)*
>
> 1. **Park in an open-sky area** with good GNSS visibility and PDOP, avoiding high buildings and
>    obstructions
> 2. Start the mission in TMI
> 3. **Log 2–3 minutes of static data** before driving
> 4. **Drive straight ahead for approximately 20 m**, with no larger dynamic steering. The
>    navigation status switches on completing this
> 5. **Drive straight at varying speed** — accelerate then decelerate — **and perform dynamic
>    steering manoeuvres.** An example profile: **0 → 50 → 20 → 50 → 20 km/h**
> 6. Navigation status progresses **red → orange → green**. Green means the user accuracies for
>    the navigation system are met
> 7. **Allow up to 10 further minutes of settling before logging data that matters**

> **IMPORTANT**
>
> **Navigation alignment must be completed before data logging is allowed** *(MX60 QSG Rev B)*.
> The system enforces this — it is not a matter of operator discipline. What is **not** enforced
> is step 7.

## 13.2 What the static period does

Two separate things, and both are worth knowing because they fail differently.

**It lets the GNSS receiver resolve a clean solution.** A continuous set of observations from a
stationary antenna under open sky is the best conditions the receiver will see all day.

**It gives the inertial filter a constraint it can exploit: the vehicle's true velocity is zero.**
Anything the motion sensors report while parked is therefore **pure error** — measurable, and
removable. This is how the filter gets its first estimate of the gyro and accelerometer biases,
which it then carries forward through the whole mission (§8.2).

> **WHY THIS MATTERS**
>
> A static period under tree cover satisfies the clock and not the physics. The zero-velocity
> constraint still applies, so some of the benefit survives; the GNSS half does not. If open sky
> is genuinely unavailable at the start point, the honest response is to drive to open sky
> *before* starting the mission, not to start it where the vehicle happens to be parked.

## 13.3 What the manoeuvres do

At constant velocity in a straight line, a small attitude error and a sensor bias produce **the
same signature** in the observations. The filter cannot separate them, because nothing in the
data distinguishes them. Change speed and change direction and they stop looking alike — the two
quantities affect the observations differently under acceleration — so the filter can tell them
apart.

| Manoeuvre | What it makes observable |
|---|---|
| **Straight run, ~20 m** | Initial heading from the direction of travel. This is the step the navigation status is waiting on |
| **Varying speed** | Along-track accelerometer bias, and the separation of bias from pitch |
| **Dynamic steering** | **Heading** — the hardest component, and the reason the turns exist |

Heading is the hardest attitude component for the reason given in §9.1: gravity anchors roll and
pitch, and nothing anchors heading. The manoeuvres are how a system without GAMS obtains it, and
they still help a system with GAMS.

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, p.12; MX60 UG Rev B, p.67)*
>
> **Straight driving is more important if a GAMS antenna is not used.** GAMS reduces
> initialization time and eliminates the special driving manoeuvres otherwise required.

> Perform the full sequence either way. It costs a few minutes, the static period is doing work
> that GAMS does not replace, and whether this system has GAMS is not yet established (**D-2**,
> §7.7).

## 13.4 Why green is not finished

> **IMPORTANT**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for up to ten more minutes before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.** Do not spend it
> on the most important part of the corridor.

This is the one part of the sequence the system does not enforce, which makes it the one part
that gets skipped. It is also the part that costs nothing but patience.

> **WHY THIS MATTERS**
>
> There is a natural but wrong mental model in which the status light is a pass/fail gate: red
> means not ready, green means ready, and the moment it turns green the system is as good as it
> is going to get. What is actually happening is that an estimate is converging, and the threshold
> was crossed somewhere on the way. Ten minutes later the same estimate is better. The light does
> not change again, so nothing tells you.

## 13.5 What a weak initialization costs, and where it shows

A weak initialization does not produce an obviously bad dataset. It produces one where the
attitude solution is carrying more error than it should, everywhere, and §3.1 says that error
acts through range — so it is worst on the features furthest from the vehicle, which are often
the ones the client cares about.

It also cannot be repaired in the office in any general way:

| Remedy | Does it help? |
|---|---|
| Reprocessing the trajectory | Only if better base data or corrections are available. The observation geometry is what it is |
| LiDAR QC | Possibly — it solves boresight angles and corrects the trajectory using scan overlap (§11) |
| Registration | It will fit the control it is given, absorbing some of the error at the control and leaving it between (§21) |
| Re-collection | Always works. Costs a mobilisation |

> **This is the asymmetry from §5.5 in its most concrete form.** Five minutes at the start of the
> mission, or a decision later about how much residual error to accept in a deliverable.

---

> **IN PLAIN ENGLISH**
>
> **What we just did.** We took the start-of-mission routine apart and said what each piece is
> for: the two or three minutes parked, the straight run, the speed changes, the turns, and the
> ten minutes of patience after the light goes green.
>
> **Why it matters.** The system is not warming up. It is solving for things it cannot see any
> other way. Parked, it knows its true speed is zero, so everything the motion sensors report is
> error it can measure and subtract. Driving straight at a steady speed, an attitude error and a
> sensor bias look exactly alike — it is only when you speed up, slow down and turn that the two
> stop resembling each other and the filter can separate them.
>
> **What can go wrong.** Green gets read as finished. It is not: green means the estimate crossed
> a threshold on its way to converging, and ten minutes later it is better. Nothing tells you
> that, because the light does not change again. So the first data after the light goes green is
> the weakest data of the day, and if that is where the important part of the corridor is, that is
> where the weakest data ends up.
>
> **What good looks like.** Open sky, the full sequence performed even if GAMS is fitted, and the
> first ten minutes spent on something that does not matter much — a drive to the site, a
> throwaway pass, the least critical end of the corridor. It costs five minutes and there is no
> office procedure that buys it back.
