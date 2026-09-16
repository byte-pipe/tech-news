---
title: Ubuntu 26.10 completes transition to Rust-based coreutils - OMG! Ubuntu
url: https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete
date: 2026-09-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-16T10:38:56.414629
---

# Ubuntu 26.10 completes transition to Rust-based coreutils - OMG! Ubuntu

# Ubuntu 26.10 completes transition to Rust‑based coreutils

## Overview
- Ubuntu 26.10 (“Stonking Stingray”) finalizes the migration of core utilities to Rust implementations.  
- The three commands (cp, mv, rm) that were held back in Ubuntu 26.04 LTS due to TOCTOU issues are now included after upstream fixes.

## Background
- In Ubuntu 26.04 LTS the GNU versions of cp, mv and rm remained because the Rust‑based uutils had time‑of‑check‑to‑time‑of‑use vulnerabilities.  
- Canonical began “oxidising” the distribution in 2025, replacing foundational C software with memory‑safe Rust alternatives.  
- Ubuntu 25.10 was the first release to ship Rust‑based utilities and made Rust‑based sudo the default.

## Security and Funding
- Rust catches memory bugs at compile time, providing security benefits over C‑based tools.  
- Canonical commissions security audits; an audit of uutils before 26.04 identified the issues that delayed the three commands.  
- Canonical contributes €40 000 per year as a gold sponsor of the Trifecta Tech Foundation, which funds Rust software development.

## Future Plans
- The Trifecta Tech Foundation is rewriting the Network Time Protocol (NTP) in Rust; Ubuntu plans to adopt it as the default time‑sync client by 27.10.  
- The Rust‑based uutils aim for drop‑in compatibility with GNU versions; any deviation is treated as a bug, so end users see no functional difference.

## Release Timeline
- Ubuntu 26.10 beta arrives later this month.  
- Stable release is scheduled for 15 October 2026.