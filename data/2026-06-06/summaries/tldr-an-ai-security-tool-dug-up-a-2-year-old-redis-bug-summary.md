---
title: An AI Security Tool Dug Up a 2-Year-Old Redis Bug That Lets Attackers Take Over Servers - Cyber Kendra
url: https://www.cyberkendra.com/2026/06/an-ai-security-tool-dug-up-2-year-old.html
date: 2026-06-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:50:38.118192
---

# An AI Security Tool Dug Up a 2-Year-Old Redis Bug That Lets Attackers Take Over Servers - Cyber Kendra

# An AI Security Tool Dug Up a 2‑Year‑Old Redis Bug That Lets Attackers Take Over Servers

## Overview
- A use‑after‑free vulnerability (CVE‑2026‑23479) existed in Redis since version 7.2.0 and was unnoticed for over two years.  
- The flaw was discovered by the autonomous AI security tool Xint Code and demonstrated live at ZeroDay.Cloud 2025.  
- Redis released patches on 5 May 2026; no active exploitation has been observed.

## Bug Description
- Located in `unblockClientOnKey()` within `blocked.c`.  
- When a blocked client is evicted at a precise moment, the function continues to use a pointer to memory that has already been freed, creating a use‑after‑free condition.  
- An attacker can fill the freed memory with crafted data to gain control.

## Exploit Chain
1. A one‑line Lua script leaks a heap address.  
2. The attacker inflates a client’s memory buffer, parks it on a stream command, then lowers memory limits to force eviction during the call.  
3. A `SET` command reuses the freed slot with a fake client structure, leading to an out‑of‑bounds write.  
4. The write overwrites the GOT entry for `strcasecmp()` with `system()`.  
5. Subsequent Redis commands are executed as OS shell commands, giving full code execution as the Redis daemon.

## Impact
- Full remote code execution with the privileges of the Redis process.  
- Access to all keys, configuration credentials, and network‑connected services.  
- Wiz analysis: ~80 % of cloud environments run Redis; ~85 % of those instances lack authentication, expanding the practical attack surface beyond the CVSS 7.7 rating.

## Affected and Fixed Versions
- Affected: 7.2.0 – 7.2.13, 7.4.8, 8.2.5, 8.4.2, 8.6.2.  
- Fixed: 7.2.14, 7.4.9, 8.2.6, 8.4.3, 8.6.3.  
- Redis Cloud customers are already protected via automatic patch deployment.

## Mitigation Recommendations
- Upgrade self‑managed Redis instances to the fixed versions immediately.  
- If immediate upgrade is not possible, restrict `CONFIG`, `@scripting`, and stream commands to only necessary roles; the exploit requires all three in a single session.  

## Current Status
- No known active exploitation in the wild as of the article’s publication.