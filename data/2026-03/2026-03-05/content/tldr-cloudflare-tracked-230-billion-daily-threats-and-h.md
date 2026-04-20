---
title: Cloudflare tracked 230 billion daily threats and here is what it found - Help Net Security
url: https://www.helpnetsecurity.com/2026/03/03/cloudflare-cyber-threat-report-2026/
site_name: tldr
content_file: tldr-cloudflare-tracked-230-billion-daily-threats-and-h
fetched_at: '2026-03-05T19:30:48.878473'
original_url: https://www.helpnetsecurity.com/2026/03/03/cloudflare-cyber-threat-report-2026/
author: Anamarija Pogorelec
date: '2026-03-05'
published_date: '2026-03-03T15:42:21+00:00'
description: The 2026 cyber threat report reveals attackers using stolen session tokens, AI tools, and cloud platforms to breach organizations fast.
tags:
- tldr
---

Anamarija Pogorelec
, Managing Editor, Help Net Security


March 3, 2026


Share


# Cloudflare tracked 230 billion daily threats and here is what it found

Cloudflare’s network blocks over 230 billion threats per day. The volume indicates how routine andautomatedthe attack cycle has become, and the patterns behind that volume point to a shift in how breaches begin and progress.

Cloudflare’s threat research unit, Cloudforce One, published its inaugural cyber threat report 2026, covering activity observed through 2025 and projecting into the year ahead. The report draws on telemetry from Cloudflare’s network, which handles roughly 20% of global web traffic.

“Threat actors are constantly changing tactics, finding new vulnerabilities to exploit and ways to overwhelm their victims. To avoid being caught off guard, organizations must shift from a reactive posture to one fueled by real-time, actionable intelligence,” saidBlake Darché, head of threat intelligence, Cloudforce One at Cloudflare.

### Stolen sessions are replacing credential guessing

Infostealers such asLummaC2extract live session tokens from infected machines rather than stored passwords. Those tokens give attackers access to already-authenticated sessions, bypassingMFAentirely. According to the report, 54% of ransomware attacks in 2025 traced back to infostealer-enabled credential theft, citingVerizon’s 2025 Data Breach Investigations Report.

Cloudforce One participated in a coordinated global operation in May 2025 to disrupt LummaC2 infrastructure, deploying warning pages across malicious command-and-control domains. The unit is already tracking successor variants expected to automate the time between infection and ransomware deployment down to hours.

Bots account for 94% of all login attempts observed on Cloudflare’s network. Of human login attempts, 46% involve credentials that have already been compromised in prior breaches. These figures reflect the scale at which automated credential testing operates across the web.

### Cloud platforms are being used as attack infrastructure

Threat actors across multiple nation-state categories are routing malicious activity through legitimate cloud services including AWS, Google Cloud, Azure, and SaaS platforms like Google Calendar and Dropbox. This approach blends attack traffic with normal enterprise usage, making detection harder for network security teams.

Cloudforce One tracks this tactic under the label “Living off the XaaS,” or LotX. Chinese-affiliated groups identified in the report use Google Calendar event descriptions to pass encrypted commands to infected hosts, and exploit F5 and VMware infrastructure for long-term persistence. Iranian-linked groups host command-and-control pages on Azure Web Apps.

Salt TyphoonandLinen Typhoon, both linked to China, continued targeting North American telecommunications providers, government networks, and IT services through 2025. The report attributes breaches at AT&T, Verizon, and Lumen to this activity, along with a July 2025Microsoft SharePoint compromise. The targeting pattern indicates a focus on persistent access to critical infrastructure for potential future disruption.

### Email authentication gaps are enabling phishing at scale

An analysis of 450 million emails found that 43% failed SPF checks, over 44% lacked valid DKIM signatures, and 46% failedDMARC. These gaps allow Phishing-as-a-Service bots to exploit incomplete authentication chains and deliver spoofed messages that appear to come from trusted internal or branded sources.

The top impersonated brands in phishing campaigns were Windows, SANS, Microsoft, Stripe, and Facebook. Researchers also intercepted over $123 million in BEC financial theft attempts in 2025. The average attempt sat at approximately $49,225, a figure the report attributes to deliberate calibration by fraudsters targeting amounts below executive approval thresholds.

### DDoS volumes reached new records in 2025

The total number ofDDoS attacksobserved by Cloudflare more than doubled in 2025 to 47.1 million. Network-layer attacks more than tripled year over year. Cloudforce One recorded 19 new world-record attacks during the year. The largest, a 31.4 Tbps UDP flood launched by the Aisuru botnet in November 2025, was nearly six times the peak volume of the largest attack recorded in 2024.

Most attacks in 2025 lasted under 10 minutes, closing the practical window for human-led mitigation. The Aisuru botnet and its successor Kimwolf collectively control an estimated one to four million infected hosts. The report notes that Kimwolf saw over 550 command-and-control nodes null-routed in early 2026.

### North Korean operatives are embedding in remote workforces

State-sponsored operatives linked to North Korea areobtaining employmentat Western organizations using AI-generated deepfake profiles and U.S.-based laptop farms that create the appearance of domestic residency. Once hired, these workers funnel salary revenue back to the regime and can introduce malicious access to internal systems. The report identifies detection indicators including impossible travel login alerts, mouse-jiggling software, and video metadata artifacts consistent with real-time deepfake rendering.

Manufacturingandcritical infrastructureaccounted for over 50% of ransomware-targeted attacks in 2025, driven by the high cost of operational downtime in those sectors.

Secure by Design:Building security in at the beginning

More about

* attacks
* CISO
* Cloudflare
* cyber risk
* cybercrime
* cybersecurity
* report
* threats

Share
