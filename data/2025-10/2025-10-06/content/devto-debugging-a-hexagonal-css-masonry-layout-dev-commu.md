---
title: Debugging a Hexagonal CSS Masonry Layout - DEV Community
url: https://dev.to/ingosteinke/debugging-a-hexagonal-css-masonry-layout-483a
site_name: devto
fetched_at: '2025-10-06T11:07:33.718445'
original_url: https://dev.to/ingosteinke/debugging-a-hexagonal-css-masonry-layout-483a
author: Ingo Steinke, web developer
date: '2025-10-01'
description: Before CSS will eventually get an official masonry layout with or without grid, we can achieve... Tagged with webdev, javascript, css, design.
tags: '#webdev, #javascript, #css, #design'
---

Before CSS will eventually get an officialmasonry layoutwith or without grid, we can achieve something similar with flex and some scripting, provided that all bricks (or tiles) have the same size. Then we can move every second row towards the top right to fill the gaps between the spikes of the previous elements.

## A Seemingly Simple Styling Idea

Now, that's another seemingly simple use case that nobody seemed to care about before, probably for similar reasons as withparallax scrolling beyond landscape images, is a simplified masonry layout where all items have the same size and a hexagonal shape like tiles in a world-building game.

I initially thought that this could be a use case for CSS Grid, and I tried to figure out how to combine grid'sauto-flow,auto-fill(orauto-fit?) withmin-contentto achieve a flex-like auto-wrapping behavior.

I gave up as I saw that flex is still a simpler solution and grid didn't have what I thought it had: an option to style items depending on which row they were auto-placed in.

I almost gave up on my silly use case, but I was rewarded by the kind of errors only possible in visual frontend development, so let me take you on my journey of mathematical misconceptions step by step towards the following result.

That's how it looks in my demo atdev-ux-lesezeichen.denow.

Let's recap my steps and how not to do it.

## Polyfilling Auto-Placement Row Detection

We can let the browser auto-place items in columns and wrap them to new rows in a responsive way, but neither flex nor grid will tell us the row that an individual item has been placed into.

### Minding the Gaps

We don't need a rocket science degree to do the maths:

* row 1: top 0 = 0 * (height + gap)
* row 2: top 1 * height + 1 * gap = 1 * (height + gap)
* row 3: top 2 * height + 2 * gap = 2 * (height + gap)

The gap is a property of the flex or grid container.

const

verticalGap

=

getComputedStyle
(
layoutContainer
).
rowGap
;

Enter fullscreen mode

Exit fullscreen mode

All tiles have the same height, so we can query any tile just once (or use the expected height that we set in CSS). Adding height and gap, we know the inclusive height of one row.

let

gappedHeight

=

firstTile
.
offsetHeight

+

verticalGap
;

Enter fullscreen mode

Exit fullscreen mode

The container must be positioned, so we can useoffsetTopto measure the distance of each item's top to the parent's top.

We can detect which rows are odd (e.g. 1, 3, 5, ...) or even (2, 4, 6, ...) just like innth-child(odd)(and remember that CSS counts uses ordinal numbers starting from 1, not 0, so the first row will be an odd row number one.

This must be done for every item, and rerun after the window has been resized or a device was rotated.

const

wrappableElements

=

layoutContainer
.
children
;

for
(
const

wrappableElement

of

wrappableElements
)

{


const

tileElement

=

wrappableElement

as

HTMLElement
;


let

offsetRows

=

Math
.
floor
(
tileElement
.
offsetTop

/

gappedHeight
);


tileElement
.
classList
.
add
((
offsetRows

%

2
)

?

'
is-even
'

:

'
is-odd
'
);

Enter fullscreen mode

Exit fullscreen mode

I thought thatMath.floorjust eliminates possible sub-pixel anomalies, but it maybe it just hides a more fundamental problem. We will see in the debugging section below.

## Hexagonal Masonry Layout in Practice, Work in Progress

Some screenshots from experiment to proof of concept:

An early app preview reminded me of a sketch of an hourglass, before I ensured all items are equally sized and clip their content if it's too long.

Another intermediate situation, appropriately with the book "Debugging CSS" at the center of my screen.

Eventually, the first two rows were correct, but not the third one.

### Debugging

I could write my intermediate calculation steps into class anmes or data attributes to see them at each item, making debugging more visual than just logging to the console.

tileElement
.
dataset
.
offsetTop

=

String
(
tileElement
.
offsetTop
);

Enter fullscreen mode

Exit fullscreen mode

#### Rounded rows vs. raw interim values

In an ideal world (or window), there would be only integer values here, likeclass="row-2".

<li


data-gapped-height=
"436"


data-offset-top=
"783"


data-offset-rows=
"1"


class=
"row-2 is-even"
>


Enter fullscreen mode

Exit fullscreen mode

Inspecting raw values before applyingMath.floor, we can see a growing discrepancy in an unexpected direction. While the second row plus gap is 1 pixel higher than expected, the third row is 89 pixels above its expected position.

let

offsetRows

=

Math
.
floor
(
tileElement
.
offsetTop

/

gappedHeight
);

Enter fullscreen mode

Exit fullscreen mode

* row 1: offsetTop 0 / 436 = 0
* row 2: offsetTop 437 / 436 = 1.002293578
* row 3: offsetTop 783 / 436 = 1.79587156 (436 *2 = 872)

That's got nothing to do with the heights. Those are still equal, as we can see with our eyes and verify in our dev tools.

However, moving the tiles towards the top without compensating by a bottom margin is what messed up my plans.

.custom-grid-has-row-behavior

.is-even

{


margin
:

-6rem

-10rem

1rem

10rem
;

Enter fullscreen mode

Exit fullscreen mode

The provisionalmargin-bottom: 1remshould have been6remto compensate the top-6remshift? That still doesn't look correct.

Now the rows are detected consistently, although I'd expect that to fail given the unexpected extra spacing.

* row 1: offsetTop 0 / 436 = 0
* row 2: offsetTop 437 / 436 = 1.002293578
* row 3: offsetTop 873 / 436 = 2.002293578 (436 *2 = 872)
* row 4: offsetTop 1310 / 436 = 3.004587156
* row 5: offsetTop 1746/ 436 = 4.004587156

The slightly growing offset won't break our layout before adding up to a mathematical extra row number 436, which will never happen™.

### Removing the Gaps

What if we simplify things and eliminate unpredictable gapping by setting the flex/grid gap to zero and adding a padding inside our list items wrapping the visible tiles? (Actually, it's even a little bit more complicated, as each of my flex children wraps not one, but two tiles, but let's just notice that we've already got a wrapper that we can pad instead of the flex gap.)

Then we can also remove our compensation margin at the bottom.

.custom-grid-has-row-behavior

.is-even

{


margin
:

-6rem

-10rem

0

10rem
;

Enter fullscreen mode

Exit fullscreen mode

and fix the failing third row detection.

* row 1: offsetTop 0 / 437 = 0
* row 2: offsetTop 437 / 437 = 1
* row 3: offsetTop 765 / 437 = 1.750572082

437 * 2 = 847847 - 765 = 109109px = 6.8125rem = 6rem + 13px = 🤔?

Instead of the row gap, we must account for the omitted 6rem bottom padding in our calculation, but that only happens every second row.

I made a misconception when I said we only move every second row to the top. We must move every row but the first! Then, at least, we have a different kind of error. That's what I love about visual debugging: even when it's broken, it looks cool! 😂

.custom-grid-has-row-behavior

*
:not
(
:first-child
)

{


margin-top
:

-6rem
;

Enter fullscreen mode

Exit fullscreen mode

That should have been "not first row", not "not first child". Detecting rows beyond CSS' native pseudo-selectors was the whole point of doing custom JS calculations.

.custom-grid-has-row-behavior

*
:not
(
.row-1
)

{


margin-top
:

-6rem
;

Enter fullscreen mode

Exit fullscreen mode

Relying on my custom class names applies the marginsaftermy calculation, but I need them before. That's a problem I already had from the beginning. That could possibly also simplify my calculations. If extra top margins don't matter, then why would we need to consider them at all?

But the point is:allitems don't have a.row-1class before the script ran, so my "fix" gives every item a negative top margin. So let's fix this. Instead of an overengineered[class^="row"]:not(.row-1)let's just add two classes each, likerowandrow-1and write CSS that's easy to read:

.custom-grid-has-row-behavior

.row
:not
(
.row-1
)

{


margin-top
:

-6rem
;

Enter fullscreen mode

Exit fullscreen mode

Let's look at the third row that's still not correctly detected.

* row 3: offsetTop 873 / 437 = 1.99771167

Math.floor(tileElement.offsetTop / gappedHeight)as a recipe for disaster?

### Overengineered or Off by One Pixel?

Pragmatically, I could changeMath.floor()toMath.round(), as we have only one pixel difference to our expected values. "Pixel imperfections happen," I thought, "and they happen inconsistently across different browser engines and screen sizes. If you still feel that rounding is a too dirty solution, I'm curious to find your better solution in the comments!"

Honestly, my fix fixed the first four rows but failed to detect the fifth, and I only noticed after I had removed the debug properties. Obviously, there's more than just an "off-by-one-pixel" issue. A narrower screen makes it more obvious and show the error on line 3 already.

* row 2: offsetHeight 765 / 437 = 1.7505720823798627-> 2
* row 3: offsetHeight 1094 / 437 = 2.5034324942791764-> 3
* row 4: offsetHeight 1422 / 437 = 3.254004576659039-> 3

Row three and four are both treated as row three, breaking the even-odd-layout, and row 2 is already off by 109 pixels (6.8125rem) again, or 437 should be 382.5? Proceeding to find a pattern:

* row 2: 2*437 = 874 (-109) (765/2 = 382.5)
* row 3: 3*437 = 1311 (-217) (1094/3 = 364.666666667)
* row 4: 4*437 = 1748 (-326) (1422/4 = 355.5)

Can you see the pattern? I can't!

## Calculating, Sorting, or Comparing?

Searching the web for alternative solutions, I came across the idea ofsorting unique offsetsinstead of dividing and rounding. Looking up the array or set index for any element's top offset is my new row number (minus one).

Does this still look overengineered? It does!

What if there was a much simpler and more robust solution?

What if I just compare each top offset to the previous element's and increase a row counter when they differ?

for
(
const

tileElement

of

tileElements
)

{


if
(
tileElement
.
offsetTop

>

previousOffset
)

{


currentRow
++
;


}


previousOffset

=

tileElement
.
offsetTop
;

Enter fullscreen mode

Exit fullscreen mode

Why didn't I think of this simple solution much earlier?

## Edge Case Testing

Let's not forget about testing edge cases by creating variations and exaggerating problems like unusually long names or arabic content that implicitly behaves like a span with a changed writing direction.

Here is a fictitious book by Hubert Blaine Wolfeschlegelsteinhausenbergerdorff about things to do in Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch. I didn't make up either, and I prefer them to repetitive Lorem Ipsum by Jane Doe examples that only test the so-called "happy path".

Resizing a window or rotating a mobile phone is another case often overlooked by web designers and developers. My initial placement function would only work once, as the counting calculation depends on the intial auto-placed element positions.

Here's my final logic:

const

refineMasonryLayout

=

// placement function

export

const

refineAllMasonryLayouts

=

():

void

=>

{


// find and reset all modified elements:


let

adjustedGridChildren

=

document
.
getElementsByClassName
(
'
custom-shifted
'
);


for
(
let

adjusted

of

adjustedGridChildren
)

{


adjusted
.
classList
.
remove
(
'
custom-shifted
'
);


}


// then do the actual placement ...

}

addEventListener
(
'
DOMContentLoaded
'
,

()

=>

{


refineAllMasonryLayouts
()

})

addEventListener
(
'
resize
'
,

()

=>

{


refineAllMasonryLayouts
();

})

Enter fullscreen mode

Exit fullscreen mode

I call the placement functions after initial rendering, after resizing, and I export it so that I can call it after a React wrapper might have rerendered.

### Software Architecture

Last but not least, where does this code belong in a project? After I reopened my Astro/React side project after some time, I'd expect it somewhere in or called byLayout.astroor in a TypeScript file called something withplacement, but it turned out I had named itrefineMasonryLayout.tsin autilsfolder.

I decided to publish the codeas an npm moduleso I can refine the code and concept in one central place to avoid further confusion and possible inconsistent states of duplicated code across projects, if I ever use it anywhere else.

### Debugging Again

Creating a minimal reproducible example on codepen, simplified without wrapped pairs, and scoping my functions to a module that you can import from npm, meant debugging again, creating more unexpected decorative patterns on my way to the expected layout.

Here is the currentcodepen (Hexagonal Masonry Layout)

The point that I missed was my original example didn't just use wrappers to group pairs of tiles but also used padding for inner spacing. Trying to use arbitrary margin outside the tiles will break the layout algorithm. A new simplified proof of concept puts a white 2-pixel border plus a 2-pixel bottom margin.

You can experiment with you own settings and have a look atdev-UX-Lesezeichen.de.

This is what I intended the layout to look like.

The final code comes with a resize handler to automatically re-apply the layout adjustment after the viewport size has changed.

I have publishedhexagonal-masonry-placement as a public npmjs package.

## Conclusions

Web development can be fun, even when nothing seems to work as it should. But if something feels overengineered, then it probably is.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
