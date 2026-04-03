---
title: 15 Years of Forking - Waterfox Blog
url: https://www.waterfox.com/blog/15-years-of-forking/
site_name: hackernews_api
content_file: hackernews_api-15-years-of-forking-waterfox-blog
fetched_at: '2026-03-30T19:26:26.739409'
original_url: https://www.waterfox.com/blog/15-years-of-forking/
author: MrAlex94
date: '2026-03-27'
description: Today marks 15 years of Waterfox!
tags:
- hackernews
- trending
---

←
 
 
 
→
 
 
 
 
 
 
 
 
 2011-2014 
 
 
 
 
 
 

2011-2014

 

The first Waterfox identity

 
 
 
 
 
 
 2014-2015 
 
 
 
 
 
 

2014-2015

 

A short lived transitional logo phase

 
 
 
 
 
 
 2015-2019 
 
 
 
 
 
 

2015-2019

 

A slicker, more modern logo

 
 
 
 
 
 
 2019 
 
 
 
 
 
 

2019

 

First redesign due to pressure from Mozilla

 
 
 
 
 
 
 2019-2023 
 
 
 
 
 
 

2019-2023

 

A logo Mozilla are happy with, after many threats

 
 
 
 
 
 
 Today 
 
 
 
 
 
 

Today

 

Current identity, smoother gradients for easier editing

 
 
 
 
 
 
 
 
Logo 2011-2014
 
 
Logo 2014-2015
 
 
Logo 2015-2019
 
 
Logo 2019
 
 
Logo 2019-2023
 
 
Logo Today
 
 
 
 
 

Fifteen years ago today, I posteda thread on the Overclock.net forums. I was sixteen, I had an HP Compaq TC4400 that I’d convinced my parents would “improve my school work”, and I was frustrated that Firefox didn’t have an official 64-bit build. So I compiled one myself, called it Waterfox, stuck it on SourceForge and went back to my A levels.

Within a week it had 50,000 downloads, completely unexpected. Frustratingly, being on an island in the Mediterranean meant there was no support network or anyone to turn to with regards to “what’s next”. Had I been stateside, with the infrastructure and institutional knowledge of “tech”, who knows - I might’ve had a guiding hand on how to manage something like this and work with the momentum. But alas, I would have to learn a lot of painful lessons myself.

Fast forward to today, 15 years later, and Waterfox is still here. So am I, albeit a bit older and significantly more tired. At best estimates, Waterfox probably has around 1M monthly active users.

## Where it started

If you go and look at thatoriginal OCN thread, it’s a very different world. People are talking about Silverlight support, MSVCR100.dll errors, and Peacekeeper benchmark scores. Someone asks for a 64-bit Chromium build and the thread title gets updated with every new Firefox version, all the way up to 56.0.2.

Originally, and under the username MrAlex, I was only trying to earn enough forum reputation so I could trade and buy second hand PC parts. I didn’t have a plan and I certainly didn’t have a business model. I just thought it was cool that you could take someone else’s source code, compile it with some changes, and end up with something different. Open source is a wonderful thing when you’re sixteen and don’t know anything about the software development lifecycle, yearning forthe minesknowledge.

## What happened in between

You can scour the internet, read this blog or view the media carousel at the bottom for then until now, but the short version: Waterfox grew - a lot - over 25 million lifetime downloads, and that figure is from calculations about seven years ago so the real number is certainly higher. I went to university, studying Electronics Engineering at York before a masters in Software Engineering at Oxford. I tried to start a charitable search engine, which failed as badly run startups tend to do. Ecosia reached out and something nice happened - Waterfox users helped plant over 350,000 trees in a single year.

Then System1 came along. I joined them, served as VP of Engineering, and helped scale the browser engineering team through a NYSE IPO - a genuine education, though companies change and focus shifts.

So I took Waterfox back under BrowserWorks, independent once again. The three years since have been simultaneously the most difficult and the most rewarding of Waterfox’s existence.

## The hard bit

I’m not going to pretend the economics of running a privacy focused independent browser are great, because they’re really not. When Bing terminated all third party search contracts it hit hard - search partnerships are basically how independent browsers survive, and revenue has been poor since. There have been a few months in the red recently.

Other ways browsers make money just feel icky, and it’s not something that Waterfox stands for either.

But, pain and all, I keep coming back. Every time I think about stepping away, someone sends a kind message through the donation page, or I see a thread somewhere of someone discovering Waterfox for the first time and being pleasantly surprised. There’s a community here that cares, and I care about it.

I want users to know that whatever future steps I’ll take, they’ll always be with Waterfox and its sustainability in mind.

## What Waterfox is in 2026

This year will see Waterfox shipping a native content blocker built onBrave’s adblocklibrary - and it’s worth explaining what that means and why.

The blocker runs in the main browser process rather than as a web extension, which means it isn’t subject to the limitations that extension based blockers like uBlock Origin face. It’s faster, more tightly integrated, and doesn’t depend on a separate extension process or require us to constantly pull in upstream updates. Brave’s adblock library is also mature - it has paid engineers working on it, a wide filterset, and crucially it’s licensed under MPL2, the same licence as Waterfox, which makes it a natural fit. uBlock Origin, as good as it is, carries a GPLv3 licence that would’ve created real compatibility headaches.

For how it works in practice: by default, text ads will remain visible on our default search partner’s page - currently Startpage. The idea is that this is what will keep the lights on.This mirrors the approach Brave takes with their search partner.

 
 
 
 
 

Info

 
 

Update (28 March 2026):Corrected a statement about Brave’s ad blocking behaviour. The original text implied Brave special cases ads on their search partner’s page - they don’t. Brave blocksthird partyads on all websites by default, regardless of any partnership, and offers an additional aggressive mode that blocksfirst partyads as well. Waterfox’s approach of allowing text ads on the default search partner page is our own decision for sustainability, not something inherited fromadblock-rs. Thanks to Shivan at Brave for the correction.

 

Users who want to disable that entirely can do so with a single toggle in settings, and it has nothing to do with any of Brave’s crypto or rewards ecosystem - we’re just using the adblocking library. Everyone else gets a fast, native adblocker out of the box, no extension required.

If you already use an adblocker, don’t worry, you can carry on using it. This will be enabled for new users or users who aren’t already using an adblocker.

In the meanwhile, Waterfox’s membership of the Browser Choice Alliance alongside Google and Opera, is pushing for fair competition and actual user choice in the browser market.

And we still don’t have AI in the browser.That hasn’t changed. The browser’s job is to load web pages, keep your data private, and get out of the way. It seems other browsers have forgotten that.

Oh and one last thing - distribution is important too, so there’s a bigger focus on different packages and architecture support (Linux, you are such a pain to target) - more specifically for ARM64.

## Fifteen more?

I’d like to think so. The browser market is more diverse than it’s ever been in terms of soft forks - everyone and their mum seems to be launching a variation of Firefox. Running an independent browser is getting harder, not easier. But there are more people who care about privacy now than there were when I was compiling a blue Firefox on a tablet PC in my bedroom. More people who want software that respects them.

Waterfox started because a sixteen year old wanted a faster browser. Fifteen years later, it’s still here because enough people want a browser that works for them - not for AI companies, and not for anyone else.

Thanks to everyone who’s been part of this - from the OCN community who gave those early builds a chance, to the people who send donations with messages that make my day, to the contributors who submit patches and file bugs. This project has always been bigger than me, even when I’m the only one working on it.

Here’s to the next 15! 🍻

## A Special Shout Out

I also wouldn’t be where I am with the constant moral support of my parents, Angela & Lakis, who since day dot have been proud of everything I’ve done, even if it’s felt like I was failing and flailing. My friends, numerous to count, but especially Lee who I’m surprised hasn’t once told me to shut up about my trials and tribulations. And finally, my wonderful girlfriend and partnerLucywho has been giving helpful design tips because while I have wonderful taste (only half joking) my creative talent is unfortunately lacking.

## Waterfox in the Media

Read the media coverage Waterfox has received over the last 15 years.

 
 
 
 
 
←
 
 
 
→
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 PCWorld 
 
 2011 
 
 
 
 
 Feature 
 

### Use a 64-Bit PC? Instead of Firefox, Try Waterfox 9.0

 
 
 
 PCWorld · 2011 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 BetaNews 
 
 2011 
 
 
 
 
 Review 
 

### Can't wait for Firefox 64-bit? Try Waterfox 8

 
 
 
 BetaNews · 2011 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Softpedia 
 
 2014 
 
 
 
 
 Review 
 

### Waterfox 28 Review - A 64-Bit Version of Firefox

 
 
 
 Softpedia · 2014 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 The Telegraph 
 
 2015 
 
 
 
 
 Feature 
 

### New search engine from Waterfox founder aims to take a punch at Google

 
 
 
 The Telegraph · 2015 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Trusted Reviews 
 
 2015 
 
 
 
 
 Interview 
 

### From bedroom coder to building a Google search engine rival

 
 
 
 Trusted Reviews · 2015 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 GIGAZINE 
 
 2015 
 
 
 
 
 Review 
 

### The fastest 64-bit web browser "Waterfox"

 
 
 
 GIGAZINE · 2015 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2017 
 
 
 
 
 Feature 
 

### Waterfox dev has big plans for the browser

 
 
 
 Ghacks Tech News · 2017 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Dedoimedo 
 
 2017 
 
 
 
 
 Review 
 

### The Fox Hunt — Firefox and friends compared

 
 
 
 Dedoimedo · 2017 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2017 
 
 
 
 
 News 
 

### Waterfox 56 is out

 
 
 
 Ghacks Tech News · 2017 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2018 
 
 
 
 
 News 
 

### Waterfox for Android update brings huge privacy improvements

 
 
 
 Ghacks Tech News · 2018 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 HostingAdvice 
 
 2019 
 
 
 
 
 Interview 
 

### The Open-Source Waterfox Browser Delivers a Balance of Privacy and Usability

 
 
 
 HostingAdvice · 2019 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2019 
 
 
 
 
 News 
 

### Waterfox development splits into Classic and Current branches

 
 
 
 Ghacks Tech News · 2019 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 It's FOSS 
 
 2019 
 
 
 
 
 Review 
 

### Waterfox Browser: Firefox Fork With Legacy Add-ons Options

 
 
 
 It's FOSS · 2019 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Slashdot 
 
 2020 
 
 
 
 
 News 
 

### Alternative Browser 'Waterfox' Acquired By System1

 
 
 
 Slashdot · 2020 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 The Register 
 
 2021 
 
 
 
 
 Feature 
 

### Waterfox: A Firefox fork that could teach Mozilla a lesson

 
 
 
 The Register · 2021 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 MakeUseOf 
 
 2022 
 
 
 
 
 Review 
 

### What Is Waterfox and Is It Safe?

 
 
 
 MakeUseOf · 2022 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2023 
 
 
 
 
 News 
 

### Waterfox Browser cuts ties with System 1 to celebrate independence

 
 
 
 Ghacks Tech News · 2023 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 MSPowerUser 
 
 2023 
 
 
 
 
 News 
 

### Firefox fork Waterfox is now available for Android with strict privacy defaults

 
 
 
 MSPowerUser · 2023 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 XDA Developers 
 
 2024 
 
 
 
 
 Review 
 

### I ditched Firefox for this privacy-focused spinoff with better features

 
 
 
 XDA Developers · 2024 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Pocket-lint 
 
 2024 
 
 
 
 
 Feature 
 

### It's possible to browse better with Waterfox, but I wish I'd known this first

 
 
 
 Pocket-lint · 2024 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Ghacks Tech News 
 
 2024 
 
 
 
 
 News 
 

### Chrome, Opera, Vivaldi, Waterfox and Wavebox join hands to fight against Microsoft Edge

 
 
 
 Ghacks Tech News · 2024 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 TechRadar 
 
 2024 
 
 
 
 
 News 
 

### Microsoft Edge gets 'unfair advantage', browser makers claim

 
 
 
 TechRadar · 2024 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 The Register 
 
 2025 
 
 
 
 
 Feature 
 

### Waterfox browser goes AI-free, targets the Firefox faithful

 
 
 
 The Register · 2025 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 heise online 
 
 2025 
 
 
 
 
 Feature 
 

### Waterfox positions itself as an AI-free Firefox alternative

 
 
 
 heise online · 2025 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 WebProNews 
 
 2025 
 
 
 
 
 Feature 
 

### Waterfox Opposes Mozilla's AI Integration in Firefox, Prioritizes Privacy

 
 
 
 WebProNews · 2025 
 

↗

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Quippd 
 
 2026 
 
 
 
 
 Interview 
 

### Fifteen Years of Waterfox: Alex Kontos on Independence, AI, and the Future

 
 
 
 Quippd · 2026 
 

↗