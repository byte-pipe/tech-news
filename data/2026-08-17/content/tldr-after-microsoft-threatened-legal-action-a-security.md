---
title: After Microsoft threatened legal action, a security researcher publishes a new Windows zero-day bug | TechCrunch
url: https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/
site_name: tldr
content_file: tldr-after-microsoft-threatened-legal-action-a-security
fetched_at: '2026-08-17T11:22:21.042305'
original_url: https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/
author: Zack Whittaker
date: '2026-08-17'
published_date: '2026-08-12T15:18:55+00:00'
description: This is the latest zero-day released by security researcher Nightmare Eclipse, despite Microsoft publicly threatening to take legal action against them.
tags:
- tldr
---

A security researcher has published details of a new vulnerability in the latest versions of Windows that allows hackers to gain system-wide access to the user’s device and data, despite facing a legal threat from Microsoft weeks earlier over the release of previously unknown software flaws.

The new bug, dubbed ShieldBreak, is the latest disclosure by security researcher Nightmare Eclipse, who in recent months has published details ofseveral bugsaffecting Microsoft’s products, including Windows.

Accordingto Nightmare Eclipse’s post, ShieldBreak takes advantage of a flaw in Windows Defender, the anti-malware and security engine built into Windows. A successful attack allows the hacker to escalate their permissions from a low-level user to full access to the device and its data.

Nightmare Eclipse published the proof-of-concept exploit as a Windows app, requiring the user to run the app to exploit the bug. The bug works on Windows 10, Windows 11 (including the latest 25H2 version), and Windows Server 2025, the researcher said.

Security researcher Will Dormannverified that the bug worksand that Windows Defender must be enabled for the exploit to work.

The latest exploit builds on an earlier exploit that Nightmare Eclipse developed dubbed RoguePlanet, according to Nightmare Eclipse. Microsoft rolled out a patch forRoguePlanet, but the researcher implied that Microsoft’s fix was not sufficient and that their latest exploit demonstrates a full bypass of the earlier patch.

Microsoft has not yet released a patch for the ShieldBreak bug. The bug is considered a zero-day because the software maker — in this case, Microsoft — was given no time to patch the bug before it was publicly disclosed.

When reached for comment, an unnamed Microsoft spokesperson said the company is “aware of the reported vulnerability and is actively investigating the validity and potential applicability of these claims.”

The release of this new zero-day is thelatest in a long back-and-forthbetween the security researcher and the software giant over the company’s alleged handling of their bug reports.

In a series of blog posts, the security researcher claimed that Microsoft mistreated them and did not handle their bug reports sufficiently, with the implication that the researcher had no other choice but to publicly disclose the bugs online. Nightmare Eclipse previously released several other bugs in Windows that werelater exploited in real-world attacksto hack into organizations.

In May, Microsoft publisheda blog postthreatening to take legal action against security researchers, like Nightmare Eclipse, if they released details of zero-days outside of the company’s disclosure policies. The company faced heavy rebuke from the security community, many of whom described similar experiences with Microsoft’s handling of their bug reports. Microsoft later walked back the comments ina social media post. Its original blog post remains published and unchanged.

ShieldBreak lands a day after Microsoft’s regularly scheduled monthly security patch releases, dubbed Patch Tuesday. This is the second month in a row where the number of patches hasreached around 500 or so bugsdriven by the company’sgrowing use of AIto find and weed out security flaws.

Updated with comments from Microsoft.

Topics

cybersecurity
, 
Microsoft
, 
Security
, 
Windows
, 
zero-day
 

When you purchase through links in our articles,we may earn a small commission. This doesn’t affect our editorial independence.

			Zack Whittaker	

Security Editor

Zack Whittaker is the security editor at TechCrunch. He also authors the weekly cybersecurity newsletter,this week in security.

He can be reached via encrypted message at zackwhittaker.1337 on Signal. You can also contact him by email, or to verify outreach, atzack.whittaker@techcrunch.com.

 

View Bio