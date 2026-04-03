---
title: 'CSS Only: Infinite Office - DEV Community'
url: https://dev.to/alvaromontoro/css-only-infinite-office-28oe
site_name: devto
fetched_at: '2025-08-03T01:05:03.324971'
original_url: https://dev.to/alvaromontoro/css-only-infinite-office-28oe
author: Alvaro Montoro
date: '2025-07-27'
description: CSS Art of an office and a person waving, created with CSS and not a single HTML tag. Tagged with frontendchallenge, devchallenge, css.
tags: '#frontendchallenge, #devchallenge, #css'
---

Frontend Challenge CSS Art Submission

This is a submission forFrontend Challenge: Office Edition sponsored by Axero, CSS Art: Office Culture.

## Inspiration

The image in itself was inspired by thisillustration on Shutterstock. And I started coding it, but as I progressed I noticed it was missing something.

I've worked in many offices, some were not-great and some were amazing. But what really mattered in the end was not the space but who I shared it with. An empty office is just that, an empty space with objects. The drawing needed some "human touch". Because of that, I used the pseudo-elements to add a person... but more on that later.

## Demo

I recommend you go to theCodePen details page, because it allows to easily resize the preview window vertically, so you'll be able to see more of the drawing.

But here's a live demo and the source code:

The demo above has the person "hardcoded" into the:rootinstead of in the::beforeand::after. This is because I found that using the pseudo-elements for this type of drawing takes a HUGE hit on performance. You can check theanimated version with pseudo-elements on this other pen(uncomment the animation at the bottom at your own peril :P).

## Journey

It's not the first time that I try to do an "infinite" CSS drawing using only CSS without HTML elements (I've been coding on-and-off this cityscape for a while), but this is the one I've done the fastest.

The idea is to create a drawing that goes on and on indefinitely. To achieve this, I used background with different sizes, so when they repeat, the pattern between them is not so obvious (although sometimes it is).

The twist: the drawing is just CSS. No HTML or JS. Some people may say "but you need HTML to include CSS" and that's normally the case (even in this demo, CodePen is adding a<body>), but there are (hacky) ways of executing CSS by itself (I've done something like that with Apache and Firefox). Anyway, the thing is that if you check the code on CodePen, you'll only see CSS.

This is a time-lapse of me coding the drawing on CodePen:

As I mentioned above, an empty office is just that, what really makes or breaks na office is the people who work in it. So I needed to add a human. And I thought about a friendly version of me waving at the viewer.

I drew the person with the pseudo-elements because that way I would be able to add some animations, but in the end I didn't (I did but performance downgraded and chose to remove them). Had I known it was going to go that way, maybe I would have drawn two people. If you want to see the animation, it is commented in the code (towards the end).

## License

This work is licensed under aCreative Commons Attribution-NonCommercial 4.0 License. This means that you are free to copy, reuse, and modify the drawing (non-commercially) as long as you give appropriate credit to the author.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
