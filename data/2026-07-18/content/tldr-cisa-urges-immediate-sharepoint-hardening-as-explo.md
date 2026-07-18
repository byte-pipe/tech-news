---
title: CISA urges immediate SharePoint hardening as exploits mount – Computerworld
url: https://www.computerworld.com/article/4197818/cisa-urges-immediate-sharepoint-hardening-as-exploits-mount-2.html
site_name: tldr
content_file: tldr-cisa-urges-immediate-sharepoint-hardening-as-explo
fetched_at: '2026-07-18T19:27:32.054270'
original_url: https://www.computerworld.com/article/4197818/cisa-urges-immediate-sharepoint-hardening-as-exploits-mount-2.html
date: '2026-07-18'
description: Three actively exploited SharePoint vulnerabilities have landed in the KEV catalog, with security experts warning that patching alone won’t prevent business disruption.
tags:
- tldr
---

by									
Shweta Sharma

Senior Writer

# CISA urges immediate SharePoint hardening as exploits mount

news

Jul 16, 2026
4 mins

The US Cybersecurity and Infrastructure Security Agency (CISA) has urged organizations to immediately secure Microsoft SharePoint deployments after warning that three vulnerabilities affecting the on-premises collaboration platform are being actively exploited.

A recentadvisoryfrom the federal cybersecurity watchdog asked administrators to patch vulnerable servers, review Microsoft’s mitigation guidance, and assume that internet-facing SharePoint instances remain attractive targets for attackers seeking an initial foothold into enterprise environments.

While applying patches remains the immediate priority, security experts caution that organizations should view the advisory as more than anotherPatch Tuesdayexercise.

“This is what separates an IT incident from a business crisis,” saidChris Boehm, field CTO at Zero Networks. “One compromised SharePoint box is a ticket. That same box, with a clear path to your domain controllers, backups, and file shares, is how you end up with an encrypted infrastructure and a disclosure event. Segmentation stops the first from becoming the second.”

CISA’s advisory highlightsCVE-2026-332201,CVE-2026-45659, and the newly addedCVE-2026-56164, all of which have now been confirmed as exploited in the wild and added to the agency’s Known Exploited Vulnerabilities (KEV) catalog.

## Exploitation tells a different severity story

The latest addition to CISA’s KEV catalog is CVE-2026-56164, an elevation-of-privilege vulnerability affecting Microsoft SharePoint Server. Although assigned a CVSS score of 5.3, the flaw can be exploited remotely without authentication, making it significantly more dangerous in practice than its severity rating alone suggests.

Microsoft has released security updates for supported SharePoint versions and recommended enabling the Antimalware Scan Interface (AMSI) integration to help detect malicious requests associated with exploitation attempts.

CISA also advised organizations to follow Microsoft’s incident responseguidance, hunt for indicators of compromise, and rotate SharePoint machine keys where appropriate, acknowledging that patching alone may not fully remove attacker persistence from already compromised servers.

## Older vulnerabilities remain active entry points

Alongside the newly disclosed flaw, CISA reiterated the urgency of addressing CVE-2026-45659, an insecure deserialization vulnerability allowing RCE that Microsoft had marked as “exploitation less likely” in itsadvisoryin May. Another old bug CISA flagged is CVE-2026-32201, an improper input validation flaw that allows spoofing over a network.

Both of these flaws are being actively exploited in the wild.

CISA called out organizations failing to catch up with SharePoint updates, adding that attackers are increasingly targeting N-days rather than relying exclusively on newly discovered zero-days.

On concerns of patching speed, Boehm noted resilience is becoming an architectural challenge as much as an operational one.

“Stop measuring this in patch speed,” he said. “That’s a race you eventually lose. Some of these landed as zero-days with no fix on day one, and the window between disclosure and exploitation keeps shrinking. So the board-level question isn’t whether a server gets compromised. Assume one will. It’s how much of the business a single-owned system can take down with it.”

Boehm argued that limiting network reachability through segmentation should sit alongside patch management and threat hunting as a core defensive strategy. Reachability, he said, is a control that organizations own, not patch timing. CISA has given Federal Civilian Executive Branch (FCEB) agencies three days to remediate CVE-2026-56164 under Binding Operational Directive (BOD)22-01.

The article originally appeared onCSO.

Collaboration Software
Productivity Software
Security
 

 

														by 															

																Shweta Sharma															

Senior Writer

1. Follow Shweta Sharma on X
2. Follow Shweta Sharma on LinkedIn

Shweta has been writing about enterprise technology since 2017, most recently reporting on cybersecurity for CSO online. She breaks down complex topics from ransomware to zero trust architecture for both experts and everyday readers. She has a postgraduate diploma in journalism from the Asian College of Journalism, and enjoys reading fiction, watching movies, and experimenting with new recipes when she’s not busy decoding cyber threats.

## More from this author

* news### Chrome encryption bypass discovered: New malware steals passwords and cookiesMar 23, 20263 mins
* news### Leaky Chrome extensions with 37M installs caught divulging your browsing historyFeb 16, 20263 mins
* news### Four new reasons why Windows LNK files cannot be trustedFeb 13, 20264 mins
* news### Newly discovered malicious extensions could be lurking in enterprise browsersDec 2, 20254 mins
* news### Microsoft fixes the fixes that broke Windows toolsAug 20, 20251 min
* news### Some Brother printers have a remote code execution vulnerability, and they can’t fix itJun 27, 20251 min
* news### Chrome extension privacy promises undone by hardcoded secrets, leaky HTTPJun 9, 20251 min
* news### If you use OneDrive to upload files to ChatGPT or Zoom, don’tMay 28, 20251 min
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### OpenAI’s new hardware is a $230, 13-switch keyboard for Codex

 
By Maxwell Cooter
Jul 17, 2026
2 mins

Developer
Input Devices
Keyboards

analysis
 
 

### July's Patch Tuesday sees an end-of-support collision amidst a massive, record-setting patch wave

 
By Greg Lambert
Jul 17, 2026
18 mins

Application Security
Microsoft
Windows

news
 
 

### Google must open Android to rival AI agents, EU orders

 
By Maxwell Cooter
Jul 17, 2026
2 mins

Android
Android Security
Mobile Security

podcast
 
 

### Microsoft Copilot Growth, ClaudeBleed Risk, LinkedIn GDPR Complaint | Ep. 84

 
By Arnold Davick
May 22, 2026
2 mins

Artificial Intelligence

podcast
 
 

### Chrome Gemini, AI Agents, CISA Infrastructure Cyber Resilience | Ep. 83

 
By Arnold Davick
May 22, 2026
2 mins

Artificial Intelligence

podcast
 
 

### AI Triage Gains, Model Reviews, Ask Jeeves Shutdown | Ep. 82

 
By Arnold Davick
May 18, 2026
2 mins

Artificial Intelligence

video
 
 

### Why AI agents fail when enterprises don't define the job

 
Jul 14, 2026
33 mins

Artificial Intelligence
Generative AI
IT Governance

video
 
 

### Why enterprise AI projects stall before delivering real value

 
Jul 7, 2026
29 mins

Artificial Intelligence
Generative AI
ROI and Metrics

video
 
 

### How AI is breaking job interviews, skills testing and evaluation

 
Jun 30, 2026
32 mins

Generative AI
Hiring
IT Skills and Training