---
title: Meta Is Using The Linux Scheduler Designed For Valve's Steam Deck On Its Servers - Phoronix
url: https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server
site_name: hackernews_api
fetched_at: '2025-12-24T11:08:01.388275'
original_url: https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server
author: yellow_lead
date: '2025-12-23'
description: Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers
tags:
- hackernews
- trending
---

# Meta Is Using The Linux Scheduler Designed For Valve's Steam Deck On Its Servers

Written by
Michael Larabel
 in
Linux Kernel
 on 23 December 2025 at 06:10 AM EST.
22 Comments

An interesting anecdote from this month's Linux Plumbers Conference in Tokyo is that Meta (Facebook) is using the Linux scheduler originally designed for the needs of Valve's Steam Deck... On Meta Servers. Meta has found that the scheduler can actually adapt and work very well on the hyperscaler's large servers.

SCX-LAVD as the Latency-criticality Aware Virtual Deadline scheduler has
worked out very well for the needs of Valve's Steam Deck
 with similar or better performance than
EEVDF
. SCX-LAVD has been worked on by Linux consulting firm Igalia under contract for Valve. SCX-LAVD has also seen varying use by the CachyOS Handheld Edition, Bazzite, and other Linux gaming software initiatives.

It turns out that besides working well on handhelds, SCX-LAVD can also end up working well on large servers too. The presentation at LPC 2025 by Meta engineers was in fact titled "
How do we make a Steam Deck scheduler work on large servers
." At Meta they have explored SCX_LAVD as a "default" fleet scheduler for their servers that works for a range of hardware and use-cases for where they don't need any specialized scheduler.

They call this scheduler built atop sched_ext as "Meta's New Default Scheduler". LAVD they found to work well across the growing CPU and memory configurations of their servers, nice load balancing between CCX/LLC boundaries, and more. Those wishing to learn more about Meta's use and research into SCX-LAVD can find the Linux Plumbers Conference presentation embedded below along with the
slide deck
.
