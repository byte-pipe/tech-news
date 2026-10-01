---
title: 16-year-old researcher found a Microsoft bug, got admin access to databases with 17.3 trillion rows
url: https://www.theregister.com/security/2026/09/30/16-year-old-researcher-found-a-microsoft-bug-got-admin-access-to-databases-with-173-trillion-rows/5300240
site_name: tldr
content_file: tldr-16-year-old-researcher-found-a-microsoft-bug-got-a
fetched_at: '2026-10-01T17:18:21.374154'
original_url: https://www.theregister.com/security/2026/09/30/16-year-old-researcher-found-a-microsoft-bug-got-admin-access-to-databases-with-173-trillion-rows/5300240
date: '2026-10-01'
published_date: '2026-09-30T18:29:41.000Z'
description: It's 2 am. Do you know what your teen is doing?
tags:
- tldr
---

security

 

# 16-year-old researcher found a Microsoft bug, got admin access to databases with 17.3 trillion rows

It's 2 am. Do you know what your teen is doing?

Jessica Lyons

Jessica

Lyons

Cybersecurity Editor

Published

wed 30 Sep 2026 // 19:29 UTC

### READ MORE

* #### Microsoft catches hackers exploiting Zimbra bug before disclosure57 minutes ago
* #### Azure maintenance mess disrupted hybrid clouds, VPNs, cloudy VMware services15 hours ago
* #### Drunk Van Halen fan called Microsoft support and demanded to speak to Gates1 day ago
* #### Microsoft sends PDFs to strange new worlds instead of SharePoint1 day ago
* #### Redmond to millions of Power BI users: You’re Fabric app devs now2 days ago

A 16-year-old security researcher named Faav found an authentication flaw in Microsoft’s Titan analytics service that allowed him to gain administrator access, submit unauthorized SQL queries with no valid credentials, and potentially reach analytics databases containing an estimated 17.3 trillion stored rows.

Titan is an internal analytics platform, and Redmond restricts access via its web interface to Microsoft employees. Faav, with an assist from an AI hackbot he built called Antares, found that he could access Titan’s API through an Azure Cloud Services host because Titan didn’t check the signature on a login token.

Microsoft has since locked down the API and paid Faav a $5,000 bug bounty for his research. He says the breakthrough came after 10 days of authentication errors, when he returned to the problem after finishing Friday’s schoolwork and finally managed to execute SQL as a Titan admin after 1 AM Saturday.

REG AD

“It was 2 AM,” Faavsaidin a blog about his findings. “I wanted to yell, or at least say something out loud, but my parents were asleep. So I just sat there staring at 17,333,335,124,315 and checked the math again.”

REG AD

He also notes that he rewrote his blog post at Microsoft’s request, cut sections and numbers, and reworded the impact prior to publication.

“We appreciate the opportunity to investigate the findings reported by Faav,” Microsoft said in a statement provided to Faav for his blog. “Their submission and coordinated vulnerability disclosure helped us to better protect our customers by hardening our services. We value and appreciate safe security research under the terms of the Microsoft Bug Bounty Program and look forward to continuing to work with Faav in the future.”

### A boy and his bot

The research began on August 25 when Antares found Titan’s public API. For the next 10 days, the human and bot tested the service’s JSON Web Token (JWT) authentication checks and email-formatted user principal names (UPNs), eventually finding an unsigned token that could reach Titan’s local user lookup - but not a UPN that Titan recognized.

Early on September 5, Faav changed the unsigned token’s UPN from an email-formatted identity to admin. Titan recognized it as a local username, resolved it to local user ID 1, which held an admin role, and allowed him to run SQL. The takeaway, according to Faav:

Titan validated the contents of the JWT (tenant, audience, app ID, user) but never verified the signature, the most important part of any authentication check. The authentication checks felt like a hotel where every door had a working keycard reader, but any keycard unlocked any room. Despite all the access-control logic existing in the app, the one missing piece made it all pointless. If you’re a developer (or coding agent) reading this, the most important takeaway from this post is to make sure you verify signatures above all else when building auth.

This gave Faav access to Titan’s platform metadata database, and from there he could query application tables directly. The metadata contained:

* About 25,000 account and email records.
* 17,990 employee email records.
* 15,001 employee organization records.
* 355 database configurations.
* 20,979 virtual-dataset SQL definitions.
* 24,569 dashboards, 425,891 charts, and 27,347 dataset definitions.

REG AD

Titan’s user and usage directory exposed employee job titles, departments, and management hierarchy, which the researcher notes could be useful for social-engineering attacks - “though I never tested or demonstrated that,” he added.

He also found a Bing analytics sample and tested two rows that contained search info, identifiers, and high-level location information, such as country- or state-level details. Faav said the location values did not contain precise user locations.

### 17.3 trillion data rows

Then he hit the jackpot, testing 56 routing values from an archived configuration and discovering 30 were still active. “Each routing value pointed to a backend configuration, and each configuration contained one or more databases, so the 30 live values resolved through 24 configurations to 17 connected analytics databases spanning 9,863 unique table names,” the bug hunter wrote.

The total comes to about 17.3 trillion rows, which Faav says is a storage estimate derived from metadata and likely includes historical, duplicated, and derived data. “But quite the high number nonetheless.”

Between September 6 and September 8, Microsoft asked the teen to stop testing and requested his IP address to confirm no nefarious activity beyond the bug bounty research.

A day later, Redmond locked down the endpoint and told Faav the “report prompted immediate investigation and remediation to address the remaining exposure.” Microsoft awarded the bug hunter $5,000 for his work on September 17.®

microsoft

azure

security

bug bounty

REG AD

## Suspected Chinese spies spoofed an Anthropic exec, ex-White House official in AI phishing

Your invite to a fake AI policy advisory committee has strings attached

## AWS offers local, open source leash for agent harnesses

Dogwood Local Engine checks AI tool calls against user-defined temporal rules before they run

## Huawei Cloud Rolls Out Enterprise AI Products Across the Board, Building an Open Agentic Cloud

PARTNER CONTENT: Huawei Cloud strengthens the silicon bedrock on the cloud

## Build the right AI factory for your needs: partner for success

SPONSORED FEATURE: HPE and NVIDIA help organizations apply accelerated computing, software, enterprise infrastructure, networking, control plane, and services to the workloads and business outcomes that matter most.

## OpenAI apes AWS Marketplace while Anthropic remains stubbornly Microsoftian

By including Baseten in its marketplace, OpenAI signals it wants its models to win on the merits, not through coercion

## Microsoft catches hackers exploiting Zimbra bug before disclosure

Attackers were probing the mail server flaw weeks before it had a CVE to its name

### TOP STORIES

* #### AI models keep posting screenshots showing sensitive data from inside tech companies
* #### Astronomer watches Starlink satellites sinking to build a ‘planetary barometer’
* EXCLUSIVE#### Microsoft tells nonprofits their deleted M365 data isn't coming back
* #### Google ending ChromeOS support two years early
* #### FBI to ShinyHunters: 'We know how to find you'
* #### Microsoft's Copilot super app comes with a meter attached

### AI

* #### Hot Dog! America's new chatbot is packed with wienersJust ask America.gov and you'll receive a favorite July 4th food.
* #### Huawei boss claims homegrown AI chip sales top Nvidia in ChinaThe chips may not be as advanced, but they won't get banned at a moment's notice, Eric Xu says
* #### Add one more AI worry to the nightmare scenario: self-replicating prompt injectionsIt's a worm attack, AI-style
* #### Zuckerberg touts enterprise AI push because Meta would never do anything to damage your reputationNew business unit to be led by former MongoDB CEO 'CJ' Desai
* #### AMD's 192 GB Gorgon Halo prices might leave you petrifiedRegular pricing starts at $6,799 - all that memory doesn't come cheap

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### Firefox 157: Could bold new look be just what Mozilla needs?*Yet another new version of Firefox, with a significant reskin
* #### KDE turns 30 and someone's brought an AI-native desktop proposalAkademy talk imagines Plasma assembling itself around a personal model of each user
* #### Shopify extends lifeline to Tailwind as vibe coding erodes web dev platform's bottom lineAcquisition gives open source CSS framework 'a stable long-term home'
* #### Switzerland tests a FOSS escape route from Microsoft 365Swiss Army sticks a knife in American cloud apps with its own FOSS push
* #### Feel peak Windows was 7? You might like Kumander LinuxDebian and Xfce – solid, sensible choices – with a pretty skin
* #### Canonical shuttering some of its legacy chat channelsThe Ubuntu Pastebin went in June, IRC gets demoted next