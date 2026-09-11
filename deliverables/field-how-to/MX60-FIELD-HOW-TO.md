# MX60 Field How To

**Trimble MX60 · Trimble Mobile Imaging**

> **LIVING DRAFT — INTERNAL REVIEW**
>
> **This document is a living draft for internal Parametrix review, training, testing and workflow
> development.** It is not an issued Parametrix standard, and it does not replace professional
> judgement, project requirements, safety procedures or approved company policy.
>
> **Items marked Parametrix Decision Required, Proposed, Testing Required or Vendor Clarification
> Required are unresolved.** There are a lot of them, and that is deliberate — an open question is
> shown as an open question rather than filled in with a guess.
>
> **Two things follow from that.** Some requirements here **bind anyway** — Trimble's and the
> equipment's, because their authority was never Parametrix's to grant or withhold; they are listed
> with their sources at **SOP §2.4**. And there is **no Parametrix MX60 acceptance standard** to
> claim, because **D-13** is open.

---

## How to review this draft

**This is not primarily a copy-editing exercise.** Typos and awkward sentences are worth reporting,
but they are not what this draft needs. Four questions matter:

| | |
|---|---|
| **1** | **Is anything technically wrong?** |
| **2** | **Is anything impractical in actual field or office use?** |
| **3** | **Is anything presented more strongly than Parametrix has actually decided?** |
| **4** | **What would prevent you from performing the work using these documents?** |

**Question 3 is the one most likely to be missed.** Every statement with procedural force in this
set carries a label saying whose authority it rests on — Trimble's, the equipment's, or
Parametrix's — and **no Parametrix requirement is adopted at this draft.** If something reads as
settled company practice when it is not, that is a defect, and it is the kind this project is least
able to catch on its own.

**Question 4 is the one that finds gaps.** If you could not actually do the work from these
documents — because a step is missing, a decision is open, a tool is not available, or the
instruction assumes something you were never told — say so. A gap is more useful than a correction.

### Who is being asked

Reviewers are identified by role, because each role sees a different failure.

| Role | What this draft most needs from you |
|---|---|
| **Survey leadership and the responsible PLS** | **Question 3.** Where does this overstate what Parametrix has decided? And which of the open decisions are actually yours to make |
| **MX60 field operators** | **Question 2**, in the vehicle. Sequence, timing, what is realistic on a real shift, and anything the Field How To gets wrong about the machine |
| **TBC mobile mapping processors** | **Questions 1 and 2.** Whether the software behaves as described, in the version you are running, and whether the workflow order survives contact with a real project |
| **QA/QC reviewers** | **Question 1**, and the records. Whether the evidence a section asks for is evidence you could actually review, and whether anything is claimed that the evidence does not support |
| **Project managers who may scope or rely on mobile mapping** | **Question 4.** What you would need to know before scoping this work, pricing it, or promising it to a client — and whether you could find it here |
| **Survey staff with conventional experience and limited mobile mapping experience** | **Question 4, and you are the most important reviewer for it.** Where does this assume something nobody explained? An unexplained assumption is invisible to the people who wrote it, and obvious to you |

### How to point at something

**When commenting, identify the document and the section.** For example: **`Field How To §17.3`**, or
**`SOP D-13`**.

Every section and subsection is numbered, and every warning, open decision, test and vendor
question carries an identifier that is the same in all four documents:

| Identifier | Means |
|---|---|
| **§n.n** | A numbered subsection of the document named |
| **W-n** | A warning. Worded identically wherever it appears |
| **D-n** | An open Parametrix decision |
| **Tn** | An open test — something nobody has measured yet |
| **V-n** | An open question for Trimble |

> *"The registration part is confusing"* cannot be acted on. *"`Field How To §17.3` is confusing"* can.

**Comments go to the MX60 Internal Review Log.** That is the working channel until Parametrix
assigns a document owner and a review process under **D-1** — there is no named owner to send them
to, and inventing one would be worse than saying so.

---

## Document control

> **Provisional.** Parametrix's document-control convention is not established (**D-1**). The
> block below is a temporary working scheme for this review only.

### Working Version — internal circulation only

> **This is a temporary working identifier, used only while the set is in internal review.** It is
> deliberately **not** a revision letter or number, so it cannot be mistaken for the Parametrix
> document-control convention that **D-1** will establish. A second circulation package on the same
> date becomes `-b`, then `-c`. When D-1 is answered, this block is replaced by the real one.

| | |
|---|---|
| **Document** | **MX60 Field How To** |
| **Working Version** | `2026-09-11-a` |
| **Status** | **LIVING DRAFT — INTERNAL REVIEW** |
| **Supersedes** | — first circulated draft |
| **Formal revision** | *Not assigned* — **D-1** |
| **Document owner** | *Not assigned* — **D-1** |
| **Approval status** | **Not approved — Living Draft** |
| **Circulated for** | Internal review, training, testing and workflow development |
| **Prepared by** | MX60 mobile mapping documentation project |
| **Review comments** | Record in the **MX60 Internal Review Log** |
| **Set circulated together** | Technical Manual · SOP · Field How To · Office How To, all at Working Version `2026-09-11-a` |

## What this guide is

**It shows you how to run the MX60 in the field.** It is meant to be used in or near the vehicle.

| Question | Document |
|---|---|
| Why does it work this way? | Technical Manual |
| Must I? | SOP |
| **How do I do it in the field?** | **This guide** |
| How do I do it in the office? | Office How To |

**This guide cannot create a requirement.** If it says something must be done and the SOP does not
require it, the SOP governs.

## Abbreviations

Everything else is in **Technical Manual §6**, the authoritative glossary for all four documents.

| | |
|---|---|
| **TMI** | Trimble Mobile Imaging — the field software, in a browser |
| **Sensor Unit** | The roof-mounted head: scanners, cameras, antenna, IMU |
| **Control Unit** | The in-vehicle computer, storage and power management |
| **GAMS** | Second GNSS antenna, for heading. **Optional** |
| **DMI** | Wheel-mounted distance sensor. **Optional** |
| **Mission** | One deployment. **Run** — one continuous stretch of collection within it |

## Before anything else

**Appendix E is the quick card.** Ten things that cost the most if missed. If you read one page of
this guide, read that one.

## Visual identity

Parametrix Brand Guide v6, November 2023. Document accent: **Future Green**.

---

# 1. How to Use This Guide

## 1.1 Shape

Short numbered steps. A **Why this matters** line only where the reason changes what you do. No
theory — that is the Technical Manual, and every reference points there.

**Every subsection is numbered.** When reporting a problem with this guide, cite the number —
**Field How To §12.3** — together with any **W-**, **D-**, **T** or **V-** identifier on the
statement you mean. Front matter explains why.

## 1.2 Order

§2 to §11 get the system on the vehicle and running. §12 to §14 initialize it. §15 to §20 collect.
§21 to §26 finish, check and hand over. §27 is what to check when something is wrong.

## 1.3 The five that cost the most

All five are silent, and four of them cannot be fixed from the office.

| | | § |
|---|---|---|
| 1 | **An aiding sensor not activated in Vehicle Settings logs nothing** — even if it is installed and wired | 10 |
| 2 | **Green is not finished.** Allow the settling time before recording anything that matters | 14 |
| 3 | **The closing sequence cannot be added later** | 21 |
| 4 | **Missed overlap removes office remedies** — and nothing warns you | 17 |
| 5 | **Do not clear a disk until the office confirms a verified copy** | 25 |

Full card: **Appendix E**.

## 1.4 If something is not covered here

**Stop and ask.** Do not improvise on the vehicle.

Three things you may always do without asking first:

| | |
|---|---|
| **Stand down** on safety or data-quality grounds · **[SOP §9.5 · PROPOSED]** | The decision and its reason are recorded. **This is not conditional on you being right.** The authority is proposed, not adopted — but nobody has to wait for D-3 to stop an unsafe job |
| **Record a comment** about anything unusual | §19 |
| **Re-drive a run while you are still on site** | §24 |

## 1.5 Who is telling you — the authority key

**This guide cannot require anything.** Everything in it is somebody else's instruction, and the
marker says whose. That matters because the SOP is not adopted: a Parametrix practice is a
recommendation today, while **a Trimble instruction and an equipment limit bind regardless.**

| Marker | Who says so | Force today |
|---|---|---|
| **[TRIMBLE]** | Trimble states it as a requirement, in the cited manual page or topic | **Binding.** Does not wait on a Parametrix decision |
| **[TRIMBLE METHOD]** | Trimble documents the method, but does not state it as a requirement | **Strong advice.** The method is Trimble's; the obligation is not |
| **[EQUIPMENT]** | A hardware or safety limit, with manufacturer evidence | **Binding.** It is a fact about the machine |
| **[SOP §n]** | A Parametrix requirement, at that clause | As strong as that clause — check its state |
| **[PROPOSED]** | Recommended by this project | **Not company policy.** Do it unless told otherwise, and say so if you cannot |
| **[TESTING · Tn]** | Depends on a result nobody has yet | An interim posture, not a rule |
| **[DECISION · D-n]** | Parametrix has not decided | **Ask.** Do not improvise a standing rule |

> **A marker never softens a Trimble instruction.** *Do not clear the disk* is as firm on day one
> as it will be after the SOP is adopted, because Trimble and the physics of a wiped disk are not
> waiting for a meeting.

> **[TRIMBLE] and [TRIMBLE METHOD] are not the same thing.** Trimble writes *"Navigation alignment
> must be done first"* — that is **[TRIMBLE]**. It heads its in-field list *"Proposal of a checklist
> for system operation"* — that is **[TRIMBLE METHOD]**. This guide does not promote the second into
> the first. A documented method is the best method anyone has published, and it is still not a
> manufacturer requirement.

## 1.6 Where a decision is open

A **PARAMETRIX DECISION REQUIRED** marker means the SOP has identified a requirement whose answer
is not set. Where this guide suggests what to do meanwhile, it is a suggestion and not a Parametrix
standard.

## 1.7 The field record

**No software produces it.** Conditions, incidents, what was not collected and why — if you do not
write it down, nothing else will. §26 and Appendix C.

---

# 2. Before You Leave the Yard

1. **Read the mission plan.** Route, passes and their directions, planned overlap, GNSS-hostile
   stretches, and the two initialization locations *(SOP §8)*
2. Confirm the **primary and backup initialization locations** are scouted, not assumed
3. Confirm the **data disk** is the intended one and has space (§11)
4. Confirm **calibration currency** — when was the system last calibrated? *(SOP §15.2)*
5. Take the **field record form** (Appendix C) and this guide
6. Confirm the vehicle's power supply is sound (§6)

> **Why this matters — the two initialization locations**
>
> Discovering the chosen lot is fenced, occupied or under trees costs twenty minutes at the worst
> moment of the day. Scout two on imagery before mobilising *(Technical Manual §15.4)*.

> **PARAMETRIX DECISION REQUIRED · D-19, D-42**
>
> **Base station strategy** — whether a local base must be occupied for this mission depends on
> whether Parametrix works in **IN-Fusion+ Single Base** or **PP-RTX**, which is not decided
> *(SOP §6.2, §8.5)*. **Check the mission plan for this job.**

### Stop if

- There is no mission plan
- The calibration date cannot be established
- The segments mobile mapping is **not** expected to serve have not been identified
  *(SOP §8.6)*

---

# 3. Equipment Inspection

## 3.1 Look at

| Item | Looking for |
|---|---|
| **Optical surfaces** — scanner windows, camera dome | Rain, dust, insects, smears, scratches. **They export as defects you cannot fix** |
| **Cables** | Chafe, cuts, bent pins, strain at the connector |
| **Mounting rack and fixings** | Anything loose. Check against the tightening method in the rack's own user guide |
| **Sensor Unit seating** | That it sits as it did when the lever arms were measured |
| **GAMS antenna**, if fitted | Secure, and the same antenna type as the primary *(MX60 UG Rev B, p.68)* |
| **DMI**, if fitted | Secure on a **non-steering** wheel |
| **Data disk** | Present, correct, seated |

## 3.2 Clean the optics before every mission

A smear on the dome is in every image of the day. It is thirty seconds now.

## 3.3 Stop if

- An optical surface cannot be cleaned properly
- A cable is damaged
- **Anything about the Sensor Unit's seating is in doubt.** A doubt about seating is a doubt about
  the lever arms, and a lever arm error is systematic and invisible *(Technical Manual §7.6)*

> **The Control Unit and Power Unit are IP30 — not waterproof** *(MX60 UG Rev B, p.53)*. They live
> inside the vehicle.

---

# 4. Mounting the Sensor Unit

> **CAUTION**
>
> **Two people are required.** The Sensor Unit weighs **24–28 kg** depending on configuration
> *(MX60 UG Rev B)*. It is awkward, it is expensive, and it is lifted above head height.

## 4.1 Do

1. Two people. Plan the lift before starting it
2. Seat the unit on the rack in the orientation it was installed and measured in
3. Secure it per the rack's documented tightening method and sequence
4. Connect the Sensor Unit cable — **5 m** *(MX60 UG Rev B)*
5. Confirm the unit is seated exactly as it was when the lever arms were measured

## 4.2 Why this matters

The lever arms — the fixed distances between sensors — are **measured, not computed**. The
calibration solves angles only, so a seating change cannot be calibrated out later. It becomes a
systematic error nobody will attribute to its real cause *(Technical Manual §7.6)*.

> **CAUTION**
>
> **Changing the rack, the roof bars, the vehicle, or the Sensor Unit's position on the rack
> invalidates the lever arms and may invalidate the calibration.** If any of those has changed,
> say so before the mission rather than after it.

## 4.3 Stop if

- You are alone
- The seating is not repeatable, or the rack fixings are not as documented

> **PARAMETRIX DECISION REQUIRED · D-26**
>
> **Does removing and refitting the Sensor Unit count as disturbing the calibration?** If the unit
> comes off between jobs, the answer decides whether calibration is annual or per-mobilisation
> *(SOP §15.2)*.

> **PARAMETRIX DECISION REQUIRED · D-46**
>
> **Where are the lever arms, the Vehicle Preset and the installation configuration recorded, and
> who verifies them?** *(SOP §9.1)*

---

# 5. Connections and Cable Routing

## 5.1 Do

1. Route cables so they cannot **chafe, catch, or be closed in a door**
2. Secure them — a cable that moves will eventually fail at the connector
3. Sensor Unit run: **5 m**. Control Unit run: about **3 m** *(MX60 UG Rev B)*
4. Confirm every connector is fully seated
5. Keep the Control Unit and Power Unit **inside the vehicle** — they are IP30, not waterproof

## 5.2 Stop if

> **CAUTION**
>
> **Never connect the USB cable while the exchangeable data disk is inside the Control Unit.**
> Remove the disk first *(MX60 UG Rev B, p.10)*.

Also stop if a connector will not seat fully, or a cable run cannot be secured away from a door
seal or a moving part.

---

# 6. Power System Checks

## 6.1 The numbers

| | Value | Source |
|---|---|---|
| Input voltage | **12–16 V DC** | MX60 UG Rev B |
| Current at startup | **25 A at 12.8 V** (320 W) | MX60 UG Rev B |
| Current in operation | 12 A (160 W) | MX60 UG Rev B |
| **Supply rating needed** | **30 A or more** | MX60 QSG Rev B, p.4 |
| Direct-connection fuse | **35 A**, close to the battery | MX60 UG Rev B |

## 6.2 Do

1. Confirm the supply is rated and fused as above
2. Confirm the battery is in good condition and charged
3. **Keep the engine running while the system is operating**
4. Confirm the auxiliary battery, if fitted, is healthy

> **An auxiliary battery as a backup power source is recommended** *(MX60 QSG Rev B, p.4)*.

## 6.3 Why this matters

A supply interruption mid-mission does not merely stop collection. **It ends the run, and takes
the closing sequence with it** — which is the one thing that cannot be added afterwards (§21).

## 6.4 Stop if

- The battery is marginal. **A mission that starts on a marginal battery will end unexpectedly**
- The supply is not rated for 30 A, or is not properly fused

---

# 7. Battery Protect

> **CAUTION · W-11**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*:
>
> | Event | Trigger |
> |---|---|
> | Audible warning | Supply below **10.5 V for longer than 12 seconds** |
> | Power cut | Supply below **10.5 V for more than 90 seconds** |
> | Recovery | Voltage rises above **12.0 V within that 90 seconds** |
>
> The alarm leaves roughly **78 seconds** to restore charge — that figure is the arithmetic of the
> two sourced timings, not a separately published one.
>
> **An interrupted run loses the closing sequence with it.**

## 7.1 If the alarm sounds

1. **Restore charge immediately.** Engine speed up, load off
2. Do not continue collecting while you work out what happened
3. Record it in the field record — time, what you were doing, what you did

## 7.2 If it sounds during preflight

**Fix it before doing anything else.** Do not start a mission on a battery that has already
tripped the warning.

## 7.3 If power cut mid-run

| | |
|---|---|
| The run is ended | It has no closing sequence |
| The mission may be incomplete | Check what was written (§23) |
| **This is a re-drive decision, on site** | §24 |

## 7.4 Treat the alarm as an instruction

Not as information. You have about a minute and a quarter.

---

# 8. Starting the System

## 8.1 Do

1. **Vehicle ignition on**
2. Confirm the power supply is live
3. Press and **hold the Control Unit power button for at least 15 seconds**
4. Sensor Unit and Control Unit LEDs **blink for about 10 seconds**
5. **Wait for the system to reach a ready state** before connecting to TMI

*(MX60 UG Rev B; MX60 QSG Rev B)*

## 8.2 Expect

Blinking LEDs settling to a steady state. Give it time — a firmware update can take **up to six
minutes** to complete on power-up *(TMI UG Rev L, p.49)*.

## 8.3 Stop if

- The LEDs do not settle
- The Battery Protect alarm sounds (§7)
- The system does not reach a ready state

> **Do not remove power or the data disk while the power button light is on** (§22).

---

# 9. Connecting to TMI

## 9.1 Do

1. Open **Chrome**
2. Go to **`http://tmi.mx-scan.net`** — the capture interface
3. Administration, if needed: **`http://admin.mx-scan.net`**

*(TMI UG Rev L)*

TMI is served by the Control Unit. It needs no internet access, and the addresses resolve only on
the Control Unit's network.

## 9.2 The status colours

**Learn these before driving. This interface is your only view of system health.**

| Colour | Meaning |
|---|---|
| **Green** | The parameter meets its accuracy threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Red** | Not meeting threshold |

> **CAUTION**
>
> **Orange permits recording. Survey-grade work does not.**
>
> TMI will let a mission be recorded on an orange navigation status. Whether Parametrix work may be
> collected on anything other than green is **D-3 / D-49** — an operator decision rule that has not
> been made. **Until it is, treat orange as a stop-and-assess condition and record it.**

## 9.3 Confirm every sensor is present

Check the device list. Every camera and both lasers.

> **A sensor absent from the list is a cable, power or sensor fault.** A run collected with a
> sensor down is incomplete, and you will not know which part of the deliverable is missing until
> the office opens it.

## 9.4 Stop if

- A sensor is not listed
- TMI will not load. Check that you are on the Control Unit's network and using Chrome

> **From TBC 2026.10 the office side requires two-step verification for Trimble ID.** That is an
> office concern, not a field one, but it is worth knowing if you are asked.

Full status reference: **Appendix D**.

---

# 10. Mission Setup in TMI

## 10.1 Vehicle settings

> **CAUTION · [TRIMBLE]**
>
> **If an aiding navigation sensor is not activated in Vehicle Settings, its data will NOT be
> logged — even though all connections may have been made properly** *(TMI UG Rev L, p.21)*.
>
> This is Trimble stating how the system behaves. It is not a rule anybody can relax.
>
> This applies to **DMI and GAMS**. The hardware can be correctly installed, wired and present, and
> log nothing. There is no cabling fault to find and nothing looks wrong.

1. Open **Vehicle Settings**
2. **Confirm DMI is activated**, if fitted — and that its lever arm and **mounting position, left
   or right**, are set
3. **Confirm GAMS is activated**, if fitted — and that its lever arm is set
4. Confirm the **Install Height** preset is the one for this vehicle

> **The mounting side matters in the office.** The DMI's scale factor sign depends on it, and the
> processor cannot see the vehicle. **Record which side it is on** *(Technical Manual §9.2)*.

## 10.2 Capture settings

> **Expect either presentation, and record which you saw.**
>
> | Source | What the operator sees |
> |---|---|
> | MX60 Quick Start Guide Rev B, p.10 | Two controls — **Measurement Prog** `[500 kHz, 1000 kHz]` and **Line Speed** `[120 Hz, 200 Hz]` |
> | TMI User Guide Rev L, p.29 | A single combined **Laser Mode** |
>
> Which you get depends on the TMI version installed, which has not been confirmed
> *(**V-2**, `CONFLICT-005`)*.

| Setting | Range | Note |
|---|---|---|
| **Laser rate** | 500 / 1000 kHz per scanner | **The higher rate costs range**: 120 m instead of 150 m |
| **Line speed** | 120 / 200 Hz per scanner | More profiles per second = closer spacing along the corridor |
| **Lateral Range Limit** | 5–50 m | **V-7** — whether it affects accuracy or is purely a data-volume control is not documented |
| **Dust filter** | on/off | For **unpaved roads and mine sites** *(Product Bulletin, January 2025)* |

> The measurements-per-second values TMI displays are **rounded** *(TMI UG Rev L, pp.28–29)*.

> **The specification sheet's 1000/2000 kHz and 240/400 Hz are system totals across both
> scanners.** TMI uses the per-scanner numbering above. Do not go looking for 2000 kHz on the
> screen.

> **TESTING REQUIRED · T12**
>
> **The DMI scale factor's 5 % default assumes somebody measured the wheel.** If the value came
> from a manual for a nominal tyre, the office is weighting the DMI on an unverified claim. **If
> you know whether this wheel was measured, record it** *(SOP §13.1)*.

## 10.3 Record

Capture settings used, **and which presentation you saw**. Field record, Appendix C.

## 10.4 Stop if

- A fitted aiding sensor cannot be activated
- You cannot establish which capture settings are in force

---

# 11. Disk Check

## 11.1 Do

1. Confirm the exchangeable data disk is **installed and seated**
2. Confirm it is **the intended disk**
3. Confirm **free space** is sufficient for the planned mission, with margin

## 11.2 Stop if

> **CAUTION**
>
> **Never connect the USB cable while the exchangeable data disk is inside the Control Unit.**
> Remove the disk first *(MX60 UG Rev B, p.10)*.

Also stop if free space is marginal.

> **Why this matters**
>
> **A mission that fills the disk mid-corridor ends the run and takes the closing sequence with
> it** (§21). Storage is 2 × 4 TB removable SSD *(MX60 Spec Sheet)*; running out is a planning
> failure, not an accident.

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **What free-space margin is required before a mission may start?** *(SOP §9.4)*

## 11.3 Never reuse a disk on a promise

**Do not clear a disk because someone said the data was copied.** §25 has the rule: not until the
office confirms a verified copy exists in two places and the `.mxdb` opens.

---

# 12. Navigation Initialization

**The sequence, in order.** Do not compress it.

## 12.1 Do

1. **Park in an open-sky area** with good GNSS visibility, away from high buildings and canopy
2. **Start the mission** in TMI
3. **Log 2–3 minutes of static data** before driving
4. **Drive straight ahead for approximately 20 m**, with no larger steering. The navigation status
   switches on completing this
5. **Drive straight at varying speed — accelerate then decelerate — and perform dynamic steering
   manoeuvres.** An example profile: **0 → 50 → 20 → 50 → 20 km/h**
6. Watch the navigation status progress **red → orange → green**
7. **Allow up to 10 further minutes of settling before logging data that matters**

**[TRIMBLE METHOD]** *(MX60 QSG Rev B, §5.3 p.11; §6 p.14)* — steps 1–7 are Trimble's documented
sequence. Trimble writes *"should be started in a static mode"* and heads its checklist *"Proposal
of a checklist for system operation"*, so the sequence is documented method, not a manufacturer
requirement. **Do it anyway** — nobody has published a better one, and the office cannot repair a
bad initialization.

**[TRIMBLE]** *(MX60 QSG Rev B, §5.3 p.11)* — one part of it is a requirement and the system
enforces it: *"Navigation alignment must be done first before data logging is allowed!"* You
cannot log through step 6 whether you want to or not.

**Step 7 is the one nothing enforces** (§14.2), and it is advice in Trimble's own words —
*"it is advised to add some time (up to 10 minutes)"*. It is also where most of the value is.

## 12.2 What each step is doing

One line each. Full explanation: **Technical Manual §13**.

| Step | Doing |
|---|---|
| **Static period** | Parked, the system's true speed is zero, so anything the motion sensors report is pure error it can measure and remove |
| **Straight 20 m** | Initial heading from the direction of travel. This is what the status is waiting on |
| **Varying speed** | Separates an accelerometer bias from a pitch error |
| **Dynamic steering** | **Heading** — the hardest component, and what the turns are for |

## 12.3 Stop if

- **Open sky is not available at the start point.** Drive to open sky *before starting the
  mission*, not after
- The status will not progress. See §14 and Appendix D — ask TMI **which** parameter is holding it

## 12.4 The system enforces one part of this, and not the other

**Navigation alignment must complete before data logging is allowed** — the system enforces that
*(MX60 QSG Rev B)*.

**It does not enforce step 7.** That one is yours (§14).

---

# 13. GAMS Considerations

**Only if GAMS is fitted.** Whether it is on this system is an open question — **D-2** *(SOP §6.4)*.

## 13.1 What it changes

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 UG Rev B, p.67)*
>
> GAMS **reduces initialization time and eliminates the special driving manoeuvres** otherwise
> required.

> **Read the second half.** By implication, **the manoeuvres are required when GAMS is not
> fitted.** Trimble says the same from the other direction: **straight driving is more important
> if a GAMS antenna is not used** *(MX60 QSG Rev B, p.12)*.

## 13.2 What to do

**Perform the full sequence either way** (§12). It costs a few minutes, the static period does work
GAMS does not replace, and whether this system has GAMS is not yet established.

## 13.3 If GAMS is fitted — the installation requirements

| | Value |
|---|---|
| Offset accuracy, **collection only** | 10 cm or better |
| Offset accuracy, **post-processing** | **A few millimetres** |
| Minimum baseline | **2.0 m** between primary and secondary antennas |
| Antenna matching | **Must be the same type as the primary.** Do not mix |
| Measured to | The **L1 antenna phase centre** of the secondary antenna |
| **Re-measure** | **Every time GAMS is re-installed on the roof for a new mission** |

*(MX60 UG Rev B, pp.67–68)*

> **All Parametrix mobile mapping is post-processed, so the requirement is millimetres, not
> centimetres.** An offset good enough to navigate with is not good enough to survey with.

## 13.4 Stop if

- GAMS is fitted but not activated in Vehicle Settings (§10.1) — **it will log nothing**
- The published rack corner offsets are being used and you are not certain which rack is fitted.
  Those offsets apply to the **standard Trimble Roof Rack only** *(MX60 UG Rev B, p.68)*

> **VENDOR CLARIFICATION REQUIRED · V-5**
>
> The **Trimble GAMS Antenna Kit Installation & Operation Manual** is not held. It is needed to
> complete the installation procedure if GAMS is fitted.

---

# 14. Reading Navigation Status

## 14.1 The colours

| Colour | Meaning |
|---|---|
| **Red** | Not meeting threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Green** | The parameter meets its accuracy threshold |

## 14.2 What green does not mean

> **IMPORTANT · [TRIMBLE]**
>
> **Green means the solution met the accuracy thresholds — not that it has finished converging.**
> That is why Trimble asks for **up to ten more minutes** before recording anything that matters
> *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day. Do not spend it on
> the most important part of the corridor.**

The light does not change again when the estimate improves, so nothing tells you. This is the one
part of initialization the system does not enforce, and therefore the part that gets skipped.

## 14.3 If it will not reach green

**Ask TMI which parameter is holding it.** The remedies are different and waiting helps neither.

| Holding | Likely cause | Do |
|---|---|---|
| **Heading** | Not enough dynamic manoeuvres, or no GAMS | **More turns and speed changes** |
| **Position** | Poor sky view | **Move the vehicle** to genuinely open sky |
| **Attitude** | Not enough motion variety | Complete the full manoeuvre profile |

## 14.4 Orange

**Orange permits recording. Survey-grade work does not.**

Until **D-3 / D-49** is decided, treat orange as a **stop-and-assess** condition: work out why,
record it, and decide deliberately rather than by default.

## 14.5 Record

The time green was reached, and the time recording of significant data began. The gap between them
is the settling time, and it is the evidence that §14.2 was respected.

---

# 15. Recording Runs

## 15.1 Do

1. Start a run at the start of a continuous stretch of collection
2. Stop it at the end of that stretch
3. Start the next one
4. Note each run's start and end, and anything that happened during it, in the field record

Each run becomes a **Run** node in the office.

## 15.2 Minimum mission time

> **TRIMBLE DOCUMENTED METHOD**
>
> **Minimum mission time: 30 minutes** *(MX60 QSG Rev B, pp.13–14)*.

> **A short corridor does not excuse a short mission.** If the collection itself is twelve minutes,
> **keep the system running and logging navigation data to reach thirty**. The trajectory solution
> improves with observation time, and closing early gives the office less to work with.

## 15.3 Drive every planned pass, in the planned direction

Direction matters. A second pass in the opposite direction fixes the far side of the corridor
better than any setting change, because it turns grazing incidence into direct incidence
*(Technical Manual §16.3)*.

> **PARAMETRIX DECISION REQUIRED · D-41 · blocks operation**
>
> **How many passes, in what pattern, by roadway type?** The mission plan states it for this job;
> the standing rule does not exist yet *(SOP §8.2)*.

## 15.4 Stop if

- Navigation status will not hold
- A sensor has stopped reporting
- Storage will not last the corridor
- The battery is cycling into protection

> **You have the authority to stand down** *(SOP §9.5)*. A mission abandoned after twenty minutes
> costs twenty minutes. A mission completed on a degraded solution costs the office days and may
> cost a return visit.

---

# 16. Driving Practices

## 16.1 Speed

| | Value | Authority |
|---|---|---|
| **Recommended maximum with the system operating** | **80 km/h (50 mph)** | **[TRIMBLE]** *(MX60 UG Rev B)* — Trimble's recommendation, not a Parametrix rule |
| Absolute maximum, operating or not | 110 km/h (68 mph) | **[EQUIPMENT]** *(MX60 UG Rev B)* |

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **What collection speed, by deliverable type?** Trimble publishes a recommended maximum and an
> absolute maximum and **no guidance relating speed to deliverable quality** *(SOP §9.4)*.
>
> *For consideration, not adopted:* collect at or near prevailing traffic speed up to 80 km/h,
> reducing where point density requires it.
>
> **[TRIMBLE METHOD] Trimble recommends not exceeding 80 km/h with the system operating.** That
> recommendation is not waiting on D-43 and it stands today — but it is Trimble's *recommended*
> maximum, not a stated limit, and this guide does not upgrade it into one. **110 km/h is the
> limit**, and that one is **[EQUIPMENT]**.

## 16.2 Smoothness

**Drive smoothly.** Sudden braking and sharp manoeuvres stress the inertial solution unnecessarily.

## 16.3 Lane choice

Choose the lane with the best line of sight to the features being collected.

> **The far side of a truck is not collected at all.** Occlusion is permanent — no office step
> recovers it.

## 16.4 Heat

> **CAUTION**
>
> **Direct sun with the vehicle stationary or driving below 10 km/h is outside the rated operating
> envelope** *(MX60 UG Rev B, p.53)*.
>
> Extended idling in direct sun — at a signal, in a queue, waiting for traffic control — is a real
> risk on a hot day.

## 16.5 Turning round

Plan turnarounds where the vehicle can complete them **without reversing under the sensor's
collection**. Where a turn must happen inside the corridor, **note it in the field record** so the
office knows why the trajectory does what it does there.

## 16.6 Record

Anything that changes what was collected: a lane you could not use, a queue you sat in, a
turnaround inside the corridor.

---

# 17. GNSS Considerations While Driving

## 17.1 What to watch

**Navigation status**, continuously. Any degradation from its ready state.

## 17.2 The hostile stretches

Your mission plan identified them (§2). As you reach each one:

1. Note the time entering and leaving — **duration is what matters, not length**
2. Drive it as planned, in the planned direction
3. **Drive the planned overlap**
4. Record the conditions actually encountered

> **Duration, not length.** Inertial drift is a function of time. A 300 m tunnel at 80 km/h is 13
> seconds; the same tunnel at 20 km/h in traffic is nearly a minute *(Technical Manual §15.1)*.

## 17.3 The one that removes office options

> **CAUTION · W-10**
>
> If a GNSS-hostile stretch planned for two passes receives one, **both LiDAR QC and run-to-run
> registration become unavailable** for that stretch. There is no software warning, and no way to
> tell afterwards except by looking at what is there.

**If you cannot drive the planned overlap, say so in the field record and say so at handoff.** It
is not recoverable in the office and it is cheap to fix while you are still here.

> **TESTING REQUIRED · T31**
>
> Whether predicted GNSS conditions correlate with achieved trajectory RMS on this system. Until
> that is established, the planning estimate is judgement — **so what you observe and record here
> is the evidence that will settle it** *(SOP §8.3)*.

## 17.4 The published limit

Trimble publishes positioning performance at **no outage** and after a **60-second outage**, and
nothing beyond *(MX60 UG Rev B, p.56)*.

**An outage materially longer than 60 seconds is a planning problem, not a driving problem.** If
you meet one that was not planned for, record it and raise it.

## 17.5 Record

Every hostile stretch: entry and exit time, conditions, whether the planned overlap was driven.

---

# 18. Field QC Indicators

## 18.1 What the field can and cannot confirm

| Can confirm here | Cannot confirm until the office |
|---|---|
| The mission recorded and closed | **Post-processed trajectory quality** |
| All planned runs exist | **Accuracy against control** |
| Data written to disk and readable | Whether GNSS degradation was bridged adequately |
| **Coverage — was the corridor driven** | Point density at the achieved standoff |
| Sensors reported present throughout | Imagery detail sufficiency |
| Gross imagery problems — obstruction, contamination | Colour fringing, boresight symptoms |
| Free space and disk health | Anything requiring the trajectory |

> **IMPORTANT**
>
> **Nothing available in the field confirms the data is of survey quality.** The field checks
> confirm that the data **exists, is complete, and is readable**. That is genuinely worth
> confirming before leaving — and it is not the same thing.

## 18.2 Watch, while driving

| Watch | For |
|---|---|
| **Navigation status** | Any degradation from the ready state |
| **Storage** | Remaining capacity against remaining corridor |
| **Sensor status** | A camera or laser that has stopped |
| **Audible alarm** | **Battery Protect** (§7) |

## 18.3 Recognising a bad collection before the day is wasted

Stop and reassess if any of these is true:

- Navigation status will not hold
- A sensor has stopped reporting
- Storage will not last the corridor
- The battery is cycling into protection
- Conditions have moved outside the go/no-go rule

> **The operator has authority to stand down** *(SOP §9.5)*.

---

# 19. Using Comments

## 19.1 Do

**Use TMI's Comments feature as things happen.** Not afterwards.

Examples worth recording:

- *"heavy canopy from the bridge"*
- *"stopped 4 min, traffic control"*
- *"parked truck occluding the north side"*
- *"could not drive second pass, road closed"*
- *"hard rain from here"*

## 19.2 Why the office needs them

**Nothing in the software knows any of this.** TBC can see the trajectory degraded; it cannot see
that a truck was there. The office will otherwise spend an hour inferring from residuals what you
could have written in ten seconds *(Technical Manual §30)*.

## 19.3 The test

If you find yourself thinking *"the office will wonder why the data looks like that here"* —
**that is a comment.**

## 19.4 Comments are not the field record

Both are needed. Comments are timestamped notes inside the mission; the field record is the
document that travels with the data (§26, Appendix C).

---

# 20. Stopping and Restarting

## 20.1 A planned break

1. Stop the run
2. **Leave the mission open and the system logging** if you are returning shortly
3. Restart a new run when you resume
4. Record the break — start, end, reason

> **Keeping the mission open keeps the navigation solution continuous.** Closing and reopening
> starts a new trajectory, and the new one has to be initialized again.

## 20.2 An unplanned stop

| Cause | Do |
|---|---|
| Traffic, obstruction, waiting | Leave the mission open. Record it as a comment (§19) |
| **Battery Protect alarm** | §7 — restore charge immediately |
| **Power cut** | The run is ended and has no closing sequence. Go to §24 |
| Sensor dropped out | Stop. A run with a sensor down is incomplete |

## 20.3 Heat

If you are stationary in direct sun, remember §16.4 — that is outside the rated operating envelope.
Move, or shut down.

## 20.4 Restarting after a mission was closed

**A new mission is a new trajectory.** It needs its own initialization (§12) and its own closing
sequence (§21). You cannot append to a closed mission.

---

# 21. The Closing Sequence

> **CAUTION · W-09**
>
> The post-processed trajectory is computed **forward and backward** and merged. A degraded stretch
> mid-mission is bracketed by good data on both sides. **A degraded stretch at the end has good
> data on one side only.**
>
> **The closing sequence is the reverse pass's anchor. It cannot be added later.**

## 21.1 Do

1. Finish the last run
2. **Drive to an open-sky location — with the mission still running**
3. **Dynamic steering manoeuvres**
4. **Vary the speed**
5. **Drive straight**
6. **Remain stationary for 2–3 minutes**, logging static data
7. **Close the mission** in TMI
8. **Wait for the Control Unit power button light to go out — up to 90 seconds**

**[TRIMBLE METHOD]** *(MX60 QSG Rev B, §5.5 p.13)* — Trimble's documented sequence. It instructs
that the mission be finalized *"according to the following sequence"*, and gives the reason rather
than an obligation: symmetrical start and end *"supports forward and reverse processing modes in
the office software"*. **Not a manufacturer requirement — and still the right thing to do**, because
W-09 above is a fact about the data regardless of who requires what. Whether Parametrix makes it
mandatory is **SOP D-56**.

## 21.2 It is initialization, backwards

Steps 3–6 are the initialization sequence in reverse order *(MX60 QSG Rev B, p.13)* — manoeuvres,
speed variation, straight, static, where the start was static, straight, speed variation,
manoeuvres.

That is not a mnemonic. The backward pass runs through the data in reverse, so what it meets first
is what the forward pass met last.

## 21.3 The mistake

> **IMPORTANT**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and *then*
> driving to open sky achieves nothing. The manoeuvres have to be inside the logged data.

## 21.4 Five minutes

**It takes about five minutes and it is the cheapest quality improvement available in the entire
workflow.**

You cannot append it the next day — a new mission is a new trajectory. There is no office
procedure that buys it back *(Technical Manual §14.3)*.

## 21.5 Record

**That the closing sequence was performed**, and the time. The office will look for it.

---

# 22. Shutdown

## 22.1 Do

1. Confirm the mission is **closed**
2. **Wait for the Control Unit power button light to go out** — up to 90 seconds
3. Only then remove power or the data disk

*(MX60 UG Rev B)*

## 22.2 Stop if

> **CAUTION**
>
> **Do not remove power or the data disk while the power button light is on.** The mission may not
> be fully written.

## 22.3 Then go to §23

**Before the vehicle moves.** Everything in §23 is recoverable here in minutes and costs a
mobilisation from the office.

---

# 23. Field Close-out

**Before the vehicle leaves the corridor.** Not at the yard.

## 23.1 Coverage — against the mission plan

| ☐ | Check |
|---|---|
| ☐ | **Every planned pass driven, in the planned direction** |
| ☐ | The corridor driven end to end, including any extent beyond the deliverable needed to bracket control |
| ☐ | **Planned overlap actually collected** — this is the one that removes office options if missed |
| ☐ | Sections not collected, and why, recorded |
| ☐ | **Closing sequence performed** (§21) |

## 23.2 Data — on the disk

| ☐ | Check |
|---|---|
| ☐ | **Mission folder present, with a plausible size** |
| ☐ | **Run count matches what was driven** |
| ☐ | **`POS_1/raw` present and not empty** |
| ☐ | Base station data captured, if a local base was used |
| ☐ | Power button light out before the disk was disturbed |

> **`POS_1/raw` is the one that cannot be recovered.** Without it there is no post-processed
> trajectory and the mission is NAV-only *(Technical Manual §5.2)*.

## 23.3 Record

| ☐ | Check |
|---|---|
| ☐ | **Field record complete** (§26, Appendix C) |
| ☐ | Comments recorded during collection (§19) |
| ☐ | Any deviation from the plan written down, with its reason |

## 23.4 Then decide

| ☐ | Check |
|---|---|
| ☐ | **Any re-drive decided and performed now** (§24) |

> **CAUTION**
>
> **While you are still at the site you can re-drive a run. Ten minutes down the road, you
> cannot.**

---

# 24. Re-collect or Not

**[PROPOSED]** — everything in this section is a recommendation from this project. **Who decides
a re-collection is D-3 and D-34, and neither is settled** (§24.5). What is not proposed is the
arithmetic: on site a re-drive costs twenty minutes, and from the office it costs a mobilisation.

## 24.1 The rule of thumb

**On site, a re-drive costs twenty minutes. From the office, it costs a mobilisation.**

So the bar for re-driving **while you are still here** is much lower than it feels.

## 24.2 Re-drive now

| | |
|---|---|
| A run ended unexpectedly — power cut, disk, sensor fault | It has no closing sequence, and may be incomplete |
| A sensor was down for part of a run | You will not know what is missing until the office opens it |
| A planned pass was not driven | |
| **Planned overlap was not collected** | Removes LiDAR QC and run-to-run for that stretch |
| Navigation status was orange or red for a significant stretch | §14.4 |
| Occlusion spoiled a stretch you cannot re-drive later | |

## 24.3 Cannot be fixed by re-driving

| | |
|---|---|
| A mission with no closing sequence | **A new mission is a new trajectory.** Re-drive the whole mission, or accept it |
| Weak initialization | The same — it is per-mission |
| A GNSS outage longer than the published envelope | Not a driving problem. Record it and raise it (§17.4) |

## 24.4 If you decide not to re-drive

**Record the decision and the reason.** The office needs to know it was a decision and not an
oversight.

## 24.5 If the segment cannot be served at all

Where no amount of re-driving will produce an acceptable result, the honest finding is that
**mobile mapping may not be the appropriate acquisition method for that segment**. Record it and
raise it — that is a project decision, not yours to absorb.

> **PARAMETRIX DECISION REQUIRED · D-34** — who decides, against what, and what the client is told
> *(SOP §22.5)*.

---

# 25. Data Transfer and Handoff

## 25.1 Removing the disk

1. Confirm the mission is closed and the **power button light is out** (§22)
2. Remove the exchangeable data disk
3. **Never connect the USB cable while the disk is inside the Control Unit** *(MX60 UG Rev B,
   p.10)*

## 25.2 What goes to the office

**The complete mission folder — not the `.mxdb` alone.**

```
TMX<serial>-<mission id>/
  ├── Base/                 base RINEX, if collected
  ├── Camera_1 … Camera_4/  imagery
  ├── Laser_1, Laser_2/     raw scanner data
  ├── POS_1/raw/            ← the one that cannot be recovered
  ├── Extcal.json           the calibration file
  └── <mission>.mxdb        an index, not the data
```

> **The `.mxdb` is a table of contents.** Copying it alone copies nothing useful
> *(Technical Manual §5.2)*.

Plus: the **field record** (§26), base station data if a local base was occupied, and any deviation
from the plan with its reason.

## 25.3 The disk rule

> **CAUTION · W-04**
>
> **Do not clear a data disk until a verified copy exists in at least two locations and the
> `.mxdb` has been confirmed to open.**
>
> A cleared disk is not recoverable, and a mobile mapping mission is not re-drivable at reasonable
> cost.

**[PROPOSED · SOP §11.2]** — the *confirmation-in-writing* step is a Parametrix practice and is
not yet adopted.

**[EQUIPMENT] The underlying fact is not proposed.** A cleared disk is not recoverable and a
mission is not re-drivable at reasonable cost. **Not on a promise, not on a message, not because
the disk is needed tomorrow.**

## 25.4 Handoff is a transfer of responsibility

Until the office has confirmed that verified copy, **the field holds the only copy of an
unrepeatable measurement**. Close-out is not complete when the vehicle is packed; it is complete
when the office confirms.

## 25.5 Record

What was transferred, to whom, when.

> **PARAMETRIX DECISION REQUIRED · D-52, D-53, D-54** — the offload and verification procedure,
> the folder structure and naming, and whether a chain-of-custody record is required *(SOP §11)*.

---

# 26. What Must Accompany the Data

## 26.1 The field record

**[PROPOSED · SOP §9.6 · D-49]** — what the record contains is not yet decided.

**No software produces it.** That part is a fact, not a proposal: it is the only record of
everything the software cannot see, and the office depends on it.

Recorded **at the time**, per mission:

| | |
|---|---|
| Date, operator, vehicle, mission ID | |
| **Capture settings used** — and which presentation you saw (§10.2) | |
| Initialization location and time | |
| **Time green was reached, and time significant recording began** | The settling time (§14.5) |
| Each run — start, end, any incident | |
| **GNSS conditions observed**, per hostile stretch | Entry/exit times, whether overlap was driven |
| Weather | |
| Traffic and occlusion events | |
| **Anything not collected, and why** | |
| **Closing sequence performed** — and the time | |
| Disk and free space at end | |
| Any re-drive decision, and its reason | §24 |

Template: **Appendix C**.

## 26.2 Why each of the hard ones matters

| | |
|---|---|
| **Conditions and occlusion** | Nothing in the software knows a truck was there |
| **What was not collected, and why** | Otherwise the office cannot tell a gap from a decision |
| **The settling time** | It is the only evidence §14.2 was respected |
| **Closing sequence performed** | The office looks for it, and cannot tell from the data alone |

## 26.3 With the data

| ☐ | |
|---|---|
| ☐ | The complete mission folder (§25.2) |
| ☐ | The field record |
| ☐ | Base station data, if a local base was occupied |
| ☐ | Deviations from the mission plan, with reasons |

## 26.4 The test

**Could somebody who was not there work out what happened on this corridor, three weeks from now,
from what you are handing over?**

If not, the missing piece is in the field record.

---

# 27. Common Problems — What to Check First

| Symptom | Check first | Then |
|---|---|---|
| **TMI will not load** | On the Control Unit's network? Using **Chrome**? | §9 |
| **System will not start** | Power button held **15 s**? Supply live? Battery healthy? | §8, §6 |
| **LEDs blink and do not settle** | Give it time — a firmware update can take **up to 6 minutes** | §8.2 |
| **A sensor is missing from the device list** | Cable, power or sensor fault. **Stop** — a run with a sensor down is incomplete | §9.3 |
| **A fitted DMI or GAMS logs nothing** | **Is it activated in Vehicle Settings?** Installed and wired is not enough | §10.1 |
| **Navigation status will not reach green** | **Ask TMI which parameter is holding it** — heading means drive more, position means move | §14.3 |
| **Status stuck on heading** | Not enough dynamic manoeuvres, or no GAMS. More turns and speed changes | §14.3 |
| **Status stuck on position** | Poor sky view. **Move the vehicle** — waiting will not help | §14.3 |
| **Status goes orange mid-corridor** | Where are you? Canopy, canyon, structure? Record it | §17 |
| **Audible alarm** | **Battery Protect.** Restore charge immediately — roughly 78 seconds | §7 |
| **Power cut mid-run** | The run is ended and has no closing sequence. Re-drive decision, now | §7.3, §24 |
| **Storage filling faster than expected** | Reassess before it fills — an interrupted run loses the closing sequence | §11 |
| **Capture settings look different from the guide** | Two presentations exist depending on TMI version. **Record which you saw** | §10.2 |
| **Cannot find 2000 kHz on the screen** | That is a **system total**. TMI uses per-scanner numbering: 500/1000 kHz | §10.2 |
| **Imagery looks wrong on the screen** | Optics — rain, dust, insects, smear. Clean and re-drive the stretch | §3 |
| **You had to skip a planned pass** | Record it and say so at handoff. **Not recoverable in the office** | §17.3, §23 |
| **You closed the mission then remembered the closing sequence** | **It cannot be added.** Re-drive the mission, or record that it is missing | §21 |
| **Unsure whether to re-drive** | On site it costs twenty minutes. From the office, a mobilisation | §24 |

## When the answer is "ask"

**Stop and ask** rather than improvising on the vehicle. You may always stand down, record a
comment, or re-drive while you are still on site (§1.4).

---


---

# Appendices — 

---


---

# Appendix A — Preflight Checklist

*Printable. One per mission.*

**Date** ________________ **Operator** ________________ **Vehicle** ________________

## A1 · Before leaving the yard

| ☐ | | § |
|---|---|---|
| ☐ | Mission plan read — route, passes and directions, overlap, hostile stretches | 2 |
| ☐ | **Two initialization locations** identified | 2 |
| ☐ | Calibration currency confirmed | 2 |
| ☐ | Field record form and this guide on board | 2 |

## A2 · Equipment

| ☐ | | § |
|---|---|---|
| ☐ | **Optics clean** — scanner windows, camera dome | 3 |
| ☐ | Cables sound, no chafe or damage | 3 |
| ☐ | Rack and fixings secure, per the rack's own guide | 3 |
| ☐ | **Sensor Unit seated as measured** — two people to mount | 3, 4 |
| ☐ | GAMS secure and same antenna type, if fitted | 13 |
| ☐ | DMI secure on a **non-steering** wheel, if fitted | 3 |
| ☐ | Cables routed clear of doors and moving parts | 5 |

## A3 · Power

| ☐ | | § |
|---|---|---|
| ☐ | Supply rated **30 A or more**, fused **35 A** near the battery | 6 |
| ☐ | Battery healthy and charged | 6 |
| ☐ | Auxiliary battery healthy, if fitted | 6 |
| ☐ | **No Battery Protect alarm during preflight** | 7 |

## A4 · Start-up

| ☐ | | § |
|---|---|---|
| ☐ | Ignition on, supply live | 8 |
| ☐ | Power button held **≥ 15 s** | 8 |
| ☐ | LEDs settled to ready | 8 |
| ☐ | TMI reached in Chrome at `tmi.mx-scan.net` | 9 |
| ☐ | **Every sensor present in the device list** | 9.3 |

## A5 · Settings

| ☐ | | § |
|---|---|---|
| ☐ | **DMI activated in Vehicle Settings**, lever arm and side set — if fitted | 10.1 |
| ☐ | **GAMS activated in Vehicle Settings**, lever arm set — if fitted | 10.1 |
| ☐ | Install Height preset correct for this vehicle | 10.1 |
| ☐ | Capture settings set — **and which presentation you saw recorded** | 10.2 |
| ☐ | Dust filter set deliberately | 10.2 |

## A6 · Disk

| ☐ | | § |
|---|---|---|
| ☐ | Correct disk, seated | 11 |
| ☐ | **Free space sufficient for the planned mission, with margin** | 11 |
| ☐ | USB cable not connected with the disk inside | 11 |

## A7 · Initialization

| ☐ | | § |
|---|---|---|
| ☐ | Parked in **genuinely open sky** | 12 |
| ☐ | Mission started | 12 |
| ☐ | **2–3 minutes static** | 12 |
| ☐ | **Straight ~20 m** | 12 |
| ☐ | **Speed varied and dynamic steering performed** | 12 |
| ☐ | Status reached green — **time recorded** | 14.5 |
| ☐ | **Settling time allowed — up to 10 minutes** | 14.2 |
| ☐ | Time significant recording began — recorded | 14.5 |

**Signed** ________________

---

# Appendix B — End-of-Mission Checklist

*Printable. Complete **before the vehicle leaves the corridor**.*

**Date** ________________ **Mission ID** ________________ **Operator** ________________

## B1 · The closing sequence

| ☐ | | § |
|---|---|---|
| ☐ | Last run finished | 21 |
| ☐ | **Drove to open sky with the mission still running** | 21.3 |
| ☐ | **Dynamic steering manoeuvres** | 21 |
| ☐ | **Speed varied** | 21 |
| ☐ | **Drove straight** | 21 |
| ☐ | **Stationary 2–3 minutes, logging** | 21 |
| ☐ | Mission closed in TMI — **time recorded** | 21 |
| ☐ | **Power button light out** — up to 90 s — before power or disk disturbed | 22 |

> **It cannot be added later.** If it was missed, record that plainly and go to §24.

## B2 · Coverage — against the mission plan

| ☐ | | § |
|---|---|---|
| ☐ | **Every planned pass driven, in the planned direction** | 23.1 |
| ☐ | Corridor driven end to end, including extent needed to bracket control | 23.1 |
| ☐ | **Planned overlap actually collected** | 17.3 |
| ☐ | Sections not collected, and why, recorded | 23.1 |

## B3 · Data on the disk

| ☐ | | § |
|---|---|---|
| ☐ | **Mission folder present, plausible size** | 23.2 |
| ☐ | **Run count matches what was driven** | 23.2 |
| ☐ | **`POS_1/raw` present and not empty** | 23.2 |
| ☐ | Base station data captured, if a local base was used | 23.2 |

## B4 · Record

| ☐ | | § |
|---|---|---|
| ☐ | **Field record complete** (Appendix C) | 26 |
| ☐ | Comments recorded during collection | 19 |
| ☐ | Deviations from the plan written down, with reasons | 23.3 |
| ☐ | **Time green reached, and time significant recording began** | 14.5 |

## B5 · Decide

| ☐ | | § |
|---|---|---|
| ☐ | **Any re-drive decided and performed now** | 24 |
| ☐ | If not re-driving, the decision and reason recorded | 24.4 |

> **CAUTION**
>
> **While you are still at the site you can re-drive a run. Ten minutes down the road, you
> cannot.**

## B6 · Handoff

| ☐ | | § |
|---|---|---|
| ☐ | **Complete mission folder** transferred — not the `.mxdb` alone | 25.2 |
| ☐ | Field record transferred | 26 |
| ☐ | **Disk NOT cleared** — not until the office confirms a verified copy | 25.3 |

**Signed** ________________

---

# Appendix C — Field Record Form

**No software produces this.** It is the only record of what the office cannot see.

---

## C1 · Mission

| | |
|---|---|
| Date | |
| Operator | |
| Vehicle | |
| **Mission ID** | |
| Project | |
| Weather at start | |
| Weather changes during | |

## C2 · Configuration

| | |
|---|---|
| **Capture settings used** | |
| **Which presentation was shown** | ☐ Measurement Prog + Line Speed ☐ Laser Mode |
| Lateral Range Limit | |
| Dust filter | ☐ off ☐ on |
| **GAMS fitted and activated** | ☐ n/a ☐ fitted, activated ☐ fitted, NOT activated |
| **DMI fitted and activated** | ☐ n/a ☐ fitted, activated ☐ fitted, NOT activated · side: ☐ left ☐ right |

## C3 · Initialization

| | |
|---|---|
| Location | |
| Time started | |
| Static period | ______ min |
| Straight run performed | ☐ |
| Speed variation and manoeuvres performed | ☐ |
| **Time green reached** | |
| **Time significant recording began** | |
| Settling time allowed | ______ min |

## C4 · Runs

| Run | Start | End | Incidents |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

## C5 · GNSS-hostile stretches

| Location | Entered | Left | Conditions | Planned overlap driven? |
|---|---|---|---|---|
| | | | | ☐ yes ☐ no |
| | | | | ☐ yes ☐ no |

## C6 · Events

| Time | Event | Effect on the data |
|---|---|---|
| | | |
| | | |

*Traffic, occlusion, stops, a lane you could not use, a turnaround inside the corridor, a Battery
Protect alarm, a sensor dropout.*

## C7 · Not collected

| What | Why | Re-drive? |
|---|---|---|
| | | ☐ done ☐ not — reason: |

## C8 · Close-out

| | |
|---|---|
| **Closing sequence performed** | ☐ yes — time: ______ ☐ **no** — reason: |
| Mission closed at | |
| Power light out before disk removed | ☐ |
| **Run count on disk** | ______ · matches driven: ☐ |
| **`POS_1/raw` present** | ☐ |
| Base station data captured | ☐ n/a ☐ yes |
| Free space at end | |

## C9 · Handoff

| | |
|---|---|
| Transferred to | |
| Date and time | |
| **Disk cleared?** | ☐ **NO — awaiting office confirmation** ☐ yes, confirmation received from: |

**Signed** ________________

---

# Appendix D — TMI Status and Warning Reference

> **VENDOR CLARIFICATION REQUIRED · V-2**
>
> **The TMI version installed on the Parametrix system has not been confirmed**, and TMI's
> interface has changed between versions. This appendix is sourced to **TMI User Guide Rev L** and
> **MX60 Quick Start Guide Rev B**. **Verify against the system before issue.**

## D1 · Reaching TMI

| | |
|---|---|
| Browser | **Chrome** |
| Capture | `http://tmi.mx-scan.net` |
| Administration | `http://admin.mx-scan.net` |
| Modules | TMI.Capture · TMI.AI |

*(TMI UG Rev L)*

Served by the Control Unit. No internet access required; the addresses resolve only on the Control
Unit's network.

## D2 · Status colours

| Colour | Meaning |
|---|---|
| **Green** | The parameter meets its accuracy threshold |
| **Orange** | Degraded but operating. **Recording is permitted** |
| **Red** | Not meeting threshold |

> **CAUTION**
>
> **Orange permits recording. Survey-grade work does not.** Until **D-3 / D-49** is decided, treat
> orange as a stop-and-assess condition and record it.

> **Green means the solution met its accuracy figures — not that it has finished converging.**
> Trimble asks for **up to ten more minutes** of settling before recording data that matters
> *(MX60 QSG Rev B)*.

## D3 · When the navigation status will not reach its ready state

| Holding parameter | Likely cause | Action |
|---|---|---|
| **Heading** | Insufficient dynamic manoeuvres, or GAMS unavailable | **More turns and speed changes.** Heading is the hardest component to resolve |
| **Position** | Poor sky view | **Move to a genuinely open location** |
| **Attitude** | Insufficient motion variety | Complete the full manoeuvre profile |

> **Ask TMI which parameter is holding the solution rather than waiting.** Heading means drive
> more; position means move the vehicle. **Waiting helps neither.**

## D4 · Alarms and protective behaviour

| Indication | Meaning | Response |
|---|---|---|
| **Audible alarm** | **Battery Protect** — supply below **10.5 V for more than 12 s** | Power cuts at **90 s**, leaving roughly **78 s**. Recovery needs the voltage above **12.0 V** within that window. **Restore charge immediately; do not continue** *(MX60 UG Rev B, p.27)* |
| **Sensor absent from the device list** | Cable, power or sensor fault | **Stop.** A run with a sensor down is incomplete (§24) |
| **Storage warning** | Disk filling | Reassess before it fills mid-run — an interrupted run loses the closing sequence (§21) |

## D5 · Capture settings

> **Two presentations exist, depending on the TMI version** *(`CONFLICT-005`, **V-2**)*:
>
> | Source | Presentation |
> |---|---|
> | MX60 QSG Rev B, p.10 | **Measurement Prog** `[500 kHz, 1000 kHz]` and **Line Speed** `[120 Hz, 200 Hz]` |
> | TMI UG Rev L, p.29 | A single combined **Laser Mode** |
>
> **Expect either. Record which you saw.**

- The measurements-per-second values shown in the interface are **rounded** *(TMI UG Rev L,
  pp.28–29)*
- **Lateral Range Limit** is settable **5–50 m** *(TMI UG Rev L, p.29)*. Whether it affects accuracy
  or is purely a data-volume control is **V-7**
- A **dust filter** is available, intended for **unpaved roads and mine sites** *(Product Bulletin,
  January 2025)*

> **A resolved conflict, recorded so it is not re-opened.** The specification sheet quotes
> **1000 / 2000 kHz** and **240 / 400 Hz** where the User Guide quotes **500 / 1000 kHz** and
> **120 / 200 Hz** — a factor of exactly two, being system totals against per-scanner figures. **TMI
> uses the per-scanner numbering.** `RESOLVED-001`.

## D6 · Comments

Recorded during collection, against the moment. §19.

## D7 · Calibration import

TMI accepts a boresight calibration JSON via **USB1** *(TMI UG Rev L, p.18)*. Relevant where a
calibration is computed in the office and applied to the system rather than to a project.

## D8 · Administration

| | |
|---|---|
| Firmware update | Copy the `.tmx.install` file to a USB stick, connect to **USB1**, **Refresh** then **Install**. The system shuts down; wait until all Control Unit LEDs are off, then power back on. **Powering on may take up to six minutes** *(TMI UG Rev L, p.49)* |
| Licence update | Copy the licence file to a USB stick, connect to USB1, **Import** *(TMI UG Rev L, p.53)* |
| **Remote access** | **When remote control is given to Trimble Support, all data on the system is visible to them.** Remove confidential data before granting it *(TMI UG Rev L, p.54)* |
| Wi-Fi country | Must be set on first use **and every time you collect in a different country** *(MX60 UG Rev B, p.48)* |
| Wi-Fi limitation | Cannot connect to a hotspot that requires logging in on a web page *(TMI UG Rev L, p.51)* |

---

> **This appendix is a reference for the indications, not a substitute for the procedure.** The
> procedure is §8 to §22.

---

# Appendix E — Quick Card

**The ten things that cost the most if missed.** One sheet, both sides. Keep it in the vehicle.

---

| # | | Why it costs |
|---|---|---|
| **1** | **Activate DMI and GAMS in Vehicle Settings** — installed and wired is not enough | A sensor that is not activated **logs nothing**, and nothing looks wrong until the office opens it *(§10.1)* |
| **2** | **Park in genuinely open sky to start** | The static period is doing real work. Under trees, half of it is wasted *(§12)* |
| **3** | **Do the full manoeuvre profile** — straight 20 m, vary speed, turn | Heading is the hardest thing the system has to solve, and turning is how it solves it *(§12.2)* |
| **4** | **Green is not finished.** Allow up to **10 more minutes** before recording anything that matters | The first data after green is the weakest data of the day. Nothing tells you when it improves *(§14.2)* |
| **5** | **Drive every planned pass, in the planned direction** | Direction is not cosmetic. A reverse pass fixes the far side of the corridor *(§15.3)* |
| **6** | **Drive the planned overlap** | Missing it removes **LiDAR QC and run-to-run registration** for that stretch. No warning, no way to tell afterwards *(§17.3)* |
| **7** | **Use Comments as things happen** | Nothing in the software knows a truck was there. Ten seconds now, an hour of office guesswork later *(§19)* |
| **8** | **Do the closing sequence — before closing the mission** | Logging stops the instant the mission closes. **It cannot be added later.** Five minutes *(§21)* |
| **9** | **Check coverage and the disk before the vehicle moves** | On site a re-drive is twenty minutes. From the office it is a mobilisation *(§23)* |
| **10** | **Do not clear a disk until the office confirms a verified copy** | A cleared disk is not recoverable, and the mission is not re-drivable at reasonable cost *(§25.3)* |

---

## And one alarm

> **CAUTION**
>
> **Audible alarm = Battery Protect.** Supply has been below **10.5 V for 12 seconds**. Power cuts
> at **90 seconds**, so you have roughly **78 seconds** to restore charge — the voltage has to rise
> above **12.0 V** within that window.
>
> **Restore charge immediately.** An interrupted run loses the closing sequence with it.

---

## And one thing you may always do

**Stand down.** On safety or data-quality grounds, without asking first. Record the decision and
the reason. **It is not conditional on you being right** *(SOP §9.5)*.
