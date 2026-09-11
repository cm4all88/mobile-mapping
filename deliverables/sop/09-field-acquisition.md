# 9. Field Acquisition Requirements

The method is in the **Field How To**. This section states what shall be done, and what shall not.

## 9.1 Before the vehicle moves

| # | Requirement | State |
|---|---|---|
| 1 | The installation configuration, lever arms and Vehicle Preset are as recorded, and have not changed since | **PARAMETRIX DECISION REQUIRED — D-46** |
| 2 | Where GAMS or DMI are fitted, **each is activated in Vehicle Settings** — not merely installed | **PROPOSED** |
| 3 | The mission plan (§8) is on board and understood | **PROPOSED** |
| 4 | Storage has capacity for the planned collection | **PROPOSED** |

> **CAUTION**
>
> An aiding sensor that is installed and wired but **not activated in Vehicle Settings logs
> nothing**, and nothing looks wrong *(TMI UG Rev L, p.21; Technical Manual §9.3)*. The office
> symptom appears days later as a dimmed settings pane, by which time the mission is collected.

> **PARAMETRIX DECISION REQUIRED · D-46**
>
> **Where are the lever arms, the Vehicle Preset and the installation configuration recorded, and
> who verifies them?** These values are entered once and used on every mission afterwards. An
> error in them is systematic, invisible, and persists until somebody re-measures.

## 9.2 Initialization

> **TRIMBLE REQUIREMENT** — *(MX60 QSG Rev B, §5.3, p.11)*
>
> **Navigation alignment shall be complete before data logging begins.** Trimble states it in
> mandatory terms and the system enforces it: *"Navigation alignment must be done first before data
> logging is allowed!"* It is not a matter of operator discipline.

> **TRIMBLE REQUIREMENT** — *(MX60 QSG Rev B, §5.4, p.13)*
>
> **A mission shall be at least 30 minutes long.** *"Important! A minimum mission time of ≥30 min is
> required."*

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, §5.3, p.11; §6, p.14)*
>
> Trimble documents an initialization sequence — static logging, a straight run, then dynamic
> manoeuvres — and it **should** be performed at the start of every mission, in the order given.
>
> **Trimble does not state this sequence as a requirement**, and this procedure does not claim it
> is one. Trimble writes *"Mobile Mapping Mission **should** be started in a static mode"*, and
> heads the in-field list *"Proposal of a checklist for system operation"*. Whether Parametrix makes
> the sequence mandatory is **D-56**.

> **IMPORTANT**
>
> **Green is not finished.** The navigation status turning green means the solution met its
> accuracy thresholds, not that it has converged. Trimble asks for **up to ten further minutes**
> before recording anything that matters *(MX60 QSG Rev B)*.
>
> **The first data after the light turns green is the weakest data of the day.**

> **PARAMETRIX PROCEDURE (PROPOSED)**
>
> That data **should not** be spent on the most important part of the corridor. Trimble asks for the
> settling time; how the crew spends it is Parametrix's to decide.

The sequence and its rationale are in **Technical Manual §13**; the steps are in the **Field How
To**.

## 9.3 The closing sequence

> **TRIMBLE DOCUMENTED METHOD** — *(MX60 QSG Rev B, §5.5, p.13)*
>
> Trimble documents a closing sequence and instructs that the mission be finalized *"according to
> the following sequence"* — dynamic manoeuvres, varying speed, then 2–3 minutes static — and it
> **should** be performed at the end of every mission, before the mission is closed in TMI.
>
> **Trimble states the reason, not an obligation.** Its note says symmetrical start and end
> procedures *"supports forward and reverse processing modes in the office software"*. That is a
> strong technical reason and a weak instruction; the strength of the rule is Parametrix's to set,
> and it is **D-56**.

> **CAUTION**
>
> **Navigation logging stops the instant the mission is closed.** Closing the mission and then
> driving to open sky achieves nothing. *(Technical Manual §14.2)*

It takes about five minutes and it is the cheapest quality improvement in the workflow. It cannot
be added later — a crew returning the next day cannot append it, because a new mission is a new
trajectory *(Technical Manual §14.3)*.

## 9.4 Operating limits

| Limit | Value | Source |
|---|---|---|
| **Recommended maximum speed with the system operating** | **80 km/h (50 mph)** | MX60 UG Rev B |
| Absolute maximum, operating or not | 110 km/h (68 mph) | MX60 UG Rev B |
| **Direct sun, stationary or below 10 km/h** | **Outside the rated operating envelope** | MX60 UG Rev B, p.53 |

> **CAUTION · W-11**
>
> **Battery Protect** *(MX60 UG Rev B, p.27)*: an audible warning below **10.5 V for longer than
> 12 seconds**, power cut below **10.5 V for more than 90 seconds**, recovery if voltage rises
> above **12.0 V** within that time.
>
> **An interrupted run loses the closing sequence with it.** Treat the audible warning as an
> instruction to restore charge, not as information.

> **PARAMETRIX DECISION REQUIRED · D-43**
>
> **Field operating rules** — wet-weather go/no-go with operator stand-down authority, night
> collection, and collection speed by deliverable type. Trimble publishes a recommended maximum and
> an absolute maximum and **no guidance relating speed to deliverable quality**
> *(Technical Manual §16.2)*.

## 9.5 Stand-down authority

**The Field Technician may stop or decline collection on safety or data-quality grounds without
seeking approval first.** The decision and its reason are recorded. This authority is not
conditional on the decision later proving correct (§4.4).

## 9.6 The field record

> **PARAMETRIX PROCEDURE (PROPOSED) · D-49**
>
> Recorded per mission, at the time: date, operator, vehicle, mission ID; capture settings; the
> initialization location and time; each run with start and end and any incident; **GNSS conditions
> observed**; weather; traffic and occlusion events; **anything not collected and why**; the closing
> sequence performed; disk and free space at the end.

> **This is the one record in the whole workflow with no software artefact behind it.** Nothing in
> TBC knows that a truck occluded the near lane for 200 m, or that the corridor was collected in
> rain. If the crew does not write it down, it is gone *(Technical Manual §30)*.

## 9.7 Records this section requires

| Record | State |
|---|---|
| Pre-flight confirmation, including aiding-sensor activation where fitted | **D-46** |
| The field record, per §9.6 | **D-49** |
| Any exercise of stand-down authority, and its reason | **D-43** |
| Operating-limit exceedance, if any, and what was done | **D-43** |


> **IN PLAIN LANGUAGE**
>
> **What this section means.** The rules for the hours the vehicle is actually moving: start the
> system the way Trimble documents, do not log until the navigation solution is ready, stay inside the
> machine's limits, and finish the mission properly before shutting it down.
>
> **Why it matters.** Almost nothing here can be fixed later. The trajectory is computed from what the
> sensors saw on the day. If the start was rushed, the closing sequence was skipped, or an aiding
> sensor was installed but never switched on, the office inherits the consequence and has no way to
> undo it.
>
> **Remember this.** Green is not finished — the navigation status turning green means the solution
> met its thresholds, not that it has settled, and Trimble asks for up to ten more minutes before
> recording anything that matters. The closing sequence takes about five minutes and cannot be added
> the next day, because a new mission is a new trajectory.
>
> **If this is skipped.** The weakest data of the day lands on the most important part of the
> corridor, and the end of the mission has good data on one side only. Neither shows up as an error;
> they show up as a dataset that quietly does not meet its accuracy requirement.
