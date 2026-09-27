---
title: 'Docker Launched Cloud Sandboxes: Containers Weren’t Designed for AI Agent Isolation – Forkast'
url: https://forkast.news/docker-launched-cloud-sandboxes-containers-werent-designed-for-ai-agent-isolation
site_name: tldr
content_file: tldr-docker-launched-cloud-sandboxes-containers-werent
fetched_at: '2026-09-27T21:52:07.005244'
original_url: https://forkast.news/docker-launched-cloud-sandboxes-containers-werent-designed-for-ai-agent-isolation
date: '2026-09-27'
published_date: '2026-09-25T20:18:31+00:00'
description: Docker's president says containers aren't sufficient for agent isolation. The company that defined containers is now defining the post-container execution model for AI agents.
tags:
- tldr
---

Docker, the company that made containers the default deployment model for cloud applications, has drawn a line between containers and AI agents. On September 24, 2026, Docker launched Cloud Sandboxes, extending its local sandbox isolation technology to Docker-managed cloud infrastructure. The message is explicit: containers were not designed for the level of isolation AI agents demand.

The core of this launch is microVM-based isolation – not containers. Each Cloud Sandbox runs in a dedicated microVM with its own kernel and hardware-level isolation (Intel VT-x / AMD-V), powered by a custom-built VMM that Docker developed specifically for this use case. This is not Firecracker or libkrun; it is a cross-platform virtual machine monitor that runs natively on macOS, Windows, and Linux via each platform’s native hypervisor.

## The Container Company’s Admission

The architecture addresses a specific limitation of the container model. Containers share a kernel with the host, which means a compromised container can potentially reach the host system through kernel-level exploits. MicroVMs provide a hard security boundary: each sandbox gets its own kernel, making kernel-level escape significantly harder. Docker’s custom VMM is optimized for fast cold starts – the company describes them as sub-second, though specific benchmarks for Cloud Sandboxes have not been published independently.

Docker’s president, Mark Cavage, stated: “While the containers Docker is known for still have a critical role to play, they weren’t designed for the level of isolation AI agents demand. That’s why we introduced local sandboxes as a new, separate solution earlier this year, and why we’re now extending the same level of isolation and control to the cloud.”

## Cloud Extension for Unattended Agents

The cloud extension is designed for unattended agentic workflows. When a developer’s laptop shuts down, the agent’s workflow continues running on Docker-managed infrastructure. There is no persistent state retained in the microVM – each sandbox is killable and restartable on demand. This removes the binary choice between local execution (where the developer must keep their machine running) and cloud execution (where the developer loses control over the execution environment).

 

Advertisement

The security controls extend beyond isolation. A network egress firewall denies all outbound traffic except the agent’s own API endpoints and explicitly allowed domains. Credentials are injected via a network proxy – secrets are inserted into requests as authentication headers only when the hostname matches, so agents never see raw host credentials. This is defense-in-depth: even if an agent is compromised, it cannot exfiltrate credentials or reach unauthorized endpoints.

## Kits: Access Rules Travel with the Agent

Docker has also published the next generation of its Kits specification (v3), an open standard for packaging an agentic sandbox as a standard OCI image. Kits define access rules – network permissions, credential proxies, volume mounts, port mappings, and skill paths – that travel inside the image itself. Each rule is a request, not a grant: the host runtime decides whether to honor it, with deny-by-default semantics. If the host cannot satisfy a required request, the launch is refused rather than starting with incorrect permissions.

The Kits specification integrates with MCP (Model Context Protocol) through a gateway that allows developers to register MCP servers and connect them to sandboxed agents. Docker has committed to submitting the Kits specification to the Cloud Native Computing Foundation (CNCF) for neutral governance, publishing it under Apache 2.0.

## The Harness Pattern Reaches the Runtime Layer

This launch is significant because of who is making it. Docker defined the container paradigm. When the company’s president says containers are not sufficient for agent isolation, it is not a competitor dismissing containers – it is the container company acknowledging that a different execution model is required for autonomous agents.

The pattern matches what this publication has documented across the agent infrastructure stack this week.AWS Strands, DigitalOcean, and Aivenshipped opinionated agent harnesses at the cloud provider level.LangChainshipped the same pattern at the framework level.Cloudflareshipped it at the edge layer. Docker is now shipping it at the container runtime layer – the deepest layer in the stack where the harness pattern has taken hold.

The deeper issue is whether this microVM-based isolation becomes the new default for agent execution. Docker’s approach – custom VMM, OCI-compatible Kits, MCP integration, CNCF governance – suggests a long-term infrastructure play rather than a point solution. If Docker Sandboxes become the standard runtime for AI agents, the company that defined containers will have defined the post-container execution model for theagent economy.

Standardization has now reached every layer of the stack. The requirements for agentic systems – persistent state, secure authentication, controlled execution, and now hardware-level isolation – are being met with identical architectural solutions from cloud providers, framework maintainers, edge platforms, and container runtimes. The harness pattern is no longer a trend; it is the baseline.