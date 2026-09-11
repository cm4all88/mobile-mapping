# 17. GNSS Considerations While Driving

## 17.1 What to watch

**Navigation status**, continuously. Any degradation from its ready state.

## 17.2 The hostile stretches

Your mission plan identified them (§2). As you reach each one:

1. Note the time entering and leaving — **duration is what matters, not length**
2. Drive it as planned, in the planned direction
3. **Drive the planned overlap**
4. Record the conditions actually encountered

> **Duration, not length.** Inertial drift is a function of time. A 300 m tunnel at 80 km/h is 13
> seconds; the same tunnel at 20 km/h in traffic is nearly a minute *(Technical Manual §15.1)*.

## 17.3 The one that removes office options

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

**If you cannot drive the planned overlap, say so in the field record and say so at handoff.** It
is not recoverable in the office and it is cheap to fix while you are still here.

> **TESTING REQUIRED · T31**
>
> Whether predicted GNSS conditions correlate with achieved trajectory RMS on this system. Until
> that is established, the planning estimate is judgement — **so what you observe and record here
> is the evidence that will settle it** *(SOP §8.3)*.

## 17.4 The published limit

Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
nothing beyond *(MX60 UG Rev B, p.56)*.

**An outage materially longer than 60 seconds is a planning problem, not a driving problem.** If
you meet one that was not planned for, record it and raise it.

## 17.5 Record

Every hostile stretch: entry and exit time, conditions, whether the planned overlap was driven.


> **IN PLAIN LANGUAGE**
>
> **What this section means.** The satellites are the only thing holding the trajectory to the ground.
> Under trees, beside tall buildings and in tunnels, the system is running on its inertial sensors
> alone and drifting.
>
> **Why it matters.** Drift is not random noise that averages out. It grows for as long as the sky is
> blocked, and every point collected during that stretch inherits it. A short gap between good sky is
> bridged well. A long one is not.
>
> **Remember this.** Watch where the sky closes in and note it. If a stretch was bad, say so in a
> Comment as it happens — ten seconds in the vehicle saves an hour of office guesswork later.
>
> **If this is skipped.** The office sees a degraded stretch with no explanation, and has to decide
> between re-collecting it and delivering it without knowing why it is poor.
