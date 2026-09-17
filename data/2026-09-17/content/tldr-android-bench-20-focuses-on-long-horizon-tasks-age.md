---
title: Android Bench 2.0 focuses on long-horizon tasks, agent evaluations
url: https://9to5google.com/2026/09/17/android-bench-2-0
site_name: tldr
content_file: tldr-android-bench-20-focuses-on-long-horizon-tasks-age
fetched_at: '2026-09-17T21:56:26.405688'
original_url: https://9to5google.com/2026/09/17/android-bench-2-0
author: Abner Li
date: '2026-09-17'
published_date: '2026-09-17T16:00:00+00:00'
description: Google’s development of Android Bench continues today with a version 2.0 that reflects how AI can handle more complex development tasks.
tags:
- tldr
---

* Android

# Android Bench 2.0 focuses on long-horizon tasks, agent evaluations

 

Abner Li
 | Sep 17 2026 - 9:00 am PT																

Google’s development of Android Benchcontinues todaywith a version 2.0 that reflects how AI can handle more complex development tasks.

The first version “focused on incremental changes to existing repositories,” like bug fixes or smaller feature requests.Android Bench 2.0targets “tasks of great complexity that take an engineer multiple days or even a week to complete,” such as adding new features, building apps from scratch, and converting cross-platform apps to Android.

This new focus required “more nuanced evaluation and scoring” that goes beyond pass or fail grading. Google is moving from binary to continuous scoring:

We calculate this completion rate through a combination of factors like functionality, visual fidelity, and avoiding regressions. We also apply objective scoring penalties for deviations from evaluation instructions or structural constraints.

Google has rated Gemini 3.7/3.8 Flash, OpenAI GPT-6, Anthropic Fable 5.1, Kimi K3, and Qwen 3.8 Max. GPT-6 Astra is at the top of the benchmark with a 28% pass rate (compared to scores in the 90% range with the previous approach).

 
Advertisement - scroll for more content

Google shared insights like how “porting cross-platform apps to Android remains an open challenge—no model hits a 100% pass rate, and frontier models reach at most a 80% completion rate.”

* “…AI does a better job at writing new code rather than refactoring existing code. Refactors and migrations get trickier because success depends on architectural complexity rather than code volume.”
* “Models show strong capabilities on well-established, deterministic transformations, such as converting Java to Kotlin, swapping Retrofit for Ktor, or introducing a ViewModel layer.”
* “…models struggle when tasks require runtime validation (like missing dependency injection graphs), involve breaking framework changes, or run into knowledge gaps with unreleased libraries.”

With agent evaluations, Android Bench ran “agents from the corresponding model provider,” like Gemini 3.8 Flash on Google Antigravity and GPT-5.6 Sol with Codex. Google says “harness design positively impacts developer outcomes,” with Android Bench planning to include different model and agent combinations in the future.

FTC: We use income earning auto affiliate links.More.

You’re reading 9to5Google — experts who break news about Google and its surrounding ecosystem, day after day. Be sure to check out 
our homepage
 for all the latest news, and follow 9to5Google on 
Twitter
, 
Facebook
, and 
LinkedIn
 to stay in the loop. Don’t know where to start? Check out our 
exclusive stories
, 
reviews
, 
how-tos
, and 
subscribe to our YouTube channel
 

Check out 9to5Google on YouTube for more news:

 

## Comments

## Guides

### Android

Breaking news for Android. Get the latest on app…

## Author

 

			Abner Li		

technacity			

Editor-in-chief. Interested in the minutiae of Google and Alphabet. Tips/talk: abner@9to5g.com