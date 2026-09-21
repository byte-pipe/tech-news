---
title: 'AI agent credentials: Four architectures compared — WorkOS'
url: https://workos.com/blog/agent-credential-architectures
site_name: tldr
content_file: tldr-ai-agent-credentials-four-architectures-compared-w
fetched_at: '2026-09-21T16:50:10.146220'
original_url: https://workos.com/blog/agent-credential-architectures
date: '2026-09-21'
description: Google, NVIDIA, Rubrik, Microsoft and Opal each solve agent credentials differently. What each one protects against, and the gap they share.
tags:
- tldr
---

In this article
September 21, 2026
September 21, 2026

# AI agent credentials: Four architectures compared

Google, NVIDIA, Rubrik, Microsoft and Opal each solve agent credentials differently. What each one protects against, and the gap they share.

Maria Paktiti
September 21, 2026
Explore with AI

Open in ChatGPT

Open in Claude

Open in Perplexity

Every team that has put an AI agent into production has hit the same wall. The agent needs to call GitHub, or a private API, or an MCP server that reaches real data. Something has to authenticate that call. And the thing doing the calling is a language model running arbitrary code in a sandbox, which is a poor place to keep a secret.

Over the past two months, five vendors have shipped four distinct architectures for agent credentials. Google and NVIDIA keep the secret out of the sandbox entirely. Rubrik mints a token per tool call. Microsoft inspects the MCP protocol on the wire. Opal decides each request and delegates enforcement. These are not variations on a theme: they intervene at different layers, and they protect against different failures. If you are designing agent infrastructure, the useful exercise is not picking the best one. It is working out which failure each one actually removes, because most of them leave a specific gap, and it is the same gap in almost every case.

Where each approach intervenes in a single tool call. Only the last layer is a check the resource server performs itself.

## The placeholder and the proxy: Google and NVIDIA OpenShell

Google'sManaged Agents in the Gemini APItake the most direct route: the credential never enters the agent's environment at all.

You store a secret once through the API. It is write-only, so no endpoint will return it, which means a compromised agent cannot read back the tokens it is using. You then reference it by ID on a network allowlist rule. At request time, an egress proxy resolves the reference and injects the header on the wire.

Where it gets interesting is the environment variable case. If an agent's SDK expects to read a token fromprocess.env, the variable is still populated, but with a placeholder string rather than the secret. The proxy swaps in the real value only for requests headed to a domain in that credential'strusted_domains. A request carrying the placeholder to any other host is rejected rather than forwarded, so the secret never crosses the perimeter and the placeholder does not leak in its place. Google is explicit that literal values are a different thing entirely: those are readable by anything in the sandbox, and belong to config likeNODE_ENV, not to secrets.

The OAuth2 credential type goes a step further. The proxy holds the refresh token, exchanges it, and refreshes access tokens as they expire, so a long-running agent session does not break mid-task when a token ages out. Creating the credential performs a live token exchange to confirm the configuration works before storing it.

NVIDIA's OpenShellimplements the same shape, with more of the sharp edges filed down. Credentials are first-class objects called providers, attached explicitly per sandbox at creation time. There is no inheritance from the host environment. A provider cannot be attached to a running sandbox, so credential scope cannot be widened after the fact, and everything is purged when the sandbox is deleted.

Two details in OpenShell are worth stealing regardless of what you are building.

The first is that the binding is to an endpoint, not just a domain. A static credential resolves only when the request host, port and path match an endpoint in the provider's profile. Send the built-inGITHUB_TOKENplaceholder to a host your policy otherwise allows, and the proxy returns a 403 with reasoncredential_endpoint_mismatch, records a denied event, and logs none of the secret, placeholder or query string.

The second is that OpenShell assumes the agent will try to go around the proxy. Seccomp blocks raw socket syscalls specifically because those are the paths that bypass it, and a network namespace forces ordinary egress through a local CONNECT proxy. A proxy you can route around is a suggestion.

OpenShell also does real token exchange rather than simulating it. Provider profiles can declare dynamic token grants, where the supervisor obtains or exchanges OAuth2 tokens per matching endpoint.client_credentialsgrants use the supervisor's SPIFFE JWT-SVID as the client assertion.token_exchangegrants have the gateway broker an intermediate token using its own JWT-SVID, which the supervisor then exchanges for the final upstream token. The gateway validates the audience, the SPIFFE subject, the expiry, and that both SVIDs sit in the same trust domain. That is a workload identity chain, not a secret store with a proxy in front of it.

## A token per tool call: Rubrik Agent Identity

Rubrik Agent Identity, announced at Black Hat on August 4, attacks a different problem. The agent does hold a credential. It just holds one that is worth almost nothing.

Enforcement sits at an MCP gateway, and every tool call clears three checkpoints before it executes. Rubrik's SAGE engine performs behavioural analysis on the request's intent, parameters and likely impact. A policy check runs at the infrastructure layer. Then an identity step authenticates the agent session and mints a token scoped to that single call. An unauthorised write outside explicit policy scope is blocked before execution rather than caught afterward.

The part that matters most for anyone doing identity work is the federation model. Access is scoped to servers and tools by user and group using On-Behalf-Of federation, which extends the identity structures an organisation already has rather than replacing them, with RBAC parity between agents and humans. The agent cannot exceed the permissions of the user behind it.

Rubrik MCPfollowed on September 15, co-engineered with Anthropic, exposing the Rubrik Security Cloud API schema to connected agents with OWASP MCP Top 10 aligned guardrails. It is in private preview, with general availability targeted for October.

## Inspect the protocol instead: Microsoft Entra and the GSA MCP firewall

Microsoft'sGlobal Secure Access MCP firewall, in public preview, is the outlier: it does not handle credentials at all.

It is a network control that inspects MCP traffic, specifically JSON-RPC 2.0 over streamable HTTP and Server-Sent Events, and enforces allow or block decisions on what it sees. You can deny all MCP traffic tenant-wide until you have approved a set of servers. You can allow or block servers by URL pattern. You can permit or deny individual primitives, tools, resources and prompt templates, on a per-server basis. You can block specific methods, unencrypted HTTP transport, and outdated protocol versions. Policies attach to a Global Secure Access security profile and are enforced through Conditional Access.

Microsoft makes a reasonable claim here: this extends identity-based access, Conditional Access and Continuous Access Evaluation to the MCP protocol layer without requiring any change to the spec, or to client, host or server implementations. That is a genuine advantage over every approach that needs the server rebuilt.

It also has two hard limits, both in the docs. It needs TLS inspection turned on, because MCP rides inside HTTPS and the firewall cannot see the method or tool otherwise. And it only covers remote servers on HTTP transports. Anything over stdio does not traverse Global Secure Access and is not covered, which excludes most of what developers run locally today.

## Decide the request, delegate the enforcement: Opal Zero

Opal Zero, launched September 17 with general availability at the end of the month, makes an argument the others do not: the decision and the enforcement should be separate jobs.

An agent files a request through Opal's MCP server. Paladin, Opal's reasoning model, evaluates it against written policy and organisational context, including who owns the agent, what it was built for, and whether the request reaches past what the owner themselves holds. It shows its reasoning and leaves an audit trail.

Then it does something deliberately unambitious. Rather than putting its own proxy in the path, Gateway Sync writes the decision as scoped, time-bound policy into the MCP gateway the enterprise already runs, with Databricks Unity Gateway and AWS AgentCore Gateway supported at launch. No second control plane, no rip and replace.

It ships with connectors for Okta Cross App Access and, notably, for Claude's Enterprise-Managed Authorization for MCP connectors, which puts Opal directly on top of the standards track rather than beside it.

## What each one actually removes

Approach

Failure it removes

Failure it leaves

Egress proxy with placeholders 
(Google, NVIDIA)

Credential theft from the sandbox, credentials in logs or model context

Over-broad credential scope, confused deputy

Per-call token minting 
(Rubrik)

Standing privilege, credential reuse across actions

Requires a gateway in the path for every call

Protocol inspection 
(Microsoft)

Unapproved servers and tools, protocol downgrade

Nothing about what the token means; stdio uncovered

Decide then delegate 
(Opal)

Permanent grants, unowned agents, unreviewed access

Depends on a gateway that can enforce what it writes

## Unstealable is not the same as scoped

Here is the thing that jumps out once you read these side by side, and it is Google who says it plainly, in its ownagents documentation:

"The agent may use any credential it has access to, so only provide credentials whose full scope you are willing to grant."

That sentence is the whole gap. An egress proxy makes a credential impossible to exfiltrate and does nothing to narrow what it can do. From inside the perimeter, the placeholder is exactly as powerful as the secret it stands for. If the token you stored is a GitHub PAT with write access to forty repositories, the agent has write access to forty repositories. It simply cannot mail the token to anyone.

That is worth having. Credential exfiltration is a real and common failure, and these designs close it well. But it is a containment control, not an authorization one, and the two get conflated constantly in how this work is described. Hiding a credential from the agent tells you nothing about whether the action the agent just took was one it should have been able to take.

The second half of the gap is the confused deputy. If a proxy will authenticate any request the agent makes to an allowlisted domain, then a prompt injection that persuades the agent to make a different request to that same domain gets authenticated too. NVIDIA's endpoint binding, down to host, port and path, is the sharpest answer to this among the five, and it is instructive that it is a scoping mechanism rather than a secrecy one.

This is also why the two proxy designs converge on token exchange as they mature. OpenShell'stoken_exchangegrants, brokered against a SPIFFE identity with audience validation, are not a secret store. They are an authorization server, reached by a different route. Google's OAuth2 credential type, holding a refresh token and minting short-lived access tokens per request, is the same recognition. Both arrived at the conclusion that the durable answer to "what may this agent do right now" is a short-lived token bound to a specific audience, because that is the only artifact the resource server can check for itself.

## Where this leaves the authorization server

The MCP authorization spec already describes that artifact, and it is worth being precise about what it requires, because it is the piece none of the four architectures above can supply on their own.

Under the current2026-07-28revision, an MCP server is an OAuth resource server. It validates every token and, critically, confirms the token was issued specifically for itself as the intended audience. Clients must send theresourceparameter from RFC 8707 on both the authorization and token request, naming the server's canonical URI, so the authorization server knows which audience to bind the token to. Servers must not accept tokens issued for anything else, and must not forward a token they received upstream.

Those rules exist to close precisely the failure that a proxy cannot reach. A token that is audience-bound cannot be replayed against a second server even by an agent holding it legitimately. A token that carries the intersection of what the agent may do and what the human behind it may do, which is what Rubrik's On-Behalf-Of federation and Okta's Cross App Access both compute, cannot be used to exceed its principal. Neither property comes from where you stored the secret. Both come from who minted the token and what they put in it.

The practical read for anyone building this: the gateway, the proxy and the firewall are all legitimate layers, and a serious deployment will likely run more than one. Network-level inspection catches the server you did not approve. A sandbox proxy keeps secrets out of model context. A gateway gives you a place to enforce a decision per call. But none of them substitute for an authorization server that issues scoped, audience-bound, short-lived tokens, because that is the one control the resource server can verify without trusting anything upstream of it.

This is the partAuthKitimplements: CIMD registration, resource indicators, protected resource metadata and issuer validation, so what stays in your MCP server is the part that has to live in your code, which is validating the token and deciding what its bearer may do.

The four architectures here are all answers to a question about credentials. The question underneath is about authority, and it is answered somewhere else.

## Frequently asked questions

Where should an AI agent's credentials live?Not in the sandbox. Both Google's Managed Agents and NVIDIA OpenShell store the secret server-side and give the agent process a placeholder, substituted by a proxy on the wire only for approved destinations. That is the right default, but understand what it buys: it prevents exfiltration, not misuse.

Does keeping a credential out of the sandbox stop prompt injection?No. If the proxy will authenticate any request the agent makes to an allowlisted domain, an injection that persuades the agent to make a different request to that same domain gets authenticated too. Narrowing what the credential can reach, as OpenShell does by binding each credential to a host, port and path, is the control that helps here. Hiding it is not.

What is the difference between a hidden credential and a scoped token?A hidden credential is as powerful as whatever you stored, and the agent can use its full scope; Google's own documentation warns that you should only provide credentials whose full scope you are willing to grant. A scoped, audience-bound token carries an explicit limit the resource server can check for itself. Only the second one constrains what the agent may do.

Does Microsoft's MCP firewall cover local MCP servers?No. It inspects MCP traffic over streamable HTTP and Server-Sent Events only, so anything running over stdio does not traverse Global Secure Access and is not covered. It also requires TLS inspection to be enabled, because MCP rides inside HTTPS.

If I run an MCP gateway, do I still need an authorization server?Yes. A gateway is a good place to enforce a decision per call, but the token it presents still has to mean something to the server receiving it. Under the2026-07-28MCP specification, the server must validate that the token was issued for itself as the intended audience, and must not accept or forward tokens issued for anything else. That property comes from whoever mints the token, not from the gateway that passes it along.

We’re hiring

Our global team is growing and we’re hiring all types of roles.

View open roles

About us

WorkOS builds developer tools for quickly adding enterprise features to applications.

Learn more