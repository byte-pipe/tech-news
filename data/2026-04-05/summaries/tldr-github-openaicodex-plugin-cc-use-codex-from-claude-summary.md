---
title: GitHub - openai/codex-plugin-cc: Use Codex from Claude Code to review code or delegate tasks. · GitHub
url: https://github.com/openai/codex-plugin-cc
date: 2026-04-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-05T01:02:59.634705
---

# GitHub - openai/codex-plugin-cc: Use Codex from Claude Code to review code or delegate tasks. · GitHub

# Codex plugin for Claude Code – Summary

## Overview
- Provides seamless access to OpenAI Codex from Claude Code for code reviews and task delegation.
- Enables read‑only reviews, steerable adversarial reviews, and background job management.

## Main Capabilities
- **/codex:review** – standard read‑only code review of current changes or a branch.
- **/codex:adversarial-review** – steerable review that challenges design decisions and risk areas.
- **/codex:rescue** – delegates tasks (bug investigation, fixes, etc.) to Codex, with options for model, effort, and background execution.
- **/codex:status**, **/codex:result**, **/codex:cancel** – monitor, retrieve, or cancel background jobs.
- **/codex:setup** – checks installation, handles authentication, and can enable a review gate that blocks Claude stops until Codex approves.

## Requirements
- ChatGPT subscription (including free tier) or an OpenAI API key (usage counts toward Codex limits).
- Node.js 18.18 or newer.

## Installation Steps
1. Add the marketplace:  
   `/plugin marketplace add openai/codex-plugin-cc`
2. Install the plugin:  
   `/plugin install codex@openai-codex`
3. Reload plugins:  
   `/reload-plugins`
4. Run setup:  
   `/codex:setup` (offers to install Codex via npm if missing)
5. If installing manually: `npm install -g @openai/codex` then `codex login`.

## Command Reference

### /codex:review
- Reviews uncommitted changes or a branch (`--base <ref>`).  
- Supports `--background` and `--wait`.  
- Read‑only; use `/codex:status` and `/codex:cancel` for background jobs.

### /codex:adversarial-review
- Steerable review that questions implementation, design, and risk assumptions.  
- Accepts extra focus text after flags.  
- Same options as `/codex:review`.

### /codex:rescue
- Delegates a task to Codex (bug investigation, fixing, redesign, etc.).  
- Options: `--background`, `--wait`, `--resume`, `--fresh`, `--model <model>`, `--effort <level>`.  
- Example: `/codex:rescue --model gpt-5.4-mini --effort medium investigate flaky test`.

### /codex:status
- Shows running and recent jobs for the repository.

### /codex:result
- Retrieves final output of a completed job, including session ID for direct Codex resume.

### /codex:cancel
- Cancels an active background job.

### /codex:setup
- Verifies Codex installation and authentication.  
- Enables/disables the optional review gate (`--enable-review-gate`, `--disable-review-gate`).

## Typical Workflows
- **Review before shipping:** `/codex:review`
- **Hand a problem to Codex:** `/codex:rescue investigate build failure in CI`
- **Long‑running tasks:**  
  `/codex:adversarial-review --background`  
  `/codex:rescue --background investigate flaky test`  
  Follow up with `/codex:status` and `/codex:result`.

## Configuration
- Default model and reasoning effort can be overridden in `~/.codex/config.toml` (user level) or `.codex/config.toml` at the project root (project level, loaded only for trusted projects).  
- Example project config to always use `gpt-5.4-mini` with high effort:
  ```
  model = "gpt-5.4-mini"
  model_reasoning_effort = "xhigh"
  ```

## Integration Details
- The plugin wraps the Codex app server, using the globally installed `codex` binary and its configuration.  
- Jobs created via the plugin can be resumed directly in Codex with `codex resume <session-id>`.

---  
This summary captures the plugin’s purpose, installation, core commands, usage patterns, and configuration options while adhering to the required markdown structure.