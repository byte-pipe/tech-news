---
title: Intel's make-or-break 18A process node debuts for data center with 288-core Xeon 6+ CPU — multi-chip monster sports 12 channels of DDR5-8000, Foveros Direct 3D packaging tech | Tom's Hardware
url: https://www.tomshardware.com/pc-components/cpus/intels-make-or-break-18a-process-node-debuts-for-data-center-with-288-core-xeon-6-cpu-multi-chip-monster-sports-12-channels-of-ddr5-8000-foveros-direct-3d-packaging-tech
site_name: hackernews_api
content_file: hackernews_api-intels-make-or-break-18a-process-node-debuts-for-d
fetched_at: '2026-03-04T11:13:08.762443'
original_url: https://www.tomshardware.com/pc-components/cpus/intels-make-or-break-18a-process-node-debuts-for-data-center-with-288-core-xeon-6-cpu-multi-chip-monster-sports-12-channels-of-ddr5-8000-foveros-direct-3d-packaging-tech
author: vanburen
date: '2026-03-03'
published_date: '2026-03-03T16:59:20Z'
description: Intel unveils x86 CPU with the industry's highest core count.
tags:
- hackernews
- trending
---

(Image credit: Intel)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

15

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands

Receive email from us on behalf of our trusted partners or sponsors

By submitting your information you agree to the
Terms & Conditions
 and
Privacy Policy
 and are aged 16 or over.

You are now subscribed

Your newsletter sign-up was successful

 An account already exists for this email address, please log in.

Subscribe to our newsletter

Intel this week formally introduced its Xeon 6+ processors codenamed 'Clearwater Forest' that pack up to 288 energy-efficient Darkmont cores and are the first data center CPUs made on the company's 18A fabrication process (1.8nm-class). Intel aims its Xeon 6+ 'Clearwater Forest' processors primarily for telecom, cloud, and edge AI workloads as they feature Advanced Matrix Extensions (AMX), QuickAssist Technology (QAT), and Intel vRAN Boost technologies.

Go deeper with TH Premium: CPU


(Image credit: Tom's Hardware)
* CPU scaling with DLSS
* Ryzen to the top: How AMD innovated in the gaming CPU market
* How ARM is working its way into PCs
* AMD CES 2026 gaming trends press Q&A roundtable transcript

Intel's Xeon 6+ processors with up to 288 cores combine 12 compute chiplets containing 24 energy-efficient Darkmont cores per tile that are produced using 18A manufacturing technology, two I/O tiles made on Intel 7 production node, as well as three active base tiles made on Intel 3 fabrication process. The compute tiles are stacked on top of the base dies using Intel's Foveros Direct 3D technology, whereas lateral connections are enabled by Intel's EMIB bridges.

Image
1
 of
2
(Image credit: Intel)
(Image credit: Intel)

Intel's 'Darkmont' efficiency cores have received rather meaningful microarchitectural upgrades. Each core integrates a 64 KB L1 instruction cache, a broader fetch and decode pipeline, and a deeper out-of-order engine capable of tracking more in-flight operations. The number of execution ports has also been increased in a bid to improve both scalar and vector throughput under heavily threaded server workloads.

From a cache hierarchy standpoint, the design groups cores into four-core blocks that share approximately 4 MB of L2 cache per block. At the top of the hierarchy, there is last-level cache across the full package that surpasses 1 GB, roughly 1,152 MB in total. This unusually large pool is intended to keep data close to hundreds of active cores and reduce dependence on external memory bandwidth, which in turn is meant to both increase performance and lower power consumption.

Platform-wise, the processor remains drop-in compatible with the current Xeon server socket, so the CPU has 12 memory channels that support DDR5-8000, 96 PCIe 5.0 lanes with 64 lanes supporting CXL 2.0.



(Image credit: Intel)

Intel positions Clearwater Forest for telecom and cloud workloads. The company says operators deploying 5G Advanced and future 6G networks increasingly rely on server CPUs for virtualized RAN and edge AI inference, as they do not want to re-architect their data centers in a bid to accommodate AI accelerators. By combining matrix/vector acceleration, vRAN offloads (using the vRAN Boost), large caches, and broad I/O in one platform, the CPU can perform jobs that are normally reserved for various accelerators that consume more power and take up space.

Also, extreme core count of Xeon 6+ 'Clearwater Forest' CPUs — that approaches 288 cores for uniprocessor configurations and 576 cores in dual socket configurations, enabling a single server to host dozens or even hundreds of virtual machines while maintaining power efficiency and low latency.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

Systems based on Intel's Xeon 6+ processors will be available later this year.



FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

TOPICS

Anton Shilov
Contributing Writer

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
