---
title: The New MCP Roadmap | Model Context Protocol Blog
url: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
site_name: hnrss
content_file: hnrss-the-new-mcp-roadmap-model-context-protocol-blog
fetched_at: '2026-08-22T19:21:38.662240'
original_url: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
author: David Soria Parra (Lead Maintainer), Den Delimarsky (Lead Maintainer)
date: '2026-08-22'
published_date: '2026-08-22T09:00:00+00:00'
description: An update on the Model Context Protocol roadmap and focus areas for upcoming specification releases.
tags:
- hackernews
- hnrss
---

Table of Contents
* Priority areasAgentic messaging primitivesHTTP-native transport unification and hardeningAgent identity and enterprise-ready securityImproved primitivesImproved SDK developer experience
* Agentic messaging primitives
* HTTP-native transport unification and hardening
* Agent identity and enterprise-ready security
* Improved primitives
* Improved SDK developer experience
* Proposal prioritization
* Get involved

Today we’re excited to publish an updatedroadmapfor the Model Context Protocol (MCP), covering the next specification release and beyond.

The roadmap sets the direction for protocol work over the coming months. It was developed by the Core Maintainers together with our community of maintainers and Working Groups.

Explore the roadmap 
→

## Priority areas#

The roadmap is organized into five priority areas. Several of them pick up work that theprevious roadmaplisted as on the horizon, including server-initiated events, result type improvements, and agent identity, which have since matured enough to become priorities in their own right. Each area is owned by a set of Core Maintainers and one or more Working Groups.

### Agentic messaging primitives#

Modern agentic workloads no longer fit the standardrequest-and-response pattern. Loops can run for longer, servers can push streamed results, and there is a clear need to steer work mid-flight. MCP has been growing to meet these requirements, introducingTasks,subscriptions/listen, andprogress notifications. We want to make sure that we not only offer the right primitives for the job, but also that they work well together. The work here spans server-initiated events (webhooks and channels, so clients aren’t left polling for results), a composition review across theAgents, Transports, andTriggers & EventsWorking Groups, and maturing the Tasks extension (SEP-2663) so it can move into the specification.

### HTTP-native transport unification and hardening#

With the2026-07-28 release, a remote MCP server is now no different from any other HTTP workload, making it easy to host and operate one on any infrastructure that developers and organizations already use for their APIs and services. The model has proven to scale, and we want to stretch it to cover other deployment modes as well, including local servers speakingStreamable HTTPoverstdio. Unifying on one transport lets us simplify MCP server and client development even further.

### Agent identity and enterprise-ready security#

MCP authorizationtoday is built around a person approving access in a browser. That works well for interactive clients, but more and more of the callers are agents running as cloud workloads with their own identity, acting on behalf of a user who isn’t present, or delegating narrower authority to sub-agents. We want MCP servers to have a standardized way to recognize and trust those agent identities, built on existing standards rather than pasted API keys and long-lived tokens.

The work here covers finalizingDemonstrating Proof of Possession(DPoP) and driving its adoption, and defining an opinionated path for agent identity and delegation throughWorkload Identity Federation, the ID-JAG grant behindEnterprise-Managed Authorization, and standard token exchange. We will also continue to grow our engagement with the OAuth standards bodies, including the IETF OAuth andWIMSEworking groups, to help the underlying standards evolve with the building blocks that agent identity needs.

### Improved primitives#

Tool calling is the part of MCP most developers touch first, and it has held up well over the lifetime of the protocol. Where it falls a bit short, however, is in the result handling. Atools/callresponse can carry the same output in more than one form, and a server developer today has no way to know which form a given client will put in front of the model. We aim to make this easier by standardizing on one clear contract.

The other challenge we need to address for primitive use is their ever-growing scale. Connecting to a server with a hundred tools means the model pays for that entire surface before the user has asked a single question, and tool selection tends to get worse as the list grows. We’re starting a progressive discovery effort so a server can offer a small entry point and reveal more of its catalog as the conversation narrows.

### Improved SDK developer experience#

Our SDKs are how developers experience MCP. We are investing in their ergonomics and theirconformance with the specification, and in making them intuitive and well-documented across every platform and language we support. This is even more important now that many developers build MCP clients and servers by pointing an agent at our libraries, where clear APIs and accurate docs decide whether the code will work with minimal friction.

## Proposal prioritization#

Specification Enhancement Proposals(SEPs) that fall within these priority areas get expedited review and have the best chance of acceptance. Proposals outside them aren’t rejected automatically, but maintainer review time is scarce and goes to the roadmap first.

If you’re considering a SEP, identify the priority area it belongs to, raise it with the relevantWorking Group, and work with its members to shape your proposal. Each area on theroadmapnames the Core Maintainers responsible for it, and anyone interested in contributing can reach them onDiscord. We’re excited to work with the community to review and build on the proposals that support this roadmap.

## Get involved#

Every priority area above has a Working Group behind it or forming around it, and all of them have room for more contributors. There are several ways to participate:

* Join a Working Group or Interest Group: see theWorking and Interest Groupspage and thecommunity channels.
* Propose or comment on a SEP: read theSEP guidelines, then open one or weigh in.
* Start an experimental extension:SEP-2133lets any WG or IG experiment in anexperimental-ext-repository before a formal SEP.
* Contribute directly: thecontributing guidecovers the specification, SDKs, and tooling.

We look forward to growing and evolving MCP together!