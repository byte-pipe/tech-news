---
title: 'Runtime: The new frontier of AI agent security | CSO Online'
url: https://www.csoonline.com/article/4145127/runtime-the-new-frontier-of-ai-agent-security.html
site_name: tldr
content_file: tldr-runtime-the-new-frontier-of-ai-agent-security-cso
fetched_at: '2026-03-31T11:22:26.938299'
original_url: https://www.csoonline.com/article/4145127/runtime-the-new-frontier-of-ai-agent-security.html
date: '2026-03-31'
description: Security leaders say monitoring agent behavior inside enterprise systems may be the next major challenge for CISOs.
tags:
- tldr
---

by
Cynthia Brumfield

Contributing Writer

# Runtime: The new frontier of AI agent security

Feature

Mar 17, 2026
10 mins


## Security leaders say monitoring agent behavior inside enterprise systems may be the next major challenge for CISOs.



							Credit: 															Rob Schultz / Shutterstock

AI agents are already operating inside enterprise networks, quietly doing some of the work employees once handled themselves — writing code, drafting emails, retrieving files, and connecting to internal systems.

Sometimes they also make costly mistakes.

At Meta, an employeeasked an AI assistantto help manage her inbox. It deleted it instead. At Amazon, an internal agentautonomously decidedto tear down and rebuild a deployment environment, knocking an AWS service offline for 13 hours.

These incidents offer glimpses of a larger shift security leaders are confronting: Autonomous software is now acting inside corporate environments with real permissions and real consequences.

“Agents are like teenagers,”Joe Sullivan, former chief security officer of Uber, Cloudflare, and Facebook, and now head of Joe Sullivan Security, tells CSO. “They have all the access and none of the judgment.”

For years, most efforts tosecure AI have focused on prevention— scanning models, filtering prompts, and analyzing AI-generated code before it reaches production. But as enterprises deploy autonomous agents that interact directly with internal systems, some security leaders say the real risk beginsonly after those agents are live.

“In security, we always assume prevention will fail,” Sullivan says. “That’s why detection and monitoring are equally important.”

The speed and autonomy of AI agents mean mistakes or unexpected actions can cascade quickly across systems. That dynamic is why a growing number of security leaders are rallying around, at least conceptually, what Sullivan callsruntime security, or continuously monitoring agents as they operate inside enterprise environments.

In simple terms, runtime security focuses on what software does while it is running, rather than only evaluating it before deployment.

## Why agents change the security model

CISOs have spent years governing human behavior inside enterprise networks. They have identity management, role-based access controls, user behavior analytics, and endpoint detection tools.

The question is whether those same frameworks — and those same tools for tracking employees —can be extended to AI agents. Security leaders studying the problem say the answer is: only partially. The traditional frameworks still apply conceptually, but the mechanisms required to observe agent behavior are fundamentally different.

“The what isn’t new — the how is new,” saysHanah-Marie Darley, co-founder and chief AI officer of Geordie AI. “How do you actually get this data, where you actually get the agent’s behavioral information mostly through logs, and not every AI agent platform will mean that you are getting logs, that you have logs in the first place.”

Traditional security tools were built to intercept human behavior at perimeter checkpoints where employees access the internet, log into systems, or move data across boundaries. Agents frequently bypass those checkpoints entirely. They operate through API calls andMCP connectionsthat may never pass through the security tooling that wouldordinarily flag anomalous behavior.

They also generate dramatically more activity. Where a typical employee might produce 50 to 100 log events in a two-hour period, an agent can generate 10 to 20 times that volume in the same window. And — critically — they often don’t produce any logs.

Some agent platforms generate robust audit trails by default. Others don’t. Coding agents can overwrite their own session logs when a previous session is replayed, meaning a security team investigating an incident may find the record of what happened has been erased.

“Having the logs in the first place is often a bigger step than people realize because not every agent natively has logs,” Darley tells CSO.

## The inventory problem

Before a CISO can monitor what agents are doing, they face a more elemental challenge: knowing which agents exist.

This simple idea is harder than it sounds. In many large enterprises, agents are proliferating faster than any central inventory can capture. Marketing teams deploy AI assistants. HR departments use agents for resume screening. Engineers run coding agents with broad filesystem access. Non-technical employees connect AI productivity tools such asnote-takers, email managers, and scheduling assistants to corporate accounts, often without formal IT approval.

“CISOs right now are getting the hard question from their board and their CEO,” Sullivan says. “What AI is being run inside the company right now? You’ve got to answer that question. What AI is being run, and what’s it doing?”

Darley recommends starting with a structured inventory effort, ideally using tools built specifically for agent discovery, since general-purpose application management systems often can’t see agents living in the cloud, in code repositories, or inside third-party SaaS platforms.

“Start with at least one system,” she advises. “It will give you a sense of scale, help you understand who the owners are, and start to educate you on the kind of tooling you actually need.”

Without inventory, behavioral monitoring has nothing to which it can anchor. Security teams can watch the logs of the agents they know about. But the agents they have missed are precisely the ones most likely to deliver unwelcome consequences.

## What runtime monitoring looks like

Once an organization knows where its agents are, the question is what to watch for — and how.

Elia Zaitsev, CTO of CrowdStrike, tells CSO that existingendpoint detection and response (EDR) toolsalready capture the kinds of behavior needed to track AI agents. They instrument operating systems like a flight data recorder, recording every application that runs, every file it touches, every network connection it makes, and every command it spawns.

CrowdStrike’s EDR, for example, builds a threat graph: a connected map of behaviors and their upstream causes. If a suspicious network connection occurs, the threat graph can trace it back through many degrees of separation to the application or agent that initiated the chain.

“EDR technology can associate this end behavior with the fact that it came from an application ultimately being driven by an agentic system,” Zaitsev explains. “A firewall just tells you something on this computer is trying to communicate with an AI model in the cloud. EDR allows you to say: This specific application is talking to this specific model.”

For AI agents specifically, this creates a new set of controls. A system that recognizes a known agent application — Claude Code, OpenAI’s Codex, OpenHands — can apply a different policy to that application than it would to the same application running under human control. “There are activities that may be benign if a human is responsible,” Zaitsev says, “but if it’s an AI agent I don’t necessarily trust, I may want to apply different policies on the fly.”

## Build-time security still has a pivotal role to play

Not all enterprises will be solely introducing AI agents off the shelf. Many will be building such systems themselves.

Because of this, runtime monitoring does not mean that build-time security — scanning code, evaluating models before deployment, and checking prompts — is yesterday’s problem.Varun Badhwar, CEO of Endor Labs, pushes back on that kind of framing.

“I’ll never say runtime isn’t important,” Badhwar tells CSO. “But you want to fix as much as you can early. The average cost of a runtime security finding is $4,000, versus $40 at build time. So, guess what? You want to fix as much as you can before it ever gets there.”

A vulnerability caught while a developer is still writing code takes minutes to fix. That same vulnerability, once deployed into a container, run through QA, and pushed to a production environment, requires retracing every step of that journey before it can be addressed — at roughly a hundredfold the cost. Badhwar uses the analogy of a car manufacturing line: Quality controls on the assembly line are always cheaper than recalling 70,000 cars from the street.

His framework is simple: Shift left, shield right. Shift as many security controls as possible into the development process — catch problems while agents are being built, not after they’re running. Then shield right with runtime monitoring as your last-mile safety net, because some things will always slip through, and zero-day vulnerabilities by definition can’t be anticipated at build time.

## What CISOs should do now

For CISOs, the shift is less about a single new tool and more about a new way of thinking about AI risk. Instead of focusing solely on how agents are built, security teams increasingly need visibility into how they behave once they begin operating inside enterprise systems.

The path forward for CISOs is therefore not a single new product or a rip-and-replace of existing infrastructure. It is a methodical extension of security discipline to a new category of actor inside the enterprise.

Zaitsev frames it using the security-in-depth model: You don’t stop securing agents at build time just because runtime monitoring is available. You build both. “EDR and runtime security is that last-level safety net,” he says. “You still want all those other layers.”

But the experts say the following starting points could be practical first steps toward implementing runtime security for most CISOs:

Build an inventory first.Pick one system — a major SaaS platform, your code repositories, your endpoint fleet — and map the agents operating within it. Identify the owners, the permissions, and the protocols. Without visibility, nothing else is possible.

Extend behavioral monitoring to agents.Whether through EDR, dedicated agent security tooling, or a combination, establish what normal looks like. What systems should each agent touch? What data should it process? Who should it communicate with? Deviations from that baseline are your signal.

Apply agent-specific policies.Don’t govern agents with the same controls you use for employees. They have different access patterns, different risk profiles, and different failure modes. Agent-aware tools can differentiate policy based on whether an application is AI-driven.

Design for incident response before you need it.Know how you’ll stop a misbehaving agent without destroying the evidence of what it did. Behavioral logs need to be captured in separate, write-protected stores — not just in the agent platform’s native logging, which may be overwritten.

Plan for AI solutions to AI problems.You won’t hire your way out of the volume challenge. Security teams will need automation to monitor systems that operate at machine speed.

See also:

* Agentic AI: A CISO’s security nightmare in the making?
* Think agentic AI is hard to secure today? Just wait a few months
* What CISOs need to know about new tools for securing MCP servers
* Misconfigured MCP servers expose AI agent systems to compromise
* How cybersecurity leaders can defend against the spur of AI-driven NHI
* MCP: Securing the backbone of agentic AI

Artificial Intelligence
Application Security
Security
DevSecOps




				SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

				Get started by entering your email address below.



Please enter a valid email address

Subscribe

														by

																Cynthia Brumfield

Contributing Writer

Cynthia Brumfield is a veteran communications and technology analyst who is currently focused on cybersecurity. She runs a cybersecurity news destination site,Metacurity.com, consults with companies through her firm DCT-Associates, and is the author of the book published by Wiley,Cybersecurity Risk Management: Mastering the Fundamentals Using the NIST Cybersecurity Framework.Cynthia holds a Master of Planning Degree from the University of Virginia and a Bachelor’s degree from The George Washington University. She has won multiple AZBEE awards for her work on CSO, including two in 2025.

## More from this author

* news### Faster attacks and ‘recovery denial’ ransomware reshape threat landscapeMar 23, 20267 mins
* feature### Anthropic ban heralds new era of supply chain risk — with no clear playbookMar 19, 202611 mins
* news### CVE program funding secured, easing fears of repeat crisisMar 9, 20267 mins
* news### Trump’s cyber strategy emphasizes offensive operations, deregulation, AIMar 6, 20266 mins
* news### Five Eyes issue emergency directive on exploited Cisco SD-WAN zero-dayFeb 25, 20265 mins
* feature### Boards don’t need cyber metrics — they need risk signalsFeb 25, 20267 mins
* news### The rise of the evasive adversaryFeb 24, 20268 mins
* feature### CISOs must separate signal from noise as CVE volume soarsFeb 11, 20268 mins


## Show me more

Popular
Articles
Podcasts
Videos

news



### Fortinet hit by another exploited cybersecurity flaw


By Taryn Plumb
Mar 30, 2026
5 mins

Security
Vulnerabilities

news



### LangChain path traversal bug adds to input validation woes in AI pipelines


By Shweta Sharma
Mar 30, 2026
4 mins

Security
Vulnerabilities

opinion



### Why Kubernetes controllers are the perfect backdoor


By Niranjan Kumar Sharma
Mar 30, 2026
6 mins

Cloud Security
Security

podcast



### CSO Executive Sessions ASEAN: From Compliance to Cyber Resilience-Securing Patient Trust in Southeast Asia’s Hospitals


By Estelle Quek
Feb 24, 2026
23 mins

Cyberattacks
Cybercrime
Ransomware

podcast



### How Intelligence and AI Are Changing Cyber Defense | Erin Whitmore, Former CIA


By Joan Goodchild
Feb 4, 2026
28 mins

Cyberattacks
Cybercrime

podcast



### Inside the SMB Threat Landscape: AT&T’s Senthil Ramakrishnan on Why Small Businesses Are Cybercrime’s Favorite Target


By Joan Goodchild
Jan 13, 2026
23 mins

Cybercrime
Small and Medium Business

video



### CSO Executive Sessions ASEAN: From Compliance to Cyber Resilience-Securing Patient Trust in Southeast Asia’s Hospitals


By Estelle Quek
Feb 24, 2026
23 mins

CSO and CISO
Electronic Health Records
Ransomware

video



### How Intelligence and AI Are Changing Cyber Defense | Erin Whitmore, Former CIA


By Joan Goodchild
Feb 4, 2026
28 mins

Cyberattacks
Cybercrime

video



### Inside the SMB Threat Landscape: AT&T’s Senthil Ramakrishnan on Why Small Businesses Are Cybercrime’s Favorite Target


By Joan Goodchild
Jan 13, 2026
23 mins

Cybercrime
Small and Medium Business
