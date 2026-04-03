---
title: The Missing GitHub Status Page
url: https://mrshu.github.io/github-statuses/
date: 2026-02-12
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-12T06:00:57.217986
---

# The Missing GitHub Status Page

# The Missing GitHub Status Page

- GitHub discontinued its official status page that provided aggregate uptime numbers. This project aims to provide a reconstruction of that information.
- This project rebuilds platform-wide and per-service uptime data from archived status updates.
- It derives minute-level downtime windows and maps incidents to services based on available source data.
- The project is open source, with pull requests welcomed.
- The pipeline reconstructs history by replaying Atom feed snapshots committed to Git via Flat Data.
- It rebuilds incident timelines and computes uptime using merged downtime windows instead of day-level buckets.
- Missing components have tags inferred using GLINER2, but only labels grounded in incident text are kept.
- The archive trail covers the years 2017, 2018, 2019, and a new addition for 2019.
- The provided snippet indicates that the GitHub platform has had 0 incidents in the last 90 days and was last updated 90 days ago, currently showing as operational with minor maintenance.
