---
title: LangChain, LangGraph Flaws Expose Files, Secrets, Databases in Widely Used AI Frameworks
url: https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html
site_name: tldr
content_file: tldr-langchain-langgraph-flaws-expose-files-secrets-dat
fetched_at: '2026-03-30T19:26:31.591734'
original_url: https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html
author: The Hacker News
date: '2026-03-30'
description: Three LangChain flaws enable data theft across LLM apps, affecting millions of deployments, exposing secrets and files.
tags:
- tldr
---

# LangChain, LangGraph Flaws Expose Files, Secrets, Databases in Widely Used AI Frameworks


Ravie Lakshmanan

Mar 27, 2026
Vulnerability / Artificial Intelligence

Cybersecurity researchers have disclosed three security vulnerabilities impacting LangChain and LangGraph that, if successfully exploited, could expose filesystem data, environment secrets, and conversation history.

Both LangChain and LangGraph are open-source frameworks that are used to build applications powered by Large Language Models (LLMs). LangGraph is built on the foundations of LangChain for more sophisticated and non-linear agentic workflows. According to statistics on the Python Package Index (PyPI), LangChain, LangChain-Core, and LangGraph have been downloaded more than52 million,23 million, and9 million timeslast week alone.

"Each vulnerability exposes a different class of enterprise data: filesystem files, environment secrets, and conversation history," Cyera security researcher Vladimir Tokarevsaidin a report published Thursday.

The issues, in a nutshell, offer three independent paths that an attacker can leverage to drain sensitive data from any enterprise LangChain deployment. Details of the vulnerabilities are as follows -

* CVE-2026-34070(CVSS score: 7.5) - A path traversal vulnerability in LangChain ("langchain_core/prompts/loading.py") that allows access to arbitrary files without any validation via its prompt-loading API by supplying a specially craftedprompt template.
* CVE-2025-68664(CVSS score: 9.3) - A deserialization of untrusted data vulnerability in LangChain that leaks API keys and environment secrets by passing as input a data structure that tricks the application into interpreting it as an already serialized LangChain object rather than regular user data.
* CVE-2025-67644(CVSS score: 7.3) - An SQL injection vulnerability in LangGraph SQLite checkpoint implementation that allows an attacker to manipulate SQL queries through metadata filter keys and run arbitrary SQL queries against the database.

Successful exploitation of the aforementioned flaws could allow an attacker to read sensitive files like Docker configurations, siphon sensitive secrets via prompt injection, and access conversation histories associated with sensitive workflows. It's worth noting that details of CVE-2025-68664 were also shared by Cyata in December 2025, giving it the cryptonymLangGrinch.

The vulnerabilities have been patched in the following versions -

* CVE-2026-34070 - langchain-core >=1.2.22
* CVE-2025-68664 - langchain-core 0.3.81 and 1.2.5
* CVE-2025-67644 - langgraph-checkpoint-sqlite 3.0.1

The findings once again underscore how artificial intelligence (AI) plumbing is not immune to classic security vulnerabilities, potentially putting entire systems at risk.

The development comes days after a critical security flaw impacting Langflow (CVE-2026-33017, CVSS score: 9.3) hascome under active exploitationwithin 20 hours of public disclosure, enabling attackers to exfiltrate sensitive data from developer environments.

Naveen Sunkavally, chief architect at Horizon3.ai, said the vulnerability shares the same root cause asCVE-2025-3248, and stems from unauthenticated endpoints executing arbitrary code. With threat actors moving quickly to exploit newly disclosed flaws, it's essential that users apply the patches as soon as possible for optimal protection.

"LangChain doesn't exist in isolation. It sits at the center of a massive dependency web that stretches across the AI stack. Hundreds of libraries wrap LangChain, extend it, or depend on it," Cyera said. "When a vulnerability exists in LangChain’s core, it doesn’t just affect direct users. It ripples outward through every downstream library, every wrapper, every integration that inherits the vulnerable code path."

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

Application Security
, 
artificial intelligence
, 
Cloud security
, 
cybersecurity
, 
Open Source
, 
sql injection
, 
Threat Intelligence
, 
Vulnerability

Trending News

Citrix NetScaler Under Active Recon for CVE-2026-3055 (CVSS 9.3) Memory Overread Bug

CISA Adds CVE-2025-53521 to KEV After Active F5 BIG-IP APM Exploitation

TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files

China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks

ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits and 20 More Stories

Coruna iOS Kit Reuses 2023 Triangulation Exploit Code in Recent Mass Attacks

FCC Bans New Foreign-Made Routers Over Supply Chain and Cyber Risk Concerns

Citrix Urges Patching Critical NetScaler Flaw Allowing Unauthenticated Data Leaks

TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 via Trivy CI/CD Compromise

FBI Warns Russian Hackers Target Signal, WhatsApp in Mass Phishing Attacks

Trivy Security Scanner GitHub Actions Breached, 75 Tags Hijacked to Steal CI/CD Secrets

Google Adds 24-Hour Wait for Unverified App Sideloading to Reduce Malware and Scams

Apple Warns Older iPhones Vulnerable to Coruna, DarkSword Exploit Kit Attacks

54 EDR Killers Use BYOVD to Exploit 35 Signed Vulnerable Drivers and Disable Security

New Perseus Android Banking Malware Monitors Notes Apps to Extract Sensitive Data

⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers and More

Popular Resources

Detect AI-Driven Threats Faster With Full Network Visibility

[Demo] Discover SaaS Risks and Monitor Every App in Your Environment

[Guide] Learn How to Govern AI Agents With Proven Market Guidance

SANS SEC401: Get Hands On Skills to Detect and Respond to Cyber Threats