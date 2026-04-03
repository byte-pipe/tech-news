---
title: I Know This Will Upset Some Devs, but Tailwind + Shadcn/ui + Shadow DOM = Pain - DEV Community
url: https://dev.to/ujja/i-know-this-will-upset-some-devs-but-tailwind-shadcnui-shadow-dom-pain-44l7
site_name: devto
fetched_at: '2026-02-07T11:08:18.612156'
original_url: https://dev.to/ujja/i-know-this-will-upset-some-devs-but-tailwind-shadcnui-shadow-dom-pain-44l7
author: ujja
date: '2026-02-05'
description: This recent post Is Learning CSS a Waste of Time in 2026? (by @sylwia-lask) really hit me,... Tagged with css, discuss, react, tailwindcss.
tags: '#discuss, #css, #react, #tailwindcss'
---

This recent postIs Learning CSS a Waste of Time in 2026?(by@sylwia-lask) really hit me, especially the part about accessibility dragging you straight back into raw CSS.

Lately, with Tailwind and shadcn, most styling just… works. Move fast, tweak a class or two, done.

Then Shadow DOM happened.

Suddenly, stuff that “should just work” broke. Overrides stopped applying, styles got tricky, and all those abstractions felt thinner than expected.

Not a Tailwind or shadcn complaint...just a reminder that knowing CSS still saves you when things fall apart.

## The dream vs. the reality

So here's the idea: build beautiful, reusable web components using React, style them with Tailwind CSS, use shadcn/ui for polished UI components, and wrap them up with Shadow DOM for perfect encapsulation. Sounds great, right?

Well... not quite. Turns out these three technologies don't play nicely together. Here's what we learned the hard way.

TL;DR:Shadow DOM + Tailwind + shadcn/ui = pain. Choose carefully based on your actual needs, not theoretical ideals. Sometimes the "impure" solution is the right one.

## The Setup

We were building:

* React components wrapped as web components
* Styled withTailwind CSS
* Usingshadcn/uicomponents for the UI
* Wrapped withShadow DOMfor style encapsulation

Let's talk about what went wrong.

## Problem #1: Shadow DOM vs. Tailwind CSS - A Fundamental Conflict

### Why they don't get along

Tailwind CSS is built on a simple idea: utility classes in a global stylesheet. You include one CSS file, and boom - every element on your page can use classes likebg-blue-500orflex justify-center.

Shadow DOM is built on the opposite idea: complete isolation. Styles inside Shadow DOM can't leak out, and styles from outside can't leak in. This is great for encapsulation, but terrible for Tailwind.

Here's what happens:

// Your React component with Tailwind classes

export

const

MyCard

=

()

=>

{


return
(


<
div

className
=
"
max-w-2xl w-full p-4 bg-white rounded-lg shadow-md
"
>


<
h1

className
=
"
text-2xl font-bold text-gray-900
"
>
Hello

World
<
/h1
>


<
p

className
=
"
text-gray-600 mt-2
"
>
This

should

look

nice
...
<
/p
>


<
/div
>


);

};

// Wrap it as a web component with Shadow DOM

const

MyCardWC

=

r2wc
(
MyCard
,

{


shadow
:

'
open
'

// Enable Shadow DOM

});

customElements
.
define
(
'
my-card
'
,

MyCardWC
);

Enter fullscreen mode

Exit fullscreen mode

Result:Your component renders, but it looks completely broken. No padding, no background color, no rounded corners. Nothing. All your Tailwind classes are ignored because the global Tailwind stylesheet can't penetrate the Shadow DOM boundary.

### The "solution" (with heavy air quotes)

You have to import the Tailwind CSS directly into each component:

// styles.css

@
tailwind

base
;

@
tailwind

components
;

@
tailwind

utilities
;

// Component file

import

'
./styles.css
'
;

// Import for every component

const

MyCardWC

=

r2wc
(
MyCard
,

{


shadow
:

'
open
'

});

Enter fullscreen mode

Exit fullscreen mode

This works, but at a cost:

Bundle size explosionEvery web component bundles its own complete copy of Tailwind CSS. If you have 5 components on a page, you're loading Tailwind 5 times. That's 5x the CSS, all identical.

No browser cachingSince each component has its own bundled styles, you can't leverage browser caching for shared CSS. Every component download includes the same Tailwind utilities.

Build complexityYour build tools need to handle CSS imports for each component separately, making your webpack/vite config more complex.

Real numbers:

* Single Tailwind CSS file: ~50-100KB (minified)
* With 3 web components: 150-300KB
* With 10 web components: 500KB-1MB

Yeah, not great.

## Problem #2: shadcn/ui and the Portal Problem

### What makes shadcn/ui special (and problematic)

shadcn/ui is built on Radix UI primitives, which are fantastic components. But they have one quirk that breaks with Shadow DOM:portals.

Components like Dialog, Dropdown, Popover, Tooltip all use React portals to render their content outside the normal component tree, usually by appending todocument.body. This is smart for z-index management and avoiding overflow issues, but it's a disaster for Shadow DOM.

### Example: The Accordion that works

import

{

Accordion
,

AccordionItem
,

AccordionTrigger
,

AccordionContent

}

from

'
@your-ui/components
'
;

export

const

FAQ

=

()

=>

{


return
(


<
Accordion

type
=
"
single
"

collapsible
>


<
AccordionItem

value
=
"
item-1
"
>


<
AccordionTrigger
>
What

is

this
?
<
/AccordionTrigger
>


<
AccordionContent
>


This

is

an

accordion

that

actually

works

with

Shadow

DOM
!


<
/AccordionContent
>


<
/AccordionItem
>


<
/Accordion
>


);

};

const

FAQWC

=

r2wc
(
FAQ
,

{

shadow
:

'
open
'

});

Enter fullscreen mode

Exit fullscreen mode

Why it works:Accordion renders everything in-place. No portals, no teleporting content. All the HTML stays within your component tree, so Shadow DOM can style it.

### Example: The Dialog that breaks

import

{

Dialog
,

DialogTrigger
,

DialogContent

}

from

'
@your-ui/components
'
;

export

const

MyDialog

=

()

=>

{


return
(


<
Dialog
>


<
DialogTrigger
>
Open
<
/DialogTrigger
>


<
DialogContent
>


<
h2
>
This

won
'
t be styled properly!</h2>
 <p>The content is outside Shadow DOM now.</p>
 </DialogContent>
 </Dialog>
 );
};

const MyDialogWC = r2wc(MyDialog, { shadow:
'
open
'
 });

Enter fullscreen mode

Exit fullscreen mode

Why it breaks:

1. DialogContentgets portaled todocument.body
2. It's now outside your Shadow DOM
3. All your Tailwind classes (inside Shadow DOM) can't reach it
4. The dialog renders, but looks completely unstyled

What you see:

* No background overlay
* No styling on the dialog box
* Text isn't centered
* Buttons look like plain HTML
* Z-index issues (might render behind other elements)

### The workaround

You have to choose: Shadow DOM or portals. Can't have both.

Option A: Disable Shadow DOM for portal-heavy components

// No Shadow DOM = portals work, but no encapsulation

const

MyDialogWC

=

r2wc
(
MyDialog
,

{


shadow
:

null

});

Enter fullscreen mode

Exit fullscreen mode

Now you need to manage styles globally and deal with potential class name conflicts.

Option B: Only use non-portal components

// ✅ Safe to use with Shadow DOM

import

{


Accordion
,


Card
,


Badge
,


Button
,


Tabs
,


Progress

}

from

'
@your-ui/components
'
;

// ❌ Don't use with Shadow DOM (they use portals)

import

{


Dialog
,


Popover
,


Tooltip
,


DropdownMenu
,


Sheet
,


AlertDialog

}

from

'
@your-ui/components
'
;

Enter fullscreen mode

Exit fullscreen mode

This limits your UI toolkit significantly.

## Problem #3: Dynamic Classes and CVA

### Class Variance Authority (CVA) complications

shadcn/ui uses CVA to handle component variants - different sizes, colors, and states. This generates Tailwind classes dynamically:

import

{

cva

}

from

'
class-variance-authority
'
;

const

buttonVariants

=

cva
(


"
inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors
"
,


{


variants
:

{


variant
:

{


default
:

"
bg-primary text-primary-foreground hover:bg-primary/90
"
,


destructive
:

"
bg-red-500 text-white hover:bg-red-600
"
,


outline
:

"
border border-input bg-background hover:bg-accent hover:text-accent-foreground
"
,


ghost
:

"
hover:bg-accent hover:text-accent-foreground
"
,


},


size
:

{


default
:

"
h-10 px-4 py-2
"
,


sm
:

"
h-9 rounded-md px-3
"
,


lg
:

"
h-11 rounded-md px-8
"
,


icon
:

"
h-10 w-10
"
,


},


},


defaultVariants
:

{


variant
:

"
default
"
,


size
:

"
default
"
,


},


}

);

// Button component

export

const

Button

=

({

variant
,

size
,

children

})

=>

{


return
(


<
button

className
=
{
buttonVariants
({

variant
,

size

})}
>


{
children
}


<
/button
>


);

};

Enter fullscreen mode

Exit fullscreen mode

### The Shadow DOM problem

All these dynamically generated classes need to exist in your Shadow DOM's stylesheet. But Tailwind's JIT (Just-In-Time) compiler only includes classes it finds in your files during build time.

When CVA combines classes dynamically at runtime, Tailwind might not have included them in the build, leading to missing styles.

### The fix: Safelist everything

// tailwind.config.js

module
.
exports

=

{


content
:

[


'
./src/**/*.{ts,tsx}
'
,


// CRITICAL: Include your UI library


'
./node_modules/@your-ui-lib/**/*.{ts,tsx}
'
,


],


// Force include commonly used variant classes


safelist
:

[


// Primary variants


'
bg-primary
'
,


'
text-primary-foreground
'
,


'
hover:bg-primary/90
'
,


// Destructive variants


'
bg-red-500
'
,


'
bg-red-600
'
,


'
hover:bg-red-600
'
,


// Sizes


'
h-9
'
,


'
h-10
'
,


'
h-11
'
,


'
px-3
'
,


'
px-4
'
,


'
px-8
'
,


// Add every possible variant combination...


],

};

Enter fullscreen mode

Exit fullscreen mode

The problem with safelist:

* You need to manually list every possible class combination
* Easy to miss classes (leading to visual bugs)
* Increases CSS bundle size (defeats purpose of JIT)
* Need to update whenever UI library changes

## Problem #4: Theme Variables and CSS Custom Properties

### How shadcn/ui does theming

shadcn/ui uses CSS custom properties (variables) for theming:

:root

{


--background
:

0

0%

100%
;


--foreground
:

222.2

47.4%

11.2%
;


--primary
:

221.2

83.2%

53.3%
;


--primary-foreground
:

210

40%

98%
;


/* ... many more */

}

.dark

{


--background
:

222.2

84%

4.9%
;


--foreground
:

210

40%

98%
;


/* ... dark theme values */

}

Enter fullscreen mode

Exit fullscreen mode

Then in your Tailwind config:

// tailwind.config.js

module
.
exports

=

{


theme
:

{


extend
:

{


colors
:

{


background
:

'
hsl(var(--background))
'
,


foreground
:

'
hsl(var(--foreground))
'
,


primary
:

{


DEFAULT
:

'
hsl(var(--primary))
'
,


foreground
:

'
hsl(var(--primary-foreground))
'
,


},


},


},


},

};

Enter fullscreen mode

Exit fullscreen mode

### Shadow DOM breaks variable inheritance

CSS custom properties inherit through the DOM tree, but Shadow DOM creates a boundary. Variables defined outside don't automatically flow in.

// This won't work as expected

export

const

ThemedCard

=

()

=>

{


return
(


<
div

className
=
"
bg-background text-foreground p-4
"
>


<
h2

className
=
"
text-primary font-bold
"
>
Title
<
/h2
>


<
p
>
Content

here
...
<
/p
>


<
/div
>


);

};

const

ThemedCardWC

=

r2wc
(
ThemedCard
,

{

shadow
:

'
open
'

});

Enter fullscreen mode

Exit fullscreen mode

Result:Your component can't access--background,--foreground, or--primaryvariables. All theme colors fallback to defaults or break entirely.

### The solution: Replicate variables

You need to redeclare CSS variables inside your Shadow DOM:

// styles.css (imported by your component)

:
host

{


/* Re-declare all theme variables */


--
background
:

0

0
%

100
%
;


--
foreground
:

222.2

47.4
%

11.2
%
;


--
primary
:

221.2

83.2
%

53.3
%
;


/* ... all other variables */

}

@
tailwind

base
;

@
tailwind

components
;

@
tailwind

utilities
;

Enter fullscreen mode

Exit fullscreen mode

Problems with this approach:

* Theme variables are duplicated everywhere
* Dark mode requires extra work (can't just toggle a class ondocument.body)
* Updating theme means updating multiple files
* No single source of truth

## Real-World Impact: A Case Study

Let's look at what this means in practice. Say you're building a dashboard with these components:

// 1. A stats card

const

StatsCard

=

()

=>

(


<
div

className
=
"
bg-white p-6 rounded-lg shadow
"
>


<
h3

className
=
"
text-lg font-semibold text-gray-900
"
>
Total

Users
<
/h3
>


<
p

className
=
"
text-3xl font-bold text-primary mt-2
"
>
1
,
234
<
/p
>


<
p

className
=
"
text-sm text-gray-600 mt-1
"
>+
12
%

from

last

month
<
/p
>


<
/div
>

);

// 2. A data table (with dropdown menu)

const

DataTable

=

()

=>

(


<
div

className
=
"
bg-white rounded-lg shadow
"
>


<
Table
>


{
/* table content */
}


<
/Table
>


<
DropdownMenu
>


<
DropdownMenuTrigger
>
Actions
<
/DropdownMenuTrigger
>


<
DropdownMenuContent
>


<
DropdownMenuItem
>
Edit
<
/DropdownMenuItem
>


<
DropdownMenuItem
>
Delete
<
/DropdownMenuItem
>


<
/DropdownMenuContent
>


<
/DropdownMenu
>


<
/div
>

);

// 3. A settings dialog

const

SettingsDialog

=

()

=>

(


<
Dialog
>


<
DialogTrigger

asChild
>


<
Button

variant
=
"
outline
"
>
Settings
<
/Button
>


<
/DialogTrigger
>


<
DialogContent
>


<
DialogHeader
>


<
DialogTitle
>
Settings
<
/DialogTitle
>


<
/DialogHeader
>


{
/* form content */
}


<
/DialogContent
>


<
/Dialog
>

);

Enter fullscreen mode

Exit fullscreen mode

### With Shadow DOM enabled:

StatsCard:✅ Works perfectly

* No portals
* All styles self-contained
* Bundle: +80KB (Tailwind CSS)

DataTable:⚠️ Partially broken

* Table looks good
* Dropdown menu broken (portal renders unstyled outside Shadow DOM)
* Bundle: +80KB (Tailwind CSS)

SettingsDialog:❌ Completely broken

* Button looks fine
* Dialog content appears but completely unstyled
* Backdrop might not work
* Bundle: +80KB (Tailwind CSS)

Total bundle cost:240KB of duplicated CSS for 3 components

### Without Shadow DOM:

Everything works:✅

* All portals work correctly
* Dropdown and dialog properly styled
* Bundle: 80KB (single Tailwind CSS file)

But:

* No style encapsulation
* Potential class name conflicts
* Global styles can leak in/out
* Need to be careful with specificity

## So What's The Answer?

### When Shadow DOM makes sense:

Good use cases:

// Simple, self-contained components

-

Cards

-

Badges

-

Progress

bars

-

Accordions

-

Tabs

-

Buttons
(
non
-
portal

variants
)

Enter fullscreen mode

Exit fullscreen mode

These components:

* Don't use portals
* Don't need complex interactions outside their boundary
* Benefit from style isolation

### When to skip Shadow DOM:

Skip it for:

// Components with portals or complex interactions

-

Dialogs

-

Popovers

-

Tooltips

-

Dropdown

menus

-

Context

menus

-

Toast

notifications

Enter fullscreen mode

Exit fullscreen mode

### Hybrid approach (what actually works):

// Option 1: Selective Shadow DOM

// Use Shadow DOM only for truly isolated components

const

CardWC

=

r2wc
(
Card
,

{

shadow
:

'
open
'

});

const

BadgeWC

=

r2wc
(
Badge
,

{

shadow
:

'
open
'

});

// Skip Shadow DOM for interactive components

const

DialogWC

=

r2wc
(
Dialog
,

{

shadow
:

null

});

const

DropdownWC

=

r2wc
(
Dropdown
,

{

shadow
:

null

});

Enter fullscreen mode

Exit fullscreen mode

// Option 2: No Shadow DOM, CSS Modules

// Use CSS Modules for scoping instead

import

styles

from

'
./Card.module.css
'
;

const

Card

=

()

=>

(


<
div

className
=
{
styles
.
card
}
>


{
/* Use scoped CSS instead of Shadow DOM */
}


<
/div
>

);

Enter fullscreen mode

Exit fullscreen mode

// Option 3: Scoped Tailwind (advanced)

// Generate component-specific Tailwind with prefixes

// tailwind.config.js

module
.
exports

=

{


prefix
:

'
card-
'
,

// All classes become card-bg-white, card-p-4, etc.


content
:

[
'
./src/Card.tsx
'
],

};

Enter fullscreen mode

Exit fullscreen mode

## The Uncomfortable Truth

Shadow DOM, Tailwind CSS, and shadcn/ui are all great technologies on their own. But together? They fight each other.

Shadow DOM wants:Complete isolationTailwind wants:Global utility classesshadcn/ui wants:Portals for proper z-index management

Pick two. You can't have all three working perfectly together.

### What we learned:

1. Bundle size matters- Duplicating Tailwind CSS across components gets expensive fast
2. Portals break Shadow DOM- Most modern UI libraries use portals heavily
3. CSS variables don't cross boundaries- Theming becomes complicated
4. CVA needs special handling- Dynamic classes require safelist configuration
5. There's always a tradeoff- Encapsulation vs. bundle size vs. functionality

### What worked for us:

We ended up with ahybrid approach:

* Skip Shadow DOM entirely for our use case
* Use TypeScript and component wrappers for type safety
* Accept the global stylesheet
* Let shadcn/ui portals work as intended
* Focus on clear component APIs instead of Shadow DOM encapsulation

Is it perfect? No. But it works, and that matters more than architectural purity.

## Resources

* Shadow DOM Spec
* Tailwind CSS
* shadcn/ui
* Radix UI Primitives
* Class Variance Authority

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)


For further actions, you may consider blocking this person and/orreporting abuse
