---
title: Why /dev/null Is an ACID Compliant Database • Joey's HQ
url: https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/
site_name: hackernews_api
fetched_at: '2025-10-25T11:08:44.285851'
original_url: https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/
author: Joey Yu
date: '2025-10-23'
published_date: '2025-08-22T02:22:02.807Z'
description: /dev/null is web scale
tags:
- hackernews
- trending
---

Back








August 22, 2025 at 2 a.m./




# Why /dev/null Is an ACID Compliant Database



/dev/null is web scale










 database






## Atomicity

Operations are "all or nothing."

Anything you write to/dev/nulldisappears entirely. There's no partial write problem: it’s either written (and discarded) or not written at all. ✅

## Consistency

The system transitions from one valid state to another.

/dev/nullalways stays in a consistent state (empty). No matter what you write, the invariant "file contains nothing" always holds. ✅

## Isolation

Concurrent transactions don’t interfere with each other.

Multiple processes can write to/dev/nullat the same time, and their outputs never conflict, because nothing is ever stored. ✅

## Durability

Once a transaction is committed, it remains so, even after crashes.

/dev/null"durably" commits your data into nothingness. After a crash or reboot, it still contains exactly what it always has: nothing. ✅

There is only 1 small problem though, it only comes with 0b of free storage. For more space, you will have to contact entreprise sales, which is actually just me!
