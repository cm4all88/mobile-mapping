# MX60 equipment-arrival validation checklist

**Project control material — living document. Not an operator checklist and not an issued SOP.**

This file captures the work that **should wait until the actual Parametrix MX60, installed TMI
build and processing workstation are available**. Its purpose is to keep the documentation honest:
do not fill a gap with a generic screenshot, guessed sensor fitment, invented network setting or a
value copied from a different MX platform.

Complete this during commissioning and the first controlled field/office missions. Feed confirmed
facts back into the Field How To, Office How To, SOP, Technical Manual, master register and figure
register as appropriate.

## 1. System identity and delivered configuration

Record once from the delivered equipment and vendor records.

- [ ] MX60 serial number
- [ ] Premium configuration confirmed against the delivered unit / serial record
- [ ] Control Unit identifier
- [ ] Sensor Unit identifier
- [ ] Mounting rack make/model and whether Trimble standard-rack offsets apply
- [ ] GAMS fitted: yes / no
- [ ] GAMS antenna type and baseline
- [ ] GAMS lever arm source and measured values
- [ ] DMI fitted: yes / no
- [ ] DMI mounting side
- [ ] DMI scale-factor source: measured wheel / other
- [ ] Vehicle Install Height / preset actually in use
- [ ] Primary GNSS antenna confirmed as **Trimble 112735**
- [ ] Current calibration date and where that record is read
- [ ] Where the authoritative system configuration record will live

**Register items this should inform:** D-2 / V-4, D-46, and any fitment-dependent wording.

## 2. TMI build and field connection

Do not invent these before observing the actual unit.

- [ ] Installed TMI version/build
- [ ] Exact method the field tablet/laptop uses to join the Control Unit network
- [ ] Network identifier visible to the operator, if any
- [ ] Confirm `http://tmi.mx-scan.net` opens the capture interface
- [ ] Confirm `http://admin.mx-scan.net` opens the administration interface when appropriate
- [ ] Record what a wrong-network condition looks like
- [ ] Capture the complete device list when the Premium system is healthy
- [ ] Confirm how the delivered GAMS/DMI appear when present and activated
- [ ] Confirm what appears when an aiding sensor is present but disabled, if this can be tested safely

**Capture figures:** P04, P05.

## 3. Physical installation photographs

Take photographs for recognition, not decoration.

- [ ] Sensor Unit correctly mounted on the actual rack
- [ ] Orientation / forward direction
- [ ] Cable exits and routing
- [ ] Operator-accessible connectors and labels
- [ ] Control Unit power/feed and normal operator controls
- [ ] DMI installation and side, if fitted
- [ ] GAMS antenna installation, if fitted
- [ ] Any measurement point used for installation-height or lever-arm verification

**Capture figures:** P01, P02.

## 4. TMI operator screenshots

Capture clean screenshots from the installed build.

- [ ] Startup / ready screen
- [ ] LED/status condition that corresponds to normal ready state
- [ ] Firmware-update indication if encountered
- [ ] Vehicle Settings
- [ ] GAMS activation and lever arm fields, if fitted
- [ ] DMI activation, mounting side, lever arm and scale factor fields, if fitted
- [ ] Install Height / vehicle preset
- [ ] **Actual capture-settings presentation** — resolve V-2 / CONFLICT-005
- [ ] Laser rate / line speed or Laser Mode as actually presented
- [ ] Lateral Range Limit
- [ ] Dust filter
- [ ] Navigation Status — green
- [ ] Navigation Status with a parameter holding initialization, if safely reproducible
- [ ] Live imagery view
- [ ] Storage/free-space view
- [ ] Run stop control and mission-close control

**Capture figures:** P03, P06–P10.

## 5. First controlled field mission

Use a training/commissioning mission, not a client-critical first attempt.

- [ ] Primary and backup initialization locations identified
- [ ] Initialization sequence performed and timed
- [ ] Time green is reached recorded
- [ ] Settling period recorded
- [ ] If GAMS is fitted, compare actual behavior with the documented GAMS initialization statement
- [ ] Confirm comments can be entered and recovered in the office
- [ ] Confirm planned run/pass record is usable in the vehicle
- [ ] Confirm expected imagery and both laser streams are present
- [ ] Confirm storage growth can be read in TMI
- [ ] Perform the closing sequence and record what the operator sees
- [ ] Confirm the mission is closed cleanly
- [ ] Capture the resulting complete mission-folder tree
- [ ] Confirm `POS_1/raw/` is present and non-empty
- [ ] Exercise the transfer-verification procedure from SOP §11.2
- [ ] Confirm what evidence the office can use to say the copy is verified

**Capture figure:** P11.

## 6. First controlled TBC processing job

Process the commissioning mission end to end.

- [ ] TBC version confirmed as the version documented by the set
- [ ] POSPac availability/licence established
- [ ] Process Raw Trajectory Data dialog captured
- [ ] Antenna model reads **Trimble 112735**
- [ ] GAMS pane behavior confirmed against fitment
- [ ] DMI pane behavior confirmed against fitment
- [ ] Backup SBET Next to MXDB behavior confirmed
- [ ] Frame/epoch log located and archived
- [ ] Scan generation performed
- [ ] Station naming before registration recorded
- [ ] Control vs independent-check UI captured
- [ ] Register a Run tested
- [ ] Register a Mission tested where applicable
- [ ] Register Run to Run tested where applicable
- [ ] Edit-registration recovery path rehearsed without stacking a second adjustment
- [ ] Residual/results screen captured
- [ ] Update Scans performed
- [ ] `_reg_####` station naming confirmed
- [ ] Registered trajectory nesting in Project Explorer confirmed
- [ ] Cutting Plane + Scan Color visual QC captured
- [ ] Imagery QC path confirmed
- [ ] Export rehearsal completed only after §31 pre-export check

**Capture figures:** P12–P18.

## 7. Tests that should use the real system

These are not all commissioning-day tasks. Run them when the prerequisites exist; record the result
in the master register rather than silently changing prose.

- [ ] Export with timestamps off/on and compare geometry — **T18**
- [ ] Cleanup behavior and preservation/deletion of numbered SBET artefacts — **T28**
- [ ] Export-state verification method by path — **T29**
- [ ] Point Cloud tab selection across different trajectories — **T23**
- [ ] Multipath/default processing settings where testing is warranted — **T11**
- [ ] DMI scale-factor/default uncertainty if DMI is fitted — **T12**
- [ ] LiDAR QC settings/capability if Parametrix adopts that workflow — applicable T-items / D-11
- [ ] GNSS-hostile section observations compared with achieved trajectory behavior — **T31**

## 8. Decisions this checklist must not make

The commissioning team records evidence. It does **not** invent company or project policy.

Leave these to the proper decision path:

- who is qualified to operate, process, register, accept or authorize destructive operations — D-3
- formal acceptance framework / accuracy decision — D-13
- project CRS, datum, epoch, geoid and grid/ground — project setup / D-21 / D-38
- Single Base vs PP-RTX and base-station strategy — D-19 / D-42
- pass pattern and required overlap by project/work type — D-41
- orange-status collection rule — D-49
- standard deliverable formats and export paths — D-38

## 9. Closeout

This checklist is complete when:

- the actual delivered system configuration is no longer described as unknown in the operator path;
- the installed TMI presentation has replaced the temporary two-presentation fork;
- the high-value Field/Office screenshots come from the real Parametrix workflow;
- commissioning observations have either closed, narrowed or explicitly preserved the relevant
  D/T/V items;
- no screenshot or setting was borrowed from another MX platform merely to make the manuals look
  finished.

**A blank item is acceptable while the set is living. A guessed answer is not.**
