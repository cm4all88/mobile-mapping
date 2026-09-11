# 19. Update Scans — Why Registration Does Not Move Points

Registration produces a **new trajectory**. The point cloud is untouched until this
command is run. That separation is the single most consequential sequencing fact in the
office workflow, and it is why Update Scans has a section of its own.

## 19.1 What it does

> **TRIMBLE DOCUMENTED METHOD** — *(TBC 22638)*

**Update Scans** regenerates scans against a different trajectory. It is how a registration (§21)
reaches the point cloud.

| | **Generate Scans** | **Update Scans** |
|---|---|---|
| Purpose | Create scans from raw data | **Switch existing scans to a different trajectory** |
| Filters pane | Yes | **No** |
| Trajectory choice | The run's current trajectory | **Switches between the imported trajectory and an adjusted one** |

Updated scan stations carry a **`_reg_####`** suffix — for example
`Run_14_Laser Right_reg_0001 (S3)`.

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**
>
> This is the most consequential sequencing fact in the office workflow, and the mistake it
> guards against is invisible: the project contains a registration, the residuals were good, the
> processor moved on — and the delivered cloud never received the adjustment.

Update Scans works in **both directions**: it switches between imported and adjusted, so it is
also the mechanism for reverting.

> **The exception.** **Register Run to Run** has an **Update Scans** checkbox inside the command,
> which regenerates the Run to Adjust's scans inline *(TBC 25096; §21.14)*. That is the only place
> where the two steps merge.



---

> **IN PLAIN LANGUAGE**
>
> **What we just did.** We took a point cloud that had been built on one version of the vehicle's
> path and rebuilt it on a better one. Nothing else in the software does this, and nothing does it
> automatically.
>
> **Why it matters.** Registering a mission improves the *path*. It leaves the points exactly
> where they were. If you stop after registering, the project contains a perfectly good adjustment
> and a point cloud that never received it — and the two look identical in every view.
>
> **What can go wrong.** The failure is silent and it is common: register, read good residuals,
> accept the result, export. The file opens, the extents are right, the residuals in your notes
> were fine, and the client has the version from before the adjustment. Nothing warns you at any
> point in that sequence.
>
> **What good looks like.** After Update Scans the scans sit beneath the registered trajectory in
> Project Explorer and their stations carry a `_reg_####` suffix. If you cannot see that suffix,
> the adjustment has not reached the data. **For the required check before export, see SOP §19;
> for how to verify it, see Office How To §21.**
