---
title: Agent substrate can power agents on Kubernetes with kagent | Solo.io
url: https://www.solo.io/blog/agent-substrate-powers-kubernetes-agents-with-kagent
site_name: tldr
content_file: tldr-agent-substrate-can-power-agents-on-kubernetes-wit
fetched_at: '2026-06-12T19:42:03.898290'
original_url: https://www.solo.io/blog/agent-substrate-powers-kubernetes-agents-with-kagent
date: '2026-06-12'
description: Kubernetes transformed how we run services. Agent Substrate and kagent are transforming how we run AI agents with fast startup, efficient resource utilization, and secure execution.
tags:
- tldr
---

About a month ago, weannounced support for NemoClaw on kagentand pointed out a number of challenges for running Agents on Kubernetes including:

“Agents are long-lived, bursty, and idle most of the time. We need lighter-weight isolation primitives: Firecracker microVMs, gVisor, Kata Containers and real lifecycle support: suspend, snapshot, resume, scale-to-zero with state preserved. “

We are happy to share updates to solving these challenges. We have been working with the community on theAgent Substrateproject as a foundational piece for running “sandboxed” AI agents in kagent on Kubernetes. We are contributing support for running any kind of AI agent inkagentwhich uses Agent Substrate under the covers.

## Why Agent Substrate?

Kubernetes is a great workload and orchestration engine. It can run all kinds of workloads. But scaling to zero, very fast workload boot times (milliseconds), equally fast tear down, idle workloads, single-tenant sandboxing, etc is not the sweet spot for Kubernetes.

Within Solo.io, for our enterprise kagent offering, we built a custom solution to solve these problems. We built a solution using Bubblewrap/Landlock/seccomp with an option to use Firecracker microVMs and a control plane that ran adjacent to the Kubernetes control plane. Our solution allowed us to pack many agent instances/actors into a single pod/VM/container and provide strict tenant sandboxing. Additionally, we could scale out across many pods and clusters. Or VMs if we wanted. Or other container orchestrators.

Our custom solution locks down all traffic and routes egress through theAAIF agentgateway projectwhich can provide sophisticated controls/security/governance for LLM/MCP/Agent communication. We can scale agents to zero, snapshot them to storage, and resume them very fast: 50ms for the Bubblewrap solution or 200ms for Firecracker.

We were about to opensource this technology. Right as we were, we caught  wind that a team at Google was working on a similar solution called Agent Substrate. Not similar insofar that it was “another sandbox project”, but rather that it was very close to what we already built. The overlap and architecture were so similar, we decided it was best to bring our experience and work on this with Google.

So what is Agent Substrate built to solve?

* Better utilization of pods – agent-per-pod models where agents sit idle waste compute resources; Agent Substrate can suspend idle agents and swap in agents ready to work
* Avoid Kubernetes API in deployment hot path – Kubernetes API server is not built to handle millions of resources / writes / updates; agent-substrate leverages the Kubernetes API for what is good for and brings a separate but complementary control layer that is better suited for the deploy/suspend/resume workflow of AI agents
* Pods can take seconds to startup – Kubernetes relies on an eventually consistent model that converges on a working pod. This is typically on the order of seconds; Agents need much faster; Agent Substrate reduces this to milliseconds
* State management is difficult – Kubernetes is not designed for millions of volumes being attached/detached; Agent Substrate can snapshot entire agents to storage (ie, GCS, S3, etc) and resume quickly

‍

Figure 1
: Going from deploying a single agent in an “always on” pod even when idle to an “on-demand” agent scheduled to worker pool and paused/evicted when idle

## How does it work?

At a high level, Agent Substrate schedules/suspends actors (agents) into workers (Pods). You pre-provision a set of Pods (could be configured with autoscaling) to act as generic workers. You configure this in a WorkerPool resource.

AgentSubstrate deploys actors (i.e., AI agents) into the workers. You define actors with an ActorTemplate resource and AgentSubstrate spins up actors from that template.

‍

Figure 2
: Actors scheduled into warm worker pool

The actual running actors are managed by the Agent Substrate control plane. Agent Substrate uses a networking layer to route requests from a client to an actor running in a worker. If the actor does not exist, it boots it up (very quickly) and services the request. When the agent becomes idle, it gets snapshotted into storage and scheduled out of the worker.

‍

Figure 3
: Network calls can trigger agent scheduled to worker pool to serve request

## How does kagent use Agent Substrate?

Kagent supports running your own agents (Langchain, CrewAI, ADK, etc). declarative agents (no-code with Agent custom resource), and agent harnesses such as OpenClaw / Hermes. Typically these would be deployed to Pods and run as “long-running” services. But with Agent Substrate, we can now deploy these agents into Agent Substrate, taking advantage of the routing, snapshotting, and quick suspend/resume cycles. Each agent runs on the substrate worker in a gVisor or Firecracker VM and is completely locked down.

‍

Figure 4
: Agent runs in a locked down sandbox via gVisor / Firecracker VM

All network traffic goes through agentgateway and can (future) be locked down with fine-grained egress and ingress policies. For example, an agent trying to make calls out to OpenAI doesn't need to have OpenAI API keys. Credentials can be injected on egress from agentgateway.

‍

Figure 5
: Agent egress goes through agentgateway for policy controls

Agents can behave with hostility (even out of the kindness of their good intentions) so they should be locked down and finely controlled. Running agents on Kubernetes has been sub-optimal up to this point. With agent substrate and kagent, we’ve solved some of these problems.

## Running agents on kagent

Here’s a quick example. We can run an OpenClaw style agent harness by creating it through the kagent UI:

‍

You can see we pick theRuntime → Control planeas “Agent Substrate”. Kagent still supports 1:1 agent to pod. You can then interact with the agent normally (through channels, or the gateway UI, etc). The OpenClaw agent will be scheduled as an actor to a worker in the worker pool.

You can review what actors are deployed to what workers in the Substrate view:

## Where to go from here?

Kubernetes transformed how we run services. Agent Substrate makes running AI agents on top a reality.

If you're building agent platforms, agent harnesses, or autonomous workflows on Kubernetes, now is the time to get involved. Try kagent, experiment with Agent Substrate, and help shape the next generation of cloud-native agentic infrastructure.

Read the docs,join the community, and start building with kagent today!!

## Featured content

See More

### kagent <3 Agent Substrate: A 101 installation & Configuration Guide

Learn how to run AI agents on Kubernetes with Agent Substrate and kagent. This step-by-step guide covers architecture, installation, configuration, and deploying agent workloads using the Substrate runtime.

Read Blog

### Solo Enterprise for Istio 1.30: Agentic Mesh, ztunnel-Native Egress, New UI, and Fine-Grained Workload Identity

This release brings agentgateway into the ambient mesh as a waypoint, ingress, and egress proxy, adds egress controls directly in ztunnel, ships a revamped Solo UI with a new advanced Service Graph, and introduces workload identity that goes beyond the service account.

Read Blog

### Agentgateway Code Mode for OpenAPI to MCP

A very common pattern for MCP servers in the enterprise is to wrap existing APIs. We’ve invested 20+ years in building useful, reusable, valuable APIs, should we really be reinventing everything just because a fancy new protocol showed up? Is that even practical? The answer is no. We need to be practical and recognize some fundamental challenges mapping APIs to MCP tools. With agentgateway, we have three ways to expose OpenAPI operations via MCP: direct exposure, custom exposure with optional API chaining, or an AI model-controlled “code mode”.

Read Blog

### From Service Mesh to Agentic Mesh

Service mesh became boring...but it's more foundational than ever before.

Read Blog

### Keeping Context and Tokens Low With Progressive Disclosure In Agentgateway

Learn how to cut MCP token usage by 91% using agentgateway’s progressive disclosure. Reduce cost, control context bloat, and optimize agent workflows.

Read Blog

### MCP Progressive Disclosure: Save Tokens, Retrieve Schemas

Read Blog

### Five Minutes to Your First MCP Server Tool: A Quickstart with agentgateway

New to agentic AI? This guide walks you through running agentgateway locally, connecting to MCP servers, and understanding core concepts like rate limiting and observability.

Read Blog

### Agentic Quality Benchmarking With Agentevals

Read Blog

### The AppMesh Migration Playbook

Read Blog

### Solo Enterprise for Istio 1.29: ECS Now GA, Enhanced Debuggability, and Flexible Global Service Aliasing

The latest Solo Enterprise for Istio release delivers General Availability of AWS ECS integration and powerful new global service aliasing capabilities.

Read Blog

### Your First AI Route: Connecting to OpenAI with AgentGateway

Read Blog

### Getting started with Multi-LLM provider routing

Read Blog

### What Comes After Ingress NGINX? A Migration Guide to Gateway API

Ingress NGINX is being retired. This guide walks through migrating Ingress configs to Kubernetes Gateway API using ingress2gateway and kgateway.

Read Blog

### Why Traditional Gateways Failed AI Workloads - and How Kgateway's Rust-powered Agentgateway Fixes It

Most AI gateways patch legacy proxies. Kgateway starts from first principles, rethinking the gateway for the agentic era with a data plane built specifically for modern AI traffic.

Read Blog

### Context-aware Security for Agentic AI Gateways

If your gateway can’t tell the difference between a tool call and a model invocation, it can’t enforce meaningful security. Agentic systems demand a new class of context-aware, AI-native gateways.

Read Blog

### Kgateway: The Best Alternative for Ingress NGINX

Learn how kgateway, a CNCF-hosted project built on Envoy, offers a trusted path forward for Ingress NGINX.

Read Blog

### The Linux Foundation’s new Agentic AI Foundation and Secure MCP Infrastructure

Read Blog

### Security Holes in MCP Servers and How To Plug Them

Learn how to close the major security gaps in Model Context Protocol (MCP) with a proper AI Gateway. This guide walks you through deploying MCP Servers on Kubernetes, adding authentication, locking down tools, and strengthening your organization’s overall MCP security posture.

Read Blog

### Announcing Gloo Mesh Support for Amazon ECS

Latest Gloo Mesh release now provides support and enterprise-grade service mesh capabilities for Amazon ECS workloads.

Read Blog

### Gloo Mesh 2.11: Expands Support to Amazon ECS and Brings Multi-Tenant Flexibility to Enterprises.

Latest Gloo Mesh release expands support to Amazon ECS and brings multi-tenant flexibility to enterprises.

Read Blog

### Reducing the costs and complexity of your cloud native architecture with Ambient Mesh

Learn how Istio's Ambient Mesh simplifies cloud-native connectivity and dramatically reduces the cost and complexity of connecting, securing, and observing services across on-prem, cloud, or hybrid environments — without sidecars.

Read Blog

### Introducing Solo Enterprise for agentgateway

From pilots to production with context-aware AI networking

Read Blog

### Introducing Gloo Gateway 2.0

We're excited to introduce Gloo Gateway 2.0, built on the CNCF kgateway project and Kubernetes Gateway API. This release unifies open-source innovation with enterprise-grade extensions, ambient mesh integration, and AI-ready data planes to deliver secure, scalable, and future-proof API gateway capabilities for cloud-native and agentic workloads.

Read Blog

### Ambient mesh deployments made easy with Gloo Operator

This article discusses different ways to install Istio ambient mesh, and contrasts the Helm approach with the Gloo Operator, a new method for installing ambient mesh in Gloo Mesh.

Read Blog

### Choosing between installation methods in Gloo Mesh: Helm vs. the Gloo Operator

Explore Istio installation options with Gloo Mesh. Compare Helm for control and flexibility vs. Gloo Operator for simplicity and automation to find the best fit for your environment.

Read Blog

### How ambient mesh challenges the security gaps in sidecar workloads

Discover how Istio’s ambient mesh strengthens microservices security beyond sidecars with improved isolation, reduced attack surfaces, and simpler operations.

Read Blog

### Migrating from sidecars to ambient with zero downtime

Learn how to migrate from Istio sidecars to ambient mesh with zero downtime. Step-by-step strategies, best practices, and tools to ensure a safe transition.

Read Blog

### Comparing Istio's ambient multicluster support with Gloo Mesh's multicluster peering

Compare Istio’s new ambient multicluster support with Gloo Mesh’s multicluster peering. Learn the similarities, key differences, and scalability trade-offs.

Read Blog

### The future of Kubernetes is context-aware: Meet Solo Enterprise for kagent

Discover how Solo.io's enterprise version of kagent extends Kubernetes to turn cloud-native infrastructure into agent-native infrastructure.

Read Blog

### kgateway as Ingress for Ambient Service Mesh

Explore how kgateway and Istio Ambient Mesh work together to deliver secure ingress, intelligent routing and clear observability.

Read Blog

### Tracing GenAI Applications Is Not Enough

Read Blog

### Gloo Mesh 2.10: More Secure, Scalable Cloud Connectivity

Gloo Mesh 2.10 adds flat network support, traffic shifting, and policy enforcement for secure, scalable multi-cluster service mesh.

Read Blog

### MCP Authorization is a Non-Starter for Enterprise

In this blog, we highlight some of MCP's foundational challenges, alternative proposals in the community, and sharing our opinion on what this should look like in enterprise environments. We know the MCP community is hard at work on revising the specification and we feel future updates will align better with our recommendations here.

Read Blog

### Securing and Observing Your Services, Simplified

Istio Ambient Mesh’s ztunnel delivers secure-by-default microservices communication and real-time traffic visibility - without sidecars. Learn how it boosts performance, simplifies management, and reduces costs while enhancing security and observability.

Read Blog

### From MCP Servers to Services: Introducing kmcp for Enterprise-Grade MCP Development

Read Blog

### The Power of a Single API to Secure, Observe, and Control Traffic in All Directions

Learn how the Omni vision unifies traffic, security, and observability control across cloud-native systems with Gloo Mesh and Gloo Gateway.

Read Blog

### Why Building Large Kubernetes Clusters Is (Still) a Bad Idea

Running massive Kubernetes clusters might seem simpler, but it’s a trap. Learn why scaling a single cluster creates hidden performance, security, and reliability issues, and how Gloo Mesh with Ambient Mesh makes multi-cluster networking finally viable.

Read Blog

### Fortifying Your Cloud Native Connectivity Security Posture with Solo and Ambient Mesh

Strengthen your cloud-native security posture with Istio and ambient mesh. Learn how ambient enhances zero-trust architecture, simplifies mTLS, reduces attack surface, and decouples security from app logic, all with less operational overhead.

Read Blog

### Migrating from Sidecars to Ambient Mesh - Risks, Challenges, and Benefits

Considering migrating from Istio sidecars to ambient mesh? Learn about the key challenges, risks, and benefits of ambient, including improved performance, lower costs, and operational simplicity, plus tips to plan a safe, successful transition.

Read Blog

### Overhaul of Agent Gateway supporting A2A, MCP, and Kubernetes Gateway API

Today, we’re excited to share the next major milestone: Agent Gateway is now a full-featured, AI-native gateway that combines deep MCP and A2A protocol awareness, robust traffic policy controls, inference gateway support, Kubernetes Gateway API support, and unified access to major LLMs, all purpose-built with Rust for real-world agentic systems.

Read Blog

### How Ambient Mesh Delivers Advanced Resource and Cost Savings

Discover how Ambient Mesh architecture can reduce service mesh infrastructure costs by up to 92% compared to traditional sidecar deployments, with real-world savings

Read Blog

### Getting Started with Ambient Mesh: From 0 to 100 mph

Learn how Ambient Mesh revolutionizes service mesh architecture by eliminating sidecars and introducing a split proxy approach for better performance and operational simplicity.

Read Blog

### Agent Discovery, Naming, and Resolution - the Missing Pieces to A2A

While the A2A specification provides the critical first steps toward discovery with Agent Cards, the infrastructure for truly dynamic, scalable agent ecosystems requires additional components that the spec intentionally leaves “up to you.” In this blog, we dig into those missing pieces.

Read Blog

### Part Two: MCP Authorization The Hard Way

Digging into the details of the MCP Authorization Spec

Read Blog

### Part One: MCP Authorization The Hard Way

Deep dive into MCP Authorization, step by step with examples and in-depth detail

Read Blog

### Agent Identity and Access Management - Can SPIFFE Work?

Digging into AI identity and how the current SPIFFE models may need to be revised to support AI Agents

Read Blog

### Deep Dive into llm-d and Distributed Inference

Digging into the llm-d project and how it does distributed inference.

Read Blog

### Gloo Mesh 2.8 simplifies service mesh operations with new enhanced user experience across multi-cluster environments.

Read Blog

### Gloo Gateway 1.19 accelerates context-rich, real-time AI apps with Gateway API

Read Blog

### llm-d: Distributed Inference Serving on Kubernetes

Read Blog

### Motive

Motive modernized its infrastructure using Solo Enterprise for kgateway to boost reliability, developer agility, and fleet innovation.

Read Case Study

### Confluent

Discover how Confluent achieved 100% mTLS coverage, FedRAMP-ready FIPS encryption, and real-time observability across 100+ services using Solo Enterprise for Istio.

Read Case Study

### Ingenico

Powered by Solo Enterprise for kgateway, Solo.io helped Ingenico modernize its global payments infrastructure—boosting scalability, resilience, and developer autonomy. Explore their journey to building a fault-tolerant, future-ready platform.

Read Case Study

### OfferUp

OfferUp leveraged Kubernetes and Solo Enterprise for kgateway to modernize its marketplace, enabling developer self-service, faster deployments, and seamless scaling beyond peer-to-peer transactions.

Read Case Study

### ParkMobile

ParkMobile’s Platform Engineering team utilized Kubernetes and Solo Enterprise for kgateway to drive innovation, scalability, and seamless mobility solutions while fostering a culture of collaboration and technological excellence.

Read Case Study

### Vonage

Solo.io helped Vonage modernize its cloud infrastructure, enhancing scalability, reliability, and developer autonomy with Solo Enterprise for kgateway. Explore their journey to a building an efficient and agile platform.

Read Case Study

### Domino’s Pizza

Powered by Solo Enterprise for Istio and Solo Enterprise for kgateway, Solo.io helped Domino’s UK transition from a monolithic system to a microservices-based architecture. Learn about our 18-month journey to transform the way they operate.

Read Case Study

### Introducing Solo Enterprise for agentgateway

Secure, govern, and operationalize AI agent connectivity at scale with Solo Enterprise for agentgateway

Read Datasheet

### Comparing Sidecars with Sidecarless Mesh Implementation

Compare sidecar-based Istio with sidecarless Ambient Mesh. Learn how Gloo Mesh simplifies service mesh operations, reduces overhead, and enables scalable, secure, multi-cluster environments — with support for both migration paths.

Read Datasheet

### Solo Enterprise for Istio Feature Comparison

Compare features across Gloo Mesh Enterprise, Gloo Mesh Open Source, and Basic Open Source Istio.

Read Datasheet

### Enterprise Support for Istio in Production

Solo.io provides enterprise support for Istio environments to help you avoid pitfalls and resolve issues quickly.

Read Datasheet

### Service Mesh for Developers, Part 1: Exploring the Power of Observability and OpenTelemetry

Navigating the complexity of modern applications requires a key ally – observability. Observability empowers teams to streamline application debugging, and within the architecture of a service mesh, provides valuable insights that increase reliability and performance.

Read Ebook

### Service Mesh at Scale

Challenges and approaches to multi-cluster deployment patterns

Read Ebook

### Compare Capabilities of the Top Service Mesh Platforms

Using a service mesh as a layer to unify communications between applications, services, and workloads empowers teams to modernize their systems, deliver faster results, and improve performance for modern enterprises.

Read Ebook

### Compare Capabilities of the Top API Gateways

Download our Buyer’s Guide to API Gateways and learn about the modern requirements of API gateways in our guide’s comparison of five leading API gateway providers.

Read Ebook

### Establishing zero trust security for modern cloud architectures

How your organization can ensure safer cloud architecture by applying a zero trust network security model

Read Ebook

### Unlocking the Power of Your API Gateway

With automated API management, organizations save time and resources and streamline the development process.

Read Ebook

### API Gateways: Productivity, Resilience, and Security for Next-Generation Cloud Applications

The rise of microservices architecture has brought about a significant shift in how software is developed and deployed, and as such, has presented new technical and organizational challenges.

Read Ebook

### Driving Business Value with Istio

How a service mesh can help your organization simplify the adoption of a distributed architecture

Read Ebook

### Service Mesh Vendor Comparison

See how top vendors with Istio-based service mesh offerings compare

Read Ebook

### Istio Then & Now

Read Infographic 

### 4 Reasons Why You Need an AI Gateway

Integrating LLM models in your applications? See our infographic to learn the top four reasons why you need an AI Gateway!

Read Infographic 

### Solo Enterprise for kgateway vs. Kong

Kong Gateway offers a very capable competitor to Gloo Gateway by Solo.io, but there are growing questions about the efficacy and stability of the Nginx open-source community behind the technology.

Read Infographic 

### Solo Enterprise for kgateway vs. Apigee

Apigee suits Google Cloud, but its traditional approach clashes with modern practices. In contrast, Gloo Gateway by Solo.io aligns with cloud-native strategies.

Read Infographic 

### 3 Reasons You Need an API Gateway for Microservices Apps

Unlock the full potential of your microservices architecture with the strategic integration of API gateways. While microservices provide flexibility and scalability, they also introduce complexities that can impede seamless communication between services. Discover the crucial role of API gateways in overcoming these challenges and optimizing your microservices ecosystem.

Read Infographic 

### Migrate to agentgateway with the ingress2gateway tool

Learn to migrate your ingress-nginx Ingress configurations to agentgateway with the ingress2gateway tool.

Read Lab

### Migrate to kgateway with the ingress2gateway tool

Learn to migrate your ingress-nginx Ingress configurations to kgateway with the ingress2gateway tool.

Read Lab

### Introduction to agentregistry

Free Lab: Learn how to curate, publish, and deploy MCP servers and AI skills using agentregistry for unified management of AI-native artifacts.

Read Lab

### Build AI agents with agent skills

Free Lab: Learn to build a declarative AI agent in kagent with a Kubernetes deployment skill, enabling automated app deployments and MCP tool integration.

Read Lab

### Program agentgateway for LLM consumption

Free Lab: Learn to proxy OpenAI requests through an agentgateway-backed AI gateway with kgateway, managing LLM traffic, credentials, and advanced features.

Read Lab

### Local development with the kagent CLI

Free Lab: Learn to build, run, and deploy AI agents with kagent, integrate MCP servers, and manage tools in Kubernetes for AI-native workloads.

Read Lab

### Secure your MCP servers with OAuth

Free Lab: Learn to build, proxy, and secure an MCP server with agentgateway and OAuth2, protecting AI-native workloads while enabling safe tool access in Kubernetes.

Read Lab

### Improve cloud native operations & troubleshooting with kagent

Free Lab: Use AI agents with kgateway and kagent to automate Kubernetes tasks, provision gateways, route traffic, and manage workloads in a cloud-native environment.

Read Lab

### Observe Agent & MCP server interactions

Free Lab: Learn how to use Solo Enterprise for kagent to create, run, and monitor AI agents in Kubernetes with full observability and control.

Read Lab

### Multiplex MCP servers & control auth policy

Solo Free Lab: Learn how to use kgateway and agentgateway to deploy, proxy, and secure MCP servers in Kubernetes with AI-native control and traffic routing.

Read Lab

### Build, run & deploy MCP servers to Kubernetes

Solo Free Lab: Learn to use the new kmcp tool to easily deploy MCP servers to Kubernetes.

Read Lab

### Kagent Lab: Discover kagent and kmcp

Explore the kagent project to build custom agents and tools

Read Lab

### Solo Enterprise for Istio Lab: OpenTelemetry collectors and relay

Solo.io Free Lab: Learn about the relay of telemetry from a workload cluster to the management cluster in Gloo Mesh.

Read Lab

### Solo Enterprise for Istio Lab: Extended telemetry from ztunnel

Solo.io Free Lab: Learn how to deploy Istio Ambient Mesh with Gloo Mesh to capture Layer 7 telemetry directly from zTunnel - no waypoints required.

Read Lab

### Solo Enterprise for Istio Lab: Configure enhanced waypoint proxies

Solo.io Free Lab: Learn how to use Gloo Gateway for your waypoints in Gloo Mesh, instead of Istio's default waypoint proxy.

Read Lab

### Solo Enterprise for Istio Lab: Multicluster peering

Solo.io Free Lab: Learn how to enable multicluster peering in Gloo Mesh to run services across clusters as a single mesh, making workloads visible and accessible between clusters with global failover and redundancy.

Read Lab

### Ambient Mesh Lab: EnvoyFilter Support

Solo.io Free Lab: Learn how to preserve and migrate EnvoyFilter configurations when transitioning from sidecar to ambient mode in Istio using Solo.io’s extended build, with step-by-step guidance and validation.

Read Lab

### Ambient Mesh Lab: SPIRE integration with Gloo Mesh in Istio Ambient Mode

Secure your Istio Ambient Mesh with SPIRE. This hands-on lab shows how to integrate SPIRE with Gloo Mesh to issue SPIFFE identities and certificates for ztunnel and mesh workloads.

Read Lab

### Ambient Mesh Lab: Introduction to ztunnel in Ambient Mesh

Learn how Ambient Mesh uses ztunnel to secure traffic without sidecars. This free lab walks you through joining workloads, observing traffic, verifying mTLS, and applying Layer 4 policies.

Read Lab

### Solo Academy Course: Service Mesh Basics

Solo Academy | Learn the fundamentals of service mesh in this free video-led course and get insights into using a service mesh to enhance your observability, security and reliability of your applications

Read Lab

### Solo Academy Course: Istio Basics

Solo Academy | Learn the basics of Istio with our free 101 course. Understand what Istio is, how it works, and its features for traffic management, security, and observability in microservices and Kubernetes.

Read Lab

### Solo Academy Course: Envoy Basics

Solo Academy | Master Envoy Proxy basics with our free 101 level course. Learn about the architecture, advanced load balancing, observability, and role in microservices, Kubernetes, and service meshes

Read Lab

### Solo Academy Course: API Gateway Basics

Solo Academy | Learn API Gateway fundamentals in Kubernetes with this free beginner level video-led course. Discover how API Gateways control traffic, secure connectivity, and complement microservices architecture

Read Lab

### Solo Academy Course: Get Started with Istio Service Mesh

Solo Academy | A fundamental level workshop for developers and operators to learn Istio service mesh. Install Istio, secure services, control traffic, and earn a Solo.io certification through hands-on labs.

Read Lab

### Solo Academy Course: Introduction to Envoy Proxy

Solo Academy | Hands-on workshop introducing the core concepts of Envoy Proxy. Learn how Envoy works under the hood from its architecture, filter chains, and request flow and beyond the abstractions of service meshes and API gateways.

Read Lab

### Solo Academy Course: Deploying Istio for Production

Solo Academy | Free hands-on workshop for operators looking to deploy Istio in production. Learn advanced routing, observability, security, mTLS, and multi-cluster setup and g free certification.

Read Lab

### Kgateway Lab: Integrating kgateway with Istio at Ingress

Explore how to integrate kgateway's ingress gateway with Istio Ambient Mesh in this free hands-on lab. Learn to deploy workloads, configure Gateway and Route resources, and enable automatic mutual TLS between the gateway and backend services.

Read Lab

### Kgateway Lab: Kgateway as a Waypoint

Learn how to deploy and configure kgateway as a waypoint in Istio Ambient Mesh. This free hands-on lab walks you through managing east-west traffic, applying custom policies, and enhancing service communication with enterprise-grade control.

Read Lab

### Kgateway AI Lab: Deploying kgateway as an AI Gateway

Learn how to enable the AI extension, configure gateway parameters, and deploy an AI Gateway using kgateway to route requests to large language models (LLMs) from within your Kubernetes cluster.

Read Lab

### Kagent Lab: How to build an AI agent

Create Your First AI Agent with Kagent in Kubernetes

Read Lab

### Kagent Lab: Integrate tools from MCP servers with kagent

Kagent Lab: Integrate tools from MCP servers with kagent

Read Lab

### agentgateway Hands-On Lab: Semantic Caching

agentgateway Labs | Semantic Caching with Gloo AI Gateway

Read Lab

### Kgateway AI Lab: Credentials Management

kgateway labs | Managing LLM Credentials with kgateway - AI Gateway

Read Lab

### Kgateway AI Lab: Prompt Enrichment

Kgateway labs | Managing Prompts for Enhanced LLM Performance

Read Lab

### Kgateway AI Lab: Prompt Guards

kgateway labs | Content Safety with Prompt Guards

Read Lab

### Ambient Mesh Lab: Migrating from Sidecar to Sidecarless

Ambient Mesh Lab | Migrate from Sidecar-based Service Mesh to Ambient Mesh

Read Lab

### Ambient Mesh Lab: Multi-cluster scalability with Istio Ambient Mesh

Mastering Multi-Cluster Scalability with Ambient Mesh

Read Lab

### Solo Lab: Gloo Cloud Preview

Simplify Mesh Management with Gloo Cloud: Onboarding, Ingress, Egress, and Service Mesh

Read Lab

### Ambient Mesh Lab: Waypoints for Traffic management, Security and Observability

Solo Lab | Waypoints in Ambient Mesh: For L4 and L7 Security, Traffic and Observability Insights

Read Lab

### Kgateway Lab: Gateway API inference extensions with kgateway

Exploring the Gateway API Inference Extension with kgateway

Read Lab

### Kgateway Lab: Securing access to workloads with Gloo Gateway

Securing Services with Gloo Gateway: TLS Termination and API Keys

Read Lab

### Kgateway Lab: Route Delegation in kgateway

Route Delegation in kgateway

Read Lab

### Kgateway Lab: Canary releases with Argo Rollouts & kgateway

Canary releases with Argo Rollouts & kgateway

Read Lab

### Kgateway Lab: Understanding kgateway and Gateway API policy attachments

Understanding kgateway patterns of extensions

Read Lab

### Kgateway Lab: Gateway API support for service mesh with kgateway

GatewayAPI support for service mesh with kgateway

Read Lab

### Kgateway Lab: Exploring HTTPRoute resource configurations with kgateway

Exploring HTTPRoute resource configurations with kgateway

Read Lab

### Kgateway Lab: Configuring gateways across multiple teams with kgateway

Configuring gateways across multiple teams with kgateway

Read Lab

### Kgateway Lab: Configure HTTPS with the Gateway API and kgateway

Configure HTTPS with the Gateway API and kgateway

Read Lab

### Kgateway Lab: Understanding the basics of Kubernetes Gateway API with kgateway

Understanding the basics of Kubernetes Gateway API with kgateway

Read Lab

### Kgateway Lab: Installing kgateway, an open-source implementation of the Kubernetes Gateway API

Installing kgateway, an open-source implementation of the Kubernetes Gateway API

Read Lab

### Ambient Mesh Lab: Employing circuit breaking in Ambient Mesh

Join our free, on-demand lab Employing Circuit Breaking to safeguard services with Istio Ambient mode. Learn to deploy waypoints, configure circuit breaking, and monitor using metrics, logs, and Prometheus.

Read Lab

### Ambient Mesh Lab: Configuring Fault Injection in Ambient Mesh

Join our free, on-demand lab Configuring Fault Injection to enhance resiliency with Istio Ambient mode. Learn to observe system latency, configure delays, timeouts, retries, and augment with outlier detection.

Read Lab

### Ambient Mesh Lab: Using Outlier Detection with Ambient Mesh

Join our free, on-demand lab Using Outlier Detection to learn how to configure Istio Ambient mode to avoid unhealthy workloads. Discover steps to implement outlier detection, assess workload health, and monitor metrics effectively.

Read Lab

### Ambient Mesh Lab: Implementing Timeouts with Ambient Mesh

Join our free on-demand lab, Implementing Timeouts, and learn how to protect applications from slow upstream services with Istio. Discover how to prevent indefinite errors, configure and verify timeouts, and decouple resiliency concerns from your apps.

Read Lab

### Kgateway Lab: Exposing, Securing, and Rate Limiting with kgateway

Free K8s Gateway Lab: Deploy, Secure, and Rate Limiting with Solo's Open Source Gateway

Read Lab

### Ambient Mesh Lab: Traffic routing with waypoints in Ambient Mesh

Learn how to route traffic using waypoint proxies in ambient mesh.

Read Lab

### Ambient Mesh Lab: Secure Your Cluster with Ambient Mesh and mTLS

Learn how to secure services in your Kubernetes cluster using ambient mesh and mTLS.

Read Lab

### Ambient Mesh Lab: Access control with authorization policies

Learn how to enforce access control and write authorization policies for L4 and L7 traffic.

Read Lab

### Ambient Mesh Lab: Getting Started with Ambient Mesh

Learn the basics of ambient and how to set up your first environment.

Read Lab

### Ambient Mesh Lab: Getting L4 and L7 observability

Learn how to view metrics and traces from L4 and L7 traffic in ambient mesh.

Read Lab

### agentgateway Hands-On Lab: Prompt Management and Prompt Guards

Sign up for the free, hands-on technical labs.

Read Lab

### agentgateway Hands-On Lab: Rate Limiting and Model Failover

Sign up for the free, hands-on technical labs.

Read Lab

### agentgateway Hands-On Lab: RAG and Semantic Caching

Sign up for the free, hands-on technical labs.

Read Lab

### agentgateway Hands-On Lab: Credentials and Access Control

Sign up for the free, hands-on technical labs.

Read Lab

### AI Agents in Kubernetes

Read Report

### Gartner® Report: How to Adapt Your API Strategy to Succeed in the AI Era

As organizations unlock the potential of generative AI, one thing is clear: a modern, scalable API strategy is essential. In this complimentary Gartner® report learn how software engineering leaders can evolve their API programs to accelerate innovation, reduce risk, and control costs in the AI era.

Read Report

### AI Gateways in the Enterprise

Read Report

### API Gateway Resource Kit

A service mesh is a dedicated infrastructure layer that helps manage and secure communications between microservices within a distributed application.

Read Blog

### Service Mesh Resource Kit

A service mesh is a dedicated infrastructure layer that helps manage and secure communications between microservices within a distributed application.

Read Blog

### AI Agents Are Not APIs. Existing Gateways Can't Tell the Difference.

Read Whitepaper

### Building Responsive and Resilient Multi-Cluster Applications with Solo’s Ambient Mesh

Read Whitepaper

### Busting 10 Myths About Istio Ambient and Sidecarless Service Mesh

Read Whitepaper

### Guide to Migrating from Ingress to Gateway API

Migrate your project from ingress-nginx and the Ingress API to the Kubernetes Gateway API with kgateway—an open-source Gateway project powered by Envoy.

Read Whitepaper

### Migrating from Sidecars to Sidecarless Istio Ambient Mesh

In our white paper Migrating from Sidecars to Sidecarless to Ambient Mesh, we share how sidecars and Ambient mode can work together, allowing for a gradual migration strategy.

Read Whitepaper

### Introduction and Best Practices to AI Gateways

Read Whitepaper

### Choosing the Right AI Gateway For You

Read our white paper and learn how to select the right AI Gateway to help you navigate the challenges of working with AI workloads.

Read Whitepaper

### Solo.io’s Guide to Navigating GenAI Complexity

Read Whitepaper

### Unlocking Business Efficiency with Service Mesh Updates in AWS

Read Whitepaper

### Evolve Your API Management

Read Whitepaper

### Transitioning From App Mesh to Istio for AWS EKS

Read Whitepaper

### How Service Mesh Supports a Zero Trust Architecture

Read Whitepaper

### Achieve Compliance, Zero Trust with Istio Ambient Mode

Read Whitepaper

### Get started

See why Solo.io is the leading provider of API Gateway and service mesh solutions.

Learn more

### Istio support

Is Istio not working properly for you? Are you having performance issues with your Istio instance? Is there an upgrade you need to manage on multiple clusters?

Get support

### Pricing

Reach out for tailored pricing options and step into a future of enhanced connectivity.

Get Started

### Book a Gloo AI Gateway demo

Powered by Istio, Gloo Mesh empowers platform engineering teams to boost security, resiliency, and observability.

Get started

### Book a Gloo Gateway demo

Gloo Gateway is a fast, Kubernetes- native API gateway packed with features IT operations teams need to deliver a full lifecycle security strategy for their cloud-native environments.

Get started

### Gloo Mesh - Ambient Readiness Assessment

A free program designed to assess your readiness for Istio Ambient adoption and prove the business benefits based on your own environment.

Get started

### Book a Gloo Mesh demo

A free program designed to assess your readiness for Istio Ambient adoption and prove the business benefits based on your own environment.

Get started

### Case Studies

Learn more

### Ebooks

Learn more

### Labs

Learn more

### Reports

Read Reports

### Resource Kits

See Resource Kits

### Webinars

A free program designed to assess your readiness for Istio Ambient adoption and prove the business benefits based on your own environment.

Watch Webinars

### Whitepapers

A free program designed to assess your readiness for Istio Ambient adoption and prove the business benefits based on your own environment.

Read Whitepapers

### Gloo AI Gateway

Secure, observe, and control your AI applications with Gloo AI Gateway, the leading cloud native gateway built on Envoy.

Learn more

### Gloo Gateway

The future of cloud APIs is omni.

Learn more

### Gloo Mesh

Connecting, securing, controlling, and observing microservice communication is tough. We make it accessible to all.

Learn more

### Datasheets

Read Datasheets

### Infographics

Read Infographics

### Videos

Watch Videos

## Cloud connectivity done right

Get started