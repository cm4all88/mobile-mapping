# 12. Checking the Scans

A first look, on one run, before you commit to the mission.

### Do

1. Open the run's scans in **3D View**
2. Set rendering to **Scan Color** — one colour per scan
3. Look along the corridor, and then at a cross-section

### Look at

| | |
|---|---|
| **Coverage** | Does the cloud run the full length you expected? |
| **Both lasers** | Left and right should both be present |
| **Density at range** | Thinning with distance is normal and expected |
| **Obvious voids** | Occlusion by a vehicle, or a filter that removed more than you meant |
| **The filters' effect** | Compare against an unfiltered generation if you are unsure |

### Expect

A clean, dense cloud. **It will look clean even when the trajectory was poor** — that is the whole
problem with mobile mapping data *(Technical Manual §3.2)*. This check is for coverage and filter
sanity, not for accuracy.

### Stop if

- A laser is missing
- Coverage is materially shorter than the run
- A filter has visibly removed something you need

> **This is not the QC pass.** The QC pass needs control, registration and a cutting plane, and it
> is §22. This is a five-minute sanity check before you spend an hour generating a whole mission.
