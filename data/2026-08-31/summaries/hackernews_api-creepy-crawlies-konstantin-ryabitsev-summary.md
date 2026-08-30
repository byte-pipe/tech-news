---
title: Creepy crawlies — Konstantin Ryabitsev
url: https://people.kernel.org/monsieuricon/creepy-crawlies
date: 2026-08-30
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:22:54.285741
---

# Creepy crawlies — Konstantin Ryabitsev

# Creepy crawlies — Konstantin Ryabitsev

## TL;DR
- Rendering commits for scrapers consumes more CPU cycles than all legitimate access combined.  
- Across five geo‑distributed nodes, 14 – 16 of the 90 cores are dedicated solely to serving scraper requests (≈20 % of capacity).

## Why git.kernel.org is attractive to crawlers
- The kernel’s full history is openly available and free of AI‑generated content, making it ideal training data for large language models.  
- Every commit, patch, diff, and plain render is reachable via simple URLs, providing billions of “clean” data points.

## The inefficient scraping method
- Instead of cloning the repository, bots request each commit as an HTML page and parse it.  
- Linux.git contains ~1.48 M commits; with ~922 forks, bots can generate over a **bajillion** valid URLs for the same data.  
- cgit exposes additional renderings (patches, diffs, etc.), further inflating the URL space.

## Early mitigation attempts
- Initially blocked obvious bots by user‑agent and IP using fail2ban.  
- Bots began masquerading as regular browsers, prompting IP‑ and subnet‑wide bans, even targeting entire ASNs.  
- Later, bots switched to millions of residential/mobile IPs, making per‑IP bans ineffective and inflating firewall rules.

## Introducing computational challenges (Anubis)
- Deployed a proof‑of‑work challenge (SHA‑256 with leading zeroes) before serving content.  
- Early low difficulty (4 leading zeroes) stopped most bots; legitimate users tolerated the delay.  
- Raising difficulty to 5 increased legitimate user annoyance (seconds of CPU, device heating) but bought more time.  
- Bots eventually adapted and solved difficulty 5, reducing the challenge’s effectiveness.

## Current traffic profile
- ~6 M daily requests for random commits.  
- 66 % are blocked by the Anubis challenge; 33 % solve it and reach the site.  
- Rough estimate: only ~2 % of total traffic is legitimate; the rest are scrapers.

## Operational impact
- System remains responsive for human users; the biggest load spikes come from poorly designed CI jobs (e.g., simultaneous shallow clones).  
- Persistent scraper load ties up 14‑16 cores continuously, creating a 20 % baseline capacity drain, with occasional spikes higher than that.

## Outlook and next steps
- No simple fix; the team is disabling crawlable features and gating expensive actions, which will reduce anonymous functionality.  
- Future depends on AI market dynamics: a burst could lower scraper volume, or smarter bots might adopt more efficient data‑gathering methods.  
- Meanwhile, the infrastructure must continue to balance legitimate developer access against the relentless “AI crawler” demand.