---
title: GitHub - tiliondev/fortress: Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change. · GitH...
url: https://github.com/tiliondev/fortress
date: 2026-07-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-13T12:29:29.679935
---

# GitHub - tiliondev/fortress: Stealth Chromium engine that stops scrapers and browser agents from getting blocked, with one line of code change. · GitH...

# Fortress – Stealth Chromium Engine

## What it is
- A fork of Chromium that modifies the browser fingerprint **inside the C++ engine**, eliminating the need for JavaScript stealth patches.  
- Presents itself as a regular Chrome installation, so bot detectors (CreepJS, Sannysoft, BrowserScan, Cloudflare Turnstile, etc.) read it as a human browser.  
- Exposes a standard CDP endpoint; existing Playwright, Puppeteer, or any CDP client can connect without code changes apart from pointing to the new endpoint.

## Key Features
- **Native‑code parity**: All spoofed getters return native code strings, consistent across main frames, iframes, and Web Workers.  
- **Drop‑in CDP**: Use `connect_over_cdp` (Playwright) or `connectOverCDP` (Node) to drive the engine; no runtime‑enable‑leak flags required.  
- **Zero headless detection**: 0 % detection on CreepJS; clears Sannysoft, BrowserScan, and live Cloudflare Turnstile challenges.  
- **Auditable patches**: 34 small, single‑purpose diffs located in `patches/`; can be reviewed in minutes and rebuilt with a single script.  
- **Coherent persona**: Engine, V8, Blink, and BoringSSL stay in sync, producing matching JA3/JA4 TLS fingerprints and user‑agent strings.  
- **Tunable identity**: One binary provides a Windows‑style persona; `--uxr-*` flags let you override GPU, screen, timezone, hardware, client‑hints, etc.  
- **Monthly upstream rebases**: Keeps the fork close to the official Chromium release cycle.

## Recent Release (151.0.7908.0)
- Per‑launch coherent personas with hardened defaults.  
- Locale‑aware keyboard layouts (QWERTY, QWERTZ, AZERTY) and per‑persona media devices.  
- Full delivery‑parity coherence pass ensuring platform, GPU, timezone, language, voices, and keyboard move together as a single real device.  
- Continued native‑code parity and realm‑invariant behavior.

## Quick Start
- **Python / Node (pre‑built binary)**  
  ```bash
  pip install -U tilion-fortress      # Python
  npm install tilion-fortress          # Node
  ```
- **Docker**  
  ```bash
  docker run --rm -p 9222:9222 tilion/fortress:latest
  ```
- **Portable bundle** (Linux example)  
  ```bash
  tar xzf tilion-fortress-linux-x64.tar.gz
  ./tilion-fortress/tilion --headless=new --remote-debugging-port=9222 --user-data-dir=/tmp/p
  ```

## Example Usage (Python)
```python
from tilion_fortress import Fortress
from playwright.sync_api import sync_playwright

with Fortress() as f:
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f.cdp_url)
        page = browser.new_page()
        page.goto("https://bot.sannysoft.com")
        page.screenshot(path="all-green.png")
```

## Example Usage (Node)
```javascript
import { Fortress } from "tilion-fortress";
import { chromium } from "playwright";

const f = await Fortress.launch();               // starts stealth engine
const browser = await chromium.connectOverCDP(f.cdpUrl);
const page = await browser.newPage();
await page.goto("https://browserscan.net");
await browser.close();
await f.close();
```

## Real‑World Results
- **Akamai Bot Manager**: Residential IP that is blocked with stock/headless Chrome becomes accepted after switching to Fortress; the `_abcksensor` cookie is set correctly.  
- **Major retailers** (Lowes, Macy’s, Kohl’s) that previously returned “Access Denied” now load normally.  
- **Full scraping pipelines**: Structured JSON extraction, auto‑pagination, deep‑detail crawls (UPC, price, tax, stock, reviews) succeed without additional stealth plugins.

## Ecosystem Compatibility
- Works with existing automation stacks: Playwright, Puppeteer, Crawl4AI, Stagehand, LangChain, etc.  
- Provides 29 stealth‑browser tools for AI agents (beta) via the “Fortress MCP”.  
- Documentation includes troubleshooting, FAQ, roadmap, and repository layout.

## Build & Verify
- Source can be rebuilt from the `patches/` directory using the provided script.  
- Verification steps ensure provenance and reproducibility of the binary.  

---  
*Fortress delivers a truly stealthy Chromium experience by fixing fingerprinting at the engine level, allowing existing automation code to run unchanged while bypassing modern bot detection.*