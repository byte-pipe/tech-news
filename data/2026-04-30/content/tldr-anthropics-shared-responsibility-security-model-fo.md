---
title: Anthropic's Shared Responsibility Security Model for AI Agents, Explained - Backslash
url: https://www.backslash.security/blog/anthropics-shared-responsibility-security-model-for-ai-agents
site_name: tldr
content_file: tldr-anthropics-shared-responsibility-security-model-fo
fetched_at: '2026-04-30T20:09:05.287355'
original_url: https://www.backslash.security/blog/anthropics-shared-responsibility-security-model-for-ai-agents
date: '2026-04-30'
tags:
- tldr
---

Back to Blog

# Anthropic's Shared Responsibility Security Model for AI Agents, Explained

-

April 29, 2026

Yossi Pik
CTO & Co-Founder

-

April 29, 2026

Earlier this month Anthropic, the company behind Claude, published a proposal to NIST (the U.S. federal agency that governs technology standards) which, for the first time, outlines the key  areas of agentic AI security, and how they should be addressed and governed. Anthropic should be applauded for taking this initiative, since existing standards and frameworks are lacking, creating confusion among end-user organizations. Security practitioners should take heed since NIST standards can later translate into Federal regulations and even legislation.

In June 2017, a misconfigured S3 bucket at Deep Root Analyticsexposed 198 million American voter records. AWS's infrastructure was fine. The encryption was available. The access controls existed. The customer didn't turn them on.

That breach - and hundreds like it - taught the industry a lesson that took years to land: the cloud provider secures the cloud,yousecurewhat's inthe cloud. It was the beginning of the so-called “shared responsibility model” that stratified and delineated who’s responsible for what in cloud security, and while it’s neither perfect nor really “shared”, it still serves as a lighthouse for an entire industry of practitioners and vendors.

Anthropic has drawn the same line for AI agents. Most organizations aren't ready for it, but it’s a beacon for the industry to follow. They published"Trustworthy Agents in Practice,"a research paper that breaks AI agent security into four layers with clear ownership. Anthropic's contribution isn't a new idea - but it's the first time a frontier model provider has clearly articulated their own part. And it comes (bravely) with uncomfortable data about what's already failing.

Key takeaways:Anthropic's framework divides AI agent security into four layers -Model,Harness,Tools, andEnvironment- with the model provider owning only the first. Anthropic's own data shows human-in-the-loop oversight has already failed at production scale (93% of permission prompts approved without reading, clarification rate of just 16.4% on complex tasks). And six NIST standards and federal frameworks structurally exclude the most likely agent failure mode: agents causing harm within their authorized permissions.

### What is Anthropic's Model for AI Agents? And How is Responsibility Assigned Within It?

Anthropic's shared responsibility model divides AI agent security into four layers, each with a different owner and a different failure mode. The framework mirrors the cloud shared responsibility model that AWS, Azure, and GCP established for infrastructure - but applied to AI agents. The reason it needs its own framework: a cloud VM doesn't remember yesterday's instructions, independently decide to call a third-party API, or pass outputs to another VM that trusts them blindly. AI agents do all three.

#### Layer 1: Model.

The AI itself - how it reasons, what behaviors are trained in, what safety guardrails are baked at the model level. This is the model provider's responsibility (Anthropic, OpenAI, Google - whoever built the model). They train it to be safe, to refuse harmful requests, to ask for clarification when things are ambiguous. You don't control this layer. You chose a vendor. They own it.

#### Layer 2: Harness.

The instructions, guardrails, and approval workflows wrapped around the agent. System prompts, security policies, rules about what the agent can and can't do. Think of it as the operating manual you handed your agent. This is the layer most organizations think they have covered. They don't.

#### Layer 3: Tools.

Everything the agent can interact with - MCP servers (Model Context Protocol - the open standard connecting AI agents to external tools and data sources), APIs, plugins, and external services. When your agent sends an email, queries a database, or calls a third-party API, that's the tools layer.

There's a structural asymmetry here: most MCP server maintainers don't consider themselves to carry security obligations to your deployment. You approved the tool. You own the risk.

#### Layer 4: Environment.

Where the agent runs, what data it can access, what systems it's connected to, and what the operational stakes are. An agent on a developer's laptop with a test database is a different risk profile than the same agent in production with access to customer PII. Same model, same harness, same tools - different environment, completely different risk.

Anthropic states directly in the paper that"a well-trained model can still be exploited through a poorly configured harness, an overly permissive tool, or an exposed environment."The model provider is telling you: a perfect model with bad instructions, bad tools, or a bad deployment is still a security problem.

Three out of four layers are the deploying organization's responsibility. That's the core message of the framework.

### Anthropic's Four-Layer Framework at a Glance

Layer

What It Covers

Who Owns It

Key Risk

Model

AI reasoning, training, behavioral guardrails

Model provider (Anthropic, OpenAI, Google)

Model-level vulnerabilities, alignment failures

Harness

System prompts, policies, approval workflows

Deploying organization

Inadequate instructions, governance gaps

Tools

MCP servers, APIs, plugins, external services

Deploying organization

Supply chain compromise, overly permissive access

Environment

Infrastructure, data access, deployment context

Deploying organization

Excessive permissions, sensitive data exposure

#### A Real Mapping Exercise

When security teams audit their MCP server connections, the results are rarely reassuring. One team found fourteen connected servers. Three had pushed updates the previous week that nobody reviewed. One had added a tool capability that didn't exist when it was originally approved.

That's the tools layer. Now multiply it across every team using AI agents and ask the same question about the harness layer (who wrote those system prompts?) and the environment layer (what data can those agents reach?).

Answering "which model" is simple. Answering the other three rarely is.

### What Are the Main AI Agent Security Threats?

Anthropic's paper identifies three agent-specific threat vectors that go beyond traditional AI security risks. These threats are distinct because they exploit the architectural properties of agents - persistence, tool access, and multi-agent communication.

#### AI Agent Tool Supply Chain Compromise

The most immediately actionable threat is tool supply chain compromise.

You vet an MCP server. It connects your agent to a database, provides three well-scoped tools, does exactly what it says. You approve it. Three weeks later, that server pushes an update - new tool descriptions, expanded capabilities, different behavior. Your one-time approval now covers a tool you never actually reviewed.

This maps to a pattern security teams already understand: SolarWinds-class supply chain risk applied to AI agent tooling. The thing you trusted changed after you trusted it. Periodic auditing can't catch changes that happen between audits.

#### Persistent Memory Poisoning in AI Agents

The second threat is persistent memory poisoning - and it's harder to detect than supply chain compromise because the malicious payload lives inside the agent's own trust boundary.

An attacker injects corrupted information into an agent's stored context. The agent clears its active memory, moves on. Days later, it retrieves that stored memory, trusts it - it's the agent's own records - and acts on poisoned data. Imagine a code review agent whose memory of "approved patterns" has been poisoned to whitelisteval()on user input. Every future review passes the dangerous pattern without flagging it. The standard defense of validating inputs at entry fails structurally, because by the time anyone checks, the poison is already inside.

#### Trust Escalation Across AI Agents

The third threat targets multi-agent systems, and it's addressed in both Anthropic's paper andOWASP's Top 10 for Agentic Applications(risks ASI07: Insecure Inter-Agent Communication and ASI08: Cascading Failures). One agent's output becomes another agent's trusted input. If Agent A is confused or compromised, Agent B inherits that confusion as fact. Research on multi-agent systems suggests it's often easier to fool an agent through another agent than to fool it directly - the receiving agent has no priors that say "distrust your peer." In multi-agent orchestrations, this means a single point of confusion can cascade through the entire chain.

### Why Human-in-the-Loop Oversight is Failing for AI Agents

Anthropic's paper includes usage data showing that human-in-the-loop oversight for AI agents has already broken down in practice.

The paper reports that on complex tasks, Claude asks for clarification on 16.4% of turns - more than twice the rate on simple tasks. The model itself distinguishes genuine ambiguity. But users don't match that diligence. Separately, Anthropic's data from theClaude Code auto mode launchshowed that developers already approve 93% of permission prompts. At hundreds of actions per session, per-action approval hits what the paper describes as consent fatigue - the human is nominally in the loop but functionally checked out.

Ilya Kabanov's analysis of the paperframed it better than I could: experienced users "are not reviewing actions before they happen. They are letting the agent run and stepping in when something goes wrong. That is incident response, not oversight." Human-in-the-loop has become human-on-the-side. Kabanov's full analysis is worth reading - it's the sharpest secondary take on the paper I've found, and several of the insights in this post build on his work.

I wrote about this exact dynamic when Anthropic launched auto mode for Claude Code. The 93% approval rate was the headline. I called it the death of the approval-based security model. The auto mode data was suggestive. The "Trustworthy Agents in Practice" paper makes it definitive: this isn't a Claude Code edge case, it's the steady-state of human-agent interaction at production scale.

I see this firsthand. I run a team of nine AI agents for my own daily work - research, content, competitive analysis, product management, call analysis. I've watched the consent fatigue cycle firsthand. You start careful… by day three you're approving file writes without reading. By week two you've configured auto-approve for most operations. Anthropic's data matches exactly what happens when agents move from demo to daily driver.

My recommendation:Stop designing governance around per-action approval. Instead, invest in security tooling that operates at the harness and environment layers - enforcing policy continuously across your agent fleet rather than asking humans to review each action. Anthropic built "Plan Mode" for individual developers. Enterprises need the organizational equivalent. More on what that looks like in practice below.

### Your Incident Playbook Has a Blind Spot

There's a less obvious problem the framework exposes.Ilya Kabanov's analysisof the Anthropic paper found that six NIST standards and federal frameworks - includingFISMA,SP 800-61, and four others - each independently scope out non-adversarial agent-caused harm. All seven illustrative incidents in SP 800-61 begin with "an attacker." Not one addresses an autonomous agent making a mistake within its authorized permissions.

An agent legitimately accesses a database, correctly follows its instructions, but produces harmful outcomes because the instructions themselves were inadequate. Your IR process never triggers. Your SIEM never alerts. The agent did exactly what you told it to do, and it still went wrong.

Yes, operational risk frameworks like theAI RMFcover this conceptually. But operational risk frameworks don't trigger SOC pages, SIEM alerts, or IR playbooks. The gap isn't governance writ large - it's the layer that fires when something is actively going wrong.

NIST is working on it - the January 2026RFI on AI Agent Securityreceived932 public comments. But standards move slowly. Your agents are running now. Your playbooks need to cover them now. And until the standards catch up, the only way to detect "authorized-but-harmful" agent behavior is tooling that monitors what agents actually do - not just what they're allowed to do.

### What Security Teams Should Do Now

Anthropic's framework makes sense and sets clear boundaries. But a framework on a page doesn't secure your agents. Security teams need to take ownership of the three layers that are theirs - and start now.

Map your agent deployments against the four layers.The model is your vendor's problem. The other three are yours. Start asking: what instructions govern your agents, and who wrote them? What MCP servers, plugins, and APIs are connected - and have any changed since they were approved? What data can your agents reach, and what's the blast radius if something goes wrong?

Shift from per-action approval to plan-level governance.Stop reviewing individual file writes and API calls. Define what agents are authorized to do at the policy level - which permissions are granted, which safety flags are set, and whether the defaults your vendor shipped last week still enforce what you think they enforce.

Treat the tool supply chain like you treat the software supply chain.MCP servers, plugins, and APIs update independently. A Slack connector that originally sent messages might now read entire channel histories. A read-only database tool might have added write capabilities. Static approval doesn't survive that kind of velocity - you need continuous monitoring of what tools actually do, not just what they were approved to do.

Update your incident definitions before your next agent failure forces the question.Add "authorized-but-harmful autonomous actions" to your IR playbook. Don't wait for NIST.

Because if your current incident playbook starts every scenario with "an attacker" - it's time to add a new chapter.

### How Backslash Secures the Three Layers

Doing all of the above continuously, across an enterprise's full agent fleet, is not a manual process.

Backslash is purpose-built to secure the three layers that Anthropic says are yours - tracking the velocity of LLM vendor releases and updates.

Harness- Continuous visibility into agent configurations, system prompts, permission settings, and safety flags across your organization. When a vendor ships new defaults or deprecates a security boundary, you don't find out from a postmortem.

Tools- Real-time monitoring of MCP server connections, plugin capabilities, and API changes. When a tool adds capabilities you never approved or changes its parameter schema, the change shows up before the next audit cycle, not after.

Environment- Full context for every agent deployment: what data agents can reach, what permissions are active, and how tool configurations interact with operational context. A tool safe in one environment might be dangerous in another - you see the difference before it matters.

If you're trying to operationalize Anthropic's framework in production,we'd like to show you what that looks like running.

Get a Live Demo

### Frequently Asked Questions

Q:What is Anthropic's shared responsibility model for AI agents?‍A:Anthropic's shared responsibility model, published in their April 2026 paper"Trustworthy Agents in Practice,"divides AI agent security into four layers: Model (owned by the AI provider), Harness (instructions, policies, guardrails), Tools (MCP servers, APIs, plugins), and Environment (deployment context, data access). Three of the four layers are the deploying organization's responsibility, mirroring the cloud shared responsibility model established by AWS, Azure, and GCP.

Q:What are the four layers of Anthropic's AI agent security framework?‍A:Model (the AI itself), Harness (instructions and policies governing the agent), Tools (MCP servers, APIs, and plugins the agent accesses), and Environment (where the agent runs and what data it can reach). The model provider owns Layer 1; the deploying organization owns the other three.

Q:Why is human-in-the-loop failing for AI agents?‍A:According to data published by Anthropic, human oversight of AI agents fails due to consent fatigue. Anthropic'sClaude Code auto mode datashowed developers approve 93% of permission prompts, and their"Trustworthy Agents in Practice"paper reports that at hundreds of actions per session, per-action approval becomes impractical. Anthropic's recommended alternative is "Plan Mode" - reviewing execution plans upfront rather than approving individual agent actions.

Q:What is an AI agent tool supply chain compromise?‍A:AI agent tool supply chain compromise occurs when remotely hosted tools - such as MCP servers - change their behavior after initial approval. An MCP server that was safe when vetted can update its tool descriptions, add new capabilities, or modify behavior, meaning a one-time approval covers a tool that has materially changed. Anthropic identifies this as one of three primary agent-specific threat vectors in their April 2026 framework.

Q:Do NIST standards cover AI agent security incidents?‍A:As of April 2026, six NIST standards and federal frameworks - including FISMA, SP 800-61, AI 100-2, AI 800-1, AI 600-1, and SP 800-218A - each independently scope out non-adversarial agent-caused harm. All seven illustrative incidents in NIST SP 800-61 Rev. 3 (revised April 2025) begin with "an attacker," and none address autonomous agents making mistakes within authorized scope. NIST's January 2026 RFI on AI Agent Security received 932 public comments, indicating updated standards are in development. (Analysis byIlya Kabanov.)

Q:What is persistent memory poisoning in AI agents?‍A:Persistent memory poisoning is an attack where corrupted information is injected into an AI agent's stored context. The agent later retrieves this poisoned memory, trusts it as its own records, and acts on the corrupted data - for example, a code review agent whose stored "approved patterns" have been modified to whitelist dangerous constructs likeeval()on user input. This attack bypasses point-in-time input validation because the malicious payload is already inside the agent's trust boundary when it's retrieved.

Q:What is the difference between Anthropic's framework and the cloud shared responsibility model?‍A:Both follow the same principle - the provider secures the infrastructure (cloud/model), while the customer secures their usage (configuration/tools/environment). The key difference is that AI agents introduce stateful behavior, tool autonomy, and multi-agent communication that cloud workloads don't have. A cloud VM doesn't remember yesterday's instructions, independently decide to call a third-party API, or pass outputs to another VM that trusts them blindly. AI agents do all three. This creates two responsibility surfaces with no direct equivalent in traditional cloud security: the harness layer (governing agent behavior through instructions and policies) and the tools layer (managing MCP servers, APIs, and plugins that agents access independently and that can change after initial approval).

Q:How should organizations implement security controls based on Anthropic's security model?‍A:Map your organization against the four layers: which models (Layer 1), what instructions and who wrote them (Layer 2), what MCP servers are connected and when they were last reviewed (Layer 3), and what data agents can reach (Layer 4). Then shift from per-action approval to plan-level governance, and invest in agent security tooling that governs and monitors these layers continuously - because tool supply chain changes, harness configurations, and environment context don't stay static long enough for manual audits to keep up.

‍

Additional Sources:

* Anthropic - "Trustworthy Agents in Practice" (April 2026)
* Anthropic - "Our Framework for Developing Safe and Trustworthy Agents" (August 2025)
* Anthropic - Claude Code Auto Mode Engineering Blog
* NIST RFI on AI Agent Security (January 2026)
* Ilya Kabanov / The Weather Report - Anthropic Trustworthy Agents Analysis
* OWASP Top 10 for Agentic Applications (2026)
* Deep Root Analytics Breach - Wired (2017)

Platform
* Vibe Coding Dashboard
* Secure AI Prompt Rules
* MCP Server Security
* IDE and Agentic AI Hardening
* AI Coding Security Assistant
Tools
* MCP Server Security Hub
* Skills Security Scanner
* Claw-Hunter
Resources
* Blog
* Vibe Coding Threat Model
Company
* News
* About Us
* Careers
* Partners
©2026 Backslash. 28 HaArba'a St., Tel‑Aviv
 
Privacy Policy
   |   
Terms of Use
Preferences

Privacy is important to us, so you have the option of disabling certain types of storage that may not be necessary for the basic functioning of the website. Blocking categories may impact your experience on the website.More information

Accept all cookies
Essential

These items are required to enable basic website functionality.

Always active

Marketing

These items are used to deliver advertising that is more relevant to you and your interests.

Personalization

These items allow the website to remember choices you make (such as your user name, language, or the region you are in) and provide enhanced, more personal features.

Analytics

These items help the website operator understand how its website performs, how visitors interact with the site, and whether there may be technical issues.

Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.

#### Open-Source Tool forOpenClaw Risk Discovery

Get it on GitHub