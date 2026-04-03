---
title: "We Mass-Deployed 15-Year-Old Screen Sharing Technology and It's Actually Better"
url: https://blog.helix.ml/p/we-mass-deployed-15-year-old-screen
date: 2025-12-24
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-24T11:11:50.966440
screenshot: hackernews-we-mass-deployed-15-year-old-screen-sharing-techno.png
---

# We Mass-Deployed 15-Year-Old Screen Sharing Technology and It's Actually Better

## The Challenge of Enterprise Networks

We embarked on a three-month journey to develop a high-performance, hardware-accelerated video streaming pipeline using H.264 codecs and WebSockets over enterprise networks with poor connectivity.

**The Reality Check**

However, our initial solution didn't quite fly as expected due to its reliance on HTTPS on port 443, which is often blocked by enterprise firewalls and configured for security reasons. Other issues also arose, including:

* UDP traffic is generally not allowed in most enterprise environments
* Custom ports lead to firewall blocking and denied access
* TURN (Traversal Using Relays around NAT) servers must be set up, configuring IT departments becomes a hassle

## **The Solution**

Undeterred, we decided to implement a pure WebSocket video pipeline. This approach requires:

1. H.264 encoding via GStreamer with hardware acceleration for CPU-intensive computations.
2. Binary frames transmitted over L7 (no intermediary proxying) via the WebSocket protocol.
3. The WebCodecs API translates the binary signals into human-readable video streams.

**Performance Benefits**

This approach yields some remarkable performance gains:

* Smooth, 40ms latency
* 60fps at 40Mbps bandwidth

However, our tests also demonstrated that 200ms network delay becomes a significant concern when traffic congestion increases. In such events, frames start to buffer up in the TCP/WebSocket layer, resulting in further delays and video drop-off.

**Challenges Continue**

Despite this, we successfully scaled the solution for an enterprise customer with poor internet connectivity due to our custom approach not being compatible with existing network policies or firewall configurations.
