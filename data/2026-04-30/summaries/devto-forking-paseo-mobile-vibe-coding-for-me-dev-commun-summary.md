---
title: Forking Paseo: Mobile vibe coding for me - DEV Community
url: https://dev.to/thisisryanswift/forking-paseo-mobile-vibe-coding-for-me-48pa
date: 2026-04-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-04-30T12:32:50.214599
---

# Forking Paseo: Mobile vibe coding for me - DEV Community

# Summary of “Forking Paseo: Mobile vibe coding for me”

## Motivation and Goals
- Wanted to improve my phone‑based coding workflow using AI agents.
- Needed a way to check on agents, answer prompts, nudge tasks, and start work without a laptop.
- Required:
  - Linux and Android support
  - Local (non‑SaaS) execution
  - Compatibility with existing agents, especially OpenCode
  - Ability to continue or inspect sessions from the main development environment

## Why Paseo Appeared Suitable
- Paseo is a local‑first app that lets a mobile client control a daemon on the host machine.
- It avoids moving code to a cloud workspace and provides a remote control layer.
- Open source nature allowed me to consider modifying it to fit my needs.

## Gaps Identified in the Original Paseo
- **Session handoff**: could not resume an OpenCode session started in the terminal without losing history.
- **Slash‑command autocomplete**: ranking and visual ordering differed from terminal OpenCode expectations.
- **Workspace defaults**: Paseo sometimes overrode OpenCode’s project‑specific model or mode settings.
- **Subagent visibility**: subagents appeared as generic “tool calls,” making it unclear whether they were stuck.
- Lack of Gemini CLI support (future interest).

## Forking and Using AI Agents
- Forked Paseo and guided AI coding agents with natural‑language prompts such as:
  - “Resume an OpenCode session that started outside Paseo.”
  - “Make `/q` behave like terminal OpenCode.”
  - “Show subagent status instead of opaque calls.”
- Agents explored the codebase, made changes, wrote tests, and iterated based on my feedback.
- My role shifted from hand‑coding features to describing desired workflows and reviewing outcomes.

## Core Improvements Implemented
- **Zero‑friction handoffs**: app now discovers active OpenCode sessions, shows recent history, and resumes seamlessly.
- **Muscular defaults**: UX respects OpenCode workspace settings; slash commands like `/q`, `/exit` are prioritized.
- **Subagent transparency**: subagents now display their identity and current task status in the timeline, eliminating mysterious hangs.

## Future Directions
- Possible continued divergence of my fork to suit personal workflows.
- Planned Gemini CLI integration.
- Interest in aggregating usage tracking across providers to make Paseo a central control plane for agents and projects.

## Takeaways
- Open source combined with AI agents dramatically reduces the effort needed to adapt a tool to personal needs.
- The approach creates a new “on‑ramp” for shaping software without following traditional engineering processes strictly.
- Mobile‑first control of local development environments is now feasible, though it may still be a niche practice.