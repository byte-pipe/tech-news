---
title: Lindenmayer Systems
url: https://justinpombrio.net/2026/02/16/l-systems.html
site_name: lobsters
content_file: lobsters-lindenmayer-systems
fetched_at: '2026-02-21T06:00:40.222580'
original_url: https://justinpombrio.net/2026/02/16/l-systems.html
date: '2026-02-21'
tags: art, math
---

# Justin Pombrio

### About Me

* WPI Transcript
* Brown Transcript
* Friends
* Pictures
* Resume

### Archive

* Blackout
* Faster Than Light
* Hex Board
* Invariants
* Listening To OEIS
* Logic Gates
* Penrose Maze
* Syntactic Sugar
* Terminal Colors

### Notes

* JJ Cheat Sheet
* Rust Quick Reference
* Notes on Concurrency

### Puzzles

* There and Back Again
* The Prisoners' Lightbulb

### Tree Editors

* Tree Editor Survey

### Programming

* Typst as a Language
* A Twist on Wadler's Printer
* Preventing Log4j with Capabilities
* Algebra and Data Types
* Pixel to Hex
* Linear vs Binary Search

### Physics

* Uncalibrated quantum experiments act clasically

### Math

* Lindenmayer Systems
* Traffic Engineering with Portals, Part II
* Traffic Engineering with Portals
* Algebra and Data Types
* What's a Confidence Interval?

### PL Design

* Imagining a Language without Booleans

* Lindenmayer Systems
* Imagining a Language without Booleans
* JJ Cheat Sheet
* Typst as a Language
* A Twist on Wadler's Printer
* Space Logistics
* Hilbert's Curve
* Preventing Log4j with Capabilities
* Traffic Engineering with Portals, Part II
* Traffic Engineering with Portals
* Algebra and Data Types
* What's a Confidence Interval?
* Uncalibrated quantum experiments act clasically
* Pixel to Hex
* Linear vs Binary Search
* There and Back Again
* Tree Editor Survey
* Rust Quick Reference
* The Prisoners' Lightbulb
* Notes on Concurrency
* It's a blog now!

# Lindenmayer Systems

Let me show you how to use Lindenmayer systems to produce beautiful images like
this one:

### Turtles

We’ll start by talking about turtles.

Some of you are nodding along like this is an obvious starting point; others
are rather confused. In 1967(!) some brilliant engineers designed an
educational programming language calledLogo. It lets you
maketurtle graphicsdrawings
by telling a “turtle” with a “pen” where to walk on the screen, drawing a line
as it goes. I just learned when writing this that there were alsophysical
programmable turtlesthat would
draw on paper!

So yeah, we’re startings with turtles. Logo turtles had all sorts of fancy
commands, but ours will need just three:

* fmeans “walk forward one unit”
* -means “turn left a quarter turn”
* +means “turn right a quarter turn”

The turtle starts in the center of the screen facing up. So the program-f+ffwill drawn an “L”:

The turtle’s path is drawn as a gradient from white to yellow to green. If you
have an active imagination you can pretend that the green dot at the end is a
turtle.

And the programf+f--f+f+fwill draw an “F”:

### Angles

What if you want your turtle to turn at angles other than a quarter turn? We
could go the route that Logo did, and give an arbitrary angle for every turn.
But for the sorts of drawing we’re going to do we can get away with something
simpler: we’ll declare up front what angle-and+should turn. (Measured inturns, of course.)

For example, to draw a hexagon we could use the angle 1/6 and run the turtle
programf+f+f+f+f+f+:

### Aristid Lindenmayer

Drawing a detailed image this way would take a really long sequence of-,+, andf. Again, Logo solved this in a general way by adding loops to the
language, but we’re going to do something a lot more specialized. We’re going to
use an idea by Aristid Lindenmayer in 1968, now called “Lindenmayer Systems” or
“L-Systems”.

(This timing—Logo in 1967 and L-Systems in 1968—is suspicious, isn’t it? I’m
not aware of any explicit cross-polination of ideas between Lindenmayer and the
Logo creators, but wouldn’t be surprised if one partially inspired the other.)

Lindenmayer’s idea is to have astart string, and someproduction rulesthat
replace a letter with a sequence of instructions. You start with thestart
stringand repeatedly replace letters according to theproduction rulesfor
some number of iterations. Then you have the turtle follow the (now very long)
sequence of instructions.

This will be easier to follow with an example.

One pretty picture that can be drawn with an L-system is thedragon curve. Its
rules are:

start: R
productions:
 R -> Rf+L
 L -> Rf-L
angle: 1/4

Iterations of the dragon curve look like this:

* The 0th iteration starts with thestartstring, so it’s justR.
* The 1st iteration replaces thatRaccording to the production ruleR -> Rf+L, so it becomesRf+L.
* The 2nd iteration replaces both theRandLaccording to the production
rules, givingRf+Lf+Rf-L.
* And so on.

We get to choose how many iterations to do. Let’s say we do 9 iterations. Then
we get:

Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-
Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-
Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-
Rf+Lf+Rf-Lf+Rf+Lf-Rf-Lf+Rf+Lf+Rf-Lf-Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf+
Rf+Lf-Rf-Lf-Rf+Lf+Rf-Lf-Rf+Lf-Rf-L

Now we just need to tell the turtle to follow these instructions. But… what’s
it supposed to do with all theRs andLs? Simple: it will just ignore them.
Erasing them from the string gives:

f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f-f+f+f-f-f+f-
f-f+f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f-f+f+f-f-
f+f-f-f+f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f-f+f+
f-f-f+f-f-f-f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f-
f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f+f+f+f-f+f+f-
f-f-f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f-f+f+f-f+
f+f-f-f-f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f+f+f+
f-f+f+f-f-f-f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f-
f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f+f+f+f-f-f+f-
f-f+f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f+f+f+f-f-
f+f-f-f-f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f+f+f+
f-f-f+f-f-f+f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f+
f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f-f+f+f-f+f+f-
f-f+f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f+f+f+f-f+
f+f-f-f+f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f-f+f+
f-f+f+f-f-f+f+f+f-f-f+f-f-f+f+f+f-f+f+f-f-f-f+f+f-f-f+f-f-f-
f+f+f-f+f+f-f-f+f+f+f-f-f+f-f-f-f+f+f-f+f+f-f-f-f+f+f-f-f+f-
f-

If we tell our little turtle to follow those instructions, it will draw:

What happens if we go further? After about 22 iterations (producing about 8
million instructions), the turtle is making turns smaller than a pixel on the
screen, so the path it took is no longer directly visible: you just see the
color gradient it was drawn with. Adding more iterations after that doesn’t make
the image look any different (beyond rotating), it has stabilized. It looks like
this:

### Code

I implemented all this as a Rust library. Here’s the code for that dragon curve:

LindenmayerSystem {
 start: "R",
 rules: &[('R', "Rf+L"), ('L', "Rf-L")],
 angle: 0.25,
 implicit_f: false,
}

The extra fieldimplicit_ftells the turtle what to do with leftover letters
likeLandRin the expanded program. For the dragon curve, like I said
above, we should just erase them. But sometimes it’s more convenient to replace
them withf; settingimplicit_f: truewould do so.

(There’s a math question here: can you express any L-system withimplicit_f:
trueas an L-system withimplicit_f: falseand vice-versa? I don’t know the
answer.)

Here are a couple more L-systems, to give you a sense what they look like. First
David Hilbert’s space filling curve:

LindenmayerSystem {
 start: "A",
 rules: &[('A', "+Bf-AfA-fB+"), ('B', "-Af+BfB+fA-")],
 angle: 0.25,
 implicit_f: false,
}

Which looks like this, at 5 iterations:

And here’s Helge von Koch’s snowflake, at 3 iterations:

LindenmayerSystem {
 start: "X-X-X-X-X-X",
 rules: &[('X', "X-X++X-X")],
 angle: 1.0 / 6.0,
 implicit_f: true,
}

### Gradient

So far all the pictures have been drawn with the same color gradient, but you
might want to use others. The gradients I’ve implemented fall into three
categories:

* CET perceptually uniform color maps.
These are color gradients designed to beperceptually
uniform.
The gradient used in all the examples so far is CET-L10.
* Color gradients built out of combinators for things like scaling, cycling, and
sawtoothing. These are all inOK-LABcolor space.
* A very fancy color gradient based on the 3D Hilbert curve. The idea is to (i)
draw a cube in OK-LAB color space; (ii) trace a 3D Hilbert curve through the
cube; (iii) dye the curve according to the cube’s colors; then (iv) straighten
the curve and then lay it out on the curve that you’re drawing.

The last approach makes for very textured pictures since the 3D Hilbert curve
changes color so quickly. (It covers all the colors on the cube, which is most
possible colors.) For example, here’s the dragon curve with a 3D-Hilbert curve
color gradient:

### Pretty Pictures

Putting this all together, you can draw some very pretty pictures.

A curve fromJ. Arioni in
2017:

A haphazard curve I made that’s pretty nonetheless:

Moore’s curve:

An “s curve” of my devising:

A curve fromDieter K. Steemann on
Pinterest:

Wunderlich’s third space filling curve:

Sierpinski’s triangle:

Sierpinski’s space filling curve:

### Repository

The code that generated these images is athttps://github.com/justinpombrio/lindenmayer. Feel free to play around with it! I’m especially interested if anyone knows of interesting space-filling curves that I’ve missed.

A couple blocks from where I live, about a year ago, a PhD student at Tufts
university namedRümeysa
Öztürkwas taken by masked, plainclothes DHS officers and held at an ICE detainment
facility for six weeks for purely political reasons (she wrote apro-Palestine
op-edin 2024). Since
then, ICEused tear gas, unprovoked, on peaceful
protesterswhile in Portland against the wishes of the cities’ elected officials, and shotAlex
PrettiandRenée
Goodto death. The
weaponization of ICE and other federal agencies against those politically
opposed to the administration needs to stop.

February 16, 2026
