---
title: I Wrote a Scheme in 2025
url: https://maplant.com/2026-02-09-I-Wrote-a-Scheme-in-2025.html
date: 2026-02-12
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-12T06:02:25.283013
---

# I Wrote a Scheme in 2025

# I Wrote a Scheme in 2025

- Matthew Plant announced the first version (0.1.0) of scheme-rs, a new Scheme implementation, a year and one week after the initial announcement.
- The first release is available on scheme-rs.org (soon to be scheme.rs) and GitHub.
- Despite being stable enough for a first release after passing 2258 tests in the R6RS test suite, significant work remains.
- A major change since the initial announcement is the addition of support for both synchronous and asynchronous programming.
- Areas needing further development include garbage collection, performance optimization, missing R6RS procedures and syntax (like pattern matching), documentation, and debugging.
- The author is excited about future work on a new strongly-typed language built on scheme-rs, potentially using calculus of construction.
- The project originated after the author lost their job and decided to focus on a personal project, rediscovering their passion for computer science and leading to a new job they enjoy.
- The author encourages others who enjoy functional programming and Rust to find challenging projects like scheme-rs.
- Readers interested in careers related to this project are invited to check the careers page at OneChonos.

## Changes since Initial Announcement

- scheme-rs now supports both synchronous and asynchronous programming.
- This was implemented to improve adoption and personal use cases without hindering async support.
- scheme-rs can be used in both async and sync contexts.

## Things That Are Not Finished

- The garbage collector requires further improvement.
- Overall performance can be significantly enhanced.
- Many procedures and syntax from R6RS are missing, including pattern matching.
- More documentation is needed.
- Debugging capabilities need improvement.

## Origin of scheme-rs

- The project began after the author lost their job and sought to rediscover their passion for computer science.
- It was a personal project undertaken with a focus on correctness and academic backing.
- The development of scheme-rs has been personally transformative, increasing the author's confidence and leading to a fulfilling career.
- The author recommends finding personally challenging projects for those with similar inclinations.
