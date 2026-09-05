---
title: 'Ask HN: Resources to get good at soldering? | Hacker News'
url: https://news.ycombinator.com/item?id=49533840
site_name: hnrss
content_file: hnrss-ask-hn-resources-to-get-good-at-soldering-hacker-n
fetched_at: '2026-09-05T13:42:04.036947'
original_url: https://news.ycombinator.com/item?id=49533840
date: '2026-09-02'
description: 'Ask HN: Resources to get good at soldering?'
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
Ask HN: Resources to get good at soldering?
161 points
 by 
tosmatos
 
19 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
91 comments
Hello. I've recently started soldering, specifically wanting to repair the joysticks on several Playstation 4 controllers I have, but I also want to get good at electronic repair in general.

Right now I've busted a board, and managed to desolder and resolder a stick but the controller doesn't turn on anymore. I'm doing this all by myself, and I think I'm following good advice (ventilation, good iron tip, using flux etc...).But there are many variables, and a lot of experts have different opinions on stuff. Does anyone know good resources that I could use for getting good and making less mistakes ? Thanks.

 
help

opan
 
16 minutes ago
 
 | 
next
 
[–]

Lots of good general soldering tips here. If the DualShock 4 PCB is half as complex as the DualSense PCB, good chance you scratched a trace whole removing the sticks. If you can locate the damaged area you can jump it with a bodge wire (think of it like a wood bridge that broke in the middle so you can't walk across, and you make a small path with planks enough for one person to still cross, restoring the connection). Also make sure you didn't introduce a GND short, you may need to cut a trace in 1 or 2 spots in addition to jumping the damaged area if you did. I had a hell of a time getting out the first analog stick on a DualSense and ended up damaging the PCB. A multimeter in continuity mode is a must here for checking that the signal travels the expected path or finding the issue if it doesn't. It is most likely fixable, it was in my case, though it may take you a few days of troubleshooting. Also I would recommend a desoldering gun if you're going to do this a lot, analog sticks are very difficult to remove with just an iron. Often just the tiniest bit of solder clings to the pins in the holes and it won't budge. A hot air station could also work, but these have a tendency to melt all surrounding plastic before the solder and IMO are a last resort.

Look at the traces that go to the stick or that are near that area, look for scratches.

reply

sandreas
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

While soldering is not that hard, different tasks require different tools. Most of them can be from very cheap to very expensive. As a beginner I'd recommend the following:

A small USB-C soldering iron supported by IronOS[1], e.g. Pinecil vor TS100A solid stand with brass woolA KU soldering tip (looks a bit like a knife) for good heat transfer, too small tips are not goodThin (<=0.5mm) solder wireNo clean flux (not a pen)Isopropyl alcoholSolder fume extractor (DIY is OK, if you're building it right) is good for your healthSolder mat (blue silicone)Multimeter (not too cheap, around 20 bucks)Self closing tweezersNormal tweezersA wirecutter (blue 5 bucks from ali express)Manual Desoldering pump (engineer ss03 or a clone for cheaper)Most important is cleaning (alcohol, then flux) and heat transfer (tin your tip, your pads or your wire before putting things together to ensure good heat transfer). Cleanup nicely and tin your tip after soldering to prevent corrosion.Optional but helpful for more professional tasks:Hot air stationAuto Desoldering pump (ZD-8965)Adjustable power supply (fnirsi usbc, 30 bucks)Oscilloscope (mini beginner with display Cost around 30 bucks)Capton tapeSolid Copper wire1:https://github.com/Ralim/IronOS

reply

eimrine
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Most of those is not a must. For me one of the most important thing is Rose alloy and some copper braid for desoldering. Also rosin is one of the best flux available because of guaranteed no corrosion. Also it is best to have not only copper soldering tip for good heat transfer but iron soldering tip as well because it will not get bent when agressively digging some crap.

reply

robk
 
42 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you have the budget the Hakko desoldering gun is a huge huge improvement over desoldering by hand w copper. I've gone from hating it to desoldering junk to harvest parts because it's so easy.

reply

eternityforest
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

C245 clones seem to be the new current standard tip format, they're pretty nice.

Not supported by any open third party firmware usually, but that's fine with me.One thing to watch out for is tip grounding, some cheap irons leak a few volts at micro to milliamp level power, relative to ground, which could matter if you solder very sensitive things that are grounded, which you probably don't.DIY fume extractors are hard to do, you need powerful fans unless you have an arm to put the extractor right above the iron. Also remember that when it's just sitting in the stand, it will still smoke for a few seconds, so the extractor must cover that too.Those thin wispy activated carbon pads probably aren't doing much, you need actual particulate filtering like a HEPA or similar, but almost anything is better than having the smoke directly in your face with no fans.

reply

butvacuum
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

and breathing flux is a far larger concern than leaded solder. Physically getting them somewhere (eating while soldering, not washing hands, etc) is still a problem.

reply

nromiun
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Both lead and lead free solder use the same chemical flux in their core. So you have the same problem with leaded flux cored solder. With the additional problem of lead.

reply

scarecrowbob
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice list.

Maybe a bit over the top for a lot of situations. I assume folks would acquire these things over a long period of time depending on their projects or what they are repairing. I have a 2-ch function generator coming because after 20 years of bodging stuff together and fixing minor things, I am tired of using the super cheapo one I got back in the day. It takes a while to amass all that crap, but it's fun.A couple other thoughts: used hemostats are super helpful for a lot of things. for a lot of years I avoided getting any kind of "3rd hand" because I would use combinations of hemostats.Or jigs- I have a very old piece of wood that has hole drilled for m and f XLR and 1/4 audio connectors with notes about which pin is which. Making tools like that is quite satisfying.I really enjoy having a stack of stainless steel condiment cups to put screw in- I stack them up during a disassembly and then unstack them as I reassemble.Also I will say that while I thought building one of those cheap-o oscilloscope kits was a pretty fun practice and I can recommend that, I don't fine them easy enough to use for beginners... the 2-ch Rigol scope I got was not super expensive and felt like the cheapest thing I'd be recommending to folks.Finally, I have had a lot of mixed successes with desoldering pumps. It took me a long time to figure out that I can only get desoldering braid to work if I put liquid flux on it, but that made it a lot cleaner for me than the solder suckers.

reply

sandreas
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh I forgot... a big magnifier glass (8x to 15x) with an LED light is way cheaper than a microscope and very helpful for small parts soldering (SMD) :-)

reply

mianos
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have a microscope, but once you get used to using hot air, you don't need it for soldering, just inspection.

reply

Retr0id
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

A cheap clip-on macro lens for a phone camera is also good for inspecting things, without the cost+space of a proper microscope.

reply

analog31
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

True but you can do actual work under a stereoscopic microscope. It has a vaunted place on my workbench.

Disclosure: Old person. ;-)

reply

SAI_Peregrinus
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've got one as well, and I'll say it's extremely nice for removing splinters. I do a bit of woodworking, so it ends up being unexpectedly dual-purpose.

reply

analog31
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Indeed, I'm the designated family surgeon. I've removed more splinters from people than I can count.

reply

radicalbyte
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I have a $40 head-mounted thing with integrated light and it's awesome for modern boards.

reply

SAI_Peregrinus
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I will say it's important that the soldering iron be temperature controlled. It's especially nice if it's one with the temperature sensing integrated into the tip in a cartridge (like the ones you suggested).

Also, 63/37 tin/lead "eutectic" solder is the easiest to use. Wash your hands after using it, or wear gloves. 60/40 solder is almost as easy, and cheaper. Lead-free is more difficult, especially for learning. Learn with lead solder, then switch to lead-free.

reply

eternityforest
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think there's no real need to learn with leaded anymore now that we have temp controlled irons and better fluxes and such.

Wearing gloves and washing your hands five million times is more annoying than just using lead free.And even with perfect precautions, the flux expands and makes it spit tiny little balls, which then contaminates your whole work area with a somewhat fine dust.

reply

skhr0680
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Wearing gloves and washing your hands five million times is more annoying than just using lead free.

RoHS was more about removing lead from electronics as a whole than health risk to an individual from soldering. To put it into perspective, if you lived in a city before the 1990s, you've already inhaled more lead than you ever will from soldering.

reply

kube-system
 
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

Flux can be hazardous too, even if your solder is lead-free.

But in a non-occupational exposure setting you're not likely to have issues if you solder occasionally even with lead solder and don't take any precautions.

reply

dotancohen
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Also, make sure your solder is high quality. I've ordered solder from AliExpress - both leaded and unleaded - and they were terrible.

reply

Retr0id
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> A wirecutter

Yes, but buy several. Maybe it's only because I buy cheap crap ones in the first place, but I treat them as consumables.

reply

boothby
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What are you using them for that consumes them?

reply

rzzzt
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If the sharp end chips, you can't get close enough to the things you want to clip.

reply

Retr0id
 
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

Cutting wires, mostly.

reply

probablybayesed
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Interesting, I want to hear the full story.

reply

whycome
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is just a great starter list. Thank you

reply

colechristensen
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>Capton tape

Kapton tape

reply

XorNot
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Get your self a microscope stand, digital from AliExpress. The 7" screen ones are quite cheap and being able to see up close what you're doing makes all the difference in the world.

reply

tamimio
 
1 minute ago
 
 | 
prev
 | 
next
 
[–]

Get one of those training boards and keep repeating till you master it, the trick is to heat the board and you put solder and wire on it, not how most beginners go by heating the solder itself. Flux and other things are there as an aux to help in certain cases. I have been soldering since i was a kid (thanks dad for having the machine) and I use only two tips and some flux occasionally, nothing too crazy and don’t go obsessing over the details or the device brand or such.

reply

timnetworks
 
18 minutes ago
 
 | 
prev
 | 
next
 
[–]

Helping Hands! Articulating clips on a heavy base, sometimes with a magnifying glass, to help you keep two objects or two parts of an object at some specific angle/distance/etc. so that all you need to worry about is the fumes.

Exhaust fan! Put your station next to a window, both for light and ventilation.

reply

Surac
 
26 minutes ago
 
 | 
prev
 | 
next
 
[–]

Old day soldering was much more easy. We had lead in the tin. Today leadless tin makes soldeing very hard. Use flux. Enormous amounts of flux

reply

jimnotgym
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Like all practical skills, practice!

Soldering new is easier than repair.Get some dirt cheap ali express electronic kits and solder them up. Or get a load of components and some strip boards. Lead solder is much easier to use.Basic antex iron. Stand with sponge...dab of solder on the iron, wipe on sponge, push iron against both board and component, feed in solder, admire.For repair work, you want scrap boards real boards. Desolder all of the components, put them back.Practice. Buy the fancier stuff once you know why it might be useful.If you are going to do much soldering you need some kind of extractor. Flux in solder will cause breathing problems fairly quickly.

reply

hypercube33
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Ts80p iron is super crazy nice for the price. Heats up really fast and there are a lot of tips out there. I'd say it beats my two soldering stations if you're only doing soldering.

reply

JohnFen
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

You don't need any real educational resources to get good at soldering. Any random primer will do. It's genuinely a simple task that doesn't require a lot of explanation or have a lot of tricks.

What gets you good at soldering is just practice. Solder a lot. A fun and easy way to do this is to pick up those cheap ($5 or less) electronic solder-it-yourself kits and do a bunch of them. Include ones that contain small surface mount parts.You can also practice desoldering on them, or pick up broken electronics and desolder parts from those.> managed to desolder and resolder a stick but the controller doesn't turn on anymore.There's a chance to practice repair (which is a completely different topic from soldering)! Odds are very high the problem is that you've made an unwanted solder bridge or you have a cold solder joint.

reply

Animats
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

> repair (which is a completely different topic from soldering)

Yes. There's repair, rework, build and debugging.Repair is mostly diagnosis, followed by cleaning and repair of mechanical damage. ICs themselves don't fail much. That's what the original poster is doing.Rework is mostly careful desoldering followed by new component installation. That's when hot-air rework stations are needed, if you have to replace ICs. This is a "use the right tool for the job" task, where you have little metal heat gun air guides for each IC shape. (I have a bag of those things.)Building, where you start with a blank board and a supply of components, all with a known-to-work design, is just small scale manufacturing. It takes some skill and training, but the process is simple and repetitive. It's automated in production shops.Debugging of new board designs requires not just soldering tools but the test equipment to test the thing and an understanding of how it works. This is what electrical engineers and technicians do.

reply

Retr0id
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I find watching videos of other people soldering is almost as good as practicing myself.

reply

kube-system
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I get frustrated watching soldering videos online because there are a lot of videos online of people who are really bad at soldering.

reply

Retr0id
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is why I watch videos of challenging repairs, it would be impossible to succeed without being good at soldering.

reply

brudgers
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Or both.

reply

ylynbuilds
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Seconding the practice-kit thing, but for the dead DS4 specifically: before you go hunting the joint you reworked, check whether you lifted a pad or cooked a via near the stick. On those boards the stick pins sit right next to thin traces and a hot iron parked too long will pull the pad up with the pin. Easiest check is continuity from each stick pin to wherever the trace lands, and check 3.3V is present with it plugged in - if the rail is gone you probably bridged something, not broken the stick.

Other thing that got me: no-clean flux residue plus a cheap iron with a bad ground can look like a dead board when it's just leakage. Clean it with IPA and a brush and retest before desoldering anything else.

reply

dannyboland
 
45 minutes ago
 
 | 
prev
 | 
next
 
[–]

The principle behind a lot of good advice here is “creating the conditions for solder to naturally go where you want it to”. Cleaning, tinning, preheating are all part of creating those conditions.

So the moment you find yourself fighting or forcing the solder, it’s better to step back and create the right conditions.

reply

MarcScott
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

1. Use a soldering iron that can hit 400, and use a needle tip

2. Use leaded solder - lead-free is a pain. If you're not doing this for hours every day, even without ventilation, you'll be fine.3. Heat the pads you're soldering to, not the solder. I used to tell kids to hold the iron to the pad for a count of three, then feed the solder in.4. Two additional tools I find helpful - a solder sucker and copper wick.

reply

simonbarker87
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Number three is basically the golden rule.

From memory when I ran a production line with soldering stations ventilation is equally (and possibly more) important for lead free solder.

reply

peterfirefly
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And do it with enough solder on the iron to get good thermal transfer. "Enough" really isn't a lot but it's also not a tip that's been wiped entirely dry. How you hold the tip relative to the via/component lead matters (because you want the liquid solder to help with the thermal transfer).

reply

nizmow
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

The biggest thing for me was just being brave enough to go for it and give it a try, and then learning how to undo your mistakes. Re-do things you’re not happy with with braid, reflow things with flux, etc. I’ve torn vias out of old valuable boards doing restoration, and I learned trace repair and fixed it.

reply

MrBuddyCasino
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

> 
just being brave enough to go for it and give it a try, and then learning how to undo your mistakes

This is true for most things. Don’t let the naysayers discourage you.

reply

MithrilTuxedo
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

NAVAIR 01-1A-23

https://www.robins.af.mil/Portals/59/documents/technicalorde...I was a 2M Mini/Micro repair technician for a few years in the Navy. That book was our school and manual.

reply

mikewarot
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

My late friend Ward was a strong supporter of Build-a-Blinkie[1] and their mission to teach people to solder by doing.

My friend Jim's been soldering since the 1950s. We solder a lot of things with leads, for this, his method is to get each item to be joined tinned, then use solder as a mechanical joint. Melt in the solder, remove the iron but hold them together, then once cool, tug on the joint to make sure it holds.[1]https://build-a-blinkie.org/events.php

reply

sdcfgy
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Find some trash and practice removing parts and soldering them back on first.

Not mentioned here yet but the majority of early soldering attempt failures mostly come from crap irons and crap solder not human issues. You need a decent quality temperature controlled iron and decent quality solder, preferably flux cored if you're doing repairs. Here, I have a second hand Metcal iron which cost less than the much recommended Hakko irons and is orders of magnitude better. Solder, I just use thin 60/40 multicore. Avoid the lead free initially until you have some practice.Watch soldering videos on youtube. Check the comments to make sure people aren't slating their technique.Removing some parts, like DIP packages really does need specialist irons with vacuum pumps built in to not mangle them. Desolder braid and solder suckers are absolutely no good for that sort of stuff and tend to lift pads.

reply

imtringued
 
54 minutes ago
 
 | 
parent
 | 
next
 
[–]

Correct, half the skill in soldering is picking a good iron with good tips. After that it's the solder.

Only at the very end does your own soldering skill matter.

reply

FLeXMurphy
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Hi tosmatos,

Please have a look at PACE soldering/desoldering videos on youtube. They are dated but very good in general. You don't need a lot of videos, just the basics.https://paceworldwide.com/video/basic-soldering-lesson-1-sol...You don't need to spend a lot of money so I'll keep it simple:Get yourself a few kits of SMD soldering components and practice. Amazon, AliExpress, whatever.Some notes on technique:You will be surprised at the tip size that works well - usually slightly larger is actually better, just need to get comfortable with the angle and size.Have a magnifying lamp or something like that to help you see better.You should always use alcohol (70-99% IPA) and flux. Clean everything properly, then flux it, then solder it. Then clean after you're done. Have a few flux pens on hand. MG Chemicals sells these things. You can also get the bottle version and some empty bottles with syringes that mount on top.Using a "shoe" iron tip is nice because you can angle it between the lead of the component (through-hole) and the pad, and this gives you a little entry way for your solder to flow. The flowing, hot solder will then naturally heat up the rest of the pad. This is a thermal mass effect.The alternative of having the iron tip on one side of the lead, and the solder wire on the other is not bad either. This makes the solder "flow" across the pad, but it does mean you don't get the thermal mass effect of the first approach. You may need to do this in tighter spaces. Regulate temperature wisely.For through-hole components, most often the hole itself is plated so it is a double-sided pad, give it an extra 0.5-1s for the solder to go to the other side appropriately.Make sure you have small wire cutters and nose pliers. The nose pliers are very handy when you need to shape the leads of transistors or chips that have 4-5 legs exactly to the through-hole positioning. Not usual, but not uncommon to see staggered layout.You will make mistakes. You won't know what you are doing because no amount of tutorials can help here. We have all busted boards for various reasons. Just don't electrocute yourself on high voltage capacitor banks.

reply

eimrine
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

The only way of doing less mistakes with expencive boards is doing more mistakes with crap boards. Soldering literature suggests that a repair man should not do anything except repairing some electronics.

Probably your board has some uncleaned flux which makes some parasitic capacitance which make your board feel dead. Also expencive boards typically have some easy to break signalizers that someone not skilled was here. Visual control is a king.

reply

roland35
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

With the correct tools and materials soldering can be very easy or with the wrong tools very difficult!

There are probably some great videos on soldering on YouTube, luckily it's a mature field so not much has changed!Some random tips...Lead solder is easier to work with, but with lead free make sure you are using the right flux and temperature.It helps to preheat things as much as you can. You want to have a hot pad and hot lead, then add solder to that. As opposed to putting a blob of solder on the iron and trying to apply it like glue.Too much heat can damage the board or part of course.Use the right tips. Fatter tips can help more evenly apply heat.If there is a lot of copper like a ground plane, it can take longer to heat.Watch for cold joints!Just overall think about getting the parts you want solder on hot, touch solder to it, remove heat.Don't eat it!

reply

eternityforest
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

The important thing with lead free is you're not looking for the color or texture when inspecting, you're looking for the shape, and absence of any tiny seam or cracks.

It's probably not gonna be 100% shiny, that's fine, it just has to wet effectively instead of just kind of hovering in a blob.Lead free is the only thing I use unless I'm repairing some old pre rohs era thing I guess, but I generally don't encounter many of those.

reply

gizajob
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Get a job where you’re soldering all day, or doing audio repair or something like that. Embrace the fumes. Sloppily test live equipment. Remove and replace amplifier chips on amp boards 8 hours a day. Any company near you importing large amounts of audio or dj or stage equipment from China will need someone doing repairs and QC.

reply

foresto
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Avoid the Hakko FX-888D soldering station. This device has one of the most bizarrely obtuse interfaces I have encountered in ages, seemingly designed to make basic adjustments as difficult as possible, and to encourage accidental decalibration of its temperature settings with no indication to the user that it has happened. I wish I had returned mine while I had the chance.

reply

scarecrowbob
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'll also echo the "practice kit" thing, especially for desoldering- solder stuff on, take it off, do it agin.

Also, good tools and supplies- kester solder and liquid flux.It took me quite a while to figure out that my preferences are for desoldering braid that's been soaked with liquid flux- if I use a manual pump it's going to be rough. I am hoping to get a hot air station at some point but I haven't been doing enough work to justify it over my ancient hakko.

reply

zhrvoj
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

If you need to remove components with many pads, like connectors, it can be daunting without Low Temp Solder Wire. Chip Quik.
Btw, I use acetone for cleaning PCBA's, and actually almost every day, and right now, in a professional R&D lab. Residues of soldering wire, after SMT component removal, before new component gets in - it goes away with cotton bud soaked in ace in a few strokes. Never destroyed anything in my whole professional life, 35+ years now, working in consumer and industrial PCBA repair service. Isopropyl works of course, but slowly, and not so clean pcb stays. Depending on the type of soldering wire. I never use lead-free for repairs. 
During soldering though hole, you need few seconds to heat up the pcb copper and a component lead. They should be on on the same temp for second or two when solder gets melted around. You can even see pad hole capillary sucking melted solder. 
I've seen young people soldering THT, by shortly touching component pin and and a pcb pad. This looks baad.

reply

cottonseed
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Get a soldering practice kit. If you're doing surface mount, get a SMD one. For next level practice, checkout azonenberg's rework challenge: 
https://github.com/azonenberg/reworkctf
. He also has some YouTube video about it.

reply

Animats
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Right. Search "surface mount soldering practice kit". For about $4, you get a board and some parts to practice on. Get a few of those kits, and keep doing them until the result looks really good. I went through about three of those before I attempted anything real.

You really do need all those little tools, plus a good soldering station, and possibly a hot-air rework station. Get a smoke extractor fan. Learn to use lead-free solder with a small silver component. That gets the melting point down. Visit a place that repairs cell phones and see what they have.

reply

efortis
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Two tips I learned from Sorin's yt channel:

- Bend the tips- Don't buy an expensive iron, use a cheap one and assist it with a hot air gunSorin is incredibly skilled. Here he is fixing a ribbon cable:https://youtu.be/P81IG0DZ1kg?t=494

reply

throwaway81523
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/NASA%20St...

reply

lrasinen
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm going to put in a good word for the SN100C / Sn100+ / SnCuNiGe lead-free solder. It's been my go-to for the past 8 years or so, and it flows almost as nicely as leaded.

reply

bariumbitmap
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

If you live near a makerspace / hackerspace, I would definitely recommend doing projects there. Mine has a weekly electronics projects and repair night with free access. This has two main benefits:

1. Access to a bunch of different equipment without breaking the bank. Want to try out a bunch of different kinds of flux? See what kind of de-soldering tools are good for different tasks? Now you can!2. Access to expertise and moral support. Trying to do everything by yourself is no fun. A YouTube video can be helpful but it's no substitute for a knowledgeable friend or more experienced mentor.I recently did an RTC battery substitution on my Framework laptop's mainboard, and I could do it with confidence because I had good tools and people to consult at my makerspace.

reply

rlue
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Here’s a great series from Pace Electronics from 1980:

https://youtube.com/playlist?list=PL926EC0F1F93C1837&si=srD8...I have not found a modern resource that explains it better.

reply

severino
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

For me, as there are so many "variables" when soldering, the most difficult thing is knowing what's wrong.

For example, you end up with a poor soldering. You try again, and again, but it doesn't get better. Maybe only worse. But what was wrong?- Was the temperature OK? (And is my iron reporting the real temperature? Should I spend another 300 bucks in a soldering tip thermometer?)- Maybe the solder I bought is not appropriate?- Was it the flux? Did I apply it correctly?- Also, is this tip the best one for the job? Besides, I could have damaged it before when trying to solder and it's not good anymore, although looks good to me- Or my technique isn't good enough. Am I drag soldering this right? Maybe I should apply heat for longer? But what if I damage the component?

reply

amelius
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

The main insight you need to have:

The things you want to solder need to be at a minimum temperature for the solder to properly flow.Parts with a lot of metal attached to it will need more time to get hot. Most notorious are pads connected to a large (ground) plane.If the solder does not flow properly because of this, increase the time of contact between your soldering iron and the items, add a small amount of solder to the tip to increase contact area. Or use a heat gun in your other hand or a preheater. Or buy a soldering iron with more power.Flux will help too.Use a fan to draw the fumes away from you, at a minimum. If you do this on a daily basis, get a fume extractor.There are many more tips on the internet. The first thing I mentioned is the most important one, imho.

reply

half_fish
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

This gives me flashbacks to the last time I tried to replace the microswitches in my mouse...

After I finished, the right click felt like it was 'glued down' or 'stuck'...I never heard the click sound again...Yep, it was broken.I've decided never to solder anything ever again...But good luck to you!

reply

readme
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

you attempted a skilled technique without practice, you were surprised when you screwed it up, and then you quit

this is not a good pattern!

reply

sssilver
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Arguably, the only resource you need to get better at it, is time.

Every next solder makes you better at soldering.Get through your first 1000 solders as soon as possible, and then keep going. The rest will figure itself out along the way.

reply

axegon_
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I picked up the skill from my granddad when I was a kid. Yeah, 6 year old with a soldering iron, what could go wrong, right? Welcome to eastern Europe. There are really 2 things: good soldering iron(and soldering helping hands kit) and practice. Which takes me to one of my hobbies: drones. Look up a kit called Diatone Mamba soldering practice board. They cost 2-3 bucks, get 10 and you'll get the hang of it in a few hours. Oh and a fume extractor(any old pc fan will do).

reply

lloydatkinson
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Just solder?

reply

bigbuppo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

The only way to learn is to do the damn thing. You'll eventually figure it out. Tinker around with projects that don't matter but are still rewarding. Like, commit a 555 timer and blinky LEDs to proto board. Then find some kits on tindie that seem interesting but won't break the bank. Wash, rinse, repeat until you're building your own multiprocessor homebrew 6502 computer.

reply

winrid
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I highly recommend a 
desoldering gun
, like a Hakko, absolutely life changing if you take stuff apart or repair often.

Also, flux is your friend.

reply

radicalbyte
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

You can buy a whole lot of practise kits on Amazon. Start with push-through components and move on to surface-mount if you fancy that.

I'd recommend checking out one of the many youtube channels who do repairs for an idea of the tools and stuff you need. Many have links and most use similar tools.For $300 in tools from AliExpress you can have a pretty complete setup.

reply

jrflo
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

FYI you're trying to repair surface-mounted components by hand, that's pretty tricky. Most hand soldering is done with through hole components, not surface mounted. Not to say it can't be done, but you're starting on hard mode for sure.

reply

readme
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I've taught people to start with surface mount before. It's really worse depending on what you're soldering. A lot of people doing hardware hacking will get tons of mileage just out of being able to solder on a chip with a soic-8 package. That's easy enough that you can learn it on day 1.

reply

anotherhue
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

This guy's youtube videos are, IMO, incredible: 
https://www.youtube.com/channel/UCw4EJfQf0KJXCyQ5qiNlcUg/vid...

reply

zachlatta
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

For teens ages 13-18, Hack Club is running a free grant program to help kids learn to solder! They can sign up and get a free kit from us at 
https://solder.hackclub.com/

reply

neom
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

This guy does a lot of videos about what you're trying to do, and explains what he is doing and why: 
https://www.youtube.com/@JoeyDoesTech

reply

mcshicks
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

This set of videos from eevblog worked for me.

https://m.youtube.com/watch?v=J5Sb21qbpEQ

reply

tosmatos
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Thanks for the tips everyone, I'm motivated now !

reply

sscaryterry
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Don't overthink it, seriously. Avoid the fumes, if the joint looks shiny, its 
probably
 cool.

reply

nprateem
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

You could read books on strategy from military campaigns, the Art of War, etc, but if you want to be a good solder the best thing would be to join your local territorial army group.

reply

aerodexis
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Are you one of those openAI swarms that got into the wild?

reply

sciencesama
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

know that unleaded solder needs higher temps to melt and heat both the joint and the plate a little to have a good fix !

reply

tootie
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I took a local class that really helped but the lesson was really just a basic project that had like 40 solder points. First few barely stuck, last few looked perfect. Just do it over and over and you'll get better pretty quickly.

reply

timonoko
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Flux like Rossmann

reply

rzzzt
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

1 milli-Paul of flux. (Or am I mixing things up with Paul Daniels of boardview software fame?)

reply

hiddencost
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Is there a local makerspace? They often will have free nights where you can pick up some knowledge with direct supervision. Having someone else watch you is incredibly helpful.

reply

atoav
 
17 hours ago
 
 | 
prev
 
[–]

The variables aren't that hard to learn. The one thing many beginners struggle with is that they don't really get the principles involved. They treat a soldering iron as some sort of heated paint brush and wonder why they can't get the paint off the brush.

In reality there are multiple factors at play, but a simple and useful abstraction is to think about solder as something that flows more easily to places that are hot. That means the solder always likes to go onto the iron, since that is likely the hottest thing around.This means your first goal is simply to heat up the places you want to solder far enough sotheycan melt the solder if you touch them with the solder wire¹.This usually means heating two things at once: be it two wires you solder together or a pad and the leg of a resistor. That means knowing the geometry of your tip well is useful: How to wedge it in to heat the two things at once. Typically only the shiny, plated bits of the tip are really good at conducting heat². A little drop of solder on the iron can help conduct the heat to a bigger surface, a bit like the fat in a frying pan.But generally you heat the parts with the iron and then you feed the solder wire into the parts. If they are hot e ough, the solder melts. If not, you wait.The solder wire typically has a resin-like fluid inside, that helps with soldering as it reduces the surface tension of the metal (this is most of the stuff in the fumes). Capillary effect is the main thing that makes solder flow where you want it to. When the flux is evaporated soldering gets harder, so you may need to add fresh solder after a while or you use flux from a dispenser that you add manually.³Then there is a lot about logistics. Heated air travels up, on earth solder tends to be affected by gravity and has a tendency to go down (although capillary effects arereallythe dominant force here), gravity affects parts, wires bend where their material wanta them to etc. The logistics part means: you have only two hands, an iron, solder wire and typically two or more parts that need to be joined.Being good at soldering is (1) having a good mental model and intuition about how and why the solder flows the way it does and (2) have skill and experience to get the logistics right. The first you can learn to understand, the latter is a matter of practise.⁴I have thought soldering sucessfully to well over 400 people during the past decade.¹ This means your iron and tip need to be able to deliver enough heat to heat the parts. If you try to heat up a 200W copper CPU cooler with a 14W soldering iron you can wait forever for the solder to melt. This also has to do with thermal mass and regulation of the iron. Modern irons with modern tips have the temperature probe inside the tip. This helps a ton with avoiding temperature dips when you start to touch something and makes soldering much easier.² This means keeping tips clean with a proper cleaner literally before every solder joint is crucial. If your tip is toast and has no shiny bit anymore, clean it. If that doesn't help use Ersa Solder Tip Reactivator or buy a new tip. Of course your parts should also be clean (Isopropanol)³ There are ways to remove excess solder. The simplest being using the right motion with the tip on a coldish joint, making the excess solder stick to the iron and not to the (colder) joint. Other things are spring loaded suction devices (very useful to get solder out of through holes!) and solder wick (very useful to clean old pads)⁴ There a tools like third hands and so on, and watching some videos by experienced solderers is a good way (nowadays) to learn it, but a steady hand only comes with practise

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