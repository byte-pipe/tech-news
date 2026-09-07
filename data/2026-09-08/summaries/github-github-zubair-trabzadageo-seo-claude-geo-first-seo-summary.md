---
title: GitHub - zubair-trabzada/geo-seo-claude: GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scorin...
url: https://github.com/zubair-trabzada/geo-seo-claude
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:32:06.186717
---

# GitHub - zubair-trabzada/geo-seo-claude: GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scorin...

# geo-seo-claude Overview

## Repository Structure
- Main directories: `geo/`, `skills/`, `agents/`, `scripts/`, `schema/`, plus configuration files (`README.md`, `install.sh`, etc.).
- `skills/` contains 13 specialized sub‑skills (audit, citability, crawlers, llms.txt, brand mentions, platform optimizer, schema, technical, content, report, PDF report, prospect, proposal, compare).
- `agents/` holds 5 parallel sub‑agents for different analysis areas.
- `scripts/` provides Python utilities for fetching pages, scoring citability, scanning brands, generating `llms.txt`, and creating PDF reports.
- `schema/` includes ready‑to‑use JSON‑LD templates for various entity types.

## Why GEO Matters (2026)
| Metric | Value |
|--------|-------|
| GEO services market | $850 M+ (projected $7.3 B by 2031) |
| AI‑referred traffic growth | +527 % YoY |
| AI traffic conversion vs organic | 4.4 × higher |
| Predicted search traffic drop by 2028 | –50 % |
| Brand mentions vs backlinks for AI | 3 × stronger correlation |
| Marketers investing in GEO | Only 23 % |

## Quick Start (Installation)
- **macOS/Linux one‑command:** `curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash`
- **Manual:** `git clone https://github.com/zubair-trabzada/geo-seo-claude.git && cd geo-seo-claude && ./install.sh`
- **Windows (Git Bash) one‑command:** `curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install-win.sh | bash`
- **Windows manual:** same clone steps, then `./install-win.sh`

## Requirements
- Python 3.8+ (Ubuntu/Debian: `python3-venv`)
- Claude Code CLI
- Git
- Optional: `uv` for faster dependency install
- Optional: Playwright (for screenshots)

## Commands (run in Claude Code)
- `/geo audit <url>` – full GEO + SEO audit
- `/geo quick <url>` – 60‑second visibility snapshot
- `/geo citability <url>` – AI citation readiness score
- `/geo crawlers <url>` – AI crawler access check
- `/geo llmstxt <url>` – analyze or generate `llms.txt`
- `/geo brands <url>` – scan brand mentions on AI‑cited platforms
- `/geo platforms <url>` – platform‑specific optimization
- `/geo schema <url>` – structured data analysis/generation
- `/geo technical <url>` – technical SEO audit
- `/geo content <url>` – content quality & E‑E‑A‑T assessment
- `/geo report <url>` – client‑ready markdown report
- `/geo report-pdf` – PDF report with charts and visualizations

## Architecture Overview
- `geo/` – orchestrator with `SKILL.md`
- `skills/` – 13 sub‑skills handling distinct audit components
- `agents/` – 5 parallel agents for AI visibility, platform analysis, technical SEO, content, and schema
- `scripts/` – Python helpers for fetching, scoring, scanning, generating files, PDF creation
- `schema/` – pre‑built JSON‑LD templates (Organization, LocalBusiness, Article‑Author, Software‑SaaS, Product, Website‑SearchAction)

## Data Storage
- Runtime data stored outside Claude Code at `~/.geo-prospects/`:
  - `prospects.json` – pipeline data
  - `proposals/` – generated proposal markdown files
  - `reports/` – monthly delta reports
- Uninstaller does **not** delete this directory; remove manually if desired.

## How It Works
### Full Audit Flow (`/geo audit <url>`)
1. **Discovery:** fetch homepage, detect business type, crawl sitemap.
2. **Parallel Analysis:** launch 5 sub‑agents simultaneously for AI visibility, platform analysis, technical SEO, content quality, and schema markup.
3. **Synthesis:** aggregate scores into a composite GEO Score (0‑100).
4. **Report:** output prioritized action plan with quick wins.

### Scoring Methodology
- AI Citability & Visibility – 25 %
- Brand Authority Signals – 20 %
- Content Quality & E‑E‑A‑T – 20 %
- Technical Foundations – 15 %
- Structured Data – 10 %
- Platform Optimization – 10 %

## Key Features
- **Citability Scoring:** evaluates content blocks (134‑167 words, self‑contained, fact‑rich) for AI citation readiness.
- **AI Crawler Analysis:** checks `robots.txt` for 14+ AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) and gives allow/block recommendations.
- **Brand Mention Scanning:** scans YouTube, Reddit, Wikipedia, LinkedIn, and 7+ other platforms; brand mentions correlate 3 × stronger with AI visibility than backlinks.
- **Platform‑Specific Optimization:** provides tailored recommendations per AI platform; only 11 % of domains are cited by both ChatGPT and Google AI Overviews for the same query.
- **`llms.txt` Generation:** creates/validates the emerging `llms.txt` standard to improve AI discoverability.