# 21. Update Scans — and Confirming It Worked

**The step that is easiest to skip and most expensive to skip.**

### 21.1 Do

1. Select the run or mission
2. **Update Scans**
3. Choose the **registered** trajectory
4. Confirm the result in Project Explorer — see **Look at**

### 21.2 Look at

The scan stations. Updated ones carry a **`_reg_####`** suffix:

```
Run_14_Laser Right_reg_0001 (S3)
```

And their position in the tree: they hang beneath the **registered trajectory**, not beneath
`Sbet`.

### 21.3 Expect

A **second** set of scans, beneath the adjusted trajectory. The original set is still there,
beneath `Sbet`, and both look identical in plan. That is not a duplicate to tidy away — they are
the same raw data computed against two different trajectories *(Technical Manual §5.3)*.

### 21.4 Stop if

- The stations do not carry `_reg_####`
- The scans still sit beneath `Sbet`

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

> **Update Scans works both ways.** It switches between the imported and the adjusted trajectory,
> so it is also how you revert.

> **One exception:** **Register Run to Run** has an **Update Scans** checkbox inside the command
> (§18). That is the only place the two steps merge.

### 21.5 Record

That Update Scans was run, against which trajectory. The pre-export check in §31 confirms it again
before anything leaves.


> **IN PLAIN LANGUAGE**
>
> **What this section means.** Registration computes a new trajectory. **Update Scans is what moves
> the point cloud onto it.**
>
> **Why it matters.** Until this runs, the project contains an adjusted trajectory and an unadjusted
> cloud sitting next to each other. Everything looks finished. Measurements taken from that cloud are
> taken from the unregistered data.
>
> **Remember this.** After Update Scans, the station names gain a suffix — that suffix is how you tell
> by looking that the cloud in front of you is the registered one. Check it before you export.
>
> **If this is skipped.** You deliver the unregistered cloud while believing you delivered the
> registered one. This is the single most common way this workflow goes wrong, and nothing in the
> software warns you.
