---
title: Eric Park
url: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/
site_name: hackernews_api
content_file: hackernews_api-eric-park
fetched_at: '2026-05-14T06:00:50.093536'
original_url: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/
author: ericswpark
date: '2026-05-13'
description: Eric Park's website
tags:
- hackernews
- trending
---

# My graduation cap runs Rust

 

### May 12, 2026

 
 

I’ve never graduated before. I mean, from college. So all the cap and gown stuff
is new to me.

Fun fact #1: you rent your cap and gown in the US. You have to return them. And
they’re expensive, too! I paid $94 just for the privilege of renting mine, which
is insane because they probably cost way less than that to manufacture. What if,
say, you say you’re fine without a cap and gown? Well, then you can’t walk in
the ceremony. So you do need to shell out to rent them. And they don’t give you
the option to buy the cap and gown outright.

OK, that’s not such a fun fact. How about:

Fun fact #2: when you graduate, they move your tassel from right to left to
signify… something? Why not left to right? What about left-handed people?!
Why are graduation ceremonies discriminating against left-handed people?!

Anyway. I was thinking about fun fact #2, and then I thought it might be cool if
my cap lit on fire as whoever it is moves my tassel. But the rental agreements
clause 98.c.2 probably forbids it, and I don’t think Purdue would like it very
much if I set the stage on fire.

Hmm. What if I made a contraption that detects when the tassel is moved away and
light up the bottom-side of the cap?

And with that, I got to building this crazy idea. And the end result is
beautiful if I do say so myself:

 

## FAQ

### What parts did you use?

* One Digispark ATtiny85
* 48 WS2812B LEDs
* Wires stripped from a dead Apple USB-C-to-C cable
* Reed switch and magnet to detect tassel movement (not shown in demo)
* A USB-C Power Delivery trigger board
* Power bank (and USB-C cable)

### How long did you spend on this thing?!

Writing the code took about 2 hours, mostly becauseavr-halandws2812-avrdo not support the ATtiny85 out of the box, at least not without a couple of
tweaks. I had to fork them and dirty-patch a couple of things, including setting
the default clock speed to 16 MHz.

It probably would’ve been easier if I didn’t use Rust and just used the Arduino
libraries, or if I used a different board. But I was really married to this blog
post title idea, and I was pretty sure a ESP32 board would’ve been overkill and
wouldn’t have stayed on the cap properly.

The hardware side took the longest, at 3+ hours. If anybody tells you hardware
is easy they’re wrong or they’re lying and have never worked on a custom
hardware project!

### Are you actually going to wear this to your graduation?

Heck no.

I thought about it but decided it looks pretty tacky. It looks like what kids
would think of as a gaming PC and what boomers would think of as a seizure.

### Speaking of seizure, there really was a missed opportunity…

…missed?

Warning: the following video contains rapid strobing of light. I’ve written
this out so people who are reading this with a screen reader know not to watch
the video!

 

WKUK eat your heart out

### Can I see the code?

https://github.com/ericswpark/gradcap-rs