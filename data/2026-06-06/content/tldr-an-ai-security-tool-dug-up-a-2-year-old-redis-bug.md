---
title: An AI Security Tool Dug Up a 2-Year-Old Redis Bug That Lets Attackers Take Over Servers - Cyber Kendra
url: https://www.cyberkendra.com/2026/06/an-ai-security-tool-dug-up-2-year-old.html
site_name: tldr
content_file: tldr-an-ai-security-tool-dug-up-a-2-year-old-redis-bug
fetched_at: '2026-06-06T11:50:19.849340'
original_url: https://www.cyberkendra.com/2026/06/an-ai-security-tool-dug-up-2-year-old.html
date: '2026-06-06'
description: 'CVE-2026-23479: A use-after-free in Redis 7.2+ lets authenticated attackers run arbitrary OS commands. Patch now.'
tags:
- tldr
---

Home

Security

Vulnerability

# An AI Security Tool Dug Up a 2-Year-Old Redis Bug That Lets Attackers Take Over Servers

CVE-2026-23479: A use-after-free in Redis 7.2+ lets authenticated attackers run arbitrary OS commands. Patch now.

Add as preferred source

A flaw that sat undetected in Redis for over two years — silently present in every stable release since version 7.2.0 — has been patched after an AI-powered security tool demonstrated a working remote code execution exploit against it.

The vulnerability, tracked asCVE-2026-23479and rated 7.7 (High), wasdiscovered by Team Xint Codeusing Xint Code, a fully autonomous AI security analysis tool. A live exploit was demonstrated at the ZeroDay.Cloud 2025 conference in London last December. Redis shipped patches on May 5, 2026.

### What's the bug?

The flaw lives insideunblockClientOnKey()in Redis'sblocked.csource file — a function responsible for handling clients that were waiting on a key to become available. When that blocked client gets evicted from memory at exactly the wrong moment, the function continues using a pointer to memory that has already been freed.

This class of bug is known as a use-after-free (UAF) — the program keeps accessing a memory address after the data at that address has been discarded, which an attacker can exploit by filling that address with their own crafted data.

### How bad is it in practice?

The exploit chain runs in three stages: first, a one-line Lua script leaks a heap memory address; next, the attacker deliberately balloons a client's memory buffer, parks it on a stream command, then drops memory limits to trigger the eviction mid-call; finally, aSETcommand reclaims the freed memory slot with a fake client structure.

Redis then uses that fake structure to perform an out-of-bounds write, which the attacker redirects to overwrite the function pointer forstrcasecmp()in the Global Offset Table, swapping it withsystem(). The next Redis command parsed effectively becomes an OS shell command.

The result: full code execution as the Redis daemon — meaning every key, every credential in config files, and network access to adjacent services.

Wiz's analysis found that 80% of cloud environments run Redis, and nearly 85% of those instances are configured without a password — substantially widening the real-world attack surface beyond what the CVSS score alone suggests.

### Who needs to act?

The bug was introduced in Redis 7.2.0 and affects every stable release up through 7.2.13, 7.4.8, 8.2.5, 8.4.2, and 8.6.2. Fixed versions are 7.2.14, 7.4.9, 8.2.6, 8.4.3, and 8.6.3. Redis Cloud customers are already protected — patches were deployed automatically.

For self-managed deployments, upgrade immediately. If patching isn't immediately possible, restrictCONFIG,@scripting, and stream commands to roles that strictly need them — the full exploit requires all three in a single session.

As of publication, there is no evidence of active exploitation in the wild.

Copy

Post a Comment

### Post a Comment