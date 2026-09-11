# 5. Project Setup

### 5.1 Do

1. Create the VCE project
2. **Set the coordinate system, datum, epoch and geoid model — before importing anything**
3. Record what you set, and who set it

### 5.2 Look at

The project's coordinate system properties, against the control network and the written client
requirement (SOP §6.1).

### 5.3 Expect

A coordinate system that matches the control you are going to register against. TBC 2026.10 ships
**Coordinate System Database v115**; selecting a predefined geoid model now enters the vertical
datum name automatically *(TBC RN 2026.10)*.

### 5.4 Stop if

- The project's accuracy requirement is not stated in writing
- The CRS, datum or epoch has not been decided *(SOP §6.2, D-21)*
- Grid or ground has not been agreed with the client *(SOP §6.3, D-38)*

> **CAUTION · W-05**
>
> **Set the project coordinate system before importing the mission.**
>
> Changing it afterwards is possible in TBC generally, but by then every derived product — scans,
> registrations, exports — was computed in the previous frame. **Treat it as irreversible in
> practice.**

> Practically: if you discover the CRS is wrong after processing, the cheapest honest route is a
> new project and a re-import, not a change in place.

### 5.5 Record

CRS, datum, epoch, geoid, and who set them.
