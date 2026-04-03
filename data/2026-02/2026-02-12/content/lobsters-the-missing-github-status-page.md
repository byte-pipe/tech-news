---
title: The Missing GitHub Status Page
url: https://mrshu.github.io/github-statuses/
site_name: lobsters
content_file: lobsters-the-missing-github-status-page
fetched_at: '2026-02-12T06:00:23.762626'
original_url: https://mrshu.github.io/github-statuses/
date: '2026-02-12'
tags: vcs
---

### Last 90 days uptime

Last updated —

0 incidents in last 90 days

GitHub Platform

—

90 days ago

Today

Operational

Maintenance

Minor

Major

Why

is

this

page

'missing'
?

Read

about

the

mirror
 →

### Service uptime (90 days)

Per-component uptime from tagged incidents.

### Uptime history

‹

Loading…

›

### Incident timeline

Show more

 Show more


### About this mirror

GitHub stopped updating its status page with aggregate uptime numberssometimeago— if you use it regularly, you might have a feeling why. This is the missing version.

We rebuild platform‑wide and per‑service uptime from archived status updates, derive
 minute‑level downtime windows, and map incidents to services whenever the source data allows.
 Everything is open source, and PRs are very welcome!

Nerd notes:the pipeline reconstructs history by replaying theAtom feedsnapshots committed to git viaFlat Data.
 It rebuilds each incident timeline and computes
 uptime using merged downtime windows rather than day‑level buckets. When components are
 missing, we infer tags withGLiNER2but only keep labels that are explicitly grounded in the incident text.

Archive trail:2017→2018→2019→2019 (new)
