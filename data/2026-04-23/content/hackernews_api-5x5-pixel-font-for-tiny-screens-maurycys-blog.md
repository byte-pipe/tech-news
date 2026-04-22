---
title: 5x5 Pixel font for tiny screens (Maurycy's blog)
url: https://maurycyz.com/projects/mcufont/
site_name: hackernews_api
content_file: hackernews_api-5x5-pixel-font-for-tiny-screens-maurycys-blog
fetched_at: '2026-04-23T09:44:23.676640'
original_url: https://maurycyz.com/projects/mcufont/
author: zdw
date: '2026-04-20'
description: 5x5 Pixel font for tiny screens
tags:
- hackernews
- trending
---

# 5x5 Pixel font for tiny screens

2026-04-18
 — 
2026-04-20
 (
Programming
) 

Font data (C header)

All characters fit within a 5 pixel square, and are safe to draw on a 6x6 grid.
The design is based off of lcamtuf's 5x6 font-inline.h, which is itself inspired by the ZX Spectrum's 8x8 font.

5x5 is the smallest sizethat doesn't compromise legibility:

* 2x2: Impossible.3x3: Technically possible, but unreadable.4x4: Not enough to draw "E", "M" or "W" properly.5x5: This font.
* 3x3: Technically possible, but unreadable.
* 4x4: Not enough to draw "E", "M" or "W" properly.
* 5x5: This font.

Five by five is actually big enough to draw most lowercase letters one pixel smaller, making them visually distinct from uppercase.

Narrower 4x5 and 3x5 dimensions are possible, but would require sacrificing the M,
dotted zero, and reduce U/V/Y distinctiveness.

There's no artistic reason to make all characters five wide just because a few must be...
but a using a constant width makes programming a lot easier:
The length of a string on screen is always 6 times the number of characters.

It also makes compact layouts much safer:
There's no need to worry that a number will overflow because "8978" is longer than "1111".

The whole font takes up just 350 bytesof memory,
which makes it ideally suited to 8-bit microcontrollers like the AVR128DA28 (16 kB of RAM)
These are cheap, low power and robust...
but they fall short on graphics:

Even a low-resolution 384x288 display has 110 thousand pixels:
way too big to fit in the AVRs memory.

... except most projects don't need anywhere near that many pixels.
A 160x128 or 128x64 OLED is more practical and cheaper —
but these need hand-drawn, pixel-efficient fonts to make good use of them.

For reference, here's a vector fontrendered at a similar scale:

Actually 6 tall, but the letters are narrower, so I'll allow it.

Antialiasing, several megabytes of code, a megabyte of font data, and it's still terrible compared 350 hand-crafted bytes.

# Realpixels:

Pixels aren't perfect squares, so the font won't actually look like the rendering at the top of this post:
This is it on an actual screen:

I actually really like the pseudo-dropshadow effect created by the subpixels.
This won't happen on monochrome displays, but the font will still look smoother than you might expect.

The gaps between pixels really help sell the "e" and "g", but this same effect should allow...

# Evensmallerfonts:

While 5x5 is the smallest no-compromise resolution, a 3x5 isn't too bad:

There are 32,768 glyphs at this size. (27,904 are distinct)

The "M", "W" and "Q" suffer, but it's still got a distinct O and zero.
Something like this might actually be a good option if you need to cram (50%) more columns into a display.

That's still readable, so what about3x4?

There are 4,096 glyphs at this size. (3,392 are distinct)

At this size, there's no way to have a distinct upper and lowercase, so I've picked whatever style works the best in the limited space.
The numbers have also taken a hit, but still work ok.

How about3x3?

There are 512 glyphs at this size. (400 are distinct)

The main loss was the numbers, but the letters don't include any duplicates and are somewhat recognizable.

This font is hugely improved by being displayed on real hardware:

That means it's still too big. How about2x3?

There are 64 glyphs at this size. (44 are distinct)

Ok, this is getting ridiculous.
Most letters are unrecognizable, and there are quite a few duplicates.
In case you couldn't tell, the bottom line reads "Hello World".

Flipping the aspect ratio to a3x2makes it a lot better:

There are 64 glyphs at this size. (44 are distinct)

Simulated pixel grid

More letters have horizontal detail (M, W, N, Q, G, P, etc) then have vertical detail (E, F).
The bottom line reads "you can probably read this", although you might have to squint or zoom out.

... and for the sake of completeness, a2x2:

There are 16 glyphs at this size. (10 are distinct)

On paper, there are 16 possible 2x2 images, but one of them is blank and 5 of them are shifted copies of another one.
That leaves 10, just enough to do all the digits...
but because they have no resemblance to the originals, it's more of a secret code than a font.# Related:/projects/mcufont/mcufont.h: The 5x5 font./projects/mcufont/test.c: Program to preview the font.https://lcamtuf.coredump.cx/soft/embedded/font-inline.h: The original font.https://moonbench.xyz/projects/tiny-pixel-art-fonts/: More tiny fonts.