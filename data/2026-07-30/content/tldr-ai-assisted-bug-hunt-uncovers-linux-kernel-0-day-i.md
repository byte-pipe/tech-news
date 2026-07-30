---
title: AI-Assisted Bug Hunt Uncovers Linux Kernel 0-Day in net/sched - Infosecurity Magazine
url: https://www.infosecurity-magazine.com/news/ai-linux-kernel-zero-day-net-sched/
site_name: tldr
content_file: tldr-ai-assisted-bug-hunt-uncovers-linux-kernel-0-day-i
fetched_at: '2026-07-30T19:33:57.750341'
original_url: https://www.infosecurity-magazine.com/news/ai-linux-kernel-zero-day-net-sched/
author: Alessandro Mascellino
date: '2026-07-30'
published_date: '2026-07-28T14:45:00'
description: AI-assisted research uncovered Linux kernel use-after-free allowing root escalation
tags:
- tldr
---

# AI-Assisted Bug Hunt Uncovers Linux Kernel 0-Day in net/sched

News

28 July 2026

## Written by

### Alessandro Mascellino

News Reporter

* Email Alessandro
* Follow @a_mascellino

A years-old Linux kernel flaw allowing local privilege escalation to root has been disclosed after AI-assisted research uncovered a race condition in net/sched.

Innew researchpublished July 27, Lee Jia Jie of Singapore offensive security firm STAR Labs said he found the use-after-free during an internship, his first Linux kernel work.

It is tracked as CVE-2026-53264.

## Race Condition Exposes Freed Kernel Object

Net/sched controls when and how network packets are transmitted. The flaw stems from mismatched locking around a shared data structure: one function reads entries under a Read-Copy-Update (RCU) lock, while another path can free an entry without waiting for the RCU grace period.

That gap creates a race window in which the kernel may continue using an object after its memory has been released. Successful abuse could give a local unprivileged user root access, but requires unprivileged user namespaces and two supporting kernel options. Testing targeted a CentOS Stream 9 desktop.

Read more on Linux kernel flaws: CrackArmor Flaws Expose Linux Systems to Privilege Escalation

Jia Jie used AI to identify the bug, produce a crash proof and improve the reliability of triggering the race. Separately, optimization reduced the time required to hit the condition from more than 15 minutes to about five seconds.

The result follows previousGoogle OSS-Fuzzwork using AI to expose hidden flaws in open-source projects.

## Competition Miss and Wider Kernel Findings

The exploit was prepared for TyphoonPwn 2026's Linux local privilege escalation category, which offered prizes of $70,000, $35,000 and $17,500. Jia Jie drew position eight of 11, but the category closed after three winners, so his entry was never demonstrated.

KyleBot, an AI system, had independently reported the same bug two days before TyphoonPwn 2026. Jia Jie said the defect had existed for two to three years, describing this as evidence that AI can make zero-day work resemble n-day analysis.

He also reported two exploitable flaws in the perf events subsystem. One was assigned CVE-2026-64300; the issues were reachable on Intel bare-metal systems under a permissive performance-monitoring setting, affecting RHEL-based and Arch systems rather than Debian-based distributions, and were mainly relevant to desktop Linux.

Jia Jie said AI accelerated bug hunting but still showed blind spots and reasoning failures. He concluded that detailed subsystem knowledge remains important for finding weaknesses automated systems miss.

CVE-2026-53264 has been patched upstream. The fix defers freeing the affected object until after the RCU grace period, removing the use-after-free window. Linux users and administrators should obtain fixed kernels through their distribution's security update channels.

## You may also like

1. ### Cloud Security Alliance Develops Assessment Spec for Third PartiesNews30 July 2014
2. ### Comment: May the (En)Force(ment) Be With You – Security Lessons from Star WarsOpinion19 October 2012
3. ### The cloud: transforming the role of the infosec professionalNews18 September 2012
4. ### Intruder alert: Star Trek Online account database compromisedNews30 April 2012
5. ### New CSA registry enables cloud providers to demonstrate security controlsNews8 August 2011

## What’s Hot on Infosecurity Magazine?

Read

Shared

Watched

Editor's Choice

### Just 1% of AI-Discovered Vulnerabilities Exploited in the Wild, Research Shows

News
29 July 2026
1

### Phishing Dominates as Initial Entry Method for Cyber-Attacks, as Hackers Hone Evasion Techniques

News
28 July 2026
2

### NCSC Publishes Guidance to Aid Incident Response and Recovery

News
29 July 2026
3

### Bugs in Hugging Face Diffusers Bypass Custom Code Safeguard

News
28 July 2026
4

### New CREST AI Standards to Deliver AI-Enabled Pentesting Accreditation

News
28 July 2026
5

### Ransomware Groups Increasingly Deploy EDR Kill Techniques

News
27 July 2026
6

### New CREST AI Standards to Deliver AI-Enabled Pentesting Accreditation

News
28 July 2026
1

### Hotel Wi-Fi Routers Compromised to Steal Corporate Login Credentials From Visitors

News
24 July 2026
2

### Same Front Door, New Visitors: Securing Humans and AI Agents at the Browser

Webinar
11:00 — 
12:00, 23 July 2026
3

### New Dolphin X Stealer Employs AI Profiling to Prioritize Targets

News
23 July 2026
4

### Human Risk in Cybersecurity: Protecting Your Organization Beyond Technology

Webinar
15:00 — 
16:00, 16 July 2026
5

### AI Agents Now the Enterprises Fastest Growing Exposed Attack Surface

News
23 July 2026
6

### Same Front Door, New Visitors: Securing Humans and AI Agents at the Browser

Webinar
11:00 — 
12:00, 23 July 2026
1

### Human Risk in Cybersecurity: Protecting Your Organization Beyond Technology

Webinar
15:00 — 
16:00, 16 July 2026
2

### How to Manage Enterprise Cyber Resilience in the Age of AI

Webinar
11:00 — 
12:00, 21 May 2026
3

### Financial Services Cyber Resilience: Stress Testing Third Parties Before Attackers Do

Webinar
15:00 — 
16:00, 30 April 2026
4

### Behind the Curtain of Microsoft 365 Cybersecurity: Lessons from Overlooked Resilience Gaps

Webinar
15:00 — 
16:00, 23 April 2026
5

### How to Harness Advanced Intelligence Capabilities to Strengthen Cyber Defence

Webinar
15:00 — 
16:00, 12 March 2026
6

### How Faster Cyber-Attacks Are Reshaping Enterprise Cybersecurity Strategies

News Feature
8 July 2026
1

### Researchers Claim First Fully Agentic Ransomware: JadePuffer

News
6 July 2026
2

### AI is Already Powering Cyber-Attacks. Can it Power Cyber Defense?

Opinion
3 July 2026
3

### Google Cloud's New CISO Chris Betz on Integrating AI in Cyber Defenses

Interview
7 July 2026
4

### How World Cup Password Trends Can Increase Active Directory Risk

Blog
23 June 2026
5

### New CISA Guide Helps Agencies Adopt SASE For Zero Trust

News
25 June 2026
6