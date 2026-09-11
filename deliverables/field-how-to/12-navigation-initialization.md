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
