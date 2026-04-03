---
title: 'Gemini CLI GitHub Actions: AI coding made for collaboration'
url: https://blog.google/technology/developers/introducing-gemini-cli-github-actions/
site_name: hackernews
fetched_at: '2025-08-08T04:06:52.341187'
original_url: https://blog.google/technology/developers/introducing-gemini-cli-github-actions/
author: michael-sumner
date: '2025-08-08'
published_date: '2025-08-06'
description: Today, we’re introducing Gemini CLI GitHub Actions. It’s a no-cost, powerful AI coding teammate for your repository. It acts both as an autonomous agent for critical routine coding tasks, and an on-demand collaborator you can quickly delegate work to.
---

# Meet your new AI coding teammate: Gemini CLI GitHub Actions

Aug 06, 2025

·

Gemini CLI GitHub Actions is a no-cost, powerful AI coding teammate for your repository. It acts both as an autonomous agent for critical routine coding tasks, and an on-demand collaborator you can quickly delegate work to.

Jerop Kipruto

 Senior Software Engineer


Ryan J. Salva

 Senior Director, Product Management


In June, we launchedGemini CLI, an open-source AI agent that brings the power of Gemini to your terminal. The enthusiastic adoption from developers has been incredible. To keep up with the flood of feature requests and contributions, we put our own tool to the test — using Gemini CLI to automate issue triage and pull request reviews. When community members noticed our new workflows, they asked us to share what we’ve built.

Today, we’re introducingGemini CLI GitHub Actions. It’s a no-cost, powerful AI coding teammate for your repository. It acts both as an autonomous agent for critical routine coding tasks, and an on-demand collaborator you can quickly delegate work to.

It’s now in beta, available to everyone worldwide, and you can find it on GitHub atgoogle-github-actions/run-gemini-cli.

### An AI teammate in your repository

While Gemini CLI is a tool built for individual use in your own terminal, Gemini CLI GitHub Actions was created for team collaboration on the platform where developers work with each other.

Triggered by events like new issues or pull requests, it works asynchronously in the background, using the full context of your project to automatically handle tasks. It knows your code, understands what you want to do, and gets it done.

We’re launching with three powerful, open-source workflows that can help you code better, faster:

1. 🤖Intelligent issue triage: Automate the overhead of managing new issues. Gemini CLI can analyze, label and prioritize incoming issues, helping focus your attention on what matters most.
2. 🚀Accelerated pull request reviews: Get instant, insightful feedback on code changes. Gemini CLI can review pull requests for quality, style and correctness, freeing up reviewers to focus on more complex tasks and decisions.
3. 🤝On-demand collaboration: Simply mention @gemini-cli in any issue or pull request to delegate tasks. Tell it to do things like, "write tests for this bug," "implement the changes suggested above," "brainstorm alternative solutions," or "fix this well defined bug."

Easily create new feature requests on GitHub for Gemini CLI to handle on your behalf

Gemini CLI GitHub Actions can handle your pull requests, providing code changes and AI-generated suggestions for improving the user experience

Delegate work with an "@gemini-cli" tag and the agent can complete a range of tasks, from writing bugs to fixing bugs

Think of these initial workflows as your launchpad. They are open-source and fully customizable — you can create your own workflows, or configure the ones that come built into Gemini CLI GitHub Actions.

## Built with enterprise-grade security and control

Robust security measures are a fundamental part of modern software development. That’s why we built Gemini CLI GitHub Actions with security and flexibility at its core.

You are always in control with capabilities including:

* Secure, credential-less authentication:Vertex AI and Gemini Code Assist Standard and Enterprise users can tap into Google Cloud'sWorkload Identity Federation(WIF) to eliminate the need for long-lived API keys in your environment, drastically reducing the risk of credential compromise.
* Granular control: Enforce the principle of least privilege with multi-layered controls. Use capabilities like command allowlisting to explicitly approve every shell command the agent can execute. You can also create a custom identity for the agent (e.g., gemini-for-your-org) and grant it only the precise permissions it needs.
* Complete transparency:GitHub on CLI comes integrated withOpenTelemetry, an industry standard for telemetry, so you can stream logs and metrics to your preferred observability platform, like Google Cloud Monitoring. This gives you full, real-time visibility into every action to monitor usage and debug complex workflows.

## Get started today

What will you build with your new coding teammate? A workflow that automatically generates release notes? One that keeps documentation in sync with your code? Don’t just imagine it; build it. We invite you to contribute your innovative workflows to our repository and share them with the community.

Gemini CLI GitHub Actions isavailable todayin beta, withgenerous free-of-charge quotasfor Google AI Studio. Vertex AI, along with the Standard and Enterprise tiers of Gemini Code Assist, are also supported. We will have free-of-charge use for Gemini Code Assist for individual users available soon.

To get started,downloadGemini CLI 0.1.18 or later and run `/setup-github`. You can find the GitHub Action atgoogle-github-actions/run-gemini-cli.

POSTED IN:

### Related stories

Chromebooks

#### See our new ChromeOS wallpapers starring Jupiter’s UV auroras

 By




 Joel Meares


 Aug 07, 2025


Google DeepMind

#### The AI model Perch, updated today, uses audio to help protect endangered species.

 By




 TK Breuer


 Aug 07, 2025


AI

#### The latest AI news we announced in July

 By




 Keyword Team


Gemini App

#### New Gemini app tools to help students learn, understand and study even better

 By




 Jennifer Shen


 Aug 06, 2025


Learning & Education

#### Guided Learning in Gemini: From answers to understanding

 By




 Maureen Heymans


 Aug 06, 2025


Google Labs

#### Jules, our asynchronous coding agent, is now available for everyone.

 Aug 06, 2025


.

 Jump to position 1

 Jump to position 2

 Jump to position 3

 Jump to position 4

 Jump to position 5

 Jump to position 6
