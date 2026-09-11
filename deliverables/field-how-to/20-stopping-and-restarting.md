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
