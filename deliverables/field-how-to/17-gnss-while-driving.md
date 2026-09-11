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

## 17.4 The published limit

Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
nothing beyond *(MX60 UG Rev B, p.56)*.

**An outage materially longer than 60 seconds is a planning problem, not a driving problem.** If
you meet one that was not planned for, record it and raise it.

## 17.5 Record

Every hostile stretch: entry and exit time, conditions, whether the planned overlap was driven.
