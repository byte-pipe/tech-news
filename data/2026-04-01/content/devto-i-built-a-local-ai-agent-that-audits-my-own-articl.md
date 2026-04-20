---
title: I Built a Local AI Agent That Audits My Own Articles. It Flagged Every Single One. - DEV Community
url: https://dev.to/dannwaneri/i-built-a-local-ai-agent-that-audits-my-own-articles-it-flagged-every-single-one-pkh
site_name: devto
content_file: devto-i-built-a-local-ai-agent-that-audits-my-own-articl
fetched_at: '2026-04-01T01:31:45.712927'
original_url: https://dev.to/dannwaneri/i-built-a-local-ai-agent-that-audits-my-own-articles-it-flagged-every-single-one-pkh
author: Daniel Nwaneri
date: '2026-03-30'
description: Not as a gotcha. As a result. Seven URLs. Seven FAILs. My Hashnode profile is missing an H1. Three... Tagged with python, automation, ai, webdev.
tags: '#python, #automation, #ai, #webdev'
---

Not as a gotcha. As a result.

Seven URLs. Seven FAILs.

My Hashnode profile is missing an H1. Three freeCodeCamp tutorials have meta descriptions that are either missing or over 160 characters. Two DEV.to articles have titles too long for Google to render cleanly.

I built the agent. I ran it on my own content first. That's the honest version of the demo.

## The problem I was actually solving

Every digital marketing agency has someone whose job is basically this: open a spreadsheet, visit each client URL, check the title tag, check the description, check the H1, note broken links, paste everything into a report. Repeat weekly.

That person costs money. The work is deterministic. The only reason it's still manual is that nobody built the alternative.

I built it in a weekend.

## The stack

* Browser Use— Python-native browser automation. The agent navigates real pages in a visible Chromium window. Not a headless scraper. Persistent sessions, real rendering, the same page a human would see.
* Claude API (Sonnet)— reads the page snapshot and returns structured JSON: title status, description status, H1 count, canonical tag, flags. One API call per URL.
* httpx— async HEAD requests for broken link detection. Capped at 50 links per page, concurrent, 5-second timeout per request.
* Flat JSON files—state.jsontracks what's been audited. Interrupt mid-run, restart, it picks up exactly where it stopped. No database needed.

Seven Python files. 956 lines total. Runs on a Windows laptop.

## The part most tutorials skip: HITL

The agent hits a login wall. Throws an exception. Run dies.

That's most automation tutorials.

This one doesn't work that way.

When the agent detects a non-200 status, a redirect to a login page, or a title containing "sign in" or "access denied", it pauses. In interactive mode: skip, retry, or quit. In--automode it skips automatically, logs the URL toneeds_human[]in state, and continues.

An agent that knows its limits is more useful than one that fails silently. That's the design decision most people don't make because tutorials don't cover it.

## What the audit actually found

I ran it against my own published content across three platforms:

URL

Failing fields

hashnode.com/
@dannwaneri

H1 missing

freeCodeCamp — how-to-build-your-own-claude-code-skill

Meta description

freeCodeCamp — how-to-stop-letting-ai-agents-guess

Meta description

freeCodeCamp — build-a-production-rag-system

Title + meta description

freeCodeCamp — author/dannwaneri

Meta description

dev.to — the-gatekeeping-panic

Title too long

dev.to — i-built-a-production-rag-system

Title too long

The freeCodeCamp description issues are partly platform-level — freeCodeCamp controls the template and sometimes truncates or omits meta descriptions. The DEV.to title issues are mine. Article titles that read well as headlines often exceed 60 characters in the<title>tag.

The agent didn't care. It checked the standard and reported the result.

## The schedule play

python index.py --auto

Add a.batfile that sets the API key and calls that command. Schedule it in Windows Task Scheduler for Monday 7am. Checkreport-summary.txtwith your coffee.

That's the agency workflow. No babysitting. Edge cases inneeds_human[]for human review. Everything else processed and reported automatically.

## What this actually costs

One Sonnet API call per URL. Roughly $0.002 per page. A 20-URL weekly audit costs less than $0.05. The Playwright browser runs locally — no cloud browser fees, no Browserbase subscription.

The whole thing runs on a $5/month philosophy. Same one I use for everything else.

## The code

GitHub:dannwaneri/seo-agent

Clone it, add your URLs toinput.csv, setANTHROPIC_API_KEYin your environment, runpip install -r requirements.txt, runplaywright install chromium, thenpython index.py.

The freeCodeCamp tutorial walks through each module — browser integration, the Claude extraction prompt, the async link checker, the HITL logic. Link in the comments when it's live.

## The shift worth naming

Browser automation has been a developer tool for a decade. Playwright, Selenium, Puppeteer — all powerful, all requiring someone to write and maintain selectors. The moment a button's class name changes, the script breaks.

This agent doesn't use selectors. It reads the page the way Claude reads it — semantically, through the accessibility tree. A "Submit" button is still a "Submit" button even if the CSS class changed.

The extraction logic is in the prompt, not in the code.

Old way:Automation breaks when the page changes.New way:Reasoning adapts. The code doesn't need to.

That's the actual shift. Not "AI does the work" but "the brittleness moved." From selectors to prompts. From maintenance to reasoning. The failure modes are different. So is the recovery.

Built this as the first in a series on practical local AI agent setups for agency operations. The freeCodeCamp step-by-step tutorial is coming. Repo is live now.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (30 comments)


For further actions, you may consider blocking this person and/orreporting abuse
