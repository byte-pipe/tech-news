---
title: Don't animate height! | Granola
url: https://www.granola.ai/blog/dont-animate-height
site_name: hackernews
fetched_at: '2025-07-23T07:05:28.961925'
original_url: https://www.granola.ai/blog/dont-animate-height
author: birdculture
date: '2025-07-23'
published_date: '2025-01-29'
---

# Don't animate height!

Jim Fisher

January 29

Our app was mysteriously using 60% CPU and 25% GPU on my M2 MacBook.
It turned out this was due to a tiny CSS animation!
In this post,
I show how to find expensive animations,
why some are so expensive,
and how to make many animations much cheaper.
Along the way,
we'll learn how the browser renders CSS animations
and how to use Chrome's dev tools for performance profiling.

## The problem

While buildingGranola, a note-taking app,
I noticed it was using 60% CPU and 25% GPU on my M2 MacBook:

Activity Monitor showing high CPU and GPU usage

What is Granola spending those cycles on?
It's an Electron app, so let's use the Chrome dev tools to find out!

First, in the "Performance" tab, we see thatmost of the time is spent not in JavaScript, but in "rendering" and "painting":

Butwhatis it rendering and painting?
To see this, open the "Layers" tab, which shows:

Our window has two layers:
one for the "action bar" at the bottom,
and another for the rest of the document content.
Each layer has a "paint count", andthe action bar's layer is painting every single frame!

Paint flashing (green) and layout shift regions (blue). Dev tools warns
that these animations "may not be suitable for people prone to
photosensitive epilepsy."

Why is the action bar painting so much?
For a clue, jump to the "Rendering" tab,
and turn on "paint flashing" and "layout shift regions".
We quickly seethe browser hates our audio volume visualizer!Those three green "dancing bars" at the bottom of the Granola window
constantly flash with layout shift and repainting.

But why are the dancing bars causing so much layout calculation?
My first suspicion was DOM updates:
the bars' styles update 10 times per second,
and DOM updates are expensive, right?
Butreducing DOM updates made little difference.

Back to the Performance tab,
and we see this pattern dominating the profile:

That stuff happens once for every frame, 60 times per second.No JavaScript here — this is pure CSS work!

Why is it doing work every frame?
The answer is in the image.
Look at those three purple "Animation" jobs.
There's one animation job for each dancing bar.
We've found our culprit,
and it's this line of CSS:

transition
:

height

300ms

ease
-
in
-
out
;

Why is thisheighttransition so expensive?
What is the browser doing when we animate theheightproperty?
We first need to understandthe browser's rendering pipeline.There are three relevant steps:Layout(deciding where elements go on the page), thenPainting(drawing those elements onto layers like in Photoshop), and finallyCompositing(merging those layers into a single image).

Here's the browser rendering one frame of Granola:

What happens when we change theheightproperty?
It triggers a layout recalculation, followed by re-painting, and re-compositing.
This makesheightalayout property,
and these are the most expensive CSS properties to animate.

The W3C spec is full of these!

Less expensive arepaint properties.
A paint property does trigger layout,
but it does repaint a layer, and then re-composites.
For example, thefillandstrokecolors on an SVG are paint properties:
they repaint the layer with new colors, then re-composite them.
A funny example is this tiny "bikeshed" SVG
which you can find onlots of W3C spec pages.
It costs ~30% CPU!

The cheapest properties arecomposite properties.
They don't trigger layout or paint;
they only trigger a compositing update.The two classic composite properties aretransformandopacity.Can we replace our expensiveheightanimations with cheapertransformanimations?

## A solution

Naive solution, with warped rounded corners.

A naive solution would be to replaceheightanimations withtransform:scaleY().
And hey presto, this fixes our performance problem!
The "Layout" and "Paint" jobs are nowhere to be seen in the Performance tab.

... Unfortunately, thisscaleYtransform isugly.
Look how those rounded corners get warped as the rectangle stretches!

Instead,
we can create the illusion of a changing height by usingtworectangles, applyingtranslateto each.
There's one rectangle for each end:

The bars are actually pairs of rounded rectangles that move in opposite directions,
creating the illusion of a single stretching bar.
Since we're only usingtransform,
the browser can skip the layout and paint phases.

Here's the optimized version of the visualizer:

Granola audio visualizer, after optimization.

On my M2 MacBook,
the renderer process is now using 6% CPU (down from 15%),
and the GPU process is now using 6% CPU and less than 1% GPU (down from 25% and 20%).
This optimization demonstrates
how understanding the browser's rendering pipeline
and choosing the right CSS properties for animations
can dramatically improve performance.
In the next post,
I'll show how to find hidden performance costs using Chrome'sabout://tracingtool,
which is like the performance profiler on steroids.
See you there!

You can see the optimized visualizer in action bytrying Granola.
If you're interested in working on performance optimizations like these,we're hiring!

Jim Fisher,Founding Engineer
