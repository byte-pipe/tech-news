---
title: CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day
url: https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/
date: 2026-06-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-15T06:01:23.431579
---

# CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

# CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day

## Vulnerability details
- CVE‑2026‑50751 affects Check Point Remote Access VPN, Mobile Access, and Spark firewalls.
- Exploits unauthenticated remote attackers to bypass authentication and gain VPN access.
- Only impacts deployments using the deprecated IKEv1 key exchange, without mandatory machine certificates, and that accept legacy Remote Access clients.

## Exploitation and impact
- First seen in attacks on May 7, with a surge over the weekend of May 2026.
- Linked to Qilin ransomware‑as‑a‑service affiliates; at least one breach confirmed.
- Exploitation has been limited to a few dozen organizations worldwide, but Qilin claims over 400 victims since August 2022.

## Mitigation and patching by Check Point
- Security updates released on Monday to fix the flaw.
- Recommended mitigations for unpatched systems:
  - Remove support for the legacy remote access client.
  - Configure Remote Access VPN authentication to IKEv2 only.
  - Enable IPS and download the latest signatures.
  - Make machine‑certificate authentication mandatory.

## CISA directive
- Added CVE‑2026‑50751 to the Known Exploited Vulnerabilities (KEV) Catalog.
- Federal Civilian Executive Branch agencies must apply patches or mitigations by **June 11** (three days from the announcement) under Binding Operational Directive 22‑01.
- Agencies may also discontinue use of the product if mitigations are unavailable.
- CISA urges private‑sector security teams to deploy the patch promptly.

## Context and related incidents
- Two years earlier, CISA flagged CVE‑2024‑24919 in Check Point Quantum Security Gateways as actively exploited by NailaoLocker ransomware.
- Recent CISA actions include orders to patch actively exploited Ivanti flaws and a new SD‑WAN vulnerability.