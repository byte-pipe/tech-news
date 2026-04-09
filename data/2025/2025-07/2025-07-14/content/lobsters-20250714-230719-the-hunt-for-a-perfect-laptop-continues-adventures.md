---
title: The hunt for a perfect laptop continues – Adventures in Linux and KDE
url: https://pointieststick.com/2025/07/13/the-hunt-for-a-perfect-laptop-continues/
site_name: lobsters
fetched_at: '2025-07-14T23:07:19.612355'
original_url: https://pointieststick.com/2025/07/13/the-hunt-for-a-perfect-laptop-continues/
date: '2025-07-14'
published_date: '2025-07-14T00:33:18+00:00'
description: This is a bit of a rant; feel free to skip it if you're here for the KDE content. This isn't the first time I've blogged about the dearth of truly great PC laptops out there, and I suspect it won't be the last. I limit myself to a single computer for simplicity's sake, so…
tags: hardware
---

Nate


Linux Hardware


July 13, 2025
July 14, 2025


6 Minutes


This is a bit of a rant; feel free to skip it if you’re here for the KDE content.

This isn’t the first time I’ve blogged about the dearth of truly great PC laptops out there, and I suspect it won’t be the last.

I limit myself to a single computer for simplicity’s sake, so it has to be a laptop. And since I replaced my2020 Lenovo ThinkPad X1 Yogaa year ago, I haven’t succeeded at finding a truly great replacement yet. From a certain point of view, you could say I’m a picky buyer, judging by mylist of requirements. But frankly, I think these requirements are not that unreasonable. All I want is a laptop that gets the basics right:

* Good screen with a DPI suitable for 175-200% scaling, generally between 240 and 280 DPI
* Good keyboard with text navigation keys (Home, End, Page Up, and Page Down) and a sensible layout: delete at the top right, no stupid replacement of normal modifier keys with fingerprint readers or copilot keys, no tiny arrow keys, etc.
* Good touchpad that’s precise, doesn’t lag, and allows clicking on most or all of the total area
* Good speakers that get reasonably loud and don’t have downward-facing tweeters
* 8 hours of battery life with low usage
* Reasonably fast CPU
* Reasonable GPU performance for desktop compositing and playing couple-year-old games
* Replaceable disk

Just the basics; no great world-shattering innovation needed, and that’s before I narrow the search to laptops that lack NVIDIA GPUs and have touch or 2-in-1 capabilities (which I quite like and are highly useful for testing touch support in KDE software). So it has to have great Linux and Plasma compatibility too!

I’ve closely followed the PC laptop market for 9 years, maintaining a giant spreadsheet of every laptop model and how they fare on the above characteristics plus many more:

The multi-year trend is “one step forward, one step back.” Most companies still change their laptops’ keyboard layouts in random negative ways every year; ship with stupid screen resolutions, woefully bad speakers, and disappointing touchpads; and stuff the most powerful processor and GPU in there and don’t focus enough on tuning the cooling, power usage, and fan profiles.

Some examples from my own usage:

My 2016 HP Spectre x360 was slow and had a poor screen DPI and a laggy touchpad. The 2024 model fixed those problems but lost its HDMI ports and text nav keys, and the USB-A port has a fiddly and annoying little hinge that’s hard to use and will eventually break. And then the 14″ version was canceled in 2025.

My 2020 Lenovo ThinkPad X1 Yoga was also slow, had miserable battery life and a loud fan, put the Fn and PrintScreen keys in inconvenient places, and its high resolution 4K screen option hadtoohigh a DPI, wasting energy. The 2025 model fixed those issues but lost the excellent quad speaker system, garaged pen, and the third key to the right of the spacebar that let you re-bind one of them into being a second Meta key.

None of this would be a problem if you could customize and upgrade laptops like you can with desktops, but you can’t. Even on theFramework 13 laptopwhich makes this an explicit selling point and has made huge leaps in 4 years, there still aren’t aftermarket speaker modules that sound good or a keyboard deck with text nav keys. And the touch/2-in-1 capabilities are only offered on the 12″ model.

## Where are the great laptops?

Let’s step back a bit and try to figure out what’s going on here. We have an industry of over a dozen PC manufacturers selling thousands of products, but few truly great ones that are satisfactory inallways, not just a few.

I feel that a major problem is over-complicated product lines. Let’s look at what the big companies offer.

Here’sLenovo:

Seven product lines (or is it eight; there’s an extra one in the sidebar not shown in the main view) and 330 distinct models! How can a normal person who isn’t a laptop enthusiast find anything in here? Even my eyes glaze over when I’m trying to distinguish the differences between the models and product lines.

HP further complicates things by having separate sites for consumer laptops and business laptops. First theconsumerlaptops:

12 product lines with 67 models. Already a lot. But now add in thebusiness laptops:

7 product lines with 352 models! Absurd. HP implicitly acknowledges the problem by advertising a sales advisor you can chat with to help you make heads or tails of this overwhelming mess (and maybe steer you towards more expensive models):

In total, HP offers19 product lines and 419 models. Madness, I tell you. Sheer madness.

ASUS makes it even harder by dividing their models into micro-targeted audiences, which makes no sense since there’s overlap in all these use cases and only limited differences between what any of them need in a laptop:

Ultimately I found 8 product lines with 289 models on the US site. Yikes!

MSI does similar segmentation but finds a way to make it even worse by putting more models in each high level category and not offering a “See all” page:

Hmm, do I want a Titan gaming laptop, or a Raider? Maybe a Vector ? Perhaps a Cyborg, or is that a Thin? Apparently they can’t even settle on one name for half of them. Ultimately MSI has divided their laptops into no fewer than 16 product lines with 159 models.

How aboutDell?

10 product lines, 70 models. A bit better than some of the competition, but 70 total is still an objectively ridiculous level of choice to offer, especially considering that most of these models are going to offer various configurations of CPUs, memory, and storage space.

I could go on, but you get the idea.

You might think that this level of choice should provide anything one could want, but that’s not true. Most of the models differ by like 1% and make all the same mistakes, copy-pasted across the while product line. Maintaining so many product lines at a reasonable level of development and quality is impossible, even for companies of their size with billions of dollars to throw at the problem.

These companies are clearly trying to micro-target specific market segments to match prices to buyers’ budgets, but offering so much choice is foolish. Most buyers — even big commercial buyers — are not informed enough to be able to pick the perfect device from among a massive blob of options presented at the same level, causing choice paralysis and lost sales, disappointing purchases that reduce brand loyalty, and expensive returns.

There has to be a better way!

## Who’s doing it right?

There are some bright spots in the industry.

The most notable isApple, which offers two product lines and five total models. The differences between them are 100% comprehensible. No matter what Apple laptop you choose, it has a world-class touchpad, great speakers, an at-least-good keyboard with a sensible layout, a nice high DPI screen, great performance, and mind-blowing battery life. There are no bad models (if you’re a Mac fan, of course).

Razeris up there too, with one product line and three models, and all of themmostlyget the basics right.

Frameworkalso does a great job, also with just three models. The Framework 13 issoclose to being the perfect do-it-all general purpose device for me. It just needs text nav keys, better speakers, and a touchscreen (ideally in a 2-in-1 form factor like the 12).

The small Linux-specificStarLabscompany does an unexpectedly great job too, with the same three models (hmm, perhapsthere’s a pattern here). And these aren’t Clevo or Tongfang units, either! They’re really nice custom engineered Linux-first laptops. I’ve come close to buying one on two occasions within the past year.

And notably, these companies’ laptops tend to get better with each revision, rather than oscillating around a specific level of quality but never consistently improving.

## How to not confuse the hell out of people

It’s not that hard: offer a small number of product lines and models with very clear segmentation (by screen size, presence or absence of a GPU, 2-in-1 vs clamshell laptop, etc) and make all of them good.Don’t sell any bad modelsthat have crappy screens, keyboards, touchpads, speakers, or battery life. Don’t sell any models that are 99% identical to other ones. Don’t do this:

No, don’t do this! Stop it! You’re hurting me!

Then make each product better every year. Don’t just put in a new generation of CPUs and ports when they become available; be thoughtful and actually make things better. Reduce power consumption, fan noise, and heat emissions. Tune the speakers to sound better. Increase the screen backlight’s brightness. Put in a nicer, higher-resolution webcam. Increase the number of microphones, and add hardware noise cancellation. Tighten up the ports so they aren’t wobbly. Thicken the case to make it more durable. Beef up the hinges. Use captive screws for the bottom cover. Lighten or roughen the surface a bit to resist fingerprints. Make it easier to remove keys for cleaning without breaking their attachment mechanism. Make the whole keyboard replaceable.

And so on. You know,care about the product!The way we do in KDE for Plasma and our apps. Make it better. Admit and undo your mistakes. Double down on your strengths. And make something great you can be proud of!

A few companies are already there, and I hope someday more follow in their footsteps.

Like

Loading...

### Related





## Published byNate

View all posts by Nate

Published

July 13, 2025
July 14, 2025
