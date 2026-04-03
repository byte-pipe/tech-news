---
title: SVGs that feel like GIFs | Vincent D. Warmerdam
url: https://koaning.io/posts/svg-gifs/
site_name: hackernews
fetched_at: '2025-07-09T10:19:52.839608'
original_url: https://koaning.io/posts/svg-gifs/
author: cantdutchthis
date: '2025-07-09'
published_date: '2025-07-07'
description: The moving image below is only 49Kb and has an incredibly high resolution. It's similar to a GIF but instead of showing moving images, it shows moving SVGs!
---

# SVGs that feel like GIFs

2025-07-07

The moving image below is only 49Kb and has an incredibly high resolution.

It's similar to a GIF but instead of showing moving images, it shows moving SVGs! The best part: Github supports these in their README.md files!

Getting these to work involvesasciinemaandsvg-term-cli. After uploading the asciinema you can use the tool to download a file that you can immediately click and drag into a README. It's something that I'm using extensively onbespoken.

## How it works?

I was surpised to learn that moving SVGs were even a thing. But then I was reminded that animations are built intothe svg spec.

* <animate>- animates individual attributes over time
* <animateTransform>- animates transformations like rotation, scaling, translation
* <animateMotion>- moves elements along a path

This is what thesvg-term-clileverages under the hood.

## Related Posts

### the LLM pizza pattern

2025-07-08

### just is just amazing

2025-07-04

### Giving daytona.io a spin

2025-07-03

### uvx pattern for two tiers of open work

2025-06-30
