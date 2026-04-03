---
title: How to Create Never-Ending Fun (🎢RollerCoaster.js + React Three Fiber + AI) - DEV Community
url: https://dev.to/webdeveloperhyper/how-to-create-never-ending-fun-rollercoasterjs-react-three-fiber-ai-57c5
site_name: devto
fetched_at: '2026-01-04T11:06:36.787183'
original_url: https://dev.to/webdeveloperhyper/how-to-create-never-ending-fun-rollercoasterjs-react-three-fiber-ai-57c5
author: Web Developer Hyper
date: '2025-12-29'
description: 'Update (2025/12/30): Added Roller Coaster Nightmare😨 Intro When do you feel excited and... Tagged with ai, webdev, css, svelte.'
tags: '#ai, #webdev, #css, #svelte'
---

Update (2025/12/30): AddedRoller Coaster Nightmare😨

## Intro

When do you feel excited and fun? Nowadays, I am totally into trying the latest and trending IT technology. But when I was a child, I thought riding a roller coaster was quite fun and exciting.🎢 However, a roller coaster ends instantly, like a momentary dream. So, I created code that let us enjoy the roller coaster excitement forever at home!🚀

## RollerCoaster.js🎢

I found a perfect library for this plan. It is theRollerCoaster.js. What a niche library it is. There is an example of this library on the officialThree.jswebsite (most popular 3D library).Roller Coaster Demo ↓https://threejs.org/examples/webxr_vr_rollercoaster.htmlGitHub repository of Roller Coaster Demo ↓https://github.com/mrdoob/three.js/blob/master/examples/webxr_vr_rollercoaster.htmlAlso, this is the GitHub repository of RollerCoaster.js. ↓https://github.com/mrdoob/three.js/blob/master/examples/jsm/misc/RollerCoaster.jsThe main funcion of this library isRollerCoasterGeometry, and you can use it to easily create realistic roller coaster tracks. ↓https://threejs.org/docs/#RollerCoasterGeometry

## Roller Coaster

I created a roller coasterCodePensample with beginner-friendly comments with the help of AI. I trimmed the code from the officialThree.jssample to make it easier for beginners to understand. I usedReact Three Fiberto handle 3D animation. It is a wrapper ofThree.js, making it easier to use withReact.

One of the fun points of this animation is that the roller coaster speeds up when going down and slows down when going up. You can adjust the speed in this part of the code. ↓

// Clamp velocity between min and max (prevent too slow or too fast)

velocityRef
.
current

=

Math
.
max
(
0.00004
,

Math
.
min
(
0.0002
,

velocityRef
.
current
));

Enter fullscreen mode

Exit fullscreen mode

You can also adjust the course. The course shape is controlled byparametric equationsusing sine and cosine:

const

x

=

Math
.
sin
(
t

*

3
)

*

Math
.
cos
(
t

*

4
)

*

50
;

const

y

=

Math
.
sin
(
t

*

10
)

*

2

+

Math
.
cos
(
t

*

17
)

*

2

+

5
;

const

z

=

Math
.
sin
(
t
)

*

Math
.
sin
(
t

*

4
)

*

50
;

Enter fullscreen mode

Exit fullscreen mode

The number aftert *controls the Frequency (how many waves/loops):

* Higher frequency = More waves/loops → More complicated track
* Lower frequency = Fewer waves/loops → Smoother simpler track
Example for Y (vertical movement):

const

y

=

Math
.
sin
(
t

*

10
)

*

2
;

// 10 ups and downs per loop

const

y

=

Math
.
sin
(
t

*

2
)

*

2
;

// Only 2 ups and per loop

Enter fullscreen mode

Exit fullscreen mode

Think of It like this:Imagine you start with a simple circular course (like a race track). Then:

1. X equation adds horizontal twists (left-right weaving)
2. Y equation adds vertical hills (up-down movement)
3. Z equation adds depth curves (forward-back spiraling)
So, higher frequencies make more complex patterns.

## Roller Coaster Rainbow🌈

OK. Let's make the roller coaster more fun and exciting!😆 I changed the track color to a rainbow, and made the background to space with colorful stars. I added a CSSlinear-gradientto create a base space atmosphere, andradial-gradientto create a fog atmosphere. ↓

/* 🌌 DEEP SPACE BASE - Simple black to dark purple gradient */

background
:

linear-gradient
(
to

bottom
,

#000000

0
%,

#0
d0019

100
%);

Enter fullscreen mode

Exit fullscreen mode

/* VIGNETTE: Dark edges fade to transparent center
 - Creates depth and atmospheric "fog" effect
 - Very dark with subtle purple hint (10, 0, 20) = almost black
 - 0.4 opacity = subtle, professional atmosphere
*/

background
:

radial-gradient
(


ellipse

at

center
,


transparent

0
%,


transparent

40
%,


rgba
(
10
,

0
,

20
,

0
.
4
)

100
%

);

Enter fullscreen mode

Exit fullscreen mode

You can adjust the number of stars by changing the "i". ↓

for
(
let

i

=

0
;

i

<

500
;

i
++
)

{

Enter fullscreen mode

Exit fullscreen mode

You can also adjust the size of the stars by changing the "size". ↓

const

size

=

Math
.
random
()

*

0.5

+

0.3
;

// Random size 0.3 to 0.8

Enter fullscreen mode

Exit fullscreen mode

Doesn't it look like a dream roller coaster? Making the stars more numerous and larger creates a quite different atmosphere for the course. ↓

## Roller Coaster Nightmare😨

I made a nightmare version of the roller coaster. I increased the values of all thet *parts, adding more ups and downs and tighter curves to create a crazy, extreme course. In addition, I increased the speed to make it even more thrilling. I also changed the track to a red-to-black gradient and changed the CSS gradient to make the center bright and the edges dark for a spooky effect.

## Svelte

Also, I made aSvelteversion for study. I usedThreltefor handling 3D. It is a wrapper ofThree.jsfor easy use withSvelte.Sveltehas many advantages overReactsuch as,simple and less code, smaller bundle size, and better performance.

<!-- Svelte -->

// Declare state
let velocity = 0.00004;
// Update state
velocity += 0.001; // Just assign!

Enter fullscreen mode

Exit fullscreen mode

// React

// Declare state

const

[
velocity
,

setVelocity
]

=

useState
(
0.00004
);

// Update state

setVelocity
(
v

=>

v

+

0.001
);

// Need setter function

Enter fullscreen mode

Exit fullscreen mode

I wanted to make aCodePensample of both default and rainbow roller coaster to compare the difference betweenSvelteandReact. However, I couldn't useThrelteinCodePen, so next I triedStackBlitz.Threlteworked there, but it takes time forStackBlitzto start... Anyway, I will paste the code.Roller Coaster Default ↓

Roller Coaster Rainbow ↓

## Future update ideas

Using these code as a base, I have some future update ideas.😆

* Add more animation to roller coaster and stars.
* Add more physics to roller coaster and stars.
* Making an UI that lets you create your own track visually without touching the code.

## More about animation and AI

I wrote about 2D/3D animation before, so please also refer to it for more information about 2D/3D animation. ↓

* ((Learn with 🖼️Meme images) How to create 🎨3D animation using 🧠AI (React Three Fiber vs Three.js vs A-Frame + GSAP)
* (🧐I created a website animation that you might stare at for a while (GSAP)🎨)

Also, here are my posts about AI ↓

* (🧠How to make Codex boost your mood like good old Claude Code (Getting back You're absolutely right!)🤖
* (🤖🤖How to run AI in parallel easily and for free (Git Worktree Runner)🧠🧠
* (🤖How to make AI follow your instructions more for free (OpenSpec)📝
* (🧠How to use AI more efficiently for free (Serena MCP)🧐

## Outro

Riding a roller coaster is fun and exciting. I cannot ride a real roller coaster endlessly, but now I can ride a virtual roller coaster endlessly. Making animation is super fun, and I would love to learn more!😊

I hope you learned something from this post. Thank you for reading.Happy AI coding!🧠You're absolutely right!🤖

Do you have any good ideas for 2D/3D animation?Do you know anything about 2D/3D animation?I would love to hear your thoughts!⬇️⬇️

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
