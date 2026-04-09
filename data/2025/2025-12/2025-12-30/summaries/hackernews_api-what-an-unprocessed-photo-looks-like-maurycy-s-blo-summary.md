---
title: "What an unprocessed photo looks like: (Maurycy's blog)"
url: https://maurycyz.com/misc/raw_photo/
date: 2025-12-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-30T11:18:05.484887
screenshot: hackernews_api-what-an-unprocessed-photo-looks-like-maurycy-s-blo.png
---

# What an unprocessed photo looks like: (Maurycy's blog)

## What an Unprocessed Photo Looks Like

### Image Description
The article discusses the challenges of capturing color images using a camera's sensor. The photographer uses a combination of demosaicing and white-balance techniques to improve the image quality.

### Key Points

* Camera sensors measure light intensity, not human perception
* Alternating color filters can affect the perceived color
* Demosaicing alone is insufficient for accurate color representation
* True linear gradient causes dark areas in the image
* Incorrect white-balancing can amplify the green channel and create a false colorcast
* White-balance correction and demosaicing provide a solution to these issues

### Technical Details
* Camera sensor ADC values range from 0 to 16382, but not all values are used
* White and black levels are set using Vnew equation
* Demosaiced image appears less colorful due to limited dynamic range
* True linear gradient is a problem in color representation
* Non-linear white-balance correction can lead to color casts

### Color Calibration Solutions
* Using a white balance tool or app
* Demosaicing with additional calculations for specific colors (green, red)
* Applying a non-linear curve to the color channels
