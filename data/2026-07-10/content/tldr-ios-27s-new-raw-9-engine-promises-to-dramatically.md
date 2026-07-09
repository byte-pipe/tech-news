---
title: iOS 27’s new RAW 9 engine promises to dramatically improve photo quality - 9to5Mac
url: https://9to5mac.com/2026/07/06/apple-overhauls-raw-photo-processing-with-ios-27-showcases-impressive-results/
site_name: tldr
content_file: tldr-ios-27s-new-raw-9-engine-promises-to-dramatically
fetched_at: '2026-07-10T09:09:42.617868'
original_url: https://9to5mac.com/2026/07/06/apple-overhauls-raw-photo-processing-with-ios-27-showcases-impressive-results/
author: Marcus Mendes
date: '2026-07-10'
published_date: '2026-07-06T22:52:54+00:00'
description: Apple is introducing a new version of its system-level RAW image processing engine that uses machine learning to greatly improve detail and reduce noise.
tags:
- tldr
---

* iOS 27
* photos

# Apple overhauls RAW photo processing with iOS 27, showcases impressive results

 

Marcus Mendes
 | Jul 6 2026 - 3:52 pm PT																

With iOS 27 and its companion systems, Apple is introducing a new version of its system-level RAW image processing engine. It uses machine learning to greatly improve detail and reduce noise, including when reprocessing older RAW photos. Here are the details.

## iOS 27 to include RAW 9

If you’re not familiar with RAW, it is basically an image format that preserves the data captured directly by a camera’s sensor, giving photographers greater flexibility when editing elements such as exposure, color, and white balance.

Apple has its own system-level pipeline for processing RAW files from third-party cameras, exposed to apps through Core Image. It currently includes support and camera-specific calibrations for nearly 800 camera models, with the full and regularly updated compatibility list availablehere.

Over the years, Apple has updated its RAW processing algorithm eight times, improving how it handles sensor data, demosaicing, denoising, and adjustments such as white balance, exposure, color, and tone.

With iOS 27, macOS 27, iPadOS 27 and beyond, Apple is introducing RAW 9, which the company says is “its biggest update yet.” Here’s David Hayward, Core Image Engineer at Apple, on theWWDC26sessionEnhance RAW image processing with Core Image:

[RAW 9] dramatically improves the rendering of RAW files. It is built atop a tiled CoreML model, that combines demosaic with denoise for best quality. And the model is run on device using the Apple Neural Engine cores, for optimal performance.

In the session, Hayward shows several examples of RAW 9 in action, comparing the results with RAW 8 and, occasionally, the original, unprocessed sensor data:

This is a zoomed-in crop of a low noise image using RAW 8. This Sony Alpha 7 II image of a vintage dial indicator actually looks quite good. However, when you explore that same image under RAW 9, the image is sharper, clearer, and the fine text is easier to read.

The differences are even more dramatic, when you view high noise images. First, observe the actual RAW data that is contained in this very noisy ISO 51,200 image. In this example from a Canon 5D Mark III, the image is a 10x Crop of a box of crayons. There is so much luma and chroma noise in the RAW data, that it’s impossible to discern the unique color of each crayon. Using our previous algorithms, this is the result! RAW 8 did an acceptable job of recovering the actual colors in the scene. But if you examine the results under RAW 9, the output is significantly better. The colors are accurate and well defined. Even the shiny specular highlights on the crayons are visible.

This last example is a crop of a photo of embroidery yarn, shot with a Fujifilm X-T5 at ISO 12,800. This camera has a non-traditional sensor pattern, which is challenging to demosaic. In the RAW 8 results, there are some color artifacts and loss of detail in the yarn. But if you observe the same image under RAW 9, the results are discernibly better. The small text is more legible, and the texture in the yarn much clearer.

For developers, the session goes into detail on how to enable RAW 9, optimize performance for editing and exporting, and much more.

To learn more about RAW 9 and the other Core Image improvements coming with iOS 27,watch the full session here.

#### Worth checking out on Amazon

* Geoffrey Cain – ‘Steve Jobs in Exile’
* David Pogue – ’Apple: The First 50 Years’
* MacBook Neo
* Logitech MX Master 4
* AirPods Pro 3
* AirTag (2nd Generation) – 4 Pack
* Apple Watch Series 11
* Wireless CarPlay adapter

FTC: We use income earning auto affiliate links.More.

You’re reading 9to5Mac — experts who break news about Apple and its surrounding ecosystem, day after day. Be sure to check out 
our homepage
 for all the latest news, and follow 9to5Mac on 
Twitter
, 
Facebook
, and 
LinkedIn
 to stay in the loop. Don’t know where to start? Check out our 
exclusive stories
, 
reviews
, 
how-tos
, and 
subscribe to our YouTube channel
 

Check out 9to5Mac on YouTube for more Apple news:

 

## Comments

## Guides

### iOS 27

### photos

## Author

 

			Marcus Mendes		

https://www.threads.com/mvcmendes			

Marcus Mendes is a Brazilian tech podcaster and journalist who has been closely following Apple since the mid-2000s.

He began covering Apple news in Brazilian media in 2012 and later broadened his focus to the wider tech industry, hosting a daily podcast for seven years.