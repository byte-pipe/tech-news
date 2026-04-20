---
title: Adobe fixes PDF zero-day security bug that hackers have exploited for months | TechCrunch
url: https://techcrunch.com/2026/04/14/adobe-fixes-pdf-zero-day-security-bug-that-hackers-have-exploited-for-months/
date: 2026-04-14
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:01:02.539140
---

# Adobe fixes PDF zero-day security bug that hackers have exploited for months | TechCrunch

# Adobe fixes PDF zero‑day security bug that hackers have exploited for months

## Vulnerability details
- Adobe patched CVE‑2026‑34621 affecting Acrobat DC, Reader DC and Acrobat 2024.
- The flaw lets attackers remotely install malware by convincing a user to open a crafted PDF on Windows or macOS.
- Exploitation targets a specific code path in certain Adobe Reader versions.

## Exploitation timeline
- The zero‑day has been active for at least four months before the fix.
- First malicious PDF samples appeared on VirusTotal in late November 2025.
- Adobe confirmed the bug is being used “in the wild” prior to the release of the patch.

## Impact and attribution
- Exact number of victims is unknown.
- The campaign’s sponsor has not been identified; both cyber‑criminal groups and state‑backed actors frequently target Adobe’s PDF software.
- Successful exploitation can give the attacker full control of the victim’s system and access to a wide range of data.

## Researcher findings
- Security researcher Haifei Li discovered the vulnerability via his EXPMON exploit‑detection system after a malicious PDF was submitted to his scanner.
- Li’s analysis indicates that opening the malicious PDF can lead to complete system compromise.
- No additional exploits were retrieved from the attacker’s servers.

## Adobe’s response and recommendations
- Adobe advises all users of the affected products to update to the latest versions immediately.
- The update addresses the remote code execution flaw and mitigates further exploitation.

## Article metadata
- Author: Zack Whittaker, Security Editor at TechCrunch.
- Contact: zackwhittaker.1337 on Signal; email zack.whittaker@techcrunch.com.
