---
title: 'GitHub - ComposioHQ/awesome-codex-skills: A curated list of practical Codex skills for automating workflows across the Codex CLI and API. · GitHub'
url: https://github.com/ComposioHQ/awesome-codex-skills
site_name: github
content_file: github-github-composiohqawesome-codex-skills-a-curated-li
fetched_at: '2026-04-25T11:37:22.835669'
original_url: https://github.com/ComposioHQ/awesome-codex-skills
author: ComposioHQ
description: A curated list of practical Codex skills for automating workflows across the Codex CLI and API. - ComposioHQ/awesome-codex-skills
---

ComposioHQ

 

/

awesome-codex-skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork117
* Star1.2k

 
 
 
 
master
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

22 Commits
22 Commits
brand-guidelines
brand-guidelines
 
 
canvas-design
canvas-design
 
 
changelog-generator
changelog-generator
 
 
codebase-migrate
codebase-migrate
 
 
competitive-ads-extractor
competitive-ads-extractor
 
 
composio-skills
composio-skills
 
 
connect-apps
connect-apps
 
 
connect
connect
 
 
content-research-writer
content-research-writer
 
 
create-plan
create-plan
 
 
datadog-logs
datadog-logs
 
 
deploy-pipeline
deploy-pipeline
 
 
developer-growth-analysis
developer-growth-analysis
 
 
domain-name-brainstormer
domain-name-brainstormer
 
 
email-draft-polish
email-draft-polish
 
 
file-organizer
file-organizer
 
 
gh-address-comments
gh-address-comments
 
 
gh-fix-ci
gh-fix-ci
 
 
helium-mcp
helium-mcp
 
 
image-enhancer
image-enhancer
 
 
internal-comms
internal-comms
 
 
invoice-organizer
invoice-organizer
 
 
issue-triage
issue-triage
 
 
langsmith-fetch
langsmith-fetch
 
 
lead-research-assistant
lead-research-assistant
 
 
linear
linear
 
 
mcp-builder
mcp-builder
 
 
meeting-insights-analyzer
meeting-insights-analyzer
 
 
meeting-notes-and-actions
meeting-notes-and-actions
 
 
notion-knowledge-capture
notion-knowledge-capture
 
 
notion-meeting-intelligence
notion-meeting-intelligence
 
 
notion-research-documentation
notion-research-documentation
 
 
notion-spec-to-implementation
notion-spec-to-implementation
 
 
paperjsx
paperjsx
 
 
pr-review-ci-fix
pr-review-ci-fix
 
 
raffle-winner-picker
raffle-winner-picker
 
 
sentry-triage
sentry-triage
 
 
skill-creator
skill-creator
 
 
skill-installer
skill-installer
 
 
skill-share
skill-share
 
 
slack-gif-creator
slack-gif-creator
 
 
spreadsheet-formula-helper
spreadsheet-formula-helper
 
 
support-ticket-triage
support-ticket-triage
 
 
tailored-resume-generator
tailored-resume-generator
 
 
template-skill
template-skill
 
 
theme-factory
theme-factory
 
 
video-downloader
video-downloader
 
 
webapp-testing
webapp-testing
 
 
README.md
README.md
 
 
codex_cover_image.png
codex_cover_image.png
 
 
View all files

## Repository files navigation

# Awesome Codex Skills

A curated list of practical Codex skills for automating workflows across the Codex CLI and API.

Want skills that do more than generate text?Codex can send emails, create issues, post to Slack, and take actions across 1000+ apps.See how →

## Quickstart: Add Skills to Codex

### Install with the Skill Installer (recommended)

git clone https://github.com/ComposioHQ/awesome-codex-skills.git

cd
 awesome-codex-skills/awesome-codex-skills

#
 Install one or more skills into $CODEX_HOME/skills (defaults to ~/.codex/skills)

python skill-installer/scripts/install-skill-from-github.py --repo ComposioHQ/awesome-codex-skills --path meeting-notes-and-actions

The installer fetches the skill and places it in$CODEX_HOME/skills/<skill-name>. Restart Codex to pick up new skills.

### Manual install

1. Copy the desired skill folder (e.g.,./spreadsheet-formula-helper) into$CODEX_HOME/skills/(defaults to~/.codex/skills/).
2. Restart Codex so it loads the new metadata.
3. In your next session, describe the task or mention the skill name; Codex will trigger matching skills based on theirdescriptionfrontmatter.

## Contents

* Bernstein- Multi-agent orchestrator with Codex CLI adapter. Runs parallel Codex agents in isolated git worktrees with quality gates.
* What Are Codex Skills?
* SkillsDevelopment & Code ToolsProductivity & CollaborationCommunication & WritingData & AnalysisMeta & Utilities
* Development & Code Tools
* Productivity & Collaboration
* Communication & Writing
* Data & Analysis
* Meta & Utilities
* Using Skills in Codex
* Creating Skills
* Contributing
* Join the Community

## What Are Codex Skills?

Codex skills are modular instruction bundles that tell Codex how to execute a task the way you want it done. Each skill lives in its own folder with aSKILL.mdthat includes metadata (name + description) and step-by-step guidance. Codex reads the metadata to decide when to trigger a skill and loads the body only after it fires, keeping context lean.

## Skills

### Development & Code Tools

* brooks-lint- AI code reviews grounded in six classic engineering books — decay risk diagnostics with book citations, severity labels, and four analysis modes (PR review, architecture audit, tech debt, test quality). Install:python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo hyhmrright/brooks-lint --path skills/brooks-lint --name brooks-lint
* codebase-migrate/- Run large codebase migrations and multi-file refactors in reviewable batches with CI verification.
* create-plan/- Quickly draft concise execution plans for coding tasks.
* deploy-pipeline/- End-to-end Stripe → Supabase → Vercel release pipelines with verify and rollback.
* Emdash Skills- 14-category autonomous product-building OS: CF Workers + Hono + Angular + D1 + Stripe. One-line prompts to deployed SaaS with 94 reference docs, 18 agents, and Codex-native.agents/skills/support.
* gh-address-comments/- Address review or issue comments on the open GitHub PR for the current branch usinggh.
* gh-fix-ci/- Inspect failing GitHub Actions checks, summarize failures, and propose fixes.
* mcp-builder/- Build and evaluate MCP servers with best practices and an evaluation harness.
* pr-review-ci-fix/- Automated GitHub/GitLab PR review plus CI auto-fix loop via the Composio CLI.
* sentry-triage/- Diagnose Sentry issues by mapping stack frames to local source — no copy-paste.
* webapp-testing/- Run targeted web app tests and summarize results.
* AuraKit- All-in-one skill framework: 46 modes, 23 sub-agents, 6-layer OWASP security, 10 lifecycle hooks, ~55% token savings. Install:npx @smorky85/aurakit

### Productivity & Collaboration

* connect/- Connect Codex to 1000+ apps via the Composio CLI for real actions (Slack, GitHub, Notion, etc.).
* connect-apps/- Wire up Composio CLI connections for Claude and kick off app workflows from the shell.
* issue-triage/- Triage Linear or Jira backlogs and run bug sweeps from the terminal.
* linear/- Manage issues, projects, and team workflows in Linear.
* meeting-insights-analyzer/- Analyze meeting transcripts for themes, risks, and follow-ups.
* meeting-notes-and-actions/- Turn meeting transcripts into summaries with decisions and owner-tagged action items.
* internal-comms/- Craft internal announcements, updates, and stakeholder messaging.
* invoice-organizer/- Normalize and extract invoice data for tracking and reporting.
* notion-knowledge-capture/- Convert chats or notes into structured Notion pages with proper linking.
* notion-meeting-intelligence/- Prepare meeting materials with Notion context plus Codex research.
* notion-research-documentation/- Synthesize multiple Notion sources into briefs, comparisons, or reports with citations.
* notion-spec-to-implementation/- Turn Notion specs into implementation plans, tasks, and progress tracking.
* support-ticket-triage/- Triage customer support tickets with categories, priority, next actions, and draft replies.
* file-organizer/- Organize, rename, and tidy files to keep workspaces clean.
* paperjsx/- Generate PPTX presentations, DOCX documents, XLSX spreadsheets, and PDF invoices/reports/charts from structured JSON. Runs locally via@paperjsx/mcp-server— no API key, no network calls.
* skill-share/- Share skills and reusable instructions across teammates.

### Communication & Writing

* email-draft-polish/- Draft, rewrite, or condense emails for the right tone and audience.
* changelog-generator/- Create clear changelogs from commits or summaries.
* content-research-writer/- Research and draft content with sourced citations.
* novel-writing- External repo: public Codex skill for fiction planning, chapter drafting, scene continuation, and revision.
* tailored-resume-generator/- Tailor resumes to job descriptions with quantified impact.

### Data & Analysis

* spreadsheet-formula-helper/- Write and debug spreadsheet formulas, pivots, and array formulas.
* competitive-ads-extractor/- Analyze competitor ads and extract structured insights.
* datadog-logs/- Filter Datadog logs from the shell via the Composio CLI, with JSON-friendly output and digest workflows.
* developer-growth-analysis/- Analyze Codex chat history for coding patterns and learning gaps.
* lead-research-assistant/- Research leads and enrich records with firmographic data.
* domain-name-brainstormer/- Brainstorm available domain names with criteria and checks.
* raffle-winner-picker/- Randomly select winners with audit-friendly logs.
* langsmith-fetch/- Pull LangSmith project/test data for analysis.
* helium-mcp/- Search real-time news with bias scoring, get live market data, ML options pricing, and balanced news synthesis via MCP.

### Meta & Utilities

* brand-guidelines/- Apply OpenAI/Codex brand colors and typography to artifacts.
* canvas-design/- Generate structured canvas layouts and design artifacts.
* image-enhancer/- Upscale and refine images with configurable presets.
* slack-gif-creator/- Generate GIFs for Slack with captions and styling.
* theme-factory/- Create reusable theme tokens and palettes.
* video-downloader/- Download and prepare videos for offline review.
* template-skill/- Starter template for building new skills.
* skill-installer/- Helper scripts to install skills from curated lists or GitHub paths.
* skill-creator/- Guidance for building effective Codex skills with progressive disclosure.

## Using Skills in Codex

* Skills live in$CODEX_HOME/skills(default~/.codex/skills). Each subfolder needs aSKILL.mdwithnameanddescriptionfrontmatter.
* After installing or updating a skill, restart Codex so it reloads metadata.
* In a session, describe the task naturally; Codex auto-triggers skills whose descriptions match the request. You can also mention a skill by name if you want it considered.
* To verify installation, list installed skills (ls ~/.codex/skills) and inspect metadata (head ~/.codex/skills/<skill>/SKILL.md).

## Creating Skills

Skill layout:

skill-name/
├── SKILL.md # Required: instructions + YAML frontmatter
├── scripts/ # Optional: helper scripts for deterministic steps
├── references/ # Optional: long-form docs loaded only when needed
└── assets/ # Optional: templates or files used in outputs

Basic SKILL.md template:

---

name
: 
my-skill-name

description
: 
What the skill does and when Codex should use it.

---

# 
My Skill Name

Clear instructions and steps for Codex to execute the task.

Best practices:

* Keep thedescriptionexhaustive about when to trigger; keep the body focused on execution steps.
* Use progressive disclosure: put detailed references inreferences/and call them out fromSKILL.mdonly when needed.
* Include scripts for repeatable or deterministic operations; mention when Codex should run them.
* Avoid extra docs (README, changelog) inside the skill folder to keep context lean.

## Contributing

PRs welcome. Add real, reusable skills, keep descriptions precise, and include any needed scripts or references. If you add new skills, ensure thedescriptionclearly states when Codex should trigger and test that metadata fits within context limits.

## Join the Community

* Join our Discord- Chat with other developers building Codex skills.
* Follow on X- Updates on new skills and features.
* Questions?support@composio.dev

Join thousands of developers building agents that ship

## About

A curated list of practical Codex skills for automating workflows across the Codex CLI and API.

### Topics

 awesome

 skills

 codex

 awesome-lists

 awesome-resources

 llm

 coding-agents

 codex-cli

 gpt-5-codex

 codex-skills

 coding-agent-skills

 gpt-5-1-codex

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.2k

 stars
 

### Watchers

5

 watching
 

### Forks

117

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%