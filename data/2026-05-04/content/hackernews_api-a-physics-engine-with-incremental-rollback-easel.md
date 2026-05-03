---
title: A Physics Engine with Incremental Rollback • Easel
url: https://easel.games/blog/2026-rollback-physics
site_name: hackernews_api
content_file: hackernews_api-a-physics-engine-with-incremental-rollback-easel
fetched_at: '2026-05-04T06:00:17.839801'
original_url: https://easel.games/blog/2026-rollback-physics
author: BSTRhino
date: '2026-05-02'
published_date: '2026-05-01T00:00:00.000Z'
description: We want Easel to be powerful enough to make the kinds of games you would play for hours.
tags:
- hackernews
- trending
---

We want Easel to be powerful enough to make the kinds of games you would play for hours.
Popular multiplayer games likeAmong Uslet you walk around an entire spaceship, completing tasks and evading impostors.
Unfortunately, up to this point, games of that scale were out of reach for Easel,
because the off-the-shelf physics engine would have to snapshot and roll back the entire world
to support Easel's predictive multiplayer architecture.
It's too much to do every frame.

Until this point, you were required to keep your worldsmall. Butnot anymore!

Easel's newcustom-built physics engineonly snapshots and rolls back the parts of the world thatchange.
That big spaceship might have thousands of objects forming the walls, the control panels, the vents, and so on.
However, each frame, a surprisingly few number of objects actually change - perhaps less than 30 per frame
as the players walk around and interact with the world.
A smart implementation keeps objects sleeping while they are offscreen.

With only 30 objects out of thousands needing to be snapshotted each frame,
a factor of 30-50x fewer than before, multiplayer Easel games with large worlds suddenly becomes feasible.
Release the feral hogs!

## Under the Hood​

Easel's new physics engine is custom-built for Easel, which is why it supports everything Easel supports, but better!
Here is a tour of some of the features that make it special.

### Sleep​

The fastest way to do something is to not do it at all.
When a body is asleep, it does not require any snapshotting, rollback,
or any physics calculations until it wakes up again.
Unlike other engines which wait for a few seconds of inactivity,
Easel puts bodies to sleep immediately when their velocity reaches zero (within a small epsilon threshold, of course, we're notslow).

One tricky case here isgravity, which has the potential to keep your entire world awake with its constant nagging force.
Easel tracks the forces and reaction forces on every object and can see whether they are balanced or unbalanced.
Regardless of whether it is at zero velocity, as long as one body in a stack has unbalanced forces,
the stack has not settled into equilibrium and so the whole stack stays awake.

### Spatial Indexing​

Like many other physics engines, Easel'sbroad phaseuses a Bounding Volume Hierarchy (BVH) to quickly find potential collisions.
Easel's BVH algorithms are optimized to minimize unnecessary snapshotting and rollback,
only performing incremental rebalancing when the tree is already undergoing change.
Do you only do the vacuuming just before your friends come over? Easel's BVH islazyefficient just like you.

One additional trick is Easel's BVH also tracks theCategoriesof each collider,
which speeds up common game queries dramatically.
It is very common, for example, for a bot to target the nearest player, and if the player is on the other side of the map,
it would have to traverse through every single collider in the world to find the nearest player.
Finding the nearestCategory:Needleamongst a sea ofCategory:Haystackcolliders is a lot faster with a metal detector!

### Stepping​

Making a character take a step is something so common but surprisingly complex in physics engines.
A common method is to add velocity for the step, then subtract it after the physics simulation is complete,
but a problem arises when the character collides with an obstacle mid-step.

Even if the physics engine does its job correctly and zeroes out the velocity,
later on when the previously-added step velocity gets subtracted, it reintroduces the bounce back that the physics engine just zeroed out.
It makes your character feel really bouncy.

* Some games fix this bydampingout all velocity, which removes bounce back but also removes knockback too,
removing some of the fun and feel of the game. Walk into a wall? No bounce, good. Get hit by a fireball? No knockback. Seems wrong.
* Other games fix this by creating akinematic character controllerbased on raycasting.
In physics engine terms,kinematic(as opposed to static or dynamic) means that the character is not affected by forces and collisions.
In other words, the physics engine has failed to produce the desired results, and so it is now being bypassed entirely.You had one job physics engine. Physics. Do it. Please. Not not like that. Okay fine I'll do it myself.

Non-bouncy stepping has been built directly into the solver of the Easel physics engine.
Simply useForcefulStepwith the newrestitution=0parameter,
and Easel's new physics engine will make sure the step does not bounce back.

#### How does it work?​

The trick is, Easel treats stepping in a similar way to how it corrects for position overlap.

Have you ever played a game where your character gets stuck in a wall,
and the physics engine tries toejectyou, sending you flying across the map?
It is a common physics engine glitch.
Super Mario 64 speedrunners famously love to make him slide backwards up the stairs on his backside using a glitch like this.
Ow.

Modern physics engines try to avoid this problem by solving forposition correctionseparately.
The force that would eject your character out of the wall is applied immediately to the position without changing your velocity,
which means theejection velocity does not lastbeyond the current frame.

ForcefulStepin Easel is implemented as part of position correction,
which is why it does not cause bounce back, unless you want it to.
We're killing two (angry) birds with one stone!

info

In reality, it is a bit more complicated for numerous reasons.
Easel first solves for both ejection+stepping and velocity at the same time,
then we store that ejection velocity, then we remove the ejection+stepping constraints and solve again, storing the stabilized velocity.
At this point, nothing has moved yet, which is why we are now free to sweep for the next time-of-impact using the correct velocities.
When it comes time to take a step, we use the ejection velocity, but at the end of the frame we only commit the stabilized velocity
and so the bounce disappears.

In other words, Easel collects all the data it needs up front without making changes, so that when it does make a move, it can make the correct one.

### Continuous Collision Detection​

We love it when two fireballs collide with each other in mid-air.

Finding the collision between two fast-moving objects like this requires continous collision detection,
because if we just checked for collisions once every frame,
we might miss the precise moment when the two fireballs overlap.

Continuous collision detection is Easel is performed by sweeping and then shape casting like other physics engines,
but in doing this we noticed a few differences between Easel other physics engines
which may be interesting to somenerdsgame developers:

* TheRapierphysics engine can produce an incorrect result when the fireball begins the frame touching a mirror.
In Easel, collisions are resolved first, causing the fireball to bounce and change direction,
andonly thendoes it search for the time-of-impact of those two fireballs.
In Rapier, the time-of-impact is searched for first using the original velocities,
meaning that in this case, it starts by sweeping that fireball in the wrong direction.
This difference happens because Rapier does the position integration early,
committing to a substep length before it knows what the time of impact is going to be.
Easel stores enough information up front that it can do the position integration after it knows the time of impact, avoiding this problem.
* Box2D 2.4does sweep using the correct velocities but takes a different approach of doing the full normal physics simulation,
then backtracking, which is why all collisions are already resolved before continuous collision detection.
Interestingly, the newBox2D 3.0does not support dynamic-to-dynamic continuous collision detection at all,
meaning those two fireballs would have no choice but to miss each other like ships in the night.
Perhaps this is a future direction for Box2D as, besides this, it seems they have achieved the holy grail of avoiding substepping at all
by using speculative contacts.
* Photon Quantum, a professional multiplayer rollback netcode engine, does not support continuous collision detection at all,
citing that their physics engine is stateless and so it would be too expensive.
It seems incremental snapshotting and rollback of our physics state has enabled Easel to support this feature performantly.

### Bodies can move themselves​

One inconvenient edge case with the previous physics engine is that a body with avelocityorturnRateand no colliders
would not move at all.

It could be argued that this is correct. If there is no mass to hold momentum, there's no movement,
but we are not just making aphysicsengine, we are making agameengine.
Sometimes bodies are just a way to group sprites together, and the physics is not important.

Now if you give a body avelocityorturnRate, it will move itself even if it has no colliders.
Attach aTextSpriteand you could have a simple billboard floating up the screen,
scrolling away to a galaxy far, far away.

Sidenote: Photons don't have mass but they still have velocity,
in fact there are10^17of them hitting your eyes right now every second,
so maybe some physics engines need a reality check.

## Thanks to​

Easel's physics engine is built upon the collision detection algorithms ofParry,
an excellent open source library created by Dimforge that powers theRapierphysics engine.

Making a physics engine has been a huge endeavor.
Many little decisions have been made to make implement it in a way
that is neat, efficient and works well with Easel's multiplayer architecture.
Now everything, not just the physics engine, but all parts of Easel only snapshot and rollback
the parts that change, meaning you can make much bigger worlds.

It's time think bigger!