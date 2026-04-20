---
title: Cisco goes all in on agentic AI security | Network World
url: https://www.networkworld.com/article/4148823/cisco-goes-all-in-on-agentic-ai-security.html
site_name: tldr
content_file: tldr-cisco-goes-all-in-on-agentic-ai-security-network-w
fetched_at: '2026-03-25T11:19:56.516461'
original_url: https://www.networkworld.com/article/4148823/cisco-goes-all-in-on-agentic-ai-security.html
date: '2026-03-25'
description: 'New offerings include DefenseClaw, an open-source agent framework designed to automate security and inventory, and AI Defense: Explorer Edition, which provides self-service tools for developers to test model and application resilience.'
tags:
- tldr
---

by
Michael Cooney

Senior Editor

# Cisco goes all in on agentic AI security

News

Mar 23, 2026
8 mins


## New offerings include DefenseClaw, an open-source agent framework designed to automate security and inventory, and AI Defense: Explorer Edition, which provides self-service tools for developers to test model and application resilience.



							Credit: 															Shutterstock

Cisco is laying the groundwork to protect enterprise customers from anonslaught of AI agentsand any security problems they may present in the near future. It’s rolling out identity and access management capabilities, a toolkit customers can use to embed security controls inAI agents, and automation features that will allow security operations teams to quickly see and respond to problems.

“We have this opportunity to be atrust layer, not just for … network activity, but actually what’s happening at the application layer, at the workload layer, between agents, between workloads, between data,”Peter Bailey, senior vice president and general manager of Cisco’s security business, toldNetwork World. “Cisco has long offered that trust layer, having trust anchors and trust boundaries and other technologies, so we’re really extending that into the world of agents and workloads.”

##### [ Related:More Cisco news and insights]

To that end, at the RSAC 2026 Conference this week, Cisco is announcing Duo Agentic Identity, a package that extends Cisco’s Identity Intelligence to the AI agent world to help enterprises discover, identify and monitor AI agents and make sure they are accessing only needed resources, Bailey said.

Duois Cisco’s cloud-based security service that provides identification and secure network access control for applications and systems. Identity Intelligence analyzes security behaviors from user identities and access patterns.

Duo Agentic Identity lets users register, map and verify agents so that businesses can identify and track agent activity.

Duo Agentic Identity builds onDuo Directoryto provide a foundational directory where agents are registered as distinct identity objects—not service accounts, not proxies of their human operators,” wroteMatt Caulfield, vice president of product, identity with Cisco in ablog postabout the news. “Each agent is mapped to a human owner, assigned to groups for policy enforcement, authenticated at access and fully logged from the moment it is onboarded. The result: Every action is traceable to a sponsor. And when an agent’s work is done, lifecycle visibility gives your team the confidence to know that access has been removed.”

“Overprivileged agents are among the highest-risk conditions in any agentic deployment. And in an agentic context, least privilege needs to be a per-action constraint, evaluated at the level of each individual tool call,” Caulfield wrote.

Duo Agentic Identity enforces this control through an MCP gateway, “a control point between your AI agents and the tools and systems they interact with,” Caulfield wrote. “MCP is emerging as a standard interface through which agents discover and invoke enterprise tools. Rather than relying on each tool server to enforce access controls correctly, the gateway intercepts every request, evaluates it against Duo’s fine-grained authorization engine, and permits or blocks the action before it reaches the target system.”

“Policies map specific agent identities and groups to specific tool calls, all while enabling granular control over scope, conditions, and permitted operations,” he wrote.

### Cisco AI Defense: Explorer Edition

Cisco is also expanding the role of its AI Defense planform for agentic AI protections.

The AI Defense package offers protection to enterprise customers developing AI applications across models and cloud services. AI Defense is made up of four components: AI Access, AI Cloud Visibility, AI Model & Application Validation, and AI Runtime Protection. AI Access offers visibility into who wants or has use of an AI application, and then it controls access to protect and enforce data-loss prevention and mitigate potential threats. AI Cloud Visibility uncovers AI assets comprising custom-built AI applications offering a single-pane-of-glass view of AI inventory, Cisco said.

Now Cisco is adding AI Defense: Explorer, which the vendor says will help organizations test, trust, and secure their AI agents and the interactions between them.

“Whether you’re building your own model or (more likely) sourcing one from the millions of open-source options available online, red teaming is critical to measure the baseline of its safety and security alignment,” wroteEmile Antone(product marketing manager for Cisco’s AI software and platform group) andGurpreet Kaur Khalsa(principal product manager at Cisco) in ablog post.

“Cisco AI Defense: Explorer Edition uses algorithmic red teaming to accomplish this in as few as twenty minutes, evaluating model performance in over 200 risk subcategories including intellectual property theft, toxicity, and sensitive data extraction.”

The package support for all major agentic frameworks, model providers, and MCP-connected systems to help customers glean a deep understanding about their AI agents.

“At the highest level, comprehensive risk scores give users an idea of how their model or agent performed across different content categories and adversarial techniques,” the authors wrote. “Results are mapped to Cisco’sIntegrated AI Security and Safety Framework, one of the industry’s most comprehensive taxonomies of AI threats. These reports make it easy to measure risk, communicate across AI stakeholders, and understand exactly what guardrails are needed to secure an agentic AI application.”

### SIEM updates

Also on tap is a new release of Cisco’s security information and event management platform, Splunk Enterprise Security (ES). Splunk ES offers tools and applications that enterprises can use to detect, investigate, and respond to cyber threats in real time. Cisco aims to move traditional SOC operations to what it calls an agentic SOC that changes and automates the fundamental operating model of the security team.

With Splunk ES, Cisco is adding a variety of agents to automate and ease security operations. For example, a new SOP Agent lets customers import security standard operating procedures (SOP) into Splunk ES response plans using multi-modal LLMs. A Triage Agent helps to autonomously enrich, prioritize, and explain alerts, greatly reducing the fatigue put on analysts, Cisco stated.

Other new ES features include:

* Detection Studio: A unified workspace for detection engineers to plan, develop, test, deploy, and monitor detections. By mapping coverage against the MITRE ATT&CK framework, teams can identify data gaps and validate detection quality in real time. Another new instrument, Malware Threat Reversing Agent, gives customers insight into malware threats, providing summaries and step-by-step breakdowns of malicious scripts.
* Federated Search: Lets SecOps teams gain comprehensive visibility across distributed data sources, according to Cisco.
* Exposure Analytics: Automatically discovers assets and users across the environment. By leveraging data already being ingested, it provides a “Security Truth Layer” without the need for additional agents or tools, Cisco stated.

### Cisco DefenseClaw

Cisco is also releasing an open-source secure agent framework called DefenseClaw that lets users define policy-based security, network, and privacy guardrails for Nvidia’s recently releasedOpenShellandOpenClawagentic environments.

DefenseClaw scans everything before it runs, according toDJ Sampath, senior vice president of Cisco’s AI software and platform group.

“Every skill, every tool, every plugin, before it’s allowed into your claw environment and every piece of code generated by the claw gets scanned. The scan engine includes five tools:skill-scanner,mcp-scanner,a2a-scanner,CodeGuardstatic analysis, and anAI bill-of-materialsgenerator. The scan engine includes five tools:skill-scanner,mcp-scanner,a2a-scanner,CodeGuardstatic analysis, and anAI bill-of-materialsgenerator,” Sampath wrote in ablog postabout the news.

DefenseClaw also detects threats at runtime, not just at the gate, Sampath stated.“Claws are self-evolving systems. A skill that was clean on Tuesday can start exfiltrating data on Thursday. DefenseClaw doesn’t assume what passed admission stays safe — a content scanner inspects every message flowing in and out of the agent at the execution loop itself,” Sampath wrote.

And thirdly, DefenseClaw enforces block and allow lists. “When you block a skill, its sandbox permissions are revoked, its files are quarantined, and the agent gets an error if it tries to invoke it. When you block an MCP server, the endpoint is removed from the sandbox network allow-list and OpenShell denies all connections. This happens in under two seconds, no restart required.”

#### More Cisco news:

* Cisco goes all in on agentic AI security
* Cisco Talos 2025 year in review and lessons learned
* How Cisco’s platform mindset is meeting the AI era
* Cisco extends AgenticOps across networking, security, observability products
* Cisco amps up Silicon One line, delivers new systems and optics for AI networking
* Takeaways from Cisco’s AI Summit
* Cisco: Infrastructure, trust, model development are key AI challenges
* AI, security tailwinds signal promising 2026 for Cisco
* Cisco adds intelligent policy enforcement to mesh firewall family
* Actively exploited Cisco UC bug requires immediate, version‑specific patching
* Cisco’s 2026 agenda prioritizes AI-ready infrastructure, connectivity
* Cisco finally patches seven-week-old zero-day flaw in Secure Email Gateway products

Artificial Intelligence
Network Security
Security




				SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

				Get started by entering your email address below.



Please enter a valid email address

Subscribe



														by

																Michael Cooney

Senior Editor

1. Follow Michael Cooney on X
2. Follow Michael Cooney on LinkedIn

Michael is a senior editor with Network World focused on deciphering the strategies of many core high-tech vendors such as Cisco, Arista, Juniper, HPE and IBM. Michael has been writing about the industry for more than 33 years and has won coverage awards from ASBPE and FOLIO. He has a BA in Journalism and Technical Writing Certificate from The Pennsylvania State University.He can be reached atmichael_cooney@foundryco.com.

## More from this author

* news### HPE, Nvidia expand AI partnershipMar 17, 20264 mins
* news### Cisco extends its Secure AI Factory with NvidiaMar 16, 20266 mins
* news### Arista targets AI data centers with new liquid cooled pluggable optic moduleMar 13, 20265 mins
* news### Cisco grows high-end optical support for AI clustersMar 12, 20264 mins
* news### Cisco blends Splunk analytics, security with core data center managementMar 10, 20264 mins
* news analysis### Cisco: LPO not a panacea but plays strategic role in AI networksMar 6, 20264 mins
* news### Cisco: AI is a double-edged sword in industrial networksMar 3, 20264 mins
* news### IBM X-Force: AI creates security challenges, but basic system flaws are more problematicFeb 25, 20265 mins


## Show me more

Popular
Articles
Podcasts
Videos

news



### 2026 network outage report and internet health check


By Denise Dubie
Mar 24, 2026
29 mins

Cloud Computing
Network Monitoring
Networking

news



### FCC bans foreign routers, putting enterprise network risk in focus


By Prasanth Aby Thomas
Mar 24, 2026
4 mins

Networking
Networking Devices

news analysis



### Nvidia: Latest news and insights


By Dan Muse
Mar 23, 2026
42 mins

Artificial Intelligence

podcast



### Has the hype around ‘Internet of Things’ paid off? | Ep. 145


Apr 18, 2024
36 mins

IoT Platforms
IoT Security

podcast



### Episode 1: Understanding Cisco’s Converged SDN Transport


Sep 24, 2021
20 mins

Cisco Systems
Internet
Networking

podcast



### Episode 2: Pluggable Optics and the Internet for the Future


Sep 23, 2021
17 mins

Cisco Systems
Computers and Peripherals
Internet

video



### Master Linux Math with the bc Command | Easy CLI Calculations Explained!


Jun 23, 2025
1 mins

Operating Systems

video



### Master Linux Math in Seconds: How to Use the expr Command Like a Pro


Jun 17, 2025
1 mins

Operating Systems

video



### How to Do Math in the Command Line Using Double Parentheses


Jun 6, 2025
1 mins

Operating Systems
