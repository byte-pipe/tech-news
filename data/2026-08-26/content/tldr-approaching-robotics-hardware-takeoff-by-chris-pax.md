---
title: Approaching Robotics Hardware Takeoff - by Chris Paxton
url: https://itcanthink.substack.com/p/approaching-robotics-hardware-takeoff
site_name: tldr
content_file: tldr-approaching-robotics-hardware-takeoff-by-chris-pax
fetched_at: '2026-08-26T12:52:30.504016'
original_url: https://itcanthink.substack.com/p/approaching-robotics-hardware-takeoff
author: Chris Paxton
date: '2026-08-26'
description: And some thoughts on the World Humanoid Games
tags:
- tldr
---

# Approaching Robotics Hardware Takeoff

### And some thoughts on the World Humanoid Games

Chris Paxton
Aug 25, 2026
23
7
4
Share
Image from ChatGPT

TheWorld Humanoid Games are underway in Beijing, and the world is watching. Robots are sprinting, long jumping, boxing, and playing soccer. The results are, at times, comical. Sights of one robot after another slamming into a wall at the end of a race, or soccer-playing Booster robots tripping over one another into a gigantic heap, make this all seem like a bit of a joke sometimes.

But feeling this way would be a mistake. Instead, I would argue that these games show a robust, mature ecosystem which can both build things and, crucially, isn’t afraid to break them. And that’s key to real progress.

It’s staggering how much different things are from last year. The robots are faster, more intelligent, and more capable. They’re also a lot more flammable, with multiple instances of fast-moving sprinters exploding or bursting into flames due to the tremendous heat being generated.

A very rapid pace of robotic hardware and software innovation is enabling a robust ecosystem, in which many different companies and laboratories can build high-quality products, and even develop one-off robots like theHonor Lightning, a humanoid robot designed purely for sprinting and which recently beat (human) Usain Bolt’s 100 meter record.

Subscribe

## Production Scale Explodes

Unitreesold over 5,500 humanoid robots in 2025, mostly its G1 humanoids. And after an explosive IPO, it seems unlikely that this will change any time soon. There’s tremendous demand right now for capable, usable, and deployable robots — and Unitree’s humanoids are something of a gold standard for the industry.

Their secret, in larger part, has been shipping and iterating. Unitree is ruthless about punishing and testing their robots. In 2024, they were hauling the first G1 around to every academic conference, watching the robot slowly accumulate scratches and nicks, even though it could at the time barely walk. At the same time, they would bring out their quadruped robots and kick them down the stairs, showing exactly how durable and reliable they were when the robot could be piloted right back up.

They’ve been iterating quickly on their humanoids, going from what used to be a relatively useless G1 to an incredibly popular and well-oiled product, in part powered by rapid hardware cycles, aggressive vertical integration, and intense optimization.

And yet by most accounts they’re not even the biggest producer of humanoid robots. That would be Agibot:

Agibot is far less seen outside China, though robots like the Agibot X2 (their answer to the Unitree G1). US companies like Faraday Future have beenselling some suspiciously similarrobots to those Agibot offers. Agibot also sells a number of industrial semi-humanoids like the A2-W:

Agibot A2-W 
from their online store.

These robots are designed for industrial use cases as they’re somewhat easier to deploy in different industrial use cases. Robots like theAgibot G2 support autonomous chargingand have beenshown in real industrial use casesalready.

Companies like Galbot on the industrial side,with its heavy-duty S1 robots, andBooster with its developer-focused K1 and T2, also provide great robots. TheGalaxea R1has established itself as a very standard manipulation research robot, starring in theoutstanding Stanford Behavior-1k benchmark. In short, there’s a massive number of companies, producing a truly amazing number of robots.

And lest we think the companies mass producing mobile robots are ALL Chinese, American humanoid company Figure, clearly at this point the manufacturing leader in the United States, also built its 1000th robot in July of this year:

From Brett Adcock on X

And multiple other humanoid companies are gearing up for increased production as well. But no one seems close to reaching the scale of hardware depth and quality as the ecosystem apparent in China right now.

## Innovation Follows

Humanoid robot designs are both showing diversity, but also converging on a couple form factors around certain roles. We’ve seen a number of robots pick up a wheeled elevator base pattern seen onSundayandWeaverobots, a number of full-sized humanoids likeFigure,1X, Tesla, and the Unitree H2, and a range of smaller developer-focused robots. The biggest robot producers (like Unitree and Agibot) all have a range of different platforms now, filling different roles — though the biggest sellers are still development-focused, child-sized robots like the Unitree G1.

TRON2 is a modular robot architecture, built by LimX Dynamics. 
Source: X

Hardware and software innovation is everywhere. LimX, for example, has been developing its modular TRON series robots, and Fourier has built itsmore care-centric GR-3 humanoids, with soft and friendly bodies.

This empowers learning research as well. Massive open datasets like theGalaxea Open World DatasetandAgibot Worldare invaluable for researchers, and couldn’t exist without abundant hardware. It also enables research and development ofrobot foundation models like Lingbot-VA-2.

It’s a robust ecosystem that will pay dividends in the future, because one of the biggest barriers in robotics is just having robots, and having robots that can do useful things! No longer is this an issue. We have a lot of robots, for every possible niche, and the real barrier now is just making them smart enough. And as we saw with LLMs, good data is key to solving that problem.

## Past Competitions Drove Progress

Think back to events like the DARPA Grand Challenges of the 2000s in the United States. DARPA asked universities and researchers to build a self-driving car, as American troops were dying to roadside bombs in Afghanistan and Iraq.

The researchers gathered in the Mojave desert to drive along a 240-km route. Not a single vehicle completed the route. Next year, five vehicles out of 23 completed a new, 212-km route. In 2007, at the Urban Grand Challenge, only six out of 11 teams completed a much shorter 89-km routethrough George Airforce Base.

Despite the atrocious failure rate, and the poor performance by human standards even of the winners, the finalists would go on to form the core of the self-driving car boom, founding companies like Waymo and Zoox which have autonomous vehicles on the roads today.

And this is where we come back to the World Humanoid Games. Competitions like this might be filled with failures —watch this amazing compilation of falls from the DARPA robotics challenge— but they spread information, ideas, and help enable real progress, just the same.

## Final Thoughts

We’re at a strange point in time for robotics. Robotic hardware — good hardware — is available in a way that has never been possible before. It’s more robust — massively so — and robots areincreasingly both affordable and capable. In this environment, it’s thrilling to see stuff like the Humanoid Robot Games, which will I think inspire and drive forward a new generation of engineers and researchers who will build robots that are actually useful.

One thing that strikes me, is that the most important thing when building robots seems to bejust building robots. That’s been a huge part of Unitree’s success: they build a lot of robots. If a robot breaks, they figure out why, and they make it stop breaking in that way.They build actuatorsbecause those are the bottleneck in the price of a robot. They sell robots and make money doing it —278.21 million yuan of profit in 2025 alone— and their explosive IPO saw their company value rise to $50 billion. They’rethecompany building and selling general-purpose robots at scale, and the recipe works for them. But, importantly, it did not start that way: it started with a line of robot dogs and a Unitree G1 that could barely put one foot in front of the other.

So, even if right now a lot of these robots fall down and burst into flames, a massive wave of real, working robots seems like it’s just on the horizon.

Subscribe

Share

Leave a comment

## Further Reading

SemiAnalysis
Unitree's Impossible Trajectory Is Still Overlooked
We are witnessing the birth of another Chinese hardware giant. Three years ago, Unitree was a quadruped company. By last year, they parlayed quadruped dominance into creating and leading the humanoid market. This year, their G1 humanoids are finally entering into viable deployments, and three new designs are on the way, including their most-direct…
Read more
3 months ago · 312 likes · 2 comments · Reyk Knuhtsen, Niko Ciminelli, Jacob Rintamaki, Robert Ghilduta, Joe Ryu, Jeremie Eliahou Ontiveros, and Dylan Patel
23
7
4
Share
Previous