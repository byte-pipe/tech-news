---
title: 'GitHub - SafeAI-Lab-X/ClawKeeper: ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers (aka The Norton for OpenClaw) · GitHub'
url: https://github.com/SafeAI-Lab-X/ClawKeeper
site_name: tldr
content_file: tldr-github-safeai-lab-xclawkeeper-clawkeeper-comprehen
fetched_at: '2026-04-04T11:11:44.117470'
original_url: https://github.com/SafeAI-Lab-X/ClawKeeper
date: '2026-04-04'
description: 'ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers (aka The Norton for OpenClaw) - SafeAI-Lab-X/ClawKeeper'
tags:
- tldr
---

SafeAI-Lab-X

 

/

ClawKeeper

Public

* NotificationsYou must be signed in to change notification settings
* Fork32
* Star336

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

15 Commits
15 Commits
clawkeeper-plugin
clawkeeper-plugin
 
 
clawkeeper-skill
clawkeeper-skill
 
 
clawkeeper-watcher
clawkeeper-watcher
 
 
fig
fig
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# 🦞🛡️ ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers

# (aka The Norton for OpenClaw)

SAFETY EXFOLIATE! SAFETY EXFOLIATE!

ClawKeeperis acomprehensive real-time security frameworkdesigned for autonomous agent systems such asOpenClaw. It provides unified protection through three complementary approaches:skill-basedsafeguards at the instruction level,plugin-basedenforcement at the runtime level, and awatcher-basedindependent monitoring agent for external oversight.

# 🔎 Overview

ClawKeeperprovides protection mechanisms across three complementary architectural layers:

* Skill-based Protectionoperates at the instruction level, injecting structured security policies directly into the agent context to enforce environment-specific constraints and cross-platform boundaries.
* Plugin-based Protectionserves as an internal runtime enforcer, providing configuration hardening, proactive threat detection, and continuous behavioral monitoring throughout the execution pipeline.
* Watcher-based Protectionintroduces a novel, decoupled system-level security middleware that continuously verifies agent state evolution. It enables real-time execution intervention without coupling to the agent's internal logic, supporting operations such as halting high-risk actions or enforcing human confirmation.

Importantly,Watcher-based Protectionissystem-agnosticand can be integrated with different agent platforms to provide regulatory separation between task execution and safety enforcement, enablingproactiveandadaptivesecurity across the entire agent lifecycle. It can be deployed bothlocallyand in thecloud, supporting personal deployments as well as enterprise or intranet environments.

# 📦 Installation

ClawKeeper supports three complementary protection mechanisms.

## 📚 I.Skill-based Protection

Inject security policies directly into the agent context through structured Markdown documents and scripts.

Quick Start:

### Windows Safety Guide

cd clawkeeper
-
skill
/
skills
/
windows
-
safety
-
guide
.
/
scripts
/
install.ps1

Then instruct OpenClaw:

Please use the windows-safety-guide skill to enforce behavior security policies, configuration protection, and enable nightly security audits.

### Feishu (Lark) Safety Guide

cd
 clawkeeper-skill/skills/feishu-safety-guide
bash scripts/install.sh

Then instruct OpenClaw:

Please use the feishu-safety-guide skill to enforce message protection, credential security, and enable periodic security reporting in Feishu (Lark).

Fordetailedsetup options and deployment from prompt, seeSkill-based Protection.

## 📚 II.Plugin-based Protection

A runtime enforcer plugin providing configuration auditing, threat detection, and behavioral monitoring.

Quick Start:

### Linux/macOS

cd
 clawkeeper-plugin
bash install.sh

### Windows

cd clawkeeper
-
plugin
.
/
install.ps1

Then verify installation:

npx openclaw clawkeeper audit

Fordetailedcommand reference and advanced usage, seePlugin-based Protection.

## 📚 III.Watcher-based Protection

An independent, decoupled governance layer providing runtime monitoring and execution control without coupling to the agent's internal logic.

Quick Start:

### Prerequisites

* Node.js and npm/pnpm installed
* Git repository cloned

### Installation Steps

1. Install repository dependencies:pnpm install
2. Build and link the launcher:cdclawkeeper
npm install
npm run build
npm linkcd..
3. Initialize operating modes:clawkeeper init remote
clawkeeper initlocal
4. Launch the watcher:#Remote governance modeclawkeeper remote gateway run#Local governance modeclawkeeperlocalgateway run

Fordetailedconfiguration, command reference, and feature documentation, seeWatcher-based Protection.

# 💡 Features

* Comprehensive Security Scanning:Regularly scans the runtime environment, dependencies, and workspace for vulnerabilities, providing clear and actionable risk alerts before threats occur.
* Real-time Threat Prevention & Gating:Evaluates AI actions in real time, blocking high-risk behaviors such as prompt injection, credential leakage, and code injection.
* Behavioral Profiling & Anomaly Detection:Builds long-term behavioral baselines for AI agents and detects anomalies when unusual actions, risky tool calls, or dangerous commands appear.
* Intent Enforcement & Trajectory Analysis:Monitors multi-turn interactions to ensure AI actions stay aligned with the user’s original intent and prevents goal drift, unsafe loops, or unauthorized actions.
* Config Integrity & Drift Monitoring:Protects critical configuration files and alerts users when unexpected changes weaken security settings or introduce new risks.
* Automated Hardening & Remediation:Provides vulnerability remediation suggestions, applies secure default configurations, and supports one-click rollback with automatic backups.
* Third-Party Extension Shield:Reviews and monitors external extensions and plugins to prevent malicious behavior or excessive permission access.
* Comprehensive Logging & Auditing:Maintains full logs of user inputs, AI outputs, tool usage, and security decisions for auditing, compliance, and traceability.
* Self-Evolving Threat Intelligence:Stores high-risk events and decisions to build a threat intelligence library that helps detect and prevent recurring or new attack patterns.
* Cross-Platform Ecosystem Security:Ensures consistent security protection across operating systems and third-party platforms, providing full ecosystem coverage.

# 🔬 Comparative Analysis of Safety Paradigms in ClawKeeper

ClawKeeper offers a comprehensive suite of security mechanisms, allowing users to freely select and combine them according to their specific requirements, whether prioritizing runtime efficiency or security performance.

# 📈 Experiment Results

To systematically assess the security capabilities of ClawKeeper, we construct a benchmark comprising seven categories of safety tasks, each containing 20 adversarial instances divided equally into 10 simple and 10 complex examples. We compare ClawKeeper against the most prominent open-source security repositories for OpenClaw-style agent ecosystems.
The results showed that ClawKeeper achieved optimal defense performance.

# 🔥 Updates

* [2026-03-25] 🎉 ClawKeeper v1.0 has been released.
* [2026-03-26] 🧠 We released ourpaper

# 📝 License

This project is licensed underMIT.

## About

ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers (aka The Norton for OpenClaw)

### Topics

 security

 skills

 plugins

 safety

 agents

 openclaw

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

336

 stars
 

### Watchers

14

 watching
 

### Forks

32

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* SafeAI-Lab-X

## Languages

* TypeScript87.9%
* Swift7.0%
* JavaScript1.6%
* Kotlin1.6%
* Shell1.0%
* CSS0.5%
* Other0.4%