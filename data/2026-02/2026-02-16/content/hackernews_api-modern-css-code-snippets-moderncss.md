---
title: Modern CSS Code Snippets | modern.css
url: https://modern-css.com
site_name: hackernews_api
content_file: hackernews_api-modern-css-code-snippets-moderncss
fetched_at: '2026-02-16T11:19:09.876914'
original_url: https://modern-css.com
author: eustoria
date: '2026-02-15'
description: A collection of modern CSS code snippets. Every old CSS hack next to its clean, native replacement, side by side.
tags:
- hackernews
- trending
---

Updated for 2026

# Stop writing CSSlike it's 2015.

Modern CSS code snippets, side by side with the old hacks they replace. Every technique you still Google has a clean, native replacement now.

Old

.child
 {

   
position
:
absolute
;

   
top
:
50%
;

   
left
:
50%
;

   
transform
:
translate(-50%,-50%)
;

 }


Modern

.parent
 {

   
display
:
grid
;

   
place-items
:
center
;

 }

/* child needs nothing. */

## All comparisons

64 snippets

Browser compatibility:

All

Newly available

Widely available

Limited

Color

Intermediate

### Perceptually uniform colors with oklch

Old

--brand
:
#4f46e5
;
--brand-light
:
#818cf8
;
--brand-dark
:
#3730a3
;
/* guess-and-check each shade */

Modern

--brand
:
oklch
(
0.55 0.2 264
);
--brand-light
:
oklch
(
0.75 0.2 264
);
--brand-dark
:
oklch
(
0.35 0.2 264
);
/* only L changes, same perceived hue */


see modern →

90%

→

Color

Intermediate

### Frosted glass effect without opacity hacks

Old

.card::before
 {
content
:
''
;
  
background-image
:
url(bg.jpg)
;
  
filter
:
blur(12px)
;
  
z-index
:
-1
; }

Modern

.glass
 {
  
backdrop-filter
:
blur(12px)
;
  
background
:
rgba(255,255,255,.1)
;
}

see modern →

96%

→

Layout

Beginner

### Preventing layout shift from scrollbar appearance

Old

body
 {
overflow-y
:
scroll
; }
/* or hardcode the scrollbar width */
body
 {
padding-right
:
17px
; }

Modern

body
 {
  
scrollbar-gutter
:
stable
;
}
/* scrollbar space always reserved */


see modern →

90%

→

Layout

Beginner

### Preventing scroll chaining without JavaScript

Old

// JS: block page scroll when inside modal
modal
.
addEventListener
(
'wheel'
,
e
 =>
  
e
.
preventDefault
(), {
passive
:
false
 })

Modern

.modal-content
 {
  
overflow-y
:
auto
;
  
overscroll-behavior
:
contain
;
}
/* page stays still */


see modern →

96%

→

Layout

Beginner

### Responsive images without the background-image hack

Old

.card-image
 {
  
background-image
:
url(...)
;
  
background-size
:
cover
;
  
background-position
:
center
;
}

Modern

img
 {
  
object-fit
:
cover
;
  
width
:
100%
;
  
height
:
200px
;
}

see modern →

96%

→

Selector

Beginner

### Form validation styles without JavaScript

Old

// JS: add .touched on blur
el
.
addEventListener
(
'blur'
, () =>
  
el
.
classList
.
add
(
'touched'
))
/* .touched:invalid { color: red } */

Modern

input
:
user-invalid
 {
  
border-color
:
red
;
}
input
:
user-valid
 {
  
border-color
:
green
;
}

see modern →

85%

→

Layout

Beginner

### Auto-growing textarea without JavaScript

Old

// JS: resize on every keystroke
el
.
addEventListener
(
'input'
, () => {
  
el
.
style
.
height
 =
'auto'
;
  
el
.
style
.
height
 =
el
.
scrollHeight
 +
'px'
; })

Modern

textarea
 {
  
field-sizing
:
content
;
  
min-height
:
3lh
;
}
/* grows with content, no JS */


see modern →

73%

→

Animation

Beginner

### Smooth height auto animations without JavaScript

Old

// measure, set px, then snap to auto
el
.
style
.
height
 =
el
.
scrollHeight
 +
'px'
;
el
.
addEventListener
(
'transitionend'
, ...)

Modern

:root
 {
interpolate-size
:
allow-keywords
; }
.accordion
 {
height
:
0
;
overflow
:
hidden
;
  
transition
:
height .3s ease
; }
.accordion.open
 {
height
:
auto
; }

see modern →

69%

→

Workflow

Advanced

### Range style queries without multiple blocks

Old

/* Multiple style() blocks */
@container

style
(
--p: 51%
) {}
@container

style
(
--p: 52%
) {}
/* ...for each value */

Modern

@container

style
(
  
--progress > 50%
) {
  
.bar
 { ... }
}

see modern →

88%

→

Animation

Intermediate

### Sticky & snapped element styling without JavaScript

Old

window
.
addEventListener
(
  
'scroll'
, () => {
    
/* check position */
});

Modern

@container

scroll-state
(
  
stuck: top
) {
  
.header
 { ... }
}

see modern →

50%

→

Workflow

Intermediate

### Typed attribute values without JavaScript

Old

// JS reading dataset
el
.
style
.
width
 =
  
el
.
dataset
.
pct
 +
'%'
;

Modern

.bar
 {
  
width
:
attr
(
    
data-pct

type
(
<percentage>
)
  );
}

see modern →

42%

→

Workflow

Intermediate

### Inline conditional styles without JavaScript

Old

// JavaScript toggling
el
.
classList
.
toggle
(
  
'primary'
,
isPrimary
);

Modern

.btn
 {
  
background
:
if
(
    
style(--variant: primary)
:
      
blue
;
else
:
gray
  );
}

see modern →

35%

→

Workflow

Intermediate

### Reusable CSS logic without Sass mixins

Old

// Sass function
@function

fluid
(
$min
,
$max
) {
  
@return

clamp
(...);
}

Modern

@function

--fluid
(
  
--min
,
--max
) {
  
@return

clamp
(...);
}

see modern →

67%

→

Layout

Beginner

### Corner shapes beyond rounded borders

Old

.card
 {
  
clip-path
:
polygon
(
    
...

/* 20+ points */
  );
}

Modern

.card
 {
  
border-radius
:
2em
;
  
corner-shape
:
squircle
;
}

see modern →

67%

→

Animation

Advanced

### Responsive clip paths without SVG

Old

.shape
 {
  
clip-path
:
path
(
    
'M0 200 L100 0...'
  );
}

Modern

.shape
 {
  
clip-path
:
shape
(
    
from 0% 100%
, ...
  );
}

see modern →

96%

→

Selector

Intermediate

### Scroll spy without IntersectionObserver

Old

const

observer
 =
new
  
IntersectionObserver
(cb);
/* 15+ lines of JS */

Modern

nav a
:
target-current
 {
  
color
:
var(--accent)
;
}

see modern →

48%

→

Layout

Beginner

### Filling available space without calc workarounds

Old

.full
 {
  
width
:
calc
(
100%
 -
40px
);
  
/* or width: 100% and overflow */
}

Modern

.full
 {
  
width
:
stretch
;
}
/* fills container, keeps margins */


see modern →

90%

→

Animation

Intermediate

### Staggered animations without nth-child hacks

Old

li:nth-child(1)
 {
--i
:
0
; }
li:nth-child(2)
 {
--i
:
1
; }
li:nth-child(3)
 {
--i
:
2
; }
/* repeat for every item… */

Modern

li
 {
  
transition-delay
:
    
calc
(
0.1s
 * (
sibling-index()
 -
1
));
}

see modern →

70%

→

Layout

Advanced

### Carousel navigation without a JavaScript library

Old

// Swiper.js or Slick carousel
new

Swiper
(
'.carousel'
, {
  
navigation
: {
/* … */
 },
  
pagination
: {
/* … */
 },
});

Modern

.carousel
::scroll-button(right)
 {
  
content
:
"➡"
;
}
.carousel li
::scroll-marker
 {
  
content
:
''
;
}

see modern →

72%

→

Typography

Beginner

### Vertical text centering without padding hacks

Old

.btn
 {
  
padding
:
10px 20px
;
  
/* looks off-center, tweak top/bottom */
  
padding-top
:
8px
;
/* hack */
}

Modern

h1
,
button
 {
  
text-box
:
trim-both cap alphabetic
;
}
/* true optical centering */


see modern →

79%

→

Layout

Intermediate

### Hover tooltips without JavaScript events

Old

// JS: mouseenter + mouseleave
btn
.
addEventListener
(
'mouseenter'
,
  () =>
showTooltip
())
/* + focus, blur, positioning */

Modern

<button

interestfor
=
"tip"
>
Hover me
</button>
<div

id
=
"tip"

popover
=
hint
>
  Tooltip content
</div>


see modern →

86%

→

Layout

Beginner

### Modal controls without onclick handlers

Old

<button

onclick
=
"
  
document
.
querySelector
(
'#dlg'
)
  .
showModal
()
"
>
Open
</button>

Modern

<button

commandfor
=
"dlg"
  
command
=
"show-modal"
>
Open
</button>
<dialog

id
=
"dlg"
>
...
</dialog>


see modern →

72%

→

Layout

Beginner

### Dialog light dismiss without click-outside listeners

Old

// JS: listen for click on ::backdrop
dialog
.
addEventListener
(
'click'
,
  (e) => {
/* check bounds */
 })

Modern

<dialog

closedby
=
"any"
>
  Click outside to close
</dialog>
/* no JS listeners */


see modern →

72%

→

Layout

Intermediate

### Customizable selects without a JavaScript library

Old

// Select2 or Choices.js
new

Choices
(
'#my-select'
);
/* rebuilds entire DOM */

Modern

select
,
select

::picker(select)
 {
  
appearance
:
base-select
;
}

see modern →

96%

→

Color

Intermediate

### Vivid colors beyond sRGB

Old

.hero
 {
  
color
:
rgb
(200, 80, 50);
}
/* sRGB only, washed on P3 */

Modern

.hero
 {
  
color
:
oklch
(0.7 0.25 29);
}
/* or color(display-p3 1 0.2 0.1) */


see modern →

90%

→

Color

Advanced

### Color variants without Sass functions

Old

/* Sass: lighten($brand, 20%), darken($brand, 10%) */
.btn
 {
background
:
#e0e0e0
; }

Modern

.btn
 {
  
background
:
oklch
(
from

var
(--brand)
calc
(l + 0.2) c h);
}

see modern →

87%

→

Typography

Beginner

### Multiline text truncation without JavaScript

Old

/* JS: slice text by chars/words, add "..." */
.card-title
 {
overflow
:
hidden
; }

Modern

.card-title
 {
  
display
:
-webkit-box
;
  
-webkit-line-clamp
:
3
;
  
line-clamp
:
3
;
}

see modern →

96%

→

Typography

Beginner

### Drop caps without float hacks

Old

.drop-cap::first-letter
 {
  
float
:
left
;
  
font-size
:
3em
;
line-height
:
1
;
}

Modern

.drop-cap::first-letter
 {
  
initial-letter
:
3
;
}

see modern →

91%

→

Layout

Beginner

### Positioning shorthand without four properties

Old

.overlay
 {
  
top
:
0
;
right
:
0
;
  
bottom
:
0
;
left
:
0
;
}

Modern

.overlay
 {
  
position
:
absolute
;
  
inset
:
0
;
}

see modern →

93%

→

Workflow

Intermediate

### Lazy rendering without IntersectionObserver

Old

// JS IntersectionObserver
new

IntersectionObserver
(
  (entries) => {
/* render */
 }
).
observe
(el);

Modern

.section
 {
  
content-visibility
:
auto
;
  
contain-intrinsic-size
:
auto 500px
;
}

see modern →

93%

→

Layout

Beginner

### Dropdown menus without JavaScript toggles

Old

.menu
 {
display
:
none
; }
.menu.open
 {
display
:
block
; }
/* + JS: click, clickOutside, ESC, aria */

Modern

button
[
popovertarget
=
menu
] { }
#menu
[
popover
] {
  
position
:
absolute
;
}

see modern →

86%

→

Layout

Advanced

### Tooltip positioning without JavaScript

Old

/* Popper.js / Floating UI: compute rect,
 position: fixed, update on scroll */
.tooltip
 {
position
:
fixed
; }

Modern

.trigger
 {
anchor-name
:
--tip
; }
.tooltip
 {
  
position-anchor
:
--tip
;
  
top
:
anchor(bottom)
;
}

see modern →

77%

→

Workflow

Advanced

### Scoped styles without BEM naming

Old

// BEM: .card__title, .card__body
.card__title
 { â€¦ }
.card__body
 { â€¦ }
// or CSS Modules / styled-components */

Modern

@scope
 (
.card
) {
  
.title
 {
font-size
:
1.25rem
; }
  
.body
 {
color
:
#444
; }
}
/* .title only inside .card */


see modern →

84%

→

Workflow

Advanced

### Typed custom properties without JavaScript

Old

// --hue was a string, no animation
:root
 {
--hue
:
0
; }
hsl
(
var
(
--hue
), â€¦)
/* no interpolation */

Modern

@property

--hue
 {
  
syntax
:
"<angle>"
;
  
inherits
:
false
;
  
initial-value
:
0deg
;
}
/* animatable, validated */


see modern →

92%

→

Animation

Beginner

### Independent transforms without the shorthand

Old

.icon
 {
transform
:
translateX
(
10px
)
rotate
(
45deg
)
scale
(
1.2
); }
/* change one = rewrite all */

Modern

.icon
 {
  
translate
:
10px 0
;
  
rotate
:
45deg
;
  
scale
:
1.2
;
}
/* animate any one without touching the rest */


see modern →

92%

→

Animation

Intermediate

### Animating display none without workarounds

Old

// wait for transitionend then display:none
el
.
addEventListener
(
'transitionend'
, â€¦)
visibility
 +
opacity
 +
pointer-events

Modern

.panel
 {
transition
:
opacity .2s, overlay .2s
;
  
transition-behavior
:
allow-discrete
; }
.panel.hidden
 {
opacity
:
0
;
display
:
none
; }
/* no JS wait or visibility hack */


see modern →

85%

→

Animation

Intermediate

### Entry animations without JavaScript timing

Old

// add class after paint
requestAnimationFrame
(() => {
  
el
.
classList
.
add
(
'visible'
);
});

Modern

.card
 {
transition
:
opacity .3s, transform .3s
; }
.card
 {
@starting-style
 {
opacity
:
0
;
transform
:
translateY
(
10px
); } }
/* no rAF/setTimeout */


see modern →

85%

→

Animation

Advanced

### Page transitions without a framework

Old

// Barba.js or React Transition Group
Barba
.
init
({ â€¦ })
transition
 hooks +
duration
 state

Modern

document
.
startViewTransition
(() =>
updateDOM
());
.hero
 {
view-transition-name
:
hero
; }
/* no Barba, no React TG */


see modern →

89%

→

Layout

Intermediate

### Scroll snapping without a carousel library

Old

// Slick, Swiper, or scroll/touch JS
$
(
'.carousel'
).
slick
({ â€¦ })
touchstart
 /
scroll
 handlers

Modern

.carousel
 {
scroll-snap-type
:
x mandatory
; }
.carousel > *
 {
scroll-snap-align
:
start
; }
/* no lib, no touch handlers */


see modern →

96%

→

Typography

Beginner

### Balanced headlines without manual line breaks

Old

// manual <br> or Balance-Text.js
h1
 {
text-align
:
center
; }
.balance-text

/* JS lib */

Modern

h1
,
h2
 {
  
text-wrap
:
balance
;
}
/* no br or JS */


see modern →

87%

→

Typography

Beginner

### Font loading without invisible text

Old

@font-face
 { ... }
/* Default: invisible text until load */

Modern

@font-face
 {
  
font-family
:
"MyFont"
;
  
font-display
:
swap
;
}

see modern →

96%

→

Typography

Intermediate

### Multiple font weights without multiple files

Old

@font-face
 {
font-weight
:
400
; }
@font-face
 {
font-weight
:
700
; }
/* 4+ files */

Modern

@font-face
 {
  
font-family
:
"MyVar"
;
  
src
:
url("MyVar.woff2")
;
  
font-weight
:
100 900
;
}

see modern →

96%

→

Workflow

Beginner

### Dark mode defaults without extra CSS

Old

@media
 (
prefers-color-scheme
:
dark
) {
  
input, select, textarea
 { ... }
}

Modern

:root
 {
  
color-scheme
:
light dark
;
}

see modern →

93%

→

Color

Intermediate

### Dark mode colors without duplicating values

Old

@media
 (
prefers-color-scheme
:
dark
) {
  
color
:
#eee
;
}

Modern

color
:
light-dark
(
#111
,
#eee
);
color-scheme
:
light dark
;

see modern →

83%

→

Selector

Intermediate

### Low-specificity resets without complicated selectors

Old

.reset ul, .reset ol
 { ... }
/* or (0,0,1) specificity, still wins */

Modern

:where
(
ul, ol
) {
  
margin
:
0
;
  
padding-inline-start
:
1.5rem
;
}

see modern →

96%

→

Layout

Intermediate

### Direction-aware layouts without left and right

Old

margin-left
:
1rem
;
padding-right
:
1rem
;
[dir="rtl"
]
.box
 {
margin-right
: ... }

Modern

margin-inline-start
:
1rem
;
padding-inline-end
:
1rem
;
border-block-start
:
1px solid
;

see modern →

96%

→

Layout

Beginner

### Naming grid areas without line numbers

Old

float
:
left
;
/* clearfix, margins */
grid-column
:
1 / 3
;
grid-row
:
2
;

Modern

.layout
 {
  
display
:
grid
;
  
grid-template-areas
:
"header header" "sidebar main" "footer footer"
;
}

see modern →

96%

→

Layout

Advanced

### Aligning nested grids without duplicating tracks

Old

.child-grid
 {
  
grid-template-columns
:
1fr 1fr 1fr
;
/* duplicate parent tracks */
}

Modern

.child-grid
 {
  
display
:
grid
;
  
grid-template-columns
:
subgrid
;
}

see modern →

88%

→

Layout

Intermediate

### Modal dialogs without a JavaScript library

Old

.overlay
 {
position
:
fixed
;
z-index
:
999
; }
/* + JS: open/close, ESC, focus trap */

Modern

dialog
 {
  
padding
:
1rem
;
}
dialog::backdrop
 {
background
:
rgb
(0 0 0 / .5); }

see modern →

96%

→

Color

Beginner

### Styling form controls without rebuilding them

Old

appearance
:
none
;
// + 20+ lines of custom box/border/background

Modern

input
[
type
=
"checkbox"
],
input
[
type
=
"radio"
] {
  
accent-color
:
#7c3aed
;
}

see modern →

93%

→

Selector

Beginner

### Grouping selectors without repetition

Old

.card h1
,
.card h2
,
.card h3
,
.card h4
 {
  
margin-bottom
:
0.5em
;
}

Modern

.card

:is
(
h1
,
h2
,
h3
,
h4
) {
  
margin-bottom
:
0.5em
;
}

see modern →

96%

→

Selector

Beginner

### Focus styles without annoying mouse users

Old

:focus
 {
outline
:
2px solid blue
; }
// Shows on mouse click too, or people remove it (a11y fail)

Modern

:focus-visible
 {
  
outline
:
2px solid

var
(
--focus-color
);
}

see modern →

95%

→

Workflow

Intermediate

### Controlling specificity without !important

Old

.card .title
 { ... }
.page .card .title
 { ... }
.page .card .title.special
 {
color
:
red

!important
; }

Modern

@layer

base
,
components
,
utilities
;
@layer

utilities
 {
.mt-4
 {
margin-top
:
1rem
; } }

see modern →

95%

→

Workflow

Beginner

### Theme variables without a preprocessor

Old

// Sass: $primary: #7c3aed;
// Compiles to static #7c3aed
.btn
 {
background
:
$primary
; }

Modern

:root
 {
  
--primary
:
#7c3aed
;
}
.btn
 {
background
:
var
(
--primary
); }

see modern →

96%

→

Typography

Intermediate

### Fluid typography without media queries

Old

h1
 {
font-size
:
1rem
; }
@media
 (
min-width
:
600px
) {
h1
 {
font-size
:
1.5rem
; } }
@media
 (
min-width
:
900px
) {
h1
 {
font-size
:
2rem
; } }

Modern

h1
 {
  
font-size
:
clamp
(
1rem
,
2.5vw
,
2rem
);
}

see modern →

95%

→

Layout

Beginner

### Spacing elements without margin hacks

Old

.grid

> *
 {
margin-right
:
16px
; }
.grid

> *:last-child
 {
margin-right
:
0
; }

Modern

.grid
 {
  
display
:
flex
;
  
gap
:
16px
;
}

see modern →

95%

→

Layout

Beginner

### Aspect ratios without the padding hack

Old

.wrapper
 {
padding-top
:
56.25%
;
position
:
relative
; }
.inner
 {
position
:
absolute
;
inset
:
0
; }

Modern

.video-wrapper
 {
  
aspect-ratio
:
16 / 9
;
}

see modern →

93%

→

Layout

Beginner

### Sticky headers without JavaScript scroll listeners

Old

// JS: scroll listener + getBoundingClientRect
// then add/remove .fixed class
.header.fixed
 {
position
:
fixed
; }

Modern

.header
 {
  
position
:
sticky
;
  
top
:
0
;
}

see modern →

96%

→

Animation

Advanced

### Scroll-linked animations without a library

Old

// JS + IntersectionObserver
observer
.
observe
(el)
el
.
style
.
opacity
 = …

Modern

animation-timeline
:
view()
;
animation-range
:
entry
;
/* pure CSS, GPU-accelerated */


see modern →

78%

→

Workflow

Beginner

### Nesting selectors without Sass or Less

Old

// requires Sass compiler
.nav
 {
  
& a
 {
color
:
#888
; }
}

Modern

.nav
 {
  
& a
 {
color
:
#888
; }
}
/* plain .css, no build */


see modern →

91%

→

Layout

Intermediate

### Responsive components without media queries

Old

@media
 (
max-width
:
768px
) {
  
.card
 { … }
}
/* viewport, not container */

Modern

@container
 (
width
 <
400px
) {
  
.card
 {
flex-direction
:
column
; }
}

see modern →

93%

→

Colors

Intermediate

### Mixing colors without a preprocessor

Old

// Sass required
$blend
:
mix
(
  
$blue
,
$pink
,
60%
);

Modern

background
:
color-mix
(
  
in oklch
,
#3b82f6
,
  
#ec4899
);

see modern →

89%

→

Selectors

Intermediate

### Selecting parent elements without JavaScript

Old

// JavaScript required
el
.
closest
(
'.parent'
)
  .
classList
.
add
(…)

Modern

.card:has(img)
 {
  
grid-template
:
auto 1fr
;
}

see modern →

94%

→

Layout

Beginner

### Centering elements without the transform hack

Old

position
:
absolute
;
top
:
50%
;
left
:
50%
;
transform
:
translate(-50%,-50%)
;

Modern

.parent
 {
  
display
:
grid
;
  
place-items
:
center
;
}

see modern →

96%

→

64
Snippets

26
CSS Features Tracked

3
Articles

0
Dependencies

## New CSS drops every month.

Get one old → modern comparison in your inbox every week.

Subscribe

modern
.css

✕


 Search…


ESC

↑
↓
 navigate

↵
 open

esc
 close
