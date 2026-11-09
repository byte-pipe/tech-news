---
title: Goodbye Claude, Hello Pi
url: https://caleb.software/posts/claude-to-pi.html
date: 2026-11-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:04.776387
---

# Goodbye Claude, Hello Pi

# Goodbye Claude, Hello Pi

## Background
- Author has been a longtime user of Claude Code since its inclusion in Claude Pro over a year ago.  
- Initially impressed by its ability to generate Python code from a single prompt.  
- Decided to retire Claude Code as the primary coding harness and switch to Pi.  
- Anthropic responded by adding AGENTS.md support, but the change came too late for the author.

## Main Complaints About Claude Code
- **AGENTS.md format** creates friction; users must copy or symlink between Claude and AGENTS formats.  
- **IDE integration limits**: only one session can be connected to VSCode at a time, preventing multiple tabs from receiving text‑selection events.  
- **Official VSCode GUI extension issues**: many built‑in slash commands fail, no custom status line, sub‑agent messages clutter the main chat thread.  
- **Feature bloat vs. stability**: rapid addition of dynamic workflows, agent teams, ultra‑reviews increases token usage without clear user benefit.  
- **Frequent disruptive releases**: 244 releases in the current year, with over 75 % altering system prompts or tool descriptions, leading to inconsistent LLM behavior.  
- **Excessive system prompt size**: default Bash tool description is ~3,000 tokens, containing redundant instructions that the model already knows.  

## Reasons for Switching to Pi
- Pi offers a **stable, minimalist design** with lower overhead.  
- High **customizability**; author has already built extensions to fit personal workflow.  
- Development of needed features (e.g., multi‑tab handling) was quick and easy with Pi (≈20 minutes).  
- Belief that open‑source harnesses can avoid the “feature‑tacking” seen in Claude Code.  

## Outlook and Recommendations
- Author acknowledges Claude Code’s pioneering role but views it as lacking a clear product vision and disciplined feature gating.  
- Encourages others experiencing similar frustrations to try an open‑source harness like Pi.  

## Contact & Publication Details
- Email: calebdotsoftware@gmail.com  
- Subscribe via email or RSS for future posts.  
- Discussion links: Twitter, Mastodon, Bluesky.  
- Original post created 21 Sep 2026, updated 07 Nov 2026, build 2f1e49.