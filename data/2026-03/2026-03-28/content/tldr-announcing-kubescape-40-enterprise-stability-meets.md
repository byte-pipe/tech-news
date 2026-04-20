---
title: Announcing Kubescape 4.0 Enterprise Stability Meets the AI Era | CNCF
url: https://www.cncf.io/blog/2026/03/26/announcing-kubescape-4-0-enterprise-stability-meets-the-ai-era/
site_name: tldr
content_file: tldr-announcing-kubescape-40-enterprise-stability-meets
fetched_at: '2026-03-28T11:10:52.725297'
original_url: https://www.cncf.io/blog/2026/03/26/announcing-kubescape-4-0-enterprise-stability-meets-the-ai-era/
date: '2026-03-28'
published_date: '2026-03-26T08:00:00+00:00'
description: We are happy to announce the release of Kubescape 4.0, a milestone bringing enterprise-grade stability and advanced threat detection to open source Kubernetes…
tags:
- tldr
---

Posted on March 26, 2026by Ben Hirschberg, Kubescape Core Maintainer, ARMO CTO

CNCF projects highlighted in this post

We are happy to announce the release of Kubescape 4.0, a milestone bringing enterprise-grade stability and advanced threat detection to open source Kubernetes security. This version focuses on making security more proactive and scalable. It also introduces capabilities that allow AI agents to utilize Kubescape to scan clusters as well as enable security posture scanning for the AI agents themselves.

### Runtime Threat Detection Reaches General Availability (GA)

The highlight of this release is the GA of our Runtime Threat Detection. After rigorous testing, we’ve achieved proven stability at scale.

The engine is powered by CEL-based detection rules. These Common Expression Language rules are highly efficient and have direct access to Kubescape Application Profiles, which act as security baselines for your workloads.

Source: Kubescpe.io

Kubescape 4.0 monitors a comprehensive suite of events including:

* System Interactions:Processes, Linux capabilities, and System calls
* Connectivity:Network and HTTP events
* Storage:File system activities

For seamless operations, Rules and RuleBindings are now managed as Kubernetes CRDs. You can export alerts to your existing stack, including AlertManager, SIEM, Syslog, Stdout, and HTTP webhooks.Check out theKubescape documentationfor more information.

### Kubescape Storage Reaches General Availability (GA)

Kubescape Storage has officially reached GA. This component leverages theKubernetes Aggregated API, a Kubernetes-native feature, to act as a centralized repository for all security metadata.

By moving custom objects like Application Profiles, SBOMs, and vulnerability manifests into this dedicated storage layer, we’ve ensured that security data doesn’t overwhelm the standard etcd instance. This architecture has been proven to handle the demands of large-scale, high-density clusters, providing the performance required for modern enterprise environments.For more information, check outAmir Malka’s session at  Kubecon + CloudNativeCon North America 2025:Extending Kubernetes API: The Hidden Power of Aggregated Server Objects – Amir Malka, ARMO

### The Enhanced Node-Agent and Host-Sensor Deprecation

Based on community feedback regarding the complexity of node scanning, we have removed the host-sensor in Kubescape 4.0. While effective, this “pop-up” DaemonSet approach was often perceived as intrusive and difficult to monitor from a security perspective.

We have also officially removed the host-agent and integrated its capabilities directly into the node-agent. By establishing a direct API between the core Kubescape microservices and the node-agent, we’ve eliminated the need for ephemeral, high-privilege Pods. This architectural shift allows you to maintain a cleaner cluster environment with only one agent to manage, making your security posture both more stable and easier to audit.

### Kubescape Enters the AI Era

With the launch of Kubescape 4.0, we are addressing the unique challenges of the AI-native era by looking at security from two equally important perspectives. This focus is critical, as the same cloud native principles that scale modern infrastructure are foundational for the next generation of inference pipelines and intelligent, agentic AI systems. We like to think of this as the “two sides of the AI security coin”: using Kubescape to empower AI agents with cybersecurity capabilities and using Kubescape to secure those same agents.

#### Empowering AI Security Sidekicks

As AI inference becomes the next major cloud native workload and Kubernetes evolves into the platform for intelligent systems, Kubescape 4.0 introduces a KAgent-native plug-in, allowing AI assistants to analyze Kubernetes security posture directly from the cluster. This plug-in provides the following capabilities to the AI agent:

* Security Scanning:AI agents can list and inspect vulnerability manifests for CVEs and review configuration scans to identify RBAC issues or missing security contexts.
* Detailed Remediation:Agents can pull specific guidance to fix vulnerabilities.
* Runtime Observability:Using ApplicationProfiles and NetworkNeighborhoods, AI assistants can look at how containers behave in real life, like what system calls they make, what files they access, and how they communicate over the network.

This integration enables an AI agent to become a true security sidekick; assisting humans to interpret complex security states and make informed decisions.

#### Scanning the AI Posture

AI agents are beginning to gain more autonomy, meaning their infrastructure must be secured. We need robust security guardrails to stop agents from exploiting them for high-risk actions like unauthorized access or deleting production data. Kubescape 4.0 introduces security posture scanning specifically forKAgent, the CNCF Sandbox project for AI orchestration.

Since KAgent creates direct pathways between AI models and enterprise infrastructure, misconfigurations can be high-risk. Our new analysis identifies 42 security-critical configuration points across KAgent’s CRDs. We are introducing 15 Rego-based controls to detect issues such as:

* Empty security contexts in default deployments
* Missing NetworkPolicies
* Over-privileged controller-wide namespace watching

By applying these rigorous standards, we are ensuring that the “brains” of your AI operations are as secure as the workloads they manage.

### Compliance

In the continuously evolving cloud native landscape, robust governance and consistent, auditable compliance are the critical foundations that allow for safe and sustainable innovation. Kubescape continues to help keep your clusters compliant with the latest industry standards:

* CIS Benchmark Updates:Support for versions1.12(Vanilla Kubernetes) and1.8(EKS, AKS).

Community Corner

We’d like to welcome our new maintainer, Amir Malka, and thank our emeritus maintainers, David Wertenteil and Craig Box, for their contributions over the years.To join the Kubescape community and find information on how you can ask questions, join in the conversation, and contribute, visit the linkhere.

If you are a Kubescape user, we’d love to hear from you. Please reach out if you would like to share an interesting use case with the community or add yourself to our list ofadopters.
