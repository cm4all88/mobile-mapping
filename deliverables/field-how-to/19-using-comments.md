# 19. Using Comments

## 19.1 Do

**Use TMI's Comments feature as things happen.** Not afterwards.

Examples worth recording:

- *"heavy canopy from the bridge"*
- *"stopped 4 min, traffic control"*
- *"parked truck occluding the north side"*
- *"could not drive second pass, road closed"*
- *"hard rain from here"*

## 19.2 Why the office needs them

**Nothing in the software knows any of this.** TBC can see the trajectory degraded; it cannot see
that a truck was there. The office will otherwise spend an hour inferring from residuals what you
could have written in ten seconds *(Technical Manual §30)*.

## 19.3 The test

If you find yourself thinking *"the office will wonder why the data looks like that here"* —
**that is a comment.**

## 19.4 Comments are not the field record

Both are needed. Comments are timestamped notes inside the mission; the field record is the
document that travels with the data (§26, Appendix C).
