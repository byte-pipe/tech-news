---
title: Shipping WebGPU on Windows in Firefox 141 – Mozilla Gfx Team Blog
url: https://mozillagfx.wordpress.com/2025/07/15/shipping-webgpu-on-windows-in-firefox-141/
site_name: hackernews
fetched_at: '2025-07-17T04:06:53.004749'
original_url: https://mozillagfx.wordpress.com/2025/07/15/shipping-webgpu-on-windows-in-firefox-141/
author: Bogdanp
date: '2025-07-17'
published_date: '2025-07-15T19:34:44+00:00'
description: After years in development, we will be releasing WebGPU on Windows in Firefox 141! WebGPU gives web content a modern interface to the user's graphics processor, enabling high-performance computation and rendering. We're excited about WebGPU because we believe it will raise the ceiling for games, visualization, and local computation on the web. You can find…
---

jblandy


Uncategorized


July 15, 2025


2 Minutes


After years in development, we will be releasing WebGPU on Windows in Firefox 141! WebGPU gives web content a modern interface to the user’s graphics processor, enabling high-performance computation and rendering. We’re excited about WebGPU because we believe it will raise the ceiling for games, visualization, and local computation on the web.

You can find a tutorial on WebGPU atwebgpufundamentals.org, try out theWebGPU Samples, and read documentation for the API atMDN. WebGPU is defined in two W3C standards,WebGPUandWGSL, whose development Mozilla has participated in since it began in 2017.

WebGPU has been available in Google Chrome since 2023, and is expected to be available in Safari 26 this fall.

Although Firefox 141 enables WebGPU only on Windows, we plan to ship WebGPU on Mac and Linux in the coming months, and finally on Android. Windows was our first priority because that’s where the great majority of our users are, but we are looking forward to enabling it on the other platforms as soon as it is robust and our test coverage is adequate. (Your humble author is strictly a Linux user, so this concern is close to his heart.) Note that WebGPU has been available in Firefox Nightly on all platforms other than Android for quite some time.

Firefox’s WebGPU implementation is based onWGPU, a Rust crate that provides a unified, portable interface to the low-level graphics APIs of the underlying platform:Direct3D 12,Metal, andVulkan. WGPU is developed as an independent open source project on GitHub, but Mozilla is a major contributor. WGPU is widely used outside Firefox, and has an active community, so if you are a Rust developer interested in contributing to Firefox’s WebGPU support, WGPU is a good place to start.

WebGPU is a large, complex API. We’ve focused our efforts so far on making high-visibility WebGPU applications and demos run smoothly, and we believe it should work well in Firefox 141 for many use cases. However, there is plenty of work remaining to be done to improve our performance and compliance with the specification. In particular:

* Firefox uses unbuffered inter-process communication to convey web content’s requests to the GPU sandbox process, which introduces significant overhead. We addressed this inBug 1968122, which improved performance significantly. The fix will appear in Firefox 142.
* Firefox currently uses an interval timer to tell when the GPU has completed a task, adding significant latency to many applications where the task finishes quickly. There are better ways to do this, we are changing Firefox to use them. You can follow our progress inBug 1870699.
* Firefox does not yet support WebGPU’simportExternalTexturemethod, which lets the GPU read decompressed video content directly from the decoder. You can follow our progress inBug 1827116.

Please give WebGPU a try in Firefox! If you encounter problems, please report them in theWebGPU componentin Bugzilla. As always, provide us with as detailed instructions as you can to make the bug occur, and attach the contents ofabout:supportto the bug so we can see what kind of system you are using.

It’s been a big project, but we’re done tinkering with the engine and taking test drives — we’re finally ready to roll WebGPU out of the garage and hand it over to you for daily use. We’re looking forward to seeing what you can do with WebGPU in Firefox!

### Share this:

* Click to share on X (Opens in new window)X
* Click to share on Facebook (Opens in new window)Facebook
Like

Loading...


* Tagged
* graphics
* mozilla
* software
* technology
* web
* webgpu




## Published byjblandy

View all posts by jblandy

Published

July 15, 2025
