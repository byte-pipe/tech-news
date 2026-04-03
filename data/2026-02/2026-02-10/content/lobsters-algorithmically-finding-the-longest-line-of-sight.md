---
title: Algorithmically Finding the Longest Line of Sight on Earth | Lobsters
url: https://lobste.rs/s/8959u3/algorithmically_finding_longest_line
site_name: lobsters
content_file: lobsters-algorithmically-finding-the-longest-line-of-sight
fetched_at: '2026-02-10T11:02:07.427170'
original_url: https://lobste.rs/s/8959u3/algorithmically_finding_longest_line
date: '2026-02-10'
description: ☶
tags: release, rust
---

1. 46Algorithmically Finding the Longest Line of Sight on Earth☶releaserustauthored bytombh13 hours ago

Hello, we're Tom and Ryan, Lobster regulars, that teamed up to build an algorithm with Rust and SIMD to exhaustively search for the longest line of sight on the planet. We can confirm that a previously speculated view between Pik Dankova in Kyrgyzstan and the Hindu Kush in China is indeed the longest, at 530km.

We go into all the details at:https://alltheviews.world

And there's an interactive map with over 1 billion longest lines, covering the whole world athttps://map.alltheviews.worldJust click on any point and it'll load its longest line of sight.

Some of you may rememberTom's postfrom a few months ago about how to efficiently pack visibility tiles for computing the entire planet. Well now it's done. The compute run itself took 100s of AMD Turin cores, 100s of GBs of RAM, a few TBs of disk and 2 days of constant runtime on multiple machines.

If you are interested in the technical details, Ryan and I have written extensively about the algorithm and pipeline that got us here:

* Tom's blog post:https://tombh.co.uk/longest-line-of-sight
* Ryan's technical breakdown:https://ryan.berge.rs/posts/total-viewshed-algorithm

This was a labor of love and we hope it inspires you both technically and naturally, to get you out seeing some of these vast views for yourselves!
