---
title: 'Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s | Hacker News'
url: https://news.ycombinator.com/item?id=48968606
site_name: hnrss
content_file: hnrss-show-hn-i-replaced-a-120k-bowling-center-system-wi
fetched_at: '2026-07-20T11:58:14.195947'
original_url: https://news.ycombinator.com/item?id=48968606
date: '2026-07-19'
description: 'Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s'
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
Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s
2460 points
 by 
section33
 
21 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
267 comments
I might be the only SRE on Earth with his own bowling center. It's a more in-depth gig than you'd think.

My family and I bought an abandoned 8-lane bowling center in the rural mid-west. In our small town there weren't many recreation options for families. You've heard of a food desert? This is an R&R desert.It had been abandoned for a good reason. The roof leaks, the electrical system was constantly surging, and my 70-year-old bowling equipment (still) doesn't work perfectly. The system that keeps your score is particularly interesting to me. It's the thing you watch during your game, but it fades into the background beyond that. Turns out these things are really cool, but absurdly expensive.Ours was installed in 2008 and cost six figures. It's calculating ball speed and trajectory, camera-based pin detection (object detection and trig, on ICs!), runs the fouling, the animations, the pinsetting machine and ball return. Very cool stuff for its age.From the business perspective, my facility only cost me $105k. To forklift-replace the score keeping system runs anywhere between $80-$120k, depending on features, vendor, and unit age. No upgrades or service contracts, mind you, and every feature and customization is a new line item. That's for a 1:1 replacement on a system installed in 2008. Incredible, given how fast the tech world moves.Replacement parts cost a shocking $4000 per pair of lanes. But wait, the bowling machines themselves are 70 years old, so what's this "advanced" system actually doing back there? Actuating a single relay to trigger that big old machine. Everything else is strictly mechanical. Meanwhile I've got a six-figure invoice in my hand. I'm upset.Given the state of open hardware, computer vision, real-time event streaming, and open source running megascale products worldwide, there had to be a way to do this myself.So far I've built an equivalent prototype for about $200 per lane-pair, $400 if you're fancy. ESP32 and ESPNow with an RS485 fallback, reporting to a raspberry pi lane computer that's really just redis and a state machine bolted to an ESP32 gateway for the mesh.Since it's all ESP32, I've got a fistful of spare controllers in a drawer, pre-flashed or waiting to be. All common off-the-shelf hardware: microcontrollers wired to relays, optocouplers, and IR-break-beam sensors, each running slightly different firmware. Writing the firmware and protocol is the actual hard part.It's an ESPNow star-topology mesh: each node emits events from its sensors and accepts commands for its controls, reporting to a gateway node connected to the raspi over UART. From there it's event streaming: RX packets get translated and tossed into redis, commands relay back out to the mesh as needed. RS485 sits underneath as a wired fallback for noisy RF environments.Once the data's in redis, it's familiar middleware/React/websocket/pub-sub stuff. Any React dev can build their own UI and bowling animations. Since it all runs on commodity hardware, I can do legit anything I want as the proprietor, and I own all my data. Repairs take five minutes; I can swap the rig on a lane pair in under 10. I'd bet a house like mine could go from zero to running in an hour or two.We're calling it OpenLaneLink, and I plan to open source the hardware, firmware, and software stack when it's ready. Bowling is fun, and I want to help keep it affordable for alleys like mine.
I hate vendor lock-in. I'm not a fan of closed systems, calling support for every hiccup, or paying to "white label" my own equipment. Want to go Tron-themed for a night? Good luck finding a neon neumorphic theme in something bought at the turn of the century.All that bugged me. Sure, bowling equipment is niche, but the open hardware and software landscape is amazing.Thanks for reading! Let me know if anyone's interested in more posts about this bowling nonsense.

 
help

HeyLaughingBoy
 
15 hours ago
 
 | 
next
 
[–]

Thank you for posting this, it reaffirms what I've been thinking for so long. There are many opportunities to retrofit old systems of all types with modern low-cost embedded technologies.

Around 2019 or so I was approached by an engineer who had a small business retrofitting very old machine tools with modern motion controls. Think very large lathes and planers. The problem they had was that in order to get these systems working with newer controls, they had to make time-consuming modifications to the old machines, in some cases modifying the axis motors and that cost added up quickly. The engineer realized that it was theoretically possible to take the old analog position signals and convert them into something a modern motion controller could read. That converter box would make the retrofit pretty much plug & play, but he didn't have the programming expertise to make it happen.We probably built the first iteration of the converter for under $50 in parts and less than 50 hours of development time. That had me searching for other similar opportunities. I have found a few, but they tend to be one-offs that aren't worth the time unless you're already building something similar. Either that or my ability to see opportunity sucks!

reply

ryukoposting
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

I think I see some parallels with the aftermarket for old cars. Holley's entire catalog is "here's a thing that'll modernize your 1960s engine without replacing the whole damn engine"

This kind of thing is a low-volume, low-margin business by nature. It's those kinds of businesses that the megalomaniacs of our field tend to ignore. There are people with needs, and money they are willing to exchange for a solution to those needs. But there's no path to world domination by selling carburetors (or bowling alley control systems) so those problems never get solved by anyone with the means to do so. It's a shame, really.

reply

red369
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I once expected an aftermarket industry to pop-up to hybridize old cars. Old rear-wheel drive manual cars sound easiest.

Generator attached to the flywheel instead of the starter motor, and then find some way to squeeze a drive motor by the rear diff (probably more complicated, but surely not impossible). I thought something might pop up once companies like Bosch started making generic e-axles for manufacturers to use.With a small Li-ion battery (and all the usual inverters, etc.), it could work like a manually operated version of the dual-motor Honda hybrid system. Put it into neutral, and whatever energy is in the battery could drive the motor on the rear axle. The engine could automatically kick-in and drive the generator if there's not enough in the battery.It would never be as economical as a purpose-built hybrid, but old manual cars are often reasonably economical on the open road, and terrible in city traffic. Targeting only the urban fuel consumption would go a long way towards keeping them useable, with the added bonus of making manual shifting optional in stop-go traffic. Small motors would be enough for city speeds, and with a small battery, it sounds cheap to me at least.I doubt it could ever be a simple kit, but I thought people would have a go.

reply

studog
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People probably are having a go. Here's one for pickups: 
https://edisonmotors.ca/trucks/pickup-conversion/

reply

kfse
 
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

My guess:

1) New cars are too cheap to make at scale.2) Old cars are quite unsafe to drive, comparatively (airbags, backup cameras, lane departure alerts, blind angle alerts, etc)

reply

jimnotgym
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

2) cars have had airbags for a pretty long time. Backup cameras are a simple retrofit. Lane departure alerts are not universally loved, mine is turned off...

reply

noir_lord
 
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

Aerodynamics as well, new cars and especially ev/hybrids are 
slippery
 compared to many/the average if we take old cars to mean 50’s through 70’s.

reply

jimnotgym
 
57 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Does that matter much if you only drive around town at 30mph?

reply

yobbo
 
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

Stuff like this exists for bicycles. For mopeds and motorcycles there are electrification kits.

It should be possible to just replace the flywheel altogether with a generator/motor that both brakes and powers during each cycle, cancelling vibrations. Then more generation during deceleration, and more power during acceleration.

reply

ozim
 
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

There is no shame and no business there.

We just read a story of someone who didn’t want to pay market price and went DIY.There are companies doing bowling alley equipment and you can pay them for maintenance.Is there a single one of those on F500 list? No and people are running those companies and what OP did … he didn’t want to pay market price.Well yeah those companies are overpriced if you are software engineer who can wire up and program couple of ESPs have own bowling alley and have free time.

reply

mrb
 
39 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Don't dismiss the OP so abruptly. IMHO he is convincingly making the case that there is likely a business opportunity for something between a $120k off-the-shelf system and $1.6k in DIY hardware.

reply

tonyedgecombe
 
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

It's just lack of competitive pressure. I bet if you investigate you will find there are only a couple of suppliers that have the bowling alley market sewn up between them.

reply

kfse
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Work out how many bowling alleys there are and how many of them are in the market for an upgrade or a fresh install, trying to get to be the king of that hill is a lot of work and risk for not really life changing rewards compared with what a self-avowed SRE could make just pulling paychecks

reply

qdotme
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, the reality of those types of businesses is that once set they do become a relatively low maintenance (and for some, very low 'urgent' maintenance) passive income.

It's really easy to pull $300k/y as an SRE (but thatdoesamount to about $100/hr equivalent in SMB, assuming realistic >40h workweeksandthe tax advantages in SMB, even less if you have to pay for services youenjoyand can't find time for due to FTE - nannies or even changing your own oil).It isextremelyhard to keep that $100/hr and a sliding scale - one week you work 50h, the other 30h, then you take a month or three off at $5h/week.Mine (and I don't regret these) is running midsize PV plants. Slightly bigger than residential (hey, does OP want solar PV on the rooftop? I have a bowling alley as a client, they are a great match), but again not large enough to attract a scaled business.I approximately put in 5h on each a year after the initial setup (around 100hr each), for $10k/y in profit from each.

reply

lostlogin
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> retrofitting very old machine tools with modern motion controls.

I have a friend who has automated an old food production line. Eg peanut butter making, Muslie roasting etc.With no background in programming he got machines hooked up measuring various things - eg peanut butter levels with ultrasound, roast temps, rotation rates.Zero version control and eyebrow raising methods but massive improvement in safety and throughput. Really impressive.

reply

eru
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I suspect this is where our AI agents will really come to shine: helping people who might have a technical bend but are not programmers do cool things.

reply

fragmede
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah. Anyone who hated writing code but had to, like biologists and chemists, now don't have to.

reply

baranul
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is arguably a dangerous fallacy, particularly for anything critical. When the person doesn't know programming, it becomes harder to guide agents and do reviews, leading to overlooking issues and accepting mistakes. This gets amplified for any creative solutions or fixing future problems, where it is something the LLM was not trained on or has limited data about the subject. Plus add how much money spent on tokens.

Maybe a way for non-programmers to better understanding what they are saying, is to think about translation. It's kind of like saying a person doesn't need to know anything about Spanish to now sell LLM translated books from English to Spanish.Yes, the LLM can do translations for you, and quickly. But, as you don't know Spanish, you won't know how good the translation is. You are less likely to catch all kinds of mistakes, from bad grammar to wrongfully translated idiomatic expressions. The less Spanish that you know, the more likely you are to be impressed or fooled into a false sense of security. Then when native and fluent Spanish speakers read your books, they may rate it as mostly gibberish and nonsense.

reply

rkuodys
 
7 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think there is negative bias. The counterpoint being that with code you can test input vs output. With foreign language you cannot. Programmed system, either computes what you want or it doesnt. For Spanish you either have a person who can do testing for you. Good practises and cybersec questions matter in programming, but system doing what it is supposed to do (success path) matters more imho.

reply

jimnotgym
 
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

Better still, the llms are easier to get on with than real developers. You explain to a real developer what you want, after a few weeks you find every word you said has been understood in the frankly weirdest way possible and every grey area, instead of asking, has gone way off piste.

The same goes for the LLM, but it replies in minutes and costs next to nothing, so you can correct it quickly, and you don't even have to be politely patient with it to avoid hurting its feelings

reply

evandijk70
 
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

The current situation is that the person that doesn't know programming will do it anyway. They will likely make more mistakes than an LLM will.

reply

gambiting
 
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

I'd argue we're there anyway with all kinds of non-programmers using languages like Python to achieve their goals.

On one hand, it results in some absolutely horrendous code that takes 100x longer to run than necessary, because it lacks the most basic principles of engineering. On the other hand....it works and does what is asked of it.

reply

silisili
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm mixed on this. They may not(or may) write elegant code, but they have clear intent about its parameters and purpose. I've seen LLMs mess up numbers by order of magnitude on multiple occasions, which could range anywhere from annoying to fatal, depending on the field.

Like all things, helpful as long as it's checked very carefully.

reply

Cthulhu_
 
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

They do still write code, to a point, but it's in human language with a humanized feedback loop instead of the lower level of code.

reply

EPWN3D
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The less physicist code exists in the world the better.

reply

eru
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes. And in addition, Claude and Kimi and friends will happily do version control and write tests etc.

They'll even volunteer to do so and recommend.

reply

BobbyTables2
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I think you’re absolutely correct.

I suspect it is practical to do a small one-time run of maybe a 1000 copies of a purely hardware device and sell them. Of course, that is just kicking the can down the road a bit farther… At least dealing with obsolescence with purely analog parts is simpler…As soon as software appears, things become less ideal. Now the HW and SW become highly specialized to a single vendor’s single family of devices. Plus, bugs and internet connectivity almost ensure a potentially unbounded number of updates or forever broken functionality. Even toolchains fade into obsolescence…Sure, one can redesign for a new microcontroller from a new vendor. Maybe with new RTOS too. Of course, that is almost as much work as the initial design and probably done by someone else at a later date. Yuck!(And I saw this as a software engineer!)Definitely something to be said of the old habit of a simple analog design with schematics fully provided to the end user. This is something probably still needed today, but perhaps commercially challenging, especially with countries like China in play…

reply

berkes
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> There are many opportunities to retrofit old systems of all types with modern low-cost embedded technologies.

I'd leave out the "old" there.An example: Friends work(ed) as engineers in theaters and music-venues. The costs for (DMX) equipment is insane. Some lamps, rigs or controllers are so expensive that shows only rent them. While there's lots of cases where you don't want to cut costs¹, quite often a cheap variant cuts it just fine. So apparently there's a lot of Pie's, Arduinos, ESP32s and old androids used to handle stuff. Custom, hacked, duckt-taped solutions. All of them are certain a startup offering generic but cheap modules that engineers can customize, would be an instant hit. Especially if "service" can be bought with it.Or a friend who installs (climate) control systems in (food)factories, who cludges together arduino's and some hacky web-interfaces, who is certain that the industry would love some "off the shelve" solutions that installers can build their own hardware- and user-interfaces on is a very much wanted product. The industry (in EU) is according to him, one built on "lock ins", where a factory starts off with AcmeInc controllers and then slowly Acme will start charging almost "extortion-fee" alike figures just to fix stuff on a sunday night.Or, a friend who has a fruit farm with lot's of freezer-storage (running hundreds of KWs), whith whom I cludged together some Arduino's and home-automation to control the freezers to run when electricity is cheap or free. Stuff like this is available for consumers at reasonable prices, but the moment the Amperages go to industry-level, the costs explode. Where a simple remote controllable power-switch can cost €1000s. I'm certain that there's hundreds of thousands of small warehouses, supermarkets, traders, logistics that could save a few hundreds to thousands of €'s a year, by controlling their freezers, heaters, pumps, pressurizers, dryers and whatnots smarter with "turn key" modules built from generic low cost hardware.--¹ relevant: There's a lot of "Nobody Ever Got Fired for Buying IBM" behind it: if you go for the cheap €800 chinese knock-off and mid-show something starts failing, its your fault. But if that €10.000 controller starts failing, it's no-ones fault.

reply

kfse
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

With respect to bowling alleys, for things like professional shows or food safety it's a bit more than "nobody got fired for buying IBM". The stuff's gotta be able to survive field conditions and not cost millions of dollars in refunded show tickets or spoiled foods. Manufacturers test and make themselves accountable for this. Cheap, customized modules work until they don't, and by then the engineer who put the custom system together in the first place isn't there to fix them. Who would you call when some quick-and-dirty integration code that was burned into these embedded modules without ever being put in a source versioning system fails in some weird edge condition? OP is an SRE, it's ok for him, but the average farmer or show operator doesn't have the skill.

reply

madaxe_again
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yup. I live on a river. We flooded catastrophically in 2019, which made me suddenly care about the government’s network of river level meters.

Turns out, they abandoned most of them in 2008, as it was the local council who were meant to maintain them, but they couldn’t afford it - a chat with the president revealed they’d been paying €15k a year for each station to maintain it and they’d cost about €100k each.I went and looked at the battered remains. Sounding tube. Ultrasound transducer. Box of 90’s electronics.Anyway, long story short I banged out six of them for them for about €80 a piece - the expensive bits were the batteries and the dinky solar panel. ESP32, ultrasonic transducer, GSM and LoRa (as two are outside of the cell network), haven’t had to touch them in five years and we now know when it’s time to evacuate, rather than wading out in the night while trees sail past us at 60kph.So much stuff like this.

reply

japhyr
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Where are you located? Around 2020 I put together a landslide risk monitoring site that's entirely based on stream gauges:

https://khmpsitka.orgIt's an interesting approach that's way simpler than relying on soil moisture sensors placed high up on mountainsides. It's not as widely applicable as measuring soil moisture directly, but it's been running steadily for over 5 years now.

reply

fragmede
 
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

They didn't offer any of the €15k a year to you, did they?

reply

madaxe_again
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They hadn’t been paying since 2008, hence it was all derelict trash - they don’t even have the budget to maintain the roads or keep the school open, never mind monitor river levels.

My interest was not drowning, rather than pecuniary.

reply

cechmaster
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

so what are they doing?

reply

TacticalCoder
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Thank you for posting this, it reaffirms what I've been thinking for so long. There are many opportunities to retrofit old systems of all types with modern low-cost embedded technologies.

At my shooting range, where security is very important, we're replacing the old antiquated "fire stop" (when everybody on "shared" lanes has to stop shooting for there's at least one person going to change the targets) system with a modern system of electro-magnets and embedded devices. Mechanical safeguards where, by default, the 10 lanes (there two times 10 lanes, the 50 meters ones and the 100 meters ones) have to stop shooting and then an embedded system with a little controller for each lane that needs to be working to give the greenlight / "fire frei" ("free to shoot").We mostly decided on the switch after a failure of the old system: the "free to shoot" system has recently been given even though there was still one person outside, changing the targets (nothing bad happened but this is a serious incident).We asked for quotes for a system that is always "door locked" / red light / "fire stop", unless everything works fine and every lane gives the greenlight (each shooter has now one badge).Same thing as in TFA: cost in hardware is minimal compared to the quoted prices. Like basically 1/50th of the quoted price.

reply

vikbez
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Lol, nice! It depends on what you mean by "owning a bowling center," but it looks like there are at least two of us into this :D

I bought a really old fully mechanical (and automated!) mini bowling lane. It works without a CPU, except for the score display, which originally used a 1970 Intel D8749H (MCS-48)!Just like yours, the only thing that turns this machine on is a single relay :D
On my model, I also get feedback on the pin status and a "ball received" signal, so I can trigger the scoring.I dumped the firmware and replaced the display PCB with a more recent DIY PCB with an Arduino that speaks a modern, documented protocol. It's now compatible with ScoreMore software, and I can do a lot more with it.Here are some pictures and more info on the Bowltech forum (you should post your stuff here too!):*https://www.bowltech.com/forum/small-scale-bowling/small-sca...@vik8 on discord if you need :)

reply

section33
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I love it! I actually looked at integrating with scoremore myself, but once I crossed into hardware world, I still couldn't get over how much fouling alone cost. $750 / unit and they're -ancient-.

Definitely will post on bowl-tech as well. I'm just new enough to have a lot of that new-guy anxiety around posting OpenLaneLink there yknow? Those guys know -everything- about this stuff.

reply

bumby
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is the fouling functionality more complicated than one would assume? From a naive perspective, it seems like it would just be a simple photo-eye sensor

reply

vikbez
 
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

Well, it's because those guys knows everything that they'll notice the little things you might have missed :)

Have fun first !

reply

tecleandor
 
27 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hah! I remember playing a couple times in one of those Alf Minibowling machines in Madrid in the early/mid nineties... It's a string machine, isn't it?

Kind of funny that factory is in a small town next to Zaragoza...

reply

cgyvbunji
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Can you explain the significance of the single relay? My car starts with a single solenoid.

reply

vikbez
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The pinsetter is either "on" or "off", there are no other states to manage. Once it's on, it runs indefinitely: it sets the pins, clears the alley, resets the remaining pins, and repeats the cycle, all without any external control.

On mine, I do have some "feedback info" on which pins are down + a signal to "when" to score points, but this is optional as you can also write your score manually if you have no scoring computer system.

reply

hinkley
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

When I was in a junior league we were at a relatively recent vintage alley and once in a while it would glitch and reset the pins twice in a row. I bet the relay stayed closed too long.

reply

lelanthran
 
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

> Can you explain the significance of the single relay? My car starts with a single solenoid.

Your caralsostarts with a single relay... that drives a solenoidanda motor.

reply

devilbunny
 
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

That one relay is the only connection between the pinsetting machine and the scoring system.

reply

taneq
 
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

Yeah this $100k system with all its expensive add ons is there to push a single button.

reply

manwe150
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But at least now I know why the lane near me just has a physical button next to each lane (and manual scorecards)

reply

eru
 
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

Well, and to display your score.

reply

tanseydavid
 
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

This is an AI app from the 1950s! Developed by Rube Goldberg who fully intended to vibe code the scoring part later. </sarc>

reply

tclancy
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I’m just going to say I am going to find a way to be the third person in your bookclub. This is so cool!

reply

section33
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Right now I'm working on adding LED + DMX DJ light control - I kinda want to be able to order LED strips to "chase" a ball as it goes down the lane or back up the return. I plan on triggering laser-light shows and such with the DMX controller.

Eventually, I want to allow a customer walk up to the lane, tap to pay and start bowling immediately, too. Kiosk-ize bowling alleys, yknow?I'm pumped. So much room for activities!

reply

hinkley
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Tap to pay probably doesn't help with getting people into the alley but probably helps with 'one more game'.

Your beginners have to come for shoes anyway, and the pointer to which lanes to take (you don't want them taking a lane at 6:30 that's reserved at 7)

reply

pants2
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At least you could display a message that says "this lane is reserved. Open lanes: 6, 7"

reply

6_7
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm sorry which lanes are open again?

reply

stuaxo
 
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

Available lanes are lit green and reserved are red ?

(Or something more complex)

reply

robocat
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hopefully you can synch the light flashes to the ball rotation:

1: maybe make the ball look like it isn't rolling - or even backspinning2: perhaps it could you make the amount of side-spin or other spin more obvious to help learningMaybe hard to read the ball rotation accurately: even if the ball was marked with dots or bands that help?

reply

TylerE
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That sounds quite hazardous to anyone who happens to be epileptic.

reply

luma
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hell yeah brother, this sounds like a fantastic project with a lot of room to dig into fun things with the double extra bonus of other people having fun with the result. Now you have me shopping for a bowling alley :D

reply

kci225
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ugh, there is a four lane bowling alley right near me for sale for $100,000 or so. Now I’m further tempted.

reply

quietsegfault
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Buy it! What else are you doing with your money?

reply

mixmastamyk
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Best post in a lonnnng time. Need any help? I have some dmx/dj experience from my days in digital signage.

reply

brcmthrowaway
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh man, Id love to find cheap surplus digital signs

reply

tonyarkles
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'll throw out two quick suggestions for you:

- DMX kinda sucks but it's manageable. Cabling isn't cheap, it really wants shielded 120 ohm cable. If you do go that route, don't cheap out and use Mic cable or Cat-5, you'll be chasing ghosts forever.- However... Art-net is an absolutely brain dead simple protocol that you can run over WiFi or ESP-Now if you don't care about it being perfect, or over Ethernet with an ESP32 with an Ethernet PHY or a Teensy or similar. I'm serious, you can implement it in an afternoon. Lots of COTS lighting controllers can talk Art-net, and you'll be amazed at how trivial it is to make a Python script to blast out the appropriate UDP packets.- sACN is the new kid on the block for this stuff though and it's a little more complex. Not to shill LLMs... I hadn't actually heard of it before, Claude mentioned it and then one-shotted both a server (ESP32-side) and a test client (Python). There were a couple little bugs, but about two hours from never having heard of the protocol to having existing COTS lighting design software talking to it was pretty dope.The other annoy bit with DMX: it's 250kbaud RS485, so it's not always trivial to just make a USB-serial-RS485 adapter that will actually run at that baud rate. With the Art-net/sACN approach, itistrivial to get an ESP32 or similar to run at that baudrate and drive the RS485 DE pin correctly as well.Enjoy!

reply

20after4
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

UDP rules for this sort of thing. Art-net sounds very similar to OSC¹ and that's a good thing.

1.https://en.wikipedia.org/wiki/Open_Sound_Control

reply

tonyarkles
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yup, they're definitely cousins. The only reason I didn't mention OSC is because you're not going to have the same ecosystem of existing open-source and commercial lighting control software available. OSC is fabulous for controlling all sorts of things and nails that COTS software compatibility layer for lots of other live production scripting stuff. (e.g. if you implement OSC on an ESP32 you can control what it's doing from an existing iPad app)

reply

dimator
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This sounds like such an amazing adventure, good luck I'm sure it will be a huge success!

reply

Polizeiposaune
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How are you handling bowling shoe rental?

reply

ErrantX
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nowhere near the OP (UK) but I've noticed a lot of fun-only lanes arent bothering to rent shoes and just let you wear whatever you have.

reply

semi-extrinsic
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Never understood the need to wear extremely uncomfortable and ill-fitting shoes just to throw a ball. Always seemed like a way to jack the price up.

Sure, professional bowlers use specialised shoes. Professional footballers and professional runners and cyclists and golfers and tennis players and skateboarders and ... do as well. But if you do any one of these activities at a low enough frequency and/or level that you're not buying your own specialised shoes, whatever sneakers you have will do just fine.

reply

abanana
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's because the way the sole slides is an integral part of bowling the ball. You can't play "properly" without a proper sliding bowling shoe.

I was a little surprised when the local bowling centres stopped bothering to make everyone use the proper shoes. I get what you're saying about playing casually, but when I last went bowling with colleagues, and won comfortably, and others were asking for tips because they just can't roll the ball properly, but won't try proper shoes, they tried to wind me up by telling me I was "cheating" by using the proper shoes that are offered for anyone who wants one - I can't win :)

reply

semi-extrinsic
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Appreciate the good answer. Out of curiosity, ofder of magnitude how much would a person need to be bowling to get good enough that choice of shoe matters?

reply

somenameforme
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you mean bowling shoe vs non-bowling shoe (as opposed to exact brand/type of bowling shoe), then they matter a lot even for a complete beginner. In a normal throw you're going to have a bit of momentum moving up to the lane and then release. You need to slide on your feet when you do this. In this [1] video go frame by frame at 12 seconds (or any time he bowls), you'll see his left foot in particular slide several inches during his throw. It's more subtle, but there's also a significant slide with his right foot as it goes across.

If you did this in tennis shoes, or any shoe with proper soles, the friction would cause your feet to stick and it'd be simply impossible. Socks would be much better than normal shoes, but then you have the opposite problem of too little friction and it's difficult to maintain control. Bowling shoes aren't like running or something where a pro runner is going to have some absurdly expensive pro shoe that improves his time by a fraction of a percent. They're much closer to something like ice skates for ice skating.And yeah that's a pro with perfect perform, but even a beginner who's not just walking up to the lane, stopping, and throwing, is going to have to deal with sliding. It's just part of the game.[1] -https://youtu.be/_qh4yOwCgOg?t=12

reply

fn-mote
 
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

> to get good enough that choice of shoe matters

Bowling shoe vs running shoe? As soon as you’re trying to get better, the shoes matter a lot. They let you use the established techniques.Bowling shoe vs socks? Never tried it, but I’m going to guess once you can break 100 that socks don’t cut it.

reply

bluGill
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Socks with no shoes are good enough for amateurs. Maybe even better than the worst bowling shoes. I'm not sure where the level of shoes matters is crossed, but socks gets that a lot farther than street shoes.

reply

dev_tty01
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Don’t drop the ball on your toes! It happens...

reply

TylerE
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A little bit of leather isn't really gonna help much there either.

reply

tmh88j
 
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

Mostly to prevent damage and minimize maintenance + cleanup. Dirty shoes can mess with the oiling and rocks lodged in soles can gouge the floor.

reply

evan_
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe they could issue those disposable over-the-shoe booties they make you wear at home showings

reply

Jolter
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Those are no fun to a customer. I’d much rather wear the loaner shoes.

reply

mixmastamyk
 
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

Hmm, thought they needed to slide. Like formal dance shoes, the opposite of sneakers.

reply

KennyBlanken
 
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

In the US they're just slippery enough to keep you from wrenching your ankle, the bowling lane knows they will have clean soles, and the soles won't damage the floor.

reply

Projectiboga
 
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

Reinforced toes? That might be a reason.

reply

section33
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We just charge a flat rate with shoes included. We do $5 / person or $25 for a whole hour for larger groups. Wanted to take some of the advanced calculus out of the price of bowling, yknow?

reply

mypalmike
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My local bowling alley charges $130 for shoes and 1 hour of bowling for 4 people off-peak. That scales up to $220 peak rates (e.g. Saturday night). It’s in the middle of a major city so it’s a different market of course, but the pricing difference is striking. No pun intended.

reply

Barbing
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Lucky Strike across from San Francisco’s baseball stadium prices like that, ouch.

reply

tclancy
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What is wrong with you, you’re going to ruin capitalism not caring about maximizing profits.

reply

Crunchified
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In capitalism, any intentional non-maximization of profits is philanthropy. Nothing wrong with that.

reply

Neekerer
 
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

spare me your humanitarian sarcasm

reply

tjoff
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Isn't that included in the lane price? Always has been for me.

reply

bee_rider
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think they mean the physical process of handling the shoes. At most places you rent your land and get your shoes at the same counter, basically in one transaction, which seems difficult to handle with a kiosk.

reply

section33
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Totally - we've got notifications wired in though, so our counter instantly knows "lane so and so needs such and such shoe sizes"

reply

KennyBlanken
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You're removing human interaction, though.

Nerds seem to forget that entertainment venues and sports are social spaces, interaction with staff matters, and is one of the more distinguishing features of a venue.Unless you've got someone walking up and down the lanes introducing themselves as the manager/owner/whatever...

reply

Johnny555
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If I go out bowling with friends, I'm there to socialize with my friends. If I rent the lane from a Kiosk, I'm fine with that being the end of the transaction I don't need the manager to come introduce himself.

reply

bluGill
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Most people don't know that the real money is food and alcohol. Buy pizza and drinks for everyone and they should throw the lane in for free.

reply

tclancy
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

How did you read everything OP posted and come to that conclusion?

reply

tjoff
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ah, most of what I've seen it's just an open area everyone goes to and does it themselves.

Which I like because I always have to try a few sizes to get one that actually fits.

reply

nomel
 
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

Which could be removed, which I, a customer, would very much enjoy. Bowling prices are absolutely insane these days. Haven't been in over 10 years. Related, nearly all of the bowling lanes in my area are empty, except for birthdays/work events.

reply

dpkirchner
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The last few times I tried to go bowling I was turned away because I was the wrong kind of customer. I didn't know when my kind was allowed (it wasn't on the outdoor signs). Layer I learned the right times but they were all weirdly inconvenient.

reply

quietsegfault
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

My local center in a big northeast us city is very cheap during the week, and reasonably priced on the weekends. Surprisingly, even their food and alcohol is priced lower than what you’d expect - cheaper than the sports bar down the block. No idea how they make money, but my kids love it and I love being able to get a good beer while I spend time bowling with my kids.

reply

bruce511
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think this is the key metric. Get people in the door.

Sure you can jack up prices on food and drink. Sure you can fleece the people who do come, but everyone who stops coming "because it's too expensive" is lost forever.The alternative is to create a space people want to come to. Yes sell food & drink. Being "good value" helps that. Being expensive fights it.While yes, the flashy electronics is cool, do people come for that? Does it make it more fun? I just saw the ball with my own two eyes. Does an animation make it better?What brings in a family? Work colleagues? Teenagers on a date? What brings in more competitive folks? Is there progression? What makes my friend group go once a week? Why do housewives want to hang out there at 11am? How to catch the bored teenagers at 3pm in the afternoon?It's not even just about bowling. Can you create a space people want to come to?

reply

robocat
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Can you create a space people want to come to?

Over many years I've tried to work out where a positive vibe comes from (mostly at food and beverage places).My current theory is that a good vibe is an emergent behaviour from the customers.Obviously poor managers/owners can make a toxic place (but negativity is a completely different issue from creating positivity). I've witnessed many owners think they cancreatea vibe, but then crash and burn (especially when taking over somewhere with an existing vibe). They often don't seem to understand how they failed (maybe have excuses that don't ring true). Starting or buying a business requires ego, but too much ego leads to mistaken self-belief.I'm sure a wise manager can encourage a vibe to grow, but actually it seems like the customers drive the process.Maybe it's just a human thing that like-minded people create spaces for themselves.I watched the vibe at one place radically shift from tradies to more gentrified customers. Same owners and staff. I also suspect I'm just not good at it myself, so I lack the skills to even see why someone is good (and might not even understand if they try and explain to me).Anyone else tried to grok how a good ambience grows? Is there some standard for learning it?

reply

robbak
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That really speaks to his initial comments of his being in a 'R&R desert'.

reply

topato
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

1. Can we stack two lanes on top of each other, please? Make homemade bunklanes?

2. Something about preventing people from rubbing the bowling balls on your precious lanes.3. Laser light shows + Liquor license = Bowling Alley Wine MixerSorry, I got overly excited by your reference. I say that so GD much, atleastonce a month, for nearly 20 years now haha. SOOO much room for activities!

reply

sleepybrett
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is interesting, i built similar for retail environments, oneoffs for events or windows or whatnot. I'm sure you could probably get away with a few terrible webcams per lane for ball tracking it's pretty much a perfect environment. A totally flat level lit are with very little noise with one circular blob moving through it. Might be an issue if you do the ever popular blacklight lanes night bowl thing, maybe just a switch to look for light blobs instead of dark blobs ;)

An NFC system for tap to play should be a pretty straight forward proposition as well on open hardware. Have tags, tie their unalterable ID numbers back to a credit card/account and you are good to go. Start it with your regulars, league players if you have them, whatnot. You can also tie that back to league scoring. A few lanes at a time.I'm excited for you, this is a super fun project with endless sidequests.

reply

HeyLaughingBoy
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Have you ever written online about your projects? This stuff is endlessly fascinating to me. And your suggestion about a webcam makes me think about a problem a client and I had a couple of years ago that was never solved. It would be a completely controlled visual environment, so an ESP-cam just be the ticket if he's still interested.

reply

kQq9oHeAz6wLLS
 
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

RFID tags in the heels of the bowling shoes, tied to the users account. Implant a reader in a spot by the lane - stomp to play!

reply

dd8601fn
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds like amazing fun. Good luck with it.

reply

Aboutplants
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love this idea!

reply

msisk6
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I grew up behind the bowling machines. My dad was a bowling machine mechanic and worked on machines all around the midwest. He often moon-lite as the on-duty mechanic during league nights and I'd go with him.

Mostly he worked at the local 16-lane alley with ancient AMF machines. The logic was all relays in a "chassis" on each machine. Relays would fail, pins and balls would end up where they're not supposed to be, folks would roll the ball into the sweep. All kinds of stuff. As a kid was was fantastic to see. A pinsetter machine is a real Rube Goldberg type contraption. Probably lead me to being an engineer.We had the several opportunities to buy a small-town bowling center, but looking at the economics -- even back in the 1980's -- wasn't good. Most of the operating profit back then came from alcohol sales and that's a totally different business.Good luck! Recently Facebook has been showing me a lot of bowling content. Be cool if it's making a comeback.

reply

cco
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

> Most of the operating profit back then came from alcohol sales and that's a totally different business.

I think this is typical of a lot of similar-ish businesses. Restaurants, bowling alleys, movie theaters, all run on high margin alcohol (or concessions) and make very little profit on the primary business.

reply

Suppafly
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah, even gas stations mostly make their money off of other stuff. if anything it's a little weird for a business to make their money off their primary business model.

reply

leetrout
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's hard to tell if it's making a comeback but it's getting attention.

Ben stiller produced a documentary for HBO "Born to Bowl" and it was very engaging.https://en.wikipedia.org/wiki/Born_to_Bowl

reply

nunez
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Bowling by itself isn't coming back, but bowling with other entertainment activities has been trending for a few years now. These lanes are usually low(er)-maintenance string lanes.

reply

monster_truck
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Is there a URL I can send people? I would like to show this to an OG in the pro circuit who has been looking to buy an alley and modernize it but is being dissuaded by the exact situation you are describing.

We so desperately need more 'third spaces' and Bowling Alleys are great for this

reply

idopmstuff
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Yeah good god OP please start writing a Substack about this! Engineer who buys a run-down bowling alley and cleverly fixes problems is exactly what the internet needs more of.

reply

codazoda
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I’ll second this. I’d probably follow along even though I don’t own an ally.

reply

angoragoats
 
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

No, not a Substack, just a regular blog please.

reply

monster_truck
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Seconded. I don't need, want, or read emails. I want a website I can go to and show to others

reply

alentred
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Professional techie and amateur bowler here. I am bowling on old-ish lanes, and the stats we have beyond the score is... well, ball speed only and it barely works on half of the lanes only. I doubt that our alley would ever agree to install anything ad-hoc, but I am super interested in finding out more about your build. If you have a blog, or can post photos and some information about your build I would be glad to read more.

Good luck with your new business!!! It sounds super exciting, hope everything works out, the roof, the patrons, and all.

reply

pants2
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Perhaps with strategic striping on the ball they could also get angular velocity, could come up with some very cool stats. Or if you're really having fun, microchip every ball with an accelerometer / gyro

reply

jevogel
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Bowlers often like to use their own balls, so it would be more useful to have a system that doesn't rely on modifying the ball.

reply

mritchie712
 
46 minutes ago
 
 | 
prev
 | 
next
 
[–]

This is far cooler than how I've been using my Pi.

I've started building a box for managing agents. I hate sitting in front of my Mac all day flipping between terminals. I wanted something that was audio and whiteboard / paper first.The Pi has a mic, camera, and projector hooked up. The Pi is always listening, so I just say most commands (i.e. "check logs on backend service, customer xyz said abc is wrong"). I can tell it "look at the board" and it can see things I've written or drawn and can project on top of or alongside anything on the board.Not sure yet if it's more efficient, but it's definitely more fun.

reply

jimnotgym
 
59 minutes ago
 
 | 
prev
 | 
next
 
[–]

I see in this one of the competetive advantages of the US at work.

I don't believe any patch of land that size, that you could build on in the UK is available for $105k, or about £78k. Let alone one with a partially functioning business installed

reply

doodlebugging
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Your project reminded me of this recent Texas Monthly article about nine-pin bowling alleys [0]. Your upgrades could help them draw in new customers.

[0]https://www.texasmonthly.com/being-texan/ninepin-bowling-end...I grew up in central Texas and bowling was a big family event. Dad was a frequent bowler, bowling in local leagues and travelling the pro-am circuit later. He debated going pro and ultimately, due to a job relocation, stopped bowling. Us kids were active in leagues for younger bowlers. We used to spend quite a bit of time at the bowling alley playing pinball or shooting pool (no video games back then). In those days, a bowling alley offered food and drinks so that you could take the whole family and spend day there without having to go anywhere else for anything. That may be the norm today too. I haven't bowled in about 6 years though.Best of luck to you! I love bowling. It is a skills game that is easy to learn and requires discipline to master.

reply

ajot
 
19 minutes ago
 
 | 
prev
 | 
next
 
[–]

I think this would make a very nice Youtube video, or ten. Quite niche, but interesting enough for anyone like me to watch.

Godspeed!

reply

starky
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

That is awesome. I worked at a bowling alley as a mechanic in high school (Brunswick A2) and got a sense of how stupid expensive the replacement equipment was. At one point another employee spilled their coffee over the keyboard used to control the score-keeping system, apparently the replacement was something like $400. What fancy proprietary keyboard did you get for that $400? The keyboard cable replaced with a phone plug.

reply

simondotau
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

One thing I've always wanted at a bowling alley is an instant slow-motion video replay of the pins being knocked down. Seems easy to do in theory, a Raspberry Pi + compatible camera could do this very easily, so long as you could mount it in a good locaiton. The only alley integration needed would be to tie into whatever sensor detects when the ball reaches the end of the lane.

* Mount a 60 fps camera pointed at the pins.* Continuously record a short looping buffer in memory (5 seconds would be more than enough).* When the ball-trigger fires, wait an extra second, then freeze the buffer and play the buffer once at normal speed, then again at 1/4 speed.* Finally, restart the recording loop.If it's a dark alley, you could use a low-light camera such as an Arducam with the STARVIS IMX462 (no IR-cut) and if ambient light is still too low, add a few infrared floodlights. Having instant slow-mo every time the ball hits would be a crowd pleaser, especially with kids and casual venues. If one of my nearby alleys had this, I wouldn't go to any other alley.

reply

desterothx
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Probably better to enable it only for strikes/spares as it would drain too much time, but the idea is great.

reply

seidleroni
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I live in the Boston area and there is a candlepin bowling place called Needham Bowlaway where the owner has done something similar. He automated the scoring system since nobody from outside New England really knows how to score it and it works really well. I believe he used some basic java code to detect whether the pixels at certain areas are white (pin) or not (no pin). He's always working on developing a video game every time I'm there although he may have finished by now. Maybe there's more overlap between bowling centers and software engineers than OP thinks.

reply

ajackfox
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

This is awesome, and I'm really happy that 
someone
 is trying this. Recreational spaces are severely lacking in so many places now: while I love digital things, it can't fully replace actual group activities in meat space, but I guess it's just not as profitable since it doesn't 
scale
.

I would totally be a patron with my family at your bowling center, and would love to read a blog or something about your journey.

reply

jjkaczor
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Heh - do you have a "blog" (ala jwz's DNA Lounge)?

(This is the kind of retiring from IT tale that I love to read and follow the trials and tribulations of over the years - good luck, thanks for open-sourcing your work!)

reply

Suppafly
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

man I haven't thought of that blog for like 20 years. crazy how many old blogs and web comics that I used to check every day that I've mostly forgotten about.

reply

MrBuddyCasino
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That one was perhaps more of a cautionary tale, given the economics.

reply

ColdStream
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

There is only one thing left to do. Get an old copy of Lightwave from the 90's and make more of those bizarre strike animations.

reply

czoido
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Awesome work! I would love to see this documented or at least a video of how everything works, not just to see the electronic setup, but to get a look at the mechanical internals of a 70 year old bowling machine.

reply

kilroy123
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I highly recommend you start a YouTube channel and document all this. It sounds like gold and would be really interesting.

reply

Huppie
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Back when I was in school I interned at a company installing bowling lanes / machines. Even back then it was fairly simple technology, no cameras or speed measurement yet, just some inputs from the machine as to what pin-cords had been pulled out (i.e. what pins fell down) translated to some simple animations. I remember the screens being just a simple VIA motherboard running DOS + their software from a compact flash card.

Sounds like a great project to work on given how cheap both hard- and software is becoming. Wishing you all the best!N.b. The forces in the machines can easily break hardware so be sure to move it away from the machine if possible, and otherwise protect it appropriately.

reply

ndiddy
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

In the US tethered pins with cords aren't really a thing, instead most bowling alleys use mechanical pinsetter machines. These machines are large, complex, and expensive (see here for a video on how they work: 
https://www.youtube.com/watch?v=Iod6uwUGM2E
 ) which is why he's talking about the equipment being 70+ years old- with the revenues most bowling alleys make, it's not economical to replace a pinsetter instead of maintaining the current one. This also means that the alley needs to have a mechanic on staff to keep the pinsetter running smoothly.

The way the machines detect the pins is still fairly simple. The assembly that puts the pins into place moves down after the ball is thrown, and has sense switches above each pin that detect which pins are still standing.

reply

fy20
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's worth noting that playing on string setters vs free-fall setters is quite different. The string alters how the pins move when they are hit. There's not really a "one is easier", it's more a different technique.

reply

Huppie
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah, I remember seeing both kind of machines. IIRC For the competitive scene string setters were (are?) a no-go but we installed plenty string-setters on holiday parks because they're just more economical.

I remember some classmates interned working on new / different firmware for the machines you're talking about though. Fun project for an internship!

reply

kamranjon
 
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

Unfortunately it is becoming more and more common for US alleys to use the pins with cords systems. Many lanes will actually upgrade to this system and I feel it is a mini tragedy in a way. I am very happy to see this because it gives me hope that there might be alternatives for bowling alleys who are considering the string based systems.

reply

ErroneousBosh
 
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

Pinsetters scare the everloving fuck out of me.

I did a bit of work for a bowling alley 30 years ago. The guy that had just bought it wanted their 1970s computers brought up to the spec of the 1990s ;-) He'd retired from an incredibly well-paying job offshore so was well and truly familiar with working on large electrical machinery on oil platforms.Day one - before he even turned the main incomer breaker on in his new bowling alley - the very first thing he did was sit everyone down in the dark and silent cafe and explain the idea behind and importance of LOTO. He didn't want to see anyone near any of the machinery without it locked out and tagged out, ever, for any reason, not even near it. As I recall the phrase "never work in this industry again" was used several times.

reply

redwall_hp
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm disappointed that the USBC is starting to certify tethered pin setups, though it is fortunately a separate category of competition. The pin action is wildly different.

reply

section33
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Same here. We're running Brunswick A2s that are just ancient, and they're buggy... but I wouldn't trade them for strings if I had them given to me, honestly.

reply

RickJWagner
 
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

String setters are on the way. They’re far cheaper to buy and run.

Bowlers hate the idea, but bowlers hated synthetic lane surfaces, urethane lane surfaces, and even lacquer surfaces before that. They also loved their old urethane balls, super soft plastic and dodo balls. All those changes went into place against the wishes of the bowlers, but that didn’t matter. Economics wins, every time.String setters are on the way.

reply

kQq9oHeAz6wLLS
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Economics wins, every time.

Indeed, it does. I wonder if anyone has ever correlated those changes to the decline in bowling popularity? It'd probably be difficult to verify how much of an impact it had (if at all) when there are so many other factors contributing to the decline.

reply

Cheiree
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Hi,

What you accomplished here sounds interesting, both from an entrepreneurial point of view and also from the engineering side.A good, nice, detailed technical write-up of what you achieved here would be very interesting. Maybe a Hackaday.com blog entry, too? Put it on GitHub?Have fun :)

reply

tclancy
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Agreed, this put a smile on my face for the day. What a cool thing to do in the specific and also in the more general sense of fighting back against “Bowling Alone” for your community.

reply

DANmode
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

+1 Hackaday

reply

busyant
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

The substance of what you wrote is interesting on its own, but I wanted to compliment you on your writing style. It was an enjoyable read.

reply

mcherm
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I nominate this post as an archetypal example of content that belongs on the Hacker News site.

Thank you for sharing; I'm so glad for you that it worked out.

reply

xxs
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Indeed, and it's filled with top-level filler comments unfortunately.

reply

kachurovskiy
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'd make all ESP32 controllers the same - same ready-made PCB, plug-in terminals for the controller and screw terminals for inputs and outputs. ESP32-S3 has enough of IO to handle an absurd variety of tasks. You can have at least 40 ESP32s on the same WiFi reporting data within milliseconds of the event and taking commands via HTTP APIs. Firmware updates are easy over WiFi, too. You can probably have the same firmware for all of them with precise logic configured via the HTTP API. Works well for me in 
https://github.com/kachurovskiy/nanoels
 - albeit with just 1 ESP32 per machine :)

reply

pauli5
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

With a materials to retail cost multiplier of x10 (which is on the low side), your system wouldn't be cheaper than the commercial one unless you can build and install it yourself. I doubt most centres would have the skills available to do this.

Nonetheless, you've done a fantastic job here.

reply

hinkley
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Short repairs are always nice, but I'm curious about the frequency. You're your own repairman, but that won't be true for all owners. So it's not if the repair takes 5 minutes, it's how long the lanes are down any time there's a problem.

I wonder what sort of things you could do to harden the system. From potting to overbuilding to redundancy.

reply

TylerE
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Was looking for this comment.

While I'm not really defending the markup of the commercial system, you're not so much paying for the system as you are paying to have someone to call when it breaks, ready spares inventory that can be overnighted, etc).

reply

portugueasey
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m living in an R&R desert myself, with some nice big abandoned shops, and have always wondered about the economics of building something. It amazes me how expensive a bowling alley actually is. Fantastic work in getting your costs way down, and doing something so genuinely useful for a wider audience. Hopefully other small bowling alleys will find this and try it out

reply

justsad
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

There’s a series of absolutely solid arcade game repair/service videos on YouTube, showing common faults and how to diagnose and fix them. The videos were actually recorded as part of a training series for working technicians during the hey-day of arcade games (now long gone in the West). Time was money so the diagnosis and fix had to make dollars.

Looking at the insides, there are massive circuit boards with dedicated logic chips - your standard HEF series NOR and NAND gates and all sorts of things. Boards mounted on boards. Huge mechanical relays with a loud clunk. All of it can now be replaced by parts that are tiny, solid state and are highly unlikely to fail due to wear/tear/usage. Granted, we all moved over to MAME long ago, but this post does not surprise me.

reply

BaseBaal
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Do you happen to remember the channel name or have a link? Would love to see some OG service videos.

reply

walrus01
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

> My family and I bought an abandoned 8-lane bowling center in the rural mid-west. In our small town there weren't many recreation options for families. You've heard of a food desert? This is an R&R desert.

On a topic not exactly related to the implementation of the ESP32 and hardware, what other R&R activities can one add to a bowling alley to make such a facility more popular and attractive for the locals? It would be very interesting to see some photos of your facility and what you've done with it since you bought it.

reply

HalfCrimp
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

> On a topic not exactly related to the implementation of the ESP32 and hardware, what other R&R activities can one add to a bowling alley to make such a facility more popular and attractive for the locals?

Pinball seems to be having a bit of a renaissance in some areas

reply

zrail
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Having grown up in a small midwest town in an R&R desert, I think the canonical answer is a liquor license.

reply

walrus01
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've always wondered about these when I see bars in tiny towns in rural parts of WA, OR, ID because the only way to get home is to drive drunk (I 
seriously
 doubt that the locals are organizing designated drivers for carloads of intoxicated people, and no taxi services exist). It seems they just take a gamble on not crashing and not getting caught by the local law enforcement.

reply

unclad5968
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Having grown up in a town of about 5000 people and 3 bars, yes this is what people did for the most part. I'm sure it's different depending on where you're at. Sometimes a DD actually will drive everyone especially since most people are less than 10 minutes away.

reply

nunez
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

This is all extremely interesting.

Lanes have been switching to Brunswick all-in-one string pinsetter/scoring systems due to, in large part, operational cost and lack of options. (Many bowling alleys still rock A-2s or GSX pinsetters whose part costs are sky-high due to not being in production anymore). The ones that are trying to not become Bowleros or Punchbowl Social type establishments might be interested in this!Have you posted this to /r/bowling yet?

reply

ivanjermakov
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

> Sure, bowling equipment is niche, but the open hardware and software landscape is amazing

Absolutely. This is what makes open source extremely powerful - ability to take absurdly small niches no big tech company is willing to fill.

reply

logdahl
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Really interesting stuff! If you're looking for bowling animations I'd look into 
https://youtu.be/ZXpETSoNWxY

Made me laugh.

reply

bschwindHN
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Also came here specifically to make sure this was posted. I'd pay good money to go to a bowling alley like this with friends.

reply

Baeocystin
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I was hoping someone would post Corridor's animations. What better for a custom rig! ...at least when playing with friends.

reply

GTP
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Great project! As I like playing with ESP8266/ESP32 boards myself, I would enjoy reading more about your bowling adventure.

reply

riazrizvi
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

This is great content. Have you thought about a second income stream by teaching prospective tech business owners on Youtube? It's a model ppl are successfully using?

reply

gonzogato
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I love stories like this. You’re doing more for your community than you even know!

reply

ectoloph
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I think that an overview of how the machinery works and how it interfaces would be interesting.

As a side note, I do enjoy the bizarre bowling animations that the screens come up with.

reply

harvey9
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

When you're up and running you should put up a display of some photos and explanatory text about the system. Might get some local kids interested in engineering.

reply

0_throwaway_000
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Have you thought about starting a youtube channel? I would love to hear more about the tech and the business.

reply

cucumber3732842
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Unless you have a stay at home spouse or teenage child who wants a video editing hobby it's usually just a huge time sink.

reply

xxs
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Even setting up camera, lights - etc. goes in the way of doing things. Then someone would have to narrate it, and so on.

reply

misiek08
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I would love to see some blog posts and/or videos about this!

reply

leecommamichael
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I started bowling in my teens and as a programmer have often wondered about how these things work, and have had a few opportunities to peek under the hood of the machines. Incredible stuff. Thank you for this work, I'll point my alleys to your creation when it's public.

reply

ruaraidh
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Ah, that's extremely cool! I'm enjoying hacking around with ESP32s etc at the moment (maybe it's just nice to do something physical that an AI can't) and it's amazing how mature the hardware ecosystem around them is. I'd love to hear more, both about the tech and the economics.

reply

anonu
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Thank you for sharing. This type of stuff gets me pumped up. It just shows that tech improvements usually 10x - or in this case 1000x - some old metric. In this case its cost. I think the same sort of rule of thumb applies to things like speed, features, user experience, etc... Getting this type of cost advantage eventually translates to a better UX, as you've alluded to. Way to go.

reply

aashhuttossh
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

This is cool! I too was thinking some time back about creating a CCTV for home using a Raspberry Pi 5 to avoid having my data leak over company-controlled data backups for those. But yeah, I guess I should start thinking about it again.

reply

orthogonal_cube
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Any plans to let people create accounts to track their scores over time?

reply

superdisk
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Are you getting any customers?

reply

section33
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

We're holding pretty steady at $3400-ish / month on open bowling alone. No leagues yet, no snack bar yet, no beer yet. It's not FAANG income by any stretch, but it's doing -so- much better than I initially expected!

reply

hahahaa
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Is that after costs? Are there much costs? I guess repairs, insurance, rates, taxes, power etc.

reply

luciana1u
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

75x markup and the entire moat was "what if your customers know what an ESP32 is." turns out one of them wanted Tron-themed laser shows bad enough to learn soldering.

reply

Tade0
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

> Any React dev can build their own UI and bowling animations.

About that: do you have any questionable quality animations for strikes etc.? To me it was always a major part of the whole experience.

reply

codazoda
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Not op, but, because I’m not a designer, I’d probably try to use an AI tool and maybe give it specific instructions to make it suck a little. Then again, not being a designer, I’d probably make it suck too, but it would take forever.

reply

eagerpace
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm a bowling fan and seeing this makes me happy. If I can help or you put something together for others to contribute, please reach out.

reply

easydidit
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Wow, this sounds super amazing! If you find the time to take some pictures or put it in a blog post, that would be amazing :)

reply

sanitizeai
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

This looks amazing! Wishing you the very best for your success.

reply

mianos
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Once I had more than a few esp32 sensors about the place, with my own firmware, I got serious about getting the OTA updates working and a good c++ wrapper around the nvram management. I don't like the vibe of multiple sensors not having the fixed firmware, just OCD. Github mianos.

reply

YeGoblynQueenne
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Wait. You didn't do all that without AI?

reply

bakies
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

With the dark patterns and lock in of LaneTalk I'm wondering if you plan at all to provide scorings to end users at all. Been getting sick of lane talk. I'm also wondering if you have any idea how LaneTalk gets their data and if it's possible to go to the source.

reply

dmboyd
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Did you consider using canbus? esp32s can handle canbus, and it would simplify the topology.

reply

deepsun
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Oh nice. I'm a hacker, finally I will be able to win at bowling for the first time in my life!

reply

dn3500
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Serious and maybe stupid question, also note I don't live in the US. Is this really needed? If you put a scoring pad and a couple pencils in each lane would your customers say "what is this shit", turn around and walk out?

reply

section33
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh yeah. We even have one lane pair the auto-scoring isn't working, we just can't assign most people to either lane. The machines themselves work fine, and we do have a way to bypass the failed unit - but for the generations that have never seen paper scoring, you'd think had asked them to file their taxes for fun.

reply

SoftTalker
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Growing up, never saw automatic scoring. Keeping score on paper was just part of going bowling. They had an overhead projector at each lane so everyone could see the score sheet.

reply

trbleclef
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I bowled some in the 90s. Back then these were still common:

https://www.youtube.com/watch?v=V1tMSdAswo4https://www.youtube.com/watch?v=HGhSoGizjxo

reply

devilbunny
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

In high school, I was invited every time even tangential friends wanted to go bowling because I was the only person who knew how to keep score on paper (the nearby lanes didn’t have electronic scoring). And that was over 30 years ago.

reply

allenrb
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This! I took “rec games” as one of my PE classes in high school. This involved bowling, among other things. A highlight of this was the time I bowled a 24…

However, as the class nerd, I knew how to score a game. My parents used to take us as kids. And fortunately, that was on the test. :-)

reply

Gangway0829
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not that it necessarily justifies the difficulty in making it work (which I just learned about, thanks OP!), but I absolutely adore the silly animations that play after you bowl. It's seriously make or break for me. I can live without beer and snacks, but it just isn't the same without the goofy animations.

reply

ChrisClark
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

actually, maybe yes for some people, it's been so common to have computer tracking forever

reply

jmpavlec
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Amazing post. I'm a enthusiastic bowler myself and in tech so this scratches both of those itches. These are the types of posts that keep me coming back to HN.

Best of luck and please post some images/videos of the prototypes in action.

reply

turkeyboi
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Ai generated wall of text is awesome!!!

reply

jmpavlec
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Re-reading it, I guess I can see the AI bits... But at least the concept is novel.

It didn't scream AI generated to me.

reply

euroderf
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

There's a scene where Jack Klugman's character is staying in a hotel in Buffalo and he leans out the window and he looks up and down the street and he says I never knew that one street could support eight bowling alleys

reply

codazoda
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m curious what sensors you’re using? My first thought was a camera up above the pins pointing down that can detect them. There are probably more reliable methods. If it were me, I’d seek to simplify as much as possible so things keep running smoothly.

reply

misiek08
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

While reading all about cameras and other sensor I would try to use distance-driven sensors every where. Standing pin vs laying one have enough height difference to not mislead even simple distance echo-based sensor. Other techs I see more reliable are LIDARs, because they don't require lighting. Pure camera should have enough light to see the pins (or you have to do some IR based markings and IR camera) or you can't make the space darker for events etc.

reply

bigcityslider
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Really cool. This reminds me of escape rooms. Since they're a newer thing, a lot of them rely on modern low-cost DIY stuff like this.

reply

ethin
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I had to read this twice because at first I thought it said that you replaced a $120 bowling system with $1600 in ESP32s and I was like "So you replaced a good-cost system with something more expensive why again?" :D

reply

articulatepang
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Hey! Thank you for posting. This a great project and an excellent illustration of progress in technology: commodity hardware and open source software got good enough that you could do this at such low cost and as a solo developer. Great work!

reply

beardyw
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

EspNow is really helpful in this kind of network.

For those not familiar it uses WiFi packets to send short messages without any WiFi log on.

reply

chromatic
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Good project! I've been tinkering with something similar for pinball, arcade, and other coin-operated machines. Lock-in for hardware and software there is a real bummer, but managing payments and security is worth the cost.

reply

shadowpho
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I’d love to see a schematic.

I’d highly recommend to make sure you have plenty of esd diodes and protection resistors on all inputs. That’ll help the longevity of the system.

reply

profsummergig
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I want to start working with arduino/raspberry pi/esp32/sensors.

What would be a good source to buy these in bulk (along with accessory components. e.g. wires etc.)?

reply

gregsadetsky
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Take a look at adafruit and sparkfun

You can find kits that have a selection of sensors - enough to get started and experimenthttps://www.adafruit.com/product/193

reply

0x62
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Aliexpress is king for cheap IoT modules/accessories

https://www.aliexpress.com/w/wholesale-esp32-s3.html

reply

dns_snek
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'd go with a more reputable vendor unless you're on a really tight budget because Aliexpress isn't even that cheap, all things considered. There are fake chips and really low quality parts out there that will waste your time.

You can get a range of ESP32 boards from Digikey for $5-$8 and you'd have to scrape the bottom of the barrel to get them much cheaper than that on Aliexpress.

reply

rufasterisco
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you have a nearby hackerspace or similar, check it out.

Likely they will be able to help you choose and guide you.For me the hurdle was less about finding equipment and more being able to learn from experienced people.

reply

Nerdrotic
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

All this tech is now off the shelf commodity items that anyone with basic skills can put together. For decades this tech was crazy expensive and required assembler machine language programming.

reply

curious_cat_163
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Where is this thing? Would like to visit!

reply

nhan123
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Awesome SRE approach to a physical legacy problem, looking forward to the GitHub repo

reply

nicoboo
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Excellent approach to an interesting issue... I hope you will share more information about everything around here! And good luck!

reply

JKCalhoun
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm in the midwaste. Love to know where you bowling alley is!

reply

wltr
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Cool project! Get a blog and post there, please! Photos, media, anything, is very welcome! One of the most interesting things I’ve read here in a very long time. Don’t let it be wasted to just lie here, for the very narrow audience.

reply

greggsy
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Any photos of the build?

reply

bigpussy
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Vendor lock-in wouldn't be a problem if successful businesses didn't become lazy, greedy, and dishonest. But somehow...

reply

effnorwood
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Much love and respect. Nerd on and may the strikes be with you.

reply

jasonmarquette
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

That is freaking amazing!!! Love it!!

reply

kasince2k
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

this post is such a breathe of fresh air (real "hacker" stuff). thank you for posting

reply

culi
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Excited to see the open sourcing of OpenLaneLink!

reply

tomashubelbauer
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Please share more :)

reply

kalev
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Honestly this sounds amazing for a vlog on YouTube

reply

saturn8601
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Did you use any AI to help you build this? If so, thats cool but if not, you are even cooler.

This is the dream. Imagine cutting out the fat with open hardware, experienced devs (assisted with AI) can rapidly learn and build systems and cut the overall cost of keeping a service running.This translates into savings for customers and could mean the difference between wage stagnated customers being able to enjoy that service or not. It can also mean the difference between a service being able to survive in a lower density area vs closing.That bloat from a vendor is eventually passed down to the customers. And to be frank, so many vendors do the bare minimum and get worse over time.I observe when people buy out an old place like an arcade, house or some other venue, rip out all the old to replace with substandard "modern" design that might be modern taste but just of poor quality(real wood, screen printing, high quality professional displays vs particle board, cheap LCDs, etc.). All of that poor quality is some vendors additional padded margin.So many "reformed" businesses are just some joker's passive income investment portfolio because they have to put all the money they have to use somewhere and they wont spend a single ounce of energy more than they have to. That means buying substandard junk from a vendor at whatever the vendor charges, passing the cost to customers and they have to just take it.Luckily with this declining K-Shaped economy more people are just deciding not to participate. Maybe that will put some fear into people who operate business like this.Will this be the very best bowling system ever invented? Maybe not but the cost savings might make it much more valuable because it allows more to enjoy the service.An average system thats low cost is better than an average system that you got to pay out the nose for. And the openness makes it possible that it could eventually become so much better than any vendor could possibly deliver.Maybe im totally wrong about this and the existing players in the 'bowling machine' space are stellar...but I have my doubts given what I've seen elsewhere.

reply

bakies
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been dreaming of owning an alley

reply

poolnoodle
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

This is the stuff I want to read on HN!

reply

mstaoru
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Why ESP-NOW and not ESP-WIFI-MESH (that has routing, self status, retries, etc. builtin)?

reply

omegadynamics
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

show it running doom and I'm on board

reply

sann2011
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

woah! that's cool

reply

pstuart
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

This is awesome! As others noted, it would be cool to have some YT videos about this that might inspire others and promote your project. I'm sure you have copious free time to do this ;-)

reply

westurner
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

- A Digital Twin of the facility in 3D?

- R3F and Drei for React-based 3D Three.js animations; but it might be best to pre-render at high FPS and encode with ffmpeg- ProjectM, MilkDrop3,limit- TIL about shuffle skating aka jam skating- OpenNext NextJS- Serwist for a PWA so that you can access your stats when not connected- IndexedDb, sqlite-wasm, duckdb-wasm- To run lights, projectors, etc. (with low enough hertz to avoid PSE Photosensitive Epilepsy risk) I have heard about: OSC (BespokeSynth, Resolume,), SMPTE LTC, Resolume projection mapping, mapmapteam/mapmap projection mapping,Open Lighting Architecture has a list of 
Ethernet Protocols including OSC, and a list of USB/Serial/Network devices.HyperHDR does ambient lightning to match displayed video.Sometimes the glare from all of the lights is too much for visually impaired persons and animals FWIU; no varying lights hour might win too.- If the machines are so old that all you need is a relay, there's possibly not as much need to model the whole system with TLA+ and check the proof.Could ask the model about an 
"SIL" (Safety Integrity Level) controller or similar for a bowling alley. Rust RTIC and Rust embassy have RTOS features.How to write unit and integration tests for the system without hardware simulators that can randomly fault.- Soft-white backlit multicolor(?) ePaper displays would save energy and cut glare.Most flying insects cannot see red, orange or yellow light;Red preserves night vision. Blue keeps operators awake. Blue and white cause the worst glare. Jet instrument gauges are reddish/orange-ish.- UV Blacklight paint, UV LED Black light.Blue light glasses are great for reducing UV blacklight glare.- Best LED projector 2026- Gogs/Gitea/Forgejo host Issues, repos and can run Actions with nektos/act.Cool project. 
Integrate an issue tracker with mobile notifications?

reply

0xbadcafebee
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

$120k for a customized system that's central to your entire business doesn't sound that expensive really. Can you make your own? Sure, but the devil's in the details. Complex systems are always more difficult to make reliable than you think. If it's down and you're losing business, who do you call? Yourself. Besides being a bowling alley owner, now you're a tech startup entrepreneur with one customer. It might end up fine, or you might end up with a whole new set of headaches.

reply

holoduke
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

It's nowadays so easy to create your own custom esp32 thing. I used to control a home battery installation. Used it on a old Landrover defender where we added a complete dash unit with digital gauges. Used it for controlling a Zigbee 12v switch to activate sprinklers in a garden. In combination with Claude one can create an entire setup in a couple days. Before I was sometimes spending a week on the lcd drivers alone.

reply

eudamoniac
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I know this is rationally a good thing to do, but I can't help but be sad imagining this bowling equipment company being run out of business because someone wanted to do their jobs but for free. It's kind of absurd from their pov. Like imagine you own a cafe you've worked hard to grow into a successful business, and then next door some guy opens a cafe with infinite free coffee just because he is a generous guy.

reply

jimnotgym
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Yes but the alley was closed. They couldn't pay the company anyway. The big providers will still pay the company, because they want support.

reply

lowbloodsugar
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am compelled to ask: Can this equipment take someone’s arm off? Do you have insurance for that? Does you insurance know you wrote this yourself?

reply

jimnotgym
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Yes it can take an arm off. But that is not the bit that is being controlled by him. The machine starts with a single relay...he fires the relay and keeps score

reply

jaynate
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

>> Thanks for reading! Let me know if anyone's interested in more posts about this bowling nonsense.

I’d say, “yes!” judging from the upvotes.

reply

bena
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you know how often is the score keeping system replaced or requires repairs?

You could potentially have a decent side gig replacing scoring systems for a fraction of others

reply

quietsegfault
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I would love to watch YouTube videos on your work!

reply

Joel_Mckay
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Nice, sounds like a lot of fun. A few years from now one may have 2 businesses, as solving the niche issues is how small business happens. =3

reply

newobj
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

God bless you

reply

omegadynamics
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

show it running doom and ill believe you

reply

underdeserver
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm interested in more posts about this bowling nonsense.

reply

kevinh456
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Github bro. Github.

reply

TZubiri
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

That's awesome.

That said, didn't you just shift the cost instead of reducing the cost?It's of course subjective, and the goal of the question isn't to devalue your work, au contraire, I'm saying that you contributed 120k worth of value.This is as-is a product that you can sell to other bowling alleys, and do not fall into the trick of selling savings and pricing it at like 20k. Your product may be better as it can be customized, modernized, it has a single author and less bureocracy than a corporate 30yo bundle that was handed over through 5 generations of programmers after resignations and layoffs.Good luck

reply

cworsley4
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

You this guy?

https://youtube.com/@yohnmav

reply

hyperhello
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Real question. Did you have any contact with organized crime? Some of the 'territory' of nothing-type technologies like vending are said to be 'owned' by certain groups.

reply

section33
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Not that I know of! My market research shows something like < 3500 remaining bowling proprietors in the US, down from 12k in the 60's. I think the lack of alternatives is just a matter of being super, super niche -and- a legacy industry if I'm being honest.

reply

washadjeffmad
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's strike one from the Bowlero family.

reply

jnaina
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You mean the Bowlini and the Pinini families

reply

Copenjin
 
5 hours ago
 
 | 
prev
 
[–]

I came for a blog with pictures and details on the development and found none :(

Edit: I had to search for this on my ownhttps://sesamedisk.com/diy-bowling-system-esp32-replacement/

reply

xxs
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Look at the picture at the title - RTL8103EL - which has absolutely nothing to do with anything regarding the text below. Then it quotes HN comments

reply

novafacing
 
5 hours ago
 
 | 
parent
 | 
prev
 
[–]

Pretty sure this is an AI summary of this HN post, not the other way around

reply

Consider applying for YC's Fall 2026 batch! 
Applications
 are open till July 27.

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