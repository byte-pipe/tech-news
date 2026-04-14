---
title: A bug on the dark side of the Moon
url: https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/
date: 2026-04-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:01:22.025243
---

# A bug on the dark side of the Moon

# A bug on the dark side of the Moon

## Overview of the discovery
- The authors used Claude and Allium, an open‑source behavioural specification language, to compress ~130 k lines of Apollo Guidance Computer (AGC) assembly into ~12.5 k lines of specifications.  
- This systematic extraction of resource‑lifecycle specifications for the Inertial Measurement Unit (IMU) highlighted a defect: a lock (LGYRO) that is not released on an error path.

## How the AGC code is organized
- AGC source code was transcribed from printed listings starting in 2003 and made publicly available.  
- The flight programs were physically woven into 74 KB of core rope memory; the women who performed the weaving were called the “Little Old Ladies.”  
- No formal verification, model checking, or static analysis has been published for the flight code; scrutiny has mainly involved reading, emulating, and verifying the transcription.

## The specific defect
- The IMU is controlled through a shared lock named LGYRO.  
- Normal operation: lock is acquired at entry, torque is applied to three gyroscope axes, and the lock is cleared on exit via `STRTGYR2`.  
- Emergency “caging” (mechanical clamp of the IMU) triggers an early exit through `BADEND`.  
- `BADEND` does **not** clear LGYRO; the two missing instructions are `CAF ZERO` and `TS LGYRO`.  
- Consequently, the lock remains set, preventing any subsequent gyro‑related routines from executing.

## Hypothetical manifestation during Apollo 11
- While Michael Collins orbited the Moon, he ran Program 52 (star‑sighting alignment) every two hours.  
- If the cage switch were inadvertently activated during a torque, the routine would abort via `BADEND`, leaving LGYRO set.  
- A second attempt to run Program 52 would appear to hang: the DSKY accepts input but no gyro commands execute, while all other computer functions remain operational.  
- The crew would likely interpret the symptom as hardware failure rather than a locked software resource; a hard reset would clear the lock, but such a reset was stressful after the earlier 1202 alarms.

## Historical context and related issues
- Margaret Hamilton’s team introduced many concepts still used today (priority scheduling, asynchronous multitasking, restart protection).  
- The most serious Apollo‑era bugs were specification errors rather than coding mistakes; for example, a radar power‑supply voltage mismatch caused the 1202 alarms.  
- `BADEND` is a generic termination routine that clears general state but not the gyro‑specific LGYRO lock, leading to the leak.

## Significance of the finding
- The bug demonstrates that even extensively examined legacy code can contain subtle resource‑management errors that only emerge under rare error conditions.  
- Behavioural specification extraction provides a systematic way to uncover such defects without exhaustive manual review.  
- Understanding this defect adds nuance to the narrative of Apollo’s software reliability and highlights the value of modern specification tools for historic codebases.