---
title: 'Agent to agent SSO across identity domains: What federation looks like when neither side is human — WorkOS'
url: https://workos.com/blog/agent-to-agent-sso-federation
site_name: tldr
content_file: tldr-agent-to-agent-sso-across-identity-domains-what-fe
fetched_at: '2026-10-20T22:05:19.703937'
original_url: https://workos.com/blog/agent-to-agent-sso-federation
date: '2026-10-20'
description: What Okta’s Agent SSO launch reveals about the unfinished standards behind cross-company agent identity.
tags:
- tldr
---

In this article
October 20, 2026
October 20, 2026

# Agent to agent SSO across identity domains: What federation looks like when neither side is human

What Okta’s Agent SSO launch reveals about the unfinished standards behind cross-company agent identity.

Maria Paktiti
October 20, 2026
Explore with AI

Open in ChatGPT

Open in Claude

Open in Perplexity

On September 22, 2026, Okta took Agent SSO, Agent-to-Agent Connections, and Resource Access Certifications to general availability. The ecosystem behind it already lists more than 25 partners, including Anthropic, Cloudflare, Keycloak, and WorkOS.

That is worth sitting with for a second. The exact problem this piece is about, letting an agent at one company prove who it is to an agent at another company, is no longer a thought experiment. It is a product category with a general availability date, a partner list, and a name: XAA, built on a protocol called ID-JAG.

It is also, underneath the announcement, still mostly unsettled. The IETF draft for ID-JAG expires on November 22, with no Working Group Last Call scheduled. At least six vendors, Okta, Descope, ServiceNow, Cequence, Postman, and Microsoft, are shipping competing agent identity products right now, each betting on a different architecture and a different standard. And a recent survey found that 96 percent of executives say they are confident in their identity and access management for non-human identities, while only 34 percent of organizations actually apply the same security controls to agents that they apply to human employees.

So the honest framing is not "here is a settled pattern for agent to agent federation." It is "here is a fast moving, partly standardized, partly product-shaped answer to a problem that single sign on was never designed to solve, and here is where the gaps still are."

## Why this is not just OAuth with extra robots

Single sign on worked for people because the assumptions behind it were stable. A small number of well known identity providers. A human in the loop who could notice a suspicious login page. Sessions measured in hours.

None of those assumptions hold once the thing authenticating is an agent, especially one that needs to talk to an agent belonging to a different company entirely.

Inside a single organization, this is close to a solved problem already. Your identity provider knows about every agent you run. Your authorization server handles delegation through on behalf of tokens. It is an extension of workload identity patterns that have existed for years.

The moment an agent needs to call an agent in a different trust domain, the ground shifts. If an agent inside your company hands a task to an agent inside a partner's company, whose authorization server issues the token that governs that interaction? Federation is the obvious answer, and cross-company federation is not new. But even once the identity layer is federated, a harder question stays open: as a token or a task moves through a chain of agents across multiple companies, how do you prove the whole chain was authorized to happen, not just that each individual hop looked fine on its own?

That gap, the difference between "this hop is valid" and "this entire chain was supposed to happen," is where most of the real engineering work currently lives.

## The stack that is converging

A handful of standards, some older and repurposed, some brand new, are forming the actual building blocks teams reach for. None of them solve the whole problem alone.

Layer

What it does

What it leaves open

Workload identity federation (WIF)

Replaces long lived API keys with short lived OIDC tokens tied to an agent's runtime context, issued by its own platform

Still assumes a pre-configured trust relationship between the two platforms involved

SPIFFE and SPIRE

Gives each agent a short lived, automatically rotated identity tied to its deployment context, verifiable across trust domains once federated

Federating SPIFFE trust domains across companies is still a manual, bilateral setup

OAuth token exchange (RFC 8693)

Lets an agent trade a token from one domain for a new one in another, while carrying forward who the original user or client was

Preserves identity context at each hop, but does not itself prove the full chain was authorized

A2A (Google's Agent2Agent protocol)

Standardizes how agents discover each other and exchange tasks, using OAuth 2.0 and short lived JWTs for identity over TLS

Explicitly puts credential provisioning out of scope, leaving each pair of organizations to agree on that separately

ID-JAG / XAA (Okta)

A JWT based grant that lets an agent carry its identity across organizational boundaries, now backing Okta's Agent SSO at general availability

The underlying IETF draft is still unratified and set to expire November 22 unless renewed

Two of these deserve a closer look because they show up constantly in current discussion.

A2Ais the communication layer agents actually talk over, and it is worth being precise about what it is not. MCP connects an agent to tools and data. A2A connects an agent to other agents, so they can discover each other and delegate tasks. An agent might use A2A to hand a task to a specialist agent, which then uses MCP to call the tools it needs to finish that task.

A2A's own specification is upfront that it does not solve credential provisioning across organizations. How a client agent actually obtains credentials to talk to a remote agent is explicitly out of scope, left to whatever HTTP security standard the two sides agree on separately. That scoping decision is reasonable for a communication protocol. It also means the cross-domain trust problem, the actual subject of this piece, sits in a gap that no single standard currently owns end to end.

ID-JAG, the protocol behind Okta's new Agent SSO, is an attempt to close part of that gap directly. The pattern looks like this across a two-company boundary.

The useful property here is that Company B's identity provider never has to trust Company A's agent directly. It only has to trust Company A's identity provider, and it issues its own narrowly scoped token for the interaction. That is a meaningfully better shape than a shared broker or a bilateral secret, and it is the same basic idea OAuth token exchange has offered for years, applied specifically to agent identity.

## Where it actually breaks

None of this is hypothetical. Teams running these patterns in production keep hitting the same handful of gaps.

TLS proves a message came from the domain it claims to have come from. It does not prove the agent on the other end is trustworthy, competent, or authorized to do what it is asking to do. There is still no standard mechanism for verifying an unfamiliar agent's actual capabilities across an organizational boundary, only its domain.

OAuth authenticates a session, not an individual message. If a token passes through three agents and the third one claims the first agent sent a particular request, there is often no cryptographic proof either way. A delegation chain carries an "act" claim showing who is currently acting, but that claim does not prove the whole chain of delegation was ever authorized in the first place. A well behaved agent can drift outside the scope a user actually intended without anyone doing anything obviously malicious. A compromised one can exploit the same gap deliberately.

Teams already running this describe the operational consequence plainly: it becomes hard to know which agent in a chain actually initiated a sensitive action, or where a token got reused across flows it was never meant to touch. Without deliberate tracing and structured logging built in from the start, auditing a multi agent workflow after the fact turns into a manual, fragmented exercise, exactly the kind of forensic reconstruction that regulators and security teams increasingly expect you not to need.

Independent security reviews of A2A flag the same shape of gap from a different angle. The protocol currently has no specialized handling for particularly sensitive payloads, payment credentials or identity documents, beyond ordinary token expiry, and tightening authorization tends to add latency and complexity in direct tension with the low friction interactions agentic systems are supposed to enable.

## A market moving faster than the standard underneath it

What makes October 2026 a strange moment to write about this is the gap between how fast products are shipping and how unsettled the standard underneath them still is.

Six vendors are now shipping agent identity products with genuinely different architectures. Descope's Agentic Identity Hub places MCP-native authorization directly in the gateway layer and both issues and validates ID-JAGs, claiming over a thousand protected MCP servers. ServiceNow's AI Passport takes a different angle entirely, grounding agent identity in enterprise business context, checking a cryptographically signed credential against a company's own configuration database and governance policies at runtime rather than against a protocol-level token alone. Okta's own Runtime Agent Gateway, the piece meant to actually enforce policy in the execution path between an agent and its tool calls, was still pre-GA as of early October, with the underlying APIs only reaching beta on September 16.

Meanwhile the Agentic AI Foundation, a Linux Foundation directed fund, has stood up an Identity and Trust working group focused on portable identity, dynamic trust, delegation protocols, and permissions flow across agent to agent interactions. That is the right instinct, a neutral body trying to keep this from fragmenting into incompatible vendor silos the way bot protection and device fingerprinting did a decade earlier. But the working group's specs are still moving from draft to implementation, and until they land, proprietary extensions fill the gap on whatever terms each vendor sets.

## The direction past the current stack

The instinct might be to solve this the way federation has always been solved, by getting everyone to agree on a shared identity provider or a shared broker both sides trust. That works within a tight partner ecosystem. It breaks down as the number of organizations grows, because it recreates the exact bilateral, one-off integration problem federation was supposed to eliminate, just one layer higher up.

What is emerging past the current vendor race looks more like decentralized identity than centralized federation. Some agent systems are being issued decentralized identifiers, giving each agent a portable identity not tied to any single cloud provider or IdP, verifiable independently of who issued it. Separately, the Trust over IP Foundation's Trust Spanning Protocol is being explored as a way to run A2A style interactions over a substrate built from the ground up for cross domain trust, rather than bolting federation onto a protocol that was not originally designed for it.

The parallel worth naming directly: email, the fediverse, and federated identity for humans all solved versions of the same underlying problem, decentralized trust between parties with no shared administrative domain, each at a different layer, each with different tradeoffs. Agent federation has to solve all of those layers at once, plus autonomous action, plus legal liability for what an agent does on someone else's behalf, plus real time compliance requirements that did not exist when those earlier systems were designed.

## The part that has to be true before any of this works

Everything above assumes each organization already has a coherent, well governed identity story for its own agents before it tries to federate that identity outward. An agent with a fuzzy, shared, long lived service account inside your own company does not become trustworthy the moment it crosses an organizational boundary. The boundary just makes the fuzziness someone else's problem too.

Cross-organization federation is only as trustworthy as the weakest identity domain in the chain. Getting your own agents onto scoped, short lived, individually accountable identities internally, with real audit trails behind every action, is not preparation for some future federation standard. It is the prerequisite for being a trustworthy party to any federation at all, which is also, not coincidentally, exactly the layer WorkOS already sits at as one of the listed partners in this ecosystem.

We’re hiring

Our global team is growing and we’re hiring all types of roles.

View open roles

About us

WorkOS builds developer tools for quickly adding enterprise features to applications.

Learn more