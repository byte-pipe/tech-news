---
title: Apple’s Thinnest iPhone Still Stands Up to Repairs - iFixit
url: https://www.ifixit.com/News/113171/iphone-air-teardown
site_name: hackernews_api
fetched_at: '2025-09-21T19:05:49.730830'
original_url: https://www.ifixit.com/News/113171/iphone-air-teardown
author: zdw
date: '2025-09-21'
description: To be honest, we were holding our breath for the iPhone Air. Thinner usually means flimsier, harder to fix, and more glued-down parts. But the iPhone Air proves…
tags:
- hackernews
- trending
---

To be honest, we were holding our breath for the iPhone Air. Thinner usually means flimsier, harder to fix, and more glued-down parts. But the iPhone Air proves otherwise. Apple has somehow built its thinnest iPhone ever without tanking repairability.

Just a few months ago, Samsung’sGalaxy S25 Edge pulled off a similar trickin an ultra-thin package. How’d they do it? And how’d Apple follow suit?

The secret: Thinner can actually bemorerepairable, with clever design.

A thin phone party! From left to right: Samsung Galaxy S25 Edge: 5.8 mm, iPhone Air: 5.64 mm, and Moto Z (the OG thin smartphone): 5.2 mm.

## Clever Use of Space

Apple made one huge design shift in the Air, which they teased in their keynote and we confirmed with ourLumafield Neptune CT scanner: The middle of this phone is basically just a battery with a frame around it. Apple popped the logic board up above the battery, a large part of how their design got thinner without compromising repair.

When we score repairability,80% of our scoreis determined by the ease of replacing the parts that are most important and most likely to break. To figure this out, we build a model of the repair process. What’s the path you have to take to get to the battery, or to the screen? We call this the “disassembly tree.” The ideal (if unlikely) disassembly tree is flat. No parts in the way of other parts.

A linear disassembly tree on the left. A flat disassembly tree on the right. Every time you’ve got to go through another component, you risk damaging it, and repairs take more time.

A thin device often means, advantageously, a flat disassembly tree. Stacked parts are thicker than parts side-by-side. Ourfriends over at Frameworkhave been saying this for a long time: It’s totally possible to make a thin and light device that’s also built for repair. The Framework Laptop has done this from the start, with nearly all major components accessible when you remove the cover.

And that’s exactly what we’re seeing in the Air. The logic board shift freed up room for the battery and helped the phone stay thin without cramming parts on top of each other. It also conveniently puts less stress on the board if the phone flexes in your pocket. It’s a smart workaround forthe “bendgate” problemsthat haunted earlier slim iPhone designs. Not that the Air’s really going to be bending much,as Zack’s test at Jerry Rig Everything suggests.

(By the way, did you see we’re teaming up with Zack to bring you a toolkit that’s made for on-the-go repairsanddurability testing?)

### Level up your toolbox

## Pro Tech Toolkit

Stop wasting your time frantically searching for the right tool. With our Pro Tech Toolkit you’re ready for any electronic or hardware repair that comes your way!

£64.99On Sale

£64.99

Shop Now

The Air trims a few extras compared to the Plus line it succeeds, losing the lower speaker and a rear camera. Like the 16e, it’s got just a single rear camera.

Inside, though, it packs the upgraded C1X modem, a new N1 WiFi chip, and the A19 Pro system-on-chip, all tucked into the logic board sandwich. It’s a lean, efficient setup that makes the most of limited space. This reduced complexity also contributes to quicker disassembly—fewer features, fewer parts,andfewer points of failure.

Here’s looking at you, camera (through the lens of the back glass).

## Battery Life? Eh. Battery Swaps? No Big Deal

There’s been a lot of buzz about battery life on this phone. Apple said “all-day battery life,” and tech reviewers of the world,noting the lack of watt-hour specificityand immediate announcement of an add-on battery pack, said, “really now?” At 12.26 Wh, this battery is certainly smaller than recent iPhones (closest comparison being the 13 Pro’s 11.97 Wh), and that raises questions about longevity. More charging cycles usually means faster wear. Still, Apple’s efficiency tricks give it solid runtime, at least for now.

But no battery lasts forever, so how difficult will swaps be? We’re relieved to see that the Air has all the greatest hits of the last few iPhone battery designs.

The Air’s battery is easy to findandaccessible through the back glass thanks to Apple’s dual entry design. Even better, it’s a metal-encased battery. This thin layer of armor makes it more bend resistant and safer to replace. Even better thanthat, it’s mounted with electrically debonding adhesive strips. Hook them up to a power source and the battery lifts right out, no dangerous prying required. We used our FixHub Portable Power Station for an easy 12 V, and each strip freed after about 70 seconds.

Even though it’s comparably a small battery, its heft accounts for 28% of the phone’s total weight, more than any other component.

And in a fun twist, we’ve confirmed that it’s theexact same cell found in Apple’s MagSafe battery pack. You can swap between them and the phone still boots up just fine. Like a rear-mounted spare tire on an SUV, an iPhone Air with a MagSafe battery pack is ready for an on-the-go swap, if you will. Granted it’ll take abitmore than a tire iron to make it happen.

Here’s our iPhone Air running off a MagSafe battery. (They’re so similar that we labeled the original so we wouldn’t mix them up!)

## Modular Port, but How About Parts to Back It Up?

How about other likely-to-fail parts? USB-C ports are among the most common failure points in modern phones. Ports tend to collect moisture,which can cause corrosion, and no one is immune to pocket lint. Not to mention the standardport problemscaused by mechanical wear and tear.

Now, to be clear, if your phone stops charging consistently, you shouldn’t jump straight to replacing the port. Every time you stick a charge cable into the port, you’re jamming pocket lint against the back.Give your charge port a cleanoutbefore you replace it.

Featured Guide

### How to Clean the Ports on your Electronic Device

Use this guide to clean the ports on your…

Follow this Guide

But when youdoneed to replace an Air charging port, you’ll be glad to know it’s decently modular, following the trend of the last few iPhone models. It’s a tedious process, with delicate flex cables, adhesive, and hard-to-reach screws, but it’s still feasible.

Interestingly, the modularity of the USB-C port doesn’t seem to be a serviceability choice. Apple won’t do USB-C repairs in-house and they don’t sell replacement ports for iPhones. Of course that won’t stop us fromselling the partsas soon as we can get them—and regardless of intent, this modularity is nice to have.

Third-party parts manufacturers may take a bit to catch up, since this is a brand new architecture for the housing of the USB port. Applereportedly used 3D printingto shrink the housing to fit the slim frame of the 6.5mm iPhone Air.

Apple says this processreduced material usage by 33%compared to conventional forging processes. Granted, the USB-C port isalreadytiny. But this isn’t the only place they’re using it: TheApple Watch Ultra 3uses the same titanium-printing process in its case.

We took a close look at the titanium material in the USB-C port, with ourEvident DSX2000 microscope.

Here’s what we put under the microscope: a chunk of the bottom frame of the phone, after it snapped in our frame-only bend test. The USB port housing is bottom center.

What we saw was fascinating: these regular bubble-like structures.

We tapped in some friends in the additive manufacturing industry, who said it wasn’tquitelike any metal 3D printing they’d seen before. Their best guess is that Apple’s using a binder or aerosol jet process in addition to some after-printing machining. This aligns with abinder jetting patent Apple inherited back in 2015when they acquired Metaio. Whatever the exact process, the result is some truly impressive titanium manipulation.

(If you’re a metal 3D printing expert and want to give us your thoughts in the comments, we’d love to hear from you!)

## How Strong Is Thin?

Titanium may have retired from the rest of the iPhone line (possibly forgeopolitical more than technical reasons) but it’s back as the backbone of this slim smartphone. This tough metal is a good choice, but it’s only as strong as its weak points. Our empty-frame bend test snapped the Air at its plastic antenna passthroughs—a necessity if you want your phone to phone properly. CT scans make it clear: Apple reinforced the center section, but the top and bottom remain vulnerable.

If you take off the screen and remove the internal components, it’s possible to break this phone by hand. Makes for a great photo op! But chances are it won’t do that in regular use.

Of course, the center is where the phone is most likely to bend, and so far testing hasn’t given any indication of undue flexibility. Will that design affect the durability of the phone? We doubt we’ll see instances of Airs snapping at the ends, but only time will tell.

## The Verdict: A 7 out of 10 Repairability Score

At 6.5 mm, the Air is a hair thinner than Samsung’s Galaxy S25 Edge, yet it manages to keep modular parts and early battery access. Apple’s dual entry design makes battery swaps simple and keeps the fancy OLED out of harm’s way. Electrically debonding adhesive makes battery replacements a lot more consistent than traditional or stretch-release adhesive, and most other major components are simple to access and remove. Apple also kept their best-in-class clipped- and screwed-in screen and back glass architecture, enabling quick reassembly without requiring special adhesive.

Combined with Apple’s continued commitment to day-one repair manuals, the iPhone Air earns aprovisional7 out of 10 repairability score. (We’re waiting on Apple to make good on their parts availability commitment as well as final results on our parts pairing tests. Their recent track record’s pretty good, though.)

Apple has proved that thin doesn’t have to mean unfixable. The iPhone Air is slimmer than any iPhone before it, but its layout and design tradeoffs make repairsmoreapproachable, not less. It still has limits, but the design shows that good engineering can make even the slimmest devices last longer in the real world. Successful field test for your new foldable, Apple. We’re onto you!

More Apple 2025 lineup teardowns coming soon. Bonus round:Can TechWoven handle… hot sauce?
