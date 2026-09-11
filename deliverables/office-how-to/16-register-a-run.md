# 16. Register a Run

One run, against surveyed control.

### Do

1. In **Project Explorer**, select a run
2. Generate its scans if not already done (§11) — **the command is dimmed without at least one
   generated scan**
3. Import the GCP file (§14)
4. **Mobile Mapping ▸ Processing ▸ Register a Run**
5. Accept the default **Registration Name** (*RunName* Trajectory) or enter one. **This name goes
   to the computed trajectory — it is what you will be identifying months later** (§27)
6. Choose a **Registration Type** — see below
7. Select a GCP under the **Points** node ▸ **Add Selection to Control Points**
8. Set **Use XY**, **Use Z**, **As Check** for that point (§15)
9. Optionally **Activate Limit Box** — hides everything outside a box, "to remove potential
   parasitic points over the target"
10. Optionally **Activate Target-Bundle Adjustment** — see below
11. Select the point in the **Control Points** list. It centres in Plan View and **Point Cloud
    Smart Picking** opens
12. Pick the target, read the residuals, **Validate**
13. Repeat for further points
14. **Compute.** The adjusted trajectory draws **blue**; the original stays **green**
15. **Apply**

*(TBC 22905)*

> **The 30 m rule**
>
> "The distance in a pair of points cannot exceed the allowed maximum distance of **30 meters**"
> *(TBC 22905)*. If a pick is further than that from its GCP, it is not a valid pair — pick a
> feature nearer the control point, or the pairing is refused.

### Look at — Registration Type

| Type | What it does |
|---|---|
| **Global** | A shift of the whole trajectory, **without rotation** |
| **Local** | Interpolates **between** control points |
| **Global, and then Local** | Global first, then Local |

> **CAUTION · W-08**
>
> **Local does not extrapolate.** Trimble states it is *"not for systematic error along the run or
> for adjusting outside the ground control points set"* *(TBC 22905)*.
>
> Beyond the first and last control point the trajectory is not adjusted, **and nothing indicates
> where the adjustment stopped.** Control must bracket the extent you intend to deliver.

> **TESTING REQUIRED · T15**
>
> Which type, when. No selection rule is published, and **Global-then-Local** appears in every
> Trimble screenshot with no guidance attached *(SOP §13.4)*.

### Look at — Target-Bundle Adjustment

**The name reads backwards.** Checked = **250 m** intervals, which is **coarser**. Unchecked =
**70 m** *(TBC 22905)*.

> **TESTING REQUIRED · T9** — test both states against independent checks.

### Expect, after Apply

*(TBC 22905)*

- An **adjusted trajectory node** beneath the run, beside `Sbet`
- A new SBET on disk: **`sbet_<date>_reg_####.out`**, incrementing with each registration
- Picked targets renamed *RunName TrajectoryGCPName*, updated ones carrying a trailing `*`
- Trajectory properties reading `Origin: Registration result`, `Input trajectory: Imported
  trajectory`, and `Registration type:`

**Those four properties and the numbered SBET file are your provenance record** (§27).

### Stop if

- The command is dimmed — you have no generated scan on the run
- You are registering a run that has already been registered. **That stacks adjustments.** Use
  **Edit** (§19)
- The residuals on your check points are not what you expected. Read §20 before doing anything
  about it

### Record

Registration name, type, the trajectory node produced, and the SBET filename **with its `_reg_####`
number**.
