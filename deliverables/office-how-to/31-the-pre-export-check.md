# 31. The Pre-export Check

**One minute. It prevents the most expensive failure in the workflow.**

**[EQUIPMENT]** — the behaviour this guards against is Trimble's, and it is silent: an export of
the unregistered cloud succeeds and produces a valid file. **[PROPOSED · SOP §19.2 · D-36]** —
whether the check is *mandatory*, and whether export may proceed without it, is not yet decided.

### Do

1. In **Project Explorer**, find the scan nodes you are about to export
2. Confirm they sit **beneath the intended registered trajectory**
3. Confirm their stations carry the **`_reg_####`** suffix
4. Screen-capture the tree
5. Decide the **Export timestamps** setting — see below
6. Only then export

*(SOP §19.2)*

### Look at

```
Run 14
  ├── Sbet                             ← NOT this one
  │     └── Run_14_Laser Right (S1)
  └── Reg. Trajectory                  ← this one
        └── Run_14_Laser Right_reg_0001 (S3)
```

### Stop if

> **CAUTION · W-02**
>
> **Registration does not modify the point cloud until Update Scans is performed.**
>
> An operator can complete a registration, obtain good residuals, accept the result, and then
> export point cloud data that still reflects the pre-registration trajectory. **The export
> succeeds. The file is valid. The data is unregistered.**

Stop if the scans sit beneath `Sbet`, or the stations have no `_reg_####`. Go back to §21.

### Export timestamps

> **CAUTION · W-03**
>
> With **Export timestamps** set to **Yes**, Trimble states that *"the exported scans are
> **reprocessed from the raw data**"* rather than being the scans processed with Generate Scans
> *(TBC 23339, 22501)*.
>
> **Which trajectory that reprocessing uses is not stated.** Until this is established, the
> exported data may not be the data that was registered and checked.

**[TESTING · T18]** — an interim posture, not a rule, and it is withdrawn the day T18 is answered
in either direction. Until then: **treat an export with timestamps enabled as unverified against the
checked dataset, and do not enable it on a delivered dataset without a recorded reason**
*(SOP §19.3)*.

> **PARAMETRIX DECISION REQUIRED · D-36**
>
> **Is this confirmation mandatory, and may export be performed without it?** *(SOP §19.2)*

> **TESTING REQUIRED · T18 — the highest-priority test in the register.** Export the same
> registered run twice, timestamps off and on, and compare point geometry.

> **TESTING REQUIRED · T29** — the reliable export-state verification method for each path. How an
> export dialog resolves its selection is not documented.

### Record

The screen capture, and the timestamps setting used.
