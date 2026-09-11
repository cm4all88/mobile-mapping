# 14. Why the Closing Sequence Exists

The closing sequence is the most commonly skipped step in mobile mapping. It takes about five
minutes, it cannot be added afterwards, and it is the cheapest quality improvement available in
the entire workflow. This section explains why it exists at all, because a crew that understands
the reason will not skip it and a crew that does not will skip it every time it is raining.

## 14.1 The reason: the trajectory is computed twice

For survey work the navigation filter is run **forward through time and backward through time**,
and the two passes are merged into the SBET (§8.3).

```
   forward pass    ──────────────────────────────────────►
                   good data       GAP        good data
   backward pass   ◄──────────────────────────────────────
                                    ▲
                   bridged from both sides — short, well constrained


   forward pass    ──────────────────────────────────────►
                   good data                      GAP    ✗ end of mission
   backward pass   ◄──────────────────────────────────────
                                                   ▲
                   nothing on this side — the smoother has one anchor, not two
```

A degraded stretch in the **middle** of a mission is bracketed by good data on both sides. The
smoother bridges it from both directions, and the two estimates constrain each other.

A degraded stretch at the **end** has good data on one side only. The forward pass arrives there
already carrying whatever error it accumulated, and there is no backward pass to meet it. The
same is true in reverse at the start of the mission, which is what initialization addresses
(§13).

> **The closing sequence is the reverse pass's anchor.** Without it, the backward pass begins
> from the system's least converged state and propagates that weakness into the end of the
> mission — which is exactly where the smoother has nothing to compensate with.

## 14.2 The sequence

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, p.13; MX60 UG Rev B)*
>
> 1. Finish the last run
> 2. Drive to an open-sky location
> 3. **Dynamic steering manoeuvres**
> 4. **Vary the speed**
> 5. **Drive straight**
> 6. **Remain stationary for 2–3 minutes**, logging static data
> 7. Close the mission in TMI
> 8. Wait for the Control Unit power button light to go out — **up to 90 seconds**

> **Steps 3–6 are the initialization sequence run in reverse order** *(MX60 QSG Rev B, p.13)* —
> manoeuvres, then speed variation, then straight, then static, where the start was static,
> straight, speed variation, manoeuvres (§13.1). That is not a coincidence or a mnemonic. The
> backward pass runs through the data in reverse, so what it encounters first is what the forward
> pass encountered last, and the sequence is arranged so that the backward pass meets the same
> conditioning the forward pass was given.

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing. The manoeuvres have to be inside the logged data to be of
> any use to the smoother.

## 14.3 Why it cannot be added later

There is no office operation that supplies what the closing sequence supplies. The remedies in
§27 all act on data that exists:

| Remedy | Why it does not substitute |
|---|---|
| Reprocess the trajectory | Reprocesses the same observations. The end of the mission is still unconstrained |
| Better base station data | Improves the GNSS side where GNSS was observed. It was not observed after the mission closed |
| LiDAR QC | Needs overlapping scan data at the location concerned (§11) |
| PFIX or registration | Fits the trajectory to surveyed control. Real, but it costs surveyed control at the end of every corridor, and it acts on the fit rather than the solution (§8.5) |

> **CAUTION · W-09**
>
> The post-processed trajectory is computed **forward and backward** and merged. A degraded stretch
> mid-mission is bracketed by good data on both sides. **A degraded stretch at the end has good
> data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

Once the mission is closed the opportunity is gone, and the data at the end of the mission is
permanently weaker than it needed to be. A crew that returns to site the next day cannot append it
— a new mission is a new trajectory.

## 14.4 Where the weakness shows up

The end of a mission is not an abstract place. It is a specific stretch of corridor, and it is
often a significant one, because crews naturally finish where the work finishes.

Three practical consequences, all of them reasons to look at the trajectory before the point
cloud (§24):

- **A check point near each end of the delivered extent is worth more than one in the middle**,
  because the ends are where the smoother had one anchor rather than two (§22)
- **A Local registration stops adjusting at the outermost control point** (§21), so the end of a
  corridor is simultaneously the weakest trajectory and the place registration helps least unless
  control brackets it
- **RMS colouring shows the degradation at the ends directly** — if the last stretch of the
  trajectory is a different colour from the rest, that is the closing sequence talking

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We explained why the end of a mission gets its own five-minute routine,
> and why that routine is the start-of-mission routine performed backwards.
>
> **Why it matters.** The trajectory is computed twice, once forwards through time and once
> backwards, and then the two are blended. Anywhere in the middle of the drive, a bad patch has
> good data on both sides of it and the two passes meet in the middle. At the very end of the
> drive there is no "other side" — the forward pass arrives carrying whatever error it picked up,
> and nothing is coming the other way to correct it. The closing sequence gives the backward pass
> something solid to start from.
>
> **What can go wrong.** Two things, and both are ordinary human behaviour. The crew finishes the
> last run, closes the mission, and then drives to somewhere convenient — but logging stopped when
> the mission closed, so the drive contributed nothing. Or it is raining, the work is done, and
> five minutes of driving in circles feels like nonsense. It is not recoverable afterwards. There
> is no office procedure that buys it back.
>
> **What good looks like.** Finish the last run, drive out to open sky with the mission still
> running, do the turns, vary the speed, drive straight, park for two or three minutes, and only
> then close the mission and wait for the light to go out. Then look at the trajectory's RMS
> colouring in the office: if the last stretch is the same colour as the rest of the job, the
> closing sequence did its job.
