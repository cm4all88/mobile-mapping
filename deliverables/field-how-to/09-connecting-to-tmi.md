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

## 9.4 If TMI will not load

Check these in order:

1. Confirm the **Control Unit is powered and has completed startup** (§8)
2. Confirm the field device is connected to the **Control Unit's network** — TMI does not require
   internet access
3. Enter the capture address exactly: **`http://tmi.mx-scan.net`**
4. Use **Chrome**
5. If the connection is still not stable, return to the documented startup/connection sequence
   rather than changing network or system settings at random

**Stop if** TMI cannot be reached reliably or the expected device list cannot be confirmed.

> **CONFIGURATION NOTE**
>
> The exact connection method, network identifier and complete expected device list must be
> confirmed against the actual Parametrix unit before independent use. Do not invent an SSID,
> IP address or sensor list that has not been observed.

Full status reference: **Appendix D**.
