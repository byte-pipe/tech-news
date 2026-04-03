---
title: How I built a "Magic Move" animation engine for Excalidraw from scratch published - DEV Community
url: https://dev.to/behruamm/how-i-built-a-magic-move-animation-engine-for-excalidraw-from-scratch-published-4lmp
site_name: devto
fetched_at: '2026-01-13T11:07:42.659643'
original_url: https://dev.to/behruamm/how-i-built-a-magic-move-animation-engine-for-excalidraw-from-scratch-published-4lmp
author: Behram
date: '2026-01-12'
description: I love Excalidraw for sketching system architectures. But sketches are static. When I want to show... Tagged with react, animation, webdev, opensource.
tags: '#react, #animation, #webdev, #opensource'
---

I love Excalidraw for sketching system architectures. But sketches are static. When I want to show how a packet moves through a load balancer, or how a database shard splits, I have to wave my hands frantically or create 10 different slides.

I wanted the ability to"Sketch Logic, Export Motion".

## The Goal

I didn't want a timeline editor (like After Effects). That's too much work for a simple diagram.I wanted"Keyless Animation":

1. DrawFrame 1(The start state).
2. Clone it toFrame 2.
3. Move elements to their new positions.
4. The engine automatically figures out the transition.

I built this engine usingNext.js,Excalidraw, andFramer Motion. Here is a technical deep dive into how I implemented the logic.

## 1. The Core Logic: Diffing States

The hardest part isn't the animation loop; it's thediffing. When we move fromFrame AtoFrame B, we identify elements by their stable IDs and categorize them into one of three buckets:

1. Stable:The element exists in both frames (needs to morph/move).
2. Entering:Exists in B but not A (needs to fade in).
3. Exiting:Exists in A but not B (needs to fade out).

I wrote acategorizeTransitionutility that maps elements efficiently:

// Simplified logic from src/utils/editor/transition-logic.ts

export

function

categorizeTransition
(
prevElements
,

currElements
)

{


const

stable

=

[];


const

morphed

=

[];


const

entering

=

[];


const

exiting

=

[];


const

prevMap

=

new

Map
(
prevElements
.
map
(
e

=>

[
e
.
id
,

e
]));


const

currMap

=

new

Map
(
currElements
.
map
(
e

=>

[
e
.
id
,

e
]));


// 1. Find Morphs (Stable) & Entering


currElements
.
forEach
(
curr

=>

{


if
(
prevMap
.
has
(
curr
.
id
))

{


const

prev

=

prevMap
.
get
(
curr
.
id
);


// We separate "Stable" (identical) from "Morphed" (changed)


// to optimize the render loop


if
(
areVisuallyIdentical
(
prev
,

curr
))

{


stable
.
push
({

key
:

curr
.
id
,

element
:

curr

});


}

else

{


morphed
.
push
({

key
:

curr
.
id
,

start
:

prev
,

end
:

curr

});


}


}

else

{


entering
.
push
({

key
:

curr
.
id
,

end
:

curr

});


}


});


// 2. Find Exiting


prevElements
.
forEach
(
prev

=>

{


if
(
!
currMap
.
has
(
prev
.
id
))

{


exiting
.
push
({

key
:

prev
.
id
,

start
:

prev

});


}


});


return

{

stable
,

morphed
,

entering
,

exiting

};

}

Enter fullscreen mode

Exit fullscreen mode

## 2. Interpolating Properties

For the "Morphed" elements, we need to calculate the intermediate state at any givenprogress(0.0 to 1.0).

You can't just use simple linear interpolation for everything.

* Numbers (x, y, width):Linear works fine.
* Colors (strokeColor):You must convert Hex to RGBA, interpolate each channel, and convert back.
* Angles:You need "shortest path" interpolation.

If an object is at10 degreesand rotates to350 degrees, linear interpolation goes the long way around. We want it to just rotate -20 degrees.

// src/utils/smart-animation.ts

const

angleProgress

=

(
oldAngle
,

newAngle
,

progress
)

=>

{


let

diff

=

newAngle

-

oldAngle
;


// Normalize to -PI to +PI to find shortest direction


while
(
diff

>

Math
.
PI
)

diff

-=

2

*

Math
.
PI
;


while
(
diff

<

-
Math
.
PI
)

diff

+=

2

*

Math
.
PI
;


return

oldAngle

+

diff

*

progress
;

};

Enter fullscreen mode

Exit fullscreen mode

## 3. The Render Loop & Overlapping Phases

Instead of CSS transitions (which are hard to sync for complex canvas repaints), I used arequestAnimationFrameloop in a React hook calleduseTransitionAnimation.

A key "secret sauce" to making animations feel professional isoverlap.If you play animations sequentially (Exit -> Move -> Enter), it feels robotic.I overlapped the phases so the scene feels alive:

// Timeline Logic

const

exitEnd

=

hasExit

?

300

:

0
;

const

morphStart

=

exitEnd
;


const

morphEnd

=

morphStart

+

500
;

// [MAGIC TRICK] Start entering elements BEFORE the morph ends

// This creates that "Apple Keynote" feel where things arrive

// just as others are settling into place.

const

overlapDuration

=

200
;


const

enterStart

=

Math
.
max
(
morphStart
,

morphEnd

-

overlapDuration
);

Enter fullscreen mode

Exit fullscreen mode

## 4. Making it feel "Physical"

Linear movement (progress = time / duration) is boring.I implemented spring-based easing functions. Even though I'm manually calculating specific frames, I apply an easing curve to theprogressvalue before feeding it into the interpolator.

// Quartic Ease-Out Approximation for a "Heavy" feel

const

springEasing

=

(
t
)

=>

{


return

1

-

Math
.
pow
(
1

-

t
,

4
);


};

Enter fullscreen mode

Exit fullscreen mode

This ensures that big architecture blocks "thud" into place with weight, rather than sliding around like ghosts.

## What's Next?

I'm currently working on:

* Sub-step animations:Allowing you to click through bullet pointswithina single frame.
* Export to MP4:Recording the canvas stream directly to a video file.

The project is live, and I built it to help developers communicate better.

Try here:https://postara.io/

Free Stripe Promotion Code: postara

Let me know what you think of the approach!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
