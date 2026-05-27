---
title: Beyond the Prompt: Claude Code | Arpan Patel
url: https://arps18.github.io/posts/claude-code-mastery/
date: 2026-05-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-28T06:05:10.768546
---

# Beyond the Prompt: Claude Code | Arpan Patel

# Summary of “Beyond the Prompt: Claude Code” by Arpan Patel  

## 1. Claude Code – From Prompt to Autonomous Agent  
- Treat Claude Code as a programmable agent with memory, custom commands, and parallel sessions rather than a simple chatbot.  
- Core principle (Boris Cherny, Anthropic): give Claude a way to verify its own work; this self‑verification yields a 2‑3× quality boost.  
- Recommended workflow: **Explore → Plan → Code**.  
  - Activate plan mode (Shift+Tab twice) for read‑only exploration and design a plan before execution.  
  - Use a second Claude instance to review the plan as an unbiased staff engineer.  
- Use precise file references (`@src/auth/login.py`) or pipe exact context (`cat error.log | claude`) instead of vague descriptions.  
- Delegate tasks: provide a concise brief up front and let Claude work autonomously, rather than micromanaging line by line.  
- Press **Ctrl+G** to edit the generated plan before Claude proceeds.  
- When Claude errs, end the prompt with “Update CLAUDE.md so you do not repeat this.” Claude can generate self‑correcting rules that compound over time.  

## 2. The .claude Directory – Layered Configuration  
- Two configuration scopes:  
  - **Project scope** (`.claude/` inside the repo, committed to Git).  
  - **Global scope** (`~/.claude/`, applies to all projects).  
- Mental model: project files describe the codebase; global files describe the user.  
- Key files:  
  - `CLAUDE.md` – loaded every session, can be project‑ or global‑level, committed.  
  - `CLAUDE.local.md` – personal notes, git‑ignored.  
  - `settings.json` / `settings.local.json` – permissions, hooks, env vars, model defaults.  
  - `.mcp.json` – team‑shared MCP server definitions.  
  - `skills/<name>/SKILL.md` – reusable prompts invoked with `/name`.  
  - `commands/*.md` – single‑file slash commands.  
  - `agents/*.md` – sub‑agent definitions.  
  - `rules/*.md` – topic‑scoped instructions, optionally path‑gated.  
- Cascading behavior: in monorepos, both root‑level and subfolder `CLAUDE.md` files load when working in a subdirectory.  
- Path‑gated rules (`rules/*.md`) keep guidance scoped to specific folders (e.g., migrations).  
- Prefer **skills** over simple commands because they support extra files, tool allowances, and agent overrides.  
- Use `claude project purge <path> --dry-run` to inspect local state before transferring a machine.  

## 3. CLAUDE.md – The Central Rulebook  
- Loaded at the start of every session; errors here are repeated by Claude.  
- Keep the file **short**: each line should be essential; remove anything that does not prevent a mistake.  
- Encourage Claude to write its own rules: after a failure, ask it to “Update CLAUDE.md so you do not repeat this.” Over weeks this becomes a curated list of project‑specific gotchas.  
- Example from the Claude Code team (Boris Cherny): a concise 15‑line file that defines the development workflow using `bun` (not `npm`), type‑checking, testing, linting, and a pre‑PR ritual. No style preferences, no codebase tours—only actionable commands.  
- PR‑time rule injection: comment “@claude add to CLAUDE.md …” to automatically append a new rule, a practice called **Compounding Engineering**.  

## 4. Skills – Structured, Reusable Prompts  
- Skills are modular prompt definitions that can include supporting files, tool permissions, and agent overrides.  
- Typical skill structure: `skills/api-conventions/SKILL.md` describing Go API conventions, invoked with `/api-conventions`.  
- Benefits over plain commands: richer context, ability to disable model invocation, and clearer separation of concerns.  
- Popular skill libraries are shared within teams; installing them accelerates onboarding.  

## 5. Subagents – Custom Agents for Repeated Tasks  
- Defined in `agents/*.md`; each file describes a self‑contained agent (e.g., `/pr-review`).  
- Workflow example: a `/pr-review` agent reads a PR diff, runs tests, and produces a review summary.  
- Teams can copy (“steal”) well‑crafted subagents and adapt them to their own codebases.  

## 6. Plugins & Marketplace  
- Claude Code supports plugins that extend functionality (e.g., integration with Obsidian, external APIs).  
- A marketplace allows sharing and discovering community‑built plugins and skills.  

## 7. Underused Commands – Power‑User Shortcuts  
- `/goal` implements the “Ralph Loop” built into Claude: set a high‑level objective, let Claude iteratively plan and execute until the goal is met.  
- Other hidden commands enable batch operations, session management, and state inspection.  

## 8. MCPs as Power Tools – Multi‑Context Projects  
- MCP (Multi‑Context Project) files (`.mcp.json`) define shared server resources and context across projects.  
- Example workflow: an Obsidian‑based knowledge base linked to code via MCP, enabling seamless navigation between notes and source files.  

## 9. Optimizing Daily Workflow  
- Combine plan mode, self‑verification, and rule updates to create a feedback loop that continuously improves output quality.  
- Treat each PR review as an opportunity to enrich `CLAUDE.md`.  
- Regularly purge stale project state and keep the `.claude` directory tidy.  

## 10. Resources & Closing Notes  
- The guide assumes familiarity with basic Claude Code usage; it focuses on advanced patterns for power users.  
- Key resources: the official Claude Code repository, community skill libraries, plugin marketplace, and the Anthropic documentation.  
- Continuous iteration on `CLAUDE.md` and skill development yields exponential productivity gains.