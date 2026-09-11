# 26. PFIX — The Two-Pass Procedure

**Generate POSPac Position Fixes.** Where registration corrects the answer, PFIX corrects the
computation: the control observations go back into the navigation solver as position fixes and the
filter re-solves with them available.

### Prerequisites

*(TBC 24460)*

- **POSPac MMS installed with a valid licence** for the IN-Fusion processing methods
- An SBET processed in POSPac — or the NAV trajectory, "in case of POSPac processing not possible"
- A VCE project whose coordinate system matches the data
- The `.mxdb` imported with that trajectory applied
- **Scan data generated from at least one run**
- A GCP file imported in the project coordinate system

### Do — part one, in TBC

1. Right-click the **Mission** node ▸ **Generate Pospac Position Fixes**. *The command does not
   open if the mission has no generated scan*
2. Select a GCP under **Points** ▸ **Add Selection to Control Points**
3. Pick the target — **the same Point Cloud Smart Picking tool as registration** (§16), with the
   same live residuals and the same **30 m maximum pair separation**
4. **Validate.** Easting, Northing and Elevation residuals display
5. Add further pairs
6. **Compute.** Updated targets are named `Mission_Name-PFIX-GCP_Name`, and
   **a `custom_events.txt` is written into a `PFIX` folder under the TBC project folder**
7. Close the dialog

### Do — part two, in POSPac

1. Start POSPac MMS, create and save a project
2. Import the POS logged files from `POS_1/raw`
3. **Copy `custom_events.txt` from TBC into the `Extract` folder of the POSPac project**
4. Open the **GNSS-Inertial Processor**
5. Optionally open **Position Fixes and Satellite Events** to inspect the fixes
6. Select the IN-Fusion processing mode
7. **All Processings.** A new SBET appears in the `Proc` folder

### Do — part three, back in TBC

1. Select the mission ▸ properties
2. **Replace the initial trajectory file with the new SBET**
3. **Update Scans** (§21)

### Expect

A better trajectory through the stretch that had no GNSS, with the correction propagated by the
filter's own model of how the system behaves rather than by interpolation between control points.

### Stop if

- **You stop after step 7 of part one.** The `custom_events.txt` does nothing by itself
- **You skip part three's Update Scans.** A better trajectory that never reaches the point cloud
  has cost a day and changed nothing in the deliverable

> **VENDOR CLARIFICATION REQUIRED · V-16**
>
> When should PFIX be preferred over registration? Trimble describes both commands and never
> contrasts them. The framing at the top of this section is this project's reading, not Trimble's
> statement *(Technical Manual §27.5)*.

### Record

That PFIX was used, on which stretch, and the check-point residuals before and after.
