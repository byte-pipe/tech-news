---
title: The Fastest Way to Board an Airplane | Navendu Pottekkat - The Open Source Absolutist
url: https://navendu.me/posts/airlines-hate-this-trick/
site_name: lobsters
content_file: lobsters-the-fastest-way-to-board-an-airplane-navendu-potte
fetched_at: '2026-02-23T06:00:33.896629'
original_url: https://navendu.me/posts/airlines-hate-this-trick/
author: map[email:navendu@apache.org name:Navendu Pottekkat]
date: '2026-02-23'
published_date: '2026-02-21T10:29:50+05:30'
description: An interactive exploration to find the mathematically perfect way to board an airplane.
tags: visualization
---

Airlines hate this trick.

Show QR code

Hide QR code

There must be a better way to do this, surely.

I’m hardly the first person to think this while stuck behind a seemingly endless line of people waiting to board an airplane. If this question hasn’t crossed your mind yet, wait till the next time you are cut off from the world as you enter the narrow metal tube between the boarding gate and the airplane—unless yours has glass windows, in which case,enjoy the view!

When you finally board the plane, you and seven others ahead of you in the aisle remain stuck waiting for the guy in 16A—who took “you can bring personal items” too liberally—to finish stowing his luggage. i.e., one person blocks theentireaisle, insideandoutside the plane.

Theresurelymust be a better way. After all, throwing the gates open and making it a free-for-all wouldn’t work (?), and theback-to-frontboarding-group strategy airlines use doesn’t seem much better either.

NOTE

In each of the simulations below, passengerswalkdown the aisle to their row,stowtheir bag in the overhead bin, and take theirseat.

Thisimaginaryairplane has 20 rows of 6 seats; 3-3 configuration, single aisle.

HitPlayand watch.

Airlines typically group rows intozones. Boarding the zonesback-to-frontseems like a perfectly sensible and intuitive way to prevent people from blocking anyone behind them.Doesn’t it?

Let’s see this in action.Watch the aisle.

Simulation Speed
15 steps/sec
Play

Reset

Skip

0
/120 seated   
0
 steps

Boarding is slow when queues form behind a single person. When the first (out of four) zone boards,everyone clusters in the same few rows and blocks the same section of the aisle. The back of the plane becomes crowded while the front remains empty.

This feels inevitable. If you group people by adjacent rows, youguaranteecongestion. Everyone needs to stow their bags and sit roughly in the same rows. When they cannot pass each other or stow in parallel, they just wait.

Boarding back-to-front is so inefficient that having people board atrandomwhenever they arrive at the gate is faster.

Simulation Speed
15 steps/sec
Play

Reset

Skip

0
/120 seated   
0
 steps

Try running both simulations a few times and compare the step counts. Boarding at random is unintuitively butconsistentlyfaster than back-to-front.

Why?

When passengers are scattered across the plane, multiple people can stow bags at the same time because they are naturally spaced apart. One person stowing in row 3 while another stows in row 17 is much faster than five people queueing behind one person in row 18.

But we can do better.

Three groups: window, middle, aisle. In that order. Thewindow-middle-aisle (WilMA)method is essentially the same idea as random, but applied three times, once for each column of seats.

Simulation Speed
15 steps/sec
Play

Reset

Skip

0
/120 seated   
0
 steps

In reality, this isslightlyfaster than random, as it eliminates seat shuffles (you know, the awkward choreography where a seated passenger has to stand up and squeeze into the crowded aisle so you can reach your window seat). This isn’t modeled in the simulation, but it contributes less to boarding frustrations than bag stowage anyway.

I was surprised to learn that some airlines use this over back-to-front boarding, although I’ve never witnessed it in the wild.I will believe it when I see it.

Now,ladies and gentlemen, if you could leave your mortal souls for a moment and ascend to the realm of theory, where passengers are perfectly obedient biological automata, executing instructions without hesitation or complaint.

In JasonSteffen’smethod, there are no boarding groups. Every passenger stands in an exact order: back-to-front, alternating rows, alternating sides, windows first.

When two consecutive passengers enter the aisle, they are going to rows that are at least two apart. They willneverblock each other. They stow bags at the exact same time. The entire aisle becomes a neat, parallel-processing pipeline.

Simulation Speed
15 steps/sec
Play

Reset

Skip

0
/120 seated   
0
 steps

Look at all those simultaneous yellow dots.Beautiful.

Of course, this version exists only in theory. Any time saved in the aisle would inevitably be lost trying to herd people into that exact order at the gate.

So let’s descend back to Earth.Fasten your seatbelts.

A practical variant uses four boarding groups instead of individual seat numbers: one side of the plane in every other row, then the other side, then back again. Within each group, the windows board first, then middle, then aisle. This isn’t the logically perfect version, but at least parents can board with their kids now.

I ran each simulation 200 times and averaged the results.

Clearly, there are faster ways to board an airplane.

But if you did make it this far, you probably already knew that efficiency isn’t the only variable in the real world. Boarding groups aren’t designed purely for throughput. There are ticket classes and loyalty programmes, infants and senior citizens, and a myriad of otherhumanfactors that dictate priority.

We aren’t neat little yellow dots.

If you’d like to explore this further, I highly recommend the original works that inspired this article:

1. CGP Grey’s video -The Airplane Boarding Method That’s Too Perfect To Use(This article borrows heavily from CGP Grey’s excellent explanation—sometimes paraphrased, occasionally quoted—because it’s that good)
2. Jason Steffen’s original paper -Optimal boarding method for airline passengers
3. His follow up study -Experimental test of airplane boarding methods

See discussions onRedditandLobsters.

Webmentions • 3 • Last updated at 10:45 AM, 22nd February 2026

Have you written a response to this? Send me a webmention by entering the URL.
* MENTIONI love the little animations in this article. They really illustrate the point the author made very neatly.
The Fastest Way to Board an Airplanenavendu.me/posts/airlin...
* MENTIONThe Fastest Way to Board an Airplane via@abnvhttps://lobste.rs/s/l0gv3h#visualizationhttps://navendu.me/posts/airlines-hate-this-trick/visualizationThe Fastest Way to Board an Airplane
* MENTION

Thank you for reading"The Fastest Way to Board an Airplane."

Subscribe viaemailorRSS feedto be the first to receive
my content.

If you liked this post, check out myfeatured postsor learn moreabout me.

Get an occasional dose of tech news, curated content, and uninterrupted musings, delivered directly to your inbox.
