# 3. How Error Behaves

This is where a surveyor's intuition needs adjusting, and it is worth being precise. The
three properties below explain most of what is unusual about mobile mapping QC.

## 3.0 Error is not uniform across the dataset

This is where a surveyor's intuition needs adjusting, and it is worth being precise.

**Error is not uniform across the dataset.** It varies along the corridor with GNSS quality, and
it varies within a single scan line with range.

## 3.1 Attitude error multiplies with range

An error in the *position* of the sensor head displaces every point by the same amount. An
error in the *attitude* — which way it was pointing — displaces points by an amount
proportional to how far away they are.

The relationship is simple geometry: lateral displacement is range multiplied by the angular
error in radians. A given attitude error therefore costs five times as much at 50 m as at 10 m.

> This is arithmetic, not a specification. **No Trimble source in the set publishes an attitude
> error budget for the MX60**, so the useful range for a given tolerance has to be established
> from the manufacturer's accuracy statement for the configuration Parametrix owns (§7.3), or by
> test.

> **WHY THIS MATTERS**
>
> This is why *useful range* is a shorter distance than *maximum range*. The scanner can return
> a point at its maximum range; whether that point is good enough to measure from is a
> different question, and the answer depends on the attitude accuracy of the trajectory at that
> instant. Two clouds collected on the same day with the same instrument can have quite
> different useful ranges if one was collected under open sky and the other in an urban canyon.

## 3.2 Error is correlated in time, not scattered

Conventional survey errors tend to be independent — one shot's error tells you little about the
next. Mobile mapping error is **strongly correlated over seconds and minutes**, because it is
dominated by the state of a filter that evolves smoothly.

The practical consequence: a bad stretch of trajectory produces a whole *region* of cloud that
is consistently displaced, not a scatter of bad points. It will look internally consistent and
perfectly clean. **It will simply be in the wrong place**, and only comparison against
independent control will reveal it.

> That is the most important thing in this section. **Mobile mapping data does not look wrong
> when it is wrong.**


## 3.3 Why this changes the QC method

The three properties above have direct consequences, and each has its own section later:

| Property | Consequence | § |
|---|---|---|
| Error is not uniform | A mission is not "good" or "bad" — it has stretches. QC produces a list, not a verdict | 24 |
| Attitude error scales with range | **Useful range is shorter than maximum range**, and varies with the trajectory quality at that instant | 16 |
| Error is correlated in time | **Spot-checking does not work.** A bad stretch shorter than the sampling interval passes every sample | 25 |

---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We looked at how mobile mapping gets things wrong, which is not how a
> total station gets things wrong.
>
> **Why it matters.** Conventional survey errors tend to be independent — one shot's error tells
> you little about the next, so a scatter of bad values stands out. Mobile mapping error is
> dominated by a filter that evolves smoothly over seconds and minutes, so it arrives in **runs of
> consistently displaced data** rather than in scattered bad points.
>
> **What can go wrong.** The consequence people find hardest to accept: **bad mobile mapping data
> does not look bad.** If the trajectory drifted through a tree-lined stretch, the cloud from that
> stretch is still crisp, still dense, still internally consistent — and sitting several
> centimetres from where it should be. There is no noise, no scatter, no visual tell. You find it
> by checking against control you surveyed independently, or you do not find it at all.
>
> **What good looks like.** A dataset where you know *where* the weak stretches are, because you
> looked at the trajectory quality before you ever generated a point cloud (§24), and where
> independent check points in those specific stretches came back in the same range as the ones in
> the open.
