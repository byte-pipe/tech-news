---
title: GitHub - luongnv89/claude-howto: A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates tha...
url: https://github.com/luongnv89/claude-howto
date:
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-03-30T01:02:15.115398
---

# GitHub - luongnv89/claude-howto: A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates tha...

# Claude Howto Guide Summary

## The Problem
- Official Claude Code docs list features but lack guidance on combining them into real workflows.
- No clear learning path; users are unsure whether to learn MCP before hooks, or skills before subagents.
- Existing examples are overly simple and do not demonstrate production‑grade pipelines (e.g., code review with memory, delegation, security scans).

## How Claude Howto Fixes This
- Provides a **structured, visual, example‑driven guide** that teaches every Claude Code feature with copy‑paste templates.
- Combines reference documentation, visual Mermaid diagrams, and production‑ready snippets.
- Organizes content by feature and follows a progressive learning path from beginner to advanced.
- Includes self‑assessment quizzes that generate a personalized roadmap.

### What You Get
- 10 tutorial modules covering slash commands, memory, checkpoints, CLI basics, skills, hooks, MCP, subagents, advanced features, and plugins.
- Ready‑to‑use configurations: slash command files, CLAUDE.md templates, hook scripts, MCP configs, subagent definitions, and full plugin bundles.
- Mermaid diagrams that explain internal workings of each feature.
- Guided learning path estimated at 11–13 hours to reach power‑user level.
- Built‑in self‑assessment quizzes runnable directly in Claude Code.

## How It Works
1. **Find Your Level** – Run the self‑assessment quiz or the `/self-assessment` command to receive a personalized roadmap.
2. **Follow the Guided Path** – Complete the 10 modules in order; each builds on the previous one.
3. **Combine Features** – Learn to wire slash commands, memory, subagents, and hooks into automated pipelines (code reviews, deployments, documentation generation, etc.).
4. **Test Understanding** – Execute `/lesson-quiz [topic]` after each module to identify and fill knowledge gaps.

## Community Adoption
- Over 3,900 GitHub stars from developers using Claude Code daily.
- More than 460 forks, many of which adapt the guide for team workflows.
- Actively maintained; synced with every Claude Code release (latest v2.2.0, March 2026).

## Learning Path Overview
| Module | Feature | Level | Estimated Time |
|--------|---------|-------|-----------------|
| 1 | Slash Commands | Beginner | 30 min |
| 2 | Memory | Beginner+ | 45 min |
| 3 | Checkpoints | Intermediate | 45 min |
| 4 | CLI Basics | Beginner+ | 30 min |
| 5 | Skills | Intermediate | 1 h |
| 6 | Hooks | Intermediate | 1 h |
| 7 | MCP | Intermediate+ | 1 h |
| 8 | Subagents | Intermediate+ | 1.5 h |
| 9 | Advanced Features | Advanced | 2–3 h |
| 10 | Plugins | Advanced | 2 h |

## Getting Started in 15 Minutes
1. Clone the repository:
   `git clone https://github.com/luongnv89/claude-howto.git && cd claude-howto`
2. Copy the first slash command into your project:
   `mkdir -p /path/to/your-project/.claude/commands && cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/`
3. In Claude Code, type `/optimize` to test.
4. Set up project memory:
   `cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md`
5. Install a skill (e.g., code review):
   `cp -r 03-skills/code-review ~/.claude/skills/`

*Optional 1‑hour essential setup:* repeat the copy steps for slash commands, memory, and a skill, then follow the guided path to add hooks, subagents, MCP, and plugins.

## Example Use Cases
- **Automated Code Review:** Slash Commands + Subagents + Memory + MCP
- **Team Onboarding:** Memory + Slash Commands + Plugins
- **CI/CD Automation:** CLI Reference + Hooks + Background Tasks
- **Documentation Generation:** Skills + Subagents + Plugins
- **Security Audits:** Subagents + Skills + Hooks (read‑only mode)
- **DevOps Pipelines:** Plugins + MCP + Hooks + Background Tasks
- **Complex Refactoring:** Checkpoints + Planning Mode + Hooks

## Frequently Asked Questions
- **Is this free?** Yes. MIT‑licensed and free forever for personal or commercial use.
- **Is it maintained?** Actively; the guide is updated with every Claude Code release (current version v2.2.0, March 2026).
- **How does it differ from official docs?** Official docs are a feature reference. This guide adds tutorials, diagrams, production‑ready templates, and a progressive learning path that complement the reference material.
