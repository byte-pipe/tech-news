---
title: A bug on the dark side of the Moon
url: https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/
site_name: tldr
content_file: tldr-a-bug-on-the-dark-side-of-the-moon
fetched_at: '2026-04-15T06:00:24.114478'
original_url: https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/
date: '2026-04-15'
published_date: '2026-04-07'
description: How a specification surfaced a defect in the Apollo flight code.
tags:
- tldr
---

ai


 Apr 07, 2026



# A bug on the dark side of the Moon



## How a specification surfaced a defect in the Apollo flight code.










Henry Garner


 CTO & AI Chapter Lead



























The Apollo Guidance Computer (AGC) is one of the most scrutinised codebases in history. Thousands of developers have read it. Academics havepublished papers on its reliability. Emulators run it instruction by instruction. We independently identified a bug in it: a resource lock in the gyro control code that leaks on an error path.†

We used Claude andAllium, our open-source behavioural specification language, to distil 130,000 lines of AGC assembly into 12,500 lines of specs. The specs were derived from the code itself, and the process signposted us directly to the defect.

## Charting the code

The source code has been publicly available since 2003, when Ron Burkey and a team of volunteers began painstakinglytranscribing it by handfrom printed listings at theMIT Instrumentation Laboratory. In 2016, former NASA intern Chris Garry’sGitHub repositorywent viral, topping the trending page. Thousands of developers scrolled through the assembly language of a machine with 2K of erasable RAM and a 1MHz clock.

The AGC’s programs were stored in 74KB ofcore rope: copper wire threaded by hand through tiny magnetic cores in a factory (a wire passing through a core was a 1; a wire bypassing it was a 0). The women who wove it were known internally as the “Little Old Ladies”, and the memory itself was called LOL memory. The program was physically woven into the hardware. Mike Stewart has analysed it down toindividual gates, and theVirtual AGC projectruns the software in emulation. The sole source for the Apollo 11 flight programs is a pair of printouts in theMIT Museum’s collection.

As far as we can determine, no formal verification, model checking or static analysis has been published against the flight code. The scrutiny has been deep, but it has been a particular kind of scrutiny: reading the code, emulating the code, verifying the transcription.

We took a different approach. We usedAlliumto distil a behavioural specification from theInertial Measurement Unit(IMU) subsystem, the gyroscope-based platform that tells the spacecraft which way it is pointing. The specification models the lifecycle of every shared resource: when it is acquired, when it must be released, and on which paths.

It surfaced a flaw.

## Losing the reference

The AGC manages the IMU through a shared resource lock calledLGYRO. When the computer needs to torque the gyroscopes (to correct platform drift or perform a star alignment), it acquiresLGYROat the start and releases it when all three axes have been torqued. The lock prevents two routines from fighting over the gyro hardware at the same time.

The lock is acquired on the way in and released on the way out. But there is a third possibility, and it doesn’t release the lock.

‘Caging’is an emergency measure: a physical clamp that locks theIMU’s gimbalsin place to protect the gyroscopes from damage. The crew could trigger it with a guarded switch in the cockpit.

When the torque completes normally, the routine exits viaSTRTGYR2and theLGYROlock is cleared. When the IMU is caged while a torque is in progress, the code exits via a routine calledBADEND, which does not clear the lock. Two instructions are missing:

 CAF ZERO

 TS LGYRO

Four bytes.

On 21 July 1969, while Neil Armstrong and Buzz Aldrin walked on the lunar surface,Michael Collinsorbited alone in the Command ModuleColumbia. Every two hours he disappeared behind the Moon, out of radio contact with Earth. “I am alone now, truly alone, and absolutely isolated from any known life. I am it,” he wrote inCarrying the Fire. “If a count were taken, the score would be three billion plus two over on the other side of the moon, and one plus God knows what on this side.”

During each pass he ranProgram 52, a star-sighting alignment that kept the guidance platform pointed in the right direction. If the platform drifted, the engine burn to bring him home would point the wrong way.

## Radio silence

Here’s how we imagine the bug might have manifested.‡

Collins has just finished his star sightings at the optics station in the lower equipment bay and keyed in the final commands. The computer is torquing the gyroscopes to apply the correction across all three axes.

He moves back toward the main panel in a cramped cockpit, past acage switchprotected by a flip-up cover. An elbow catches the cover and nudges the switch. The code handles this gracefully: a routine calledCAGETESTdetects the cage, abandons the torque and exits. The P52 fails, and he understands why: the cage interrupted the correction. He uncages the IMU and heads back to the optics station to realign.

He starts a new P52. The program hangs.

No alarm, no program light. TheDSKY(display and keyboard, his only interface to the computer) accepts the input and does nothing. He tries V41, the manual gyro torque verb. Same result. Everything else on the computer works. Only gyro operations are dead.

The first failure looked normal: a cage event during alignment, with a known recovery. The second gives no clue what is wrong. The trained response to an accidental cage is to uncage and realign. Collins had been trained to restart the computer, but nothing about this failure would suggest he needed to. Commands were accepted, everything else worked. It would look like faulty hardware, not a stuck lock.

“My secret terror for the last six months has been leaving them on the Moon and returning to Earth alone”, Collins later wrote of therendezvous. A dead gyro system behind the Moon, with Armstrong and Aldrin on the surface waiting for a rendezvous burn that depends on a platform he can no longer align, is exactly that scenario.

A hard reset would have cleared it. But the1202 alarmsduring the lunar descent had been stressful enough with Mission Control on the line and Steve Bales making a snapabort-or-continue call.

Behind the Moon, alone, with a computer that was accepting commands and doing nothing, Collins would have had to make that call by himself.

## The known landmarks

Margaret Hamilton (as“rope mother”for COMANCHE) approved the final flight programs before they were woven into core rope memory. Her team at the MIT Instrumentation Laboratory pioneered concepts we nowtake for granted: priority scheduling, asynchronous multitasking, restart protection and software-based error recovery. Even the term ‘software engineering’ is attributed to her.

Their restart protection saved the Apollo 11 landing when the 1202 alarms fired during descent, clearing the backlog of stalled jobs and restarting only those the programmers had marked as essential. Most modern systems don’t handle overload that gracefully.

The most serious bugs that did surface were specification errors, not coding mistakes. Don Eyles, who wrote the lunar landing guidance code,documented several. For example, the ICD for therendezvous radarspecified that two 800 Hz power supplies would be frequency-locked but said nothing about their voltage levels or phase relationship. The conventional explanation blamed an arbitrary phase offset between the supplies. But recent experimental work byMike Stewarton Apollo hardware has reproduced the exact oscillation seen in the Apollo 11 telemetry without any phase shift at all. The voltage difference between the two references was enough on its own to drive the system manic. This appears to be the underlying cause of the 1202 alarms.

BADENDis a general-purpose termination routine shared by all IMU mode-switching operations. It clearsMODECADR(the stall register), wakes sleeping jobs, and exits. ButLGYROis a gyro-specific lock, acquired only by the pulse-torquing code and released only by the normal completion path inSTRTGYR2. When the error path routes throughBADEND, it handles the general resources correctly, but not the gyro-specific lock.

The AGC was written so defensively thatLGYROwould be cleared by anyrestartor major program change. Normal recovery procedure after a failed alignment would begin with a program change, clearing the lock automatically. Partly because of this,the anomalywasn’t discovered until several missions later.

## Star sighting

We identified the issue independently by distilling a behavioural specification of the IMU subsystem usingAllium, an AI-native behavioural specification language. The specification models each shared resource as an entity with a lifecycle: acquired, held, released.

The IMU entity declares agyros_busyfield modellingLGYRO. Two rules govern it:

rule GyroTorque {
 -- Sends gyro torquing pulse commands. Reserves the gyros,
 -- enables power supply, and dispatches pulses per axis.
 when: GyroTorque(command: GyroTorqueCommand)

 requires:
 imu.mode != caged
 imu.gyros_busy = false

 ensures:
 imu.gyros_busy = true
 GyroTorqueStarted()
}

rule GyroTorqueBusy {
 -- Gyros already reserved by another torquing operation.
 -- Caller sleeps until LGYRO is cleared.
 when: GyroTorque(command: GyroTorqueCommand)

 requires: imu.gyros_busy = true

 ensures:
 JobSleep(job: calling_job())
}

GyroTorquerequiresgyros_busy = falseand ensuresgyros_busy = true: the lock is acquired. Somewhere, on every path that follows, the lockmustbe released. The spec doesn’t show where in the code the release happens, but it makes the obligation explicit: ifgyros_busygoes to true,somethingmust set it back to false.

With that obligation written down, Claude traced every path that runs aftergyros_busyis set to true. The normal completion path (STRTGYR2) clears it. The cage-interrupted path (BADEND) does not.MODECADR, the other shared resource, is correctly cleared inBADEND:LGYROis missing.

The specification forces this question on every path through the IMU mode-switching code. A reviewer examiningBADENDwould see correct, complete cleanup for every resourceBADENDwas designed to handle.

The specification approaches from the other direction: starting fromLGYROand asking whether any paths fail to clear it.

Tests verify the code as written; a behavioural specification asks what the code is for.

A specification distilled by Allium models resource lifecycles across all paths, including the ones that are hardest to test. You can view theAllium specificationsandreproduction of the bugon GitHub.

## Course correction

Hamilton’s team released resources by loading the constant zero into theaccumulator(CAF ZERO) and storing it into the lock register (TS LGYRO). Every release placed manually, by a programmer who remembered every path that could reach that point.

Modern languages have tried to make lock leaks structurally impossible: Go hasdefer, Java hastry-with-resources, Python haswith, Rust’sownership systemmakes lock leaks a compile-time error.

Nevertheless, lock leaks persist. MITRE classifies the pattern asCWE-772: “Missing Release of Resource after Effective Lifetime”, and rates its likelihood of exploitation as high. Not all resources are managed by a language runtime. Database connections, distributed locks, file handles in shell scripts, infrastructure that must be torn down in the right order: these are still often the programmer’s responsibility. Anywhere the programmer is responsible for writing the cleanup, the same bug is waiting.

Every Apollo crew came home safely. The defect was present acrossmissionsin both the Command Module software (COMANCHE) and the Lunar Module software (LUMINARY) from Apollo 11 to 14.

A latent issue sat in flight-proven assembly. What’s hiding in yours?Let’s talk.

Thanks toFarzad “Fuzz” Pezeshkpourfor independentlyreproducing the bug, and toDanny SmithandPrashant Gandhifor reviewing early drafts of this article.

†8 April 2026. This article has been revised to correct factual errors. AsRon Burkeyput it: “it’s often dangerous to assert that just because a given AGC issue hadn’t been fixed that it hadn’t been noticed”. We are grateful to him andMike Stewartfor sharing their deep knowledge of the Apollo programme and for taking the time to set the record straight.

‡8 April 2026. The scenario described above could not have played out as written. AsMike Stewartpointed out,LGYROis also zeroed inSTARTSB2, which is executed viaGOPROG2on any major program change. Starting a new P52 would itself clear the lock before the torque began. HittingBADENDwhile actively pulse-torquing is rare, and avoided by normal procedure. In the very specific scenarios where the bug can be triggered and persist, it does not fail silently: multiple jobs stack up attempting to torque the gyros until the computer runs out of space and a program alarm is triggered. The issue was found before the flight of Apollo 14, and a description of how it might occur along with a recovery procedure was added to theApollo 14 Program Notes.



Recommended Resources




ai
Mar 30, 2026

## Software's second heroic age

### The window where one person could reshape the whole field had closed. AI has re-opened it.

Henry
Garner
CTO & AI Chapter Lead


ai
Mar 16, 2026

## Capability hyperinflation

### What happens when your roadmap is priced in a rapidly depreciating currency?

Henry
Garner
CTO & AI Chapter Lead


ai
Mar 09, 2026

## New vocabulary for an old problem

### Two recent terms that describe an engineering challenge as old as the hills.

Henry
Garner
CTO & AI Chapter Lead
