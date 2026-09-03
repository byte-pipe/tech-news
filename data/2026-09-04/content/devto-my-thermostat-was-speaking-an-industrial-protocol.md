---
title: My Thermostat Was Speaking an Industrial Protocol. Just Not to Me. - DEV Community
url: https://dev.to/managerfx/my-thermostat-was-speaking-an-industrial-protocol-just-not-to-me-2a0p
site_name: devto
content_file: devto-my-thermostat-was-speaking-an-industrial-protocol
fetched_at: '2026-09-04T07:24:57.822173'
original_url: https://dev.to/managerfx/my-thermostat-was-speaking-an-industrial-protocol-just-not-to-me-2a0p
author: Felice Lombardi
date: '2026-09-03'
description: A senior software engineer who knew nothing about hardware, a BACnet MS/TP thermostat, and an RS-485 bus. How I ended up with an ESP32-S3 gateway on a DIN rail, wired into Home Assistant, in 15 evenings. Tagged with bacnet, esp32, iot, ai.
tags: '#bacnet, #esp32, #iot, #ai'
---

## Where I actually started, and it isn't the thermostat

Before telling the story, I need to say who did it, or none of it will make sense.

I'm a senior software engineer. I can design systems, read a spec, debug ugly problems. Abouthardware I knew close to nothing. The only program I had ever written for an ESP32 was a loop that blinked some LEDs to a beat: adigitalWrite()inside adelay(), and the satisfaction of someone who has just invented fire.

I had never soldered anything that mattered, never used a multimeter with any real understanding, and the basics of electronics — logic levels, what happens if you feed a module 5V instead of 3.3V, what a differential line even is — I knew only vaguely, the way you know a subject you've never actually had to deal with.

What I do have is the DIY habit. And there is a very specific satisfaction that people who only write software never fully get to feel: the code you write every day lives inside a screen, and when it works, a green test tells you so. Nice, but abstract.

When instead the code you wrote runs through a wire you stripped yourself, into a connector you soldered yourself, and on the other enda physical thing moves— a fancoil spins up, a display changes a number, a valve opens — the satisfaction is an order of magnitude bigger. It stops being a program. It becomes an object that does something in the world, and it does it because you put it there.

And if that object then solves a real, everyday annoyance instead of being a demo you push to GitHub and forget, that's about as good as it gets. It's the only real reason anyone spends fifteen evenings on a thermostat instead of watching a show.

That said: without AI, this project would not have happened. Not "it would have taken longer" —it would not have happened. I would have stopped at the first six-pin RS-485 module, with nobody to ask whether the bus GND needs to be tied in or not.

The rest of this article is the story of where what I already knew ends, and where what I learned along the way begins.

## The problem

There is a Delta Controls eZNT-T331 on my living room wall. It manages three zones and drives the fancoils: cooling in summer, heating in winter. It's done its job reliably for years, without a single hiccup.

No API. No cloud. No app. And no technical documentation anyone ever handed me.

What itdoeshave is a serial bus, on which it chats with the system's central control unit twenty-four hours a day.

It talked to everyone except me. And since the rest of my home is already automated, having to get up and walk to the wall to change a setpoint had become genuinely annoying — the kind of friction that irritates you a little more every single time.

Swap it for a smart thermostat? Not a workable path. This isn't a standalone appliance: it's part of a centralized HVAC system and talks to a controller that manages several zones together. Replacing it means reworking the interface with that system, involving whoever manages it, paying an integrator, and ending up with yet another closed device anyway.

The only sensible route was the opposite one: leave the thermostat exactly where it is, and learn to speak its language.

## Phase 0: a user manual and some stubbornness

Starting inventory:

* One wall thermostat.
* Itsuser manual. The end-user one: buttons, menus, "press here to set holiday mode."
* No datasheet, no protocol spec, no integrator documentation, no credentials.

I started by reading the device. Menu by menu, screen by screen: which values it shows, which it lets me change, which change on their own.

Then the discovery that cracked the whole thing open: there's aninstaller menu, password-protected. Protected by the default password, naturally.(Thank you, installers of the world. Never change.)

Inside that menu was an entry that makes no sense on a standalone appliance: the ability tochange the device's MAC address. An address. On a tiny scale, something like "14." Not an Ethernet MAC — a node address on a bus.

That's when it clicked: this thermostat is a node on a network.

I went and looked up the model's technical specs online, and the picture completed itself: the eZNT-T331 exists intwo variants, oneBACnet/IPand oneBACnet MS/TP. The IP variant needs an Ethernet connection, and there's none in my wall. MS/TP runs over RS-485 and identifies nodes with exactly the kind of small address I'd just seen in the menu.

It was the MS/TP variant. And the bus terminals were sitting right there behind the faceplate.

### Two evenings of study, before touching anything

BACnet MS/TP is the building-automation protocol that runs over RS-485 in atoken ring: master nodes take turns holding the right to speak, and whoever misses their timing gets dropped from the ring.

Before wiring anything up I studied the protocol: frame format, header CRC and data CRC, token passing, the Poll For Master procedure, the difference between amasterand aslavenode, and the application services I'd need —ReadPropertyMultipleto read,SubscribeCOVto get notified of changes.

I didn't skim, and not out of diligence: I was about to attach a device of my own making to a live bus shared with other devices on the system.

### The rule I gave myself, and why

If I couldn't explain what a frame does, that frame didn't go on the wire.

It's worth explaining where this comes from, because the actual risk isn't where you'd guess.

Acorruptedframe is the minor problem: MS/TP protects both header and data with two CRCs, and whoever receives garbage simply discards it. On that front the protocol is robust. There are three real ways to cause damage.

The first is addressing.On MS/TP every master has a node address, and they must be unique. If I power up my gateway on an address already held by another master, two nodes end up answering the same token: the ring gets confused, and it isn't just my problem — it's a problem for everyone attached to that bus. That's why I spent my first session with YABE just listening, to see which addresses were already taken, and picked 125 in a free slot.

The second is timing.RS-485 is half-duplex: only one node speaks on the wire at a time, and the token decides who. If I transmit out of turn, my transmission collides with someone else's and I destroytheirframe, not mine. And if I hold the token and don't pass it within the expected window, every other master times out and has to rebuild the ring. A slow node doesn't just fail on its own — it slows the whole bus down. This is exactly why, later in the firmware, there's a hard rule that the scheduler performsone BACnet operation per tick, and the core talking to the bus contains not a single blocking call.

The third, the most serious, is semantics.A frame can be formally perfect and conceptually disastrous. AWritePropertyis a real write to a real device: if I get the object wrong — or worse, the target — I don't get a compiler error. I change the configuration of a system that other people also depend on. And since I had no documentation, everything I knew about any given object was something I'd deduced myself. So: read for weeks before writing anything, write only to objects whose role I'd actually understood, and only after confirming the effect on my own display.

Bottom line: the bus isn't mine, and a mistake there isn't paid for by whoever makes it. That's where the rule comes from.

## Phase 1: reconnaissance, or the work AI could not do

To listen to a bus you have to get on it. I pulled the thermostat off the wall, found the two wires A and B — the differential pair RS-485 signaling runs on, the same twisted pair MS/TP travels over — and tapped it: in parallel, non-destructively, so the system's bus kept working while I eavesdropped.

On the other end, aWaveshare Industrial USB-to-RS485 converter: genuine FT232RL, resettable fuse, TVS diode, ESD protection. This is not the place for a three-euro no-name dongle: that converter sits electrically between my laptop and a live bus shared with other devices, and the protection circuitry is the entire reason you buy it.

For the record, AI was genuinely useful here: which converter to buy and why, how to tap a differential pair without interrupting the bus, whether to tie in the GND, where the 120 Ω termination lives and why I should care. All things an electrical technician knows and I learned the week before.

### And then YABE

YABEstands forYet Another BACnet Explorer: an open-source Windows tool that acts as a browser for BACnet networks. You point it at a bus, it sends a discovery message, and it shows you the devices that respond as a navigable tree. For each device you can list theobjectsit exposes — in BACnet, every value is a typed object, for exampleAV:10000(Analog Value number 10000) orMV:90010(Multi-state Value) — read their properties, and write to them.

In developer terms: it's Postman for building automation.

You connect it, hit refresh, and there's that moment every person who's done reverse engineering recognizes: the tree populates, and a black box turns into a list.

### The actual work

From here on there's no shortcut, and no language model is of any help. I found the objectsmyself, one at a time, by hand, over several evenings:

* read a property, write down the value;
* go to the thermostat and physically change something;
* come back, re-read, see what moved;
* guess the meaning, then test the guess.

AV:10000moves when I change zone 1's setpoint.MV:10001takes four discrete values that map to the fancoil speeds shown on the display.MV:90010flips when the system switches between heating and cooling season.AV:510reflects eco status, whileBV:90003commandsit and is never written back.

That last distinction cost me an evening, and later saved me from a bug:the object you write is often not the object you read.

The result was a hand-built CSV: type, instance, my own name for the object, unit, zone, whether it's writable, how often it's worth reading. Around fifty useful objects.

That CSV became the source of truth for the whole project, and I want to be blunt about this.

No language model could have produced that file.It has no access to my bus, no knowledge of this device, and no way to correlate a register with a fancoil physically spinning up in my hallway.

And even if I'd given it that access — an agent turned loose to discover the bus on its own would have flooded it. A shared token ring is not a place you explore by trial and error: every request occupies the channel, and an overeager tool degrades a system that also serves other purposes. This called for surgery and patience: one reading at a time, hand on the brake.

That part I did myself. And that's exactly why everything after it moved fast.

## Phase 2: from sniffer to gateway

A laptop running YABE is a diagnostic tool, not an integration. I needed something stable, permanently on the bus.

First prototype: ESP32-WROOM-32E plus an XY-S485 module.The XY-S485 handles direction automatically, so there's no DE/RE pin to toggle in software (on many cheap RS-485 converters there's a pin, called DE/RE, that you have to drive yourself to tell the chip "now I'm transmitting" or "now I'm listening"; get that timing wrong by a hair and you corrupt the frame): one less real-time trap on a protocol where mistiming gets you thrown off the token ring. UART2 on GPIO16/17, ground shared with the bus, jumper wires everywhere.

By the second evening it was reading and writing real values on a live bus.Not a demo, not a mock: genuineReadPropertyMultipleresponses from the actual thermostat.

That matters more than it sounds. From that point the project was never in a broken state again: every following step was an increment on something that already worked, revertible with a single commit if it made things worse. Never a big-bang integration.

Later I ported everything to aSeeed XIAO ESP32S3: 21 × 17.8 mm, 8 MB flash, 8 MB PSRAM, native USB CDC. The port hid one genuine trap worth documenting, because it will bite anyone moving code from a classic ESP32 to an S3:

On the ESP32-S3,GPIO16 and GPIO17 are not the UART2 pins. They're wired to the OPI PSRAM and aren't even exposed on the board. UART2 gets remapped through the GPIO matrix to D6/D7, i.e. GPIO43/44.

## Phase 3: the firmware

🔧Technical chapter — skip to Phase 4 if you don't care about the implementation detail.As an engineer, though, I couldn't get away with "and then I wrote the firmware": these fourdecisions are the reason the gateway sits on a shared bus without bothering anyone.

The finished gateway does more than shovel bytes from one side to the other. A few design decisions are worth pulling out.

### Two cores, with a rule written on top

The ESP32-S3 has two cores, and MS/TP does not forgive latency: miss the window in which you must pass the token, and the ring cuts you off.

* Core 1,bacnet_task: the MS/TP state machine and the BACnet scheduler, in a tight loop. No blocking calls, ever.
* Core 0,network_task: WiFi, the async web server, MQTT.

Traffic between the two cores passes through exactly two channels: a mutex-protectedDataCache, and a write queue into the scheduler. This iswritten down in black and whiteas a hard rule, and I'll come back to why writing it down changed everything.

### One BACnet operation per tick

BACnetScheduler::tick()performsat most onebus operation per call. No loops, no batching inside a tick. It runs a four-phase state machine —BOOT_WAIT→UNSUB_ALL→SEED_RPM→READY— and once inREADYit alternates four sub-operations, one per tick: drain the post-write refresh queue, reconcile one COV subscription, read one object in round-robin, renew one expiring subscription.

The constraint is deliberate: a tick that can only do one thing cannot starve the token ring.

### Budgeted COV subscriptions

Change-of-Value subscriptions are how you get notified of changes instead of asking over and over. The eZNT-T331 acceptsat most 12 simultaneous subscriptions— a device limit, and one of the first things I measured.

So subscriptions are a budget to spend, not a resource you can assume. Every object in the registry declares its own condition:

* CC_NONE— never subscribed, read only via round-robin;
* CC_FE_ACTIVE— subscribed only while a browser is actually connected;
* CC_FE_ACTIVE_AREA_ENABLED— subscribed only if a browser is connectedandthat zone is enabled in the device's configuration.

At rest, with nobody watching, the gateway holdszerosubscriptions and falls back to round-robin polling. Open the web UI and subscriptions spin up; close it and they're cancelled 30 seconds later. The system's bus carries no traffic on my behalf that nobody is looking at.

### The registry is the single source of truth

That hand-built CSV compiles into a PROGMEM table:

{
 
OT_AV
,
 
10000
,
 
"A1_StpEffettivo"
,
 
"area1/setpoint_effective"
,

 
"C"
,
 
1
,
 
PI_5MIN
,
 
DOM_STATUS
,
 
CC_FE_ACTIVE
,
 
false
 
},

Enter fullscreen mode

Exit fullscreen mode

Type, instance, internal name, MQTT subtopic, unit, zone, poll interval, domain, COV condition, read-only flag.Nowhere else in the codebase is a BACnet instance number hardcoded.Not in the web layer, not in MQTT, not in the frontend. The table today holds 56 objects, 11 of them COV-capable.

### A lean data contract

The Angular frontend polls the gateway once a second, so the payload had to be small. Two endpoints:

* GET /schema— fetched once: names, units, types, ids;
* GET /status?since=<seq>— a positional array of values plus a sequence counter, and anHTTP 304when nothing has changed.

No key repeated on every response, no JSON object per value. On an idle system, a poll cycle costs a 304 and nothing else.

## Phase 4: where AI earned its keep

Now the part everyone actually wants to read about. I want to be precise here, because "I built this with AI" is doing a lot of unearned work in most posts.

I didn't chat with a model and paste snippets. I built anenvironmentfor the agent to work inside. Four pieces.

### 1. An architectural contract the agent reads before every task

ACLAUDE.mdat the repo root, holding the invariants that are expensive to rediscover and disastrous to violate:

* BACnet operations live inbacnet_task, network and MQTT innetwork_task, no exceptions;
* DataCache::update()is the only safe path for writing across cores;
* object_registryis the single source of truth: never hardcode an instance or type anywhere else;
* C++17, no dynamic allocation aftersetup()— static, stack, or PROGMEM;
* the frontend is zoneless Angular with signals, no RxJS for UI state.

It's the highest-leverage file in the whole project. An agent thatknowsit can't allocate on the heap aftersetup()writes different code from one that doesn't. Not because it's smarter — because the constraint ispresentinstead of guessed at. A good chunk of what we call AI hallucination, on a real codebase, is an agent doing something reasonable in a context where nobody told it the rules.

### 2. Custom skills for repetitive, error-prone work

The riskiest routine operation in this project is regenerating the firmware registry when the CSV changes. Do it by hand and sooner or later you'll typo an instance number, and you'll find out weeks later, when a value is silently wrong.

So it became a skill,/regen-registry, with an explicit procedure: parse the CSV, parse the current table, diff them bytype:instance, list added/removed/changed, apply, updateREGISTRY_SIZE, run the invariant checks and the build, and present the diff for human review.

The skill's own text carries judgment earned the hard way, including this line:

Do NOT drop in-domain objects on a hunch that "the FE does not use them".

That's a mistake made once, fixed once, and then written down so it can't happen again. Note also the last step:never commit without human review, because generation isn't deterministic. The skill automates the tedium, not the accountability.

A second skill,/add-fe-icon, handles adding an icon to the pre-bundled offline icon set — small, boring, and exactly the kind of multi-file ritual that's easy to half-do.

### 3. Plan first, then code — with subagents in parallel

For anything non-trivial the flow was:spec → written plan → execution → code review, with parallel subagents doing exploration, planning, and review as distinct passes instead of one long conversation.

The repo holds16 implementation plans and 11 design specs, committed alongside the code. Not documentation written afterward: documents writtenbefore, reviewed by me, then executed. When the OTA update feature required several sessions across several evenings, each resumption started by re-reading the plan instead of reconstructing my intent from a diff.

There's also anADR(Architecture Decision Record, a short document that writes down an architectural choice, the alternatives considered, and the reasoning behind the decision) recording a design that was evaluated andrejected: an SSE-driven COV subscription lifecycle instead of one driven by the web UI's polling. Writing down what you decided against is worth as much as writing down what you chose — especially when the thing rediscovering it in a month is a model with no memory of the conversation.

### 4. Tests as the verification loop

This is the piece that makes everything else safe.

All the genuinely tricky logic is factored intopure modules with no Arduino dependency, unit-tested with Unity in PlatformIO's native environment: the COV reconciler, the post-write refresh ordering, the season-change detector, the MS/TP CRC, the master-node state machine, the receive state machine, the frame router, the status payload serializer, the OTA chunk planner and its header parser, the status-LED state machine, the write guard, the setpoint limits, the token verifier.

20 test suites, all running on the host in under a second.

The point isn't coverage as a virtue. The point is that an agent proposing a change to subscription reconciliation gets animmediate, objectiveverdict without touching hardware. AI-generated code and a fast test suite are close to a symbiotic pair: if generating is cheap, verifying has to be cheaper still. Without that suite, every change costs a flash cycle and a walk to the electrical panel.

### The hardest thing it did

The MS/TP layer I'd originally written was a simplified implementation that assumed a quiet bus. My bus isn't quiet — there are several other active masters on it, and a simplified implementation on a busy token ring is a slow-motion failure: it works for days, then starts dropping in ways you can't explain.

The fix was to port a realASHRAE 135 Clause 9.5.6 master node state machinefrom bacnet-stack: the receive FSM, the master node FSM, token passing, Poll For Master, frame assembly, both CRCs. Vendored as pure C, kept free of Arduino dependencies, tied to the hardware through a thin callback seam, and covered by host tests before it ever touched the bus.

That's legitimately hard embedded work for anyone, let alone someone who six months earlier was blinking LEDs to a beat. With the plan written first, the port structured as its own vendored library, and the state machine tested on the host, it cost evenings, not weeks.

## Phase 5: the bug that sums it all up

The most instructive failure of the whole project:

The first write after boot always timed out. Every subsequent write was fine.

Not a logic error, not a protocol error. The BACnet layer was correct, and I could prove it: the state machine's tests passed on the host.

The cause:AsyncTCP spawns its task with no core affinity and a high priority.When the first HTTP request arrived, that task got scheduled onto Core 1 and preemptedbacnet_task— the one task in the whole system that must never be interrupted. The gateway lost the token mid-transaction, and the write died with it.

The fix is a single build flag:

-D
 
CONFIG_ASYNC_TCP_RUNNING_CORE
=
0

Enter fullscreen mode

Exit fullscreen mode

Pin AsyncTCP to Core 0, where the rest of the networking already lives, and Core 1 belongs to MS/TP alone.

I keep this bug as the honest summary of the whole collaboration. Finding it required knowing that a token ring has hard timing, that a third-party library ships its own task, and that FreeRTOS will happily schedule that task on whichever core it likes. The first piece I knew because I'd studied the protocol; the other two I learned right there.

But narrowing it downsystematically— ruling out the protocol layer because the tests passed, correlating the failure with the first HTTP request, then going and reading how that library creates its task — was a debugging loop the agent drove faster than I would have on my own.

Neither half would have gotten there alone in one evening.

## Phase 6: Home Assistant, and the electrical panel

The gateway exposes three surfaces:

* a local web UI— the watchword is lightness: Angular 21, standalone components, zoneless, signals only; built, gzipped, and served straight from LittleFS in just three files, because the gateway's flash memory isn't a server's;
* a REST API—/schema,/status,/write, plus the OTA endpoints;
* MQTT with Home Assistant discovery— the thermostat shows up as a nativeclimateentity, with the right modes, fan speeds, setpoint limits, and current HVAC action; plus a custom Lovelace card for the three-zone layout the stock card doesn't cover.

Then the things that turn a prototype into an appliance: aweekly schedule editor— from the web UI you set, day by day, which time bands the thermostat should follow its normal program in (I use it for presence/absence bands, without ever touching the physical buttons on the wall again); firmware updatesover the network, so when I find a bug I don't have to open the electrical panel and reconnect the ESP32-S3 over USB, I just push the new firmware from a browser; and a status LED whose blink rhythm encodes AP mode, STA connected, scheduler ready, and device reachable — one monochrome LED, the state lives in the duty cycle, and the logic that decides it is pure and unit-tested.

Then the physical finish, which took as long as any feature:

* apermanent tapon the MS/TP pair behind the thermostat: parallel, non-invasive, the shared bus untouched;
* the cablerouted through the wall to the electrical panel;
* adedicated power supplyfor the ESP32-S3 inside the panel, so the gateway isn't hanging off a USB charger in a hallway outlet;
* aDIN rail enclosure, designed in CAD and 3D printed, because nothing off the shelf fits a 21 × 17.8 mm board plus a converter module and a strain-relieved bus tap. For the design I had to call in a friend who does mechanical design — my own CAD skills run out well before a DIN clip that has to snap in to the millimeter — and watching his 3D model turn into a real part, custom-fit tomyproblem, was another huge satisfaction, mostly his and a little bit mine.

From a breadboard on the kitchen table to a component on a DIN rail. That last 10% is where hobby projects usually stop, and it's the entire difference between a demo and something you forget you even have, because it just works.

And the soldering, I did myself. The first attempt was with a Parkside iron from Lidl, which mostly succeeded in sending an ESP32-S3 up in smoke — and taught me that a fifteen-euro iron has no temperature control at all, so it either doesn't get hot enough or it cooks the component. After that I bought the real gear: a temperature-controlled station, decent tips, flux, desoldering braid, a helping-hands jig. Now I have more of it than I need, as tradition demands.

## What I'm taking away from this

The numbers:~15 hours total, spread across 15 evenings. Working prototype on the second evening. 279 commits. 56 BACnet objects. 20 test suites on the host. 16 plans, 11 specs, 1 rejected design recorded for posterity.

The lessons:

1. Bring what you know, let yourself be taught the rest.My contribution was the method: read the spec, isolate the logic, never put anything on the bus you couldn't explain, keep the system always working. The hardware — the wiring, the logic levels, the soldering iron — I learned during the project, with AI as an infinitely patient tutor. Neither half was enough on its own.
2. Some things stay yours.The bus tap, the eyedropper-careful sniffing session, the hand-built CSV: not delegable, and not out of pride. An agent turned loose on a shared system floods it; that part called for meticulousness.
3. Invest in the setup, not the prompt.The architectural contract, the custom skills, the plan-before-code workflow, tests that run in a second on the host. Every hour spent there paid back many times over. The prompt is the least interesting part of working with an agent.
4. Write mistakes down where they can't recur.Every rule in myCLAUDE.mdand every warning in my skills is a scar. Written down, scars become guardrails.
5. Make verification cheaper than generation.Generated code costs almost nothing; that only helps if checking it costs even less.
6. Get to something working by day two, and never let it be broken again.Fifteen one-hour sessions only work if each one starts from something that runs.
7. Write down what you rejected, too.Otherwise future-you — and any agent reading the repo — will propose it again with great enthusiasm.

The thermostat on the wall looks exactly like it did six months ago. It just answers to Home Assistant now. And the interesting part was never the code.

## One last, less technical thought

There's something this project made clear to me, and it's bigger than the thermostat.

For years, technical competence has also functioned as a barrier to entry: to do serious hardware you had to have studied electronics, to port an industrial protocol onto a microcontroller you had to have read hundreds of pages of spec, to 3D print a custom mechanical part you had to know CAD. People without that background stayed out, rightly, or relied on someone who had it.

AI hasn't eliminated that competence: someone, somewhere, still has to know how a token ring works, what a core-affinity build flag does, how to size a DIN clip. What it eliminated is the requirement that that someone always has to beme, and exactly when I need it. It compressed the distance between "I have an idea" and "the idea exists" — for anyone who still brings a method: the ability to verify, to not trust blindly, to know when an answer sounds wrong even before you can say why.

It isn't the democratization of expertise. It's something more modest and more useful: shortening the distance between a software engineer's curiosity and the piece of metal that ends up, working, inside an electrical panel. For someone with DIY in their blood but not on their résumé, that's not a small thing.

And here's a provocation I'll aim at myself before someone aims it at me in the comments: in ten years, how much of this will still be done by a human? The reverse engineering with a soldering iron in hand, the bus tap, the custom-printed part from a friend's CAD file — today those are still mine because an agent has no hands, no eyes on a multimeter, can't reach behind a wall plate to tap a twisted pair. But "can't yet" and "will never" are different sentences, and the gap between them is closing faster than I'd like to admit: manipulation robotics, vision, agents driving physical tools. The day a robot can hold a soldering iron with the same care an agent today holds a code review, the "mine" part of this story moves further downstream — toward decidingwhatto build andwhy, no longerhow. That doesn't scare me; it's the same shift I already lived through writing fewer lines of code by hand and more lines of intent. But it would be dishonest to pretend it stops here.

Happy to go deeper on any piece — the MS/TP master state machine port, the conditional COV budgeting, or the skill definitions. Ask in the comments.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse