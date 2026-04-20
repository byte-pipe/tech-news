---
title: I Built a Local AI Agent That Audits My Own Articles. It Flagged Every Single One. - DEV Community
url: https://dev.to/dannwaneri/i-built-a-local-ai-agent-that-audits-my-own-articles-it-flagged-every-single-one-pkh
date: 2026-03-30
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-04-01T01:33:02.920753
---

# I Built a Local AI Agent That Audits My Own Articles. It Flagged Every Single One. - DEV Community

# I Built a Local AI Agent That Audits My Own Articles. It Flagged Every Single One.

## The problem I was actually solving
- Agencies spend time each week manually opening spreadsheets, visiting client URLs, checking title tags, meta descriptions, H1s, and broken links, then compiling reports.
- The work is deterministic but remains manual because no alternative tool existed.

## The stack
- **Browser Use** – Python‑native automation with a visible Chromium window (Playwright), not headless, preserving real rendering and session state.
- **Claude API (Sonnet)** – Reads a snapshot of each page and returns structured JSON (title status, description status, H1 count, canonical tag, flags) with one call per URL.
- **httpx** – Asynchronous HEAD requests for broken‑link detection (max 50 links per page, 5 s timeout).
- **Flat JSON files** – `state.json` tracks progress, enabling safe interruption and restart without a database.

## Human‑in‑the‑loop (HITL) handling
- When a non‑200 response, login redirect, or a title containing “sign in”/“access denied” is detected, the agent pauses.
- Interactive mode lets the user skip, retry, or quit; auto mode logs the URL in `needs_human[]` and continues.
- This prevents silent failures that most tutorials ignore.

## What the audit actually found
| Platform / URL | Failing field(s) |
|----------------|------------------|
| hashnode.com/@dannwaneri | H1 missing |
| freeCodeCamp – how‑to‑build‑your‑own‑claude‑code‑skill | Meta description |
| freeCodeCamp – how‑to‑stop‑letting‑ai‑agents‑guess | Meta description |
| freeCodeCamp – build‑a‑production‑rag‑system | Title + meta description |
| freeCodeCamp – author/dannwaneri | Meta description |
| dev.to – the‑gatekeeping‑panic | Title too long |
| dev.to – i‑built‑a‑production‑rag‑system | Title too long |

- FreeCodeCamp issues stem from platform‑level template constraints.
- DEV.to titles exceed the ~60‑character limit for clean Google rendering.

## Scheduling the run
- Command: `python index.py --auto`
- Wrap in a `.bat` file that sets `ANTHROPIC_API_KEY` and call the command.
- Schedule with Windows Task Scheduler (e.g., Monday 7 am) to generate `report-summary.txt` automatically.

## Cost
- One Claude Sonnet call ≈ $0.002 per page.
- A 20‑URL weekly audit costs < $0.05.
- Browser runs locally, avoiding cloud browser fees.
- Entire setup fits a $5/month budget.

## Code and usage
- Repository: `github.com/dannwaneri/seo-agent`
- Steps: clone repo → add URLs to `input.csv` → set `ANTHROPIC_API_KEY` → `pip install -r requirements.txt` → `playwright install chromium` → `python index.py`.
- The freeCodeCamp tutorial walks through each module (browser integration, Claude prompt, async link checker, HITL logic).

## The shift worth naming
- Traditional automation relies on fragile selectors (Playwright, Selenium, Puppeteer).
- This agent extracts information via Claude’s semantic view of the accessibility tree, using prompts instead of hard‑coded selectors.
- Result: scripts no longer break when CSS classes change; reasoning adapts to page changes.
- The brittleness moves from selector maintenance to prompt design and LLM behavior.

## Outlook
- First in a series of practical local AI agents for agency workflows.
- Full step‑by‑step tutorial for freeCodeCamp forthcoming; repo already live.
