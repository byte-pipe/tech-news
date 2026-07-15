---
title: Microsoft Patches a Record 570 Security Flaws – Krebs on Security
url: https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/
date: 2026-07-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:38:11.647321
---

# Microsoft Patches a Record 570 Security Flaws – Krebs on Security

# Microsoft Patches a Record 570 Security Flaws – Krebs on Security

## Overview
- Microsoft released updates fixing at least 570 security flaws across Windows and other software, nearly three times the number patched in the previous record‑smashing Patch Tuesday.  
- The surge is attributed to vulnerability discoveries aided by artificial intelligence.

## Severity and Notable Vulnerabilities
- Approximately 60 of the patched bugs received a “critical” severity rating, allowing remote control of a Windows device with little or no user interaction.  
- Three zero‑day flaws were addressed; two are already being exploited in the wild.  
- Elevation‑of‑privilege issues: about 250 fixes, including  
  - CVE‑2026‑56155 – Active Directory Federation Services bug  
  - CVE‑2026‑56164 – Microsoft SharePoint vulnerability  
- CVE‑2026‑50661 – a security‑feature bypass in Windows BitLocker that could expose encrypted data if the attacker has physical access; publicly disclosed but not known to be actively exploited.  
- CVE‑2026‑48561 – remote code execution flaw in Microsoft Copilot (CVSS 9.6); exploitable via a malicious website that forces Edge for Android to send crafted prompts to Copilot.

## AI’s Impact on Vulnerability Management
- Microsoft EVP Pavan Davuluri explained that AI enables faster, broader discovery and analysis, resulting in a higher volume of updates per release.  
- Concerns about Microsoft’s “exploitability index” being outpaced by AI tools:  
  - Satnam Narang (Tenable) noted AI models can generate proof‑of‑concept exploits for vulnerabilities rated “Exploitation Less Likely,” suggesting the index needs to adapt to machine‑speed discovery.

## Industry Context
- Other major software makers are increasing their patch cadence:  
  - Adobe moving to twice‑monthly security bulletins, also citing AI acceleration.  
  - Cisco, Mozilla, and Oracle are shipping updates more frequently.  
  - Google’s June 2026 patch batch contained over 900 security fixes.

## Recommendations for Users
- Back up Windows systems and data before applying the updates.  
- Given the large number of patches, it may be prudent to wait a few days before installing them, as extensive updates can sometimes introduce stability issues.

## Further Reading
- Action1’s Patch Tuesday blog  
- Automox’s rundown