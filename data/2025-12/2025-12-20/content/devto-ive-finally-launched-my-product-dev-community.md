---
title: I've FINALLY launched my Product!! - DEV Community
url: https://dev.to/nombrekeff/ive-finally-launched-my-product-4am7
site_name: devto
fetched_at: '2025-12-20T11:06:45.226050'
original_url: https://dev.to/nombrekeff/ive-finally-launched-my-product-4am7
author: Keff
date: '2025-12-16'
description: Cardboard.js is now on Product Hunt Hi everyone, After years of working on Cardboard.js,... Tagged with webdev, devjournal, watercooler, product.
tags: '#watercooler, #webdev, #devjournal, #product'
---

## Cardboard.js is now on Product Hunt

Hi everyone,

After years of working onCardboard.js, I’ve finally launched it onProduct Hunt. This project started as a way to build small, interactive web appswithout writing HTML, JSX, or separate CSS files— you write everything in plain JavaScript or TypeScript and let Cardboard handle rendering and reactivity.

If you’ve followed my earlier posts about building this framework, thanks for sticking around. If not, here’s a quick intro and a few snippets to show what it feels like to use.

## What Cardboard.js Is

Cardboard.js is alightweight reactive UI library(~16 KB), focused on simplicity and performance. It provides:

* No HTML required— you generate DOM elements with JS.
* Built‑in state management.
* Reactive updates(UI updates when state changes).
* Reusable componentsandCSS‑in‑JSstyle support.

## Quick Snippets

### Basic Usage

Instead of writing HTML, you initialize the framework and define UI with JavaScript:

import

{

tag
,

init
,

allTags

}

from

'
@nkeff/cardboard-js
'
;

const

{

div
,

p

}

=

allTags
;

// Initialize Cardboard (defaults to <body>)

const

root

=

init
();

// Append elements

root
.
append
(


div
(


p
(
'
Hello world!
'
)


)

);

Enter fullscreen mode

Exit fullscreen mode

This creates and attaches the DOM for you without a template file — everything lives in code.

### A Simple Reactive Counter

Cardboard includes reactive state primitives so your UI updates automatically:

const

Counter

=

()

=>

{


const

count

=

state
(
0
);


return

button
()


.
text
(
`Clicked $count times`
,

{

count

})


.
addStyle
(
'
color
'
,

'
gray
'
)


.
stylesIf
(
count
.
greaterThan
(
5
),

{

color
:

'
red
'

})


.
clicked
(()

=>

count
.
value
++
);

};

// Mount it to the body

tag
(
'
(body)
'
).
append
(
Counter
());

Enter fullscreen mode

Exit fullscreen mode

Here you define a component function that returns UI with reactive state. Ascount.valuechanges, the text and styles update automatically.

## Why It Matters

If you’ve worked with frameworks where you juggle templates, build steps, and lots of boilerplate, Cardboard offers asimpler alternativewhere logic and UI live together in plain JavaScript or TypeScript. It’s small, fast, and doesn’t need HTML, CSS, or JSX if you don’t want them.

## How You Can Help

If you think this could be useful — or even just interesting — I’d love your support on Product Hunt. A visit, upvote, or comment goes a long way and helps this project get more visibility.

producthunt.com

Thanks for reading — and if you try it out, I’d really like to hear what you build with it.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
