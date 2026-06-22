---
title: help i accidentally a wigglegram
url: https://lmao.center/blog/wiggle-accidents/
site_name: hackernews_api
content_file: hackernews_api-help-i-accidentally-a-wigglegram
fetched_at: '2026-06-22T13:05:24.775673'
original_url: https://lmao.center/blog/wiggle-accidents/
author: gregsadetsky
date: '2026-06-20'
description: Help I accidentally a wigglegram
tags:
- hackernews
- trending
---

<<< older

lmaocenter

 ~ 

blog

## help i accidentally a wigglegram

Do you know what awigglegramis?

↳ c. "suavecorn" on reddit

It is a kind of stereo image you make by looping frames together, like as a GIF.

↳ c. "aka_hochstapler" on reddit

The effect is quite convincing.

↳ c. "suavecorn" on reddit

I am something of an indecisive photographer and when I like an angle I will take a lot of frames, from slightly different angles etc., looking for "the shot". And since I am also a bit of a hoarder I never clear out my camera roll.

"Same shot from different angles"? You know what that sounds a bit familiar.

↳ scrollin'

Sure enough my phone is full of wigglegrams that I took by accident. Years' worth, waiting for me to sit down and stitch them together.

Or, perhaps, forsomethingto stitch them together. It occurred to me last weekend that I can useperceptual hashing- what TinEye (et al.) uses for reverse image search - to try and find runs of similar images and pull them out from my library automatically. So I wrote a little script to hash all my pictures:

↳ slowly, slowly

Hashing is quick but downloading photos from iCloud is not.

The result is a hash that - unlike a cryptographic function like sha1 - will share more bits with hashes of similar-looking images than with dissimilar ones. We can use that to calculate the hamming distance between pairs of images and find a threshold:

↳ ten seems like a good boundary

And extract pairs:

↳ plausible...

And hundreds of wigglegrams spew forth.

↳ space mountain?

↳ block island

↳ deland

↳ probably also disney?

A few of them I am guilty of taking intentionally. But most are true accidents. As such many of them come out as less "stereoscopic" and more "kinescopic" - like little unintentional movies.

↳ notting hill

↳ perugia

Animals are a natural fit for the concept, unpredictable as they are:

↳ cat

↳ another cat

↳ dog

↳ pigeon

Design-work also. (I am always indecisive.)

↳ ipad sidecar I should write on

↳ baby book

↳ same but doing a rad flip

↳ resistor bridge

↳ leg in pieces

And sculpture:

↳ olivetti

↳ charlotte?

↳ frog with a joint

What fun. I have the script up onGithubif you want to play with it - it'll work on your iCloud photos library if you're on a Mac, or you can point it at a directory of pictures otherwise.

Cheers~

↳ and happy birthday ig

<<< older

home
 ~ posted june 04 2026