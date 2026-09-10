# APPENDIX E — FIRST DAY TRAINING EXERCISE

For someone who has never operated a mobile mapping system. **Not a production project** —
nothing collected here should be delivered to a client.

**Time:** one field day plus one office half-day.
**Crew:** trainee, an experienced operator, and a driver.

---

## E1. What the trainee should be able to do afterwards

- Set the system up and take it down safely, unsupervised
- Run a mission start to finish, including both initializations
- Read every TMI status indicator and say what it means
- Recognise a bad collection **while still on site**
- Explain why the trajectory determines everything
- Point at real occlusions in their own data and say why they happened

---

## E2. Route

Pick a route with these five features. It does not need to be long — 5 to 10 km is plenty.

| Feature | Why |
|---|---|
| **Open-sky area** for initialization, both ends | The exercise cannot start without it |
| **A straight segment**, ~500 m, driveable both ways | Repeat-pass comparison |
| **An intersection** | Coverage geometry and turn behaviour |
| **A GNSS-challenged stretch** — underpass, tree canopy, or buildings both sides | Watching NAV degrade is the lesson |
| **Something the vehicle cannot see** — behind a barrier, a ditch, a structure | Teaches limits better than any explanation |

> **FIELD TIP**
>
> Choose the GNSS-challenged stretch so the vehicle is under it for **15–45 seconds** at
> collection speed. Long enough to see degradation, short enough to recover.

---

## E3. Field exercise

### Part 1 — Setup (trainee leads, operator supervises)

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Walk the components checklist (Appendix A2) | What "before and after every mission" actually covers |
| ☐ | Mount the Sensor Unit — **two people** | Weight, lock mechanism, why one person cannot do it |
| ☐ | Cable the system, secure everything | Which end is which; why cables are fixed before entering the cabin |
| ☐ | Clean the optics using the correct method | Air first, then a moist — not dripping — cloth |
| ☐ | Measure installation height from the ERP | Where the External Reference Point is, and why ~1 cm matters |
| ☐ | Create a Vehicle Preset | Where the measurement goes and what depends on it |

**Talking point:** ask the trainee what happens if the install height is entered 10 cm too
high and the dust filter is on. *(Answer: the mask reaches the ground and data is lost —
visible immediately in the waterfall view.)*

### Part 2 — Startup

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Power up in the correct order | Why the vehicle starts **first** — 25 A surge |
| ☐ | Watch the LED sequence | Blink ≈ 10 s, then solid green |
| ☐ | Connect the tablet, open TMI | Chrome, `tmi.mx-scan.net`, no software installed |
| ☐ | Find every status button and name its colours | The vocabulary for the rest of the day |
| ☐ | Open Capture Settings; find User Accuracies | What "green" actually means numerically |

**Talking point:** Position RMS defaults to 10 m. Ask why green is not a promise of a
centimetre corridor.

### Part 3 — Initialization (the core lesson)

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Park in open sky; start the mission | Site selection matters |
| ☐ | **Sit still 2–3 minutes** — watch the clock | It feels long. It is not optional |
| ☐ | Note when the blue arrow and UTC time appear | Navigation logging has **already started** |
| ☐ | Drive straight ~20 m — **watch NAV go red → orange** | Seeing the transition is the point |
| ☐ | Vary speed, 2–3 turns — **watch orange → green** | Dynamics create observability |
| ☐ | Open Nav View; identify which parameter converged last | Usually heading. Ask why |
| ☐ | Wait the settling period | Green is the start of convergence, not the end |

**Talking point:** why can roll and pitch be solved sitting still, but not heading?
*(Gravity gives an absolute vertical reference. Nothing gives an absolute heading
reference — it must be inferred from motion, or measured by GAMS.)*

### Part 4 — Collection

| ☐ | Run | Purpose |
|---|---|---|
| ☐ | **Run 1** — straight segment, direction A | Baseline |
| ☐ | **Run 2** — straight segment, direction B | Repeat-pass comparison |
| ☐ | **Run 3** — straight segment, direction A again | Three-pass redundancy |
| ☐ | **Run 4** — through the intersection, both approaches | Coverage geometry |
| ☐ | **Run 5** — the GNSS-challenged stretch, **watching NAV throughout** | The key observation of the day |
| ☐ | **Run 6** — past the feature the vehicle cannot see | Limits |

During every run the trainee monitors and calls out: NAV colour · camera and laser status ·
**thick blue line appearing** · SSD fill.

| ☐ | Extra exercises |
|---|---|
| ☐ | Enter a **Comment** when NAV degrades — see it time-tag |
| ☐ | Open the **waterfall view** while driving |
| ☐ | Adjust panoramic exposure entering and leaving shade |
| ☐ | Perform a **mission re-configuration** to a different capture preset — note no re-initialization is required |

**Talking point:** during Run 5, ask the trainee to predict what the point cloud will look
like there. Check the prediction in the office.

### Part 5 — Ending

| ☐ | Task | Learning |
|---|---|---|
| ☐ | **Review the map before closing** — thick blue line over every run | The last moment a missing run is cheap |
| ☐ | Perform the **full finalize sequence** | Mirror of the start, and why |
| ☐ | Complete Mission, then Shutdown | Never by removing power |
| ☐ | Wait for the light to go out — up to 90 s | Patience is part of the procedure |
| ☐ | Complete the field protocol | What the office will need |
| ☐ | Post-mission safety check | It happens after, not just before |

**Talking point:** what would have been lost by skipping the finalize sequence?
*(The reverse-processing pass loses its anchor. The middle of the mission — already the
weakest part — is then solved from one strong end instead of two.)*

---

## E4. Office exercise

### Part 6 — Data handling

| ☐ | Task | Learning |
|---|---|---|
| ☐ | Remove both SSDs; offload via both Docks | Why USB is never connected with a disk in the Control Unit |
| ☐ | Find navigation data on the SSD 1 copy | Why the two disks are one dataset |
| ☐ | Locate the Mission Report and system log | What exists for troubleshooting |
| ☐ | Verify, **then** back up, **then** clear the disks | The order matters |

### Part 7 — Inspect the results

| ☐ | Inspection | Look for |
|---|---|---|
| ☐ | **Trajectory** — plot reported accuracy along the route | Spikes at the GNSS-challenged stretch. Compare to what was seen live |
| ☐ | **Point cloud, overall** | Coverage against the route driven |
| ☐ | **Repeat passes 1 vs 2 vs 3** — before any registration | How far apart are they? This is the system's internal consistency |
| ☐ | **Cross-section** through the straight segment | Thickness of the road surface across passes |
| ☐ | **The GNSS-challenged stretch** | Is the cloud displaced? Does it recover? |
| ☐ | **Near vs. far from the vehicle** | Density and noise as range increases |
| ☐ | **The intersection** | Coverage gaps at corners |
| ☐ | **Occlusions** — list every one found | Traffic, parked cars, barriers, vegetation |
| ☐ | **The feature that could not be seen** | Confirm it is genuinely absent |
| ☐ | **Imagery** | Exposure, blur, lens cleanliness, coverage |

### Part 8 — Write it up

The trainee writes one page:

1. What was collected, and how
2. Repeat-pass agreement — the actual number
3. Where trajectory quality degraded, and by how much
4. Every occlusion found, and its cause
5. What could not be captured at all, and what would be needed instead
6. What they would do differently

> **IMPORTANT**
>
> Item 5 is the one that matters. A trainee who can look at their own data and say
> "this ditch invert needs conventional survey, and no amount of re-driving will fix it"
> has understood mobile mapping.

---

## E5. Assessment

| ☐ | Competency |
|---|---|
| ☐ | Mounted and dismounted the Sensor Unit safely, two-person |
| ☐ | Measured installation height correctly and entered it |
| ☐ | Powered up in the correct order |
| ☐ | Completed initialization unprompted |
| ☐ | Named every status indicator and its colours |
| ☐ | Monitored correctly during runs, and noticed at least one real event |
| ☐ | Performed the finalize sequence unprompted |
| ☐ | Shut down and offloaded correctly |
| ☐ | Identified occlusions in their own data |
| ☐ | Explained why the trajectory determines everything |
| ☐ | Identified where conventional survey is required |

> **PARAMETRIX DECISION REQUIRED**
>
> Confirm whether this exercise, plus supervised participation in a production collection,
> is sufficient for an operator to work unsupervised — and who signs it off.
>
> *Recommended practice:* both required, signed off by an experienced operator, recorded
> on a qualified-operator list. See Appendix D item 4.

---

## E6. Things to deliberately show, not explain

Five demonstrations worth more than a paragraph each:

1. **Sit through the full static period in silence.** Two to three minutes is longer than
   anyone expects, and that is the lesson.
2. **Watch NAV go red → orange → green in real time.** Nobody forgets seeing it.
3. **Point at the thick blue line** and say "that is your proof you were recording."
4. **Open the repeat passes side by side** and let the trainee see they do not perfectly
   coincide — before registration hides it.
5. **Stand at the feature the vehicle could not see**, then show its absence in the cloud.
