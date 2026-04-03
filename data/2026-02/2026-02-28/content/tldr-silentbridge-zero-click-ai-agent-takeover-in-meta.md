---
title: 'SilentBridge: Zero-Click AI Agent Takeover in Meta Manus'
url: https://aurascape.ai/resources/auralabs-research/silentbridge-zero-click-agent-takeover-meta-manus/
site_name: tldr
content_file: tldr-silentbridge-zero-click-ai-agent-takeover-in-meta
fetched_at: '2026-02-28T11:07:48.622034'
original_url: https://aurascape.ai/resources/auralabs-research/silentbridge-zero-click-agent-takeover-meta-manus/
author: Aurascape
date: '2026-02-28'
published_date: '2026-02-24T22:53:56+00:00'
description: SilentBridge is a zero-click indirect prompt injection class in Meta Manus that turns normal actions like “summarize this” into tool abuse, data exfiltration, and sandbox compromise.
tags:
- tldr
---

AuraLabs Research

### Critical Vulnerability in Meta Manus AI Agent Enables Zero-Click Indirect Prompt Injection Attacks

Aurascape Auralabs exposes a security vulnerability, named SilentBridge where everyday workflows can quietly inherit the risk of the tools and data they are allowed to access.

 

Qi Deng, Principal Threat Research Engineer | AurascapeFebruary 24th, 2026

🕑 25 minute read

## Introduction

Aurascape AuraLabs security researchers recently conducted a security assessment of Meta’s Manus Agent, an autonomous AI agent acquired through Meta’s acquisition of Manus.

Meta’s Manus Agent integrates high-privilege capabilities—such as web browsing, code execution, and third-party connectors (for example, Gmail)—into an autonomous AI assistant designed to operate across user data and external content.

During this assessment, we identified aseries of critical zero-click vulnerabilities, which we collectively refer to asSilentBridge. These vulnerabilities arise fromindirect prompt injection, where hidden instructions embedded inuntrusted content—including web pages, documents, and search results—are silently ingested by the agent and allowed to influence high-privilege tool invocation.

We identified multiple SilentBridge variants, each representing a distinct attack surface:

* SilentBridge-Page (CVSS v3.1 9.8 – Critical)Indirect prompt injection delivered through ordinary web pages, which can be exploited zero-click to compromise the agent sandbox, exfiltrate sensitive data via privileged connectors (such as Gmail), and escalate to root-level control within the agent environment.
* SilentBridge-Search (CVSS v3.1 9.8 – Critical)Prompt injection delivered via search engine results consumed during routine “research” workflows, enabling remote agent takeover, connector-driven data exfiltration, and root-level execution without explicit user intent.
* SilentBridge-Doc (CVSS v3.1 9.8 – Critical)Document-based indirect prompt injection that transforms a benign file-summarization request into zero-click agent compromise, including arbitrary code execution, root-level control inside the agent sandbox, and access to high-sensitivity connectors.

Across these variants, we demonstrated end-to-end exploit chains in which a seemingly harmless user action—such as clicking“Summarize this page”or asking the agent“Help me research <keyword>”—resulted in full compromise of the agent and its surrounding infrastructure. In practice, this enabled:

* Email Data Theft:Exfiltration of sensitive Gmail content via Manus’s email connector.
* Secret Leakage:Extraction of internal secrets, including API keys, internal endpoints, and customer-related data from within the agent container.
* Remote Code Execution:Execution of arbitrary code and establishment of a root-privileged shell inside the agent’s runtime.
* Infrastructure Exposure:Public exposure of internal code-server tooling, enabling arbitrary command execution via a browser.
* Cross-Tenant Access:Unauthorized access to other customers’ media files through a public, unauthenticated CDN.

Notably, none of these attacks required explicit malicious input from the user. The agent was compromised entirely throughnormal, expected interactions, while untrusted content silently bridged the gap between passive data ingestion and high-impact actions.

We responsibly disclosed these SilentBridge vulnerabilities to the Manus security team, who implemented mitigations prior to this publication. This post details the SilentBridge vulnerability class, how each variant operates, why these flaws are particularly dangerous in agentic AI systems, and what their existence implies for the broader industry as AI agents become deeply embedded in enterprise workflows.

We score SilentBridge-Page, SilentBridge-Search, and SilentBridge-Doc asCVSS v3.1 9.8 (Critical)(AV:N/AC:L/PR:N/UI:N/C:H/I:H/A:H) because each variant can be exploited zero-click to achieveroot-level agent compromiseandsensitive data exfiltrationvia privileged connectors. In deployments where the agent’s tools/connectors are treated as separate security authorities, the class can also be reasonably interpreted asScope Changed(up to10.0).

## Background: SilentBridge and the Risk of Indirect Prompt Injection

Prompt injection is no longer limited to adversarial chat messages or obvious attempts to manipulate a model’s output. In modernagentic AI platforms, large language models function as autonomous controllers that continuously ingestexternal contentand translate it intohigh-privilege actions.

Today’s AI agents routinely:

* Browse and parse web pages and search results
* Open and summarize documents and files
* Invoke tools and APIs
* Read emails and cloud documents through connectors
* Execute code and shell commands

As a result,any content an agent consumes—whether a web page, a document, or a search result—must be treated asuntrusted input. If a platform does not enforce a strong trust boundary between that untrusted content and the agent’s privileged capabilities, the content itself can become an unintended control channel.

We collectively refer to this class of vulnerabilities asSilentBridge.

SilentBridgedescribes a failure mode in which untrusted content silentlybridgesinto privileged execution paths inside an AI agent. Instructions embedded in otherwise ordinary content are absorbed into the agent’s reasoning process and used to drive tool invocation, data access, or code execution—without explicit user intent or visibility.

We categorize these vulnerabilities based on thesource of the untrusted content:

* SilentBridge-Page– Indirect prompt injection delivered through ordinary web pages visited by the agent.
* SilentBridge-Search– Prompt injection delivered via search engine results consumed during agent-driven research workflows.
* SilentBridge-Doc– Indirect prompt injection embedded in documents or files opened or summarized by the agent.

Although the delivery mechanisms differ, all SilentBridge variants share the same underlying weakness:untrusted content is allowed to influence high-privilege agent behavior without meaningful isolation or validation.

In practical terms, this collapses the intended security model into something like:

“Open this page or document”→ hidden instructions are ingested → privileged tools are invoked → sensitive data or infrastructure is affected

Crucially, these attacks requireno overtly malicious input from the user. The agent appears to be performing a normal task—such as summarizing a document or researching a topic—while quietly executing attacker-supplied instructions embedded in the content itself.

This SilentBridge pattern is exactly what we demonstrated in Manus.

## Attack Surface in the Manus Agent

Manus exposes a broad and powerful set of capabilities that are representative of many modern AI agent platforms. In our assessment, the Manus agent was able to:

* Browse the web via Google search and page retrieval
* Access Gmail through a first-party connector
* Execute arbitrary code and shell commands
* Expose internal developer tooling (such as a code server)
* Run inside a sandboxed container with environment variables, outbound network access, and access to real customer data flows

Our core research question was simple:

What happens when untrusted content—originating from pages, search results, or documents—is allowed to directly influence all of these capabilities?

SilentBridge provides the answer. Even when code execution occurs inside a sandboxed environment, the agent still has access to sensitive connectors, secrets, and infrastructure actions. As a result, compromising the agent through indirect prompt injection leads to real-world data exfiltration and external side effects.

The issue is not a single bug or misconfiguration, but asystemic trust-boundary failure. Without explicit isolation between untrusted content and high-privilege tools, AI agents become silent conduits through which external content can exert control over internal systems.

## SilentBridge-Page: Webpage-Based Indirect Prompt Injection Leading to Gmail Data Exfiltration

Scenario

We prepared an otherwise ordinary web page containinghidden prompt injection instructionsembedded in the page content. Separately, a user’s Gmail account was connected to Manus through the platform’s email connector.

To trigger the attack, we issued a single, benign request in the Manus chat interface:

“Summarize this page.”

No additional permissions, confirmations, or atypical user actions were required.

What Happened

When Manus retrieved the page to generate a summary, the agent ingested not only the visible text but also the hidden instructions embedded within the content. Those instructions directed the agent to:

* Query the connected Gmail account for messages matching sensitive patterns or keywords
* Transmit the extracted results to an attacker-controlled endpoint

Because the platform did not enforce a strict trust boundary between untrusted web content and high-privilege connectors, the agent executed these instructions without hesitation. A routine summarization request was silently transformed intounauthorized Gmail data access and exfiltration.

From the user’s perspective, the interaction appeared completely normal. Behind the scenes, however, untrusted web content had crossed a SilentBridge into a privileged connector, resulting in full Gmail-level data exposure.

Demo video:

Why This Matters

* The user never typed anything malicious.
* The website looked normal to the user.
* All the damage came fromuntrusted page contentsilently hijacking the agent.

This breaks the intuitive security model users have:“If I just click summary on a page, I shouldn’t lose my email.”

## Exploit 2 – Indirect Prompt Injection via Search Results

Scenario

Next, we moved the injection one step further away from the user.

* We prepared a website that ranks highly inGoogle search resultsfor a niche technical query (e.g., exploit payloads).
* In Manus, we asked the agent to “research” that keyword.

Manus then:

* Called Google search
* Followed the links
* Landed on our malicious page

What Happened

The manuscript of the attack:

* Thesearch result itselfwas the delivery vehicle.
* Manus, acting as a “research assistant,” visited the page and:
* Got silently prompt‑injected
* Was now under the attacker’s control, ready to run arbitrary tool calls

The user merely typed: “Help me research <topic>.”

This shows thatsearch engines become a powerful attack surfacein an agentic world—if your AI platform doesn’t defend against indirect prompt injection,any search query can become a backdoor.

## SilentBridge-Search: Indirect Prompt Injection Delivered via Search Results

Scenario

To demonstrate that indirect prompt injection does not require the user to interact with attacker-controlled content directly, we moved the delivery mechanism one step further away from the user.

We prepared a web page containing hidden prompt injection instructions and ensured that it ranked highly in Google search results for a niche technical query. In Manus, the user then issued a routine request:

“Help me research <keyword>.”

To fulfill this request, Manus automatically:

* Queried Google Search
* Followed one or more search results
* Retrieved and processed our attacker-controlled page

What Happened

In this scenario, thesearch result itself became the delivery vector.

While acting as a research assistant, Manus ingested the content of the retrieved page, including the embedded hidden instructions. Those instructions silently prompt-injected the agent, placing it under attacker influence and enabling arbitrary tool invocation without user awareness.

From the user’s perspective, nothing unusual occurred—they simply asked the agent to research a topic. In reality, untrusted content delivered through a search engine had crossed a SilentBridge into the agent’s high-privilege execution path.

This demonstrates that in agentic AI systems,search engines become a critical attack surface. Without defenses against indirect prompt injection, a single research query can act as a remote control channel, turning routine information retrieval into an entry point for full agent compromise.

Demo video:

After demonstrating SilentBridge attacks through web content and search results, we next targeted a more sensitive execution path:document processing combined with code execution inside the agent sandbox.

Scenario

We crafted a document that appeared entirely benign to the user, containing:

* Ordinary, user-visible text
* A hidden prompt instructing the Manus agent to execute an embedded Python script
* Python code designed to establish a reverse shell back to an attacker-controlled server

To trigger the exploit, the user performed a routine action:

“Please summarize this document.”

No warnings, confirmations, or elevated permissions were required.

What Happened

When Manus opened the document, the language model processed both the visible content and the hidden instructions embedded within it. Rather than limiting its behavior to summarization, the agent interpreted the hidden prompt as actionable guidance and proceeded to:

* Execute the embedded Python code automatically
* Initiate an outbound connection to the attacker-controlled server
* Establish an interactive reverse shell inside the agent’s sandboxed environment

Because the sandbox allowed passwordless sudo, this access quickly escalated toroot-level control within the agent container.

Once again, the trigger was an entirely ordinary workflow. A simple request to summarize a document silently crossed a SilentBridge, transforming untrusted file content into arbitrary code execution with full control over the agent runtime.

Demo video:

Again, the trigger was a completely ordinary workflow: “summarize this file.”

## SilentBridge-Doc: Prompt Injection Leading to Public Code Server Exposure and Root Command Execution

After achieving code execution inside the agent sandbox, we examined how the agent’sown operational toolscould be abused to further expand the attack surface. In particular, we focused on tools intended to expose developer-facing services for legitimate debugging and development workflows.

Scenario

We crafted a document containing hidden prompt injection instructions that directed the Manus agent to perform a sequence of high-privilege actions:

* Invoke Manus’s internal deploy_expose_port tool to expose an internal code server over a publicly accessible domain
* Read the code server’s authentication credentials from a local configuration file
* Construct a URL embedding both the public endpoint and its associated password
* Transmit this information to an attacker-controlled server

The user interaction required to trigger this chain was again minimal and routine:

“Summarize this document.”

What Happened

Upon processing the document, the agent executed the embedded instructions without restriction. As a result:

* The internal code server was exposed to the public internet
* The server’s access credentials were extracted and exfiltrated
* The attacker was able to access the code server directly through a web browser

From the code server interface, we were able to:

* Browse and modify arbitrary files within the agent environment
* Execute arbitrary shell commands
* Escalate to root within the agent container due to passwordless sudo configuration

The net effect was a complete compromise chain:

Malicious document → agent processes content → internal tooling exposed externally → attacker gains interactive, root-level control via browser

This exploit demonstrates how SilentBridge vulnerabilities can turn legitimate agent tools into attacker-controlled infrastructure, further amplifying the impact of indirect prompt injection beyond data access and into full operational control.

Demo video:

## Sensitive Data Exposure Inside the Agent Container

With root on the agent container, we analyzed the environment and traffic.

1. Secrets in Environment Variables

Running basic system commands inside the container exposed:

* API endpoints and API keysvia environment variables (e.g., an OpenAI‑compatible endpoint and its API key).
* The API endpoint was accessible from outside the container and appeared to lack meaningful restrictions.

This means a successful container compromise could enableunrestricted use of internal LLM APIswith the platform’s own credentials.

2. Sniffing Customer Traffic

Since we had root, we couldcapture and decrypt trafficwithin the container.

We observed:

* Requests uploading media toAmazon S3via presigned URLs
* Responses containing file paths and public URLs being written back into Manus’ infrastructure
* Detailed request/response metadata for search‑related features and media search flows

In practical terms, this means a compromised agent container can:

* Steal presigned S3 URLs
* Access customer media files
* Potentially tamper with data being processed by the agent

## Public Media CDN Without Tenant Isolation

During traffic analysis, we noticed that images processed by Manus were stored on apublic CDN domain.

We verified:

* Media URLs returned by the agent could be requested directly, unauthenticated.
* There wasno apparent tenant isolationat the CDN level—anyone with the URL could access the file.
* An attacker who can guess or obtain URLs (e.g., via compromised agents, logs, or browser history) could access potentially sensitive media belonging to other users.

While presigned URLs sometimes have expiry, the combination of…

* Public CDN paths, and
* Weak segmentation

….significantly increases cross‑tenant risk.

## Sensitive Manus Infrastructure Exposure

We also found clues that could be used to pivot further into Manus’ infrastructure.

Instance Metadata Access

From configuration files and startup scripts, we observed that Manus containers were accessing the typical metadata IP (169.254.169.254) to retrieve instance identifiers and write them into local files.

In some cloud environments, if not carefully locked down, metadata access can be abused for:

* Fetching credentials
* Getting environment‑level secrets
* Enumerating infrastructure

We did not exploit metadata in this research, but its presence alongside RCE is a serious red flag.

Internal 10.* Network

Traffic analysis also revealed communication between the agent container and10. internal IPs*, including:

* Hosts handling VNC access
* Hosts serving the code server

If an attacker controls the container, they can:

* If an attacker controls the container, they can:
* Craft malicious responses to those internal endpoints
* Exfiltrate data back into the 10.* network
* Potentially leverage trust relationships to move laterally inside Manus’ infrastructure

## Root Causes: How SilentBridge Emerges

Across all of the exploits we demonstrated—SilentBridge-Page, SilentBridge-Search, and SilentBridge-Doc—the same fundamental design failures repeatedly surfaced. These were not isolated implementation bugs, butsystemic trust-boundary violationsthat allowed untrusted content to silently influence high-privilege agent behavior.

1. Collapsed Trust Boundary Between Content and Capabilities

At the core of SilentBridge is the absence of a strong separation betweenuntrusted contentandprivileged tools.

Content sourced from web pages, search results, and documents was treated as if it were benign reasoning context, and was allowed to directly influence:

* Tool invocation
* Connector access
* Code execution
* Infrastructure-level actions

This allowed attacker-supplied instructions embedded in content to “bridge” directly into execution paths that were never intended to be driven by external input.

2. High-Risk Connectors Treated as Ordinary Tools

Sensitive integrations—such as the Gmail connector—were exposed through the same abstraction layer as low-risk tools. As a result:

* There was no meaningful separation of duties between content processing and data access
* Connector actions could be triggered indirectly by untrusted content
* Per-operation user consent and justification were not enforced

This allowed SilentBridge attacks to escalate from content ingestion directly into email data exfiltration.

3. Excessive Privilege in Agent Execution Environments

Although the agent executed code inside a sandboxed container, the sandbox itself wasover-privileged:

* Code execution and shell access were available by default
* Passwordless sudo enabled rapid escalation to root within the container
* The runtime had access to sensitive environment variables, internal services, and outbound network connectivity

Once SilentBridge enabled code execution, the sandbox became an amplification mechanism rather than a containment boundary.

4. Runtime Exposure of Secrets and Infrastructure Details

The agent runtime exposed high-value assets that should not have been accessible from content-driven execution paths:

* Long-lived API keys and internal endpoints in environment variables
* Access to instance metadata services
* Reachability of internal 10.* networks and developer tooling

These exposures significantly increased the blast radius of a successful SilentBridge exploit.

5. Media Handling Without Strong Tenant Isolation

Media generated or processed by the agent was stored on public CDN infrastructure without strict, tenant-aware access controls. This created opportunities for:

* Unauthorized access to other customers’ data
* Cross-tenant data leakage once URLs were discovered or exfiltrated

6. Lack of Prompt-Injection–Aware Design

Finally, Manus lacked systematic defenses against indirect prompt injection:

* Untrusted content was not classified or isolated
* Embedded instructions were not detected or neutralized
* Sensitive tool calls driven by external content did not require human confirmation

As a result, the agent could not distinguish between “information to summarize” and “instructions to execute.”

## Recommendations: Designing Against SilentBridge

While our research focused on Manus, SilentBridge is not platform-specific. Any agentic AI system that combines untrusted content ingestion with high-privilege capabilities is susceptible to similar failures unless deliberate safeguards are put in place.

We recommend the following architectural principles for AI agent platforms.

1. Explicit Trust Boundaries and “Untrusted Content” Mode

Treat all externally sourced content—web pages, documents, search results, emails—ashostile by default. Content ingestion must be isolated from:

* Code execution
* Connector access
* Infrastructure-level actions

Untrusted content should never be able to directly trigger high-impact tools without additional validation or human oversight.

2. Fine-Grained Tool and Connector Policies

High-risk connectors should not be exposed as generic tools. Platforms should enforce:

* Per-connector authorization policies
* Clear scoping of what data can be accessed
* Per-action consent or strong justification for sensitive operations

Connector calls influenced by external content should be heavily restricted or disallowed entirely.

3. True Least-Privilege Execution Environments

Sandboxing alone is insufficient if the sandbox is over-privileged. Platforms should:

* Run execution tools as non-root users
* Remove passwordless privilege escalation paths
* Separate “read-only” tools from “execute” tools
* Eliminate unnecessary access to metadata services and internal networks

4. Robust Secret Hygiene

Agent runtimes should never expose long-lived secrets to content-driven execution paths. Instead:

* Use short-lived, narrowly scoped credentials
* Enforce authentication and rate limits on internal APIs
* Assume agent compromise is possible and design accordingly

5. Secure Media Handling and Tenant Isolation

Media storage must enforce strict, tenant-aware authorization:

* Avoid public-by-default CDN paths
* Use per-tenant namespaces with signed, short-lived URLs
* Treat media URLs as sensitive artifacts

6. Prompt-Injection–Aware Agent Design

Finally, agent platforms must explicitly defend against indirect prompt injection by:

* Detecting and neutralizing instruction-like patterns in untrusted content
* Preventing content from overriding system intent or tool policies
* Requiring human confirmation when content attempts to trigger sensitive actions

## The Core Lesson of SilentBridge

SilentBridge demonstrates thattreating untrusted content as “just text” is no longer safein agentic systems. When LLMs are empowered to act, any ambiguity between data and instructions becomes a security liability.

Until AI platforms enforce explicit, policy-driven trust boundaries between content and capabilities, normal user workflows—like “summarize this document” or “research this topic”—will continue to serve as silent escalation paths for attackers.

## Disclosure Timeline

* 2025‑09‑15– Vulnerabilities discovered during Manus assessment.

* 2025‑09‑18– Initial report sent to Manus security team.

* 2025‑10‑05– Acknowledgement received from Manus.

* 2025‑11– Manus deploys mitigations/patches for critical issues.

* 2026‑02‑24 – This blog post published after coordinated disclosure window.

## Conclusion

Manus is not an outlier. The vulnerabilities we uncovered are symptoms of a broader structural problem in modern AI agent architectures. As LLM-driven agents are increasingly connected to code execution, enterprise connectors, and internal infrastructure, the long-standing assumption that untrusted content is “just text” no longer holds. SilentBridge demonstrates that in today’s agent designs, a routine request—such as“summarize this document”or“research this topic”—can silently cross trust boundaries and trigger a chain of high-impact actions.

Through responsible disclosure, we worked with the Manus team to address these issues before they could be exploited in the wild. However, the significance of SilentBridge extends far beyond a single platform. It highlights a systemic risk facing any agentic AI system that allows untrusted content to influence high-privilege behavior without explicit isolation, validation, or user awareness.

We hope this research serves as a catalyst for the industry to adopt stronger, security-first agent designs. AI platforms must treat indirect prompt injection as a first-class threat, enforce clear trust boundaries between content and capabilities, and implement prompt-injection-aware controls that prevent hidden instructions from driving sensitive actions. Least-privilege execution, connector-level authorization, and explicit user consent must become defaults—not afterthoughts.

At Aurascape, our focus is on making LLM trust boundaries explicit, enforceable, and policy-driven. We believe that as AI agents become deeply embedded in enterprise workflows, only deliberate control over how models interact with untrusted content, sensitive data, and high-risk tools will prevent normal user actions from becoming silent escalation paths. Without these safeguards, “summarize this” will remain one of the most dangerous prompts in modern computing.

To learn more,Contact Aurascape.

August 25, 2025

AuraLabs Research

#### Your Agent, My Shell: How We Got a Reverse Shell on OpenAI ChatGPT Agent Mode

January 15, 2026

At a Glance

#### AI Risk Assessment Checklist

## Aurascape Solutions

* Discover and monitor AIGet a clear picture of all AI activity.
* Safeguard AI useSecure data and compliancy in AI usage.
* Copilot readinessPrepare for and monitor AI Copilot use.
* Coding assistant guardrailsAccelerate development, safely.
* Frictionless AI securityKeep users and admins moving.