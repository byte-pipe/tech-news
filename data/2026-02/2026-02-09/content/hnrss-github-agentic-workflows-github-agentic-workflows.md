---
title: GitHub Agentic Workflows | GitHub Agentic Workflows
url: https://github.github.io/gh-aw/
site_name: hnrss
content_file: hnrss-github-agentic-workflows-github-agentic-workflows
fetched_at: '2026-02-09T11:22:46.388781'
original_url: https://github.github.io/gh-aw/
date: '2026-02-08'
description: Automated repository agents running in GitHub Actions.
tags:
- hackernews
- hnrss
---

# GitHub Agentic Workflows


Repository automation, running the coding agents you know and love, with strong guardrails in GitHub Actions.



 Quick Start with CLI


 Creating Workflows







Imagine a world where improvements to your repositories are automatically delivered as pull requests each morning, ready for you to review. Issues are automatically triaged, CI failures analyzed, documentation maintained, test coverage improved and compliance monitored - all defined via simple markdown files.

GitHub Agentic Workflows deliver this: repository automation, running the coding agents you know and love, in GitHub Actions, with strong guardrails and security-first design principles.

Use GitHub Copilot, Claude by Anthropic or OpenAI Codex for event-triggered, recurring and scheduled jobs to improve, document and analyze your repository. GitHub Agentic Workflows are designed toaugmentyour existing, deterministic CI/CD withContinuous AIcapabilities

GitHub Agentic Workflows has been developed by GitHub Next and Microsoft Research with guardrails in mind. Agentic workflows run with minimal permissions by default, with explicit allowlisting for write operations and sandboxed execution to help keep your repository safe.

## Key Features

Section titled “Key Features”







### Automated Markdown Workflows






Write automation in markdown instead of complex YAML









### AI-Powered Decision Making






Workflows that understand context and adapt to situations









### GitHub Integration






Deep integration with Actions, Issues, PRs, Discussions, and repository management









### Safety First






Sandboxed execution with minimal permissions and safe output processing









### Multiple AI Engines






Support for Copilot, Claude, Codex, and custom AI processors









### Continuous AI






Systematic, automated application of AI to software collaboration





### Guardrails Built-In

Section titled “Guardrails Built-In”

Workflows run with read-only permissions by default. Write operations require explicit approval through sanitizedsafe outputs(pre-approved GitHub operations), with sandboxed execution, tool allowlisting, and network isolation ensuring AI agents operate within controlled boundaries.

## Example: Daily Issues Report

Section titled “Example: Daily Issues Report”

How they work:

1. Write- Create a.mdfile with your automation instructions in natural language
2. Compile- Rungh aw compileto transform it into a GitHub Actions workflow with guardrails (.lock.yml)
3. Run- GitHub Actions executes your workflow automatically based on your triggers

Here’s a simple workflow that runs daily to create an upbeat status report:

---
on
:

schedule
:
daily
permissions
:

contents
:
read

issues
:
read

pull-requests
:
read
safe-outputs
:

create-issue
:

title-prefix
:
"
[team-status]
"

labels
: [
report
,
daily-status
]

close-older-issues
:
true
---

## Daily Issues Report

Create an upbeat daily status report for the team as a GitHub issue.

Thegh awcli converts this into a GitHub Actions Workflow (.yml) that runs an AI agent (Copilot, Claude, Codex, …) in a containerized environment on a schedule or manually.

The AI coding agent reads your repository context, analyzes issues, generates visualizations, and creates reports - all defined in natural language rather than complex code.

## Gallery

Section titled “Gallery”







### Continuous Improvement






Daily code simplification, refactoring, and style improvements









### Continuous Refactoring






Slash commands for on-demand analysis and automation









### Continuous Documentation






Continuous documentation maintenance and consistency









### Issue & PR Management






Automated triage, labeling, and project coordination









### Metrics & Analytics






Daily reports, trend analysis, and workflow health monitoring









### Continuous Scanning & Compliance






Scanning, alert triage, and compliance monitoring









### Quality & Testing






CI failure diagnosis, test improvements, and quality checks









### Multi-Repository






Feature sync and cross-repo tracking workflows









### Scheduled Workflows






DailyOps, research, and automated maintenance





## Getting Started

Section titled “Getting Started”






Your browser doesn't support HTML5 video. Download the videohere.





Install the extension, add a sample workflow, and trigger your first run - all from the command line in minutes.

## Creating Workflows

Section titled “Creating Workflows”






Your browser doesn't support HTML5 video. Download the videohere.





Create custom agentic workflows directly from the GitHub web interface using natural language.




Made withbyGitHub Next&Microsoft Research•Terms of Service
