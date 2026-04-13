---
title: Servo is now available on crates.io - Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.
url: https://servo.org/blog/2026/04/13/servo-0.1.0-release/
site_name: hackernews_api
content_file: hackernews_api-servo-is-now-available-on-cratesio-servo-aims-to-e
fetched_at: '2026-04-14T06:00:19.447433'
original_url: https://servo.org/blog/2026/04/13/servo-0.1.0-release/
author: The Servo Project Developers
date: '2026-04-13'
description: Initial crates.io release and LTS version of Servo
tags:
- hackernews
- trending
---

# Servo is now available on crates.io

Initial crates.io release and LTS version of Servo

Posted2026-04-13

Today the Servo team has released v0.1.0 of the servo crate.
This is ourfirstcrates.io releaseof theservocrate that allows Servo to be used as a library.

We currently do not have any plans of publishing our demo browser servoshell tocrates.io.
In the 5 releases since our initial GitHub release in October 2025, our release process has matured, with the main “bottleneck” now being the human-written monthly blog post.
Since we’re quite excited about this release, we decided to not wait for the monthly blog post to be finished, but promise to deliver the monthly update in the coming weeks.

As you can see from the version number, this release is not a 1.0 release. In fact, we still haven’t finished discussing what 1.0 means for Servo.
Nevertheless, the increased version number reflects our growing confidence inServo’s embedding APIand its ability to meet some users’ needs.

In the meantime we also decided to offer a long-term support (LTS) version of Servo, since breaking changes in the regular monthly releases are expected and some embedders might prefer doing major upgrades on a scheduled half-yearly basis while still receiving security updates and (hopefully!) some migration guides.
For more details on the LTS release, see the respectivesection in the Servo book.

Back