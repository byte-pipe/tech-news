---
title: Anthropic and OpenAI Models Still Attempt Restricted Actions in Safety Tests
url: https://thehackernews.com/2026/09/anthropic-and-openai-models-still.html
site_name: tldr
content_file: tldr-anthropic-and-openai-models-still-attempt-restrict
fetched_at: '2026-09-23T15:19:30.177984'
original_url: https://thehackernews.com/2026/09/anthropic-and-openai-models-still.html
author: The Hacker News
date: '2026-09-23'
description: Anthropic and OpenAI report fewer boundary circumvention and unauthorized actions in safety tests of their latest AI models.
tags:
- tldr
---

# Anthropic and OpenAI Models Still Attempt Restricted Actions in Safety Tests


Ravie Lakshmanan

Sep 23, 2026
Artificial Intelligence / Cybersecurity

Anthropic and OpenAI on Tuesday announced new models, with both artificial intelligence (AI) companies noting that they are continuing to invest in improving alignment to combat risky behavior.

Opus 5.5, perAnthropic, is a "major step up from Opus 5," and "achieves the best scores of any model to date on our automated behavioral audit, our alignment suite that tests Claude across thousands of simulated scenarios."

The AI company said the model is less likely than its other recent models to carry out hard-to-reverse actions or act outside the boundaries it's been given, adding it's more resistant than Opus 5 to prompt injection.

In its systems card, Anthropic explained that the latest model exhibited less misaligned behavior and less cooperation with misuse than any other recent Claude model.

"It also took overeager or destructive actions less than any other model we tested," Anthropic said. "Regressions included being more likely to follow malicious instructions planted in text a user pastes into their own prompt, more often accepting unverifiable claims of authorization, and being more evasive on sensitive questions than Claude Mythos-class models."

Anthropic highlighted that Claude Opus 5.5 attempted to escape or tamper with a sandbox in 1.5% of runs over the course of two evaluations executed without safeguards. It also pointed out that the model, when given apparent credentials to a public package registry in a simulated security exercise, took potentially harmful actions in roughly half of the cases.

"In a new evaluation designed to test a model’s propensity to cross containment boundaries, Opus 5.5 attempted to circumvent boundaries around 85% less often than Opus 5 or Claude Mythos 5.1, and every attempt it made was low severity and self-reported," it said.m

The company also noted that most cybersecurity tasks will be re-routed to Opus 4.8, given the "strong cyber capabilities" of Opus 5.5.

### OpenAI Debuts GPT‑6 Sol and Luna

The release of Opus 5.5 coincides with OpenAI's own expansion of the GPT‑6 universe with GPT‑6 Sol and GPT‑6 Luna, bringing theAstra'sstate-of-the-art performance and alignment to more affordable models.

"GPT‑6 Sol and Luna build on the alignment work introduced with Astra, our most aligned model to date," OpenAIsaid. "In our alignment evaluations, both Sol and Luna show improvements over their GPT‑5.6 counterparts, including lower rates of misleading claims about their coding work."

In tests carried out by the AI company, GPT‑6 Luna attempted to work around "access denied" restrictions in about 42% of runs, down from 77% for its predecessor. GPT‑6 Sol's rate was at 64%, compared with 68% for its predecessor.

OpenAI also said it evaluated its models to check whether they followed unauthorized instructions on a simulated message board. Among runs in which the models found the board, GPT‑6 Sol has been found to take the specified unauthorized action in 11% of cases, compared with 52% for GPT‑5.6 Sol. Neither GPT‑6 Luna nor Astra initiated such actions, the company added.

### OpenAI to Let Outside Groups Evaluate AI Models

Therecent spate of cybersecurity incidentswith AI models hasraisedsafety concernsand their ability to operate without human control, prompting Anthropic CEO Dario Amodei to call forpacing the progress of the technologyso as to prioritize responsible development and incorporate safeguards to prevent the tools from being misused.

Google has since launchedthe DeepMind Instituteto further the safe development of artificial general intelligence (AGI). Demis Hassabis, co-founder and chair of Google DeepMind, has proposed a U.S.-led frontier AI standards body to evaluate the most advanced AI models.

"Model assessments should include rigorous scientific evaluations of capabilities in cybersecurity, biological threats and other high-risk domains," Hassabissaid. "These evaluations would be regularly updated, perhaps quarterly to start, with outdated or saturated benchmarks being deprecated and replaced."

OpenAI, for its part, hasoutlined plansto let third-party groups scrutinize its AI models for safety risks during the process of training, evaluation, and deployment, at the same time ensuring "strong independence mechanisms, scientific rigor, robust security practices, and clear responsibilities."

The independent assessments are expected to cover safety cases (i.e., alignment), critical safeguards, capability evaluations, and misalignment incidents.

"We are committed to supporting independent assessors and establishing clearer, shared international standards – both through future laws and private governance institutions – for effective third party assessments," OpenAI said.

"While the independent evaluation ecosystem is still growing, we will help it grow by supporting and working with a diverse community of independent assessors with deep expertise across frontier safety questions. No one third party can or should comprehensively cover urgent frontier safety questions. We will move deliberately and with intention to grow our capacity and enable the growing third party ecosystem to align on the best practices and principles."

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

artificial intelligence
, 
cybersecurity
, 
Prompt Injection

⚡ Top Stories This Week

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws

Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up

OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads

Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root

New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution

Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root

ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories

Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks

Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers

Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories

Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation

KREMLIN Banking Malware Hijacks Chrome and Edge to Steal Credentials and Session Tokens

LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server

China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE

Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution

New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing

⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits

Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users

Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data

N0va Phishkit Targets US and EU Businesses: A New Challenge for Identity Security

An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.

How to Evaluate a Unified Security Platform Using a One-Incident Test

Stop Trying to Control AI Behavior. Control What AI Can Reach

⭐ Featured Resources

Validation Summit ’26: See How Pen Testing, Exposure Validation and BAS Work Together

Red Teams: Learn How Attack Path Chaining Changes Automated Security Testing

Turn Threat Intelligence Into Verified Risk With Threat-Led Penetration Testing

Deploy Browser Security Monitoring in Minutes With a Single Header