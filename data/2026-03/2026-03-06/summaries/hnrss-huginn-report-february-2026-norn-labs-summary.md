---
title: Huginn Report: February 2026 | Norn Labs
url: https://www.norn-labs.com/blog/huginn-report-feb-2026
date: 2026-03-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-06T06:01:27.072459
---

# Huginn Report: February 2026 | Norn Labs

# Summary of Huginn Report: February 2026

## Overview
- This post launches a monthly series sharing the phishing sites Huginn discovers, analyzing attacks, and evaluating detection tools.
- Goal: provide a resource on the current phishing landscape and showcase our tools.

## Key Numbers
- **254** confirmed phishing URLs identified from public threat‑intel feeds in February.
- Google Safe Browsing (GSB) flagged only **41** (≈ 16 %) → **83.9 %** missed at scan time.
- **Muninn Automatic Scan** caught **94.1 %** (238/254) of phishing sites.
- **Muninn Deep Scan** caught **100 %** of phishing sites (zero false negatives).
- **58.7 %** of phishing sites (149/254) were hosted on trusted platforms such as Weebly, Vercel, GitHub, Google Docs, etc.

## Detection Performance
- **Automatic Scan (263 URLs total)**
  - True Positives: 238
  - False Positives: 6
  - False Negatives: 15 (all recovered by Deep Scan)
  - True Negatives: 3
- **Deep Scan** flagged all 254 phishing sites but also marked all 9 legitimate sites as suspicious—acceptable when actively investigating a link.
- Interpretation: Automatic Scan serves as a low‑noise, always‑on safety net; Deep Scan provides a thorough second opinion.

## Where Phishing Lives
- Attackers exploit reputable hosting services to avoid blocklist bans.
- Platform breakdown (phishing sites / GSB catches):
  - Weebly: 51 / 2
  - Vercel: 40 / 8
  - Wix: 7 / 0
  - IPFS: 13 / 1
  - Google domains (Docs, Forms, Sites, Apps Script): 16 / 0
- Because these domains host millions of legitimate sites, detection must occur at the page level rather than via domain blocklists.

## Impersonated Brands
- Most‑targeted brands (by number of phishing pages):
  1. Microsoft – 28
  2. Google – 21
  3. Netflix – 19
  4. Amazon – 16
  5. AT&T – 13
- Crypto/DeFi focus: 14 sites impersonating Uniswap, Raydium, pump.fun, Trezor, MetaMask, reflecting the fast‑moving, wallet‑connected user base.

## Notable Attack Example
- **Two‑Stage S3 Credential Harvest**
  - Stage 1: Lure page on an Amazon S3 bucket with innocuous URL path, prompting email entry.
  - Stage 2: Redirect (token‑based) to a Microsoft login page that pre‑fills the entered email.
  - Evasion tricks:
    - First visit shows login page; later visits redirect to benign content (e.g., Wikipedia).
    - Anti‑bot measures on redirect domain hinder automated scanners.
  - Splitting the flow helps bypass email filters, Safe Browsing, and other blocklist‑based defenses.
