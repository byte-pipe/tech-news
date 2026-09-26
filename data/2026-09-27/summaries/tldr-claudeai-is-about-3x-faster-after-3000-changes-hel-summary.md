---
title: Claude.ai is about 3x faster after 3,000+ changes - Help Net Security
url: https://www.helpnetsecurity.com/2026/09/24/anthropic-claude-ai-faster
date: 2026-09-27
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-27T06:01:09.880876
---

# Claude.ai is about 3x faster after 3,000+ changes - Help Net Security

# Claude.ai is about 3x faster after 3,000+ changes

## Overview
- Anthropic engineers increased the speed of Claude.ai and the Claude desktop app by roughly three times during a two‑week sprint in August 2026.  
- More than 3,000 code changes were merged, and none resulted in customer‑facing incidents or rollbacks.

## Process
- All coordination occurred in a single Slack channel.  
- An internal research model comparable to Opus 5.5 (via the Claude Tag beta) was used.  
- Claude generated benchmarks, opened pull requests, and monitored each deployment; humans set goals, made judgment calls, and approved every change.  
- At peak activity, over 150 Slack threads were running concurrently.

## Performance Metrics
- Wall‑clock timing was deemed too noisy, so deterministic counts such as CPU instruction counts were used.  
- Reducing instruction count by 48 % on a hot path cut real‑time latency by 78 %.  
- A CI check rejected any change that increased the instruction count, preserving the performance gains.

## Specific Optimizations
- Highlighting a finished code block could freeze the page for about a second; the cause was em dashes.  
- Any character outside Latin‑1 (e.g., em dashes, curly quotes) forced V8 (Chrome’s JavaScript engine) to store the reply as UTF‑16 and push syntax‑highlighting regexes onto a slower execution path.  
- A 20‑line code change resolved the issue.

## Risk Management
- Risky changes were placed behind short‑lived feature flags and first rolled out to employees.  
- Nearly 200 flags were added during the sprint; more than half were removed by the end.  
- Engineer Isaac G. remarked, “You could not have convinced me this was possible even six months ago.”

## Source
- Anthropic internal reports summarized in Help Net Security.