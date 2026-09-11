# Appendix D — First-Week Training Exercise

A structured introduction for someone new to the MX60. It uses a real site and produces a real,
throwaway dataset — nothing here should be delivered to a client.

> **PARAMETRIX DECISION REQUIRED · D-3**
>
> **Is this exercise a requirement before operating alone, and who signs it off?** The exercise is
> offered as a structure; whether it is a qualification gate is not decided.

## D1 · Before the exercise — reading

| Order | Read | Why |
|---|---|---|
| 1 | **§2** Mobile Mapping in Plain Terms | Everything else depends on it |
| 2 | **§1.5** the evidence tags | So the reader knows what is and is not policy |
| 3 | **All In Plain English boxes, end to end** | A complete picture of the workflow in ordinary language |
| 4 | §4 Equipment and Software | What the system is |

> **The In Plain English boxes read end to end are a document in their own right.** A trainee who
> reads only those has a true, if simplified, picture of the whole workflow — deliberately so.

## D2 · Day one — the system

**Goal:** understand what is on the vehicle and why.

| Task | § |
|---|---|
| Identify every component: Sensor Unit, Control Unit, Power Unit, disk, rack, and GAMS/DMI if fitted | 4.1 |
| Locate the two scanners, the 360° camera, the back-down camera | 4.1 |
| **Understand the vehicle frame: +X forward, +Y right, +Z down.** Point at each axis on the vehicle | 7.3 |
| Find where the lever arms are recorded, and read them | 7.3 |
| Connect to TMI in Chrome; identify every status indication | 7.6, App. B |
| Power the system up and down correctly | 7.5, 8.8 |

**Check of understanding:** *Why is Z negative for a sensor mounted above the reference point?*

## D3 · Day two — a mission, done properly

**Goal:** a complete mission with a full initialization and a full closing sequence.

Choose an easy corridor: open sky, light traffic, 20–30 minutes of driving.

| Task | § |
|---|---|
| Complete the preflight checklist — **A2** | 7.9 |
| Initialize: static 2–3 min, straight run, dynamic manoeuvres | 8.2 |
| **Wait out the settling time** and understand why green is not finished | 8.3 |
| Collect the corridor, recording Comments as things happen | 8.4–8.6 |
| **Perform the full closing sequence** | 8.7 |
| Complete the field QC checklist — **A3** | 9 |
| Offload and verify — **A4** | 10.3 |

**Check of understanding:** *Why does the end of the mission matter as much as the start?*

## D4 · Day three — a mission done badly, deliberately

**Goal:** see the failure modes, safely, on data that does not matter.

> **This is the most valuable day of the week.** Mobile mapping failures are invisible in the
> data. The only way to recognise one is to have seen one.

| Deliberate error | What to observe |
|---|---|
| Initialize under tree cover or beside a building | How long the solution takes, or whether it reaches ready at all |
| Record immediately on green, with no settling | Compare the first minutes against the rest, later, in §12 |
| Drive a stretch under heavy canopy | The RMS colouring in §12.4 |
| **Skip the closing sequence** | The trajectory quality at the end of the mission |
| Drive one stretch once, with no overlap | That LiDAR QC and run-to-run are unavailable there |

Collect a second, correct mission over the same corridor for comparison.

**Check of understanding:** *Looking at both point clouds, can you tell which is which without
being told?* — Usually not. That is the point.

## D5 · Day four — the office chain

**Goal:** take the good mission from raw data to a point cloud.

| Task | § | Checklist |
|---|---|---|
| Set the project CRS **before** import | 11.2 | A4 |
| Import; **check covered distance against the field record** | 11.4 | A4 |
| Process the trajectory; **verify the antenna model reads Trimble 112735** | 12.3 | A5 |
| **Read the SBET filename** and say what it indicates | 12.4 | A5 |
| **Colour the trajectory by RMS and find the degraded stretches** | 12.4 | A5 |
| Compare against the day-three bad mission | 12.4 | — |
| Generate scans on one run; inspect; then the mission | 13 | A6 |
| Find the scans in Project Explorer and say which trajectory they are under | 11.3 | — |

**Check of understanding:** *Show the degraded stretches in plan and explain what caused each.*

## D6 · Day five — registration and QC

**Goal:** register to control, and understand what the numbers do and do not prove.

| Task | § | Checklist |
|---|---|---|
| Import control; identify targets in the cloud | 15.2, 15.6 | A8 |
| **Designate control and check points before starting** | 17.4 | A8 |
| Register the mission; read residuals **before** validating each pick | 15.4, 15.6 | A8 |
| Compute, inspect, apply | 15.3 | A8 |
| **Run Update Scans** and find the `_reg_####` suffix | 13.6 | A8 |
| **Set rendering to Scan Color** and inspect in Cutting Plane View | 18.5 | A9 |
| Drag the cutting plane the **full length** of an overlap | 18.5 | A9 |
| Compare check-point residuals against control-point residuals | 17, 18 | A9 |

**Exercises in judgement:**

1. **Register the same run twice instead of using Edit.** Watch the residuals improve. Explain why
   that is not an improvement.
2. **Turn Scan Color off** and look at a known 4 cm misalignment. Explain what you see.
3. **Export before running Update Scans.** Open the file. Explain what is wrong with it and how
   you would have caught it.

**Check of understanding:** *Trimble says good RMS does not prove success but bad RMS proves
failure. Why is that asymmetry true?*

## D7 · Competence check

A trainee should be able to answer these without the document open:

| # | Question | § |
|---|---|---|
| 1 | What is the trajectory, and why does everything depend on it? | 2.1 |
| 2 | Why does the end of a mission matter as much as the start? | 2.2, 8.7 |
| 3 | Why does bad mobile mapping data look fine? | 2.3 |
| 4 | What does green mean in TMI, and what does it not mean? | 8.3 |
| 5 | Name the three registration commands and what constrains each | 15.1 |
| 6 | What does **As Check** do, and why can't every point be one? | 17.2 |
| 7 | Why does a good RMS not prove the registration worked? | 18.1 |
| 8 | What happens if you export without running Update Scans? | 13.6, 22.2 |
| 9 | Why is Cleanup dangerous, and what should happen first? | 21 |
| 10 | Can you tell which trajectory produced a delivered point cloud? | 23.4 |
| 11 | Name two degraded-GNSS remedies that must be arranged **before** driving | 20.3 |
| 12 | Which parts of this SOP are binding Parametrix policy? | 1.5 — **none yet** |

> Question 12 is not a trick. A trainee who answers "all of it" has misread the document, and a
> trainee who can explain why the answer is "none yet" has understood what it is for.
