---
title: An MCP governance checklist for the CTO | Amir Pournasserian
url: https://pournasserian.com/writing/mcp-buyer-governance-checklist
site_name: tldr
content_file: tldr-an-mcp-governance-checklist-for-the-cto-amir-pourn
fetched_at: '2026-10-24T14:29:40.541827'
original_url: https://pournasserian.com/writing/mcp-buyer-governance-checklist
date: '2026-10-24'
published_date: '2026-10-24'
description: 'What a CTO has to decide before MCP servers reach a company''s AI tools: who controls each primitive, where the trust boundaries lie, which authorization model fits, and what the host must enforce.'
tags:
- tldr
---

# An MCP governance checklist for the CTO

October 24, 2026·Part 2 of 4

When a company connects its AI assistants to its systems through the Model Context Protocol (MCP), the decisions that matter most aren’t in any server’s code. They’re about which hosts employees use, who may approve what, how identity is managed, and what gets logged. This is the list I’d hand a chief technology officer (CTO): what the specification settles, what it leaves to you, and the policy each gap needs.

This is part 2 of a short series for the people who buy, approve and govern MCP servers rather than build them, afterpart 1 on what to require from a vendor. It draws on the same facts asmy series for builders, under the 2026-07-28 specification, as I read them in October 2026. MUST, SHOULD and MUST NOT in capitals are the specification’s words; where something is my advice, I say so.

MCP is an open standard that lets AI applications discover and use external tools, data and prompt templates through one common interface. A server connects a probabilistic system, the large language model (LLM), to deterministic systems that hold real data and take real actions, and that is where governance begins.

## In brief

1. Everything the model reads is potentially attacker-influenced,your vendors’ tool descriptions and instructions included. Most MCP security problems come from forgetting that.
2. Three primitives have three deciders.The model decides when a tool runs, the application when a resource is read, the user when a prompt is used. Your policy should say which mechanisms each server may use.
3. The host has duties the specification spells out:it SHOULD keep a human in the loop, confirm sensitive operations, show tool inputs before sending them, validate results, enforce timeouts and log tool usage, and it MUST treat a server’s annotations as untrusted unless the server is trusted.
4. Identity comes in four models, chosen by who is calling.Enterprise-managed authorization puts access under your identity provider, but as of October 2026 the mainstream hosts don’t list it, so pre-registered clients with core authorization are the practical option.
5. My advice: keep a register of approved servers with versioned definitions,separate reads from writes, write a policy for local servers, and look at what your hosts support every quarter.

## Where the risk enters

Picture four zones. Your users and their host, with its model, share one. A server, with its tool descriptions, instructions and skills, belongs to whoever operates it, which for a bought server is the vendor. Your APIs and databases sit in a backend zone of their own. The fourth holds untrusted content from outside: web pages, emails, tickets and documents. Data crosses between them at three boundaries.

Untrusted content: Web pages, emails, tickets, documents; Server operator zone: MCP server, Tool descriptions, instructions, skills; User's trust zone: User, Host + model; Backend trust zone: APIs, databases; Tool descriptions, instructions, skills – MCP server; Host + model – User; Web pages, emails, tickets, documents → MCP server: boundary 3: untrusted content enters tool output; MCP server → Host + model: boundary 1: definitions and outputs flow into the model's context; MCP server → APIs, databases: boundary 2: delegated credentials
Untrusted content
Server operator zone
User's trust zone
Backend trust zone
Web pages, emails,
tickets, documents
MCP server
Tool descriptions,
instructions, skills
User
Host + model
APIs, databases
boundary 3: untrusted content
enters tool output
boundary 1: definitions and outputs
flow into the model's context
boundary 2: delegated credentials

The first boundary is the one most policies miss. A tool description is text the model reads, so it can steer the model as well as describe a tool. These are the threats I’d plan for, with the side of the boundary that can do something about each. Where a mitigation is a requirement of the specification, its word is in capitals.

Threat
What happens
What the vendor’s server does
What your host does
Tool poisoning
Hidden instructions in a tool description or the server’s instructions steer the model
Keeps descriptions factual and reviews them like code
Shows definitions to users, flags suspicious text, treats annotations as untrusted
Rug pull
A server changes its tool definitions after a user approved them
Versions its definitions and announces changes
Asks for approval again when definitions change
Prompt injection through outputs
A document, email or web page a tool returns contains instructions
Marks fetched content as data and sanitizes outputs (MUST)
Separates untrusted content and confirms sensitive follow-up actions
Confused deputy and token passthrough
The server uses its own broad credentials, or forwards the user’s token, on the user’s behalf
Audience-bound tokens and on-behalf-of flows, never passthrough (MUST NOT)
Least-privilege scopes
Over-broad scopes
One token grants everything
A minimal set of scopes, plus step-up
Requests only the challenged scopes
Data exfiltration through arguments
The model is tricked into putting secrets into a call to an attacker’s server
Validates inputs (MUST)
Shows tool inputs before calling (SHOULD)
Local server compromise
A local server runs arbitrary code on the user’s machine
Signed releases, minimal dependencies
Trust prompts and sandboxing; as of October 2026, 
VS Code
 can sandbox local servers on macOS and Linux
Malicious skills
A skill tells the agent to run scripts or grant tools
Ships minimal, reviewable skills
Per-skill approval bound to file digests
Interface phishing
An MCP App shows misleading content
Honest interfaces, minimal Content Security Policy domains
Sandboxed iframes, clear boundaries
Resource exhaustion
Runaway loops, huge outputs, floods of tasks
Rate limiting (MUST), output caps, per-caller quotas
Timeouts and output limits

Half of that table is the host’s job, which is why the choice of host is a governance decision. The specification says a client SHOULD keep a human in the loop, confirm sensitive operations, show tool inputs before sending them, validate results, enforce timeouts and log tool usage. It MUST treat tool annotations, the hints a server gives about whether a tool only reads or may destroy something, as untrusted unless the server is trusted. When you evaluate a host, those are the behaviours to check.

## Who decides what

A server can offer three things, and they differ in who decides when each is used. Tools are functions with schemas, called by the model while it reasons. Resources are context identified by an address, which the application attaches or the user picks. Prompts are templates the user runs on purpose, as a slash command.

Model decides: Tools functions with schemas, tools/call, Model calls it while reasoning; Application decides: Resources context by URI, resources/read, Host attaches it as context; User decides: Prompts reusable templates, prompts/get, User runs a slash command; Tools functions with schemas → tools/call; tools/call → Model calls it while reasoning; Resources context by URI → resources/read; resources/read → Host attaches it as context; Prompts reusable templates → prompts/get; prompts/get → User runs a slash command
Model decides
Application decides
User decides
Tools
functions with schemas
tools/call
Model calls it while reasoning
Resources
context by URI
resources/read
Host attaches it as context
Prompts
reusable templates
prompts/get
User runs a slash command

Extensions add more: skills, which are workflow instructions with supporting files; MCP Apps, interactive interfaces rendered in the conversation; and tasks, long-running work the server runs on its own. Each mechanism carries a different kind of risk, so I’d decide, per server, which ones are allowed.

Mechanism
Who triggers it
Side effects?
The policy question
Tool
The model
Yes, potentially
Which tools may run without a person confirming?
Resource
The application or the user
No, read-only
What may be attached to a conversation, and from which servers?
Prompt
The user
No; it produces messages
Who may publish prompts your people will run?
Server instructions
The host, when it loads them
No
Who reviews the paragraph the model reads first?
Skill
The model or the user, after any approval
Only through the tools it uses
Who approves a skill, and what revokes that approval?
MCP App
The model, through a tool
Through the tools the app may call
Which servers may render interfaces, and may an app call tools without consent?
Task
The server, per request
Yes, potentially
How long may work run unattended, and who can cancel it?

My advice for tools is simple: separate read tools from write tools, and give writes clear, honest names. A host can then approve reads quietly and confirm writes, which keeps a person in the loop without burying them in prompts.

## Which identity model fits

Core MCP authorization pictures one person in a browser, approving one client for one server. That fits consumers; in a company it causes friction and gaps. Employees shouldn’t have to understand every server’s authorization details, security teams can’t enforce one policy, and onboarding and offboarding mean authorizing, then revoking, dozens of services by hand. Two official extensions cover what the core handles poorly, and the right model depends on who is calling.

Who is calling the MCP server? → Is a human user present?; Is a human user present? → Is access governed centrally by an enterprise IdP?: yes; Is access governed centrally by an enterprise IdP? → Enterprise-Managed Authorization with an ID-JAG: yes; Is access governed centrally by an enterprise IdP? → Core MCP authorization authorization code + PKCE: no; Is a human user present? → Local process on the user's machine?: no; Local process on the user's machine? → stdio: credentials from the environment: yes; Local process on the user's machine? → OAuth Client Credentials prefer JWT assertions: no
Who is calling the MCP server?
Is a human user present?
Is access governed
centrally by an
enterprise IdP?
Enterprise-Managed
Authorization
with an ID-JAG
Core MCP authorization
authorization code
+ PKCE
Local process on the
user's machine?
stdio: credentials
from the environment
OAuth Client Credentials
prefer JWT assertions
yes
yes
no
no
yes
no

Model
Who it serves
Status, October 2026
Core authorization, an authorization code with Proof Key for Code Exchange (PKCE)
A person authorizing a client for a server
Part of the specification
Enterprise-Managed Authorization
A person whose access the company’s identity provider (IdP) governs
Stable extension; the official 
client matrix
 lists it in Archestra.AI and Apify’s mcpc command-line client, and no mainstream chat or IDE host
OAuth Client Credentials
A job with no person present: a pipeline, a scheduled task, a service
Draft extension; listed in mcpc
Credentials from the environment
A local server on the user’s own machine
The specification’s rule for stdio

Enterprise-managed authorization is the one to watch. The organization’s IdP (Okta, Microsoft Entra ID or a corporate single sign-on system) becomes the decision-maker: the user signs in to the host with corporate single sign-on (SSO), the host trades that sign-in for an Identity Assertion JSON Web Token (JWT) Authorization Grant (ID-JAG) at the IdP, and exchanges the grant for an access token, with the IdP applying its policy on groups, roles and conditional access before anything is issued. What the organization gets is central policy, one sign-in, enforcement before a token exists, revocation in one place and an audit trail. It needs support on the IdP’s side as well as in the host, so check with your IdP vendor.

For callers with no person present, the client-credentials extension allows two credential formats, and the guidance prefers a signed JWT assertion to a client secret: the private key stays with the service, the assertion lives minutes, and a leak gives a limited window rather than silent impersonation until someone rotates the secret.

Whatever the model, two rules from part 1 hold: a server validates every token’s audience, and it never forwards your token to another system. If Entra ID is your IdP, expect clients to be pre-registered, since as of October 2026 it supports neither open Dynamic Client Registration nor Client ID Metadata Documents.

## Approvals for skills, apps and local servers

Skills are the mechanism with the clearest approval rules. TheSkills extensionlets a host gate loading behind approval, per skill or per server, and makes approval mandatory for four things: running code on the host, granting tools through anallowed-toolslist, reading files across servers, and activating a nested skill. A host MUST verify every file it loads against the digest the server published, and a persisted approval binds to the complete set of files, so any changed, added or removed file revokes it. A host MUST NOT fetch skill files ahead of need, MUST stop same-named skills from silently replacing each other, and tags loaded content with the server it came from. Those are the behaviours I’d check in a host, and the reason a skill’s approval is worth recording.

MCP Apps run in a host-controlled sandboxed iframe with a Content Security Policy built from the domains the server declared; the host may tighten it and MUST NOT loosen it, and SHOULD log the policy for audit. The host decides what an app may do: it may restrict which tools the app can call, disable link opening, or require the user’s consent before forwarding a tool call. A tool an app calls on its own behalf can be hidden from the model altogether. The policy question is which servers may render interfaces at all, and whether an app’s tool calls need consent.

Local servers trade operational simplicity for supply-chain and trust concerns, because they run code on the user’s machine. If you allow them, my advice is to require signed, versioned packages with minimal dependencies, secrets read from the environment, and the host’s sandboxing where it exists. A local HTTP server should bind to localhost and validate theOriginheader, or a web page can reach it.

## The checklist

Each row is a decision I’d want written down before the first server is approved.

Decision
What to write down
Hosts
Which AI applications are approved, and which of the host duties above each one performs
The register
Every approved server, with its tool definitions and instructions as reviewed, versioned, and re-approved when they change
Reads and writes
Which tools run without confirmation, and that writes always confirm
Mechanisms
Per server: tools, resources, prompts, instructions, skills, apps, tasks, each allowed or not
Identity
The authorization model per server; scopes kept minimal; no token passthrough, in the contract; how access is revoked
Approvals
Who approves a skill, and that approval dies with any changed file; which servers may render apps, and whether app tool calls need consent
Logging
Tool usage logged by the host; trace context continued end to end; an audit record of the caller, the tool, a hash of the arguments and the outcome
Limits
Rate limits, output caps and timeouts, on the server and in the host
Local servers
Allowed or not; if allowed, signed packages, sandboxing, secrets from the environment
Review
A look at what the hosts support every quarter, and the server’s own telemetry as the record of which hosts use it

## Method and caveats

* Built from my guide to MCP servers, written against the 2026-07-28 specification, and reframed for the people who govern a deployment. The builder series has the detail behind each row; product facts, such as which hosts list an extension, are as of October 2026.
* The MUST, SHOULD and MUST NOT marks are the specification’s or its extensions’. The zones, the policy questions and the checklist are my way of organizing the decisions, not a list from the specification.
* Everything here is framed from the specification. It describes no particular company, vendor or deployment.