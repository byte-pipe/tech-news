---
title: Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution
url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
site_name: tldr
content_file: tldr-google-fixes-cvss-10-gemini-cli-ci-rce-and-cursor
fetched_at: '2026-05-04T12:21:23.237279'
original_url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
author: The Hacker News
date: '2026-05-04'
description: Gemini CLI CVSS 10.0 flaw in versions below 0.39.1 enabled RCE in CI workflows, forcing Google to mandate explicit workspace trust.
tags:
- tldr
---

# Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution


Ravie Lakshmanan

Apr 30, 2026
AI Security / Vulnerability

Google has addressed a maximum severity security flaw in Gemini CLI -- the "@google/gemini-cli" npm package and the "google-github-actions/run-gemini-cli" GitHub Actions workflow -- that could have allowed attackers to execute arbitrary commands on host systems.

"The vulnerability allowed an unprivileged external attacker to force their own malicious content to load as Gemini configuration," Novee Securitysaidin a Wednesday report. "This triggered command execution directly on the host system, bypassing security before the agent’s sandbox even initialized."

The shortcoming, which does not have a CVE identifier, carries a CVSS score of 10.0. It affects the following versions -

* @google/gemini-cli < 0.39.1
* @google/gemini-cli < 0.40.0-preview.3
* google-github-actions/run-gemini-cli < 0.1.22

In its advisorypublishedlast week, Google said the impact is limited to workflows using Gemini CLI in headless mode, adding that any use of the tool in headless mode without folder trust will require manual review to configure this trust mechanism.

"In previous versions, Gemini CLI running in CI environments (headless mode) automatically trusted workspace folders for the purpose of loading configuration and environment variables," it said.

"This is potentially risky in situations where Gemini CLI runs on untrusted folders in headless mode (e.g., CI workflows that review user-submitted pull requests). If used with untrusted directory contents, this could lead to remote code execution via malicious environment variables in the local .gemini/ directory."

This automatic trust of the current workspace folder meant that the tool could load any agent configuration it found without review, sandboxing, or explicit user consent. An attacker could weaponize this behavior by planting a specially crafted configuration that could pave the way for code execution on the host running the agent, effectively turning CI/CD pipelines into supply-chain attack paths.

The update addresses the problem by requiring folders to be explicitly trusted before configuration files can be accessed. To that end, users are being urged to review their workflows and adopt one of two approaches -

* If the workflow runs on trusted inputs (e.g., reviewing pull requests from trusted collaborators), set GEMINI_TRUST_WORKSPACE: 'true' in the workflow.
* If the workflow runs on untrusted inputs, review Google's guidance ingoogle-github-actions/run-gemini-clito harden the workflow against malicious content, and set the environment variable.

The tech giant also noted that it's taking steps to harden tool allowlisting when Gemini CLI is configured to run in --yolo mode to prevent scenarios where untrusted inputs (e.g., user-submitted GitHub issues) could lead to remote code execution via prompt injection by taking advantage of the fact that the auto-approve mode would ignore any allowlist in "~/.gemini/settings.json" and run all tool calls automatically (including "run_shell_command") without requiring user confirmation.

"In version 0.39.1, the Gemini CLI policy engine now evaluates tool allowlisting under --yolo mode, which is useful for CI workflows that allowlist a few safe commands to run when processing untrusted inputs," Google said. "As a result, some workflows that previously depended on this behavior may fail silently unless tool allowlists are modified to fit the task."

### Cursor Bug Leads to Code Execution

The disclosure comes as Novee Security also highlighted a high-severity vulnerability in the AI-powered development tool Cursor prior to version 2.5 (CVE-2026-26268, CVSS score: 8.1) that could also lead to arbitrary code execution by means of a prompt injection.

Cursor, in an alertreleasedin February 2026, described it as a case of sandbox escape through .git configurations, allowing a rogue agent to set up a bare repository (".git") with a maliciousGit hookthat's automatically fired every time a commit operation runs within the embedded repository context without requiring any user interaction.

The end result is auto-approved arbitrary code execution on the victim's machine through the following sequence of actions -

* User clones a public GitHub repository with the embedded bare repository containing a malicious post-checkout hook
* User opens the repository in CursorIDE
* Users ask an innocuous prompt to "explain the codebase"
* Cursor agent parses theAGENTS.mdthat instructs it to navigate to the bare repository and performs a "git checkout" of the master branch
* The post-checkout hook inside the bare repository is triggered, leading to code execution.

"The root cause is not a flaw in Cursor's core product logic, but rather a consequence of a feature interaction in Git, one that becomes exploitable the moment an AI agent starts autonomously executing Git operations inside a repository it doesn't control," security researcher Assaf Levkovichsaid.

"When the agent runs git checkout as part of fulfilling a routine request, it is not doing anything the user didn't implicitly authorize. But neither the user nor the agent has visibility into what the repository's Cursor Rules have set in motion. A malicious pre-commit hook embedded in a nested bare repository executes silently, outside the agent's reasoning chain and outside the user’s field of view."

The findings also coincide with the discovery of another high-severity access control vulnerability in the IDE (CVSS score: 8.2) that could allow any installed extension to access sensitive API keys and credentials stored locally in an SQLite database, enabling account takeover, data exposure, and financial loss stemming from unauthorized API usage. The issue, codenamedCursorJackingby LayerX, remains unpatched.

"Cursor does not enforce access control boundaries between extensions and this database," LayerX researcher Roy Paz said. "Exploitation of this vulnerability can lead to exposure of session tokens and API keys, unauthorized access to Cursor backend services, and data theft via user impersonation."

Cursor has maintained that the access is limited to the local machine where the user has already installed and granted permissions to the extension, meaning any rogue extension with local file system access could potentially extract valuable information from various application data stores. To counter the threat, it's essential that users stick to downloading trusted extensions.

Found this article interesting? Follow us on 
Google News
, 
Twitter
 and 
LinkedIn
 to read more exclusive content we post.

SHARE










Tweet


Share


Share


Share

SHARE 


Continuous Integration
, 
cybersecurity
, 
GitHub
, 
Prompt Injection
, 
remote code execution
, 
Supply Chain Security
, 
Vulnerability

⚡ Top Stories This Week

Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph API

Malicious KICS Docker Images and VS Code Extensions Hit Checkmarx Supply Chain

Apple Fixes iOS Flaw That Let FBI Recover Deleted Signal Messages

Vercel Finds More Compromised Accounts in Context.ai-Linked Breach

ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM Farms +25 New Stories

Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign

LMDeploy CVE-2026-33626 Flaw Exploited Within 13 Hours of Disclosure

FIRESTARTER Backdoor Hit Federal Cisco Firepower Device, Survives Security Patches

Researchers Uncover Pre-Stuxnet ‘fast16’ Malware Targeting Engineering Software

⚡ Weekly Recap: Fast16 Malware, XChat Launch, Federal Backdoor, AI Employee Tracking and More

Checkmarx Confirms GitHub Repository Data Posted on Dark Web After March 23 Attack

Microsoft Confirms Active Exploitation of Windows Shell CVE-2026-32202

Chinese Silk Typhoon Hacker Extradited to U.S. Over COVID Research Cyberattacks

Microsoft Patches Entra ID Role Flaw That Enabled Service Principal Takeover

Researchers Discover Critical GitHub CVE-2026-3854 RCE Flaw Exploitable via Single Git Push

Critical cPanel Authentication Vulnerability Identified — Update Your Server Immediately

⭐ Featured Resources

[Webinar] Stop Chasing Alerts and Start Focusing on Real Exposures

[Guide] How to Enable Secure Data Movement Without Added Risk

Learn How Hidden Identity Blind Spots Weaken Your Security Systems

[Guide] Learn a Practical Framework to Evaluate AI Tools for Production