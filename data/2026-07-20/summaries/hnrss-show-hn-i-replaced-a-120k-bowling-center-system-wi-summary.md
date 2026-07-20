---
title: Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s | Hacker News
url: https://news.ycombinator.com/item?id=48968606
date: 2026-07-19
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-20T12:03:39.492936
---

# Show HN: I replaced a $120k bowling center system with $1,600 in ESP32s | Hacker News

# Show HN: Replaced $120k Bowling Center System with ESP32s
===========================================================

### About the Journey

*   The author is a system engineer who bought an abandoned 8-lane bowling center in rural mid-western town.
*   They wanted to use an existing system (2008) for more efficiency and cost savings due to several reasons like roof leaks, outdated electrical system, and high maintenance costs of the expensive system.

### What Changed

*   Rather than replace the entire system with new components, the author replaced only the score-keeping system installed in 2008.
*   Using open-source electronics, the author created a mesh network using ESP32s for reliable data streaming from bowling center sensors to a Raspberry Pi controller.

### Benefits and Results

*   The cost of replacement parts (for this part of the system) was approximately $4000 per pair of lanes or roughly twice as expensive as original installation.
*   Using open hardware, computer vision, real-time event streaming, and open-source running megascale products worldwide has provided a viable workaround for low-cost alternatives.

### Why ESP32s were Chosen

*   The author chose ESP32 due to their high performance in embedded devices with a variety of sensors (optocouplers, IR-break-beam sensors), making them suitable for real-time application and reliable operation.
*   By using an existing system, with most common off-the-shelf hardware available, the costs were simplified without sacrificing quality in data handling.

### Practical Implementation

*   Using pre-flashed controllers saves valuable time as they can be used directly instead of software installation.
*   A mesh network design keeps all nodes (controllers and the gateway) aware of messages to relay commands and updates accurately without the need for traditional infrastructure like Ethernet cabling or router placement issues.

### Takeaway

*   The author demonstrated that with knowledge on existing hardware, open-source components, and proper implementation, it is possible to reduce costs by replacing or customizing expensive systems for specific use cases.
*   This experience emphasizes the importance of assessing requirements carefully, choosing suitable technologies, and leveraging local off-shoe resources when feasible.