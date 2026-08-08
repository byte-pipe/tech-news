---
title: 'The Comfort Atlas: What Does Home Taste Like? - DEV Community'
url: https://dev.to/ale3oula/the-comfort-atlas-what-does-home-taste-like-3a6i
site_name: devto
content_file: devto-the-comfort-atlas-what-does-home-taste-like-dev-co
fetched_at: '2026-08-08T19:27:39.755133'
original_url: https://dev.to/ale3oula/the-comfort-atlas-what-does-home-taste-like-3a6i
author: Alexandra
date: '2026-08-01'
description: This is a submission for Frontend Challenge - Comfort Food Edition, Perfect Landing What I... Tagged with devchallenge, frontendchallenge, webdev, javascript.
tags: '#devchallenge, #frontendchallenge, #webdev, #javascript'
---

Frontend Challenge Perfect Landing Submission 🍲🥧

This is a submission forFrontend Challenge - Comfort Food Edition, Perfect Landing

## What I Built

The Comfort Atlas is a spinning 3D globe of comfort food from ~100 countries.

Virtually travel the globe and have a taste of the comfort foods from 100~ countries. Moussaka in Greece, Jollof Rice in Nigeria, Pho in Vietnam. There is also a "featured dish of the day" that rotates deterministically so it's the same for everyone visiting that day. And the fun feature: visitors can type in their own comfort dish and generate a downloadable, passport-stamp-style card in one of three color styles.

## Demo

https://comfort-atlas.netlify.app/

## Journey

I started with a flat SVG world map, clickable countries, keyboard support, a hover tooltip on the map, all built on realelements so accessibility came for free. It worked fine, but it looked very meh.

So i decided to try something i have never done before. Make a globe! I usedcobewhich promised a 3D globe out of the box. First attempt rendered absolutely nothing but floating dots. 😂 With a lot of the help of my friend claude, we found out that their docs are outdated, and there is acreateGlobe()that draws exactly one synchronous frame and expects you to drive a requestAnimationFrame loop calling .update() yourself.

Two things on the globe I'm proud of, because neither had any library support: a hover tooltip that tracks a marker in 3D space, and a fading "trail" of great-circle arcs between the countries you've visited. Both came down to translating the projection math out of a minified bundle into something readable.

What I would do next: dark mode, enrich the content, comfort food battles per country.

What I learned: a lot about accessibility in 3D/canvas, which is so much more difficult than the 2d one, one check for a11y is never enough. Maps are hard, and getting something to track a moving 3D object from regular DOM is even harder.

Licensed under MIT

Fun fact: I don't like Moussaka, even though i am greek, my comfort food is Pizza or Giouvetsi. xD

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse