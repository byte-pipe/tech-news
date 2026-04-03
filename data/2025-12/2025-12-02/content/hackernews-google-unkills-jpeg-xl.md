---
title: Google *unkills* JPEG XL?
url: https://tonisagrista.com/blog/2025/google-unkills-jpegxl/
site_name: hackernews
fetched_at: '2025-12-02T11:08:03.045890'
original_url: https://tonisagrista.com/blog/2025/google-unkills-jpegxl/
author: Toni Sagrista Selles
date: '2025-12-02'
description: A quick summary of the format's road to stardom
---

I’ve written about JPEG XL in the past. First, I notedGoogle’s move to kill the format in Chromiumin favor of the homegrown and inferior AVIF.12Then, I had a deeper look at the format, and visuallycompared JPEG XL with AVIFon a handful of images.

The latter post started with a quick support test:

“If you are browsing this page around 2023, chances are that your browser supports AVIF but does not support JPEG XL.”

Well, here we are at the end of 2025, and this very sentence still holds true. Unless you are one of the 17% of users using Safari3, or are adventurous enough to use a niche browser likeThorium,LibreWolfor the newerZen Browser, chances are you see the AVIF banner in green and the JPEG XL image in black/red.

The good news is, this will change soon. In a dramatic turn of events, the Chromium team has reversed itsObsoletetag, and has decided to support the format in Blink (the engine behind Chrome/Chromium/Edge). Given Chrome’s position in the browser market share, I predict the format will become ade factorstandard for images in the near future.

## Let’s recap

I’ve been following JPEG XL since its experimental support in Blink. What started as a promising feature was quickly axed by the team in a bizarre and ridiculous manner. First, they asked the community for feedback on the format. Then, the community responded very positively. And I don’t only mean a couple of guys in their basement.Meta,Intel,Cloudinary,Adobe,ffmpeg,libvips,Krita, and many more. After that came the infamous comment:

da...@chromium.orgda...@chromium.org

#85 Oct 31, 2022 12:34AM

Thank you everyone for your comments and feedback regarding JPEG XL. We will be removing the JPEG XL code and flag from Chromium for the following reasons:

* Experimental flags and code should not remain indefinitely
* There is not enough interest from the entire ecosystem to continue experimenting with JPEG XL
* The new image format does not bring sufficient incremental benefits over existing formats to warrant enabling it by default
* By removing the flag and the code in M110, it reduces the maintenance burden and allows us to focus on improving existing formats in Chrome

Yes, right, “not enough interest from the entire ecosystem”. Sure.

Anyway, following this comment, a steady stream of messages pointed out how wrong that was, from all the organizations mentioned above and many more. People were noticing in blog posts, videos, and social media interactions.

Strangely, the following few years have been pretty calm for JPEG XL. However, a few notable events did take place. First, the Firefox teamshowed interest in a JPEG XL Rust decoder, after describing their stance on the matter as “neutral”. They were concerned about the increased attack surface resulting from including the current 100K+ lines C++libjxlreference decoder, even though most of those lines are testing code. In any case, they kind of requested a “memory-safe” decoder. This seems to have kick-started the Rust implementation,jxl-rs, from Google Research.

To top it off, a couple of weeks ago, the PDF Association announced their intent to adopt JPEG XL as a preferred image format in their PDF specification. The CTO of the PDF Association, Peter Wyatt, expressed their desire to include JPEG XL as the preferred format for HDR content in PDF files.4

## Chromium’s new stance

All of this pressure exerted steadily over time made the Chromium team reconsider the format. They tried to kill it in favor of AVIF, but that hasn’t worked out. Rick Byers, on behalf of Chromium,made a commentin the Blink developers Google group about the team welcoming a performant and memory-safe JPEG XL decoder in Chromium. He stated that the change of stance was in light of the positive signs from the community we have exposed above (Safari support, Firefox updating their position, PDF, etc.). Quickly after that, theChromium issuestate was changed fromObsoletetoAssigned.

## About JPEG XL

This is great news for the format, and I believe it will give it the final push for mass adoption. The format is excellent for all kinds of purposes, and I’ll be adopting it pretty much instantly for this and the Gaia Sky website when support is shipped. Some of the features that make it superior to the competition are:

* Lossless re-compression of JPEG images. This means you can re-compress your current JPEG library without losing information and benefit from a ~30% reduction in file size for free. This is a killer feature that no other format has.
* Support for wide gamut and HDR.
* Support for image sizes of up to 1,073,741,823x1,073,741,824. You won’t run out of image space anytime soon. AVIF is ridiculous in this aspect, capping at 8,193x4,320. WebP goes up to 16K2, while the original 1992 JPEG supports 64K2.
* Maximum of 32 bits per channel. No other format (except for the defunct JPEG 2000) offers this.
* Maximum of 4,099 channels. Most other formats support 4 or 5, with the exception of JPEG 2000, which supports 16,384.
* JXL is super resilient to generation loss.5
* JXL supports progressive decoding, which is essential for web delivery, IMO. WebP or HEIC have no such feature. Progressive decoding in AVIF was added a few years back.
* Support for animation.
* Support for alpha transparency.
* Depth map support.

For a full codec feature breakdown, seeBattle of the Codecs.

## Conclusion

JPEG XL is the future of image formats. It checks all the right boxes, and it checks them well. Support in the overwhelmingly most popular browser engine is probably going to be a crucial stepping stone in the format’s path to stardom. I’m happy that the Chromium team reconsidered their inclusion, but I am sad that it took so long and so much pressure from the community to achieve it.

1. https://aomediacodec.github.io/av1-avif/↩︎
2. https://jpegxl.info/resources/battle-of-codecs.html↩︎
3. https://radar.cloudflare.com/reports/browser-market-share-2025-q1↩︎
4. https://www.youtube.com/watch?v=DjUPSfirHek&t=2284s↩︎
5. https://youtu.be/qc2DvJpXh-A↩︎
* Motion trails in Gaia Sky
