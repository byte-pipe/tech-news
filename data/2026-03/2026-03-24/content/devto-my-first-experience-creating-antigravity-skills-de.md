---
title: My First Experience Creating Antigravity Skills - DEV Community
url: https://dev.to/googleai/my-first-experience-creating-antigravity-skills-524b
site_name: devto
content_file: devto-my-first-experience-creating-antigravity-skills-de
fetched_at: '2026-03-24T19:28:01.466119'
original_url: https://dev.to/googleai/my-first-experience-creating-antigravity-skills-524b
author: Shir Meir Lador
date: '2026-03-20'
description: Experimenting with Agent skills for the first time, feeling empowered! Last week, I was at an... Tagged with antigravity, ai, googlecloud, agents.
tags: '#antigravity, #ai, #googlecloud, #agents'
---

Experimenting with Agent skills for the first time, feeling empowered!

Last week, I was at an event where we taught developers how to buildMCP servers,agents, anddeploy open modelstoGoogle Cloud Run. After the session, one of the developers shared something that really stuck with me: he was already using our content to create specializedSkillsto share with his entire team.

I got inspired and decided it was time to dive intoAgent Skills. During my last project, the dev-signal agent, I had a lot of learnings about how to bring agents and AI applications to production in a robust and scalable manner. I thought,this is a great opportunity to give my favorite coding agent, Google’sAntigravity(Google’s “agent-first” IDE), those skills so that going forward, it will just do it for me!

In this post, I’ll walk through how I built the 13 production skills in thisrepositoryand the patterns behind them.

## What are Agent Skills?

AsRomin Iraniexplains in“Getting Started with Google Antigravity Skills”, skills represent a shift from monolithic context loading toProgressive Disclosure.

Agents get “overwhelmed” when providing them too many tools all at once (a phenomenon known as “Tool Bloat”), to solve for that, Skills allow the agent to “load” specialist knowledge only when needed. When you ask an agent to “evaluate a shadow revision,” it will figure out it will need to leverage theShadow Deployerskill as context for this operation.

## Workspace vs. Global Scope

In Antigravity, you can manage these skills in two distinct ways depending on how you want to use them:

* Workspace Scope:Located in.agent/skills/within your project root. These are specific to your project and can be committed to GitHub so your entire team can benefit from the same production patterns.
* Global Scope:Located in~/.gemini/antigravity/skills/.These are your personal utilities that stay with you across every project you work on.

## How I built the skills

Following the principles inDaniela Petruzalek’s“Building Agent Skills with skill-creator”,I took a “methodology-first” approach. I used the existing dev-signal blog series I’ve been working on and thecodebaseitself as core context, asking Antigravity to identify and codify the unique skills needed tobuild a production agent on Google Cloud.

For some of the more specialized areas, I provided additional context with patterns I’d like to follow, such as the agent evaluationcodelabandblogand the agent securitycodelab, both written by my awesome team.

These 13 skills provide Antigravity (or any developer using them) the crucial toolkit of a Google Cloud Production Engineer. I’m currently finalizing a detailed, step-by-step walkthrough of the dev-signal agent which will be published on theGoogle Cloud Blogvery soon! (follow me for future updates)

In the meantime, you don’t have to wait — the fullrepositoryand theskillsare available for you to explore and leverage in your own projects today.

Here is the full inventory of the skills:

## 🏗️ Production Agent

* adk-memory-bank-initializer:Long-term state logic with Vertex AI Memory Bank.
* agent-containerizer:Mixed-runtime Dockerfiles (Python + Node.js).
* cloud-run-agent-architect:Least-privilege Terraform for Cloud Run.
* gcp-production-secret-handler:In-memory secret fetching pattern (Secret Manager).
* mcp-connector-generator:Standardized MCP connection logic.

## 📊 Evaluation

* gcp-agent-eval-engine-runner:Parallel inference and reasoning trace capture.
* gcp-agent-eval-metric-configurator:Setup for Grounding and Tool Use rubrics.
* gcp-agent-golden-dataset-builder:Tools for building datasets with reference trajectories.
* gcp-agent-shadow-deployer:“Dark Canary” deployment scripts with revision tagging.
* gcp-agent-tool-trajectory-evaluator:Custom Python metrics for Precision and Recall.

## 🛡️ Security

* gcp-agent-model-armor-shield:Intelligent firewall (Prompt Injection, RAI, Malicious URL filters).
* gcp-agent-safety-gatekeeper:Python integration pattern (safety_util.py) for sanitizing user inputs.
* gcp-agent-sdp-template-factory:Terraform for Sensitive Data Protection (PII/Secret redaction).

By codifying these patterns to production skills, Antigravity can now leverage these automatically in my day to day development. I hope you find these as helpful as I do!

## Pro tip - self improving skills!

Because these skills were AI-generated, they might not work perfectly for your specific environment on the first try. But that’s actually the best part of working with an agentic IDE. If a skill doesn’t work well for you, don’t just manually fix the code, let the coding agent figure it out. Once it finds the solution, you can ask it to update the corresponding SKILL.md with the learned workflow. This will capture the corrected workflow for the future, ensuring the agent doesn’t repeat the mistake while saving you tokens and time on the next run. Think of these as living documents that actively improve as you build.

Ready to get started?Clone therepositoryand add these skills to your Workspace or Global Scope to start building your own production-ready agents. Learn more aboutAgent skills.

Follow me onLinkedInandXfor updates on my next blogs and videos.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
