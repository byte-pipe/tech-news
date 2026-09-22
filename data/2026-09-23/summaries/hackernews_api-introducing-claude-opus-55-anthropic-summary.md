---
title: Introducing Claude Opus 5.5 \ Anthropic
url: https://www.anthropic.com/claude-opus-5-5
date: 2026-09-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-23T06:46:30.352599
---

# Introducing Claude Opus 5.5 \ Anthropic

# Claude Opus 5.5 Summary

## Overview
- First model in the new Claude 5.5 family, released September 22 2026.  
- Performs at the level of Claude Fable 5.1 on most tasks while costing 40 % less than Opus 5.  
- Tested by external evaluators (Frontier Design, METR) and passes Anthropic’s most comprehensive alignment audit.

## Performance Improvements
- Major step up from Opus 5; early testers report large gains on complex work.  
- Example: 680 k‑line code migration completed in under a day (weeks for a team).  
- Software optimization: succeeded 39/40 times in cutting load times without altering behavior, compared to smaller, riskier improvements by Opus 5.  
- Game‑building from a single prompt achieved higher graphics and polish scores than any prior Claude model.

## Safety Enhancements
- Highest scores to date on the automated behavioral audit, reducing hard‑to‑reverse actions and out‑of‑bounds behavior.  
- More resistant to prompt injection than Opus 5.  
- Alignment testing expanded to longer, impossible, and real‑incident‑modeled tasks (still with limits).  
- Deployed with safeguards similar to Claude Fable 5.1; life‑science and cyber verification programs opened for vetted organizations.

## Cost and Speed
- Requires less compute; default pricing is 40 % lower than Opus 5.  
- Token pricing: input $4 / M, output $20 / M (20 % cheaper).  
- Cache reads $0.20 / M (60 % cheaper).  
- Generates output >30 % faster than Opus 5.  
- Five‑hour usage limits increased for Pro, Max, Team, and Enterprise plans; subscription users receive a reusable rate‑limit reset.

## Communication
- Writes more naturally, with clearer structure and important information placed up front.  
- Early testers note it “writes the way I do,” improving readability and safety in long sessions.

## Benchmark Highlights
- Leads in agentic coding, computer use, and knowledge work on internal benchmarks.  
- Scores often close to Claude Fable 5.1 despite higher headline numbers.  
- Efficiency advantage evident: lower token usage translates to a 40 % cost reduction.  
- Detailed benchmark tables compare Opus 5.5 with Opus 5, Fable 5.1, GPT‑6 Astra, and GPT‑5.6 Sol across tasks such as Terminal‑Bench, FrontierCode, GDPval‑AA, Humanity’s Last Exam, and OSWorld.

## Pricing Details
| Item | Opus 5.5 | Opus 5 |
|------|----------|--------|
| Cache reads | $0.20 per M | $0.50 per M |
| Input tokens | $4 per M | $5 per M |
| Output tokens | $20 per M | $25 per M |
| Cache writes | $5 per M | $6.25 per M |

- Fast mode (up to 2.5× speed) available in Claude Code and Platform: $8 input / M, $40 output / M.

## Coding Capabilities
- Excels at large‑scale code migrations and audits.  
- Example: 200 k‑line codebase audited and fixed in <3 hours (Opus 5 took >20 hours, using 2.5× tokens).  
- HAProxy translation from C to Rust completed in 9.5 hours (vs. 12 hours for Fable 5.1) with 51 % lower cost.  
- Beats GPT‑6 Astra on FrontierCode tasks at roughly 20 % of the cost per task at default effort.

## Future Releases
- Claude Sonnet 5.5 and Claude Haiku 5.5 slated for release in the coming weeks, inheriting similar performance, efficiency, and safety improvements.