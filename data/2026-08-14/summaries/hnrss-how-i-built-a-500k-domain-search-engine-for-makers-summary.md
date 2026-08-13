---
title: How I built a 500k-Domain Search Engine for Makers in a Weekend for $10 | marlin
url: https://alexmorleyfinch.github.io/marlin/history/v1/article/the_birth.html
date: 2026-08-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-14T06:03:11.839266
---

# How I built a 500k-Domain Search Engine for Makers in a Weekend for $10 | marlin

# How I built a 500k-Domain Search Engine for Makers in a Weekend for $10

## Goal and Scope
- Build a personal search engine that surfaces makers, artists, indie developers, and small projects, not the corporate bulk of the web.  
- Index only homepages, storing about 1 KB of metadata per domain (name, short summary, category, tags).  
- Target size: a few hundred thousand sites, under 1 GB on disk.  
- No multi‑tenant features, no full‑HTML storage, no recrawl scheduler, no user accounts.

## Architecture
- **Fetcher** – pulls a pending domain via HTTPS/HTTP, extracts title, body text, and outbound links with a simple HTML parser (no JavaScript). Marks the row “ready.”  
- **Worker** – consumes “ready” rows, skips empty or bot‑challenge pages, sends the text to a small local LLM (Gemma, 4 B parameters) which returns a name, summary, category, and tags; then discards the raw text and enqueues outbound links with priority.  
- **Steward** – monitors hosts that produce many pages, asks the model to “block, keep, or unsure,” and maintains a blocklist.  
- **API & UI** – tiny web interface with fuzzy search, category filters, and a dashboard showing crawl progress.  
- All metadata lives in a single Postgres table; raw page text exists only while the model processes it.

## Crawl Strategy and Queue Prioritization
- Initial seed list was corporate‑heavy, resulting in >90 % corporate pages.  
- Introduced `category‑priority.txt` to boost portfolios, zines, software, and demote corporate/docs pages.  
- Prioritization rules:
  - Trust visible body text > title > domain name when generating summaries.  
  - Skip the model for near‑empty or parked pages; mark them and move on.  
  - Cap subdomains per root domain at 100 to prevent Tumblr/Neocities domination.  
  - Maintain an explicit blocklist for known spam or “forum farm” sites.  
- Reseeded crawl with ~10 deliberately chosen “maker” doors (tilde communities, indie blogging platforms, webrings); the final index largely derives from links discovered from these seeds.

## Issues Encountered
- **Misplaced category label** – a short summary like “academic‑profile” ended up in the wrong field; solved by treating unusually short summaries as failures and retrying with a stricter prompt.  
- **Parked domain misclassification** – a GoDaddy parking page was labeled “for the furry community” because the model latched onto the word in the hostname; fixed by prioritizing visible text and ignoring empty bodies.  
- **GPU rental problems** – first setup used a wrapper that spawned an unnecessary distributed framework, causing CPU contention and throttling the GPU. Switched to a plain inference server. A cold‑start memory spike crashed the server at high concurrency; resolved by ramping concurrency gradually instead of launching at full load.

## Cost and Performance
- Overnight GPU rental cost ≈ $10.  
- Local consumer GPU processed ~1 page/second; rented GPU provided needed concurrency for the weekend run.  
- Final dataset: 560,183 homepages, stored in <1 GB of disk space.

## Lessons Learned
- Simple priority weighting of categories is an effective steering mechanism for a focused crawl.  
- Discarding raw HTML after model inference keeps storage requirements minimal.  
- Subdomain caps and explicit blocklists prevent spam‑heavy platforms from overwhelming the index.  
- Renting a GPU is inexpensive but requires a clean inference setup; avoid extra CPU‑heavy wrappers and handle cold‑start spikes carefully.