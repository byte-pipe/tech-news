---
title: Postgres LISTEN/NOTIFY does not scale
url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
site_name: hackernews_api
fetched_at: '2025-07-11T16:07:15.183551'
original_url: https://www.recall.ai/blog/postgres-listen-notify-does-not-scale
author: davidgu
date: '2025-07-08'
description: Postgres LISTEN/NOTIFY can cause severe performance issues under high write concurrency due to a global lock during commit. Learn why it doesn't scale and how to avoid outages.
tags:
- hackernews
- trending
---

New
Recall.ai has released a Desktop Recording SDK!
Read more

Deep Dive

# Postgres LISTEN/NOTIFY does not scale

Updated at:
July 10, 2025
Written By:
Elliot Levin
Table of Contents

* TL;DR
* How we discovered it
* Reproducing the problemWith NOTIFYWithout NOTIFY
* With NOTIFY
* Without NOTIFY
* Remediation

AtRecall.ai, we run an unusual workload. We record millions of hours of meetings every month. Each of these meetings generates a large amount of data we need to reliably capture and analyze. Some of that data is video, some of it is audio and some of it is structured data – transcription, events and metadata.

The structured data gets written to our Postgres database by tens of thousands of simultaneous writers. Each of these writers is a “meeting bot”, which joins a video call and captures the data in real-time.

We love Postgres and it lives at the heart of our service! But this extremely concurrent, write-heavy workload resulted in a stalled-out Postgres. This is the story of what happened, how we ended up discovering a bottleneck in the LISTEN/NOTIFY feature of Postgres (the event notifier that runs based on triggers when something changes in a row), and what we ended up doing about it.

## TL;DR

When aNOTIFYquery is issued during a transaction, it acquires a global lock on theentire database(ref) during the commit phase of the transaction, effectively serializing all commits. Under many concurrent writers, this results in immense load and major downtime. Don’t useLISTEN/NOTIFYif you want your database to scale to many writers.

## How we discovered it

Between the dates 2025-03-19 to 2025-03-22 our core Postgres database experienced three periods of downtime. Each of these downtimes had a similar set of symptoms:

* Massive spikes in database load and active awaiting sessions
* Database query throughput drops massively
* Database CPU, disk I/O and network traffic allplummeted

Why would increased load on the database result in a drastic drop in CPU and I/O? This was extremely surprising to us, and lead us to our first clue. We suspected increased lock contention but we didn’t have enough information to confirm if this was the root cause or a symptom given that load spikes so suddenly. Our first change was to enablelog_lock_waitsso we could identify the queries, connections and locks being contested.

After extended investigation we correlated the increased load with increased requests to our update endpoint, specifically our update bot endpoint, which triggered aNOTIFYquery that notifies a running bot that its configuration has been updated. After combing through gigabytes of logs we spotted a flood of interesting log lines:

2025-03-22 15:16:59 UTC:10.3.206.139(34877):postgres@meeting_api:[45081]:DETAIL: Process holding the lock: 20841. Wait queue: 17474, 20898, 1931, 20926, 35855, 14865, 20846, 31717, 36912, 20927, 45081, 61596, 44128, 17462, 4576, 35852, 35940, 35854, 35864, 37057, 26765, 37041, 35872, 18380, 44271, 35802, 35840, 33384, 44279, 62275, 35440, 35948, 35804, 45084, 45147, 32250, 35898, 20932, 35862, 35859, 56845, 44233, 17448, 26745, 35883, 35865, 26753, 20809, 1929, 14858, 36904, 17452, 35892, 36910, 32798, 20892, 35899, 36901, 45137, 45105, 36835, 36897, 35901, 32036, 35856, 45171, 35941, 37046, 45160, 33013, 17458, 35874, 44092, 35893, 18356, 37055, 35942, 1939, 38662, 45079, 35889, 35839, 37058, 36900, 35910, 37056, 35951, 35907, 36908, 26767, 25575, 32037, 35868, 44278, 45188, 45120, 61287, 35863, 20817, 45062, 37048, 45151, 45179, 35939, 35849, 45161, 44220, 37054, 32265, 45119, 37059, 32264, 26239, 32822, 36894, 44224, 44121, 28308, 36906, 18367, 36914, 26821, 37047, 35894, 44210, 57960, 37042, 25564, 45136, 35908, 35866, 20895, 35882, 45208, 45138, 17475, 35871, 20857, 35953, 44108, 45215, 42698, 44280, 26782, 35847, 44253, 25571, 20906, 61366, 35944, 45172, 45221, 45228, 45223, 20896, 33015, 45193, 26740, 1873, 44288, 61619, 44234, 26744, 35295, 17464, 45220, 35838, 35845, 35900, 36963, 1883, 35848, 35895, 61368, 45227, 1919, 45069, 31716, 45243, 20814, 35850, 20156, 36889, 18207, 35952, 35765, 45277, 35801, 36896, 20802, 35877, 45348, 35873, 33264, 44125, 36895, 26211, 20907, 20851, 45187, 25561, 45238, 45066, 33263, 61274, 33261, 45371, 20161, 61410, 32545, 6762, 40503, 38660, 45242, 20937, 20936, 20928, 44187, 42696, 35766, 61414, 17442, 36911, 45121, 45307, 35897, 25566, 25574, 45417, 33807, 35881, 45183, 37052, 45386, 45408, 45381, 45368, 33223, 45150, 35902, 44256, 45311, 45294, 35943, 45310, 44042, 37050, 32796, 45364, 45256, 45387, 45330, 26743, 35886, 45332, 44199, 45293, 45331, 45329, 45291, 45312, 38658, 45366, 45363, 44043, 45184, 35905, 33260, 37043, 7160, 45435, 45323, 6750, 45288, 35906, 45336, 17453, 42695, 45333, 25565, 45545, 45321, 33810, 45326, 45320, 44184, 45395, 20859, 44293, 33014, 36837, 35945, 45442, 1943, 45423, 45396, 42700, 12431, 36892, 45181, 45400, 44174, 35767, 45401, 35904, 36832, 12082, 45425, 17469, 45278, 45511, 20940, 45585.
2025-03-22 15:16:59 UTC:10.3.206.139(34877):postgres@meeting_api:[45081]:STATEMENT: COMMIT
2025-03-22 15:16:59 UTC:10.3.161.44(22163):postgres@meeting_api:[20841]:LOG: process 20841 acquired AccessExclusiveLock on object 0 of class 1262 of database 0 after 1015.921 ms
2025-03-22 15:16:59 UTC:10.3.161.44(22163):postgres@meeting_api:[20841]:STATEMENT: COMMIT
2025-03-22 15:16:59 UTC:10.3.254.68(52497):postgres@meeting_api:[61596]:LOG: process 61596 still waiting for AccessExclusiveLock on object 0 of class 1262 of database 0 after 1000.192 ms
2025-03-22 15:16:59 UTC:10.3.254.68(52497):postgres@meeting_api:[61596]:DETAIL: Process holding the lock: 20841. Wait queue: 17474, 20898, 1931, 20926, 35855, 14865, 20846, 31717, 36912, 20927, 45081, 61596, 44128, 17462, 4576, 35852, 35940, 35854, 35864, 37057, 26765, 37041, 35872, 18380, 44271, 35802, 35840, 33384, 44279, 62275, 35440, 35948, 35804, 45084, 45147, 32250, 35898, 20932, 35862, 35859, 56845, 44233, 17448, 26745, 35883, 35865, 26753, 20809, 1929, 14858, 36904, 17452, 35892, 36910, 32798, 20892, 35899, 36901, 45137, 45105, 36835, 36897, 35901, 32036, 35856, 45171, 35941, 37046, 45160, 33013, 17458, 35874, 44092, 35893, 18356, 37055, 35942, 1939, 38662, 45079, 35889, 35839, 37058, 36900, 35910, 37056, 35951, 35907, 36908, 26767, 25575, 32037, 35868, 44278, 45188, 45120, 61287, 35863, 20817, 45062, 37048, 45151, 45179, 35939, 35849, 45161, 44220, 37054, 32265, 45119, 37059, 32264, 26239, 32822, 36894, 44224, 44121, 28308, 36906, 18367, 36914, 26821, 37047, 35894, 44210, 57960, 37042, 25564, 45136, 35908, 35866, 20895, 35882, 45208, 45138, 17475, 35871, 20857, 35953, 44108, 45215, 42698, 44280, 26782, 35847, 44253, 25571, 20906, 61366, 35944, 45172, 45221, 45228, 45223, 20896, 33015, 45193, 26740, 1873, 44288, 61619, 44234, 26744, 35295, 17464, 45220, 35838, 35845, 35900, 36963, 1883, 35848, 35895, 61368, 45227, 1919, 45069, 31716, 45243, 20814, 35850, 20156, 36889, 18207, 35952, 35765, 45277, 35801, 36896, 20802, 35877, 45348, 35873, 33264, 44125, 36895, 26211, 20907, 20851, 45187, 25561, 45238, 45066, 33263, 61274, 33261, 45371, 20161, 61410, 32545, 6762, 40503, 38660, 45242, 20937, 20936, 20928, 44187, 42696, 35766, 61414, 17442, 36911, 45121, 45307, 35897, 25566, 25574, 45417, 33807, 35881, 45183, 37052, 45386, 45408, 45381, 45368, 33223, 45150, 35902, 44256, 45311, 45294, 35943, 45310, 44042, 37050, 32796, 45364, 45256, 45387, 45330, 26743, 35886, 45332, 44199, 45293, 45331, 45329, 45291, 45312, 38658, 45366, 45363, 44043, 45184, 35905, 33260, 37043, 7160, 45435, 45323, 6750, 45288, 35906, 45336, 17453, 42695, 45333, 25565, 45545, 45321, 33810, 45326, 45320, 44184, 45395, 20859, 44293, 33014, 36837, 35945, 45442, 1943, 45423, 45396, 42700, 12431, 36892, 45181, 45400, 44174, 35767, 45401, 35904, 36832, 12082, 45425, 17469, 45278, 45511, 20940, 45585.
2025-03-22 15:16:59 UTC:10.3.254.68(52497):postgres@meeting_api:[61596]:STATEMENT: COMMIT
2025-03-22 15:16:59 UTC:10.3.147.201(10551):postgres@meeting_api:[44128]:LOG: process 44128 still waiting for AccessExclusiveLock on object 0 of class 1262 of database 0 after 1000.136 ms
2025-03-22 15:16:59 UTC:10.3.147.201(10551):postgres@meeting_api:[44128]:DETAIL: Process holding the lock: 20841. Wait queue: 17474, 20898, 1931, 20926, 35855, 14865, 20846, 31717, 36912, 20927, 45081, 61596, 44128, 17462, 4576, 35852, 35940, 35854, 35864, 37057, 26765, 37041, 35872, 18380, 44271, 35802, 35840, 33384, 44279, 62275, 35440, 35948, 35804, 45084, 45147, 32250, 35898, 20932, 35862, 35859, 56845, 44233, 17448, 26745, 35883, 35865, 26753, 20809, 1929, 14858, 36904, 17452, 35892, 36910, 32798, 20892, 35899, 36901, 45137, 45105, 36835, 36897, 35901, 32036, 35856, 45171, 35941, 37046, 45160, 33013, 17458, 35874, 44092, 35893, 18356, 37055, 35942, 1939, 38662, 45079, 35889, 35839, 37058, 36900, 35910, 37056, 35951, 35907, 36908, 26767, 25575, 32037, 35868, 44278, 45188, 45120, 61287, 35863, 20817, 45062, 37048, 45151, 45179, 35939, 35849, 45161, 44220, 37054, 32265, 45119, 37059, 32264, 26239, 32822, 36894, 44224, 44121, 28308, 36906, 18367, 36914, 26821, 37047, 35894, 44210, 57960, 37042, 25564, 45136, 35908, 35866, 20895, 35882, 45208, 45138, 17475, 35871, 20857, 35953, 44108, 45215, 42698, 44280, 26782, 35847, 44253, 25571, 20906, 61366, 35944, 45172, 45221, 45228, 45223, 20896, 33015, 45193, 26740, 1873, 44288, 61619, 44234, 26744, 35295, 17464, 45220, 35838, 35845, 35900, 36963, 1883, 35848, 35895, 61368, 45227, 1919, 45069, 31716, 45243, 20814, 35850, 20156, 36889, 18207, 35952, 35765, 45277, 35801, 36896, 20802, 35877, 45348, 35873, 33264, 44125, 36895, 26211, 20907, 20851, 45187, 25561, 45238, 45066, 33263, 61274, 33261, 45371, 20161, 61410, 32545, 6762, 40503, 38660, 45242, 20937, 20936, 20928, 44187, 42696, 35766, 61414, 17442, 36911, 45121, 45307, 35897, 25566, 25574, 45417, 33807, 35881, 45183, 37052, 45386, 45408, 45381, 45368, 33223, 45150, 35902, 44256, 45311, 45294, 35943, 45310, 44042, 37050, 32796, 45364, 45256, 45387, 45330, 26743, 35886, 45332, 44199, 45293, 45331, 45329, 45291, 45312, 38658, 45366, 45363, 44043, 45184, 35905, 33260, 37043, 7160, 45435, 45323, 6750, 45288, 35906, 45336, 17453, 42695, 45333, 25565, 45545, 45321, 33810, 45326, 45320, 44184, 45395, 20859, 44293, 33014, 36837, 35945, 45442, 1943, 45423, 45396, 42700, 12431, 36892, 45181, 45400, 44174, 35767, 45401, 35904, 36832, 12082, 45425, 17469, 45278, 45511, 20940, 45585.

SpecificallyAccessExclusiveLock on object 0 of class 1262 of database 0stood out. What isobject 0 of class 1262? That is not table, row or anything familiar. We found a similar report of this behavior on a12 year old thread in the postgres mailing list. A response fromTom Lanein this thread led us to an extremely surprising finding in thepostgres source code:

 /*
 * Serialize writers by acquiring a special lock that we hold till
 * after commit. This ensures that queue entries appear in commit
 * order, and in particular that there are never uncommitted queue
 * entries ahead of committed ones, so an uncommitted transaction
 * can't block delivery of deliverable notifications.
 *
 * We use a heavyweight lock so that it'll automatically be released
 * after either commit or abort. This also allows deadlocks to be
 * detected, though really a deadlock shouldn't be possible here.
 *
 * The lock is on "database 0", which is pretty ugly but it doesn't
 * seem worth inventing a special locktag category just for this.
 * (Historical note: before PG 9.0, a similar lock on "database 0" was
 * used by the flatfiles mechanism.)
 */
 LockSharedObject(DatabaseRelationId, InvalidOid, 0,
 AccessExclusiveLock);

After reading through the surrounding code and a call sites, we found that this lock is acquired duringCOMMITqueries when a transaction has previously issued aNOTIFY. It makes sense that notifications are only sent after the transaction has committed, so that’s why the code which triggers the notifications is found inPreCommit_Notify. This is a global lock on theentire database(or to be pedantic, a global lockon all databases within the postgres instance). This lock effectively ensures that only a singleCOMMITquery can be handled at a time. Under a heavy multi-writer scenario, this turns out to be very sad news.

## Reproducing the problem

To confirm our hypothesis that the global database lock was indeed the cause, we simulated load tests on Postgres with and without theLISTEN/NOTIFYcode. The results confirm that the global database lock drastically increases lock contention in the database, often stalling it.

### WithNOTIFY

During these periods of “high load” with theLISTEN/NOTIFYcode, the database’s CPU, and I/O load actually plummet, suggesting that the database is indeed bottlenecked by a globally exclusive mutex.

### WithoutNOTIFY

Eliminating LISTEN/NOTIFY means the database is able to make full utilization of all allocated CPU cores. This means it can make quick progress through the spike in load and recover without intervention.

## Remediation

We concluded that having a single global mutex withinCOMMITqueries was unacceptable. We decided to migrate away fromLISTEN/NOTIFYin favor of tracking this logic at the application layer. Given we had only a single (but critical) codepath relying on it, the migration took under a day to ship. Since then, our Postgres has been ticking along smoothly.

We are hiring engineers!Join us in building the future of engineering at Recall.ai
We are hiring for a number of roles,apply hereto join our close-knit team.

Written By:
Elliot Levin
Table of Contents

* TL;DR
* How we discovered it
* Reproducing the problemWith NOTIFYWithout NOTIFY
* With NOTIFY
* Without NOTIFY
* Remediation
