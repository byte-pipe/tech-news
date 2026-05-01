---
title: Everyone's Talking About Gemini. The Real Story at Google Cloud NEXT '26 Was GKE Agent Sandbox. - DEV Community
url: https://dev.to/sreejit_caab72e273a4faa1f/everyones-talking-about-gemini-the-real-story-at-google-cloud-next-26-was-gke-agent-sandbox-19g2
site_name: devto
content_file: devto-everyones-talking-about-gemini-the-real-story-at-g
fetched_at: '2026-05-01T11:58:28.155564'
original_url: https://dev.to/sreejit_caab72e273a4faa1f/everyones-talking-about-gemini-the-real-story-at-google-cloud-next-26-was-gke-agent-sandbox-19g2
author: Sreejit
date: '2026-04-29'
description: 'Google Cloud NEXT ''26 had one clear headline: the Gemini Enterprise Agent Platform. A full-stack... Tagged with cloudnextchallenge, googlecloud, ai, devchallenge.'
tags: '#cloudnextchallenge, #googlecloud, #ai, #devchallenge'
---

Google Cloud NEXT '26 Challenge Submission

Google Cloud NEXT '26 had one clear headline: theGemini Enterprise Agent Platform. A full-stack rebrand of Vertex AI. An Agent Designer. Long-running agents with persistent memory. Fancy demos with Unilever and Team USA. Thomas Kurian stood on stage in Las Vegas and told 32,000 people that we've left the AI pilot era behind.

He's right. But if you want to understandwhythat transition is actually possible now — technically, mechanically, in production — you need to look at an announcement that got maybe a tenth of the keynote airtime.

GKE Agent Sandbox.Now GA.

Let me tell you why I think this is the most important thing Google shipped at NEXT '26, and why developers building agent workloads should care about it before they care about any of the shiny stuff.

## The Problem Nobody Likes Talking About

Every agent tutorial ends the same way: the agent reasons about what to do, writes some code, and... executes it. Usually with aexec()call or a subprocess. Usually directly on whatever machine is running your app.

If you've shipped this to production, you already know the existential dread that comes with it. LLM-generated code isfundamentally untrusted— it's not code a human engineer reviewed. It could write to the wrong path. It could make outbound network calls. It could loop forever and eat your CPU. And in any multi-tenant environment, one agent's bad output could poison another's environment entirely.

The "solutions" most teams reach for aren't great:

* Human review gates: Defeats the point of automation.
* Strict output parsers: Brittle, breaks with model updates.
* Full VMs per agent: Slow (10-30s cold start), expensive, operationally heavy.
* Docker containers: Better, but containers share the host kernel — gVisor or similar isolation still isn't there by default.

So most teams just... accept the risk and move fast. Which works until it doesn't.

## What GKE Agent Sandbox Actually Does

GKE Agent Sandbox is a GKE add-on that gives you isolated, stateful, single-replica environments for agent code execution — with kernel-level isolation viagVisor, and provisioning speed that actually fits real-time workloads.

Here are the numbers that matter:

* Sub-second time to first instruction
* 300 sandboxes per second, per cluster
* ~30% better price-performanceon Axion N4A vs. the next leading hyperscaler

That first two bullets are what change the equation. When your options were "fast but unsafe" or "safe but slow," teams picked fast. Now the tradeoff is gone. Sub-second isolation means you can sandbox every single agent tool call without your users noticing.

The architecture is clean. Each sandbox is represented by a Kubernetes CRD (theSandboxresource). A controller manages lifecycle — creation, stable identity, networking, and storage. ASandbox Routergives each sandbox a stable endpoint, so you can route traffic to it without your application needing to track Pod IPs. The whole thing sits on Kubernetes primitives, so if you already operate GKE, there's no new mental model to learn.

# This is the level of simplicity we're talking about

`apiVersion
:
 
sandbox.gke.io/v1

kind
:
 
Sandbox

metadata
:

 
name
:
 
agent-task-abc123

spec
:

 
template
:

 
spec
:

 
containers
:

 
-
 
name
:
 
executor

 
image
:
 
my-agent-executor:latest

 
runtimeClassName
:
 
gvisor`

Enter fullscreen mode

Exit fullscreen mode

## The Claim Model: Why the API Design is Good, Actually

One design decision I want to highlight: theClaim Model.

In a standard Kubernetes StatefulSet, if you want an isolated Pod, you manage the Pod directly — you know its name, you track its IP, you handle restarts. That's fine for databases. It's a nightmare for ephemeral agent sandboxes that might be created and destroyed thousands of times per hour.

The Claim Model separatesasking for a sandboxfromknowing where the sandbox lives. Your application says "I need an environment for this task" — the controller handles placement, node assignment, network identity, and volume binding. You get back a stable endpoint via the Sandbox Router. You never touch the underlying Pod.

This is the same pattern that made PersistentVolumeClaims a developer-friendly abstraction over storage. It's the right call for agent environments too, and I'm glad they shipped it this way rather than just exposing raw StatefulSet management.

## Pause and Resume: The Underappreciated Feature

Long-running agents — tasks that take hours, involve many steps, and need to wait for external signals — are a cornerstone of the NEXT '26 pitch. Google showed demos of agents running procurement analysis, sequencing sales follow-ups, doing overnight reconciliation work.

Those agents need towaitsometimes. Waiting while holding a hot container wastes money and compute.

GKE Agent Sandbox integrates with GKEPod Snapshots: you can pause a sandbox, serialize its full in-memory state, and resume it later from exactly where it left off. An agent paused mid-reasoning picks up where it stopped. No re-running from the beginning, no "the agent forgot what it was doing."

For genuinely long-horizon agentic tasks, this is table stakes. It's good that it shipped alongside the sandbox, not as a follow-up feature.

## Real Signal: 200,000 Projects a Day at Lovable

When companies drop GA announcements, they usually come with a reference customer. The sandbox gotLovable— the AI-powered web app builder that spins up isolated development environments on demand, constantly.

200,000 new projects per day. Each one needs an isolated environment. That's the exact workload GKE Agent Sandbox was built for, and it's running in production.

That's not a beta signal. That's a "we've already stress-tested this at scale" signal. It matters.

## Where I'd Push Back

I want to be honest about what the sandboxdoesn'tsolve.

gVisor isolates syscalls. It doesn't isolate intent.

If an agent's generated code makes an outbound HTTPS call to exfiltrate data, gVisor won't stop it — that's a valid syscall. If the agent calls an external API with destructive side effects, the isolation layer doesn't know. The sandbox keeps your host kernel safe. It doesn't make your agenttrustworthy.

The answer to that problem is network policy + egress controls + Google's Agent Gateway and Agent Identity features — but the integration story between sandbox-level networking constraints and agent-level permission scoping is still evolving. The documentation is thin on "here is exactly how you configure an agent sandbox to only be able to call APIs X and Y." That's the gap I'll be watching in the months after NEXT.

Also: the 30% price-performance claim is onAxion N4Aspecifically. If your workloads run on N2 or C3 instances today for other reasons, the economics look different. Run your own numbers before accepting the headline.

## Why This Matters More Than the Platform Announcements

Gemini Enterprise Agent Platform is a product. It will evolve. Features will be added, deprecated, rebranded. The roadmap will change.

GKE Agent Sandbox is aprimitive. Infrastructure primitives have a way of outlasting the products built on top of them. When Kubernetes PersistentVolumes shipped, nobody predicted all the ways stateful workloads would eventually use them. When Firecracker shipped at AWS, "fast microVMs" unlocked Lambda use cases that weren't in the original vision.

The same will happen here. Sub-second, gVisor-isolated, Kubernetes-native ephemeral environments will enable workloads nobody has built yet — not just AI agents. Interactive notebooks that auto-provision per user. Secure eval sandboxes for CI pipelines. Per-request isolation for multi-tenant developer tools.

Google built a tool for their agent story. Developers will use it for ten other things.

## Getting Started

If you want to try it yourself:

1. Enable the add-onon an existing GKE cluster (Autopilot support is coming; for now, Standard clusters with Axion N4A nodes get the best price-performance).
2. Install the Agent Sandbox Python SDKfrom GitHub for programmatic sandbox management without dealing with raw Kubernetes resources.
3. Start with the Claim Model— request sandboxes declaratively and let the controller handle placement. Don't reach for raw StatefulSets.
4. Set egress policies immediately— don't leave sandbox network access open while you prototype. The habit is easier to build early.

The docs are at cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox.

## Final Take

Google Cloud NEXT '26 was the conference where "we're exploring AI" became "we're running AI in production." The Gemini Enterprise Agent Platform got the keynote. The TPU 8t got the infrastructure spotlight. The Agentic Data Cloud got the data engineering talk.

GKE Agent Sandbox got a slide and a bullet point in a 260-item wrap-up post.

That's fine. The best infrastructure ships quietly and lets the workloads speak for themselves. 200,000 sandboxes a day at Lovable is speaking pretty loudly already.

If you're building agents that execute code, I'd spend less time this week exploring the Agent Designer UI and more time reading the gVisor isolation docs. The platform is impressive. The primitive is what makes it real.

Tried GKE Agent Sandbox already? Drop your experience in the comments — especially curious whether anyone has wired up egress controls end-to-end.

If you want to try it yourself:

1. Enable the add-onon an existing GKE cluster (Autopilot support is coming; for now, Standard clusters with Axion N4A nodes get the best price-performance).
2. Install the Agent Sandbox Python SDKfrom GitHub for programmatic sandbox management without dealing with raw Kubernetes resources.
3. Start with the Claim Model— request sandboxes declaratively and let the controller handle placement. Don't reach for raw StatefulSets.
4. Set egress policies immediately— don't leave sandbox network access open while you prototype. The habit is easier to build early.

The docs are atcloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox.

## Final Take

Google Cloud NEXT '26 was the conference where "we're exploring AI" became "we're running AI in production." The Gemini Enterprise Agent Platform got the keynote. The TPU 8t got the infrastructure spotlight. The Agentic Data Cloud got the data engineering talk.

GKE Agent Sandbox got a slide and a bullet point in a 260-item wrap-up post.

That's fine. The best infrastructure ships quietly and lets the workloads speak for themselves. 200,000 sandboxes a day at Lovable is speaking pretty loudly already.

If you're building agents that execute code, I'd spend less time this week exploring the Agent Designer UI and more time reading the gVisor isolation docs. The platform is impressive. The primitive is what makes it real.

Tried GKE Agent Sandbox already? Drop your experience in the comments — especially curious whether anyone has wired up egress controls end-to-end.``

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse