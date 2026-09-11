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
