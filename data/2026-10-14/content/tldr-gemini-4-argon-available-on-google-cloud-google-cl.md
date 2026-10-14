---
title: Gemini 4 Argon available on Google Cloud | Google Cloud Blog
url: https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud?e=48754805
site_name: tldr
content_file: tldr-gemini-4-argon-available-on-google-cloud-google-cl
fetched_at: '2026-10-14T22:04:14.967454'
original_url: https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud?e=48754805
date: '2026-10-14'
description: Starting today, we are making our new frontier model, Gemini 4 Argon, available for everyone on Google Cloud.
tags:
- tldr
---

AI & Machine Learning

# Gemini 4 Argon available on Google Cloud, built to help solve your business’ hardest problems

October 13, 2026

##### Michael Gerstenhaber

VP, Product Management, Gemini, Google Cloud

##### Try Gemini 4 Argon

Access the model in Google Cloud

Try now 

Last week we announced that Gemini Enterprise has evolved to make it even simpler to get work done, and introduced theGemini agent, your new universal agent for work. It's always on and ready to answer your questions. It will write code, complete longer and more complex tasks, or perform whatever you need to get the job done, all from a single prompt box. And model intelligence underpins it all.

To enable a new frontier of work, we are making our new frontier model,Gemini 4 Argon, available on Google Cloud.

We trained Argon to work with both depth and precision, which allows it to maintain context across long, multi-step tasks which are reinforced with strong domain expertise along the way. Whether your team is running complex software builds, handling detailed financial and legal work, or deploying cybersecurity tools likeCodeMender, Argon helps your teams maintain focus from start to finish.

Customers and partners using Gemini 4 Argon

### Four ways Argon changes how your business works

#### 1. Hand off your hardest work

Your teams already use Gemini for business to answer questions and draft content. With Argon, they can hand off the deep, multi-step work that used to take hours or days, and get back finished work they can use.

Argon reads long documents that mix text, tables, charts and images, and turns them into one clear output grounded in those sources. It can pull findings from many sources into a single structured answer, analyze data over time, and write stronger legal, finance, and executive documents. On long tasks, it keeps going until the job is done. We trained Argon to respect system boundaries, report negative findings honestly, and pause for confirmation before taking irreversible steps, and it tells you when it couldn't find something or finish a task.

Customers who tested Argon tell us it excels at turning huge, unstructured inputs into cohesive outputs.

"As software development becomes more agentic, teams need models that can support long-running, multi-step work across all stages of the development lifecycle. Gemini 4 Argon is designed to help organizations bring AI into development, security, and operations while keeping it within established enterprise workflows and controls.”– Stuart Moncada, VP, GitLab.

#### 2. Precise, verifiable results on the work that drives your business

In finance, legal, tax, and other regulated work, calculations and data extraction need to be precise, repeatable, and verifiable.

For financial quantitative work, Argon can help automate multi-step ledger reconciliations, spreadsheet formulas, and variance analyses. It delivers high calculation integrity, citation fidelity, and formula accuracy across quantitative models. The proof is in the numbers: Argon leads on theVals Index, which measures economic impact across finance, coding, legal, and tax work.

In legal research, Argon can help legal teams review case law and regulatory filings to pull out verified citations and key precedents. It leads on domain-specific evaluations like Harvey's Legal Agent Benchmark for legal research and drafting, with strong citation fidelity and direct answers when helping teams evaluate complex legal precedents.

"Gemini 4 Argon shows how much progress Google has made on agentic legal reasoning. We saw substantial improvements over Gemini 3.1 Pro across our legal agent evaluations, particularly in corporate M&A, data privacy and cybersecurity, and EC/VC. Accuracy also held up on long-document analysis, an encouraging result for lawyers working through detailed transactional matters."– Niko Grupen, Head of Applied Research, Harvey.

“We collaborated with Google on NowAI-Bench to help shape Gemini 4 for key enterprise work. In early access, it delivered roughly 20% improved task success than Gemini 3.8 Flash, with standout gains in HR and customer service. On the ServiceNow AI Platform, our L1 Service Desk AI specialist brings Google’s most advanced intelligence, governed and secure, turning tasks into fully autonomous work.”- Nenshad Bardoliwalla, Senior Vice President, AI Products, ServiceNow.

#### 3. Build and ship products faster

Argon is built to handle complex, multi-step projects from start to finish. Our customers consistently ask for intelligence that can break down goals, track progress, and update multiple files at the same time.

"Gemini 4 Argon handles complex tasks reliably, from 3D games to rich animations. In Figma Make, it helps teams turn their most ambitious, multi-step ideas into impressive prototypes.”– Loredana Crisan, Chief Design Officer, Figma.

To see how well Argon handles this, we put it to work on our own tools. The team behind our open-source Agent Development Kit (ADK) set out to reduce framework overhead and improve code performance while maintaining full compatibility with existing applications. Working autonomously overnight within automated testing guardrails, Argon surfaced optimizations, now live in google/adk-python, thatcut in-memory session prep time by 40% in long sessions and speed up cold imports by 21%.To learn more, read the engineering deep divehere.

Across Google, engineering teams using Argon in Google Antigravity have increased agentic code submissions by more than 35% while cutting code rollbacks by nearly a third. The Chrome team used Argon to finish an architectural refactor across hundreds of files in Chromium's 40 million-line codebase, completing months of work in weeks.Argon's improvements in spatial reasoning, mathematical precision and visual coding also make it faster to go from idea to working prototype.

For more advanced algorithms, our code optimization and discovery agentAlphaEvolveusesArgonto deliver strong performance improvements across real-world enterprise workloads, including factory scheduling, logistics, game code speed-ups, and chip layout — as well as complex mathematical benchmarks, and more.

To learn how to best use Argon, check out the developer'sguide.

#### 4. Stronger defense for your code and business

While Argon has cyber mitigations that block offensive tasks such as pentesting and exploitation,you can still take full advantage of Argon’s defensive capabilities usingCodeMenderto find and fix vulnerabilities, or use Argon with your own security harness.It ties for first place on CWE-Bench v1 with a top score of68% for remediating security vulnerabilities.

"We are integrating Gemini 4 Argon into MarketingX for automated codebase security audits. In our evaluations, the model successfully identified 100% of top-priority vulnerabilities with 0% fabricated vulnerabilities across verified claims. This precision unlocks proactive, code-level security for our customers before deployment.”- Yunus Emre, Chief AI Officer of AI Lab, HubX.

Security also means being able to trust Argon inside your own environment.Argon is our most resilient model yet against indirect prompt injections, where malicious instructions or context are used to hijack a model’s behavior. It leads the Gray Swan Indirect Prompt Injection benchmark, cutting attack success across 15 adaptive attempts to 0.7%. That matters when Argon reads email, documents and webpages that may contain hidden malicious instructions.

We are also releasing Argon without cyber guardrails to a select set of trusted defenders, which allows for testing a full breadth of cybersecurity capabilities. Trusted defenders are vetted through ourFairwind Program, a limited access initiative that provides government, critical infrastructure, and cybersecurity partners exclusive, unmitigated access to advanced  models.

### Enterprise customers and partners in our early access program are already seeing strong wins with Argon.

Leaders from Amplitude, Deloitte, and Rakuten share Gemini 4 Argon results

### Get started

Starting today, Gemini 4 Argon is available inGemini for businesson the web, desktop, and mobile. Enterprise developers and builders can access Argon via API inGemini platformunder model IDgemini-4-argon, inGoogle AI Studio, and inGoogle Antigravity.

Argon launches at an introductory rate of $2 per million input tokens and $10 per million output tokens through November 30, 2026, with cached input tokens priced at 95% off. After November 30, standard pricing of $4 per million input tokens and $20 per million output tokens will apply. Review themodel cardanddeveloper guidefor complete technical specifications, token limits, and migration instructions.

Cyber defenders can join us atSecurity Summitto learn how to use Gemini 4 Argon to defend against machine-speed threats and automate remediation.

Posted in
* AI & Machine Learning

##### Related articles

Data Analytics

### Predictable AI spend in BigQuery: Introducing cost management for generative AI functions

By Tushar Jaiswal • 9-minute read

AI & Machine Learning

### Welcome to Gemini at Work 2026: Introducing the Gemini agent

By Thomas Kurian • 29-minute read

Customers

### Innovation in Ireland: How Irish brands scale with Gemini Enterprise

By Sandeep Khanna • 5-minute read

AI infrastructure

### What’s new in AI infrastructure and orchestration in September

By Alex Barrett • 19-minute read