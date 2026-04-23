---
title: Over 1,300 Microsoft SharePoint servers vulnerable to spoofing attacks
url: https://www.bleepingcomputer.com/news/security/over-1-300-microsoft-sharepoint-servers-vulnerable-to-ongoing-attacks
date: 2026-04-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:01:53.148402
---

# Over 1,300 Microsoft SharePoint servers vulnerable to spoofing attacks

# Over 1,300 Microsoft SharePoint servers vulnerable to spoofing attacks

## Key Points
- More than 1,300 publicly‑exposed SharePoint servers remain unpatched for CVE‑2026‑32201, a spoofing vulnerability first disclosed as a zero‑day.
- The flaw affects SharePoint Enterprise Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition (the on‑premises version with continuous updates).
- Exploitation allows unauthenticated attackers to perform network spoofing, compromising confidentiality and integrity of data, though it does not affect availability.
- Microsoft released patches on the April 2026 Patch Tuesday; however, fewer than 200 of the vulnerable servers have been updated since the release.

## Impact and Threat Landscape
- Shadowserver reported the large pool of unpatched servers and warned that the vulnerability is actively being abused.
- CISA added CVE‑2026‑32201 to its Known Exploited Vulnerabilities (KEV) Catalog and issued a Binding Operational Directive (BOD 22‑01) requiring Federal Civilian Executive Branch agencies to apply patches by 28 April 2026.
- The agency highlighted the vulnerability as a common attack vector for malicious actors and advised mitigation per vendor guidance or discontinuation of the product if mitigations are unavailable.

## Related Security Activity
- The same week Microsoft issued patches for 167 vulnerabilities, including two zero‑day flaws.
- Earlier, CISA warned about a separate Windows Task Host privilege‑escalation zero‑day being exploited in the wild.
- Additional related reports include active exploitation of Apache ActiveMQ, F5 BIG‑IP APM, Roundcube, and a critical Microsoft SharePoint flaw.