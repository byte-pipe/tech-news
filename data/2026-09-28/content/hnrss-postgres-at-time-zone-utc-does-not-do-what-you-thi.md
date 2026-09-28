---
title: Postgres AT TIME ZONE 'UTC' does NOT do what you think it does
url: https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does
site_name: hnrss
content_file: hnrss-postgres-at-time-zone-utc-does-not-do-what-you-thi
fetched_at: '2026-09-28T18:26:14.973747'
original_url: https://bookofrevenue.com/blog/6ab81e9a97a13f0001f7e4e1/postgres-at-time-zone-u-does-not-do-what-you-think-it-does
date: '2026-09-27'
description: And why you may need to repeat AT TIME ZONE 'UTC' twice. SUMMARY * AT TIME ZONE 'UTC' converts the data type from timestamptz to timestamp (example). * Now you are inadvertently using the timestamp without time zone (aka timestamp) data type, which is markedly discouraged. * There are tons of footguns with timestamp. * For example, the equality of timestamp and timestamptz will always be false. * Adding a month with + INTERVAL '1 months' is timezone-dependent. If your product
tags:
- hackernews
- hnrss
---

