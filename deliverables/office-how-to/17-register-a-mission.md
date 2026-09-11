# 17. Register a Mission

A set of runs at once, **with every GCP reusable**. For ordinary corridor work this is probably the
command you want.

### 17.1 Do

The sequence is that of §16, run from the mission rather than a run. What differs:

| | Register a **Run** | Register a **Mission** |
|---|---|---|
| Scope | One run | A set of runs |
| GCP reuse | Once | **Every GCP, as many times as it appears** |
| Control list | One row per GCP | **One row per GCP `instance`** |
| Instances | — | One per **250 m scan section** whose bounding box contains the GCP |
| Side | — | An instance binds to the **left**, **right**, or **both** sides of the scan section |
| Default name | *RunName* Trajectory | **Reg** |
| Target naming | `RunName TrajectoryGCPName` | `RegistrationName_GCPName_RunName` |
| Output node | `Reg. Trajectory` under the run | **`RegTrajectory` under each involved run** |

*(TBC 26473)*

### 17.2 Look at

The **Control Points** list. One painted mark visible in four passes produces **four instances**,
and each is picked separately. Unused instances are removed from the list when you compute.

### 17.3 Expect

Four runs adjusted against the same observation, and therefore mutually consistent — which is the
point of the command. A corridor driven in both directions twice is the ordinary case.

### 17.4 Stop if

- You expected instances and got none. The GCP is outside every 250 m scan section's bounding box
- You are about to re-register a mission that has already been registered (§19)

> **PARAMETRIX DECISION REQUIRED · D-12**
>
> Is Register a Mission the corridor default, with Register a Run reserved for single-run cases and
> for repairing one run in an otherwise accepted mission? And what happens to a mission
> registration when one run is later re-collected? *(SOP §13.4)*

### 17.5 Record

As §16, plus which runs were included.
