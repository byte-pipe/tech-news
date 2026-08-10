---
title: 'Backend Engineer (Me) Ships a Browser Game With One Unintentional System Requirement: My Monitor - DEV Community'
url: https://dev.to/georgekobaidze/backend-engineer-me-ships-a-browser-game-with-one-unintentional-system-requirement-my-monitor-1ojd
site_name: devto
content_file: devto-backend-engineer-me-ships-a-browser-game-with-one
fetched_at: '2026-08-10T19:54:33.595407'
original_url: https://dev.to/georgekobaidze/backend-engineer-me-ships-a-browser-game-with-one-unintentional-system-requirement-my-monitor-1ojd
author: Giorgi Kobaidze
date: '2026-08-09'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. Prefer... Tagged with devchallenge, bugsmash.'
tags: '#devchallenge, #bugsmash'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

## Prefer Watching Instead?

If reading isn't your thing, no worries, I've got you covered. You can watch the video below:

## Table of Contents

* Introduction: In What Universe Did I Think This Was a Good Idea?
* The Game
* The Game Loop
* The Game Physics
* It Worked on My Machine Goddammit
* Understanding the Root Cause
* The Fix: Delta Time
* But There's a Catch: Not Everything Is Fixed With× dtPattern 1: Linear operationsPattern 2: Exponential decayPattern 3: Lerp smoothing
* Pattern 1: Linear operations
* Pattern 2: Exponential decay
* Pattern 3: Lerp smoothing
* Summary: The Three Patterns
* One More Thing: Re-tune Your Constants
* Pull Request
* The Takeaway

## Introduction: In What Universe Did I Think This Was a Good Idea?

It was a nice, calm day. Everything was going smoothly, I was just minding my own business.

Out of nowhere, a notification from@jesspopped up. And I see this:

Good morning! Good afternoon! Good Evening!

Welcome to our first DEV Weekend Challenge, a short focused challenge designed to fit into your weekend. Since submission window is tight, we've set the timing to ensure that no matter where you are in the world, you'll have the majority of your Saturday and Sunday to participate.

Let's get started!

I don't know what's exactly wrong with me, but whenever I see a word "challenge", something clicks in my brain and it starts a multi-thousand thread process to think of an idea until the idea isn't generated. This time was no different. But in some ways, it really was quite different.

Let me explain why. So here's my thinking process:

* OK I just have the weekend. 2 days tops, that's it. Well, sometimes just planning can take way more than that.
* I'm a full-stack engineer with extensive back-end background, so back-end is my primary comfort zone.
* Building something fun and flashy would be great, like a... browser game? Hell yeah!!! ... well, except, I ain't no game developer and I have never ever written a browser game.

...

So I decided to build... drum rolls ... A BROWSER GAME!

If you're not a technical person, a back-end developer building a browser game is an NFL player playing tennis.

You already know this isn't gonna end well, don't ya?

## The Game

You're probably wondering what kind of game I created. It's basically a driving simulator (well... kinda) - a synthwave 3D driving game where your DEV community articles appear as neon billboards along the endless highway. It fetches articles, stats, and things like that using the DEV Community by the username.

If you'd like to give it a try before continuing, here are the relevant links:

DemoSubmission articleGitHub Repo

## The Game Loop

Sunday DEV Drive is a browser game built on top ofThree.js- a JavaScript library that handles 3D rendering in the browser. The game runs entirely client-side: no server, no backend, no build step. Just HTML, JavaScript, and your DEV Community articles fetched from a public API.

The game is built around agame loop: a function that runs over and over, many times per second. On each iteration it does the same three things:

1. Read inputs- is the player pressing the accelerator? Turning left?
2. Update the world- move the car, adjust the camera, apply physics
3. Draw the frame- render everything to the screen

In the browser, the standard tool for this isrequestAnimationFrame. You give it a function, and the browser calls that function right before it repaints the screen — as fast as the display allows:

function
 
animate
()
 
{

 
requestAnimationFrame
(
animate
);
 
// "call me again next frame"

 
updatePhysics
();

 
updateCamera
();

 
renderScene
();

}

animate
();
 
// start the loop

Enter fullscreen mode

Exit fullscreen mode

Think of it like a flipbook. Each call toanimate()draws one page. The faster the pages flip, the smoother the motion looks. On a 60Hz monitor, the browser flips 60 pages per second. On a 165Hz monitor, 165 pages per second.

## The Game Physics

The car's movement is simple Newtonian-ish math applied every frame, nothing exotic, just the kind of physics you vaguely remember from high school:

* Throttle→ adds to the car's speed (acceleration)
* Speed→ moves the car's position
* Steering→ rotates the car's angle
* Friction→ slowly reduces speed when no input is held
* Camera→ smoothly follows the car from behind

Simple stuff. Which is exactly why the bug hiding inside it was so easy to overlook.

## It Worked on My Machine Goddammit

I tested the game. Multiple times. Zero issues. The car moved naturally. Steering felt great. Acceleration was progressive. The brakes had a nice bite to them.

Everything felt perfect.

Well, until I tested it on another computer. Ladies and gentlemen, I need your attention, please: I don't care how certain you are that your code works:

ALWAYS TEST IT ON ANOTHER COMPUTER.

I decided to flex a little and show the game to my mom and brother. So I sent them the links.

"Hey, check this out. I made a game."

A few minutes later, they texted me back:

* "The visuals are really good, but the car is barely moving. Is this by design?"
* "Umm... whaddaya mean "barely moving?" I just tested it and it's fine. Are you sure you're pressing the gas?"

So I started troubleshooting.

And troubleshooting.

And troubleshooting some more.

Nothing made sense.

The controls were working. The game was running. There were no obvious errors. Yet somehow, on their machines, my beautifully engineered car had apparently decided to become a mobility scooter.

I had no idea what was going on.

So I did what any developer would do in this situation:

I GoogledI asked AII stared at the codeI sketched things outI questioned my architectural decisions.

...

I questioned my life choices.

And then it just clicked.

I had used the monitor's refresh rate as part of my movement calculations.

Yep.

My physics weren't actually frame-rate independent.

My monitor was running at 165 Hz. Their monitor was running at 120 Hz.

That's a 45 Hz difference.

45 frames per second was enough to turn my perfectly drivable car into a perfectly drivable car, but in slow motion.

The game wasn't broken on my machine. My monitor was secretly a system dependency.

I had messed up... And badly.

And now it was time to fix it.

## Understanding the Root Cause

My animate loop looked like this:

function
 
animate
()
 
{

 
requestAnimationFrame
(
animate
);

 
carState
.
speed
 
+=
 
acceleration
;

 
car
.
position
.
x
 
+=
 
Math
.
sin
(
carState
.
angle
)
 
*
 
carState
.
speed
;

 
car
.
position
.
z
 
-=
 
Math
.
cos
(
carState
.
angle
)
 
*
 
carState
.
speed
;

}

Enter fullscreen mode

Exit fullscreen mode

requestAnimationFramecalls your functiononce per display refresh. On my 165Hz monitor, that's 165 times per second. On a 120Hz monitor, 120 times.

The problem:every physics value was per-frame, not per-second.

Look at what actually happens across different hardware:

Frame Rate

Updates/sec

Effective speed/sec

165 fps (my machine)

165

0.42 × 165 = 69.3
 ✅ feels right

120 fps

120

0.42 × 120 = 50.4
 🙂 73% of intended

60 fps

60

0.42 × 60 = 25.2
 😐 36% of intended

30 fps

30

0.42 × 30 = 12.6
 😩 18% of intended

I had unknowinglytuned the entire game for 165fps. Everyone else was experiencing a completely different game.

## The Fix: Delta Time

The solution is to measure the actual time elapsed between frames and use it to scale all physics updates. This is calleddelta time.

const
 
clock
 
=
 
new
 
THREE
.
Clock
();

function
 
animate
()
 
{

 
requestAnimationFrame
(
animate
);

 
const
 
delta
 
=
 
clock
.
getDelta
();
 
// real seconds since last frame

 
const
 
dt
 
=
 
delta
 
*
 
60
;
 
// normalized: 1.0 at 60fps baseline

 
// Now multiply everything by dt

 
carState
.
speed
 
+=
 
acceleration
 
*
 
dt
;

 
car
.
position
.
x
 
+=
 
Math
.
sin
(
carState
.
angle
)
 
*
 
carState
.
speed
 
*
 
dt
;

 
car
.
position
.
z
 
-=
 
Math
.
cos
(
carState
.
angle
)
 
*
 
carState
.
speed
 
*
 
dt
;

}

Enter fullscreen mode

Exit fullscreen mode

clock.getDelta()returns the real elapsed time in seconds. At 60fps that's~0.0167s.At 165fps it's~0.006s.At 30fps it's~0.033s.

I multiply by 60 to normalize:dt = delta * 60. This means:

* At 165fps →dt ≈ 0.36(smaller steps per frame, same per second)
* At 60fps →dt ≈ 1.0(baseline)
* At 30fps →dt ≈ 2.0(larger steps per frame, same per second)

Now the same distance is covered per second regardless of hardware:

Frame Rate

dt
 per frame

Movement per frame

Movement per second

165 fps

≈ 0.36

speed × 0.36

speed × 60
 ✅

60 fps

≈ 1.0

speed × 1.0

speed × 60
 ✅

30 fps

≈ 2.0

speed × 2.0

speed × 60
 ✅

## But There's a Catch: Not Everything Is Fixed With× dt

Simple* dtfixes linear operations. But a real game has more than just linear math. In this fix alone, there were three distinct patterns, each requiring a different approach.

### Pattern 1: Linear operations

The straightforward one. Any additive rate just gets multiplied bydt:

// ❌ Frame-rate dependent

carState
.
speed
 
+=
 
CAR
.
acceleration
 
*
 
throttle
;

carState
.
speed
 
-=
 
CAR
.
brakeForce
 
*
 
brake
;

car
.
position
.
x
 
+=
 
Math
.
sin
(
carState
.
angle
)
 
*
 
carState
.
speed
;

carState
.
angle
 
+=
 
carState
.
steer
 
*
 
carState
.
speed
 
*
 
CAR
.
turnSpeed
;

// ✅ Frame-rate independent

carState
.
speed
 
+=
 
CAR
.
acceleration
 
*
 
throttle
 
*
 
dt
;

carState
.
speed
 
-=
 
CAR
.
brakeForce
 
*
 
brake
 
*
 
dt
;

car
.
position
.
x
 
+=
 
Math
.
sin
(
carState
.
angle
)
 
*
 
carState
.
speed
 
*
 
dt
;

carState
.
angle
 
+=
 
carState
.
steer
 
*
 
carState
.
speed
 
*
 
CAR
.
turnSpeed
 
*
 
dt
;

Enter fullscreen mode

Exit fullscreen mode

If you're adding or subtracting a value per frame, multiply it bydt. Done.

### Pattern 2: Exponential decay:

Math.pow(factor, dt)

This one is less obvious. When driving off-road, the car slows down using a multiplier applied each frame:

// ❌ Frame-rate dependent

carState
.
speed
 
*=
 
0.97
;
 
// 3% drag per frame

Enter fullscreen mode

Exit fullscreen mode

At 165fps this applies 3% drag 165 times per second. At 30fps, only 30 times. The off-road drag behaves completely differently depending on hardware.

The naive fix:carState.speed *= 0.97 * dtiswrong.You can't linearly scale a multiplier. Atdt = 2you'd get0.97 * 2 = 1.94, which wouldacceleratethe car instead of slowing it down.

The correct fix uses exponentiation:

// ✅ Frame-rate independent

carState
.
speed
 
*=
 
Math
.
pow
(
0.97
,
 
dt
);

Enter fullscreen mode

Exit fullscreen mode

Why does this work? Repeated multiplication is exponential decay. Consider what happens over one second:

At 60fps (dt = 1, 60 frames):

speed after 1s = speed × 0.97^60

Enter fullscreen mode

Exit fullscreen mode

At 30fps (dt = 2, 30 frames):

speed after 1s = speed × (0.97^2)^30 = speed × 0.97^60 ✅ identical

Enter fullscreen mode

Exit fullscreen mode

Math.pow(factor, dt)correctly scales the decayexponentrather than the multiplier itself. The result over any given real-world time is always the same.

The same pattern applies to smooth steering interpolation, instead of a fixed lerp coefficient, it uses the same exponential trick:

// ❌ Frame-rate dependent

carState
.
steer
 
+=
 
(
steerDir
 
-
 
carState
.
steer
)
 
*
 
0.1
;

// ✅ Frame-rate independent

carState
.
steer
 
+=
 
(
steerDir
 
-
 
carState
.
steer
)
 
*
 
(
1
 
-
 
Math
.
pow
(
0.9
,
 
dt
));

Enter fullscreen mode

Exit fullscreen mode

### Pattern 3: Lerp smoothing

1 - Math.pow(1 - alpha, dt)

The trickiest one. The camera smoothly follows the car usinglerp:

// ❌ Frame-rate dependent

camera
.
position
.
lerp
(
targetPos
,
 
0.08
);

Enter fullscreen mode

Exit fullscreen mode

lerp(target, alpha)movesalphapercent of the remaining distance each frame. At 165fps the camera takes 165 small steps per second - buttery smooth. At 30fps it takes 30 steps - sluggish, visibly lagging.

Again,alpha * dtis the wrong fix. Atdt = 2you'd getalpha = 0.16, which changes the feel, and at high enough values it would overshoot the target entirely.

The correct formula:

// ✅ Frame-rate independent

camera
.
position
.
lerp
(
targetPos
,
 
1
 
-
 
Math
.
pow
(
1
 
-
 
0.2
,
 
dt
));

Enter fullscreen mode

Exit fullscreen mode

Here's the intuition. Afternlerp steps at factoralpha, the remaining distance is:

remaining = (1 - alpha)^n

Enter fullscreen mode

Exit fullscreen mode

To make this time-independent, you want the same remaining distance afternframes atdt=1as aftern/2frames atdt=2. The solution is to raise(1 - alpha)to the power ofdt:

adjusted_alpha
 
=
 
1
 
-
 
(
1
 
-
 
alpha
)
^
dt

Enter fullscreen mode

Exit fullscreen mode

Plugging in the numbers:

* Atdt = 1.0(60fps baseline):1 - 0.8^1.0 = 0.200- original feel ✅
* Atdt = 0.36(165fps):1 - 0.8^0.36 ≈ 0.083- smaller steps, same tracking speed ✅
* Atdt = 2.0(30fps):1 - 0.8^2.0 = 0.360- larger steps, same tracking speed ✅

The camera now follows the car at the same real-world speed on any display.

## Summary: The Three Patterns

Situation

Frame-rate dependent

Frame-rate independent

Add/subtract per frame

value += rate

value += rate * dt

Multiply per frame (decay)

value *= factor

value *= Math.pow(factor, dt)

Lerp toward target

lerp(target, alpha)

lerp(target, 1 - Math.pow(1-alpha, dt))

## One More Thing: Re-tune Your Constants

After making physics frame-rate independent at a 60fps baseline, my original constants felt wrong, they were implicitly tuned for 165fps. I had to re-tune them fordt = 1:

// Before (accidentally tuned for 165fps)

maxSpeed
:
 
0.42
,

acceleration
:
 
0.0006
,

brakeForce
:
 
0.0015
,

friction
:
 
0.00005
,

// After (tuned for dt = 1 baseline at 60fps)

maxSpeed
:
 
1.155
,

acceleration
:
 
0.004538
,

brakeForce
:
 
0.011344
,

friction
:
 
0.000378
,

Enter fullscreen mode

Exit fullscreen mode

If you're migrating an existing game, expect to spend time re-tuning. The physics will now be consistent across hardware, but the feel may shift from what you were used to on your own monitor.

## Pull Request

Check out the pull request for this bug fix:

Click Here to Check Out the Pull Request

## The Takeaway

If you're building a game or animation loop withrequestAnimationFrame, assume nothing about frame rate. Your players are on everything from 30fps integrated graphics to 240Hz gaming monitors.

The fix isn't too complicated, but it's also not just "multiply everything bydt." Linear operations, exponential decay, and lerp smoothing each need their own treatment. Get all three right and your game will feel identical whether it runs on a decade-old laptop or a high-refresh gaming rig.

My car now drives the same on every machine. And I learned far more about frame-rate-independent math than I expected from what looked like a simple bug.

Enjoyed this deep dive? Let's stay connected!

I share more software engineering insights, projects, and experiments across these platforms:

* 💼Connect with me on LinkedIn
* 💻Explore my projects on GitHub
* 💬Follow me on X
* 🎥Watch my videos on YouTube

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse