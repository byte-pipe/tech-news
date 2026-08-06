---
title: Mario meets Pareto
url: https://www.mayerowitz.io/blog/mario-meets-pareto
site_name: hackernews_api
content_file: hackernews_api-mario-meets-pareto
fetched_at: '2026-08-07T06:00:17.283227'
original_url: https://www.mayerowitz.io/blog/mario-meets-pareto
author: Antoine Mayerowitz
date: '2026-08-06'
description: Discover how to find the best Mario Kart 8 build using the Pareto frontier method. This interactive guide explores multi-objective optimization of speed, acceleration, and other key stats to help you beat your friends on the race track.
tags:
- hackernews
- trending
---

Mayerowitz.io
 

# Mario meets Pareto

 
 
 
 

## Step on the Front Line and Beat your Friends

 

Written byAntoine Mayerowitz

 
 
 
 
 
 
 
0
 
 
 
0
 
 
 
0
 
 
 
0
 
 
 
 

In Mario Kart 8, choosing your driver, kart's body, tires, and glider isn't just
 about style — it's as crucial as your racing skills to win a race. Ever
 wondered how to truly find the best ones?

 

For each of those four elements, you have tens of options. For each option,
 there are distinct statistics (speed, acceleration, ...) affecting your
 performance.

 

This adds up to an unbelievable amount of builds to choose from.

 

Hopefully, many choices are just stylistic — they have identical
 statistics — but even after ignoring those duplicates, it remains a tough
 job to navigate the thousands of options.

 

Is there any chance to find thebestbuild or is it
 just luck? Should you favorspeedto be the fastest, oraccelerationto quickly recover after taking a hit? Let me show you a solution proposed over a
 century ago by economist Vilfredo Pareto.

 
 
 
 
 

Finding the fastest driver is as simple as ranking them by theirspeedstatistic. Here you might think thatBowser orWario are a no-brainer.

 

But you can't just rely on
 speed
 to find the optimal build. You have to consider
 one as well. Now, finding the bestdriverbodytireglideris not trivial anymore — you have to make trade-offs betweenspeedaccelerationhandlingweightoffroadmini turboandspeedaccelerationhandlingweightoffroadmini turboReset

 

Look closely though! You'll find out that some options are alwaysdominated. Let's focus on this poorKoopa for instance.

 

Cat Peach has more speed for the same acceleration, andToadette has more acceleration for the same speed. Between you and me, if you
 want to win, never allowKoopa to sit in your kart!

 

You can identify all efficient drivers that, unlike Koopa, are never dominated
 on bothspeedandacceleration. Together, they form what is called
 thePareto front(or frontier).

 

Mind you: not all elements of the frontier are equally good. You probably won't
 pick a driver sitting on the edge of the frontier because you want some balance
 betweenspeedandacceleration. The Paretoefficiencyis an
 objective criteria to filter out suboptimal choices, but you still need to make up
 your final decision.

 

Given your play style and skills, you may put moreweighton one statistic over
 the other. Those preferences will reveal the component on the frontier that
 suits you the best.speedaccelerationhandlingweightoffroadmini turbospeedaccelerationhandlingweightoffroadmini turboBestdriverbodytireglider: {}

 
 
 

In practice, you not only choose a driver, but a full set of body, wheels, and glider.
 In the next section, I'll display every build as a distinct point. It will however make
 the number of choices explode. But Pareto's with us!

 

We've had a bit of fun here, but don't you see the pattern? We're often faced with
 similar trade-offs. You want ameal that's both cheap and delicious? A job that's both well-paid, easy, and fulfilling?A portfolio with low risks and high returns? A flexible and strong material that's also easy to produce?A fair taxation that remains efficient?A high quality LLM that is also fast and cost-efficient. In all these cases, you're facing a multi-objective optimization problem, and you
 have to make trade-offs.

 

Of course, if you already know the exact weights you want to assign to each dimension
 (i.e., you know your utility function), you reduce the problem to a single objective
 optimization. This is because you can combine the dimensions with the weights into a
 single quantity to optimize (often called utility, cost, or fitness). In that case, you
 don't need Pareto at all.

 

But you're often faced with situations where your utility function is unknown or
 uncertain. In those situations, the Pareto front helps you eliminate objectively all the
 sub-optimal options. It won't reveal the one best option right from the outset, but you
 may now experiment with these efficient options and select the one that fits you the
 best.

 

### Acknowledgments

 

I've made some simplifying assumptions in this article to keep it readable for a large
 audience. In truth, the statistics that I presented are translated into derived in-game
 stats that are not always linear with the base statistics. Additionally, there are 4
 speed stats and 4 handling stats for all gears (except for the driver), but I decided to
 simply average those. I've also completely hidden the functional form of the utility
 function, which can play a great role. To get access to more details behind this article
 or if you just like my work and want to see more in the future, please considerdonating some coins.

 

### Credits

 

Super Mario WikiMario Kart 8 Deluxe in-game statistics

 

Henry H.Mario Kart and the Pareto Frontier, 2015