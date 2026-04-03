---
title: Algorithmically Finding the Longest Line of Sight on Earth | Lobsters
url: https://lobste.rs/s/8959u3/algorithmically_finding_longest_line
date: 2026-02-10
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-10T11:03:00.667714
---

# Algorithmically Finding the Longest Line of Sight on Earth | Lobsters

# Algorithmically Finding the Longest Line of Sight on Earth

* Tom and Ryan, Lobster regulars, developed an algorithm using Rust and SIMD to find the longest line of sight on Earth.
* Their research confirms a previously speculated view between Pik Dankova in Kyrgyzstan and the Hindu Kush in China is indeed the longest, measuring 530km.
* Detailed information about the project can be found at https://alltheviews.world.
* An interactive map showcasing over 1 billion longest lines across the globe is available at https://map.alltheviews.world. Users can explore the longest line of sight from any point on the map.
* The computational process involved packing visibility tiles for the entire planet and required significant resources: hundreds of AMD Turin cores, hundreds of GBs of RAM, several TBs of disk space, and two days of continuous runtime across multiple machines.
* Technical details of the algorithm and pipeline are documented in:
    * Tom's blog post: https://tombh.co.uk/longest-line-of-sight
    * Ryan's technical breakdown: https://ryan.berge.rs/posts/total-viewshed-algorithm
* The project is presented as a labor of love, aiming to inspire both technical exploration and appreciation for vast natural views.
