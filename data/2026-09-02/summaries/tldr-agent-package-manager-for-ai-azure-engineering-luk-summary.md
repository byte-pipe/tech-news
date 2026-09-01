---
title: Agent Package Manager for AI Azure Engineering | luke.geek.nz
url: https://luke.geek.nz/azure/agent-package-manager/
date: 2026-09-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-02T09:08:21.727029
---

# Agent Package Manager for AI Azure Engineering | luke.geek.nz

# Agent Package Manager for AI Azure Engineering

## Problem Statement
- AI coding tools are improving rapidly, but their setup often consists of scattered local files, copied prompts, one‑off MCP servers, and tribal knowledge.  
- Platform teams need to enforce approved Azure patterns, Microsoft Learn grounding, cost guidance, security checks, and repeatable onboarding.  
- Audits ask a simple yet uncomfortable question: *What agent context was installed, where did it come from, and who allowed it?*

## What is APM?
- APM is a dependency manager for AI agents.  
- The core model declares skills, prompts, instructions, plugins, and MCP servers in a `oneapm.yml` manifest.  
- Running `apm install` deploys the declared primitives to each agent harness.  
- A lockfile records exact versions and content hashes for reproducibility.  
- `apm-policy.yml` provides install‑time governance for dependencies, MCP servers, and targets.

## Why It Matters for Azure Teams
- Azure engineering rarely uses a single tool; a realistic repo may involve:
  - GitHub Copilot for daily implementation  
  - Claude Code for deep repository work  
  - Cursor or OpenCode for local workflows  
  - Microsoft Learn MCP for current Azure documentation  
  - Azure MCP for cloud resource inspection and operations  
  - Foundry MCP for Microsoft Foundry work  
  - Context7 for SDK and framework documentation  
  - Team‑specific skills for AKS, App Service, Functions, API Management, identity, monitoring, reliability, and cost  
- Example manifest declares active agent targets (`copilot`, `claude`, `cursor`, `opencode`) and reusable skill packages for various SDKs and platforms.  
- The workflow mirrors traditional dependency management: declare, lock, validate.

## MCP Servers as Dependencies
- MCP servers are listed in the same dependency manifest, making their usage explicit rather than hidden on a developer’s machine.  
- Sample entries include `microsoft.learn.mcp`, `context7`, `azure`, and an npm‑based Azure MCP server.  
- This moves MCP configuration from “whatever is on my machine” into the repository contract.

## Governance Without Ceremony
- The smallest useful policy is an allowlist defined in `apm-policy.yml`.  
- The policy lists permitted:
  - Package sources (e.g., `DietrichGebert/ponytail`, `dotnet/skills`)  
  - MCP servers (e.g., `azure`, `context7`, `microsoft.learn.mcp`)  
  - Transports (`http`, `sse`, `stdio`)  
  - Agent targets (`claude`, `copilot`, `cursor`, `opencode`)  
- Enforcement occurs at install time, preventing unauthorized files from being written. Runtime behavior remains governed by the agent harness and underlying platform.

## From One Repository to an Organization
- APM’s value grows when many repositories share a common agent engineering baseline.  
- Organizational layering:
  - **GitHub Organization** → organization‑wide policy  
  - **Team level** (platform, data, security) → shared skill packages  
  - **Repository level** → repo‑specific `apm.yml`  
- Teams receive a common starting point but can customize with domain‑specific context.  
- Responsibility split:
  - **Organization**: defines what is allowed and required.  
  - **Team**: decides which capabilities are needed.  
  - **Repository**: specifies workload‑specific requirements.  
  - **APM**: resolves, locks, installs, and audits the final set.

## GitHub Makes This Practical
- APM integrates with GitHub’s existing organization and repository model.  
- An organization can store an APM policy in its configuration; repositories automatically inherit it via the remote URL.  
- Policies can cover approved package sources, MCP servers, transports, agent targets, required packages, and manifest metadata.  
- Teams keep their own `apm.yml` without needing platform‑team edits for every change.  
- Enforcement can be tied to GitHub Rulesets and required status checks in CI:
  - Pull request → GitHub Actions (`apm audit --ci`) → dependency checks → Ruleset validation → merge.  
- Policy enforcement is install‑time/CI‑based; runtime security remains the responsibility of the agent harness.

## Impact
- The platform team provides a “paved road” of approved agent context, reducing per‑repository maintenance, ensuring auditability, and aligning AI agent usage with Azure engineering standards across the organization.