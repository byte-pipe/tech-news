---
title: 'AI agent deprovisioning: Revoking access doesn''t erase what it read — WorkOS'
url: https://workos.com/blog/ai-agent-deprovisioning-revocation
site_name: tldr
content_file: tldr-ai-agent-deprovisioning-revoking-access-doesnt-era
fetched_at: '2026-10-19T17:20:44.484349'
original_url: https://workos.com/blog/ai-agent-deprovisioning-revocation
date: '2026-10-19'
description: Revoking an AI agent's access stops new reads but not what it already learned. What OpenAI's dots reveal about deprovisioning, and four controls that help.
tags:
- tldr
---

In this article
October 19, 2026
October 19, 2026

# AI agent deprovisioning: Revoking access doesn't erase what it read

Revoking an AI agent's access stops new reads but not what it already learned. What OpenAI's dots reveal about deprovisioning, and four controls that help.

Maria Paktiti
October 19, 2026
Explore with AI

Open in ChatGPT

Open in Claude

Open in Perplexity

When you revoke an AI agent's access to an app, the agent can't read anything new, but whatever it already read stays in its context. Agent context is a copy of your data, not a view of it, so deprovisioning an agent means limiting what gets copied, logging what was read, and getting the copy cleared, not just cutting the connection.

OpenAI'ssafety page for dots, published September 29, 2026, prints the sentence most deprovisioning runbooks assume away:

"In the Plugins section of Settings, you can review connected accounts and change what dots can access going forward. Disconnecting an app stops new information sharing through that connection. But information a dot has already learned remains in its own context."

That's an honest description of how any agent with persistent context behaves, and OpenAI put it right next to the control it qualifies instead of leaving customers to find out later. The problem it exposes lives on your side. Deprovisioning, as practiced, assumes revocation reaches back in time. Against an agent that keeps working between conversations, it doesn't. Agent context is a copy of your data, and every revocation control you own governs the view.

A view goes dark when you cut the line. A copy doesn't care that the line is gone.

## Was revocation ever retroactive?

No. It just used to look that way.

RFC 7009has described OAuth token revocation since August 2013. Its promise is narrow and precise: "A revocation request will invalidate the actual token and, if applicable, other tokens based on the same authorization grant and the authorization grant itself." The invalidation "takes place immediately, and the token cannot be used again after the revocation," allowing for propagation delay. The security considerations are blunt about the scope: the spec "in general does not intend to provide countermeasures against token theft and abuse."

Revocation kills the credential. It has never said anything about the data that credential already moved.

What made it feel retroactive was the shape of the client. A SaaS integration holds a token and renders your data on request; when the token dies, the screens go blank and the sync stops. Whatever got cached is incidental, and mostly nobody thinks about it. We've spent years hardening that model:revoking sessionsso later requests fail, and making SCIMactive: falsemean more than a database write, becausesessions, refresh tokens and API keys outlive the user recorduntil the app explicitly kills them.

An agent flips that shape. Reading isn't a side effect of rendering a page; reading is the product. Each dot "has its own cloud computer," works across the apps you connect, and can "keep making progress between conversations." Background research adds reads nobody asked for: read-only tools gather information from permitted connected sources and save private notes for that dot. OpenAI enforces real limits on those tasks: they can't send messages to other people, change content in connected apps, or control a browser or desktop. Those limits bound what the agent can do. They say nothing about what it has.

Revocation cuts the arrows, not the container. Everything read before the line is still there after it.

## Who can reset an agent's context?

The same page that documents the gap also ships a control for it: "Each dot has its own context that you can reset at any time." Nothing here is hidden, and treating it as a scandal would miss the actual problem.

The problem is who holds the control and what triggers it. Revoking access doesn't trigger a reset; disconnecting an app changes only what dots can reach from then on, and the context survives. And the "you" in that sentence is the dot's user, not the company whose data the dot read. Those permissions are the user's own connections, "shared across ChatGPT, ChatGPT Work, and Codex."

Follow that through an offboarding. A contractor's access to your deal room ends when the engagement does. Your SCIM handler marks the user inactive, your app revokes their sessions and keys, the connected app is disconnected, and the audit log looks clean. The pricing, customer list and renewal dates the contractor's agent read last month are still in that agent's context, and the reset that would clear them lives in the contractor's own account. OpenAI doesn't document any way for you, as the data owner, to trigger it. You can ask. You can't confirm it happened.

## Isn't this the same as a person remembering what they read?

This is the strongest objection, and it deserves a straight answer. People keep what they read. Offboarding has always been partly a legal instrument rather than a technical one, backed by an NDA and the expectation that nobody dumps the CRM on the way out. An agent's context is arguably the same kind of risk, and we already live with it for people.

The analogy breaks on accumulation. A person stops reading your deal room when their access ends; background research keeps pulling from permitted sources and writing notes into the dot's context without anyone remembering to ask, so the copy grows right up to the moment the connection is cut. It also spreads sideways. When dots delegate work, the other agents "are instructed to keep the information needed for the task and avoid retaining unnecessary sensitive details." That's a reasonable choice at that layer, but it's an instruction, not enforcement, sent over the same text channel that carriesmalicious instructions aimed at agents.

The copy can also change category. Notes from background research can reach a later conversation, and OpenAI says information brought into a conversation that way "may be used for model training" depending on the user's settings. ChatGPT Business, Enterprise and Edu workspaces are excluded from training by default, so your exposure depends on which plan the agent's user happens to be on. That's a fact about someone else's billing, not about your controls.

OpenAI's own design concedes the point where the stakes are most obvious. Secure sign-in sends credentials straight to the browser environment "without exposing them to the model's context," and the page warns that "a secret placed separately in a readable message or document may still be visible to the model." Passwords get a dedicated path around the context window precisely because what enters context is hard to get back out. Your customer records don't get that path.

## How do you design for the copy?

If context is a copy, the controls that matter shape what gets copied, how long the copying window stays open, and what you know afterward. Four are available today, and none needs anything from the agent vendor.

Control

What it limits

What it costs

Short-lived grants

How much gets copied before someone reviews the grant

Periodic re-approval

References, not records

What lands in context in the first place

One extra call per record the agent actually needs

A read log keyed to the connection

What you don't know after revocation

Logging every read, not just every login

Context reset in the runbook and the contract

How long the copy survives

Enforced by agreement, not by code

Keep the access window short on purpose.RFC 7009 already makes this argument for tokens: short-lived access tokens let the authorization server "impose a limit on the time revoked when access tokens are in use." For an agent connection, the same dial controls something bigger: not how long a stale token keeps working, but how much of your data gets copied before someone has to look at the grant again and decide whether it's still needed. A grant that renews weekly bounds the copy; a grant that never expires bounds nothing. The same reasoning applies to anything durable the agent holds on your side, which is whyan MCP event subscription is a credentialand its time to live is your revocation window.

Hand out references, not records.A list tool that returns full rows puts every field it touched into the agent's context for good. A list tool that returns handles puts in almost nothing:

 

{
 "results": [
 { "id": "deal_8831", "summary": "Acme renewal, closes next quarter" },
 { "id": "deal_8914", "summary": "Globex expansion, in legal review" }
 ],
 "read_tool": "get_deal"
}
 

The agent callsget_deal("deal_8831")when it actually needs the numbers, and that call runs your authorization check at call time instead of trusting a grant from last month. The cost is one round trip per record the agent genuinely needs; the benefit is that after revocation the next read fails, which is what you thought revocation did all along. And keep the credential itselfout of the agent's context, so a revoked grant can't be replayed from the copy.

Treat the read log as a copy inventory.Once the connection is cut, the only honest answer to "what does that agent still have?" is whatever your logs say it read. Most access logging answers who; this one has to answer what, tied to a connection and bounded by a revocation timestamp. Without it, you can't scope an incident or tell a customer what a departing employee's agent walked away with.Audit logs for AI agentscovers what those events should contain.

Put context reset in the runbook and in the contract.The reset exists and you can't press it. Offboarding checklists already ask people to return laptops and confirm they've deleted shared passwords; asking a leaver to reset the agents that read company data is the same kind of control, with the same enforcement gap. Put the obligation where it binds, in the contractor agreement, the acceptable use policy and the vendor data processing agreement, instead of pretending a technical path exists. Users can also follow ongoing work and tell a dot to stop from Activity View, which is a containment tool for them, not for you.

## What does offboarding have to answer now?

For twenty years, deprovisioning answered one question: who still has access? That's now the easy half. The half that decides your blast radius is what was already read, by which agent, before the grant was cut. Nothing in a standard identity stack is built to answer that.

Start with the read log. The rest is policy you can argue about next quarter; the log is the only record that will tell you, when a customer asks, which copies are already out there.

If you already send events toWorkOS Audit Logs, an event per agent read, with the agent as the actor and the delegating user and connection in its metadata, gives you that inventory alongside the other events you emit for that organization, ready to export when a customer asks, as long as your retention period or a Log Stream covers the window they're asking about.

## Read more

* SCIM deprovisioning deep dive
* Session revocation explained: protect your users, systems, and AI agents
* Gemini agents in your SCIM feed: provisioning non-human users
* Best practices for AI agent access control

We’re hiring

Our global team is growing and we’re hiring all types of roles.

View open roles

About us

WorkOS builds developer tools for quickly adding enterprise features to applications.

Learn more