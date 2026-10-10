---
title: A Cray-1 supercomputer replica from 30 "obsolete" Mac Minis
url: https://arstechnica.com/gadgets/2026/10/a-cray-1-supercomputer-replica-from-30-obsolete-mac-minis/
site_name: newsfeed
content_file: newsfeed-a-cray-1-supercomputer-replica-from-30-obsolete-ma
fetched_at: '2026-10-10T16:08:08.862390'
original_url: https://arstechnica.com/gadgets/2026/10/a-cray-1-supercomputer-replica-from-30-obsolete-mac-minis/
date: '2026-10-09'
published_date: '2026-10-09T21:51:12+00:00'
description: Stylish upcycling, with a retro flair, at Spain's Museo de Historia de la Computación.
tags:
- ars-technica
- tech
- apple
- cray-1
---

Text
 settings

TheMuseo de Historia de la Computaciónin Spain has unveiled a 1:1 scale visual replica of the famousCray-1supercomputer from 1976. Instead of sourcing expensive, cutting-edge tech to run the system, the creative team powered the project with 30 2012-era Mac Minis. Developed over 18 months, the project serves as a 50th-anniversary tribute to the Cray-1 and Apple’s founding.

Mac Minis from over a decade ago might not seem like the obvious first choice for building a cluster supercomputer, but when networked together, the developers can orchestrate the 64 active processing cores into a combined 1.3 teraflops of performance in their most recent tests. The museum reportedly achieved 1.5 teraflops previously using all 70 available cores, prior to one node going offline. Benchmarks were obtained using a custom matrix-multiplication Python script. Five PCs are quad-core i7s, and the remaining 25 are dual-core i5 models. Except for two units from 2014, the rest of the array dates to 2012.

The replica is a valuable tool for museum-goers to understand the shifts in computer architecture since 1976. The original Cray-1 used vector processing, applying a single instruction to multiple data elements simultaneously, whereas the replica distributes work across independent processors in a parallel cluster. The peak theoretical performance of the original Cray-1 was approximately 160 megaflops. What was originally a purpose-built research machine has been re-created with consumer hardware that’s vastly more capable than the machine that inspired it.

Rather than opting for a more standard Linux distribution, the team found thatmacOS Mojave (10.14)met their project needs by harnessing macOS’s built-in support forMPI(Message Passing Interface), the software layer that allows all the nodes in the cluster to pass tasks to one another.

 The Cray-1 replica, complete with iconic padded bench seating. The only thing missing is Robert Redford and Ben Kingsley having a discussion on SECTEC Astronomy. Credit: Museo de Historia de la Computación
 

 Credit:
 Museo de Historia de la Computación
 

 The Cray-1 replica, complete with iconic padded bench seating. The only thing missing is Robert Redford and Ben Kingsley having a discussion on SECTEC Astronomy. Credit: Museo de Historia de la Computación

 

 Credit:

 
 Museo de Historia de la Computación

 

Guests at theMuseo de Historia de la Computacióncan watch in real time as the system runs matrix algorithms, mapping the scale of system performance from a single core to the full suite running in parallel.

## Stealth supercomputing

Combining 30 consumer PCs into an operational cluster wasn’t the only engineering challenge the team faced. If you’ve ever stepped inside a server room, or, like me, foolishly installed one in your own basement, you know that fan cooling can beloud. The museum team used passive convection cooling via a steel rack chassis and aluminum tray mounts for each Mac Mini. Compared to the roaring thunder of a modern data center, this cluster is nearly inaudible.

 Macs are mounted vertically on aluminum racks in a steel chassis. Credit: Museo de Historia de la Computación
 

 Macs are mounted vertically on aluminum racks in a steel chassis. Credit: Museo de Historia de la Computación

 

The secret to the near-silence comes from vertical mounting. The PCs’ vertical orientation, combined with the steel chassis and aluminum trays, allows the tower to act as a natural thermal chimney. Hot air rises through the structure and out of the top grills without the need for added mechanical fans. According to the museum, the only noticeable noise inside the Cray-1 replica comes from two gigabit Ethernet switches at the base of the unit that register between 30–33 decibels, though the team plans to replace them with silent models. The fully assembled replica is said to make so little audible sound that you have to get right up next to the tower to be able to hear anything. While exact dB  measurements from inside the exhibit weren’t available, each individual PC is stated to produce12–15 dBA of noiseat idle.

## Mission control

To manage this quiet giant, designers built a custom terminal that looks straight out of a Cold War control room. The team combined elements of theDEC VT05andProcessor Technology Sol-20 Terminal Computerdesigns of the 1970s, even incorporating an analog control panel, with future plans to add original lamps from anIBM System/3. One master Mac Mini resides in the terminal and serves to direct all the other cluster nodes.

 Classic design elements lend the Cray-1 control terminal some retro style. Credit: Museo de Historia de la Computación
 

 Classic design elements lend the Cray-1 control terminal some retro style. Credit: Museo de Historia de la Computación

 

The original design had planned for the terminal to feature CRT monitors for added authenticity, but modern flat Samsung displays eliminated the connectivity headaches that come from attempting to bridge different technological eras. Future design plans will see 3.5- and 5.25-inch floppy drives mounted to the underside of the desk, and a 3D-printed shell will encase the keyboard to mimic the look of the classicHP 250 design.

 Mockup of the shell that will fit over the existing PowerMac G4 keyboard. Credit: Museo de Historia de la Computación
 

 Mockup of the shell that will fit over the existing PowerMac G4 keyboard. Credit: Museo de Historia de la Computación

 

## Targeting the TOP500

The Cray-1 team hopes to fill the currently empty second half of the tower through a crowdfunding campaign to secure 70–80 additionalM4 Mac Minis. The goal: create a cluster capable of ranking on theTOP500 supercomputerslist.

 The Cray-1 replica among its classic computing peers. Credit: Museo de Historia de la Computación
 

 The Cray-1 replica among its classic computing peers. Credit: Museo de Historia de la Computación

 

The replica is on permanent display in the museum, alongside two unused authenticCray CX1systems. TheMuseo de Historia de la Computaciónoffers guided tours on Saturdays from 11:30 am to 2 pm. Additional project information can be found on themuseum website.

 Nick Indge
 

Senior Technology Reporter

 Nick Indge
 

Senior Technology Reporter

 Nick Indge is a Senior Technology Reporter at Ars Technica covering hardware, embedded systems, and self-hosted infrastructure. A former security investigator turned tech writer, he writes to help readers escape subscription traps and regain ownership of their digital lives. He lives in Chicagoland with his family and a goofball husky.
 

1. 1.Feds get ready to rewrite car headlight rules
2. 2.Neanderthal wooden tools from Spain found preserved in stone
3. 3.AI disqualification yields new Nikon Small World in Motion winner
4. 4.A Cray-1 supercomputer replica from 30 "obsolete" Mac Minis
5. 5.SpaceX calls for better coordination in orbit after near-misses with Starlink

Customize