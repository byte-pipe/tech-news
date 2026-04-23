---
title: An update on recent Claude Code quality reports \ Anthropic
url: https://www.anthropic.com/engineering/april-23-postmortem
date: 2026-04-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:02:40.574234
---

# An update on recent Claude Code quality reports \ Anthropic

# An update on recent Claude Code quality reports

## Overview
- Three separate changes caused reported quality issues in Claude Code, the Claude Agent SDK, and Claude Cowork; the API was unaffected.  
- All issues were resolved by April 20 (v2.1.116).  
- Usage limits were reset for all subscribers on April 23.

## Issues and fixes

### 1. Change to default reasoning effort (Mar 4 – Apr 7)
- Default effort was lowered from **high** to **medium** to reduce UI‑freeze latency for Sonnet 4.6 and Opus 4.6.  
- Users reported lower intelligence and poorer code quality.  
- Reverted on Apr 7; default is now high effort for Opus 4.7 and high effort for all other models.

### 2. Caching optimization that dropped prior reasoning (Mar 26 – Apr 10)
- Intended to clear old thinking after a session was idle > 1 hour to save latency.  
- Bug caused the clearing to occur on **every** turn after the idle threshold, leading to forgetfulness, repetition, and higher token usage.  
- Affected Sonnet 4.6 and Opus 4.6.  
- Fixed on Apr 10 in v2.1.101; added support for additional repositories as context for code‑review evaluations.

### 3. System prompt change to reduce verbosity (Apr 16 – Apr 20)
- Introduced a prompt instruction to cut verbosity; combined with other prompt tweaks it degraded coding quality.  
- Impacted Sonnet 4.6, Opus 4.6, and Opus 4.7.  
- Reverted on Apr 20.

## Lessons learned and future safeguards
- Overlapping changes created the impression of broad, inconsistent degradation.  
- Initial internal usage and evaluations missed the issues because they occurred in corner cases (idle sessions, specific prompt combinations).  
- Improvements include:
  - More thorough testing of idle‑session handling and cache behavior.  
  - Expanded context support for code‑review evaluations.  
  - clearer UI communication of effort defaults and easy access to effort selectors.

## Current status
- All three issues are resolved as of v2.1.116 (April 20).  
- Usage limits have been reset for all subscribers.  
- Ongoing monitoring is in place to prevent similar regressions.