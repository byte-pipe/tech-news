---
title: Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products
url: https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html
site_name: tldr
content_file: tldr-critical-atlassian-flaw-lets-unauthenticated-attac
fetched_at: '2026-10-06T22:54:14.343734'
original_url: https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html
author: The Hacker News
date: '2026-10-06'
description: Atlassian fixes a critical path traversal in 8 Data Center products that lets unauthenticated attackers read files if exact paths are known.
tags:
- tldr
---

# Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products


Swati Khandelwal

Oct 06, 2026
Vulnerability / Web Security

A critical flaw in 8 Atlassian Data Center products, which customers host themselves, allows an attacker with no login access to read specific files in each product's web application root directory.

The attacker must already know a file's exact name and path and cannot list what the directory holds. Atlassiandisclosed the flaw,CVE-2026-21589, on October 5, rated it 9.3 out of 10, and listed a fixed version for each product.

The web application root directory is the folder on the server that holds the web application itself. In some configurations, it may contain sensitive files, which raises the risk, according to Atlassian.

Atlassian's cloud products affected by the flaw have already been patched, and cloud customers do not need to take any action.

Atlassian advises customers who cannot upgrade all at once to take the instance offline if possible. Any instance reachable from the public internet, including one that requires a login, should be restricted from outside network access until it is upgraded or a temporary blocking rule is in place.

### Affected Products and Fixed Versions

The flaw affects all versions of the 8 products before the fixed versions listed below. That may include versions that have reached end of life, according to Atlassian, which recommends upgrading to a fixed long-term support (LTS) version or later.

Atlassian listed these fixed versions as of October 6:

 Product
 

 Fixed versions
 

 Bitbucket Data Center
 

 9.4.26, 10.2.8, 10.5.1
 

 Confluence Data Center
 

 9.2.26, 10.2.19
 

 Jira Software Data Center
 

 9.12.40, 10.3.26, 11.3.12
 

 Jira Service Management Data Center
 

 5.12.40, 10.3.26, 11.3.12
 

 Bamboo Data Center
 

 10.2.24, 12.1.12
 

 Crowd Data Center
 

 6.3.7, 7.0.3, 7.1.7, 7.2.4
 

 Crucible
 

 4.9.15
 

 Fisheye
 

 4.9.15
 

For Crowd's 7.1 branch, the ticket's fix version field said 7.1.7. A table in the same ticket showed 7.1.6, which the ticket also listed as an affected version.

TheCVE recordAtlassian filed gave different numbers for 2 products. For Crowd, it listed 7.1.1, which theCrowd 7.1 release notesdate to November 27, 2025, more than 10 months before the flaw was disclosed. For Bamboo, one field said 10.2.4, while the record's own description said 10.2.24.

The CVE record also listed the Server editions of these products, Atlassian's older self-hosted line, which the advisory did not mention. It marked every version of Bamboo Server, Bitbucket Server, Confluence Server, and Crowd Server as affected and listed no fixed versions for them.

For Jira Software Server, the record listed versions from 9.12.40 as unaffected, for Jira Service Management Server from 5.12.40, and for Crucible Server and Fisheye Server from 4.9.15. It did not say whether Server licenses can run those versions.

Crowd has had no Server release since version 5.2 in September 2023, according to Atlassian'sCrowd release notes, so none of the fixed Crowd versions are Server releases.

### If You Cannot Upgrade Yet

Atlassian labels the flaw a path traversal in the CVE record. In a path traversal, a request uses a specially built file path to reach files it should not.

Atlassian describes 3 temporary blocking rules, which it calls mitigations. All 3 block requests whose URL contains .. directly next to /, \ or ::, including URL-encoded forms.

Which ones apply depends on the product:

* All 8 products:a rule on a web application firewall (WAF) or reverse proxy that blocks matching URLs.
* Confluence, Jira Software, Jira Service Management, Bamboo and Crowd:a Tomcat RewriteValve rule, installed on each node, which must be shut down and restarted.
* Bitbucket:a rule in urlrewrite.xml, applied to every node, mirror and mirror farm node, followed by a restart.

Crucible and Fisheye have only the first option. Theadvisorygives the rule and the file changes for each one.

The mitigations "are limited and not a replacement for patching your instance," Atlassian says in its product tickets.

### Checking for Past Access

Atlassian said its affected cloud products have been patched and that its investigation has not found evidence of exploitation. Bitbucket Cloud is not affected.

The advisory does not say whether attacks on self-hosted instances have been seen. "Atlassian cannot confirm if your instances have been affected by this vulnerability," it says.

It tells customers to have their security teams search access logs. One method is to URL-decode each request line, up to 2 times, and look for .. directly next to /, \ or ::. The other is to run Atlassian's block pattern over the raw log lines.

The advisory does not explain how to distinguish a failed attempt from a request that returned a file, or what else a customer who encounters such requests should do after upgrading.

Attackers have exploited this kind of flaw in an Atlassian product before.CVE-2021-26086is a path traversal vulnerability in Jira Server and Data Center that allows remote attackers to read specific files. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added it to its catalog of known exploited vulnerabilities on November 12, 2024.

### How Atlassian Scored the Flaw

The 9.3 rating uses version 4.0 of the Common Vulnerability Scoring System (CVSS) and is Atlassian's own. The company tells customers to judge how it applies to their environment.

The score rates the flaw as reachable over the network without privileges or user action. It rates the effect on the vulnerable system's confidentiality as high, its integrity and availability as none, and on other systems as high.

The advisory does not identify the sensitive files or the configurations that contain them, nor does it explain the high rating for other systems.

Found this article interesting? Follow us on 
Google News
, 
Twitter
 and 
LinkedIn
 to read more exclusive content we post.

SHARE










Tweet


Share


Share


Share

SHARE 


Atlassian
, 
Vulnerability
, 
Web Security

⚡ Top Stories This Week

⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats

Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent

RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims

Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks

OpenAI Shelves GPT-6.1 Astra After Tests Find Deception and Unauthorized Actions

Dutch Police Arrest 24-Year-Old Amsterdam Man in ShinyHunters Investigation

New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses

French Tax Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks

Citrix NetScaler CVE-2026-88772 Exploit Details Show Pre-Auth Path to Shellcode Execution

OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted

Cisco Warns of Attackers Exploiting Critical Authentication Bypass in SD-WAN Manager

Attackers Exploit Zimbra Flaw to Deploy Web Shells and Harvest Authentication Secrets

Citrix NetScaler Post-Exploitation Payload Creates Superuser, Maps Web Shell to CSS-Like URLs

Bitget Confirms Third-Party Zero-Day Behind $387.5 Million Cryptocurrency Theft

Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path

WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory

ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories

Police Arrest 16-Year-Old Suspected of Running KillSec, Seize Ransomware Leak Site and Servers

Critical FortiMail Zero-Day Flaw Exploited in Attacks Allows Unauthenticated Arbitrary File Writes

Dell CSM Flaws Enable Unauthenticated Admin Access and Root on Kubernetes Nodes

GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers

ShinyHunters Suspect Rey Reportedly Detained in Jordan, Helping FBI Identify Group Members

How Financial Services Companies Can Modernize Their Software Supply Chain

US-Focused CSuite Phishing Steals Microsoft 365 Sessions and Deploys RMM Tools for Remote Access

Zero Trust for AI Agents Starts With Fixing Zero Visibility

⭐ Featured Resources

Discover Hidden AI Agents and Lock Down Their Access — Get a Demo

The CISO Playbook for Board-Ready Security Reporting

The Browser Attacks Your Security Stack Is Missing

41 Cybersecurity Courses. One Week to Level Up Your Skills