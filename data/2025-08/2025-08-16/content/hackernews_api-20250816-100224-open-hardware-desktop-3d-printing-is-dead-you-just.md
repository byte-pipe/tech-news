---
title: Open hardware desktop 3D printing is dead - you just don't know it yet | Josef Prusa / 3D printing
url: https://www.josefprusa.com/articles/open-hardware-in-3d-printing-is-dead/
site_name: hackernews_api
fetched_at: '2025-08-16T10:02:24.851984'
original_url: https://www.josefprusa.com/articles/open-hardware-in-3d-printing-is-dead/
author: rcarmo
date: '2025-08-15'
description: How Chinas strategic focus on 3D printing and patent incentives since 2020 created a "minefield".
tags:
- hackernews
- trending
---

## Hello Hacker News 🚀🚀🚀

I’ve done a little update on social since publishing of the article, let me copy paste it here.

Since I posted my “Open Hardware is dead” article, you’ve been asking me about “that patent” 🤔 I didn’t want you to miss the forest (thousands of filings since 2020) just because of one tree. But let’s take a look now. In this case: the MMU multiplexer (we open sourced it 9 years ago). Anycubic (another IDG Capital-backed company) used the tactic of filing in China for an easy initial grant:CN 222407171 U➡️DE 20 2024 100 001 U1➡️US 2025/0144881 A1. The playbook: file a Chinese utility model (10-year patent, same protections, lower examination, already granted) ➡️ claim that priority in Germany (again as a utility model, already granted) ➡️ file in the US. Cheap to file, but expensive and time-consuming to fight. I already wrote why prior art isn’t a magic wand that solves it immediately in my article ⤵️ And there are many more, we just found a new juicy one 🔥

I am in the comments on hacker news here!

## Original article ⤵️

Hi, FAB 2025 is still happening in Prague and it has been a wonderful event. It’s been great to meet so many people from our community at home, in Czechia! But during my chats with the attendee’s, there was one topic which was emerging time and time again, and that is the state of open hardware. I cannot talk about all of the open hardware, but I can share experience from 3D printing. And it is not good! Open hardware in 3D printing is dead - you just don’t know it yet. This is an opinion piece, imagine we are talking about this topic over a cold Pilsner …

## What happened?

Well, if you are in 3D printing a little bit longer, you must have noticed that over the last 5 years, a huge number of vibrant brands died. Basically every country in Europe and many states in the USA had a couple of their own machines and the industry was very very creative in that regard. Somebody brought an innovation, others adopted it and shared it back.

But around the year 2020 we registered the first mention of 3D printing as a strategic industry by the Chinese government. We know that now, after a few years of research. We first realized something is off when the price of the parts is higher than the sale price of a complete machine in some cases. That is what sparked our interest and research into the subsidies. They exist, and are very efficienthttps://rhg.com/research/far-from-normal-an-augmented-assessment-of-chinas-state-support/. Our industry, desktop 3D printing, faces a bleak future. Comparable to the automotive sector as if only one high volume car brand, say Audi, remained outside of China. That’s it. An inch away from complete dependency on China in an vital piece of tech, the one absolutely critical for creation of new IP.

## Patent minefield

When looking into the data we were wondering why there is suddenly a multiple fold increase in 3D printing patent applications in China just around the year 2020, take a look yourself.

(Data from Espacenet International Database by European Patent Organization, March 2025)

Just 4 household names went from filing 40 total applications in 2019 to 650 in 2022. WTF has happened, right? Did so much new innovation suddenly happen in desktop 3D printing? Are these patents bogus? Are they dangerous? Isn’t there prior art for everything in 3D printing? So many questions…

### WTF has happened?

3D printing became a strategic industry and things like “Super deduction” became applicable to it. It is quite normal that R&D costs are tax deductible around the world. But definitely not 200% as in this case. From our understanding you have to prove the true innovations to qualify and of course a patent application is clear proof! It doesn’t even have to be granted! Perfect!

So even in industries where a lot of the low-hanging fruit is gone, and the true innovations are now really rare - like 3D printing, you just patent spam every little variation of the stuff out there. And that is why open hardware is very disadvantaged because it’s just so easy to file the stuff which is out there already or do minimal modifications to it. From what we’ve seen the validity checks are not stringent at all and prior art doesn’t seem to matter much.

#### Are these patents bogus?

Mostly, but when hunting with a shotgun you don’t need to hit with all the pellets. With the sheer number just statistically some have to land.

#### Are they dangerous?

There are already some patents on our watch that could hamper the industry if they slip through and get granted in the EU or USA.

#### Isn’t there prior art for everything in 3D printing?

There is a huge discrepancy at the cost of filing the patent and then striking it down. 125 USD to file it in China. It is almost unrealistic for an open source project to even monitor these, let alone try to strike them in the application stage if not local to China. Proactively striking down the application when brought to EU/USA roughly 12,000 USD in really straightforward cases and multiple times that in other cases. When already granted it is 75,000 USD just to start and it is not a short run.

The fact you hold a prior art in your hand, doesn’t mean much. The patent will still prevent you from importing/selling etc of the “infringing” stuff. And you will have to battle the thing in the court to use the prior art card you hold. That can be a nice million dollar bill all while not being able to do your thing for years …

Open hardware has a huge disadvantage as it has to be manufactured/transported/sold and even if you do not want to manufacture and sell your own product, you want someone else to do it. And they will always try to avoid the risk.

Once the patent is awarded, there is a priority period for filing in other IP markets when you can ask for the protection and you have a good head-start compared to fresh filing.

All in all I think this super deduction is a great exploitation of the global IP law treaties but as always the small innovators and businesses outside are hurt the most.

### Impact

True impact is still not here “you just don’t know it yet” because of the timescale IP protections take, it can be well over 5 years from first filing in China to having someone’s project killed.

## What are we doing

Because of this reality, we’ve had to build an early warning team to monitor this and prepare the prior art. And we will welcome everyone who wants to join us in these efforts. Boutique, small, hobby, desktop, industrial - anyone who wants 3D printing out of IP clusterfuck!

I mean our MMU1 multiplexer (from 2016!) has been patented as an exact copy. This is already granted as utility model (sometimes called small patent - exactly the same protection but for shorter period) in Germany and China and filed as full utility patent application in USA 🤦‍♂️

We are working on a new community license so we are feeling more comfortable sharing as much as we used to share again with minimal risk of exploitation.

We are actively looking at the critical points which should be protected from the patent wall being erected and ways to do it. A possible option is to start an organization which would take care of this, to even out the skew happening now.

It is so bizarre to me, that we got to a stage where you need to think about protecting your designs and inventions in order to share them with the community …

## Takeaway

This is a story from 3D printing, but all the areas with heavy open hardware development are in Made in China 2025https://en.wikipedia.org/wiki/Made_in_China_2025and its successors. Make sure you keep an eye on the filings around your expertise, it is incomparably much easier to do something now than later.
