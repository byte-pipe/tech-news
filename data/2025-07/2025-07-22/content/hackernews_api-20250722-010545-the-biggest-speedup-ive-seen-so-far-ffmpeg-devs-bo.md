---
title: '''The biggest speedup I''ve seen so far'' — FFmpeg devs boast of another 100x leap thanks to handwritten assembly code | Tom''s Hardware'
url: https://www.tomshardware.com/software/the-biggest-speedup-ive-seen-so-far-ffmpeg-devs-boast-of-another-100x-leap-thanks-to-handwritten-assembly-code
site_name: hackernews_api
fetched_at: '2025-07-22T01:05:45.579182'
original_url: https://www.tomshardware.com/software/the-biggest-speedup-ive-seen-so-far-ffmpeg-devs-boast-of-another-100x-leap-thanks-to-handwritten-assembly-code
author: harambae
date: '2025-07-21'
published_date: '2025-07-17T15:10:48Z'
description: Some operations in FFmpeg are now as much as 100x faster due to the crafting of handwritten assembly code.
tags:
- hackernews
- trending
---

(Image credit: FFmpeg)

The developers behind the FFmpeg project are again claiming major performance uplifts delivered by wielding the art of handwritten assembly code. With thelatest patchapplied, users should see a “100x speedup” in the cross-platform open-source media transcoding application. However, the developers were soon to clarify that the 100x claim applies to just a single function, “not the whole of FFmpeg.”

BREAKING: FFmpeg 100x speedup from handwritten assembly13:55:30 <•haasn> rangedetect8_avx512: 121.2 (100.18x) that may be the biggest speedup I've seen so farJuly 16, 2025

## “The biggest speedup I've seen so far”

Last November, we reported on an FFmpeg performance boost that could speed certain operationsby up to 94x. The latest handwritten assembly patch boosts the app’s ‘rangedetect8_avx512’ performance by 100x. If your modern processor doesn’t support AVX512, you should still see a 64% uplift with the rangedetect8_avx2 code path.

Where will you feel these speed increases? In some follow-up tweets, the FFmpeg developers admit that “It's a single function that's now 100x faster, not the whole of FFmpeg.” They would later go on to elaborate that the functionality, which might enjoy a 100% speed boost, depending upon your system, was “an obscure filter.”

The obscurity of the function means it hadn’t been prioritized by the devs until now. But we also gather that the filter code was recoded using the SIMD (Single Instruction, Multiple Data) processing concept for vastly improved parallel processing on today’s powerful chips.

Evidently, compilers – programs that take higher-level language code and spit out assembly (machine) code – are still not competitive with handwritten assembly. Or you could say, “register allocator sucks on compilers,” as FFmpeg tweeted today.

(Image credit: FFmpeg)

## Assembly language evangelicals

Harking back to the golden age of home computing in the 1980s and 1990s, where fixed-spec systems had lifecycles measured in half-decades - and strictly limited processing resources - handwritten assembly code optimizations played a larger part in the business of speeding up computers, games, and other software.

FFmpeg is perhaps one of the few ‘assembly evangelists’ remaining. The dev team evenruns a ‘school.’

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

FFmpeg tools and libraries run across Linux, Mac OS X,MicrosoftWindows, the BSDs, Solaris, systems, and more. One of the most popular video player software utilities,VLC, uses the libavcodec and libavformat libraries from the FFmpeg project.

FollowTom's Hardware on Google Newsto get our up-to-date news, analysis, and reviews in your feeds. Make sure to click the Follow button.

TOPICS

Mark Tyson
News Editor

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
