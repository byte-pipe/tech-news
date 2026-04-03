---
title: "Meta Is Using The Linux Scheduler Designed For Valve's Steam Deck On Its Servers - Phoronix"
url: https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server
date: 2025-12-23
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-24T11:10:21.023000
screenshot: hackernews_api-meta-is-using-the-linux-scheduler-designed-for-val.png
---

# Meta Is Using The Linux Scheduler Designed For Valve's Steam Deck On Its Servers - Phoronix

## Meta Uses Linux Scheduler Designed for Valve Steam Deck on Servers

### Key Points:

* Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers, despite it being a latency-critical component.
* This decision was made after finding that SCX-LAVD adapts well to various hardware configurations on large servers.
* However, this doesn't necessarily guarantee it will perform as optimally or efficiently in all scenarios.

### Key Details:

* SCX-LAVD is a Linux scheduler tailored for latency-critical components like the Steam Deck, which was built on top of sched_ext.
* It also works well with growing CPU and memory configurations on Meta servers, providing efficient load balancing.
* The decision to use SCX-LAVD as its default fleet scheduler stems from its performance in various hardware configurations.
* Experts can learn more about Meta's findings through the Linux Plumbers Conference presentation and attached slides.

---

# Meta's Decisions Regarding LCx Scheduler

Written by
Michael Larabel
 in
Linux Kernel
 on 23 December 2025 at 06:10 AM EST.
22 Comments

A peculiar anecdote from this month's Linux Plumbers Conference in Tokyo highlights an interesting choice made by Meta regarding its server architecture.

Meta decided to integrate the Linux scheduler designed for Valve's Steam Deck, SCX-LAVD, on their servers instead of using a more specialized one. This decision was influenced significantly by SCX-LAVD's performance and robust adaptability in various hardware configurations.

SCX-LAVD has been successfully utilized by several other projects like Igalia under contract for Valve and other Linux gaming initiatives. Its functionality extends beyond the Steam Deck, being applied to other desktop versions as well.

For those seeking insight into Meta's approach, this article at the Linux Plumbers Conference conference can be found both embedded and accessed using a slide deck accompanying it.
