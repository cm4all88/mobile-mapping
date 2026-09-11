# 18. Register Run to Run

**Cloud-to-cloud, against a fixed Reference Run. It uses no surveyed control.**

That is the whole point and the whole limitation: it makes two runs agree with each other. It
cannot make them agree with the ground.

### Do

1. Import the missions
2. **Mobile Mapping ▸ Processing ▸ Register Run to Run**
3. Enter a **Registration Name** — "This name will be given to all computed trajectories"
4. Select a pair: one **Run to Adjust**, one **Reference Run**. They may come from the same
   mission or from different missions. Runs list as `<mission ID last two digits> - Run <n>`
5. **Swap Runs** inverts the two
6. **+** adds the pair to the batch
7. In Plan View the **Run to Adjust draws green**, the **Reference Run draws red**
8. Repeat for further pairs. **−** removes; the arrows reorder — **TBC registers the pairs in the
   order given**
9. Set the **Update Scans** option — see below
10. Check **Open Cutting Plane View**
11. **Compute**

*(TBC 25096)*

### Look at — the Results tab

RMS in **tangential, orthogonal and vertical**, every **20 m**, plus `No overlap` where the two
runs do not overlap.

`No overlap` rows are information, not noise. They tell you where the comparison had nothing to
compare.

### Update Scans is inside this command

**This is the only place the two steps merge.** The **Update Scans** checkbox regenerates the Run
to Adjust's scans inline *(TBC 25096)*. Everywhere else, Update Scans is a separate command (§21).

### Expect

- A trajectory beneath the **Run to Adjust**, named `GivenName: Runname_X To Runname_X+1`
- RMS statistics in the Results tab
- A cutting plane per pair, named `MissionID Last Two Digits - Run to Adjust`

### Stop if

- **You have not registered to surveyed control first.** Run-to-run improves *relative* agreement.
  It cannot establish absolute position, and if the Reference Run is itself displaced, run-to-run
  will faithfully propagate that displacement into the run you adjusted
- **You have not re-checked against independent check points afterwards.** The Run to Adjust has
  moved; its residuals against control have changed

> **The order that matters** *(SOP §13.4)*:
>
> 1. Register the mission to surveyed control (§17)
> 2. Assess against independent check points (§20) and visually (§22)
> 3. **Only then** use run-to-run, choosing as Reference Run the pass with the better GNSS
>    conditions and the better residuals
> 4. **Re-check against the independent check points**
>
> Step 4 is the one that gets skipped.

> **CAUTION**
>
> The same principle as §13 applies here, in Trimble's identical wording: **good RMS does not mean
> the registration succeeded; bad RMS means it failed; a visual check is needed** *(TBC 25096)*.

> **TESTING REQUIRED · T24** — how much run overlap is enough.

### Record

Registration name, the pairs and their order, the RMS statistics, and the check-point residuals
**after** the adjustment.
