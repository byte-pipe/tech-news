---
title: AI agents get better at IT ops, but only with humans in the loop – Computerworld
url: https://www.computerworld.com/article/4205062/ai-agents-get-better-at-it-ops-but-only-with-humans-in-the-loop.html
site_name: tldr
content_file: tldr-ai-agents-get-better-at-it-ops-but-only-with-human
fetched_at: '2026-08-05T20:40:10.361349'
original_url: https://www.computerworld.com/article/4205062/ai-agents-get-better-at-it-ops-but-only-with-humans-in-the-loop.html
date: '2026-08-05'
description: A study of nearly 150,000 real-world agent actions found AI increasingly handling low-risk IT tasks while human analysts iteratively shape and improve their actions.
tags:
- tldr
---

by									
Taryn Plumb

# AI agents get better at IT ops, but only with humans in the loop

news

Aug 4, 2026
6 mins

AI agents are performing roughly 1 in 3 actions in enterprise IT workflows (but that share is rising quickly), while human analysts are rejecting about one-quarter of AI-proposed actions (but that rate is falling), according to a new study of tens of thousands of human-AI interactions. Operational data, rather than underlying AI infrastructures, is often the culprit when things go wrong.

Human analysts are approving the most consequential actions, managing exceptions, and supervising and shaping agentic systems, while AI agents are carrying out routine tasks and executions, automation platform providerFixify found in the study.

“That may sound less dramatic than replacing the help desk,”Matt Peters, Fixify’s co-founder and CEO, wrote in ablog post. “It’s also a much more credible path to changing how IT work gets done.”

## Building scaffolding

Fixify identified four steps of agentic work: Planning, proposing, approving or declining, then acting on approved steps.

It analyzed nearly 18,000 plans and over 147,000 actions executed by agents across 40 companies over a three-month period, finding that agents are taking over one-third of IT actions, most notably in software, applications, security, and collaboration work where requests tend to be “repeatable and easy to reverse.”

Tasks that are well understood and that present low risk are best suited for the current generation of agents, Peters wrote.Human analystsremain closely involved in higher-stakes areas like identity verification, setting up and removing IT access (onboarding and offboarding), and hardware environments.

However, AI’s share of the work is increasing as feedback loops improve: Over the three-month period, human approval of AI-proposed actions rose from 23% to 41%, and rejection fell from 27% to 16%, Fixify found.

The company identified six types of actions in AI automation. Running a skill — actually doing something — accounted for 39.4% of all actions). Most of the rest were coordination: sending a message to the human requester (27.7% of actions), leaving an initial comment (13.2%), giving instructions to a human analyst (9.8%), or waiting (8.8%). Running entire workflows accounted for just 1.1% of actions.

AI is building “scaffolding” that wraps around meaningful changes, often planning far more scenarios than the agent will execute. Typically, agents map out 15 possible actions but run only two, Fixify said.

“The agent maps the paths a request could take, then walks down the path that makes the most sense as it meets reality,” the study said.

Peters pointed to one example where an AI agent identified which team needed access to process a high-volume type of ticket. Rather than fully automating the process, the agent did the initial triage, asked questions, then routed tickets to the team that had the information to act immediately.

“We didn’t need a world-ending hive mind,” he said. “We just needed to point a little conversational intelligence in the right direction.”

## When AI breaks down

IT automation typically involves analyzing tickets and moving them along; in other words, low-risk tasks.

But agents do participate in areas likesecurity(albeit only about 6%), most notably adding and removing people from groups or channels, unlocking accounts, resetting passwords, analyzing multi-factor authentication (MFA), provisioning (or deprovisioning) accounts, and assigning software licenses.

However, this identity-lifecycle work is where agents failed the most, particularly in onboarding and offboarding and identity-access management (IAM), the study found. “Hardware and connectivity changes rarely fail; identity-lifecycle changes fail three-to-nine times as often.”

## Why AI breaks down

Thanks to human-in-the-loop controls, Fixify was able to analyze scenarios where agent recommendation diverged from human judgment. This occurred about 23% of the time.

The largest failure category (nearly 50%) was ‘target not found,’ meaning the agent couldn’t uncover what it needed. This typically comes down to poor data: A user, group, account, or resource was not where the system expected it to be. When people change teams, groups are restructured, accounts are renamed, or work has already been done but not reflected in the system, this is more of an identity hygiene problem than an AI problem. The system needs cleaner and more current data.

Invalid inputs accounted for around 29% of failures, followed by unhandled errors, denied permissions, or invalid operations or configurations. The latter signal “real breakage” in integrations, according to Fixify.

## AI becomes more sophisticated over time

The good news is that AI automation improves over time, even if it might take a while. Inhybrid systems, humans keep the most consequential changes under their own control, and iterative rejection and approval helps AI learn.

Over time, agents’ plans get leaner and they start to re-plan when conditions change, rather than pre-planning all kinds of scenarios that may never occur. “That’s a sign of sophistication,” the study said. “Adapting in the moment is a more advanced behavior than trying to pre-script every contingency.”

In turn, humans second guess the system less often and feel comfortable handing off more work. Instead, they control how agents behave, make high-impact decisions, and handle exceptions. “The hardest requests remain human-heavy, especially those that require repeated replanning or contextual judgment,” the study said.

## How teams can adapt to AI agents

As agentic AI becomes embedded in more workflows — and at deeper levels — enterprises must evolve to accommodate, Fixify emphasized.

This means investing in clean identity data and building strong playbooks, review workflows, and reliable integrations.

Teams should judge agentic tools by their supervision loop and view rejections as a training process, Fixify advised. Analyst time, queues, and metrics should be built around reviewing proposals. Agent replanning can be seen as a routing signal: A single replan might indicate healthy adaptation, while repeated replanning means ambiguity, irrelevance, or unclear policies.

“Make the review surface easy to understand so analysts can assess proposed actions and make quick decisions about how to proceed,” the study advised. “This is where the analyst’s attention belongs.”

Artificial Intelligence
IT Operations
 

														by 															

																Taryn Plumb															

Taryn Plumb is a freelance writer specializing in AI and cybersecurity. She has also written about data infrastructure, quantum computing, networking hardware and software, and the metaverse. In a previous life she was a news and features reporter for The Boston Globe and numerous other outlets and business journals. She is also the author of several regional history books.

## More from this author

* news### Microsoft doubles down on multi-model AI as it builds a Copilot super appJul 30, 20266 mins
* news### Hackers are compromising hotel Wi-Fi gateways to hijack Microsoft 365 accountsJul 27, 20266 mins
* news### Monday.com cuts 20% of its workforce to restructure for the AI eraJul 22, 20267 mins
* news### The EU’s AI transparency deadline is weeks away. Is your enterprise ready?Jul 20, 20268 mins
* news### Did AI decide who lost their jobs? Meta is heading to court over that questionJul 15, 20267 mins
* news### Microsoft is forcing an enterprise transition to passkeysJul 14, 20266 mins
* news### Microsoft bets that enterprise AI needs engineers, not bigger sales teamsJul 6, 20266 mins
* news### Microsoft and Amazon devote billions of dollars to thousands of FDEsJul 2, 20267 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### Microsoft moves to limit AI use by its employees

 
By Mikael Markander
Aug 5, 2026
1 min

Artificial Intelligence
Generative AI
Microsoft

news analysis
 
 

### Apple’s memory crisis is a big red flag for tech

 
By Jonny Evans
Aug 5, 2026
6 mins

Apple
CPUs and Processors
Computer Components

analysis
 
 

### 6 things you should know about Google's new selfie sign-in system

 
By JR Raphael
Aug 5, 2026
9 mins

Android
Data and Information Security
Google

podcast
 
 

### Physical AI: How Intelligent Robots Are Changing the Future of Work

 
Aug 3, 2026
29 mins

Artificial Intelligence
Robotics

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

video
 
 

### Physical AI is changing robotics. Here's what it means for enterprise automation

 
Jul 28, 2026
29 mins

Automotive Industry
Manufacturing Industry
Transportation and Logistics Industry

video
 
 

### How modern work is creating a cybersecurity nightmare

 
Jul 22, 2026
34 mins

Hacking
Security
Vulnerabilities

video
 
 

### Why AI agents fail when enterprises don't define the job

 
Jul 14, 2026
33 mins

Artificial Intelligence
Generative AI
IT Governance