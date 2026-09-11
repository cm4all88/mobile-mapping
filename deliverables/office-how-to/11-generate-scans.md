# 11. Generate Scans

This is where the trajectory meets the measurements. Before it, the scanner data is ranges and
angles from a moving sensor; after it, every return has a coordinate.

### Do

1. Select a **run** in Project Explorer — **one run first**, not the mission
2. **Generate Scans** from the context menu
3. Set the **Filters**
4. Set **Colorization**
5. Run it, inspect the result (§12), and only then repeat at **mission** level

### Look at — the filters

| Filter | Removes |
|---|---|
| **Range Min / Max** | Returns outside a distance window |
| **Isolated Points** | Points with too few neighbours |
| **Fog** | Returns caused by fog |
| **Sun** | Returns caused by direct sunlight on the sensor |
| **Reflective Panels** | "the noise before and after a target" |
| **Dust** | Airborne dust returns *(Product Bulletin, January 2025)* |

Then the **Results of Scan Generation** dialog, which records per run the filters applied, the
range, and the counts.

### Expect

Scans appearing **beneath the trajectory node**, not beneath the run. Generating at mission level
processes all runs; at run level, one.

### Stop if

- **The deliverable is sign or retroreflectivity work and Reflective Panels is on.** Those returns
  may be the deliverable
- The filter set is not the one you intended. Regenerating is cheap in effort and expensive in
  time; getting it right on one run first is why step 1 says one run

> **PARAMETRIX DECISION REQUIRED · D-22**
>
> **Are scans generated coloured by default?** *(SOP §13.3)*

> **TESTING REQUIRED · T6**
>
> **Colouriser camera preference** — forward versus backward — and its effect on fringing at
> feature edges. Untested.

> **TESTING REQUIRED · T1, T3**
>
> Filter defaults are untested against Parametrix work. **T3:** whether **Reflective Panels**
> removes legitimate retro-reflective returns from signs and line marking *(SOP §13.3)*.

> **The MX60 has no MTA stage.** If you find TBC documentation about configuring a GPU driver for
> MTA range-ambiguity correction *(TBC 23856)*, it does not apply to this system — that is the MX9
> and MX90 path *(Technical Manual §5.1)*.

### Record

**Capture the Results of Scan Generation into the project record.** It is the only artefact that
states which filters produced a given cloud *(SOP §13.3)*.
