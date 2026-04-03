---
title: Art of Roads in Games
url: https://sandboxspirit.com/blog/art-of-roads-in-games/
site_name: hackernews_api
content_file: hackernews_api-art-of-roads-in-games
fetched_at: '2026-02-09T11:22:37.555941'
original_url: https://sandboxspirit.com/blog/art-of-roads-in-games/
author: linolevan
date: '2026-02-08'
published_date: '2026-01-29T00:00:00.000Z'
description: How games implement roads
tags:
- hackernews
- trending
---

# Art of Roads in Games




January 29, 2026



 7 min read








Not sure if it’s just me, but I often get a primal satisfaction whenever I see intricate patterns emerging out of seemingly disordered environments.

Think about the galleries of ant colonies, the absurdly perfect hexagons of honeycombs, or the veins on a leaf. No architect, no blueprint. Just simple rules stacking on each other that result in beautiful patterns. I can’t explain why, but seeing those structures always felt good.

Humans do this too. And for me, one of the most fascinating patterns we’ve come up with is the roads.

Sometimes I imagine aliens from faraway galaxies discovering Earth long after we’re gone. Forests reclaimed by nature, cities reduced to rubble, yet between them, a faintly pattern is still visible - the road network. I like to think they will feel the same way I do when looking at nature patterns. - “Man, someone really thought this through.”

# City Builders and Their Roads

I’ve got to say, roads have fascinated me since I was a kid.

I still remember playing SimCity 2000 for the first time when I was about five or six years old. I didn’t understand much. Definitely didn’t know what zoning, taxes, or demand were. But roads fascinated me from the start.

I think roads lie at the heart of every city builder. It’s the fabric on which cities are built. Since that moment, I’ve played almost every modern-themed city builder out there. In the meantime, I’ve also started noticing them in the real world. Examining them in more detail.

Roundabouts. Interchanges. Overpasses. Merge lanes. Noticing every intricacy.

Despite every game bringing an improvement over the one before, something always felt… off.

SimCity 4 added elevation and diagonal roads. SimCity 2013 introduced curved roads. Then came Cities: Skylines with a ton of freedom. You could know freeplace roads and merge them into intersections at any angle, build flyovers at different elevations to construct crazy, yet unrealistic, interchanges. I think this was the largest breakthrough.

But something was still nagging me. Highway ramps were unrealistically sharp or wobbly, lanes that were supposed to be high-speed bent too sharply at certain points, and the corner radii of intersections looked strange.

I mean look at this. This is probably what highway engineers have nightmares about.

And then came the mods. Mods changed everything. The great community enabled a new kind of freedom. One could build almost anything: perfect merge lanes, realistic markings, and smooth transitions. It was a total game-changer. I am particularly proud of this 5-lane turbo roundabout:

But even then, mods didn’t feel completely natural. They were still limited by the game’s original system.

Cities: Skylines 2 pushed it even further, with lanes becoming even more realistic and markings as well. I think at this point, a non-trained eye won’t know the difference from reality.

Then I stopped stumbling around and started asking why? I tried to understand how engineers design roads and how game developers code them.

That’s when I ran straight into the fundamental issue - right at the base of it. And it comes to something every developer knows about and loves:

## The Bezier Spline

If you’re a Unity or Unreal developer or played with basically any vector graphics editing software, you already know them well. Bezier curves are an elegant, intuitive, and incredibly powerful way to smoothly interpolate between two points while taking into consideration some direction of movement (the tangent).

That’s exactly what roads are supposed to do, right? Of course, developers naturally think they are the perfect tool.

They’ve gottheir beauty, I need to admit. But hidden beneath the surface lies an uncomfortable truth.

## When Bezier Splines fall short

You see, the shapes of roads in real life come from an underlying essential fact: the wheel axles of a vehicle. No matter how you drive a car, the distance between the left and right wheels remains constant. You can notice this in tyre tracks in snow or sand. Two perfectly parallel paths, always the same distance apart maintaining a consistent curved shape.

Cars don’t follow abstract splines. They ride some imaginary tracks.

Here’s the issue with Bezier splines: they don’t preserve shape and curvature when offset.

At gentle curves, they kinda look fine, but once you have tighter bends, the math falls apart. In mathy terms: The offset of a Bezier curve is not a Bezier curve.

When game engines try to generate a road mesh along a Bezier spline, the geometry often fails at tight angles. The inner edge curves at a different rate than the outer edge. This creates “pinching,” self-intersecting geometry.

Here is the best example of how they start to fail in extreme scenarios.

To sum up: Bézier curves are unconstrained. The freedom they enable is exactly the “Achilles’ heel”. Real roads are engineered with the constraints of real motion in mind. A car’s path can’t magically self-intersect.

## Kindergarten math

Ok, so what preserves parallelism? If you’ve already been through kindergarten, you’re already familiar with it: It’s theCIRCLE.

It has almost like a magical property: no matter how much you offset it, the result is still a circular arc. Perfectly parallel with the initial one. So satisfying.

Scrapping Bezier curves for Circle Arcs also yields a nice, unexpected bonus. To procedurally build intersections, the engine has to perform many curve-curve intersection operations multiple times per frame. The intersection between two Bezier curves is notoriously complex. On one side, you have polynomial root finding, iterative numerical methods, de Castelaju’s method + bounding boxes, and multiple convergence checks vs a simple, plain O(1) formula in Circle Arcs.

By stitching together circular arcs of different radii, you can create any shape while adhering to proper engineering principles.

## The Next Level

But this is not the end of the story. Circle arcs have issues as well (Oh no). The problem with circles in infrastructure is that they have constant curvature. What this means is that when entering a circular curve from a straight line, the lateral force jumps from 0 to a fixed constant value (determined by the radius of the circle). If you were in a car or train entering at high speed into this kind of curve, it would feel terrible.

Civil engineers have to account for this as well. So then, what curve maintains parallelism when offset and has a smoothly increasing curvature?

Introduce you to: transition curves - most famously, the clothoid.

Aclothoidgradually increases curvature over distance. You start almost straight, then slowly turn tighter and tighter. The steering wheel rotates smoothly. The forces ramp up naturally, and a passenger’s body barely notices the transition.

These curves provide comfortable rides at high speeds by maintaining parallel offsets and continuous curvature changes.

And they are also… a math nightmare. Differential geometry. Integrals. Oh my… Which is probably why most games don’t even dare.

But that’s fine.

Vehicles move slowly on city streets. For intersections of urban roads, circular arcs are more than a decent choice.

# Why I Built My Own Road System

Does everything I just rambled about matter? Do 99% of city-builder players care what shape the corner radius of the intersection has? Most likely, no. Then why bother?

First, because of curiosity. As any other nerd overly obsessed with the nitty-gritty details of a very specific subject, I just wanted to see how I would implement it. Like challenging the status quo.

Second, even if established titles might not accurately render roads, they are still light-years ahead of what solutions an indie developer can find online. The tutorials and assets for this are just sad. I personally got bored with grids, and I just wanted to built a better solution to share with anyone who wants to build a city builder.

These assets ^ make me sad.

In the next blog post, I’ll discuss more technicalities and dive into how I’ve built my own solution. If you want to follow along or get notified when I release this asset, scribble your email below.













## Join my mailing list




Hello there 👋 I share a new blog post once a month-ish.If you
 find my work interesting and want to stay in the loop enter your email
 below. I guarantee I’ll never spam you.



Subscribe
By submitting the form, I agree to the

Privacy Policy
.
