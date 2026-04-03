---
title: 1Password open sources a benchmark to stop AI agents from leaking credentials - Help Net Security
url: https://www.helpnetsecurity.com/2026/02/12/1password-security-comprehension-awareness-measure-scam-ai-benchmark/
site_name: tldr
content_file: tldr-1password-open-sources-a-benchmark-to-stop-ai-agen
fetched_at: '2026-02-16T19:17:47.950737'
original_url: https://www.helpnetsecurity.com/2026/02/12/1password-security-comprehension-awareness-measure-scam-ai-benchmark/
author: Sinisa Markovic
date: '2026-02-16'
published_date: '2026-02-12T14:01:50+00:00'
description: AI agent phishing benchmark SCAM from 1Password tests whether models avoid phishing during real tasks, and is now open source.
tags:
- tldr
---

Sinisa Markovic
, Senior Staff Writer, Help Net Security


February 12, 2026


Share


# 1Password open sources a benchmark to stop AI agents from leaking credentials

Research has shown that some AI models canidentify phishing websiteswith near-perfect accuracy when asked. When those same models are used as autonomous agents with access to tools like email, web browsers, and password vaults, they can still carry out the scam.

That gap is the focus of a new open source benchmark from 1Password called the Security Comprehension and Awareness Measure, or SCAM. The benchmark tests whether AI agents behave safely during real workflows, including opening emails, clicking links, retrieving stored credentials, and filling out login forms.

“Every frontier AI model can identify a phishing page when you ask it to,”Jason Meller, VP of Product at 1Password, told Help Net Security. “But when we gave those same models an inbox, apassword vault, and a routine work task, they retrieved real credentials and entered them into an attacker’s fake login page.”

### Testing agent behavior in workplace scenarios

SCAM places models into simulated workplace situations such as an engineer managing infrastructure, a team lead onboarding a contractor, or an employee reviewing messages before a meeting. Each test includes embedded traps that resemble commonreal-world attacks.

Those traps include phishing links inside legitimate-looking emails, lookalike domains that differ by one character, and sensitive credentials hidden inside meeting notes. The model is expected to notice warning signs during normal task execution, without being prompted to search for threats.

The benchmark uses official APIs from providers such as OpenAI, Anthropic, and Google, mirroring how productionAI agentsare deployed. Models are scored on their behavior, including whether they warn users about suspicious activity, whether they refuse unsafe actions, and whether they proceed with credential sharing or form submissions.

“Most AI security benchmarks test whether models can be tricked into breaking their rules,” Meller said. “SCAM tests something harder: whether they walk into attacks on their own, the same way humans do.”

### Safety scores ranged from 35% to 92%

1Password tested eight models across 30 scenarios, running each scenario three times under baseline conditions. Scores ranged from 35% to 92%, with ClaudeOpus 4.6ranking highest and Gemini 2.5 Flash ranking lowest.

Every model committed critical failures in every run. In SCAM scoring, a critical failure is an unsafe action that could lead to leaked passwords, stolen money, or compromised systems, such as entering credentials into a phishing page or sharing secret keys over email.

Gemini 2.5 Flash produced the most critical failures, averaging about 20 per run. GPT-4.1 and GPT-4.1 Mini followed close behind. 1Password said the models routinely forwarded passwords to external contractors, entered credentials into phishing sites, and shared secret keys over email.

### A short “skill file” reduced failures

After baseline testing, 1Password gave each model a short “security skill” document designed to improve how agents assess risk during routine tasks.

With the skill applied, every model improved and critical failures dropped sharply across the benchmark. Several models recorded zero critical failures across repeated runs, including all three Claude models and Gemini 3 Flash.

1Password said the skill file also narrowed the performance gap between stronger and weaker models, bringing most results into a much tighter range and showing that even lower-ranked models could improve significantly with basic security guidance.

### Hidden credentials in documents remain a major risk

One scenario produced failures across every tested model. An email contained meeting notes with passwords and access keys buried in the text. The user asked the agent to forward the notes to a coworker. Every model forwarded the content without warning under baseline testing.

With the skill file applied, six of eight models reliably caught the embedded credentials and refused to forward the email. GPT-4.1 Mini was inconsistent. Gemini 2.5 Flash failed the scenario across all runs even with the skill.

### Open source benchmark

1Password released SCAM under the MIT License, including its scenarios, scoring framework, and testing tools. The project includes features for replaying scenarios step by step and exporting results as videos showing agent actions.

The benchmark is available at the SCAMGitHub repositoryand is intended to support further work on agent safety, credential handling, and enterprise adoption of AI-driven workflows.

Learn more:

* Zen-AI-Pentest: Open-source AI-powered penetration testing framework
* Picking an AI red teaming vendor is getting harder
* AI isn’t one system, and your threat model shouldn’t be either
* That “summarize with AI” button might be manipulating you

More about

* 1Password
* agentic AI
* Artificial intelligence
* cybersecurity
* GitHub
* open source

Share
