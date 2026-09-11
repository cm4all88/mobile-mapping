# 7. Importing the Mission

### Do

1. Confirm the project CRS is already set (§5)
2. Import the **`<mission>.mxdb`**
3. If you will process the trajectory in house, **import the base station observation file** from
   `Base/` — the **`.YYo`**

### Look at

Project Explorer, under **Mobile Mapping**. Then go straight to §3 and do the seven checks.

### Expect

A mission node, a **Capture Devices** node, and one node per run with an **Sbet** trajectory
beneath it.

### Stop if

- The `.mxdb` will not open. Go back to the copy (§2) — this is the definitive test that the
  transfer worked
- The run count or covered distance disagrees with the field record (§3)

> **CAUTION**
>
> **Import the observation file only.** The `Base/` folder also holds `.YYn` and `.YYg` ephemeris
> files. Trimble states: **"Do not import the ephemeris files into TBC."** *(TBC 25943)*

> **Scans are children of a trajectory, not of a run.** That is why a run can end up with two sets
> of scans that look identical in plan, and it is the structural fact the whole of §27 rests on
> *(Technical Manual §5.3)*.

### Record

Import date, and that the seven intake checks were done.
