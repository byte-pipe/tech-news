---
title: 'What an unprocessed photo looks like: (Maurycy''s blog)'
url: https://maurycyz.com/misc/raw_photo/
site_name: hackernews_api
fetched_at: '2025-12-30T11:07:06.217682'
original_url: https://maurycyz.com/misc/raw_photo/
author: zdw
date: '2025-12-28'
description: What an unprocessed photo looks like
tags:
- hackernews
- trending
---

# What an unprocessed photo looks like:

Dec 27, 2025

(
Photography
)

Here’s a photo of a Christmas tree, as my camera’s sensor sees it:

Sensor data with the 14 bit ADC values mapped to 0-255 RGB.

It’s not even black-and-white, it’s gray-and-gray.

This is becuase while the camera’s analog-to-digital converter (ADC) output can theoretically output values from 0 to 16382, the data doesn’t cover that whole range:

Histogram of raw image

The real range of ADC values is ~2110 to ~136000.
Let’s set those values as the white and black in the image:

Vnew= (Vold- Black)/(White - Black)

Progress

Much better, but it’s still more monochromatic then I remember the tree being.
Camera sensors aren’t actually able to see color: They only measure how much light hit each pixel.

In a color camera, the sensor is covered by a grid of alternatingcolor filters:

Let’s color each pixel the same as the filter it’s looking through:

Bayer matrix overlay

This version is more colorful, but each pixel only has one third of its RGB color.

To fix this, I just averaged the values each pixel with its neighbors:

Demosaicing results

Applying this process to the whole photo gives the lights some color:

Demosaiced tree

However, the image is still very dark.
This is because monitors don’t have as much dynamic range as the human eye, or a camera sensor:
Even if you are using an OLED, the screen still has some ambient light reflecting off of it and limiting how black it can get.

There’s also another, sneakier factor causing this:

True linear gradient

Our perception of brightness is non-linear.

If brightness values are quantized, most of the ADC bins will be wasted on nearly identical shades of white while every other tone is crammed into the bottom.
Because this is an inefficient use of memory, most color spaces assign extra bins to darker colors:

sRGB gradient

As a result of this, if the linear data is displayed directly, it will appear much darker then it should be.

Both problems can be solved by applying a non-linear curve to each color channel to brighten up the dark areas… but this doesn’t quite work out:

ohno

Some of this green cast is caused by the camera sensor being intrinsically more sensitive to green light, but some of it is my fault:
There are twice as many green pixels in the filter matrix.
When combined with my rather naive demosaicing, this resulted in the green channel being boosted even higher.

In either case, it can fixed with proper white-balance:
Equalize the channels by multipling each one with a constant.

However, because the image is now non-linear, I have to go back a step to do this.
Here’s the dark image from before with all the values temporarily scaled up so I can see the problem:

… here’s that image with the green taken down to match the other channels:

Banishing the green

… and after re-applying the curve:

Finally: A decent photo.

This is really just the bare minimum:
I haven’t done any color calibration, the white balance isn’t perfect, the black points are too high, there’s lots of noise that needs to be cleaned up…

Additionally, applying the curve to each color channel accidentally desaturated the highlights.
This effect looks rather good — and is what we’ve come to expect from film — but it has de-yellowed the star.
It’s possible to separate the luminance and curve it while preserving color.
On its own, this would make the LED Christmas lights into an overstaturated mess, but combining both methods can produce nice results.

For comparison, here’s the image my camera produced from the same data:

"in camera" JPEG image.

Far from being an “unedited” photo: there’s a huge amount of math that’s gone into making an image that nicely represents what the subject looks like in person.

There’s nothing that happens when you adjust the contrast or white balance in editing software that the camera hasn’t done under the hood.
The edited image isn’t “faker” then the original: they are different renditions of the same data.

In the end, replicating human perception is hard, and it’s made harder when constrained to the limitations of display technology or printed images.
There’s nothing wrong with tweaking the image when the automated algorithms make the wrong call.
