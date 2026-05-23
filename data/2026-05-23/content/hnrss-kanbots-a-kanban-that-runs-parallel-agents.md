---
title: KanBots — a kanban that runs parallel agents
url: https://www.kanbots.dev/
site_name: hnrss
content_file: hnrss-kanbots-a-kanban-that-runs-parallel-agents
fetched_at: '2026-05-23T11:28:50.514118'
original_url: https://www.kanbots.dev/
date: '2026-05-22'
description: A kanban board that runs Claude Code and Codex agents in parallel. Drop a folder. Get a board. Dispatch on every card. Free, MIT-licensed OSS desktop. Cloud for teams.
tags:
- hackernews
- hnrss
---

v1.0 · MIT licensed
·
Open source on GitHub

# A kanban that runsparallel agentson every card.

Drop a folder. Get a board. Dispatch Claude Code or Codex agents on as many cards as you want — each in its own worktree. Or hit autopilot and let personas split the work, run in parallel, and check their own output while you sleep.

Download desktop
macOS · Linux · Windows
See cloud for teams

Free forever · Pay-what-you-can donations · MIT licensed

my-app workspace · my-app
main
my-app
/
Board
10 issues
·
 2 active
·
 1 awaiting
·
$1.06 today
+
 New task
Inbox
1
SENTRY
#42

TypeError: Cannot read properties of undefined (reading 'email')

4h
Backlog
2
FEAT
#37
p1

Stripe billing portal for subscriptions

9d
FEAT
#34
p2

Weekly email digest of new activity

12d
Todo
2
FEAT
#31
p2

Dark mode toggle in settings

4d
FEAT
#28
p2

Forgot password email flow

6d
In progress
3
FEAT
#24
p1
running

Sign in with Google

Edit
lib/auth/google.ts
feat/google-sso
+
18
−
2
$0.13
18h
FEAT
#22
p1
running

Email when invoice fails

Write
emails/invoice-failed.tsx
feat/invoice-emails
+
24
−
0
$0.31
14h
FIX
#19
p2
awaiting

Profile picture upload broken on iOS Safari

How should I handle iOS HEIC files?

1
Convert in browser
2
Convert on server
3
Reject HEIC
fix/ios-upload
16h
Review
2
FEAT
#15
p1

CSV export from admin dashboard

+
41
−
5
tsc
tests
lint
2d
CHORE
#11
p2

Migrate to next-intl for i18n

+
8
−
2
tsc
tests
lint
3d
.kanbots/db.sqlite · local-first · 0 telemetry
 claude-opus-4.7 ready

2

CLIs supported

Claude Code · Codex

0

bytes leave your machine

MIT

license · free forever

Two products on purpose

## Solo on a laptop, ora team that ships together.

Same kanban metaphor. Same agent runtime. Different scale of collaboration. Both are legitimate paths.

FREE FOREVER
MIT

### KanBots OSS

Desktop · local-first · no account · no telemetry

$0
+ pay-what-you-can donations
Download desktop

macOS · Linux · Windows · all features included

* Parallel agent dispatch
* Autopilot — feature-dev + qa
* Decision prompts
* Personas (built-in + custom)
* Cost analytics, live
* Recipe library
* MCP server (kanbots-mcp-server)
* Sentry import
* GitHub Issues mode (personal PAT)
* Branch preview
* Promote / draft PR
* Claude Code + Codex
* Pre-push hook (containment)
FOR TEAMS
per-seat

### KanBots Cloud

Hosted · multi-user · agents stay local on your hardware

$19
per seat / month · $190 billed yearly
Get Pro

Everything in OSS, plus the team features below.

* Real-time presence on the board
* Assignment notifications to teammates
* Cross-device sync
* Audit log for compliance (Enterprise)
* SSO / SCIM (Enterprise)
* Slack notifications
* Org-wide cost rollup
* Real-time collaborative card editing
* Per-org agent activity dashboard
* REST API + PATs (Enterprise)
* Outbound webhooks (Enterprise)
* Managed GitHub App

Every Cloud-only feature requires eitheranother personoranother devicein the picture. None of them help a solo user on one machine — so we don't gate them. OSS is what one person does on their machine; Cloud is what a team does together.

Plays nice

## Plays nice withthe tools you already use.

cl

Claude Code

CLI

co

Codex

CLI

GitHub

Issues + PRs

se

Sentry

Error import

cu

Cursor

MCP client

cl

Claude Desktop

MCP client

sq

SQLite

Local store

el

Electron

Desktop shell

Capabilities

## Built for the way agentsactually ship.

Not a chat tab. A board. Eight features that turn AI agents from a curiosity into a system of record.

### Parallel agents on the board

Dispatch on as many cards as you want; each agent runs in its own git worktree on a kanbots/issue-N branch. The board updates live as runs progress, decisions surface, costs accrue.

### Autopilot — self-evolving feature dev

Plug in personas — product, engineer, reviewer, tester — and a parallelism count up to 4. The orchestrator round-robins through personas, splits parent issues into subtasks, and evolves the backlog as agents discover work. Personas spawn personas.

### Decision prompts you actually answer

Agents pause and ask. You click an option; the run continues. Numbered shortcuts, edit-and-resubmit, slash commands like /spec, /review, /split. Reviewable decisions, not silent tree mutations.

### Bring your own CLI

Claude Code or Codex. Same board, same worktrees, same decision UI — kanbots speaks both stream formats behind a single AgentCliAdapter. Use your existing claude /login or OPENAI_API_KEY.

### Local-first, zero servers

Everything lives in .kanbots/ next to your repo: SQLite database, configs, worktrees. No cloud account, no telemetry, no HTTP server. Your code never leaves the machine.

### Cost analytics, live

Per-run, per-card, per-project rollups. Watch the cost meter accrue as agents work. Set per-run and per-session caps; runs stop on cost-budget. No surprise bills.

### GitHub mode + draft PRs

Drive real GitHub issues with your personal PAT. Promote a worktree to a commit, or open a draft PR with one click. A pre-push hook means agents never publish on their own.

### MCP server included

kanbots-mcp-server exposes the board over the Model Context Protocol so Cursor, Claude Desktop, or anything MCP-aware can drive it. The board becomes a first-class tool for your other agents.

Inside the app

## Every surface,designed for the loop.

Not just a wrapper around a CLI. A full UI for dispatching, reviewing, splitting, and shipping agent work.

AUTOPILOT

### Pick personas. Set parallelism. Walk away.

Up to 4 parallel slots round-robin through your roster. Each slot atomically claims the next persona; agents split parents into subtasks as they go. Stops on completion or session budget.

my-app workspace · my-app
main
kanbots
·
Start an autopilot
×
Feature dev
QA 
soon

Pick one or more personas. The autopilot will cycle through them in order, ideating and shipping features until you stop it.

model
Claude Opus 4.7
effort
medium
parallel
2
🎯
✓
Product Manager
User value, prioritization, market fit
🏗
✓
Senior Engineer
Architecture, dev experience, tech debt
🎨
UX Designer
Flows, polish, accessibility
📈
Growth Lead
Activation, retention, virality
🛡
Reliability Engineer
Robustness, observability, security
✦
Agent Expert
Custom · orchestration & containment

Need a different perspective?Refresh personas— create custom ones from the Suggest flow on the Backlog column.

2 personas selected · parallelism 2.
Cancel
Start autopilot
DECISIONS

### Decisions, not silent mutations.

Live thread streams every tool_use and tool_result. When the agent needs a call, the run pauses with numbered options. Reply box accepts slash commands: /spec, /review, /split.

my-app
·
#28
Forgot password email flow
Stop
·
Fork run
Open preview ↗
#28

### Forgot password email flow with secure reset token

awaiting input · run #5
FEAT
 feat/forgot-password
opened 16h ago
Overview
Thread
Diff
Preview
Runs
agent thread · run #5 · awaiting input

— moved to In progress · 3m ago —

claude
·
1s ago
I've drafted three approaches for the password reset token. Which one fits your security requirements?
1
Single-use JWT signed with HS256, 15 min expiry
2
DB-stored opaque token, 1 hour expiry, revocable
3
Magic link only — no token, email-verified login
4
I'll explain the tradeoffs first
Dismiss
Bash
( 
pnpm test lib/auth/__tests__/reset-token.test.ts
 )
▸
just now
Reply to agent
/spec to refine · /review to spawn reviewer · /split to fan out…
Send
⌘↵
Live run
model
claude-opus-4.7
elapsed
3m 18s
tokens
7.7k in
cost
$0.10
tsc
tests
lint
Run checks
Open worktree ↗
Properties
Status
awaiting input
Priority
P2
Folder
my-app
Worktree
.kanbots/.../issue-28-5
Branch
feat/forgot-password
Base
main
Author
L
Leonardo Cunha
PERSONAS

### Personas as first-class lenses.

A persona is a named system prompt snippet. Built-ins ship with the app; New persona lets you write your own — save, reuse forever. Custom personas stay on your machine.

my-app workspace · my-app
main
kanbots
·
Pick a perspective
×

The selected agent will look at your repo and the backlog through the lens you pick. Feature suggestions shift accordingly.

🎯
Product Manager
User value, prioritization, market fit
🏗
Senior Engineer
Architecture, dev experience, tech debt
🎨
UX Designer
Flows, polish, accessibility
📈
Growth Lead
Activation, retention, virality
🛡
Reliability Engineer
Robustness, observability, security
+
New persona
Define your own perspective

Custom personas are stored locally on this machine.

Cancel
PROVIDERS

### Bring your own CLI.

Claude Code or Codex behind one AgentCliAdapter. Reuse your existing claude /login or codex login — no extra account, no extra key management. Switch per dispatch.

my-app workspace · my-app
main
AI providers
×
Claude Code subscription
configured

Use your Claude Code account session. Best for agentic runs.

✓
Enabled

✓ Signed in to Claude Code.

Default model
Claude Opus 4.7
Test connection
Save
Codex CLI (OpenAI)

Run agent tasks through OpenAI's codex CLI. Requires `codex` on PATH. Issue drafting and Sentry analysis still run on Claude.

✓
Enabled

Spawns codex login and opens auth.openai.com in your browser. You can also set OPENAI_API_KEY in your environment.Learn more

Sign in with codex
Default model
GPT-5
Test connection
Save
Close
TASKS

### Spec first. Or dispatch immediately.

Bug fix · Feature · Refactor · Review · Spike templates. Three start modes: spec-first (run /spec, await approval), create-and-dispatch, or queue-for-later. Title becomes branch + PR title.

my-app
·
New task
Press ⌘↵ to create
Title
→ becomes branch + PR title
e.g. Add “Sign in with Google” to the login page
Template
!
Bug fix
+
Feature
~
Refactor
?
Review
*
Spike
Description
Markdown · use AC: for acceptance criteria
What is the user-facing outcome?
AC:
- “Continue with Google” button on /login
- New users land on onboarding; returning users on /home
How should this start?
✦
●
Spec first
Run /spec to refine acceptance criteria. Wait for my approval.
▸
Create & dispatch
Spawn the agent immediately on a fresh worktree.
◷
Queue for later
Sit in the Backlog. I'll start it manually.
Agent
assignee
claude (auto)
model
Claude Opus 4.7
effort
medium
provider
claude-code
How it'll appear
Awaiting input
FEAT
#0
P2
Queued
Untitled task
claude/untitled
1s

Branchclaude/untitledoffmainin.kanbots/worktrees/issue-N.

Will create a worktree and run /spec — agent waits for approval.
Cancel
Create & spec
⌘↵
CHAT

### Talk to the workspace.

Ask anything — "which routes don't have rate limiting?", "where do we use the old auth helper?". A general-purpose agent that knows your repo, your tests, and your git state.

my-app chat
·
general-purpose agent
which API routes don't have rate limiting?
 run #12 · COMPLETE
you
which API routes don't have rate limiting?
Grep
(
router\\.(post|get|put|delete) src/routes
)
▸ 2d ago
claude
 
· 2d ago
Found 23 routes. 
8 of them
 don't pass through
 
rateLimit
 middleware:
 
/api/login
,
 
/api/signup
,
 
/api/forgot-password
… want the full list?
you
add rate limiting to /api/login and /api/signup
Edit
(
src/routes/auth.ts
)
▸ 2d ago
claude
 
· 2d ago
Done — added
 
rateLimit(
{
 windowMs: 60_000, max: 10 
}
)
 
to both. Want me to write a test that hits the cap?
you
yes, test all 5 attempts then expect 429
Write
(
src/routes/__tests__/auth.rate-limit.test.ts
)
▸ 2d ago
claude
 
· 2d ago
Test added and passing — 
tests 14 passed
. Anything else?
Ask the agent…
Send
› Options
⌘↵ to send

Autopilot

## Personasspawn personas.The backlog evolves itself.

Hand kanbots an issue and a budget. The orchestrator round-robins through a roster of personas, runs up to four slots in parallel, splits parent issues into subtasks, and keeps cycling until the work converges or the cost cap hits.

Autopilot · Feature Dev

### Pick a perspective

parallel
4
model
opus 4.7
🎯
Product Manager

User value · prioritization · market fit

🏗️
Senior Engineer

Architecture · dev experience · tech debt

🎨
UX Designer

Flows · polish · accessibility

📈
Growth Lead

Activation · retention · virality

🛡️
Reliability Engineer

Robustness · observability · security

+
 New persona
cycle 14
$4.27 of $25.00 session budget
Product Manager
Draft AC for #54
completed
Senior Engineer
Implement bridge schema in #54
running
UX Designer
Review #48 for keyboard-only flow
awaiting
Growth Lead
Spawn #61 — onboarding banner experiment
queued
1. 01#### Pick a rosterBuilt-in personas ship with kanbots; or write your own — define the system prompt, save, reuse forever. Custom personas never leave your machine.
2. 02#### Set parallelism (1–4)Each slot atomically claims the next persona via a round-robin counter. Four agents, four lenses, four worktrees — at the same time.
3. 03#### Personas split workAs agents discover work, they file new cards on the board. Later cycles pick those up. The backlog grows and shrinks under the orchestrator.
4. 04#### Stop on budget or completionPer-session cost budget caps total spend. Stop button kills the parent and all children. In-flight runs finish their iteration cleanly.

QA mode

Run typecheck / tests / lint / build / e2e in the worktree. Optionally start your dev server and watch it. For every failing check, dispatch a fix run on a derived child issue. Repeat until green.

tsc
tests
lint
build
e2e
 Free · MIT · No account

## Stop talking to chat tabs.Ship from a board.

Download the OSS desktop app today and put every agent run on a kanban — visible, decisioned, contained. When your team needs to share a board, cloud is one upload away.

Download desktop
Star on GitHub
See cloud for teams →

macOS .dmg · Windows .exe · Linux .AppImage / .tar.xz