---
title: Introducing the JFrog Plugin for Claude Code
url: https://jfrog.com/blog/introducing-the-jfrog-plugin-for-claude-code/
site_name: tldr
content_file: tldr-introducing-the-jfrog-plugin-for-claude-code
fetched_at: '2026-06-22T20:05:09.244791'
original_url: https://jfrog.com/blog/introducing-the-jfrog-plugin-for-claude-code/
author: zoer
date: '2026-06-22'
published_date: '2026-06-10T13:10:23+00:00'
description: Learn how the JFrog plugin for Claude Code brings security awareness into your AI-assisted development workflow.
tags:
- tldr
---

AI coding agents are changing the pace of software development. With tools like Claude Code, developers can move from idea to implementation faster than ever, generating code, exploring unfamiliar repositories, refactoring services, and turning plain-language intent into working software. That speed is powerful. But speed without governance = risk. It also creates a new challenge:how can you govern what an AI agent builds, suggests, and pulls in from the internet?

The JFrog plugin for Claude Code answers that question directly. It gives your AI coding agent real-time access to security scanning, package safety checks, governed MCP server management, and artifact workflows, all from inside your development environment.

## Why AI-assisted Development Needs Governed Guardrails

Claude Code and similar agentic development tools are designed to help developers stay in flow; reasoning across files, suggesting changes, generating code, and automating repetitive tasks directly in the development environment. For developers, this is a major productivity unlock. For engineering and security teams, it also raises an important question:how do you ensure the output of an AI agent meets your organization’s security and governance expectations?

Traditional application security workflows operate later in the pipeline: pull request reviews, CI/CD scans, artifact promotion, and release gates. Those controls remain important. But AI-assisted development compresses the time between a code suggestion and a build artifact. When Claude Code recommends a dependency or writes an implementation pattern, that choice can propagate downstream through your entire software supply chain, from source to package to container to production.

That compression is where governance gaps form. Without security context at the moment of development, AI-generated code can introduce the same issues that have always challenged software teams: vulnerable dependencies, risky open-source packages, and non-compliant implementation patterns — all at the speed and scale of an AI agent. And the rework that follows isn’t just a security problem; it’s a cost problem. Every remediation cycle burns developer time and token budget, turning a productivity tool into a source of compounding overhead.

Anthropic hasflagged the systemic nature of this challenge, noting that as agents become more capable, attack surfaces keep shifting — and that the failures seen so far are likely to repeat across industries unless the field collectively invests in agent-specific security posture, from shared benchmarks and cross-vendor red-teaming to common identity standards and coordinated disclosure norms.

## What Does the JFrog Plugin for Claude Code Do?

The JFrog plugin for Claude Code integrates the JFrog Software Supply Chain Platform directly into your Claude Code workflow. Once installed and authenticated, the plugin gives your AI agent four core capability areas.

Here’s what the plugin enables:

JFrog Artifactory integration— Claude Code can interact with your Artifactory repositories, builds, permissions, access tokens, projects, and release bundles via the JFrog CLI and REST/GraphQL APIs. Security audits, CVE lookups, and JFrog Advanced Security exposure queries are available through natural language.

Package safety checks via JFrog Curation— Before downloading a dependency, the plugin checks whether packages from npm, Maven, PyPI, Go, and other ecosystems are safe, curated, or policy-compliant. Packages are downloaded through Artifactory remote caches or curation-aware package managers — not directly from public registries.

Governed MCP server management via Agent Guard— Claude Code manages MCP servers through the JFrog Agent Guard feature. You can discover, install, configure, update, and remove MCP servers approved for your project from the JFrog AI Catalog, with authentication via OAuth, API key, or bearer token.

Platform administration— Plugin capabilities extend to platform administration workflows, supporting SDLC operations across the full software supply chain.

Together, these capabilities mean your AI coding agent is no longer operating outside your governance model. Claude Code can accelerate development while staying connected to the same security and compliance controls your team relies on everywhere else.

## How Does the JFrog Plugin Help Security and Platform Teams?

Modern software delivery is not just about source code. It includes open source packages, internal components, build artifacts, containers, models, configuration, metadata, and the policies that determine what can safely move toward production. AI coding agents operate at the beginning of that chain, but their impact can flow all the way downstream.

Security and platform teams face a structural challenge with AI coding tool adoption: blocking these tools is unrealistic, and adding manual review at every step doesn’t scale. The answer isn’t a later gate — it’s an earlier one. The JFrog plugin for Claude Code brings governance into the developer workflow itself, connecting AI-assisted development to the same software supply chain practices your team relies on everywhere else.

The JFrog plugin for Claude Code supports that goal in three ways:

1. Dependency governance at the point of suggestion— When Claude Code suggests a package, JFrog Curation checks it against your organization’s policies before it enters your environment. Malicious packages, non-compliant licenses, and unapproved versions are blocked before they ever reach a developer’s machine.
2. MCP server control via the JFrog AI Catalog— Unmanaged MCP servers carry real security risks: prompt hijacking vulnerabilities, over-privileged access, and credential exposure. Agent Guard gives security teams a governed registry of pre-approved MCP servers, ensuring AI agents only connect to trusted integrations.
3. Artifact traceability through JFrog Artifactory— Every artifact the AI agent interacts with goes through Artifactory. Build provenance, access controls, and release bundle management remain intact regardless of how quickly the agent is working.

It’s also worth noting that the JFrog plugin for Claude Code is part of a broader strategy, not a one-off integration. JFrog is building governance infrastructure designed to work across any AI coding environment (Claude Code, Cursor, GitHub Copilot, and others), so that security and compliance travel with the developer regardless of which agent they’re using. The goal is a universal system of record for software artifacts and AI assets that doesn’t have to be rebuilt every time the tooling landscape shifts.

The result is a more balanced model for AI adoption. Developers use Claude Code to move faster. Security teams retain the controls they need. Neither team has to choose between velocity and responsibility.

## What This Means for Your Development Team

For developers, the promise of AI coding tools isn’t simply writing more code. It ‘s reducing toil, accelerating exploration, and focusing on higher-value engineering decisions. That promise breaks down when security shows up as a separate step after the work is done. The JFrog plugin for Claude Code keeps it intact: security context arrives where you’re already working, as part of the workflow rather than a gate at the end of it.

This is especially important as organizations move from individual experimentation with AI coding tools to broader team adoption. The more AI becomes part of everyday engineering, the more important it becomes to make those workflows observable, governed, and aligned with trusted software delivery practices. The JFrog plugin connects Claude Code to the governance infrastructure your organization has already built — so that infrastructure scales alongside your AI adoption, not behind it.

### What the plugin delivers

The table below summarizes how the JFrog plugin creates value across your organization. Each stakeholder gets a concrete capability, not just a general promise about “security awareness.”

Stakeholder

What you get

Developer

Security-aware dependency checks and artifact access inside Claude Code, without workflow interruption

Security team

Policy enforcement at the point of AI-assisted development; governed MCP server management via Agent Guard

Platform team

Artifact traceability, access control, and release bundle management through JFrog Artifactory

Engineering leader

A governed AI coding workflow that scales with team adoption, not around it

 

## Getting Started with the JFrog Plugin for Claude Code

The JFrog plugin is available now for Claude Code. Setup requires Claude Code CLI version 1.0 or higher, Node.js version 14 or higher with npx on your PATH, and a JFrog platform URL with a valid access token.

To install and start using the plugin, follow these steps:

1. Authenticate— Configure your JFrog credentials usingjf config addvia the JFrog CLI (recommended), or setJFROG_URLandJFROG_ACCESS_TOKENas environment variables.
2. Install the plugin— Run the plugin installation command from the Claude Code CLI or install directly from the Claude Plugins Official Marketplace.
3. Verify the installation— Confirm the plugin is active under/plugins Installedtab. Version 0.1.1 or higher is required.
4. Enable Agent Guard (optional)— If your JFrog subscription includes the AI Catalog entitlement, configure a JFrog project to activate governed MCP server management. Contact your JFrog account team if you need to confirm entitlement.

Once configured, you can interact with the JFrog plugin through natural language directly in Claude Code.

### Ship AI-Assisted Software You Can Trust

AI coding agents are now part of the modern developer toolkit. The question is no longer whether tools like Claude Code can help teams move faster. It’s whether your organization can make that speed safe, governed, and sustainable.

The JFrog plugin for Claude Code brings security awareness into your AI-assisted development workflow. It connects JFrog Artifactory, JFrog Curation, JFrog Xray, and Agent Guard directly to Claude Code so your AI agent works within your software supply chain governance model, not outside it. Security context arrives at the moment of development, not after the build, not after the release gate, but where decisions are actually made.

Speed is only valuable when you trust what you ship.Try the JFrog plugin for Claude Codeand bring a security conscience to your AI-assisted development workflow.