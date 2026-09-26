---
title: Claude.ai is about 3x faster after 3,000+ changes - Help Net Security
url: https://www.helpnetsecurity.com/2026/09/24/anthropic-claude-ai-faster
site_name: tldr
content_file: tldr-claudeai-is-about-3x-faster-after-3000-changes-hel
fetched_at: '2026-09-27T06:00:37.646030'
original_url: https://www.helpnetsecurity.com/2026/09/24/anthropic-claude-ai-faster
author: Anamarija Pogorelec
date: '2026-09-27'
published_date: '2026-09-24T08:01:04+00:00'
description: Anthropic made claude.ai faster by about 3x in a two-week sprint, with Claude writing fixes across 3,000+ changes and no reported rollbacks.
tags:
- tldr
---

Anamarija Pogorelec
, Senior Staff Writer, Help Net Security
 

September 24, 2026
 

Share
 

# Claude.ai is about 3x faster after 3,000+ changes

Anthropic engineers made claude.ai and the Claude desktop app roughly three times faster during a two-week sprint in August, with Claude finding the bottlenecks and writing the fixes. The team merged more than 3,000 changes and says none of them caused a customer-facing incident or rollback.

The engineers ran the whole thing out of one Slack channel, using an internal research model roughly comparable toOpus 5.5through the Claude Tag beta. Claude built benchmarks, opened pull requests, and watched each deploy. The humans set goals, made the judgment calls, and approved every change. At one point, more than 150 threads were running at once.

Claude worked best when it had a number to beat. Wall-clock timing is too noisy to gate code on, so Claude switched to deterministic counts such as CPU instructions. On one hot path, cutting instructions by 48% cut real time by 78%. After that, a CI check failed any change that pushed the count back up, so the win stayed put.

Some of the slowdowns hid in strange places. Highlighting a finished code block could freeze the page for about a second, and the cause was em dashes. Any character outside Latin-1, like an em dash or a curly quote, made V8, the JavaScript engine behind Chrome, store the whole reply as UTF-16 and push the syntax-highlighting regexes onto a slower path. A twenty-line change fixed it.

The team kept risky changes behind short-lived feature flags and rolled the riskiest out to employees first. Engineers added nearly 200 flags over the two weeks and removed more than half by the end. Issac G., one of the engineers behind the sprint,said: “You could not have convinced me this was possible even six months ago.”

More about

* Anthropic

Share