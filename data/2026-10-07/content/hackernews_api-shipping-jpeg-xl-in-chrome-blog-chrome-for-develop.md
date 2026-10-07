---
title: Shipping JPEG XL in Chrome | Blog | Chrome for Developers
url: https://developer.chrome.com/blog/jpeg-xl-in-chrome
site_name: hackernews_api
content_file: hackernews_api-shipping-jpeg-xl-in-chrome-blog-chrome-for-develop
fetched_at: '2026-10-07T17:42:31.807475'
original_url: https://developer.chrome.com/blog/jpeg-xl-in-chrome
author: AshleysBrain
date: '2026-10-07'
description: JPEG XL offers better compression than JPEG, built-in HDR support, lossless JPEG transcoding, and more.
tags:
- hackernews
- trending
---

* Chrome for Developers
* Blog

# Shipping JPEG XL in ChromeStay organized with collectionsSave and categorize content based on your preferences.

Luca VersariXGitHubHomepageMoritz FirschingXGitHubMastodonHomepagePhilip JägenstedtGitHubBlueskyHomepage

Published: October 6, 2026

We're excited to announce that Chrome is shipping decoding support for the JPEG
XL (.jxl) image format starting from Chrome 155. JPEG XL is a next-generation
image format designed to meet the needs of modern web developers and
photographers. It offers 30-50% better compression than JPEG, lossless
compression, built-in HDR support, lossless JPEG transcoding, and more.

In general, we recommend trying both AVIF and JPEG XL to get the best results.
We expect that JPEG XL is most helpful for high-fidelity or lossless
compression, especially of photographic images or in cases in which fine-grained
progressive decoding is preferred.

In this post, we share why we brought JPEG XL to Chrome, how we used Rust to
ensure memory safety first, the extensive performance work that makes it fast,
and what the journey tells us about developer feedback and the web standards
ecosystem.

## Safety first: Reimplementing the decoder in Rust (jxl-rs)

Image decoders are one of the most critical and targeted attack surfaces in any
modern web browser. They process complex, untrusted binary structures directly
from the network and run inside the renderer process. Historically, decoders
written in memory-unsafe languages like C++ have been prone to vulnerabilities
such as out-of-bounds reads, heap overflows, and use-after-free bugs.

Our security model relies on sandboxing and defense-in-depth, guided by therule of
two.
However, sandboxing is a secondary layer of defense. To eliminate these security
risks at the source, we have integratedjxl-rs, a pure Rust implementation of
the JPEG XL decoder.

## Design for speed, without compromising safety

Memory safety is crucial, but a memory-safe decoder that is approximately as
fast as the best non-memory-safe alternative is a much more obvious choice than
a choice with a significant performance compromise.

A fundamental part of the performance of modern codecs is making full use of the
SIMD hardware available on modern devices. To do so safely,target_feature_11Rust
feature had to be stabilized, which allowed the use of SIMD instructions without
requiringunsafecode.

The next step was to build a SIMD abstraction layer (jxl_simd), inspired by
the C++Highwaylibrary (itself originally
developed forlibjxl, the C++ reference implementation of JPEG XL). Together,
those developments allowed writing a multi-platform library that doesn't
compromise on SIMD performance optimizations, while restricting unsafe
operations to a small number of highly-vetted locations.

Performance optimizations injxl-rsbuild on those inlibjxl. This includes
a generic processing pipeline for steps crossing region borders, while
minimizing data copies to maximize hardware performance. We've been tracking the
performance of the Rust reimplementation across different hardware platforms on
thejxl-rs performance dashboard.

We verified thejxl-rsimplementation with various state-of-the-art
techniques, including fuzzing and AI review of the code, and have not found any
memory safety bugs throughout the entire implementation history, providing yet
another validation of the huge improvements that Rust brings to memory safety.

## Developer feedback and the Interop Project

The Chrome team considers web developer feedback from a wide range of channels,
such as bugs, surveys, theDeveloper Signals
Project,
and theInterop Project. Our
decision to ship JPEG XL was based on consistent feedback and requests from web
developers, most visible in the Interop Process, where it was apopular
proposal in 2026and
several years prior.

To ensure the format is interoperable across browsers, we have participated in
theInterop 2026 JPEG XL
Investigationto ensure
there is test coverage for all of JPEG XL's features in browsers, and that those
tests pass in Chrome.

## Try it out

With JPEG XL officially landing in Chrome, the web becomes faster, richer, and
safer. We encourage developers, content creators, and platform owners to start
using.jxlimages and animations in their pipelines.

Try it out,file bugs,
and help us continue building a faster and safer web for everyone.

## Acknowledgements

We'd like to thank all the people who contributed tojxl-rsor its integration
in Chrome, and especially Helmut Januschka for the substantial contributions
both to the Chrome integration andjxl-rs, and Martin Bruse, Zoltan Szabadka,
Sami Boukortt and Wonwoo Choi for their substantial contributions tojxl-rsitself.

Except as otherwise noted, the content of this page is licensed under theCreative Commons Attribution 4.0 License, and code samples are licensed under theApache 2.0 License. For details, see theGoogle Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.