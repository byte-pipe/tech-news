---
title: 'Ask HN: Who''s still keeping a DOS machine up because the business depends on it? | Hacker News'
url: https://news.ycombinator.com/item?id=49848955
site_name: hnrss
content_file: hnrss-ask-hn-whos-still-keeping-a-dos-machine-up-because
fetched_at: '2026-09-26T14:54:22.288458'
original_url: https://news.ycombinator.com/item?id=49848955
date: '2026-09-25'
description: 'Ask HN: Who''s still keeping a DOS machine up because the business depends on it?'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Ask HN: Who's still keeping a DOS machine up because the business depends on it?
178 points
 by 
mlaux
 
19 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
174 comments
Do you currently work with or know anyone who is still using:

* dBase/Clipper/CLARION/Paradox/other DOS RAD environments on period hardware to run business processes?* CNC mills/spectrometers/microscopes/other industrial instruments controlled by ISA cards (either bespoke or standards like GPIB)?* Anything with a parallel port dongle?If so, I'd be very interested in hearing your experience here, or feel free to send me an email at the address in my profile. I'm not trying to sell anything, just doing some research for an idea around keeping these going on modern hardware.

 
help

freeli
 
16 hours ago
 
 | 
next
 
[–]

A certain nuclear power plant had a Windows NT 4.0 machine running as late as 2007. The reason is interesting.

The machine's purpose was to report status of the control rods that mitigate nuclear reactions. Basically, "are the rods inserted, and if so, how many / how far?". I want to emphasize that this was reporting only, NOT control.The original software was written back in the 80's, when the plant was originally commissioned, for AmigaOS. Of course, it's hard to buy Amigas anymore, and the original one died long ago (nobody remembers when).So in the mid '90s, the utility purchased an AmigaOS emulator that ran on Windows NT 4.0, which was current at the time. The emulator (IIRC) was developed by a firm in the UK. The firm went out of business sometime in the late '90s. The control rod monitoring software ran under this emulator on top of NT4.Windows NT 4.0 was the last OS to allow the emulation software direct access to the physical hardware that produced the status signal. Later versions of Windows abstracted the hardware access away, and the monitoring software broke. Because the emulation company had gone belly up, there was no way to fix the incompatibility.So the utility had a choice: get new hardware/software certified (by NRC?), or keep doing what they were doing with the software (and hardware) that they had. They chose the latter.So this is how, in 2007, during a tour of the facility, I stumbled across a Pentium 1 system running an AmigaOS emulator on Windows NT 4.0 that was responsible for displaying the status of the control rods of a nuclear power plant.Spare hardware for this setup was purchased off of eBay and stocked on an adjacent shelf.

reply

justin66
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

To me the funny part of this story is that they used to show you this warning as part of the EULA when installing Windows NT 4, which I remember joking about:

NOTE ON JAVA SUPPORT. THE PRODUCT MAY CONTAIN SUPPORT FOR PROGRAMS WRITTEN IN JAVA. JAVA TECHNOLOGY IS NOT FAULT TOLERANT AND IS NOT DESIGNED, MANUFACTURED, OR INTENDED FOR USE OR RESALE AS ONLINE CONTROL EQUIPMENT IN HAZARDOUS ENVIRONMENTS REQUIRING FAIL-SAFE PERFORMANCE, SUCH AS IN THE OPERATION OF NUCLEAR FACILITIES, AIRCRAFT NAVIGATION OR COMMUNICATION SYSTEMS, AIR TRAFFIC CONTROL, DIRECT LIFE SUPPORT MACHINES, OR WEAPONS SYSTEMS, IN WHICH THE FAILURE OF JAVA TECHNOLOGY COULD LEAD DIRECTLY TO DEATH, PERSONAL INJURY, OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE. Sun Microsystems, Inc. has contractually obligated Microsoft to make this disclaimer.Also:The machine's purpose was to report status of the control rods that mitigate nuclear reactions. Basically, "are the rods inserted, and if so, how many / how far?". I want to emphasize that this was reporting only, NOT control.It would take a whole lot more context to make this somehow comforting. :D

reply

throwaway2037
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is a great post. How does someone write software that needs to run for ~50 years where the hardware will need to be replaced with non-equivalent, newer hardware? If I were facing this issue 
today
, I might start with an OS that has excellent emulation. Example: Can I run 32-bit MS Windows 95 via emulation on a variety of current 64-bit OSes, like MS Windows, Linux, AIX, HP-UX, etc. If yes, then we can assume(?) this emulation will remain relatively stable even if we upgrade our hardware later. Maybe I am overthinking the whole problem: Can VMs do exactly what I want today? Will VMs running 
ancient
 OSes, such as 32-bit MS Windows 95, continue to be stable/viable in the future? I am unsure.

reply

ninalanyon
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Make sure that you have as thorough a specification of what the system is supposed to do as you can.

Then define the version control system and the build process, specifying the dependencies, and so on.Think about any opaque blobs in the system and try to eliminate them so that you have plain text source code so that no tools are needed to read the code.Make sure that the build process runs entirely locally and never fetches anything from outside.Simplify everything, use only tools and languages that are well understood and supported.The real problems are not strictly technical but social: how do you prevent loss of the code, the tools, the specification, how do you maintain the expertise needed to maintain it. How do you ensure that all those things that are obvious to you now are written down in all their gory detail so that your great grandchildren will not apply their new and different preconceived ideas to the system?Document all this on paper as well as electronic storage, make sure that version ids are recorded on every page as well as being available to the user of the machine or program.In the industry in which I worked for the last thirty years of my career it was not uncommon to have things come back for repair after fifty years use and to be able to consult the original drawings and bill of materials so that exact replacement parts could be made.

reply

jl6
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> How does someone write software that needs to run for ~50 years where the hardware will need to be replaced with non-equivalent, newer hardware?

Some ideas:Write it in a popular language/ecosystem, stick rigidly to well-defined APIs, use commodity hardware, flatten out any malignant cleverness, maintain documentation onwhyevery part does the thing it does, and make the source code readily available.This is based on working with some very old systems, and each point above is the opposite of something that made life harder.

reply

dmos62
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> how does someone write software that needs to run for ~50 years where the hardware will need to be replaced with non-equivalent, newer hardware?

Make it open-source, or don't buy without source.

reply

ndsipa_pomu
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I'd recommend not having it so dependent on the hardware and choose an OS that is relatively hardware agnostic (e.g. Linux). Also, ensure that the software is open source and if compiled, has an open source toolchain to do so.

Though people often decry it (due to the many, many footguns), writing something in Shell/BASH will make it trivial to move to newer machines.

reply

Froedlich
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

A friend works for an airline as a flight simulator tech. Their entire software stack, including the compiler and OS, is FAA-certified.

Then their ancient Honeywell(?) mainframes reached end-of-life they scouted for compatible hardware, of which there was none. The cost of certifying new software, plus the time involved, was astronomical. So, after consulting with the FAA, they paid a hardware company to clone the ancient mainframes in modern silicon. The FAA signed off on it, and they had all-new computers - much smaller than the originals - running the old stack.

reply

zx8080
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's _very_ hard to believe some company to simply "clone the mainframe" into chip. Mind sharing any link to this effort?

reply

mitxela
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Custom chips aren't as expensive as you think. About a few million dollars for the design and a hundred thousand chips, way out of reach for a hobbyist, but accessible to large enough companies. Just because it's opaque to us software people doesn't mean it's not a real industry you can buy things from.

reply

realo
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And all that expensive engineering is still less costly AND faster (!!) than a new software certification.

Cannot refrain myself from asking why ...

reply

ianjbutler
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Situation: Software-1 on Platform-1, both certified.

Time-evolution: P1 is deprecated, replaced by uncertified P2, but S1 remains certified.. just nowhere certified to run yet.Solution: There'sanothersoftware S2 which originally vouched for P1, itself still certified, which can still be used to certify P2.Counterfactual?: If S1 were deprecated in favor ofnewS3.. there'd be no plan to certify it!The problem: None of this actually makes any sense! But we're trying to fake due diligence. Everyone knows the hardware/platforms kinda need to be certified with respect to each other anyway, but if we did it that way it would all be even more expensive an time-consuming.

reply

mitxela
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Doesn't seem crazy to me. Which one do you suppose needs more proof of correctness: a cake recipe, or the oven you bake the cake in? The recipe has to be correct or the cake won't work, but the oven just has to hold a temperature.

reply

flyinghamster
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It could be an FPGA. Given enough gates, and the know-how to program them, you can make an FPGA emulate anything. Speed and efficiency could be better or worse, but if you're targeting old hardware, better is likely.

reply

vincent-manis
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

When Xerox established PARC, they asked the assembled scientists what computer they wanted. The majority view was a DEC PDP-10 KA10, with the BBN memory management unit that let it run Tenex (the ancestor of DEC TOPS-20). Xerox couldn't really buy a competitor's mainframe, so they built MAXC (maximum access computer), which was a complete emulation of the Tenex machines.

reply

zem
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

very apt that xerox parc was full of tenex engineers!

reply

znpy
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Meh, old architectures are relatively simple and you can get 95% of those via fpga softcores (some freely available, some paid) and run them on fpga. The rest can be implemented by a proper ee team.

reply

theodric
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I mean...there's some precedent. The XKL TOAD ("Ten On A Desk") implements the PDP-10 instruction set, and will happily run TOPS-10/TOPS-20. LCM had one doing just that.

https://www.computerhistory.org/collections/catalog/10277383...https://www.twenex.org/?network

reply

betaby
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That's interesting. That means there are fewer checks for hardware than software?

reply

hulitu
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Software "engineers" like to abstract things. This doesn't pay well e
with reliability.

reply

soulofmischief
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hardware is more amenable to static analysis than running programs which may receive an arbitrary number of inputs and express an arbitrary number of possible intermediate states.

I am interested in how firmware is treated, since perhaps in the case of these old machines it's small enough to be analyzable or at least cloned bit-for-bit.

reply

CobaltFire
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Having worked on nuclear plants (as a reactor operator) around that time this doesn't surprise me in the least.

Thats far more advanced than the systems I worked with, one of which reported rod position via resistance measurement on a brushed cylinder (one for angular and one for depth).Cleaning and calibrating those was a constant maintenance item every time the reactor was shut down.

reply

the__alchemist
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It is wild to me that you would use any GPOS for something like this instead of dedicated firmware for the task. This is evoking similar reactions to when I read articles about infrastructure being hacked remotely: Something must have taken a wrong turn with the architecture design for this to happen!

reply

rkagerer
 
30 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nothing wrong with this.

If it ain't broke, don't 'fix' it.

reply

kccqzy
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Did they not need NRC recertification when they moved from a physical machine running AmigaOS to an AmigaOS emulator?

reply

freeli
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That is an advanced question best asked of the folks in charge of the plant. At the time I was just trying to figure out how to explain to the IT auditors why there was no antivirus software on this piece of crap.

reply

CursedSilicon
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Could you skirt around it and just remark "there are no viruses for AmigaOS"

(Probably notliterallytrue. Butfunctionallytrue in the sense that they were likely transmitted via infected floppy disks, of which there'd be virtually none left in the wild in 2007)

reply

kamma4434
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hello, my name is Lamer Exterminator, pleased to make your acquaintance.

https://en.wikipedia.org/wiki/Lamer_Exterminator

reply

freeli
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It wasn't the AmigaOS running in the emulator that they were worried about, it was the Windows system running the emulator. (Not that the average IT auditor there could have understood the difference.)

reply

M95D
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

How would a virus get in there?

reply

EvanAnderson
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If it were a newer version of NT I'd be concerned about USB media, but being NT 4.0 and not supporting USB it's imminently more capable of being air-gapped than later versions. (I recall a fun Ed Skoudis quote-- "At best, an air gap is a high-latency connection". Evidence Stuxnet.)

reply

jabl
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The auditor probably doesn't know nor care. "Every windows machine runs antivirus" is a checkbox item, zero thought involved.

reply

rcxdude
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Depends. A lot of these audits are quite prescriptive and don't leave much room for actually thinking about the problem. There is often some kind of mechanism for 'this is sufficiently segregated it doesn't matter that it's utterly out of date' but then usually some awkward rules develop that prevent some things from being put into that category. More subtly you can get whether the thing even exists as a thing that the audit cares about, and that often depends on the framing (embedded software is often invisible here but it needs to not look too much like a general-purpose OS even though it often is).

(Also, in my experience, what the auditors think the rules are and what is written down can often be divergent and even contradictory)

reply

slicktux
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Was this status indicator simple vertical bars that were black and white and displayed on an old CRT Monitor? 
Almost looks like black and white terminal vertical bars (like Alsamixer)?

reply

gerdesj
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

"Windows NT 4.0 machine running as late as 2007"

lol. I know a ... factory, that had a BBC model B (with a rather complicated wiring loom) still doing a job around that time.The IT supplier at the same factory went to a museum in Cambs. around late '90s, early '00s to ask if they could buy an exhibit because something had failed locally. The museum gave them the part.That was just aerospace and nothing fancy like your nuke plant!

reply

icedchai
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm curious, how did the hardware present itself? It couldn't have been an Amiga Zorro card since it would've been impossible to get that into a PC. Did it connect over a serial or parallel port?

reply

freeli
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I recall it being some custom ISA card with connectors on the back. The emulation software had drivers that interfaced directly with the card.

reply

icedchai
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Interesting! So they were able to port the hardware but not the software for whatever reason?

reply

ErroneousBosh
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If it's what I suspect it might be, it was probably a generic IO card with maybe a bunch of 8255 PIOs on.

reply

tombert
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I find it deeply upsetting that anything important for a nuclear power plant is using an OS without protected memory.

reply

M95D
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Protected against what?

reply

tombert
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just another program poking memory it’s not supposed to. Not even necessarily maliciously.

reply

JdeBP
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That AmigaDOS emulation will almost certainly never run another program. (-:

Far more concerning from a RISKS point of view is the spare parts being physically in the same place as the live machine.

reply

vincent-manis
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This reminds me of the apocryphal story of the IBM System/360 running a 1410 emulator that ran an IBM 705 simulator that ran a business-critical application.

reply

JdeBP
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not 
wholly
 apocryphal. The U.K.'s air traffic control ran, and possibly still is running, on an IBM 4381 substituting for an IBM 9020.

*https://news.ycombinator.com/item?id=49763972They've reportedly already tried,and failed, to replace it with a more modern system.

reply

genxy
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Which is why we should target VMs directly. Then that VM can be brought forward to new platforms rather than emulating the entire machine, not that emulating the entire machine is bad. One could argue that the emulation stack you outline was made possible by putting in the work to make simple, fully specified and documented hardware.

reply

ikidd
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

NT4.0 in 2007? That wasn't even very late. I was replacing NT4 servers into the early 10s. Car dealerships were terrible for keeping that crap around.

reply

ptek
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If it's still running I wonder what they are going to do about the year 2038.

reply

mitxela
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Set the date back to 1980 and sticky tape over the corner of the screen where the date is displayed.

reply

DoctorDabadedoo
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I wonder if there is push in the public sector for open source software/hardware for cases like this.

I completely get the decisions over time here, but it's unsettling having a relevant piece of software (reports are important too!) working on with parts from ebay, in 50 years time they might be gone.

reply

NegativeK
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've dreamt of governments hiring devs with promises of full time OSS work. It _might_ get some people over the lower salaries of government work. But I overheard a state CIO once say "We configure, we don't create".

That's to say nothing about opinions of open source that rival early 2000s Microsoft.For old ass critical software and hardware, the org can always have a backlog of hardware and contingency plans (paying someone to fix the hardware, paying someone to create a fully certified and modern solution..) for when they start running out of parts.

reply

sajithdilshan
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is crazy. Why on earth wouldn’t the respective government spend money to modernize a critical infrastructure like a nuclear power plant?

This is how we would end up with nuclear disasters, not because the technology is bad, but purely because of mismanagement and human negligence.

reply

onion2k
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is crazy. Why on earth wouldn’t the respective government spend money to modernize a critical infrastructure like a nuclear power plant?

Safety and reliability come from understanding the system. Something that's old but that you knoweverythingabout is far safer than something new. This risk is that the people who know move on, or the sources of replacement parts stop working, or that other things around the system change. Then the risk curve inverts and you find the old system more of a liability than a asset.Almostalwayspeople choose to update things either too early or too late. Knowing when to do something is hard.

reply

sajithdilshan
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That’s pure negligence. It’s not like the people that have the know how disappear suddenly . It’s the responsibility of the management to make sure the knowledge transferred to new generation.

I guess that kind of thinking is what led to the collapse of ancient civilisations like why even bother to improve anything and let everything decay and die out

reply

somenameforme
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can only say such things with hindsight. In the moment, nobody knows what the future will hold. Take the space program in the US for instance. In 1969 we landed a man on the Moon. We'd repeat that several times until 1972. At that point Nixon made a speech which implied various unpleasant things about space's future, but he'd be out of office, disgraced, a couple of years later, so how big a deal could it have been anyhow?

I think almost nobody from that era would have believed you if you told them that more than 50 years later not a single human would have traveled beyond low Earth orbit, and that we'd now be struggling to recreate what we did in 1969. Furthermore a significant chunk of the world doesn't even believe we landed on the Moon anymore, no doubt in part because of this apparent anachronism.It's not like there was any sort of collective or even singular decision to just let things die out. I mean sure Nixon did his thing intentionally, but even as a President in the golden years of the US, he was still just one man.

reply

onion2k
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It’s the responsibility of the management to make sure the knowledge transferred to new generation.

That's just lazy thinking, and probably a sign you've never been a manager. For all the responsibility to lie with management you'd have to be leading people who enthusiastically do what they're asked to do, raise problems, document things, follow processes, and make sure everything is handed over to the next person when they leave.That's not how people are. They'll have times when they're unmotivated, underpaid, grumpy, over-worked so they miss things, etc. That's when the organisational tech debt starts piling up, and there's nothing a manager can do to stop it except manage it as best they can even though they're under the same pressure, with the same lack of motivation and crap pay as everyone else.It's so easy to think you can fix it just by keeping on top of it and micromanaging where it starts to show up. It doesn't work that way.

reply

philipallstar
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> This is how we would end up with nuclear disasters, not because the technology is bad, but purely because of mismanagement and human negligence.

I'm pretty sure constant upgrading would be more likely to cause disasters.

reply

VBprogrammer
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I can only imagine how much less reliable a modern JavaScript Electron app would be in this role...

reply

cromka
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If it's not broken, don't fix it.

Same reason why MTA in NYC still operates subway using 100 y/o signaling hardware on most of the lines.In a way, your comment and the responses you get is a perfect allegory to inexperienced vs experienced engineering.

reply

jodrellblank
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But similar reasoning is why Canadian trams are worse than other countries, and it's not "good experienced engineering". In this nearly hour long rant by NotJustBikes[1] the section I've linked is about the technology and how the transit authority will not move on from 100 year old track technology which makes everything worse for customers. There are junctions where tram drivers have to stop and look at the track to make sure the junction is correctly set because the single-point switching is less reliable than modern designs. Or the driver has to stop the tram and get out to use a stick to move the track and change the junction because they aren't electrified. And then pass through junctions as slowly as 10km/h because the old track design has higher risk of derailment than modern designs.

The designs for the electrified track switches were made by one company which was sold, re-sold, and then burned down and the designs lost, and there isn't anywhere else to buy them because nowhere else uses such old track design anymore, so not only is Toronto struggling to buy parts to continue electrifying the manual junctions, it's struggling to custom-make enough replacement parts to keep the aging electric switches working faster than they fail.And they were using trolley poles to connect to the overhead power lines instead of Pantographs until 2017, 50-100 years after everywhere else, which meant a) they couldn't get enough power through them to run air conditioning, and b) they are more likely to fall off the power line and the tram stops and the driver has to get out and reconnect them, and c) their newer trams now have to have custom dual-power connections to go through older parts of the network, and d) the carbon shoes on the trolley poles wear out quicker which means the trams are dirtier and taken out of service for maintenance more often in the wet which is when people want to use trams more.[1]https://youtu.be/HhQxNHrD6fA?t=2311

reply

mitxela
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Their 100 y/o hardware is built from stuff that's still produced though. We still make relays (not identical ones but ones that perform the same function), wires, and mechanical levers. The system's behavior is not encoded in the relays but in the connections between them. If you had a CPU made of separate transistors you could replace burned out transistors with any future transistors but if you had one made of chips you'd need those exact chips that were out of production.

Replacing the relays in old telephone switches is a problem because they use so many weirdly specific types of relays - but those systems are only found in museums now. I believe track control uses fairly ordinary DPDT, etc., relay designs.

reply

sajithdilshan
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> If it's not broken, don't fix it.

I understand that way of thinking for a small business computer system. Not for a critical infrastructure. Also if people actually thought about like that we would still be in stone age, like why invent something new or use a new technology? Keep on using rocks to crack nuts and kill animals

reply

sokoloff
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think you can imagine the difference between “I did some work and made this thing that is clearly better, but we might have a few kinks to work out” and “I did some work, and if I did it perfectly, it’s just as good as the old thing, but we might have a few kinks to work out.”

reply

IG_Semmelweiss
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Lindy's law:

For non-perishable things - i.e technologies, ideas, books, institutions - the expected remaining lifespan is roughly proportional to how long they have already survivedTime acts as a filter: what has already withstood a long stretch of disorder is more robust, so the longer it lasts, the longer it is expected to last.The old nuclear software running on mainframes have passed the test of time. The new software, has yet to.Nassim Taleb talks about this at length in his book, Antifragile.

reply

cube00
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Why on earth wouldn’t the respective government spend money to modernize a critical infrastructure like a nuclear power plant?

Same reason they don't modernize health care infrastructure. It's too expensive, people die if they get it wrong and they get voted out of office for their troubles.

reply

mitxela
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Now you know why "nuclear power may have been dangerous in the past, but with modern technology it's completely safe and Chernobyl will never happen again" is not a good argument.

reply

idiotsecant
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Now you know why making arguments from 20 year old anecdata makes you look foolish

reply

sajithdilshan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Chernobyl didn’t happen because of technological blunder or even human negligence. It happened because poverty caused by communism in Soviet Union had to use old outdated (not the modern nuclear technology at that time) graphite tips in carbon rods because it was cheap and also kept it as a secret from the facility operators giving them a false sense of trust on the kill switch.

Chernobyl is the perfect example to not use outdated old technology. Had they used the modern western technology at that time to upgrade their nuclear reactors the kill switch would have prevented the whole disaster instead of increasing the neutrons make the core a nuclear bomb.Next time educate yourself with facts before making a fool out of yourself

reply

HPsquared
 
7 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Chernobyl was very much not "old", it was a more modern design than the PWRs which are built today. Chernobyl Unit 4 was also basically brand new, only 3 years old at the time of the disaster. The RBMK design dates from the 60s, whereas the PWR is from the 40s.

reply

lukan
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"Had they used the modern western technology" ... "Next time educate yourself with facts before making a fool out of yourself"

But you are aware that this thread is about a reactor in the west, that "updated" their certified hardware to a VM instead running on windows NT?

reply

mitxela
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Everyone knows that all technology newer than Windows 2.0 will never be obsolete!

reply

carlosjobim
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

There is no reason a more modern system would be better in any aspect.

reply

TMWNN
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>So this is how, in 2007, during a tour of the facility, I stumbled across a Pentium 1 system running an AmigaOS emulator on Windows NT 4.0 that was responsible for displaying the status of the control rods of a nuclear power plant.

Vernor Vinge'sA Deepness in the Skydepicts a human society thousands of years in the future, in which pretty much all software has already been written; it's just a matter of finding it. So programmer-archaeologists search archives and run code on emulators in emulators in emulators as far back as needed. <https://web.archive.org/web/20231114211656/http://www.gareth...>(Heck, recently I migrated a VM to its third hypervisor. It began as a physical machine a quarter century ago.)

reply

freddealmeida
 
6 minutes ago
 
 | 
prev
 | 
next
 
[–]

An old story. I used to work for Fox Home Entertainment (CDs etc)this is 20+ years ago. And we had proper DOS running on old machines. We used it to do all our finances (including all of Japan, Asia sales). Most of the money we made on movies like Titanic were tracked on DOS. Until about 2003 if memory serves me where we moved to SAP. Why this was worrisome was how easily fraud occurred. In my tenure there $5-10M was stolen. At the time sent to companies in Brazil. I'm still surprised by larger firms where they keep these things alive to retain the data. CocaCola did it. A few large Insurance firms too. Crazy.

reply

jjbinx007
 
23 minutes ago
 
 | 
prev
 | 
next
 
[–]

Not DOS but we recently had to virtualise a Windows XP box as it was running crucial software for a visitor attraction. The software was written by a member of staff who sadly passed away and the PC it was running on was approximately 20 years old.

We managed to virtualise it and then run it in a VM, and it needed a couple of USB-to-serial adapters passing through as well.We're also finding some kiosks are running Shockwave Flash apps provided by companies that are no longer trading. We can decompile the files to extract the assets but at some point it's easier to just replace completely.

reply

sse
 
4 minutes ago
 
 | 
prev
 | 
next
 
[–]

I do, for two clipper programs. But no extra machine, just a VM.
Until not long ago, it was running without VM on 32 bit Windows 10.

reply

yitchelle
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Not MSDOS, but I feel obliged to shared the story of an auto shop in Poland using a Commodore 64 to run the calibration and wheel balancing some years back. It was viral news at the time but worth sharing again.

https://www.youtube.com/watch?v=tXdLtnt-nvEOriginal Polish article -https://www.trojmiasto.pl/wiadomosci/Warszatat-samochodowy-z...

reply

proxysna
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

2014-2017 I was supporting a clipper setup for issuing work order and many other tasks for an old civil aviation repair plant. I’ve ended up virtualising and moving it to a hyperv cluster. Definitely the case of “if it works, don’t touch it”.
Also set up a closed network for CNC machines to let engineers in the shop send jobs over the net instead of running around with floppies or manually entering gcode through the console.
Fun times.

reply

AugustoCAS
 
16 minutes ago
 
 | 
prev
 | 
next
 
[–]

I don't, but the abbey at the city I live has an ancient PC running a program from the 80s that controls the bell ringing.

I recall seeing it connected via a parallel port to a large board that then operates the switches/relays of the hammers.

reply

rleigh
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Not any longer. Back in the mid-2000s the company I worked for sold point-of-sale systems based upon a multi-user 4GL application (TAS Pro). Similar to dBase/Clipper etc., using the Novell Btrieve ISAM database engine.

With the advent of USB and SATA we ceased to be able to source industrial embedded x86 boards which could run the application. At the time this was with Novell DR-DOS, which was relatively modern in terms of hardware support but still behind the times and we were struggling to manufacture new systems. The company was very small, so a full rewrite was investigated--I did a prototype using PostgreSQL and Gtkmm--but it wasn't realistic. Today, an AI could probably do a full rewrite in a day or two, including migration tooling. Back then, it would have been a multi-year effort for one person given the application's size and complexity.My solution was to run Linux since it had full support for the hardware. Debian Sarge at the time. This used a Perl frontend and dialog(1) to present a simple menu system at startup. This did backups, software updates (over dialup!), remote access for support (again over dialup), ran backups and ran the main application. It would start DOSEMU which provided the application with VGA display, COM ports and parallel ports for the application to drive "directly" (from its perspective). It also used Samba and CUPS to provide the DOS environment with shared network drives with exclusive byte-range file locking needed for the multi-user network database to work with concurrent users without data corruption, and also multi-user report printing and receipt printing.I left the company a year after this was put into full production, but the last I heard it kept the company viable with a supportable product for many years after until its owners retired. This kept software from the early 1990s running well into the 2010s, and there are likely still sites running it to this day.

reply

Felger
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Not DOS, but I sold a '99 HP computer running win98 last month, to replace an identical failed system. It was used to control a 50 meters long custom industrial paint booth line for special equipments (like 57" rims). Luckily, their HDD was OK. Urged them to make a few sector-to-sector copies of it on a few spare HDD. This $100 sell surely has prevented this business from massive bills or even going bankrupt in the meantime from production loss.

reply

adithyassekhar
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Think that’d be worth more than 100 :)

reply

shakna
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

dBase, MS-DOS 3.x, not using industrial anything. And as its a front of house tally machine, there's literally zero incentive to ever upgrade it. Downtime is measured in the yearly reboot, but there are non-operational business hours, so everything is just scheduled around that.

We've already got it running on modern hardware. It's running under qemu. And the dBase stuff gets ripped out and sent to a REST server for broad monitoring and so on.We... Have one small oddity? There's a tape backup system, that throws everything through the soundcard. (Sound Blaster only.)Would be nice if onboarders didn't see dBase and just throw everything at AI instead of actually learning the skills they'll need when data migrations happen. But that's a people problem that can't be solved with tech.

reply

mococa
 
2 minutes ago
 
 | 
prev
 | 
next
 
[–]

Not now, but few years ago I worked on a toll that runs DOS because… yes.

Also worked ~2014 DOS slot machines - in next year we ported to Linux

reply

Kuyawa
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

One interesting thing of living in the AI era is that every single one of these old apps (that people still use and never paid big money to upgrade because it it ain't broke don't fix it) can now be rebuilt for $5 in ten minutes if you really know what to do (YMMV)

If you don't know, you'd have to pay an expert big money to do that and the migration abandoned just like before, so another decade will go buy until AI does that without permission just because it found a possibility for optimization and it is instructed to do so without human approval, because governments

reply

asciimov
 
1 minute ago
 
 | 
parent
 | 
next
 
[–]

You would think so, but most of the low hanging fruit has already been rewritten and replaced. The biggest hurdle is hardware lock in, ISA boards, hardware keys, or other hardware interfaces that can’t be easily connected to new systems. Never mind the problem of verification. That app that takes days to rewrite can annoyingly take months to verify.

reply

reddozen
 
7 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> if you really know what to do

The so called "load-bearing gap" you pay experts for.

reply

Aldipower
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

The Detusche Bahn still runs DOS and Window 3.11 in their ICE I trains! They searched for admins 2 years ago. 

https://www.tomshardware.com/software/windows/ms-dos-and-win...

reply

tefkah
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

i don’t want to say this explains things, but i do want to imply it

reply

carefree-bob
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You should check out the NYC subway, which has electromechanical relays, cloth covered wiring, and pre-WW2 analogue panels.

They do not even have an OS!

reply

alexpotato
 
40 minutes ago
 
 | 
prev
 | 
next
 
[–]

Not DOS but another dad in my town works for one of the opera houses in NYC.

They have what are called "supertitles" [0] so that people can follow along with what the opera singers are actually saying. There is one on the back of each seat in the theater.As near as I can figure, it's basically hundreds of LCD displays on some kind of bus network and connected to a computer via serial connection aka "D pin connector".The software only runs on Windows XP and he has to keep finding old Windows XP machines on eBay in order to keep it working. I think he also has a couple hard drive images of the working OS + software.I had suggested using a USB to D pin adapter and then use an LLM to sniff the protocol and then reverse engineer it.His response:"It HAS to work correctly. In 30 years we've never had an outage with the old system."0 -https://en.wikipedia.org/wiki/Surtitles

reply

indrora
 
2 minutes ago
 
 | 
parent
 | 
next
 
[–]

Ah, that sounds like it's The Met, who have a bespoke electronic libretto system.

You're right, itisa bunch of LCDs on a bus (iirc rs485).

reply

throwup238
 
59 minutes ago
 
 | 
prev
 | 
next
 
[–]

I don’t know the specifics of their systems but both of my local lumberyards here in SoCal still use DOS systems for their point of sale and inventory management, with slow dotmatrix printers and everything.

They simply have no reason to modernize. The one big benefit they’d have is an online inventory system but they make most of their money from negotiated bulk orders so there’s zero incentive.

reply

pumplekin
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Not DOS, but two similar era cases.

A FTSE 100 company I used to work for, still maintains a SCO UNIX machine that was first installed in 1993. It hasn't had any upgrades since, has specialist hardware in it, and still has an IP stack that is classful (ie. no subnet masks, 10.x.x.x is always a /8). It runs in a 100% airgapped network, and it isn't essential to keeping the core companies operations, but it is a ticking time bomb nobody seems to want to address that will cause a lot of distruption when it finally dies.Also I was recently (very lightly) involved in a consultancy project to remove an OS/2 based point of sale system for a small local retailer with 6 stores.

reply

adithyassekhar
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

If you don’t mind me asking, how can a thing that causes disruption when it dies still not be considered essential?

reply

BlackRabbit1
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Blind Control for the C-Suite?

reply

londons_explore
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

This thread reminds me that there is a 
huge
 benefit to using a super common OS+hardware.

In 30 years time it will all be outdated... But emulators will exist and a business process in 2050 that still depended on something I built today could still run with minimal effort or risk.

reply

chr15m
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

If you have the source code it's going to be a lot easier to continue.

reply

hulitu
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It depends on the gcc/llvm version.

reply

amelius
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I bet most AI is capable enough now to migrate you away to some emulator for a few dollars.

And I would even bet that in most cases you could run a solution on a sub $10 board from aliexpress.

reply

MarkSweep
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A company I used to work at still ships a piece of hardware with an Intel 186 microcontroller in it. The compilers are 16-bit DOS applications and the tool to program the DIP packages with the program was also a DOS application. I’m not sure what the physical interface between the programmer and computer was.

reply

deathgripsss
 
43 minutes ago
 
 | 
prev
 | 
next
 
[–]

Still have a liquid scintillation counter running on DOS with raw data printed on a dot matrix

reply

andix
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I had to keep an old clipper/dbase application running until recently. It worked perfectly seamless with vdos (vdos.info). It's commercial software, but very reasonably priced. Dosbox is another alternative, but didn't work as well with printing and I think also wasn't able to do row locking of dBASE databases over the network.

reply

M95D
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I had a functional STA Compact [1] coagulation analyzer until 2022. It ran a customized DOS version on a ITX computer board that was integrated into the analyzer. UI was in text mode and used the keyboard only. It had no mouse. The video in the link shows the UI for a few seconds at the end. We kept it functional as a backup and even used it a few days when the replacement broke down. It was one of the best analyzers I ever used.

The newer version of that anaylzer, STA Compact Max [2] has mostly the same analyzer hardware, but newer ITX board inside. It runs Windows (XP, 7, 10...). Bugs galore.I know labs that used a Beckman-Coulter HmX hematology analyzer [3] until 2015 or so. That machine is attached to an external MS-DOS computer via a very thick cable and an ISA board. The cable connector looked a bit like a 68-pin SCSI-3. The software used VGA graphics mode.[1] https://www.youtube.com/watch?v=Kti6Zdyp8dQ
 [2] https://www.youtube.com/watch?v=MJan25vkpEA
 [3] https://www.soriaudio.com/index.php?mid=m_eqp&document_srl=62138152

reply

83457
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

My dad ran a commercial 2-way radio business. There were multiple radios with programming software that would not work on anything above a 386 and DOS. He had a couple computers from the late-80s running for nearly 25 years, though I think he had to replace one of them with another of similar vintage. Also, had a 486 that he used for customer notes in WordPerfect up to about 2015.

I suspect he could have found a way to use a newer computer, but if it ain’t broke…

reply

betaby
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Intel was seling 386 CPU up until 2007. I personally was using brand new special equipment with 386 soldered to custom MBs with no VGA, serial only access.
I suppose you can purchase such boards from ebay/recyclers today.

reply

Froedlich
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I still have a circa-1996 486 running Windows 95. It has an EPROM burner card and software that I use to reprogram the ECM in my car.

The cost of upgrading to modern software and hardware is substantial, plus the learning curve for something I only do rarely nowadays.

reply

_trampeltier
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Siemens Field PG. It is a rugged Notebook for PLC programmers. At least in the last version until last year, the "Field PG M6" was possible to buy the Notebook with a special serial port for old S5 PLCs ant the Step5 software came in a special DosBox version with it.

The Field PG has also another special port called "MPI/Profibus" for S7 PLCs, 2 Ethernet ports and a DVD drive.https://support.industry.siemens.com/cs/document/109766662/d...

reply

fires10
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I work at a multi billion dollar facility for a Fortune 100 company and we still depend on DOS. Keeping the mandatory DOS machines going is an exercise. Especially integrating them into modern systems.

Edit: There is no required hardware, however maintaining a stable serial connection through a VM and timing issues due to faster hardware has been fun.

reply

mlaux
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

The serial port stuff is very close to what I'm working on - what's on the other end of the connection? What does "integrating them into modern systems" look like for you: getting data out/pushing data in/both?

reply

fires10
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We typically integrate them by encapsulation. Building multiple layers of more modern systems for them to communicate through. A combination of Windows and Linux boxes. The other end of the connection is very old industrial equipment. This is not to run the equipment per se but to configure and program it.

reply

1over137
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Actual MS-DOS or FreeDOS?

reply

fires10
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

MS-DOS or Windows 2003 running DOS vdm.

reply

sgerenser
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Does the idea make use of 
https://86box.net
? Just heard of this recently on hn and it seems promising for anything that requires low level/cycle accurate emulation vs. your typical high level emulator.

reply

mlaux
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

My idea is a DOS emulator with a really thorough log of every DOS interrupt called and I/O port interacted with. This could then be used to automatically, say, insert rows into a sqlite table when the DOS app updates a .DBF file, or forward GPIB data to a modern USB adapter. I wanted to avoid low level/cycle-accurate emulation as much as possible, only adding quirks as needed to support the most popular business application suites.

reply

Froedlich
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Me!

I have a client with some business software that runs on DOS. They have a dozen seats. A single Linux server gives serves a dozen VNC sessions with the software running in DOSEMU. Printing is done with the Linux print stack and three Ethernet print servers.It has been working without a hitch since 2008. Oh, so has the server, which is a VirtualBox VM.

reply

andix
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Just out of curiosity: is it possible to somehow attach an ISA Adapter via USB to a VM? ISA does depend a lot on DMA and timing, but the clock is only 8 mhz and gives a software layer on a modern cpu a lot of time to do stuff between ISA bus cycles.

Keeping old hardware running is very fragile. Most spare parts are decades old now too, and nobody knows if they still work properly.

reply

Teknoman117
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

To a VM? Possibly.

The DMA might actually be the easy part.The main concern is how many VM exits per second a modern CPU can handle. Even though the interface is "slow", you can probably do ~500k to 1 million IN/OUTs or MOVs per second to ISA. You'd have to trap (VM exit) every access to a IO port or memory within the ISA window.During the pandemic I cobbled together a KVM-accelerated emulator for an old 386EX based board I had and trapping every memory access to IO was slower than the real hardware.

reply

lysace
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

USB and VM latencies are both questionable here, I would think.

ISA motherboards still work and have been mass produced in the hundreds of millions. (I have about a dozen in my retro closet.)The esoteric ISA expansion cards would be the bottleneck, not the motherboards.

reply

andix
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

All those layers add some latency, but 8 mhz is really slow. USB 4 can do extremely low latency, otherwise PCIe over USB wouldn't work.

reply

labcomputer
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The problem is that a lot of those old ISA drivers were peeking and poking card registers as fast as the bus would allow, which was over 1 MHz (less than 1 microsecond per transaction), not DMAing data to RAM (though some did that too).

With a modern 4 GHz CPU, that means your budget is only 4000 clocks per interrupt. The context save alone can make it hard to hit 1MHz, and you really want to have your interrupt code pinned to the L1 cache because a few memory reads will blow your entire budget.As nice as USB4 is, I’ve never heard anyone claim it has single-digit microsecond latency, to say nothing of sub-microsecond latency. The typically-quoted ~20 usec latency of USB4 limits it to around 50 kHz for an emulated ISA card.

reply

rdtsc
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Often people confuse latency vs throughput/bandwidth. With streaming and batching USB4 will shuffle a lot data through on average per second. But it will never hit reliable microsecond level or even submicrosecond latencies.

At the same time ISA card will never reach 40Gbps throughout with CPU clocking at tens of MHz only or often less.

reply

lysace
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This looks quite interesting:

https://www.reddit.com/r/vintagecomputing/comments/jbaw38/is...(2020)ISA-over-USB, using real ISA cards in an emulatorhttps://github.com/Manawyrm/ISASTM/

reply

boelboel
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've seen some older retail stores use DOS machines, ones where the owners are 70+. They just don't have a reason to upgrade what they're used to.

reply

zdragnar
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

It's been a few years now, but I know a major manufacturer had some windows XP boxes around because they were the newest hardware/software they could get with native parallel port support to interface with their machines.

To give you an idea of the complexity of the manufacturing lines, shutting the machines down and starting them back up again was measured in days. Upgrading them would be obscenely expensive, let alone replacing them, just in the opportunity cost of not making anything alone.

reply

mgk123
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

For anyone that needs true native serial & parallel ports, a Dell Latitude E series laptop (or Precision 7xx0) with docking station is an easily-available option.

The last machines with dock port have 6th gen Core CPUs (Latitude E5x70), or 7th gen for Precision 7x20.

reply

rkagerer
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not as pure, but for what it's worth I've had success with a Syba SD-PEX50023 in applications where USB-based parallel port emulation failed.

reply

Sleaker
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

The last company I worked for still had customers they were dragging forward to get upgrades from coax connexted green screen terminals to modern network thin clients. It wasnt on DOS, but very old unix OS, tape drives for backups, parallel for printers, serial for scanners. No USB. Lovely troubleshooting when you were dealing with 30+ year old hardware setups. There was only one company that would even servicenthe green screens if they failed, and you couldn't buy them anymore.

reply

ynac
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

It's not totally for business, but I run some antennae and radio telescopes that feed through a Gateway 386/33/16MB RAM. As well as a Getac, no idea what model, but it's from the early 2000s. They both feed through to a A/B switched Paradise CRT (so cute). dBase is on the list.

reply

EvanAnderson
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

A Customer of mine has an 386 machine with an ISA interface board connected to an optical comparator instrument. I believe they also still have some MS-DOS-based computers connected to CNC machines, too.

I have two Customers who use DOS applications under DOSBox (a Clipper-based accounting package at one, and a Symantec Q&A-based application at another).

reply

dazhbog
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I run 2 old Juki pick and place machines. They run DOS 6.22 on a 486 I think. My biggest pain points are, 1) booting them up without errors, and 2) transferring files to them wirelessly without any floppies. (without installing any DOS software)

Closest I got was with a GOTEK and an ESP32 emulating a USB. But it was flaky so I dropped it for now.

reply

nanochess
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I've an AMD K5 processor machine running at 100 mhz. for testing Transputer ISA cards when someone buys one, I also use the same machine to format and copy my Pascal compiler into a pair of 5 1/4" floppy disks. All using DOS.

reply

bartread
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

> Transputer ISA cards when someone buys one

Your use of “when” is interesting - suggests it’s notthatoccasional. Wonder what people are doing with these nowadays.

reply

NBJack
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Do scanners count?

I'm pretty sure they moved on from them, but a while ago I did seasonal work for a company that rented out scanners for year end inventory (tax related, IIRC). The scanners had to be "cooked" (flashed) on racks, boxed, and sent. The flashing usually worked, but on occasion, the scanner would fail the checksum or something and drop you into a DOS prompt.

reply

rjh29
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Not recently but when I was a teenager (2001-ish) my supermarket was using a DOS computer to handle stock, print new labels when prices updated each day, etc.

reply

ChrisMarshallNY
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I did, for a while. Then, I used VMs. I haven't had a Windows VM for years.

If I were a serious gamer (I'm not), then I'd get a hardware rig, but otherwise, I've not needed it.I had a doctor that kept an original NT machine, for many years, because his bespoke app worked on it.

reply

CobaltFire
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I had to keep a disturbingly old machine with GPIB running until a few years back. They are still in operation in Australia (who we sold them to).

It was a test/repair bench for military aircraft avionics, with the only flying platform left using it being the legacy F/A-18 (A/B/C/D). Harris H-100 minicomputer hooked to an HP terminal and several full racks of GPIB test equipment with half of a rack of solenoids for switching between stimulus and response and which pin.Not what you asked, but the question brought back memories.

reply

ksec
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

We were talking about Visual FoxPro only a few days ago. [1] And one of those same companies in my comment [2] uses an old ordering system that is still in DOS and they boot up a VM to use it. They still have a printing machine ( not a normal printer ) for those order printing connected via a Parallel Port. I don't know the details of how that works though.

And by the end of all that, the order will beFaxed. Manually.Did they tried to email it or automate it. Hell yes. Did it work? No.[1]https://news.ycombinator.com/item?id=49808023[2]https://news.ycombinator.com/item?id=49811716

reply

smackeyacky
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I know of a DOS machine at a wool testing place that uses an ISA card based imager for measuring the micron and other things. They also have a supporting DOS machine with a dBase looking database on it. When I spoke to the owner he didn’t really understand the risks involved in running ancient hardware and in fact had a storage room with period PCs in it if the machines failed. He didn’t have much of a backup plan for the imaging hardware though.

My opinion is that if these guys are still running this gear, they already have a strategy in place (no matter how flawed) and would likely retire before throwing money at something they consider a non problem.Good luck with the idea. It likely is a tiny niche market with customisation for every customer and given they are normally hardware constrained AI may not be much of a help.All of them have no money as well.

reply

mlaux
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

My idea is basically a DOS runtime with hooks on interrupts and I/O that would allow for either migrating databases to modern formats, or converting I/O accesses for modern USB peripherals. Customization for every customer and AI not being much of a help are pluses for me... lack of money not so much.

reply

Froedlich
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have been porting sections of the business software I mentioned earlier from QuickBASIC on DOS (nice to have the source code!) to Tcl on Linux using ChatGPT to automate the conversion. It gets it right the first try, almost every time.

The BASIC code is very simple by modern standards, and Tcl overlaps BASIC neatly, making conversion easy.Unfortunately it's just a short-term stopgap to add some features management suddenly can't live without, that weren't practical to implement in BASIC/DOS. They'll replace the whole stack with a commercial product and support contract when they find something they like.

reply

Dwedit
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You can still get ISA slots on systems as new as Broadwell with an adapter.

reply

mikewarot
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

The Gear cutting job shop I worked for had a CNC lathe running with a GE Computer from the late 1970s that stored data on punched Mylar tape, until it was bought out in 2019.

The bevel gear generator setup was some formula calculations running in version 1 of TK!solver, which would have been a $5000 upgrade to get the latest version, so they ran them under MS-DOS in DOSbox, and saved the grief.Without that software, they would have to pay Gleason $500+ to do the calculations for each new gear setup.There are strong and reasonable reasons to keep very old systems alive in offline production environments.

reply

saidnooneever
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

i know still some accountant who use a DOS program to do his work because he hates the fact modern UI has load times. slows him down too much o.O 
(his program is all keybinds).

i do not have exp myself but i found it a delightful reasoning. i told him modern PC could also do the same on modern OS (ncurses or ratatui or so maybe) but that if he ask a programmer to make an upgrade he'd need to find the right kind of guy. He had someone do it few times but they came back with web interfaces.

reply

womod
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

We keep a FreeDOS machine at work for dialing in to configure and service paging terminals and using old two-way radio programming software.

Most of the stuff I've moved over to run in DOSbox but it's still in use occasionally for the software that's difficult to port over.

reply

DASD
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Perhaps look into environmental services labs that do contract EPA work. I would not be surprised to see entire HP-Agilent(ISA-carded) - (think liquid chromotography analyzers) fleets that would match what you're looking for.

reply

techteach00
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

It's not DOS but my private school still uses an IBM 5100 to do payroll and record attendance.

reply

roryirvine
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

What's the reason for not using a more modern MIS?

(I can certainly understand why organisations with niche requirements might hang on to old systems for as long as they continue to work, but I'd have thought that school payroll and attendance were much too commonplace to fall into that category)

reply

techteach00
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm kidding. BRO, no school would be running the first (imo) commercial desktop still in the year 2026. The machine I cited was released in 1976!

reply

zerr
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've stumbled upon DOS on the LCD screen of the otherwise seemingly modern gas station.

reply

alightsoul
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

You're trying to create and sell a version of dos box? These companies have not replaced their computers because to the user there is no separation between the computer and the machine it controls. So the computer will be updated along with the equipment, which is not connected to the internet or a network anyways so it's not a cybersecurity risk. For the user, if it runs fine, there's no need to update just the computer, and the computer is updated along with the machine

In other words, these are embedded systems.

reply

mlaux
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Not exactly, freely available solutions are already good enough for people who just want to run their apps on modern hardware, and have been for a long time. What I was thinking about writing is a tool that eases migration by using interrupt and I/O hooks to detect common patterns and, say, builds a modern SQLite database as the business uses their dBase program. Whether anyone actually needs this, I don't know.

reply

alightsoul
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's a few car dealerships that still use databases from the 80s. As for why they haven't migrated, I'd guess must be reasons I'd assume at this point it's a choice they have made

reply

Postosuchus
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

This is probably a wrong audience. Most people here are very technical - the kind that would not put up with tiptoeing around a sacred computer from decades ago running some magic software from the DOS era. This crowd will aggressively move it to modernized architecture or at least emulate it using a more modern platform.

The company I worked at in the late nineties, used Managing Your Money (MYM) for bookkeeping - initially on a dedicated DOS machine. My colleague set up a DOSEMU-based emulator and moved the software to it (bye-bye, dedicated DOS machine!). Later, he re-wrote it in STk (Scheme w/ Tk bindings, running natively in Linux) as ageneral-purpose transaction storage. ¯\_(ツ)_/¯

reply

fires10
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

This is not always possible when the systems are validated and regulated.

reply

jlarocco
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah. Sometimes old hardware forces its hand and causes a big PITA.

I had a job working on VAX/VMS around 2009, but it was actually an emulator running on a PC because they just couldn't find any hardware to fix the VAX. At some point before I joined they had to get a ton of government approvals to use the emulator.Fortunately they had a project to modernize the whole stack. And it was going to Solaris :-/

reply

lormayna
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Few years ago I was working for a F500 company and during an assessment we discovered couple of OS/2 Warp machines that were controlling CNC equipment

reply

gerdesj
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Until recently several customers have an industrial machine that boots DOS. I think the oldest effort we deal with is Win XP now. I do have a C>64 at home ...

In a world that requires security audits etc here's some notes that might help:Scenarios:
You have a device that only talks NetBIOS or even NetBEUI for file sharing. You need to get files to and from it and your CAD workstations run Windows 11 and anything less than SMB 3, with signing and sealing and all that jazz is laughable.... Devices requiring ftp, telnet, serial over carrier pidgeonSolution options:Networking:
The first job is to segregate your industrial gear from your general network and you might want to create two or more industrial gear and internet of things type networks with differing access policies. Start with one for now, you can improve it later.You use 801.1Q VLANS logically or physically (why the hell did I want to write literally?) separate via separate switches.Please do not skimp on this step. Buy a network bod to sort it out or put your IT bod on a course or hopefully they will have labbed this up at home already!Comms:
Samba is bloody wonderful and speaks everything that MS has ever done and deprecated. Even Samba does need to be asked to start speaking some of those dialects again but it will.Put a Linux (other Unices are available) box on the same VLAN as your machines. You will need to set quite a few options relating to the minimum version for its server version. When talking to the machines, Samba is the server and when talking to your file server, Samba is the client.Create a data share on a Windows box on the corp LAN. For example it might be on a file server for multiple access or just a single CAD PC.Get the Samba box to mount that share to itself at say /srv/data_share_mc1Now get the Samba box to create a share from /srv/data_share_mc1 which it calls DAT_MC1 (8.3 chars for NetBIOS)With luck, you should be able to map DAT_MC1 on your machine.

reply

myself248
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A few years ago, I helped repair a broken USB port, on a USB-floppy emulator...

...which was so the operators could sneakernet their NC tape files into an IBM PC 5150 that thought it was talking to a floppy drive, of course......which hosted an ISA card that emulated the punch-tape reader that the NC lathe had originally been designed with.The NC lathe hadn't missed a beat in 50+ years, why mess with what works?

reply

nickhalfasleep
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I know of some laboratories where they have a host of old machines for software to support some critical instruments that only runs off a dongle or an ISA card and it still does accurate work.

reply

reaperducer
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Not DOS, but my company has a Windows XP machine with a dialup connection that I have to keep running for obtuse legal reasons.

If it goes down, the company gets fined. It happened in the gap between my predecessor leaving, and me being hired.

reply

gerdesj
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Does it have to be a XP box or is just keeping a serial dialup connection working the key?

reply

andix
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is it a physical machine and not a VM? I already had issues with getting XP compatible spare parts years ago. Had to buy used parts that were already pretty old (so high risk of failing again).

reply

reaperducer
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's a physical machine.

Fortunately, I don't have to deal with swapping parts. There's an outside contractor on call 24/7 for that.The last time I saw it was about two years ago when I taped yet another piece of paper to the filing cabinet it sits on reading "DO NOT TURN OFF UNDER PENALTY OF LAW!"Someone keeps taking the paper down.

reply

andix
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Put a proper sticker on, that can't be removed easily.

reply

newman314
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I virtualized a bunch and they seem to work well. At one point, I even had Ultima running on one. =D

reply

al_borland
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

It’s gone now, but we used to have a random OS/2 box well past the point where that was extremely weird.

reply

gerdesj
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

What's weird about Warp?

reply

Froedlich
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Like most people who bought into the OS/2 hype, I bailed after 1.3.

reply

al_borland
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The weird part was still using it into the 2010s.

reply

Natsu
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I used to be doing that, but this was a bit over a decade ago at this point. There was an SBC with DOS on a chip that connected to Novell Netware. I set a few variables in autoexec.bat, let it connect to the network drive, then had it run a script from there to admin them / do backups (by which I mean xcopy the C: drive).

These were for some industrial CNC machines with a poorly version-controlled app (send us the single-file .c for the program, we'll make changes & recompile for you, then send back a new .c and .exe file) that would just malloc() all the memory on the machine for a million element array instead of tracking the 1k or so unit IDs a more efficient way. They were six digits long, it worked... mostly.I kept a 3.5 floppy with the contents of sys a: that I used to run sys c: after restoring a machine from backup in my office.EDIT: oh, and of course by "restoring from backup" I mean reversing the xcopy to copy everything from the network drive's copy back to C:EDIT2: My memory is going, they didn't use malloc() at all, anywhere in the programs, they just had a static million element array.

reply

api
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Not current and not DOS... but years ago, around 2011, I helped set up a series of QEMU emulators running DEC Ultrix and MIPS Unix software that called out and retrieved data from weather stations only reachable by modem. The software had been written years prior in C and nobody had the source.

The box running the QEMU emulators had a bunch of old US Robotics modems hanging off it via USB serial dongles.

reply

TMWNN
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

>Anything with a parallel port dongle?

https://news.ycombinator.com/item?id=46849567

reply

Aeolun
 
5 hours ago
 
 | 
prev
 
[–]

In the AI era, can’t we just release a new version of DOS?

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: