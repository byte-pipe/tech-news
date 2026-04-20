---
title: AI coding agents are running on your machines — Do you know what they're doing? | Sysdig
url: https://www.sysdig.com/blog/ai-coding-agents-are-running-on-your-machines-do-you-know-what-theyre-doing
site_name: tldr
content_file: tldr-ai-coding-agents-are-running-on-your-machines-do-y
fetched_at: '2026-03-26T01:01:30.420653'
original_url: https://www.sysdig.com/blog/ai-coding-agents-are-running-on-your-machines-do-you-know-what-theyre-doing
date: '2026-03-26'
description: Runtime security is critical for AI coding agents. Sysdig TRT analyzes Claude, Gemini, and Codex at the syscall level to detect prompt injection, credential theft, and agent abuse.
tags:
- tldr
---

< back to blog

# AI coding agents are running on your machines — Do you know what they're doing?

Published by:
Miguel Hernández
@
linkedin
Alessandro Lo Prete
@
linkedin
Get a demo
Published:
March 23, 2026
Table of contents
falco feeds by sysdig

## Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered.

learn more

AI coding agents are now running on developer laptops and insideCI/CD pipelinesacross every sector. They write code, execute commands, read files, and make network connections, often without the developer watching. Unlike almost every other piece of software on those same machines,there is no established detection layer that understands what normal agent behavior looks like, let alone what an attack looks like at that level.

TheSysdig Threat Research Team (TRT)set out to build that layer. This article covers what we found and why runtime security is a fundamental layer in approaching the security of these tools.

## What we saw when we looked

We set out to understand what it would take to detect these agents — and what they look like to a defender. We started with their surface-level properties, then instrumented environments running each of the three major agents and captured their behavior at the syscall level using Sysdig and Falco.

At a high level, the security-relevant characteristics are straightforward. Each agent stores sensitive state in a predictable location — a config directory in the user's home folder (`~/.claude/`, `~/.gemini/`, `~/.codex/`) containing API tokens, session data, and settings. These directories are accessible to any process running under the same user. Agents typically operate with the invoking user's full OS-level permissions, with no capability restriction beyond the agent's own application-level safety controls. The agent's judgment — and whatever sandbox it implements — is the only gate between a prompt and a privileged system operation.

To build detection beyond these surface properties, we moved to the syscall layer. Here, a different picture emerges — one that is not visible from the agent's user interface or logs.

### Three agents, three runtimes

While the three agents share a common agentic loop architecture,each presents a different process-level fingerprint. Claude Code runs as a bundled Bun binary — its orchestrator process resolves to a Bun executable at an installation-specific path. Gemini CLI executes as a Node.js script, meaning its orchestrator resolves to the system's shared Node interpreter. Codex CLI compiles to a standalone Rust binary with a unique executable path. These differences make an agent-agnostic approach to process identification impractical and required us to map the specifics of each installation to reliably identify agent activity with Falco rules.

### The agentic loop

All three agents follow a common execution pattern. The agent runtime maintains a persistent connection to its LLM API. When the model decides to use a tool — run a command, read a file, make a network call — the agent deserializes the instruction, spawns a short-lived shell to execute it, collects the result, and sends it back to the API. The model then decides what to do next. This cycle repeats until the model produces a final response.

From the syscall layer, this manifests as a distinctive and repeating sequence of events:

In a captured session, we observed five iterations of this loop in 10 seconds — each spawning a disposable bash shell that executed a single command and exited, with an API callback between every iteration. The developer saw a single response. The kernel saw 64`execve`events, multiple outbound HTTPS connections, and a process tree several levels deep.

## Three reasons that make this a different kind of security challenge

The security challenge posed by AI coding agents is not simply "another application to monitor." It differs from conventional endpoint security in ways that matter for detection engineering.

### Agents are structurally vulnerable

LLM-powered agents share a well-understood architectural limitation: there is no robust separation between instruction and data. The same natural-language channel that carries user intent also carries untrusted content — repository files, error messages, and dependency documentation. An attacker who can inject content into any source the agent reads can redirect its behavior. This is not a bug in a specific agent; it is a structural property of how current LLM architectures process input.

Prompt injection does not require network access, exploits, or elevated privileges. A malicious comment in a code file or a poisoned dependency README can be sufficient to cause the agent to access credentials, exfiltrate data, or modify its own configuration.

### Built-in sandboxes operate in the wrong trust boundary

Each agent implements internal safety controls — permission prompts, filesystem sandboxing, and approval workflows. These are useful for a defense-in-depth approach, but they are fundamentally limited because they operate within the agent's own process, enforced by the agent's own code. Recent incidents have demonstrated that agents can access sensitive files despite sandbox restrictions, circumvent their own permission systems, or manipulate configuration to escalate capabilities. A successfully manipulated agent may disable its own safety controls as part of the attack.

This is not a criticism of the engineering behind these controls. It is a statement about trust boundaries: an application-level sandbox cannot protect against threats that operate at the same privilege level as the sandbox itself.

### From deterministic programs to prompt-driven actors

Conventional runtime security monitoring relies on the premise that a program’s executable logic defines its functional limits. Even for complex software, behavioral baselines can generally be established because the program’s code governs the range of possible actions.

AI coding agents do not fit this model well. An agent can read any file, spawn any process, and make any network call the invoking user has access to. Its behavior is determined not by its code but by its prompt, which changes with every interaction. In this respect, agents are closer to interactive users than to conventional programs. They are general-purpose actors whose access patterns cannot be predicted from the binary alone. This complicates the standard approach of defining what a programshoulddo and alerting on deviations, since for agents the space of legitimate behavior is, by design, very broad.

### The case for kernel-level observation

The considerations above — structural vulnerability to prompt injection, limited reliability of application-level sandboxes, and the difficulty of establishing behavioral baselines — suggest that monitoring agent behavior requires observability at a level the agent itself cannot influence.

Syscall-level instrumentation through eBPF, which underpins Falco and Sysdig's runtime detection engine, already provides this for conventional workloads. It captures system events across the entire process tree, operates independently of the monitored application, and exposes process ancestry for attribution. Many existing detections — reverse shells, data exfiltration patterns, privilege escalation sequences — apply to agent-initiated activity without modification.

Therefore, we prioritized covering the gap: the novel attack surface that using agents introduces.

## Mapping threats to observable behavior

The threat model for AI coding agents is still forming. New attack techniques, tooling, and real-world incidents are being documented at a pace that challenges the industry ability to proactively respond to them. To promptly devise our detection strategy, we identified four observable behaviors that represent high-confidence indicators across the attack scenarios documented so far. Each corresponds to a specific detection rule and targets a behavior that is observable at the syscall layer, regardless of the attack's origin or sophistication.

There is one key design principle we took into consideration when building the new detection coverage: detection is anchored to the observable behavior, not to the attack vector that produced it. Prompt injection, context poisoning, and MCP server exploitation are distinct attack methods, but at the syscall layer, they may converge at the same outcome — an agent process reading a file it should not. This principle is what makes the detection durable across attack variants.

### Agent manipulation via prompt injection

The most widely documented attack class against coding agents so far is prompt injection: adversarial instructions embedded in content the agent processes such as repository files, error messages, dependency documentation, and MCP server responses. The agent interprets the injected instruction as part of its task and acts on it.

The consequence we detect is not the injection itself — that occurs within the LLM's inference, outside the kernel's visibility - but the resulting system-level behavior. In fact, a manipulated agent must still issue syscalls to carry out the attacker's intent: reading credential files, spawning unexpected processes, opening network connections, accessing other agents' configuration directories.

This attack pattern is already being exploited. PromptArmor documentedindirect prompt injection against Slack AI(ATLAS AML.CS0035), where instructions embedded in messages caused credential exfiltration. Backslash Security documented adirect attack on Cursor IDE via a malicious MCP server(ATLAS AML.CS0045), where prompt injection executed a shell command that exfiltrated credentials via curl. Projects such as thePrompt Injection Attack Classification Systemmaintain a growing catalog of similar techniques. In each case, the attack culminates in observable syscall-level activity — process spawning, file reads, outbound connections — that our rules are designed to detect.

### Credential theft targeting agent configuration

Agent configuration directories contain API tokens that provide direct access to LLM accounts, conversation history, and in some cases billing infrastructure. These tokens are stored in predictable paths within the user's home directory — a property that makes them straightforward targets for any process running as that user.

Our detection targets a different boundary than the previous category: here, the threat isexternal to the agent. Any process outside the agent's own process family that performs file I/O on the agent's config directory triggers this detection. This is anchored to the unauthorized access itself — it fires regardless of the tool used, its origin, or what it does afterward.

The downstream implications of stolen agent credentials are becoming clearer. In July 2025, Microsoft DART documentedSesameOp(ATLAS AML.CS0042): malware that used the OpenAI Assistants API as an encrypted command-and-control channel. This was the first confirmed case of an LLM API repurposed for covert C2. Operators deleted API artifacts post-operation to cover tracks. A compromised developer machine with agent credentials already present gives attackers a pre-authenticated channel to LLM APIs without needing to provision their own.

### Safety control bypass

Each agent provides command-line flags that disable built-in safety controls — permission prompts, sandboxing, and approval workflows. These flags are intended for automation in trusted environments, but they can be exploited by anyone who can influence how the agent is launched: a compromised shell alias, a modified CI configuration, or a manipulated environment variable.

This is the most straightforward detection in the ruleset: match on proc.cmdline for known unsafe flags at agent invocation. It is also the most immediately actionable — the alert fires before the agent executes any operations, providing an opportunity to intervene before downstream impact occurs.

We consider this a starting point for sandbox-related detection. Deeper research into behavioral patterns of sandbox evasion — agents circumventing their own safety controls through indirect means rather than explicit flags — is an area of ongoing investigation.

### Agent presence on infrastructure

Before detecting agent-specific threats, it is necessary to know that agents are present. Installation detection provides an asset inventory baseline. This detecition fires when package managers, download tools, or installer scripts spawn processes that match agent installation signatures.

This is an informational rule but it serves a foundational role. Organizations that do not expect AI coding agents on their infrastructure can treat any installation event as an unauthorized deployment. Those that do can use it for inventory and compliance tracking.

## Building detection that understands agents

Our detection strategy follows directly from the observations and threat model above. We do not attempt to interpret what an agent intends to do, or to classify prompts as benign or malicious. Instead, we treat agents as what they are at the OS level — privileged processes with observable behavior — and apply the same principle that has guided runtime security for conventional workloads: define what should not happen, and detect when it does.

The first challenge is attribution. An agent does not announce itself in the process table. A Bun binary, a Node interpreter, a Rust executable — none of these are inherently identifiable as AI agents without understanding the specific installation paths and process ancestry chains that distinguish them from other software using the same runtimes. Solving this identification problem per agent, across their various installation methods, is a prerequisite for everything else. Without reliable attribution, agent-specific detection is not possible.

With identity established, the rules themselves are deliberately straightforward. Four behavioral patterns — installation, unauthorized config access, sensitive file reads, and safety control bypass — applied symmetrically across all three agents, mapped toMITRE ATT&CKand ATLAS, and tuned against production workloads. The complexity is not in the individual rules but in the infrastructure beneath them: the process identification layer, the multi-syscall-family coverage, and the exception framework that makes them deployable in environments ranging from developer VMs to Kubernetes clusters.

The four patterns we cover represent high-confidence, immediately actionable detections — but the full threat surface of agentic AI systems extends well beyond them. As the threat model matures, as new attack techniques are documented, and as agents gain deeper integration with cloud infrastructure, the ruleset will need to grow accordingly. The foundation we have built — per-agent process identification, production-tuned exceptions, systematic MITRE mapping — is designed to support that evolution. The rules are available to Sysdig Secure customers via the managed Falco rules feed.

## What’s coming: Expanding attack surfaces and the rise of the agent supply chain

As agentic systems scale and interconnect, their risk profile expands significantly.

Multi-agent pipelines amplify the impact of a single prompt injection, allowing compromised data to propagate across workflows. At the same time, the MCP ecosystem is emerging as a new kind of supply chain. A compromised server becomes a continuous channel for prompt injection or data exfiltration, not a one-time event. Early MCP vulnerabilities (CVE-2025-53109 and CVE-2025-53110) highlight that this risk is already materializing.

Detection must evolve accordingly. Behavioral profiling—understanding what normal agent activity looks like at the syscall level and flagging deviations—is a promising path, but still an ongoing challenge. This becomes even more critical as agents move from developer machines into CI/CD pipelines and cloud environments, where they often have access to sensitive credentials and production systems.

The combination of non-deterministic behavior, inherited OS permissions, and broad data exposure creates a risk threat model that existing defenses were not built to address.

The detection principle is durable: watch what agents do at the OS level, understand what normal looks like for each one, and treat deviations with the same seriousness you would give any other privileged process on your infrastructure.

Because that is exactly what these agents are.

## Appendix: Threat intelligence frameworks

### MITRE ATLAS

MITRE ATLAS(Adversarial Threat Landscape for Artificial-Intelligence Systems) extends ATT&CK with 16 AI-specific tactics and over 80 techniques, covering the full attack lifecycle for ML systems. The tactics most relevant to coding agents:

* AML.TA0004 — Initial Access: Supply chain compromise via malicious packages, slop-squatting, poisoned MCP servers
* AML.TA0005 — Execution: Indirect prompt injection (AML.T0051.001) via documents, web content, or MCP tool output; agent tool invocation (AML.T0053) abusing shells and APIs
* AML.TA0006 — Persistence: Memory poisoning (AML.T0080.000) across sessions; agent config modification (AML.T0081) to inject persistent instructions
* AML.TA0013 — Credential Access: Credentials from agent config files (AML.T0083) — API keys stored in `~/.claude/`, `~/.cursor/`, `~/.codex/`
* AML.TA0007 — Defense Evasion: Prompt obfuscation (AML.T0068) via base64, hidden HTML; LLM jailbreak (AML.T0054) bypassing safety guardrails
* AML.TA0014 — Command and Control: Reverse shells (AML.T0072); LLM APIs as covert C2 (SesameOp)

The ATLAS case study library (52 documented cases) includes AML.CS0045 (Cursor MCP), AML.CS0035 (Slack AI), and AML.CS0040 (ChatGPT memory poisoning) — documented attack chains that directly informed our detection logic.

#### ATLAS Case Studies — Real Incidents Relevant to Coding Agents

* AML.CS0035: Indirect prompt injection on Slack AI — embedded instructions caused credential exfiltration via deceptive URL rendering
* AML.CS0040: ChatGPT memory poisoning via indirect prompt injection in Google Doc — persistent cross-session instruction injection
* AML.CS0042: SesameOp (Microsoft DART) — real malware using OpenAI Assistants API as encrypted C2; first confirmed LLM API-as-C2 incident
* AML.CS0045:  Cursor + malicious MCP server — prompt injection executed base64-encoded shell command exfiltrating credentials from `~/.cursor/mcp.json`

### OWASP LLM Top 10

TheOWASP LLMTop 10 maps critical vulnerability classes in LLM-integrated applications. Three categories apply directly:

* LLM01 — Prompt Injection: Highest-priority risk. Covers direct and indirect injection. OWASP explicitly flags MCP servers and external tool integrations as high-risk injection surfaces.
* LLM06 — Excessive Agency: Agents with more permissions or autonomy than their task requires amplify every other vulnerability. Maps directly to our safety bypass detection pattern.
* LLM08 — Vector and Embedding Weaknesses: Poisoned RAG databases become persistent injection channels for agents with retrieval capabilities.

### Google Secure AI Framework (SAIF)

Google SAIFidentifies behavioral monitoring of AI systems as a required security control. Two of its six core elements align directly: *Extend detection and response to bring AI into an organization's threat universe* and *Automate defenses to keep pace with existing and new threats* — consistent with our conclusion that runtime security is the only effective detection layer for non-deterministic agent behavior.

## About the author

Security for AI
Cloud detection & response
Cloud Security
featured resources

## Test drive the right way to defend the cloud with a security expert

GET A DEMO
