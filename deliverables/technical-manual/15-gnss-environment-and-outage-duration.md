# 15. GNSS Environment and Outage Duration

## 15.1 Duration, not length

The quantity that determines how much a GNSS-hostile stretch costs is **how long the vehicle is
inside it**, not how long it is on the map. The inertial solution drifts as a function of time.

> A 300 m tunnel at 80 km/h is **13 seconds**. The same tunnel at 20 km/h in traffic is nearly a
> **minute**. Same tunnel, materially different problem.

This has a planning consequence that is easy to miss: a hostile stretch in congested traffic is
worse than the same stretch on a clear road, and neither the route length nor the aerial imagery
shows it. The time of day is part of the GNSS assessment.

## 15.2 The 60-second boundary in the specification

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.56)*
>
> Trimble publishes positioning performance at **no outage** and after a **60-second GNSS
> outage**, and nothing in between or beyond:
>
> | Condition | Core / Pro | **Premium — ours** |
> |---|---|---|
> | **No outage** *(all configurations, post-processed with POSPac, with the DMI option)* | X,Y < 0.01 m · Z 0.01 m | X,Y < 0.01 m · Z 0.01 m |
> | **After 60 s GNSS outage** | X,Y **0.12 m** · Z **0.1 m** | X,Y **0.1 m** · Z **0.07 m** |
>
> **Ours is the Premium column: X,Y 0.1 m and Z 0.07 m after a minute of outage.**

Two things in that table are worth dwelling on.

**The no-outage figure is stated with the DMI option.** The configuration is established —
Premium — but **the DMI is not**. The published best-case accuracy assumes a sensor this system
may or may not carry (§9.2, **D-2**). Until that is answered, the sub-centimetre figure is not
one to quote.

**One minute of outage costs an order of magnitude.** Under 1 cm becomes 10–12 cm. That is not a
gentle degradation; it is the difference between a survey-grade deliverable and something else.

> **IMPORTANT**
>
> **Trimble publishes nothing beyond 60 seconds.** A two-minute outage is not "twice as bad as one
> minute" — inertial drift is not linear in time, and beyond the published figure you are
> extrapolating past the manufacturer's stated envelope.
>
> Treat outages materially longer than 60 seconds as a **planning** problem, not a driving
> problem: additional control, planned overlap for LiDAR QC, a DMI if one is available, or a
> different acquisition method for that segment (§27.7).

## 15.3 The environments, and what each does

| Environment | What happens | Typical duration |
|---|---|---|
| **Tunnel, long underpass** | Total loss. The solution is purely inertial | Computable from length and speed |
| **Urban canyon** | Not loss but **multipath** — reflected signals producing plausible, wrong ranges | Sustained over the whole stretch |
| **Heavy canopy** | Intermittent loss and re-acquisition, with poor geometry between | Sustained, and worse when wet |
| **Deep cut, retaining walls** | Reduced sky, degraded geometry, high PDOP | Sustained |
| **Overhead structures, sign gantries** | Brief interruptions | Seconds |

> **Urban canyon is the one that misleads.** A total outage is honest: the filter knows GNSS is
> absent and propagates inertially, and the RMS record says so. Multipath supplies *observations*
> that are wrong, and the filter has no way to know they are wrong. The TBC **Multipath** setting
> exists to tell it how much to distrust them (§17.3), and the appropriate setting for Parametrix's
> normal environments is untested (**T11**).

## 15.4 What can be known before mobilising

Satellite geometry is predictable. The route is known. Both of the things that determine GNSS
quality are therefore knowable in advance, which makes a poor window an avoidable problem rather
than a discovered one.

| Knowable in advance | How |
|---|---|
| Satellite geometry and PDOP through the window | Almanac |
| Which stretches are hostile, and roughly how hostile | Aerial and street-level imagery |
| How long the vehicle will be in each | Length ÷ realistic speed, including traffic |
| Where initialization can be done | Imagery — and **scout two**, because a lot that is fenced, occupied or under trees costs twenty minutes at the worst moment of the day |

> **FIELD TESTING REQUIRED · T31**
>
> No Trimble source relates a *predicted* PDOP or canopy condition to an *achieved* trajectory
> RMS for this system. The relationship is establishable by driving a known route and comparing
> the prediction against the RMS colouring afterwards (§24), and it is the thing that would turn
> GNSS planning from judgement into estimate.

## 15.5 What it changes downstream

A GNSS assessment made before mobilising is not a formality; it determines four later decisions.

| Predicted degradation | Consequence |
|---|---|
| Where the solution will be weak | Where control is worth most, and where check points belong (§22) |
| How long each weak stretch is | Whether the smoother can bridge it, or whether a remedy is needed (§8.3, §27) |
| Whether overlap is available there | Whether LiDAR QC is even possible — it needs overlapping runs (§11.5) |
| Whether any segment is beyond remedy | Whether **mobile mapping is the appropriate acquisition method for that segment at all** (§27.7) |

> That last row is the one people avoid. It is easier to collect a corridor and discover the
> problem in the office than to say before mobilising that a particular 400 m of it should be
> collected another way. The office discovery costs a remobilisation and, sometimes, a conversation
> with the client about accuracy that nobody wants to have.

> **Open Parametrix decision — D-42.** *Base station strategy — own base on project control, VRS,
> RTX, or CORS post-processing, and at what maximum baseline?* This interacts with **D-19**
> (§12.3): **IN-Fusion+ Single Base** requires a local base station, **IN-Fusion+ PP-RTX** does not
> *(TBC 25943)*. The decision determines field logistics on every mission. Stated and tracked in
> the **SOP §8**; see also the master register.

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at what the sky does to the job: which environments hurt, how
> much, and what Trimble actually publishes about it.
>
> **Why it matters.** The number that matters is seconds, not metres. The inertial sensor drifts
> with time, so a tunnel you pass through in thirteen seconds and the same tunnel crawled through
> in a minute are different problems. And the published numbers are stark: under a centimetre with
> good GNSS, ten to twelve centimetres after one minute without it. That is the whole range from a
> survey deliverable to something you would not hand over.
>
> **What can go wrong.** Extrapolating. Trimble publishes a figure at sixty seconds and stops
> there, and the temptation is to assume two minutes is twice as bad. Drift does not work that
> way, and past the published figure you are guessing on the manufacturer's behalf. The other trap
> is urban canyon: an outage at least tells the truth about itself, whereas multipath hands the
> filter wrong measurements that look like right ones.
>
> **What good looks like.** The hostile stretches were identified on imagery before anyone
> mobilised, each one has a duration estimate at a realistic speed for that time of day, and the
> segments that cannot be done well were named before collection rather than discovered after.
> Two initialization sites were scouted, not one.
