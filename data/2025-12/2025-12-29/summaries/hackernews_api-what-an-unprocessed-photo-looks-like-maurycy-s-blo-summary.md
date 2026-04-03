---
title: "What an unprocessed photo looks like: (Maurycy's blog)"
url: https://maurycyz.com/misc/raw_photo/
date: 2025-12-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-29T11:16:25.030592
screenshot: hackernews_api-what-an-unprocessed-photo-looks-like-maurycy-s-blo.png
---

# What an unprocessed photo looks like: (Maurycy's blog)

## What an Unprocessed Photo Looks Like

A photo of a Christmas tree taken with a camera sensor shows a black-and-white image due to the limitations of analog-to-digital conversion (ADC) on board. The sensor can only output values from 0 to 16382, which is insufficient for representing the full color spectrum.

## Mapping Raw Image Data to Color Representation
To achieve better results, the image data should be mapped to a more suitable range that spans from 0-255 in the RGB color space. This is done by calculating `Vnew = (Vold - Black) / (White - Black)` and setting white and black as the minimum and maximum values of V_new.

## Color Reconstruction Using Bayer Matrix Overlay
Color can be effectively reconstructed using a Bayer matrix overlay, which simulates how cameras measure light hitting pixels. By averaging pixel values with their neighbors, it produces a more colorful image without losing detail.

## Demosaicing Results
To enhance highlights in the image, demosaicing is applied to reconstruct missing color information for each pixel. This process allows light to be allocated across all three axes (x, y, and z) rather than treating different areas of an image as having only one hue.

## Dynamic Range Limitation on Monitors
Monitors with lower dynamic range can limit the perceived brightness in photographs by not having enough black-to-white contrast ratio. They also lack high-contrast ambient light effects due to their color limitations.

## Non-Linearity in True Linear Gradient
The true linear scale of image data is constrained when displayed directly as it would appear darker or less bright. To overcome this limitation, a non-linear transformation should be applied by multiplying each channel with a constant value to adjust the perceived brightness range accurately.

## Color Calibration Requires Adjustments
For photographs that are color calibrated, adjustments must be made to account for non-linearity in the transformed image data. This helps ensure accurate representation of colors and preserves true nuances between hues as seen by cameras and monitors alike.
