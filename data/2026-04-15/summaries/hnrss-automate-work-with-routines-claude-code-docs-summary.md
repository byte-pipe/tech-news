---
title: Automate work with routines - Claude Code Docs
url: https://code.claude.com/docs/en/routines
date: 2026-04-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:01:32.913485
---

# Automate work with routines - Claude Code Docs

# Automate work with routines – Claude Code Docs

## Overview
- Routines are saved Claude Code configurations (prompt, repositories, connectors) that run automatically on Anthropic‑managed cloud infrastructure.
- They can be triggered by schedules, API calls, or GitHub events, and multiple triggers can be combined.
- Available on Pro, Max, Team, and Enterprise plans with Claude Code on the web; manage them at `claude.ai/code/routines` or via the CLI (`/schedule`).

## Trigger types
- **Scheduled** – recurring cadence (hourly, nightly, weekly, custom cron).
- **API** – on‑demand HTTP POST to a per‑routine endpoint with a bearer token.
- **GitHub** – reacts to repository events such as pull requests, pushes, issues, or workflow runs.

## Example use cases
- **Backlog maintenance** – weekly schedule scans issue tracker, labels and assigns owners, posts Slack summary.
- **Alert triage** – monitoring tool calls API; routine creates draft PR with fix based on stack trace.
- **Bespoke code review** – GitHub trigger on `pull_request.opened`; routine adds checklist comments and summary.
- **Deploy verification** – CD pipeline calls API after deploy; routine runs smoke checks and posts go/no‑go decision.
- **Docs drift** – weekly schedule scans merged PRs, flags outdated docs, opens update PRs.
- **Library port** – GitHub trigger on `pull_request.closed` (merged); routine ports change to parallel SDK repository.

## Creating a routine

### From the web
1. Open `claude.ai/code/routines` and click **New routine**.
2. Provide a descriptive name and write a self‑contained prompt (includes model selector).
3. Add one or more GitHub repositories; enable “Allow unrestricted branch pushes” if needed.
4. Choose a cloud environment (default or custom) that defines network access, environment variables, and optional setup script.
5. Select trigger(s): schedule, GitHub event, API (URL and token generated after saving).
6. Review and optionally remove unused MCP connectors (Slack, Linear, Google Drive, etc.).
7. Click **Create**; the routine appears in the list and runs when a trigger matches. Use **Run now** to start immediately.

### From the CLI
- Use `/schedule` in any session to create a scheduled routine conversationally, e.g., `/schedule daily PR review at 9am`.
- The CLI supports only schedule triggers; add API or GitHub triggers later via the web UI.
- Manage routines with `/schedule list`, `/schedule update`, and `/schedule run`.

### From the Desktop app
- Open the **Schedule** page, click **New task**, choose **New remote task**.
- The app shows both local scheduled tasks and cloud routines in a single grid.

## Managing runs and limits
- Each run creates a new cloud session; you can view actions, review changes, and create pull requests.
- Routines belong to your individual Claude account, count against your daily run allowance, and act as you (GitHub commits, Slack messages, etc.).

## Key considerations
- Prompt must be explicit about desired outcome because runs are fully autonomous.
- Scope repositories, environment settings, and connectors to only what the routine needs.
- Permissions are determined by selected repositories, branch‑push settings, environment network access, and included connectors.
