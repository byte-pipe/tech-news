---
title: 'Daniel Lemire on X: "Xiaomi is the Chinese tech giant. Their phones compete with iPhones. Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And" / X'
url: https://twitter.com/lemire/status/2091894299289874926
site_name: hackernews_api
content_file: hackernews_api-daniel-lemire-on-x-xiaomi-is-the-chinese-tech-gian
fetched_at: '2026-08-24T19:27:10.977535'
original_url: https://twitter.com/lemire/status/2091894299289874926
author: tosh
date: '2026-08-24'
published_date: '2026-08-24T14:24:01.000Z'
description: Xiaomi is the Chinese tech giant. Their phones compete with iPhones. Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And
tags:
- hackernews
- trending
---

## Post

Log in
Sign up

## Post

# Daniel Lemire on X: "Xiaomi is the Chinese tech giant. Their phones compete with iPhones.

Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And"

* Daniel Lemire@lemireXiaomi is the Chinese tech giant. Their phones compete with iPhones.

Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And you may find it it difficult to find a phone with the next CPU (Xring O3).

But the new Xiaomi processor is worth discussing further as it reveals an important trend.

The chip has a lot of cache (44 MB in total). It is more than most laptop CPUs. If you have an Intel processor in your laptop, chances are good that you have less cache.

The biggest cores on the the Xring O3 are the C1-Ultra. C1-Ultra really powerful cores. They support SME2 (Scalable Matrix Extension 2) for matrix/AI acceleration, SVE2 for data parallelism (SIMD).

It is astonishingly wide, with 21 execution ports, six of which support SIMD operations (128 bits).

This is more execution ports than you have on your Intel/AMD processor. The AMD Zen 5 has the upper hand because it can do 4x512-bit but 6x128-bit is the best you can do on an ARM chip as far as I know.

So the trend is clear. We are getting cores that are massively parallel in terms of the number of execution units. We get better SIMD (more units) and many more units capable of doing arithmetic.

This means that you can do many, many independent additions or multiplications per cycle. And much more cache.

This is where all the transistors go.Ice Universe@UniverseIce13hXiaomi’s Xring O3 delivers a massive performance leap, scoring 3,945 in Geekbench single-core and an unprecedented 15,221 in multi-core.2:24 PM · Aug 24, 202627.4KViews2334416131
* Jon Clegg@jonclegg773hThis smells somewhat legitimate and somewhat BS. The architecture itself looks impressive — TSMC 3nm, a 4+ GHz prime core, tons of cache, and a very wide execution engine. And the claimed Geekbench numbers, around 3,945 single-core and 15,221 multi-cor, are especially impressive,Show more4152.2K
* Chris Allen@theodorvaryag3hSVE2 with 21 execution ports? good golly miss molly I could make that thing scream.41.2K
* Omar Mahdi@bloeys4hBut programming all those cores still feels very tough14856