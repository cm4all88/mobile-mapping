# 8. GNSS/INS Integration

§2 said the trajectory is the job. This section says how the trajectory is computed, because
almost everything the field procedure asks for is an attempt to give this computation what it
needs.

## 8.1 Two sensors that fail in opposite ways

The trajectory is a time series: position (X, Y, Z) and attitude (roll, pitch, heading) at a high
rate, for the whole mission. It is produced by combining two sensor types whose failure modes are
complementary.

| | **GNSS** | **Inertial (IMU)** |
|---|---|---|
| Measures | Absolute position | Change in orientation and velocity |
| Error behaviour | **Bounded but noisy** — it does not drift, but it jumps and can be lost entirely | **Smooth and precise instant to instant, but drifts without limit** over time |
| Fails when | Sky is obstructed — trees, buildings, bridges, tunnels | Always, gradually, by its nature |
| Rate | Low | High |

Neither is adequate alone. Combined, each covers the other's weakness: GNSS anchors the inertial
solution and stops the drift; the IMU carries the solution smoothly through the gaps when GNSS is
degraded or absent.

> **WHY THIS MATTERS**
>
> This is the whole reason mobile mapping works, and also the whole reason it fails quietly. The
> integration is *designed* to keep producing a plausible answer when one of its inputs stops. It
> does not stop, warn, or degrade visibly. It keeps going, and the error grows in a way that is
> smooth, continuous and invisible in the point cloud (§3).

## 8.2 What the filter does with them

The combination is done by a filter that maintains an estimate of the system's state — position,
velocity, attitude, and the sensor errors themselves — and updates it as observations arrive.

Three consequences follow from the way such a filter works, and all three show up in the field
procedure:

**It estimates sensor errors, not just position.** Gyro and accelerometer biases are part of what
the filter solves for. That is why a period of good observations early in the mission improves
the whole mission, and why initialization is a procedure rather than a warm-up.

**Some states are only observable under motion.** Heading, in particular, cannot be separated
from a gyro bias when the vehicle is stationary and moving in a straight line at constant speed.
It becomes observable when the vehicle accelerates, decelerates and turns. This is why
initialization requires manoeuvres and not merely time (§13).

**It weights each observation by an assumed accuracy.** Those assumptions are settings —
multipath level, DMI scale factor standard deviation, GAMS baseline standard deviation (§17.3).
A setting that overstates an input's accuracy pulls the solution toward a measurement it should
have discounted.

## 8.3 Forward, backward, and the smoother

For survey work the filter is run **twice** — once forward through time and once backward — and
the two passes are merged. The merged result is the **Smoothed Best Estimate of Trajectory**,
universally abbreviated **SBET**. The real-time solution computed in the vehicle is the **NAV**,
which is a fallback and not an option for survey deliverables (§17.2).

```
   forward pass    ────────────────────────────────────────────►
                   good data      GAP        good data
   backward pass   ◄────────────────────────────────────────────
                                   ▲
                   the gap is bridged from both sides
```

> **The backward pass is why the end of a mission matters as much as the beginning.**
>
> A gap in the middle of the drive is bracketed by good data on both sides, and the smoother can
> bridge it from both directions. A gap at the **end** has good data on one side only — the
> forward pass arrives at it already degraded, and there is no backward pass to meet it. The same
> is true in reverse at the start.

This is the practical reason the field procedure requires a proper closing sequence (§14), and it
is the single most commonly skipped step in mobile mapping. It is also why the degraded stretches
at the two ends of a trajectory are worse than an identical stretch in the middle, and why
control and check points at the ends are worth more than control in the middle (§22).

## 8.4 What the filter cannot do

Three limits are worth stating explicitly, because a good deal of misplaced confidence comes from
assuming otherwise.

**It cannot create information that was not collected.** A long GNSS outage is bridged by
propagating an inertial solution that is drifting. The smoother makes the bridge as good as the
surrounding data allows; it does not make it as good as observed data.

**It cannot tell you that it struggled, in the point cloud.** The output of a degraded stretch is
a clean, dense, internally consistent cloud in the wrong place (§3.2). The evidence of the
struggle lives in the trajectory's RMS record, not in the points (§24).

**It cannot distinguish a systematic error in its inputs from the truth.** A wrong antenna model,
a mis-keyed base station coordinate, a DMI scale factor for the wrong wheel: each is a consistent
error that the filter will happily absorb and propagate. Nothing in the RMS will look wrong,
because nothing in the internal consistency of the solution *is* wrong (§23).

## 8.5 Where each remedy acts

It helps to see the whole set of remedies as acting at different points on this diagram, because
they are not interchangeable and their costs are different (§27):

| Remedy | Acts on | Needs |
|---|---|---|
| **Better acquisition** | The observations themselves | Planning, and a second mobilisation if discovered late |
| **Reprocessing with better base data** | The GNSS side of the filter | Raw data intact, better corrections available |
| **LiDAR QC** | Adds the scan data as a third aiding sensor | Overlapping runs, a large workstation (§11) |
| **PFIX** | Injects surveyed control into a **second POSPac pass** | POSPac licence, surveyed control, picked targets (§27) |
| **Registration** | Bends the finished trajectory to fit control | Surveyed control, and it acts after the fact (§21) |

> The first four improve the *solution*. Registration improves the *fit*. That distinction matters
> because a registered trajectory has been adjusted to agree with the control it was given, and
> its agreement with that control is therefore no longer evidence of anything (§23).

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked inside the thing that produces the trajectory: two sensors that
> fail in opposite ways, a filter that combines them, and a second pass run backwards through time
> so that gaps are bridged from both ends.
>
> **Why it matters.** Every odd-sounding requirement in the field procedure comes from this. Why
> sit still for a few minutes at the start — because the filter is solving for sensor biases and
> needs quiet observations to do it. Why drive straight, then vary speed, then turn — because
> heading is not observable until the vehicle accelerates and turns. Why finish the mission the
> same way you started it — because the backward pass needs good data at the end, and a gap at the
> end of a drive has good data on one side only.
>
> **What can go wrong.** The filter never stops producing an answer. That is the point of it and
> it is also the trap. Drive under half a kilometre of tree cover and the solution keeps coming,
> smooth and confident, drifting the whole way. Nothing in the point cloud from that stretch looks
> different from the good data on either side of it.
>
> **What good looks like.** Continuous observations, short well-bracketed gaps, a proper start and
> a proper finish. Then the RMS record of the trajectory — which you can look at before any point
> cloud exists (§24) — tells you where the solution was strong and where it was not, which is
> exactly where to put your control and your check points.
