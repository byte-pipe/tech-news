---
title: Simulating Hand-Drawn Motion with SVG Filters - Camillo Visini
url: https://camillovisini.com/coding/simulating-hand-drawn-motion-with-svg-filters
site_name: hackernews
fetched_at: '2025-07-22T01:05:47.792973'
original_url: https://camillovisini.com/coding/simulating-hand-drawn-motion-with-svg-filters
author: camillovisini
date: '2025-07-22'
description: A practical guide to implementing the boiling line animation effect using SVG filter primitives and JavaScript - Blog post by Camillo Visini
---

# Simulating Hand-Drawn Motion with SVG Filters



## A practical guide to implementing the boiling line animation effect using SVG filter primitives and JavaScript




Published on


 July 09, 2025






Ever wondered how cartoons create that hand-drawn “jitter” effect? I recently watched anARTE documentaryabout Neapolitan pizza and was fascinated by the animated illustrations (drawn in simple shapes and plain colors) that accompanied thesegmentwhere the recipe and its ingredients were presented. The illustrations were static, but they had a subtle animation effect that made them look like they were moving slightly.

See for example in this short clip, where you can see the ingredients being presented (pay attention to the edges of the shapes):





 Animated illustration of ingredients for Pizza Napoli - Source: ARTE


I was curious to find out how this effect might have been achieved. First, I had to find out what it was called – turns out that this specific effect is actually quite common in cartoon-style animations and illustrations.

After some research, I found out that this effect is called“boiling”orline boiland was traditionally achieved by drawing the same frame multiple times in a row, with slight variations in position and rotation. This creates the illusion of movement in an otherwise static scene. The technique is often used in animation to create a more dynamic and engaging visual experience (instead of just a static image or scene, for example when a character is standing still).

Let’s take a look at a simple example of this effect in the demo below. I have traced the same object multiple times. Naturally, as these drawings are tracings by hand and not perfect copies, there are subtle differences between them. But, this becomes only apparent when the drawings are overlaid and animated!

When looking closely at the initial short clip, you will notice that the effect is more of a trick. There seems to be a layer of a rough paper-like texture with some kind of overlay effect that is applied to the whole scene, giving it a dynamic quality. That’s not the part we will focus on, though.

More interestingly, the edges of the shapes seem to wobble slightly and appear gritty or sketch-like, as if they were drawn by hand. But are they drawn by hand, as in my demo above? I don’t think that’s the case, because the contours are wobbling “in a loop”. Or in other words: The boiling effect is somehow achieved artificially: Rather than by drawing the same frame multiple times with slight variations, it seems to be a post-processing effect applied to the static illustrations, which were likely drawn as “perfect” shapes.

This blog post describes my attempt to recreate this effect in a simple way and bring it to the web. Let’s dive in.

## Decomposing the effect

To recreate the boiling effect, we can break it down into two main components:

* Distorting the edges: The edges of the shapes should not be perfectly straight, but rather have a slight wobble that gives them a more organic and hand-drawn look. This could be achieved by applying a distortion effect to the edges of the shapes – which could be controlled by a set of parameters.
* Animating the effect: Then, thesedistortion parametersare animated over time (for example, updated with new values every 200 milliseconds), creating a subtle movement that makes an otherwise static scene feel more engaging.

Probably, the second part is intuitive to understand, but the first part is a bit more complex. Because we are trying to create this effect in a web context, we will useSVG filter effectsfor our approach (step 1). What follows is that we can then easily manipulate (and therefore animate) the properties of these filter effects using JavaScript (step 2). But how do these SVG filter effects work, exactly? Let’s take a closer look.

## SVG filter effects

SVG filter effectsallow us to apply various visual effects to SVG elements, such as blurring, color manipulation, and distortion. In our case, we will use a combination of thefeTurbulenceandfeDisplacementMapfilter primitives to create the boiling effect.

Conceptually, theTurbulence Fieldgenerates a noise texture that can be used to distort the edges of the shapes. TheDisplacement Mapthen uses this noise texture to displace the pixels of the original image, creating the desired distortion effect. See this visualization:











 Turbulence + Displacement: How SVG filter effects work together to create the distortion effect



Additionally, I’ve created a demo that let’s you explore the interplay of these two filter effects. You can move the layers to see how the distortion changes at the intersection of the two filter effects. Note: The demo contains some added elements and visual indicators for demo purposes and easier understanding.

The above demo illustrates how the distortion effect is applied to the image. Let’s take a closer look at how to set up the SVG filter effects in terms of code.

<
svg
 width
=
"400"
 height
=
"400"
 viewBox
=
"0 0 400 400"
>

 <
defs
>

 <
filter
 id
=
"distortionFilter"
>

 <!-- Step 1: Create a turbulence field to generate noise -->

 <
feTurbulence

 type
=
"turbulence"

 baseFrequency
=
"0.03"

 numOctaves
=
"2"

 seed
=
"1"

 result
=
"noise"

 />



 <!-- Step 2: Use the noise (in2) to displace the image (in) -->

 <
feDisplacementMap

 in
=
"SourceGraphic"

 in2
=
"noise"

 scale
=
"20"

 xChannelSelector
=
"R"

 yChannelSelector
=
"G"

 />

 </
filter
>

 </
defs
>



 <!-- Step 3: Apply the filter to the image -->

 <
image

 x
=
"0"
 y
=
"0"
 width
=
"400"
 height
=
"400"

 href
=
"/image.jpg"

 filter
=
"url(#distortionFilter)"

 />

</
svg
>

The code shown above applies a filter that distorts an image using procedural noise.feTurbulencegenerates the noise texture, andfeDisplacementMapuses it to offset the image pixels (more specifically, for thex-axis, the red channel, and they-axis, the green channel). The result is a subtle warping effect applied to the image. For now, the parameters of the filter are static, but we can animate them to create the boiling effect. The real magic happens there!

## Animating the effect

Now that we know how to apply the effect to an image, we can additionally animate the parameters of the filter using JavaScript. The key is to update the various attributes of the SVG filter effects at regular intervals, creating a dynamic distortion effect that simulates the boiling motion that we are looking for.

Here’s an interactive demo that shows the original image and the animated boiling effect applied to it. You can control the parameters of the effect. Use the dropdown to choose from some sample images. I created these simple illustrations as raster images, but SVG filter effects can also be applied to, you guessed it, SVG images. The result is identical.

Here’s what the animation scale slider does. We begin with abaseFrequencyof0.02and a small list of offsets that we define:[-0.02, 0.01, -0.01, 0.02]. Every100ms, we take the next offset, multiply it by the slider value, and add the result to that base. With the slider at0.5the first tick becomes0.02 + (-0.02 × 0.5), resulting in thebaseFrequencybeing set to0.01. The wobble appears gentle in this tick or frame. Set the slider to1and you will see the full±0.02wobble changes between frames. If you set it to0, there’s no wobble.

Here’s a full scene. The parameters are the same as the initial parameters in the previous demo (use the reset button to restore their values).

Nice! With just two humble filter primitives and a bit of JavaScript, we’ve turned boring shapes into something that feels alive, simulating the warmth and imperfections found in hand-drawn animation styles.

## Conclusion

In short, the “boiling” effect boils down to a procedural noise field (feTurbulence) fed into a displacement map (feDisplacementMap), whose parameters we shuffle every few milliseconds in JavaScript. By decomposing the problem into distortion and animation and wrapping the whole thing in SVG filters, we get an effect that lets us bring this effect to the web, and bring static illustrations to life.

The interactive demos I created (which was pretty fun to do so, I must admit!) show how small tweaks to the base frequency, displacement scale and animation scale can shift the mood from a subtle jitter to an extreme and annoying wobble, which leaves the original image’s shapes barely recognizable. A little goes a long way here: Don’t let things boil over. Now it’s your turn and try it out yourself!

By the way, you can findmore recipesfrom the ARTE series, all of which contain animations of this style. Unfortunately, even after searching for quite a while, I could not find out whom to give (well deserved) credits to for creating these cool illustrations in this documentary series.

I hope you enjoyed this little excursion into the world of “hand-drawn” motion effects and SVG filter primitives. If you have any questions or feedback, feel free to reach out.






Find me on...



LinkedIn


 LinkedIn


GitHub


 GitHub


X/Twitter


 X/Twitter


BlueSky


 BlueSky


Mastodon


 Mastodon








Sign up for my personal newsletter



Enter your email address below in order to receive an email when I write a
 new article:












Subscribe






Note:
 You can unsubscribe at any time by clicking
 on the unsubscribe link included in every email.
















Camillo Visini


CEO & Founder ·

Visini AG








Published on


 July 09, 2025




Share Article
