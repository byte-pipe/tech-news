---
title: The Cascade
url: https://thecascade.dev/article/least-amount-of-css/
site_name: hackernews_api
fetched_at: '2025-10-07T11:09:19.660408'
original_url: https://thecascade.dev/article/least-amount-of-css/
author: loughnane
date: '2025-10-06'
description: Sharing CSS tips, tricks, and best practices
tags:
- hackernews
- trending
---

The fun part of making a website is that if you write your HTML and nothing else, you have a responsive website.

Granted, if you have images they can cause some overflow issues.

So we can start things off by fixing that:

img

{


max-width
:
 100%
;


display
:
 block
;

}

It’s possible you have videos or SVGs that are also causing problems (less likely with SVGs though), so if you need, you can expand upon this a little bit.

img,
svg,
video

{


max-width
:
 100%
;


display
:
 block
;

}

## Improving the typography

The first thing we can do is change the font family since the default is never very exciting.

We’ll just use a basicsystem-uifor this example. It has pretty good support these days, and looks good on every system without having to worry about loading in any extra fonts.

In general, the font-size is a little small as well, so we can bump it up, and the default line-height is always a bit tight, so anything within the 1.5 to 1.7 range should do:

body

{


font-family
:
 System UI
;


font-size
:
 1.25rem
;


line-height
:
 1.5
;

}

Though not perfect, this is already a huge improvement over the regular defaults.

## Adding Dark Mode Support

Many people love dark mode, so let’s enable it based on a user’s system preferences.

We can do this by using thecolor-schemeproperty:

html

{


color-scheme
:
 light dark
;

}

This will set the user-agent-styles to either a light or dark theme, based on the users system preferences.

If you’d prefer, we can do this without CSS as well!

<
html

lang
=
"
en
"

color-scheme
=
"
light dark
"
>
</
html
>

### A small note on following the system preferences

While this is really handy, it is a best practice to allow users to manually toggle the color-scheme as well.

Some people prefer a dark system theme, but light website themes, and vice-versa.

## Restraining Content Width

Line-length is one of the most important things when it comes to the readability of text.

We generallywant to try and fall somewhere in the 45-90 characters per line range(for body text, not headlines).

To make the website more readable, we’ll limit the content width using amainelement and some CSS magic:

main

{


max-width
:

min
(
70ch
,
 100% - 4rem
)
;


margin-inline
:
 auto
;

}

Themin()function here will pick whatever is smallest, either70chor100% - 4rem. Because we are inside amin()function, we don’t need to use acalc().

Whatever the output from that min() function, the width is less than 100%, so the page will be stuck to the left side of the viewport.

We can then use margin-inline: auto to center it, as this acts on the margins on the inline axis, so in any horizontal writing modes, that means both the margin-left and margin-right are auto.

You might want to switch out the main selector for a .container or .wrapper so you can have more control over where you use it.

And with that, our final CSS file looks like this:

html

{


color-scheme
:
 light dark
;

}

body

{


font-family
:
 system-ui
;


font-size
:
 1.25rem
;


line-height
:
 1.5
;

}

img,
svg,
video

{


max-width
:
 100%
;


display
:
 block
;

}

main

{


max-width
:

min
(
70ch
,
 100% - 4rem
)
;


margin-inline
:
 auto
;

}

## Build on top of this

This is just a quick start to get things off the ground, though it could be used for a very simple page as well.

For the most part, though, you’ll probably want to build on top of this, but it should be able to act as a nice jumping off point!


Link copied to clipboard
