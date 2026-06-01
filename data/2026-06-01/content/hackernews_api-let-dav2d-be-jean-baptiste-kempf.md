---
title: Let dav2d be — Jean-Baptiste Kempf
url: https://jbkempf.com/blog/2026/dav2d/
site_name: hackernews_api
content_file: hackernews_api-let-dav2d-be-jean-baptiste-kempf
fetched_at: '2026-06-01T12:54:58.372958'
original_url: https://jbkempf.com/blog/2026/dav2d/
author: captain_bender
date: '2026-05-31'
description: VideoLAN announces dav2d, an open source AV2 decoder — continuing the work started with dav1d for AV1.
tags:
- hackernews
- trending
---

31 MAY 2026

VIDEOLAN

6 min read

# Let dav2d be

## dav2d

A codec does not really exist until everyone can decode it.

Today, we announcedav2d, a fast decoder for the newAV2codec, developed by members of theVideoLANcommunity.

A few weeks ago, we opened the repository and started development in public. Since then, AV2 itself has reached its first official specification release, making this a good moment to explain what dav2d is, why we started it, and where the project stands today.

dav2dis the continuation of the work we started withdav1d, our AV1 decoder.

The goal is similar: provide a small, fast, portable and correct decoder, suitable for real applications, media players, browsers, test tools and operating systems.

## AV2

AV2is the successor toAV1and the latest royalty-free video codec from theAlliance for Open Media.

The specification is now publicly available at:

* https://av2.aomedia.org/
* https://github.com/AOMediaCodec/av2-spec

AV1 was finalized in 2018 and became one of the most successful video codecs ever deployed. Today it is available in browsers, mobile devices, operating systems, televisions, streaming services and video applications around the world.

AV2 builds on that success. The codec introduces new coding tools across prediction, transforms, entropy coding, filtering and chroma processing, while continuing the goal of improving compression efficiency.

The reported gains vary depending on the test conditions, but improvements around 25% compared to AV1 are commonly seen, with some evaluations reporting even larger gains.

AV2 decoding is roughlyfive timesmore complex than AV1 decoding. In practice, that means software running on today’s hardware will struggle to decode AV2 in real time without careful, architecture-specific optimization.

This is why we started dav2d early rather than waiting for the specification to stabilize.

## From dav1d to dav2d

The origins ofdav2dgo back to the beginning ofdav1d.

When AV1 was being finalized, we pushed for a fast software decoder, because we did not believe hardware decoding would become available quickly enough, or on enough devices.

Not everyone agreed with that assessment. Some members of the AOM community felt that hardware implementations and the reference decoder would be sufficient.

We thought otherwise. Browsers, media players, operating systems and mobile devices would need a production-quality decoder long before dedicated hardware became commonplace.

In the end, AOM itself funded part of the initial development work and some members of the Alliance eventually joined that effort.

The result was dav1d.

In hindsight, the need for a fast software decoder proved larger than many people expected.

Today, dav1d is the most widely deployed AV1 software decoder.

It is used inVLC,FFmpeg,mpv, Firefox, Chrome, Safari, Android, Windows, Linux and many other applications and platforms.

The project has also become the reference AV1 decoder implementation for many developers working on AV1 deployment, testing and optimization.

You can read the full history of dav1d on this blog:Introducing dav1d,the road to the first release,First release,dav1d 1.2and1.5 “Sonic”.

With AV2, we are trying to start that work earlier.

A codec specification is important, but it is not enough. Developers need a decoder that can be built, tested, benchmarked, integrated and compared against other implementations.

This is what dav2d is meant to provide.

## Current status

The current dav2d tree already contains a feature-complete AVM v15 decoder supporting both 8-bit and 10-bit decoding.

Most major parts of the codec are already implemented and are now being optimized, including:

* bitstream parsing;
* frame and sequence headers;
* entropy decoding and CDF handling;
* intra prediction;
* inter prediction and reference motion vectors;
* transforms;
* CCTX and CfL;
* deblocking;
* CDEF;
* Wiener filtering;
* film grain synthesis.

This is still early work, and the AV2 ecosystem itself is still young, but the decoder is already functional and far beyond an empty announcement repository.

A growing part of the work is now focused on correctness, conformance, optimization and platform support.

One reason the project has progressed so quickly is that dav2d does not start from scratch. AV2 shares many concepts with AV1, and dav1d already solved a number of architectural questions around threading, SIMD organization, testing, portability and API design.

While AV2 requires substantial new decoder code, a lot of the experience accumulated over years of dav1d development transfers directly to dav2d.

## Performance work

The performance work has already started.

On x86, dav2d already contains AVX2 code for several inverse transform sizes, as well as work around CCTX, deblock, intra prediction and CfL-related paths.

On ARM, there is already AArch64 NEON work for entropy decoding, SAD, intra prediction, palette prediction, DC predictors, smooth predictors and motion-related functions. Some arm32 work has also started.

There is also early RISC-V work, mostly around re-enabling and adapting existing intra prediction and motion compensation assembly.

This is the same kind of progression we had with dav1d: first a clean C implementation, then validation infrastructure, then architecture-specific optimized code for the most important hot paths.

## checkasm

One important difference compared to the early days of dav1d is tooling.

During the development of dav1d, we createdcheckasm, a framework used to validate and benchmark optimized implementations against their C equivalents.

dav2d benefits from that infrastructure from day one.

Combined with the architectural experience gained from dav1d, this has allowed the project to progress considerably faster than dav1d did at a comparable stage.

The current tree already contains checkasm coverage for several areas, including inverse transforms, motion compensation, film grain, CfL and reference motion-vector code.

This should make future optimization work both faster and safer.

## Open source

Like dav1d before it, dav2d is developed as an open source project.

The decoder is released under the same BSD-style license as dav1d, making it easy to integrate into open source and proprietary applications alike.

As with mostVideoLANprojects, development happens in public from day one:

* Repository:https://code.videolan.org/videolan/dav2d
* Issues:https://code.videolan.org/videolan/dav2d/-/issues
* Merge Requests:https://code.videolan.org/videolan/dav2d/-/merge_requests

We believe open implementations are essential for the healthy deployment of new media technologies. They provide interoperability, independent validation of specifications, easier experimentation, and a common foundation for the ecosystem.

## What comes next

There is still a lot of work ahead.

We need to continue tracking the AV2 specification, improve conformance, extend test coverage, optimize further x86 and ARM, work on RISC-V, improve high bit-depth performance, improve threading, reduce memory usage and prepare future releases.

But the foundations are already there: the tooling, the architecture and the experience gained from dav1d, with additional improvements.

dav1d helped make AV1 practical long before hardware support became ubiquitous.

We intend to do the same for AV2.

Let dav2d be. From VideoLAN, with love.