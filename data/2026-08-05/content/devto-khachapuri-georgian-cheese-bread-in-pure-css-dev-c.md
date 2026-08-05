---
title: 'Khachapuri: Georgian Cheese Bread in Pure CSS - DEV Community'
url: https://dev.to/highflyer910/khachapuri-georgian-cheese-bread-in-pure-css-47o7
site_name: devto
content_file: devto-khachapuri-georgian-cheese-bread-in-pure-css-dev-c
fetched_at: '2026-08-05T20:40:06.987798'
original_url: https://dev.to/highflyer910/khachapuri-georgian-cheese-bread-in-pure-css-47o7
author: Thea
date: '2026-08-03'
description: This is a submission for Frontend Challenge - Comfort Food Edition, CSS Art. ... Tagged with frontendchallenge, devchallenge, css.
tags: '#frontendchallenge, #devchallenge, #css'
---

Frontend Challenge CSS Art Submission 🍲🥧

This is a submission forFrontend Challenge - Comfort Food Edition, CSS Art.

## Inspiration

When I think about comfort food, the first dish that comes to my mind is Imeretian Khachapuri (იმერული ხაჭაპური). It's a traditional cheese bread from the Imereti region in western Georgia. It has soft yeast dough with melted Imeruli cheese inside, baked until golden brown and brushed with butter after baking. Unlike pizza, the cheese is completely inside the dough. For me, khachapuri is more than food; it's warmth, home, and childhood memories. I wanted to recreate this fresh, steaming bread using only HTML and CSS.

## Demo

## Journey

### 1. Pure CSS

Every visible part, from the bread texture to the steam and slicing animation, is made only with HTML and CSS.No images, SVG, canvas, or JavaScript.

### 2. Slicing the Circle with clip-path Math

Instead of creating one full loaf and hiding it with overlays, I divided it into 13 slices, usingclip-path: polygon(). Thirteen slices were enough to make the bread disappear smoothly without adding too many HTML elements.

.khachapuri-slice
:nth-of-type
(
1
)
 
{
 

clip-path
:
 
polygon
(
50%
 
50%
,
 
38.01%
 
1.46%
,
 
61.99%
 
1.46%
);

animation
:
 
slice-cut-1
 
20s
 
linear
 
infinite
;
 

}

Enter fullscreen mode

Exit fullscreen mode

Each slice uses the same gradient layers, so together they look like one seamless loaf until the animation starts.

### 3. Layering the Oven-Baked Sheen

To recreate the look of freshly baked bread, I layered several radial gradients to create:

* Darker baked spots (rgba(135,65,20,.55))
* Toasted golden areas (#efb33d)
* A glossy highlight (rgba(255,245,170,.55)) to simulate fresh butter brushed over hot dough.

### 4. Magazine Layout with shape-outside

To make the layout feel more like a food blog, I wrapped the text around the plate using CSS shapes:

.khachapuri-frame
 
{

 
float
:
 
left
;

 
shape-outside
:
 
circle
(
48%
);

 
width
:
 
clamp
(
180px
,
 
24vw
,
 
320px
);

 
height
:
 
clamp
(
180px
,
 
24vw
,
 
320px
);

}

Enter fullscreen mode

Exit fullscreen mode

### 5. Accessibility & Polish

The slice animations respect@media(prefers-reduced-motion: reduce), so the dish stays as a whole loaf for users who prefer less motion. The closing line, გემრიელად მიირთვით!, is also marked with lang="ka" so screen readers can pronounce it correctly as Georgian.

გემერიელად მიირთვით!Enjoy your meal!❤️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse