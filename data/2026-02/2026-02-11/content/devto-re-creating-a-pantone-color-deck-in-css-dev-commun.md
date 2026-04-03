---
title: Re-creating a Pantone Color Deck in CSS - DEV Community
url: https://dev.to/madsstoumann/re-creating-a-pantone-color-deck-in-css-3108
site_name: devto
content_file: devto-re-creating-a-pantone-color-deck-in-css-dev-commun
fetched_at: '2026-02-11T19:27:28.748072'
original_url: https://dev.to/madsstoumann/re-creating-a-pantone-color-deck-in-css-3108
author: Mads Stoumann
date: '2026-02-11'
description: If you’ve ever held a Pantone fan deck — the kind graphic designers used to carry around like a... Tagged with html, css, tutorial, webdev.
tags: '#html, #css, #tutorial, #webdev'
---

If you’ve ever held a Pantone fan deck — the kind graphic designers used to carry around like a sacred artifact — you know the satisfying way those cards fan out from a single rivet point. Each card swings on its own arc, and you flip through the colors by hand.

I wanted to recreate that experience for this week’s CodePen challenge, which is all about color palettes.

Follow along as we build a fully interactive color fan deck where the spread adapts to the container width, cards know their position among their siblings, and clicking a card to "focus" it is handled entirely by the browser’s native<details>element.

No JavaScript! Let’s dive in!

## The Markup

Our fan deck is a<section>containing a cover card, followed by color cards, each wrapped in a<details>element:

<section>


<!-- cover card -->


<details

name=
"deck"
>


<summary>
Reds
<span>
×
</span></summary>


<ul>


<li

style=
"--c: lab(45% 67 30)"
>


<strong>
Poppy Red
</strong>


<dl>


<dt>
HEX
</dt><dd>
#DC3D4C
</dd>


<dt>
RGB
</dt><dd>
220, 61, 76
</dd>


<dt>
LAB
</dt><dd>
45, 56, 25
</dd>


</dl>


</li>


<!-- more colors -->


</ul>


</details>


<details

name=
"deck"
>


<summary>
Blues
<span>
×
</span></summary>


<!-- ... -->


</details>


<!-- more cards -->

</section>

Enter fullscreen mode

Exit fullscreen mode

A few things to note:

* Thecover carddoesn’t toggle — it just sits at the front of the deck.
* Eachcolor cardis a<details name="deck">element. Thenameattribute is the key — it makes them anexclusive accordion. Only one can be open at a time, and clicking the open one closes it.
* The<summary>serves as both the card label and the click target.

Not much to see yet. Let’s add some CSS:

I won’t go into the CSS in depth here; it’s simply a<ul>with the color values defined in a<dl>and wrapped up in a grid.

## Stacking the Deck

First, we need all cards to occupy the same grid cell, stacked on top of each other:

section

{


container-type
:

inline-size
;


display
:

grid
;


place-items
:

end

center
;

}

section

>

*

{


grid-area
:

1

/

-1
;


z-index
:

calc
(
sibling-count
()

-

sibling-index
());

}

Enter fullscreen mode

Exit fullscreen mode

Settingcontainer-type: inline-sizeon the<section>lets us usecontainer query unitslater. Every direct child is placed in the same grid cell withgrid-area: 1 / -1, creating a stack.

Thez-indexline uses two new CSS functions —sibling-count()andsibling-index()— to ensure the first card sits on top. The first child hassibling-index()of 1, so it gets the highestz-index. The last child gets 1. Natural stacking order — no hardcoded values, no counters, no JavaScript.

So, for now, we just see the cover card — the color cards are hidden behind it (the rivet is an::afterpseudo-element with aradial-gradient):

## The Fan Spread withprogress()

This is where it gets interesting. A real fan deck spreads wider when you have room, and collapses into a tight stack in a narrow space. We want the same behavior — and the new CSSprogress()function makes it elegant:

section

>

*

{


--spread
:

progress
(
100
cqi
,

300px
,

1440px
);


--end-degree
:

calc
(
var
(
--spread
)

*

45deg
);


--start-degree
:

calc
(
var
(
--spread
)

*

-45deg
);

}

Enter fullscreen mode

Exit fullscreen mode

progress()returns a value between0and1based on where a value falls within a range. Here,progress(100cqi, 300px, 1440px)asks: "How far is the container’s inline size between 300px and 1440px?"

* At 300px or below:--spreadis0— no fan, cards stacked flat.
* At 1440px or above:--spreadis1— full fan, cards spanning from -45° to +45°.
* At 870px (midpoint):--spreadis0.5— half fan.

No@containerqueries, just one line of CSS, and the spread iscontinuously responsive.

## Positioning Each Card withsibling-index()

Now each card needs its own rotation angle, interpolated between--start-degreeand--end-degreebased on its position in the deck:

section

>

*

{


rotate
:

calc
(


var
(
--start-degree
)

+


(
var
(
--end-degree
)

-

var
(
--start-degree
))

*


(
sibling-index
()

-

1
)

/

(
sibling-count
()

-

1
)


);


transform-origin
:

calc
(
100%

-

var
(
--rivet
))

calc
(
100%

-

var
(
--rivet
));

}

Enter fullscreen mode

Exit fullscreen mode

Let’s break it down:

1. sibling-index() - 1gives us a zero-based position (0 for first card, 1 for second, etc.)
2. sibling-count() - 1gives us the total number of "gaps" between cards
3. Dividing them gives a progress value from0to1for each card’s position
4. We multiply that by the degree range and add the start offset

Thetransform-originis set to the bottom-right corner — offset by--rivet— so all cards rotate around the same pivot point, just like a physical fan deck with a rivet pin.

Cool! The cards now fan out from a single point, and the spread adjusts automatically with the container width, but they’re not interactive yet.

Now we have:

Let’s resize the browser:

I find this incredibly satisfying!

## Click-to-Focus with Exclusive<details>

Here’s where the<details>element earns its place. By giving all color cardsname="deck", the browser enforcesexclusive accordionbehavior:

* Click a card’s summary→ it opens (gets the[open]attribute), any other open card closes automatically.
* Click the same summary again→ it closes, returning to the default fan.

But the<details>element normallyhidesits content when closed. We want the color cards to always be visible — the open/closed state should only affect the card’srotation, not its content visibility. This is where the new::details-contentpseudo-element comes in:

details
::details-content

{


content-visibility
:

visible
;


display
:

contents
;

}

Enter fullscreen mode

Exit fullscreen mode

The::details-contentpseudo-element targets the content slot of a<details>— everything that isn’t the<summary>. By overridingcontent-visibilitytovisibleand settingdisplay: contents, the card’s color list is always rendered, regardless of the open state.

Let’s see how it looks when we select a card:

## CSS-Only State Detection

When a card is open, we want three things to happen:

1. Theactive cardrotates to 0° (straight up)
2. Cardsbeforeit collapse toward the start
3. Cardsafterit push toward the end

We need boolean-like flags —0or1— that each card can use in its rotation formula. And we can set them entirely with CSS selectors:

/* Any card is active */

section
:has
(
details
[
open
])

>

*

{

--has-active
:

1
;

}

/* Cards before the active one */

section

>

:has
(~

details
[
open
])

{

--is-before
:

1
;

}

/* The active card itself */

details
[
open
]

{

--is-active
:

1
;

}

/* Cards after the active one */

details
[
open
]

~

*

{

--is-after
:

1
;

}

Enter fullscreen mode

Exit fullscreen mode

Four selectors, four flags. Let’s unpack them:

* section:has(details[open])matches the sectionwhen any details child is open, then sets--has-active: 1on all children.
* :has(~ details[open])matches any element that has asubsequent siblingthat isdetails[open]— i.e., it comesbeforethe active card.
* details[open]matches the active card directly.
* details[open] ~ *matches allsubsequent siblings— the cardsafterthe active one.

The defaults are all0, set on the basesection > *rule. When no card is open, all flags are0, and the cards fan normally.

### The Full Rotation Formula

With the flags in place, the rotation formula handles all states:

section

>

*

{


rotate
:

calc
(


(
var
(
--start-degree
)

+

(
var
(
--end-degree
)

-

var
(
--start-degree
))


*

(
sibling-index
()

-

1
)

/

(
sibling-count
()

-

1
))


*

(
1

-

var
(
--is-active
))


-

var
(
--is-before
)

*

(
var
(
--end-degree
)

-

var
(
--start-degree
))


*

(
sibling-index
()

-

1
)

/

(
sibling-count
()

-

1
)

*

0.85


+

var
(
--is-after
)

*

(
var
(
--end-degree
)

-

var
(
--start-degree
))


*

(
1

-

(
sibling-index
()

-

1
)

/

(
sibling-count
()

-

1
))

*

0.85


);


transition
:

rotate

.25s

linear
;

}

Enter fullscreen mode

Exit fullscreen mode

So what’s going on?

* Line 1–2:The normal fan rotation — the same formula from before.
* * (1 - var(--is-active)):Multiplying by 0 when active zeroes out the rotation — the card snaps to 0°.
* Before cards:Subtract a value that pushes them further toward the start. The0.85factor collapses them tightly but not completely.
* After cards:Add a value that pushes them further toward the end, using theinverseposition(1 - progress)so they fan toward the opposite edge.

Thetransitiongives it a smooth, satisfying swing.

## The New CSS Features — a Recap

This component leans on several CSS features that are all relatively new — so use a modern browser.

Feature

What It Does Here

progress()

Returns 0–1 based on container width, driving the fan spread

sibling-index()

Each card knows its position — used for rotation and z-index

sibling-count()

Total number of cards — used to normalize position to 0–1

<details name="">

Exclusive accordion — click to open/close, only one active

::details-content

Override content visibility so cards always show their colors

## Final Thoughts

I’m constantly blown away by how far CSS has progressed — and is progressing. What I find exciting is how these new featurescompose. None of them alone are revolutionary — butprogress()feeding intosibling-index()-driven rotation, toggled by native<details>state detected via:has()selectors, all without a single line of JavaScript.

Here’s a CodePen demo. I urge you to open it full-screen, resize, click etc.:

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
