---
title: 'GitHub - akitaonrails/ai-memory: Solution for long term memory for agent coding CLIs and to facilitate handoff between different agent vendors · GitHub'
url: https://github.com/akitaonrails/ai-memory
site_name: github
content_file: github-github-akitaonrailsai-memory-solution-for-long-ter
fetched_at: '2026-08-16T11:18:43.140669'
original_url: https://github.com/akitaonrails/ai-memory
author: akitaonrails
description: Solution for long term memory for agent coding CLIs and to facilitate handoff between different agent vendors - akitaonrails/ai-memory
---

akitaonrails

 

/

ai-memory

Public

* NotificationsYou must be signed in to change notification settings
* Fork162
* Star1.5k

 
 
 
main
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

1,231 Commits
1,231 Commits
.github
.github
 
 
bin
bin
 
 
companions/
ai-memory-importer
companions/
ai-memory-importer
 
 
crates
crates
 
 
docker
docker
 
 
docs
docs
 
 
evals
evals
 
 
hooks
hooks
 
 
packaging
packaging
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
.ignore
.ignore
 
 
.mailmap
.mailmap
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
deny.toml
deny.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

Long-term memory for AI coding agents. Quit Claude Code mid-task,
start OpenAI Codex in the same directory, continue without
re-explaining the architecture, the failed approaches, or the open
questions.

## Support Matrix

Area

Status

Notes

Linux

Supported

Primary Docker/server target and CI platform. Published Docker images support 
linux/amd64
 and 
linux/arm64
. Native Arch/AUR packages include system and user systemd units.

macOS

Supported

Workspace tests run in CI; tagged releases publish native 
ai-memory-macos-aarch64.tar.gz
 and 
ai-memory-macos-x86_64.tar.gz
 binaries. The native binary is the recommended path on Apple Silicon. See 
docs/macos.md
.

Windows via WSL2

Supported

Use the Linux install path inside WSL2 when the agent runs there.

Native Windows

Experimental

Tagged releases publish 
ai-memory-windows-x86_64.zip
 with 
ai-memory.exe
; Docker Desktop wrapper and source builds are also available. Local supported profiles default to host-native hook commands; Claude Code may use its Windows exec form, while other agents use native single command strings matching their hook schema. PowerShell/Git Bash scripts are compatibility fallbacks. See 
docs/windows.md
.

Claude Code

Supported

MCP config + lifecycle hooks; native commands enforce capture exclusions. 
install-mcp --session-aware
 optionally enables per-session auto-scope isolation through a local stdio bridge. Optionally captures the assistant's final turn on 
Stop
 when installed with 
--capture-assistant
 and the server enables 
capture_assistant
 (double opt-in, off by default).

Codex

Supported

MCP config + lifecycle hooks; native commands enforce capture exclusions. No automatic true session-end hook, so run 
ai-memory finalize-session
 when you need a final summary/handoff.

Command Code

Supported

MCP config (
~/.commandcode/mcp.json
) + its four stable lifecycle-hook events (
~/.commandcode/settings.json
); native commands enforce capture exclusions and 
SessionStart
 injects handoffs. 
Stop
 is only a turn boundary, so use 
ai-memory finalize-session --agent command-code
 after the final turn. 
ai-memory run command-code
 adds exact v3 native-session resume and visible-event import; experimental unsandboxed Mods remain excluded.

Devin CLI

Supported

MCP config + lifecycle hooks. Hooks use Devin's 
PostCompaction
 event, inject handoffs via 
hookSpecificOutput.additionalContext
, and omit subagent events because Devin does not expose them.

OpenCode

Supported

Remote MCP config + generated TypeScript plugin; generated plugin enforces capture exclusions.

Cursor

Supported

MCP config + lifecycle hooks.

Gemini CLI

Supported

MCP config + lifecycle hooks.

Oh My Pi / OMP

Supported

Use 
--client omp
 / 
--agent omp
 (or 
oh-my-pi
) for native 
.omp
 MCP config + TypeScript extension; generated extension enforces capture exclusions.

Pi

Supported

Generated 
~/.pi/agent/extensions/ai-memory.ts
 extension provides lifecycle capture and an HTTP MCP bridge; generated extension enforces capture exclusions.

Crush

Managed-only

ai-memory run crush
 resumes its project-local session database and supplies portable context through a temporary supported global-context file; no lifecycle-hook installer is provided.

Managed workstreams

Opt-in

ai-memory run
 provides transparent cross-harness continuity for Claude Code, Codex, OpenCode, Pi, Crush, Kimi Code, Command Code, both incompatible Kiro CLI engines, OMP, Grok Build CLI, and Antigravity CLI. Direct launches remain unchanged. See 
docs/managed-workstreams.md
.

Claude Desktop

MCP-only

Uses 
mcp-remote
; no lifecycle hooks.

OpenClaw

Supported

MCP config + native plugin lifecycle hooks; generated plugin enforces capture exclusions.

Antigravity CLI

Supported

MCP config (
serverUrl
) + lifecycle hooks (
agy
 alias). Only 
PreInvocation
 with 
invocationNum = 0
 maps to SessionStart; later model calls cannot consume a next-session handoff. No automatic true session-end hook, so run 
ai-memory finalize-session --agent antigravity-cli
 after the final turn when you need a summary, handoff, and opt-in SessionEnd consolidation. 
ai-memory run antigravity
 (aliases 
antigravity-cli
, 
agy
) adds managed workstream resume via 
--conversation
; conversation text is not decoded, so the ledger for this harness comes from hook capture.

Grok Build CLI

Supported

MCP config (
install-mcp --client grok
 → 
$GROK_HOME/config.toml
, default 
~/.grok/config.toml
) + lifecycle hooks (
install-hooks --agent grok
 → 
$GROK_HOME/hooks/ai-memory.json
, default 
~/.grok/hooks/ai-memory.json
, Grok-specific hook bundle). Capture works; no hook handoff injection — Grok ignores 
SessionStart
 stdout, so recover handoffs via MCP 
memory_handoff_accept
. 
ai-memory run grok
 adds managed workstream resume with the context packet delivered natively through 
--rules
. Skills root: 
.grok/skills
 / 
$GROK_HOME/skills
 (default 
~/.grok/skills
).

Swival CLI

MCP-only

install-mcp --client swival --apply
 merges a native HTTP entry into the project-root 
.swival/mcp.json
, preserving sibling servers. Lifecycle and managed-workstream support are not claimed because Swival's callback contract does not expose a stable session identifier.

Zero

Supported

install-mcp --client zero
 (native HTTP + bearer in 
~/.config/zero/config.json
) + lifecycle hooks via 
install-hooks --agent zero --apply
 (exec-form native commands in 
~/.config/zero/hooks.json
, JSON payload on stdin, no shell). Capture works incl. specialist (subagent) events; no handoff injection — Zero discards 
sessionStart
 stdout, so recover handoffs via MCP 
memory_handoff_accept
.

Kimi Code

Supported

MCP config (
url
 entry in 
~/.kimi-code/mcp.json
) + lifecycle hooks (
[[hooks]]
 in 
~/.kimi-code/config.toml
, 10 events including subagent start/stop and 
PostToolUseFailure
 for tool-failure capture); both paths honor 
$KIMI_CODE_HOME
. Handoffs inject via 
UserPromptSubmit
 stdout (Kimi Code discards 
SessionStart
 hook stdout); 
ai-memory run kimi
 adds managed workstream resume.

Kiro CLI

Supported

MCP config uses 
install-mcp --client kiro-cli
 (alias 
kiro
) and Kiro's Bedrock-compatible schema flavor. 
install-hooks --agent kiro-cli
 merges v2 hooks into existing agent configs; the explicit 
--agent kiro-cli-v3
 target writes the incompatible standalone v3 registration. Both preserve unrelated entries, honor 
$KIRO_HOME
, enforce capture exclusions, and inject pending handoffs at session start. Kiro has no true SessionEnd hook; use 
ai-memory finalize-session --agent kiro-cli
, with 
--session-id <uuid>
 for concurrent sessions. 
ai-memory run kiro
 manages v2; add 
--v3
, 
--mode
, or 
--agent-engine v3
 for version-safe v3 resume.

VS Code Copilot

MCP-only

.vscode/mcp.json
 for Copilot agent mode; no lifecycle hooks (Copilot does not expose them yet).

Zed

MCP-only

Native remote MCP under 
context_servers
 in Zed's user 
settings.json
; no lifecycle hooks or managed-workstream support.

Hermes Agent

Community

Core hook ingestion recognizes 
agent=hermes
 and Hermes' documented shell-hook 
tool_name
 / 
tool_input
 payload for concrete session attribution, tool-family titles, and capture exclusions. A community-maintained 
ai-memory-hermes-plugin
 is available, but no first-party installer is shipped; review its compatibility matrix, install/uninstall scripts, and secret handling before using it. Hermes ignores session-start hook stdout, so recover handoffs through MCP.

LLM/auth providers

Supported

Anthropic, OpenAI, OpenAI OAuth/Codex, GitHub Copilot, Gemini, OpenCode Zen/Go, OpenAI-compatible endpoints, and generic OIDC device auth for native hooks.

Embedding providers

Supported

OpenAI, Voyage, Google Gemini, and keyless OpenAI-compatible endpoints such as Ollama, LM Studio, and vLLM.

## What it is

LLM coding agents lose context when a session ends. ai-memory gives them a
shared, persistent wiki compiled from sanitized lifecycle observations. When a
session ends, relevant observations become a coherent summary; the next agent
receives a bounded handoff. Optionalai-memory runlaunches add a portable
visible-event ledger and native per-harness resume for higher-fidelity
cross-harness continuity.

The wiki is plain markdown in a git repo -grep-able, openable in
Obsidian, backed up withrsync. No vector database to babysit, nowrite_noteceremony, no manual context-loading. The full design is
indocs/ARCHITECTURE.md; the influences and
priors are at thebottom.

## Key features

* Zero-friction lifecycle capture.Hooks fire-and-forget bounded,
sanitized prompt, tool-lifecycle, and session-boundary observations. Direct
launches keep this lightweight path; it is not a complete native transcript.
User prompts and post-compaction summaries retain up to 16 KiB;
notifications and tool excerpts retain up to 2 KB, with a 16 KiB durable
backstop for every observation body.
* Opt-in managed workstreams.ai-memory run claude, thenai-memory run codex --yolo, thenai-memory run command-code, transparently resumes one
logical workstream with native per-harness sessions, a portable visible-event
ledger, and full-ledger search. Delivered packets are origin-marked; Claude
transcript import rejects a packet that Claude persisted and read back through a tool.ai-memory runwith no harness continues the newest usable Claude Code,
Codex, OpenCode, Pi, Crush, Kimi Code, Command Code, or Kiro CLI v2/v3
session for this checkout.
On first
explicit use, an interactive launcher can adopt a previous session from the
same checkout; later switches cannot select unrelated native history. Native
arguments pass through unchanged except the wrapper-owned--yoloand--fresh; direct
commands are unaffected.kimi-codeandkimi-cliare accepted aliases for
the installedkimicommand;commandcode,cmdc, andcmdselect the
cross-platformcommand-codeexecutable (cmdcon native Windows); andkiro-cliselects the installedkiro-clicommand. Kiro defaults to v2;ai-memory run kiro --v3selects v3, while a
returning linked v3 workstream selects its engine transparently.
* Per-repository capture exclusions.A nearest-marker[capture]ignore_pathspolicy drops matching recognized file-tool events before they
reach the local spool or server. Seethe capture policy reference.
* Optional per-operator memory slots.On shared servers,[slots] per_user = truekeeps engine-written_slots/context in a bounded
namespace derived from the authenticated operator. Session briefs and
consolidation prompts receive shared slots plus the caller's own; exact wiki
reads and searches remain project-wide, so this is context-injection
isolation rather than RBAC. Seemulti-user operation.
* Cross-agent handoffs.Quit Claude Code mid-task, start Codex
in the same directory hours later - the next agent sees a
"where you left off" block before its first prompt.
* Per-project isolation by construction.Each project lives at<wiki_root>/<workspace_id>/<project_id>/…keyed by stable UUIDs.
Workspace defaults to"default". Project is derived from$cwd:
CLI subcommands (bootstrap,write-page,lint, …) walk to the
main git repo root so all worktrees of the same repo share one
project identity; the hook router defaults tobasename($cwd)and
can opt into the repo-root rule. Drop a.ai-memory.tomlmarker filein any
ancestor directory to override either field explicitly — perfect for
multi-client consultancies, work/personal split, mono-repos, or
linked git worktrees.
Same page path can exist in two projects without collision; a
rename is one column update; a purge is onerm -rf.
* Global preferences scope.Standing user/team context — tech
choices, code style, durable personal rules — lives in the reserved_globalscope (memory_write_pagewithscope: "global"). Defaultmemory_queryreads union it into every project asglobal_scope_hits, so preferences travel with you into new projects
without naming a magic project or paying the all-projectsglobal=truefan-out. Event capture never writes there.
* Entity-assisted recall.Consolidation stores up to 10 specific nouns per
page in canonicalentities:frontmatter. Exact, prefix, and compound-word
matches form a project-scoped RRF stream, so a query can recover a page even
when its body uses different wording. The stream is lexical and adds no
query-time LLM call.
* Authority-aware recall.FTS5, entity-match RRF, graph-neighbor RRF, and
optional vector RRF generate candidates by relevance. Before truncation, a
bounded adjustment favors maintained_rules/,decisions/,procedures/, andgotchas/pages over closely matching episodic session evidence. Tier,pinned, and explicitcanonical/active/source-of-truthorsuperseded/historical/test-fixture/do-not-answer-fromtags
contribute without becoming absolute filters, so targeted history searches
still find session pages. These signals affect retrieval provenance only;
retrieved text remains untrusted historical evidence and never gains
instruction authority from its namespace, tier, tags, pin, or rank.
* Clear routing alongside code-intelligence tools.Run ai-memory beside a
structural MCP server, LSP, or other live-code tool without synchronizing
their stores. Use memory for prior decisions, rationale, failed attempts,
procedures, and handoffs; use the current checkout and structural provider
for symbols, callers, dependencies, and impact analysis. Verify historical
code claims against the checkout before acting, and treat source, builds,
tests, and observed runtime behavior as operational truth. SeeHistorical memory and live code intelligence.
* Karpathy-style LLM wiki.Pages are compiled from observations
at session-end (or PreCompact; clients without a true session-end event can
useai-memory finalize-session --agent <agent>for a manual final close),
not retrieved over raw logs.
Supersession chain + git-versioned markdown means you can
time-travel withai-memory checkpoints,restore-page, or rawgit log.
* Built-in/webbrowser.Read-only HTML UI for the wiki -
project list, folder tree, FTS5 search, markdown rendering, dark
mode. Mounted on the same axum server as MCP.
* Server-wide MCP client activity.GET /admin/activity/by-client?since_days=7shows which MCP clients are
calling memory tools, split into reads and writes. Counts use bounded UTC-day
buckets, so arbitrary client names cannot grow the database with request
volume; shared deployments keep the endpoint root-only. SeeMCP client activity.
* Multi-agent + multi-machine ready.Supported clients: Claude
Code, Codex, Command Code, Devin CLI, OpenCode, Cursor, Claude Desktop (viamcp-remote),
Gemini CLI, Antigravity CLI, Grok Build CLI, Kimi Code, OpenClaw, Oh My Pi
/ OMP (omp/oh-my-pi), Pi via generated bridge extension, VS Code
GitHub Copilot agent mode (MCP-only, workspace.vscode/mcp.json), Kiro CLI
(MCP + v2 lifecycle hooks), and Zed (MCP-only, usersettings.json).
Server runs local (loopback) OR on a homelab box (LAN/VPN/cloud)
with bearer-token auth. Shared servers can opt into[auto_scope]modesfor per-user or
session-aware current-project routing; Claude Code has a built-in opt-in
bridge viainstall-mcp --session-aware.
* Thin-client CLI.ai-memory status,bootstrap,checkpoints,restore-page,purge-project,rename-project,move-project,audit-contamination,lint,curator,auto-improve,auto-improve-report,pending-writes,embed,forget-sweep,backup,finalize-sessionare
all HTTP clients of the running server - never touch SQLite or
wiki files directly.statusalso reports passive LLM/embedding
provider health from the last real provider call. Server is the
single source of truth.finalize-sessionlists matching open
sessions throughGET /admin/open-sessions, then posts syntheticsession-endhooks back to the server. On shared deployments it defaults to
the caller's own plus unattributed sessions; root can pass--all-ownersfor
explicit cross-operator recovery. When concurrent sessions share an agent and
scope, pass--session-id <uuid>to target one exact open session; it cannot
be combined with--all.
* LLM is opt-in.Zero-LLM mode still gives you FTS5, manually declared
entity, and graph-neighbor search plus rule-based summarisation. Add a
provider when you want consolidated pages, lint contradictions, or staged
auto-improvement proposals.

## Use cases

* "Quit Claude Code and continue the same work in Codex."Use the optional
managed launcher when you want native session resume plus the portable visible
history, not only a summary handoff:cd/path/to/project
ai-memory run claude#Quit Claude Code, then continue the same workstream in Codex.ai-memory run codex --yolo#Continue in Command Code, preserving its own exact native session.ai-memory run command-code#Later, omit the name to resume the newest usable managed session here.ai-memory run#Start a new Codex session in the same workstream, keeping portable history.ai-memory run --fresh codex#Kiro defaults to v2; select its incompatible v3 engine explicitly once.ai-memory run kiro --v3
* "Pick the project instead of remembering where it lives."Start from a
directory containing your checkouts and choose the checkout before the
managed harness:ai-memory show#Machine-readable discovery without launching anything.ai-memory show --jsonEach successfulai-memory runsaves a client-local checkout link keyed by
the configured server plus workspace/project.showjoins those links with
the server's public activity and page-count metadata. A fast, bounded depth-1
scan of the current directory also finds new checkouts carrying a project
marker (.git,Cargo.toml,package.json,go.mod,pyproject.toml, and
friends), while skipping dependency and build directories. The server never
exposes a checkout path, so two client machines can safely use different
local paths for the same project on a remote homeserver.The list always leads with+ New project: type a name and ai-memory
validates a portable directory name, stages the new checkout privately, pins
its workspace and project in.ai-memory.toml, and installs the routing block
and managed Agent Skills for the chosen agent. The final directory appears
only after every setup step succeeds, thenshowlaunches from it.The harness menu only offers agents actually installed on the host, using the
samePATHlookuprunenforces at launch.--no-scanuses only saved links;--workspacefilters both sources;--yolo,--fresh, and trailing native arguments are forwarded unchanged.
Non-terminal use must pass--json; JSON mode is discovery-only and never
launches a harness.The first explicit run can offer an existing session from this exact checkout
or start a new one. Switching harnesses starts or resumes the native session
linked to the shared workstream, so an obsolete local session cannot replace
newer cross-harness history. After a normal quit, the next launch waits
briefly if the previous launcher is still finalizing; handled failures release
the workstream immediately. If a linked native transcript was deleted,
ai-memory detects the orphan before launch and starts fresh;--freshforces
that recovery for one harness. Managed mode currently covers Claude Code,
Codex, OpenCode, Pi, Crush, Kimi Code, Command Code, Kiro CLI v2/v3, OMP,
Grok Build CLI, and Antigravity CLI; direct harness launches remain unchanged. SeeManaged cross-harness workstreams.
* "Just put me back where I was."From any directory, with no name to
type and no list to read:ai-memorycontinueIt picks the checkout whose managed launch is most recent, revalidates the
path and its resolved scope, then continues there exactly as bareai-memory runwould. A link whose directory moved, was replaced, now
resolves to a different project, or has a corrupt ordering timestamp is
reported on stderr and skipped, so a resume never quietly lands in the wrong
project.--workspacenarrows the search;--yoloand--freshare
forwarded.
* "Quit at 4 PM, pick up at 9 AM in a different agent."The
classic. SessionStart hook in the next supported hook client prepends a
typed handoff with open questions, next steps, and a session summary. Grok
captures lifecycle events but ignores SessionStart stdout, so ask it to callmemory_handoff_acceptwhen resuming from a handoff. Zero has the same
no-stdout behavior and also must callmemory_handoff_accept.
* "What did we decide about X six weeks ago?"Usememory_query Xfrom
the agent for FTS5 fused with entity matches and linked-page expansion (plus
vector similarity when an embedder is configured). For a quick terminal-only
FTS5 lookup, useai-memory search X; that admin command does not run the
hybrid streams. Pages are
LLM-consolidated, so the hit is a coherent decision page, not a raw
chat log. Passexplain: trueto see why each hit ranked where it
did in project or explicit-scope retrieval. Cross-projectglobal: truesearch uses its separate FTS-only ranker and reports
that active stream without per-hit RRF details.
* "Remember this permanently."When something is worth keeping
beyond auto-captured session logs - a decision, a convention, a
gotcha - tell the agent "save a permanent note that we standardised
on Postgres for X" or "annotate this as a project rule" and it callsmemory_write_pageto write a durable, git-versioned wiki page. From
a terminal it'sai-memory write-page --path decisions/0007-db.md --body $'# Standardised on Postgres\n\n...' --pinned.--pinnedexempts it from the decay sweep; the H1 on the first line of--bodybecomes the page title (omit--title— it's still
accepted, but LLM callers trip over JSON-escaping their way through
it, see issue #67). Unlike a handoff (single-use) or an
auto-synthesised session page (rewritten on consolidation), a
write-page note is yours: it shows up inmemory_query, renders in/web, and stays until you change it.
* "That page you found is out of date."The agent callsmemory_feedbackwith the page's path and a signal:helpful/not_helpfultune how strongly retention keeps a sweep-eligible episodic
page (they move its salience, which scales the decay formula's time term),
whilestale/wrongfloor the salienceandmake any current page
show up as afeedback_flaggedfinding in the nextmemory_lintreport.
Feedback never deletes anything — it lowers confidence and flags for review —
and it attaches to the version current when feedback is recorded, so a
later rewrite clears the flag. Retrieved page text is untrusted and never
authorizes feedback by itself.
* "Remember this, but only until the sprint ends."Passexpires_attomemory_write_page(RFC3339 orYYYY-MM-DD= end of
that day, UTC) — or putexpires_at:in a page's frontmatter by
hand. Past the TTL the page disappears from search/recent/briefing
(passinclude_expired: truetomemory_queryto still see it) and
the next forget sweep hard-deletes the file and its rows. A TTL beats
a pin;memory_lintwarns about pinned+expiring combos.
* "This new project has months of history before ai-memory."cd /path/to/my-project && ai-memory bootstrapcollectsgit log, README,docs/, module headers, project rules and
one-shot-summarises them into seed wiki pages. Future sessions
build on top.
* "What durable lesson did that session teach?"When an LLM provider is configured, ai-memory runs a background
auto-improvement scheduler for newly completed sessions in every project. It
records proposed wiki edits in the pending-writes audit trail, then approves
them immediately through the normal wiki write path by default. Scheduler ticks
are non-overlapping: if reviewing all projects takes longer than the interval,
the next tick is delayed until the current one finishes. Scheduling and
approval are separate: set[auto_improve.scheduler] enabled = falseto stop
automatic review, or set[auto_improve] require_approval = trueto keep both
scheduled and manual proposals pending for human review.ai-memory auto-improve --session-id <uuid>and MCPmemory_auto_improveremain
available for manual catch-up or targeted reruns. When itssession_idis
omitted, the MCP tool selects the newest completed session without a
persisted auto-improvement run, so repeated calls advance past short
preflight-skipped sessions; an explicit ID reruns that session.ai-memory auto-improve-report --workspace <w> --project <p>returns a read-only
telemetry report for recent auto-improvement outcomes without staging or
creating proposals; add--stageto create one pending report page for
audit/approval. On deployments that distinguish operators, pending learning
proposals are isolated by qualified operator identity, so one person's
proposal for a page does not block another's; unattributed and single-user
deployments retain the shared pending queue. Seedocs/auto-improve-eval-gates.mdfor
example executable eval scorers.Existing installs do not need per-project migration. The scheduler initializes
a per-project first-run watermark so historical sessions are not reviewed
automatically on upgrade, then records per-session claims so failed scheduled
reviews do not retry forever; use manual auto-improve for old sessions or
failed scheduled sessions you want to catch up. Older configs may still contain
an[auto_improve] mode = ...line; current ai-memory ignores that legacy key,
so you can remove it when convenient.
* "What housekeeping should I consider?"ai-memory curatorruns a no-LLM, rule-based maintenance report over cold
episodic pages, stale slots, duplicate exact normalized titles, and dangling
cross-project links. It is report-only unless--stageis passed; staging
queues one report page for approval and still performs no maintenance actions
itself. Shared servers can opt into[decay] breadth_weightto give pages
reinforced by several identified operators a retention bonus; the default0.0leaves existing retention scores unchanged.
* "Run one ai-memory for the whole household."Stand the server
up on a homelab box at0.0.0.0:49374with a bearer token; every
laptop/desktop talks to it. Per-cwd routing keeps each project's
pages cleanly separated; the/webUI is reachable from a
browser anywhere on the LAN.
* "Audit what landed before sharing with a teammate."Browse
the wiki athttp://<server>:49374/web- HTTP Basic dialog if
auth is on, paste the token as password. Per-project tree view,
rendered markdown, supersession chain visible per page.
* "Undo one bad page edit without rolling back the whole server."ai-memory checkpointsshows recent wiki commits, thenai-memory restore-page --path notes/foo.md --from <rev>restores that one
markdown file and reindexes it into SQLite. Fullbackup/restoreis
still the answer for DB-only state such as sessions, observations, handoffs,
users, audit rows, and embeddings.
* "Drop an experiment, keep the rest."ai-memory purge-project --project experimental --confirm.
Atomic: that project's DB rows cascade away, its wiki subdir getsrm -rf'd, every sibling project is untouched by construction.

## Quick start

### Arch Linux (AUR)

For native Arch installs, use the AUR packages. They install/usr/bin/ai-memory, packaged hook sources, and both system-level and
user-level systemd units.

yay -S ai-memory-bin 
#
 prebuilt Linux x86_64/aarch64 binary

yay -S ai-memory 
#
 builds from source

Single-user workstation:

mkdir -p 
~
/.config/ai-memory 
~
/.local/share/ai-memory
ai-memory --data-dir 
~
/.local/share/ai-memory \
 --config 
~
/.config/ai-memory/config.toml init
systemctl --user 
enable
 --now ai-memory.service
ai-memory install-mcp --client claude-code --apply
ai-memory install-hooks --agent claude-code --apply

System service installs use/var/lib/ai-memoryand/etc/ai-memory/via the
packaged unit. Full user-service, system-service, auth, and provider setup is indocs/install.md#arch-linux-native-packages-aur.

### Docker

You need: Docker + an agent CLI from theSupport Matrix, or
anything else that speaks MCP.

The published Docker image includeslinux/amd64andlinux/arm64variants,
so Apple Silicon Macs and ARM64 Linux hosts can pullakitaonrails/ai-memorywithout--platform linux/amd64emulation.

The default quick-start hasno authentication- the server binds
to loopback only, so on a single-user laptop nothing else can reach
it. Adding a bearer token is a one-line change once you're ready to
expose the server on the LAN; seeSecuritybelow.

#
 1. Install the ai-memory CLI wrapper (a small shell script that

#
 runs the binary inside docker with your $HOME mounted). This is

#
 the only thing that needs to live on the host filesystem.

mkdir -p 
~
/.local/bin
wrapper_tmp=
"
$(
mktemp -d
)
"

trap
 
'
rm -rf "$wrapper_tmp"
'
 EXIT
wrapper_base=https://github.com/akitaonrails/ai-memory/releases/latest/download/ai-memory-wrapper
curl -fsSL 
"
$wrapper_base
"
 -o 
"
$wrapper_tmp
/ai-memory-wrapper
"

curl -fsSL 
"
$wrapper_base
.sha256
"
 -o 
"
$wrapper_tmp
/ai-memory-wrapper.sha256
"

expected=
"
$(
awk 
'
NR == 1 { print $1 }
'
 
"
$wrapper_tmp
/ai-memory-wrapper.sha256
"
)
"

if
 
command
 -v sha256sum 
>
/dev/null 
2>&1
;
 
then

 actual=
"
$(
sha256sum 
"
$wrapper_tmp
/ai-memory-wrapper
"
 
|
 awk 
'
{ print $1 }
'
)
"

else

 actual=
"
$(
shasum -a 256 
"
$wrapper_tmp
/ai-memory-wrapper
"
 
|
 awk 
'
{ print $1 }
'
)
"

fi

[ 
-n
 
"
$expected
"
 ] 
&&
 [ 
"
$actual
"
 
=
 
"
$expected
"
 ] 
||
 { 
echo
 
"
wrapper checksum mismatch
"
 
>&2
;
 
exit
 1
;
 }
install -m 0755 
"
$wrapper_tmp
/ai-memory-wrapper
"
 
~
/.local/bin/ai-memory
rm -rf 
"
$wrapper_tmp
"

trap
 - EXIT

#
 Most distros put ~/.local/bin on PATH automatically. If `which

#
 ai-memory` comes up empty, add this to ~/.bashrc / ~/.zshrc:

#
 export PATH="$HOME/.local/bin:$PATH"

#
 2. Start the server. `--restart unless-stopped` makes it come back

#
 on docker daemon restart and on machine boot (provided your

#
 docker service is enabled at boot — `sudo systemctl enable

#
 docker` on most distros). Loopback-only bind (`127.0.0.1:49374`)

#
 so nothing outside this machine can reach it. Omit the LLM /

#
 EMBEDDING lines for zero-LLM mode — FTS5 search still works

#
 without any keys.

docker run -d --name ai-memory \
 --restart unless-stopped \
 -p 127.0.0.1:49374:49374 \
 -v ai-memory-data:/data \
 -e AI_MEMORY_LLM_PROVIDER=anthropic \
 -e ANTHROPIC_API_KEY=sk-ant-... \
 -e AI_MEMORY_EMBEDDING_PROVIDER=openai \
 -e OPENAI_API_KEY=sk-... \
 akitaonrails/ai-memory:latest

#
 3. Wire your agent CLI in two commands. The wrapper takes care of

#
 mounts and each client's config-path detection. Re-run with

#
 `--agent codex`, `--agent command-code`, `--agent devin`, `--agent opencode`, `--agent gemini-cli`,

#
 `--agent grok`, `--agent kimi-code`, `--agent kiro-cli`, `--agent omp`,

#
 `--agent oh-my-pi`, `--client cursor`,

#
 `--client gemini-cli`, `--client grok`, `--client kiro-cli`, etc.

#
 for additional agents; full list in docs/install.md.

ai-memory install-mcp --client claude-code --apply
ai-memory install-hooks --agent claude-code --apply

#
 Grok Build CLI example:

#
 ai-memory install-mcp --client grok --apply

#
 ai-memory install-hooks --agent grok --apply

#
 Kiro CLI v2 example (requires an existing Kiro agent config):

#
 ai-memory install-mcp --client kiro-cli --apply

#
 ai-memory install-hooks --agent kiro-cli --apply

#
 Kiro CLI v3 example (standalone hook registration):

#
 ai-memory install-hooks --agent kiro-cli-v3 --apply

#
 Command Code stable MCP + lifecycle example:

#
 ai-memory install-mcp --client command-code --apply

#
 ai-memory install-hooks --agent command-code --apply

On Linux/macOS, that's it. Start a Claude Code session as usual - every
prompt and tool call now lands in ai-memory, and the next session you
open in this project will see a handoff with where you left off.
On macOS, the native release binary is also supported and recommended when you
do not need Docker; seedocs/macos.md.

If two Claude Code sessions use the same server concurrently, enable
per-session routing on the server and replace only theai-memoryMCP entry
with the optional bridge:

#
 <ai-memory data dir>/config.toml

[
auto_scope
]

mode
 = 
"
per_session
"

ai-memory install-mcp --client claude-code --session-aware --apply

The bridge still connects to the configured local or remote HTTP server and
forwards its bearer token, but also attaches Claude's lifecycle session id to
every MCP request. Existing static HTTP installs remain the default. Seedocs/auto-scope.mdfor Claude's/clearand
implicit-resume limitations.

Theinstall-mcp/install-hookscommands useAI_MEMORY_SERVER_URL/AI_MEMORY_AUTH_TOKENwhen set; otherwise
they default tohttp://127.0.0.1:49374(matching the server above)
and no bearer token. If hooks are installed after an ai-memory MCP
entry already exists,install-hooksreuses that endpoint so a remote
MCP setup cannot silently regenerate loopback-only hooks. Both commands
are idempotent - re-runs replace ai-memory's entry, preserve every
other server / hook you have configured, and write a timestamped.bak-<ts>next to the file before each modifying write. The hook
scripts are staged into~/.local/share/ai-memory/hooks/<agent>/automatically; re-running overwrites them so future image updates ship
updated hooks. Drop--applyto print the snippet instead of mutating.
For Claude Code,CLAUDE_CONFIG_DIRrelocates MCP registration to$CLAUDE_CONFIG_DIR/.claude.json, hooks to$CLAUDE_CONFIG_DIR/settings.json, and global managed skills to$CLAUDE_CONFIG_DIR/skills. The Docker wrapper forwards this variable when
the directory is under its existing$HOMEbind mount. Use the native binary
when the Claude config root is outside$HOME. Uninstall checks both the
active relocated paths and Claude's home defaults, so enabling the variable
does not leave an older default-path ai-memory installation behind.
If your agent often starts inside repository subdirectories or linked
worktrees, add--project-strategy repo-roottoinstall-hooksso captures
collapse to the main git repo name; seedocs/install.mdanddocs/marker-file.mdfor details. Later bare--applyrefreshes, includingai-memory upgrade, preserve that choice;
pass--project-strategy basenameexplicitly to remove it.

The Docker wrapper also bridges thin-client commands such asai-memory statusandai-memory bootstrapback to the host's
loopback server. With the local Docker quick start above, noAI_MEMORY_SERVER_URLoverride is needed.

Managed workstreams are optional. They execute the harness on the host while
the server may remain local or remote:

ai-memory run claude

#
 later, continue the same workstream in another harness

ai-memory run codex --yolo

#
 omit the name to continue the newest usable local harness session

ai-memory run

#
 or resume the newest managed checkout without changing directories first

ai-memory 
continue

To remove ai-memory later, runai-memory uninstall --applyfrom the
same host environment. It removes ai-memory-owned config entries, instruction
blocks, default-root managed skill files, and generated plugin files only after
matching their ai-memory signatures; custom skill roots installed with--target-dirare cleaned up manually. Use--mcp-urlif you installed MCP
with a custom endpoint, and--mcp-nameonly when you need to narrow removal to
one matching entry.

### Install Notes

* SELinux:on enforcing Linux hosts, the wrapper automatically adds--security-opt label=disableonly to short-lived helper commands that touch
bind-mounted host files. It does not alter the long-lived server container
or relabel$HOME; do not add:z/:Zto the whole home bind. Rootless
engines also get-u 0:0for those commands. Docker and podman report
rootless mode and SELinux support under differentinfokeys; both are
read. The same treatment applies wheneverAI_MEMORY_DATA_DIRselects a
host directory or an explicit--configreads a host file. Seedocs/install.md.
* Windows:use the Linux path inside WSL2, or the native Windows wrapper
from PowerShell/cmd. Local supported profiles default to host-native commands:
Claude Code may use its supportedai-memory.exeexec form, while other
agents use native single command strings matching their hook schema. The
Docker wrapper protects.ps1fallback commands from nested PowerShell
expansion with-EncodedCommand; reruninstall-hooks --agent <agent> --applyafter upgrading so existing hook
entries receive the current form.
PowerShell/Git Bash script bundles are compatibility fallbacks and do not
enforce capture-policy v1. Do not mix path worlds. Seedocs/windows.md.
* Docker compose:docker compose -f docker/docker-compose.yml up -dis supported; agent setup is the same as step 3 above.
* Remote server:setAI_MEMORY_SERVER_URL=http://<server-ip>:49374andAI_MEMORY_AUTH_TOKEN=<token>on the client before installing
MCP/hooks. Explicit--server-urlflags still work, but are no longer
required when the env vars are set. Any non-loopback server should use
bearer auth.
* Managed-launch wrapper:ai-memory run,ai-memory show, andai-memory continuemust be intercepted by the current host wrapper so local
checkouts, native harnesses, and session stores remain accessible. An old
wrapper may pass these commands into Docker and fail to find a checkout or
host executable. Runai-memory upgradeon the agent machine to refresh it. The host-native runner
inheritsAI_MEMORY_SERVER_URL,AI_MEMORY_AUTH_TOKEN, and the hostPATH.
* Upgrades:for Docker-wrapper installs, runai-memory upgradeon each
agent machine. It refreshes the local wrapper, pulls the latest image, and
re-stages hook scripts under~/.local/share/ai-memory/hooks/<agent>/.
Native package/source installs should rerunai-memory install-hooks --agent <agent> --applyafter upgrading the binary.
Remote/homelab servers must still be redeployed separately; local wrapper
upgrade only updates the client machine. Existing project prompt files keep
working. Refresh the managed ai-memory routing package
(ai-memory install-instructions, or--target AGENTS.mdfor AGENTS-based
projects) when you want new tool guidance. The refresh writes the slim
markered snippet and managed Agent Skills from the same binary-owned assets.

For every client in theSupport Matrix, plus curl-based hook
installs, source builds, CLI environment variables, and the full subcommand
reference, seedocs/install.md.

Tab completion for the CLI is available in bash, zsh, fish, PowerShell, and
elvish:

ai-memory completions fish 
>
 
~
/.config/fish/completions/ai-memory.fish

Seedocs/shell-completions.mdfor the other
shells' install paths.

## Security

Loopback-only (127.0.0.1:49374) with no auth is the default because
it is safe for a single-user laptop: no process outside the machine can
reach the server.

Unauthenticated non-loopback HTTP now fails closed. SetAI_MEMORY_AUTH_TOKENor bind loopback;--allow-insecure-no-authis an
intentional, dangerous exception for plain HTTP only. Authentication does not
encrypt bearer tokens: for LAN or remote access, use the readyCaddyorCloudflare Tunneltemplates described in
theHTTPS reverse-proxy guide.

Enable bearer auth when the server is exposed beyond loopback, when
untrusted local processes share the machine, or when the data dir holds
sensitive project history:

TOKEN=
$(
ai-memory generate-auth-token
)

docker run -d --name ai-memory \
 --restart unless-stopped \
 -p 0.0.0.0:49374:49374 \
 -v ai-memory-data:/data \
 -e AI_MEMORY_AUTH_TOKEN=
"
$TOKEN
"
 \
 -e AI_MEMORY_ALLOWED_HOSTS=
"
<server-ip>,localhost,127.0.0.1
"
 \
 akitaonrails/ai-memory:latest

ai-memory install-mcp --client claude-code --apply \
 --server-url 
"
http://<server-ip>:49374/mcp
"
 --auth-token 
"
$TOKEN
"

ai-memory install-hooks --agent claude-code --apply \
 --server-url 
"
http://<server-ip>:49374
"
 --auth-token 
"
$TOKEN
"

Bearer auth protects/mcp,/hook,/handoff,/admin/*, and/web/*. Browser access to/webuses HTTP Basic auth with the token
as the password. When/webis exposed through an HTTPS reverse proxy, setAI_MEMORY_AUTH__SECURE_COOKIE=true; it makes the browser cookie HTTPS-only.
Close or redirect direct HTTP access to that hostname. Non-loopback binds should also setAI_MEMORY_ALLOWED_HOSTSto guard against DNS rebinding.

Busy shared hook servers can also setAI_MEMORY_HOOK_RATE_PER_SEC(tokens per
second per actor/session source) and optionallyAI_MEMORY_HOOK_RATE_BURSTto
bound one runaway session without blocking unrelated hook sources. Unset or0rate leaves the limiter disabled.

For shared servers where each developer should authenticate their own hook
writes, native Claude Code hooks can use a stored OIDC device token instead of
embedding a shared static token:

ai-memory auth login oidc-device \
 --issuer 
"
https://issuer.example.com/realms/team
"
 \
 --client-id 
"
ai-memory-cli
"

ai-memory install-hooks --agent claude-code --apply \
 --server-url 
"
http://<server-ip>:49374
"

OIDC hook auth requires the nativeai-memory hook ...command path. The Docker
wrapper keeps shell-script hooks by default; set up OIDC from a native release
binary or source install. Thin-client HTTP commands such asai-memory statusandai-memory searchalso use the stored OIDC access token when no staticAI_MEMORY_AUTH_TOKEN/[auth].bearer_tokenis configured; the static bearer
still wins when present. This is for OIDC-aware gateways/bridges; native
ai-memory server auth still accepts static root bearer / DB-user tokens, and/admin/*remains root-only unless a gateway translates accepted OIDC auth into
upstream auth that ai-memory accepts.

OIDC/Keycloak session ids are login-provider sessions, not ai-memory agent
sessions. Shared servers that rely on[auto_scope]session isolation still
need explicitworkspace+project/scopes, or a bridge that forwards the
real lifecycle-hook session id on MCP requests.

Want HTTPS?ai-memory deliberately does not terminate TLS itself —
the right answer is a battle-tested reverse proxy in front of it.docs/https-via-proxy.mdis the deployment
guide, with copy-paste docker compose templates indocker/compose.tls.caddy.yml(Caddy
with Let's Encrypt or internal CA) anddocker/compose.tls.cloudflared.yml(Cloudflare Tunnel — no open ports). Both are recommended once you
turn on multi-user or bind beyond loopback. The Quick Start happy
path of single-user on loopback doesn't need TLS — that case is
called out explicitly in the guide so you don't add ceremony where
it doesn't earn its keep.

Multi-user attribution (v0.8, optional).When more than one human
shares a server, ai-memory can attribute each write to a named user.
The bearer token continues to authenticate at the wire level; users
created viaai-memory user addget their own tokens that resolve to
their identity in audit logs, page frontmatter,/api/v1responses, and the
page view UI. Data stays single-tenant — there is no per-page RBAC. A[auth].token_pepperis required for DB-user authentication, but creating the
first user row is what immediately switches every/admin/*endpoint to
root-only, including status/search/read-page and user-management routes.ai-memory initgenerates a pepper for new installs without changing
single-user behavior until a user is added. An SSO gateway can instead use a
dedicated[auth].actor_proxy_bearer_tokenand trustedX-Memory-Actor-*headers; its credential is deliberately separate from the root bearer so a
missing identity cannot become root. Seedocs/users.mdfor the full walkthrough and the
four-rung auth ladder.

Seedocs/deploy.mdfor the full homelab pattern
with bearer auth, host allowlisting, and TLS/reverse-proxy options.

## Using Memory

Day to day, you mostly do not think about ai-memory. Lifecycle hooks
capture prompts, tool calls, compaction checkpoints, and session
boundaries. SessionStart hooks fetch pending handoffs before your first
prompt in the next agent.

Useful entry points:

* Ask "where did we leave off?" to continue from the pending handoff.
* Ask "have we discussed X?" or "search memory for Y" to query the wiki.
* Ask "catch me up" for a prose digest of recent project activity.
* Runai-memory bootstraponce when adopting ai-memory in an existing
project with months of history.
* Start the server with--enable-weband visit/webfor a read-only
browser view of the markdown wiki.--enable-webalso mounts a
read-only JSON frontend API at/api/v1(workspaces, projects, pages,
recent, briefing, search) so custom web UIs can read the memory without
opening SQLite or wiki files directly:GET /api/v1/workspaces
GET /api/v1/projects?workspace=...
GET /api/v1/workspaces/{workspace}/projects/{project}/pages
GET /api/v1/workspaces/{workspace}/projects/{project}/pages/{path}
GET /api/v1/workspaces/{workspace}/projects/{project}/recent?limit=...
GET /api/v1/workspaces/{workspace}/projects/{project}/briefing?limit=...
GET /api/v1/workspaces/{workspace}/overview?limit=...
GET /api/v1/workspaces/{workspace}/projects/{project}/overview?limit=...
GET /api/v1/workspaces/{workspace}/projects/{project}/handoffs?state=...&limit=...
GET /api/v1/search?q=...&workspace=...&project=...&limit=...
POST /api/v1/search { "q": "...", "scopes": [{ "workspace": "...", "project": "..." }] }overviewbundles the open handoff + briefing + memory-health for a workspace
or project in one call (the data a project overview screen needs). The
handoff history defaults to the caller's own plus shared rows; root can useall_owners=truefor recovery across operators.Full integration guide:seedocs/frontend-api.mdfor auth setup, response schemas, error model, limits/pagination,
custom-UI hosting, a workedfetch/curlexample, and the canonical
source-of-truth files. Read that first if you're building a frontend.To serve your own static frontend instead of the built-in UI, point--web-ui-dirat the frontend's build output (same-origin with/api/v1,/mcp,/admin/*, so the existing auth applies):ai-memory serve --transport http --bind 127.0.0.1:49374 \
 --enable-web --web-ui-dir ../ai-memory-ui/distA reference implementation — a SolidJS knowledge browser with
screenshots and e2e tests — lives atdjalmajr/ai-memory-ui.Richer products such as import/migration pipelines and write-capable
browser chat/editors should live as optional companion crates or projects
that call ai-memory's public HTTP/MCP surfaces. The first implemented
companion is the standalone OMC wiki importer atcompanions/ai-memory-importer, which is
intentionally not a root workspace member and is not included in rootcargo test --workspace. Seedocs/companion-crates.mdfor the boundary.When a reverse proxy hosts ai-memory under a URL subpath, set--base-path(orAI_MEMORY_BASE_PATH) so every HTTP surface moves
together. Example:--base-path /wikiserves MCP at/wiki/mcp, hooks at/wiki/hook, the API at/wiki/api/v1, and the default browser at/wiki/web. Set--web-slug /if you want the browser or custom SPA at/wikiitself.

Install the managed routing package once so agents proactively call the
right MCP tool for those prompts:

ai-memory install-instructions

That command writes or updates the slim<!-- ai-memory:start -->block and
the managed ai-memory Agent Skills that carry the detailed routing guidance.
Seedocs/usage.mdfor handoff examples, proactive query
routing, bootstrap details, web UI screenshots, and the raw-wiki inspection
commands. CLI URL/auth configuration lives indocs/install.md.

### Entity retrieval

Consolidation extracts specific technologies, components, services, files, and
domain nouns into each page's canonical frontmatter. Hand-edited wiki pages can
declare the same bounded index explicitly:

---

title
: 
Queue choice

entities
:
 - 
nats jetstream

 - 
delivery guarantees

---

Names are lowercased, whitespace-normalized, de-duplicated, capped at 10 per
page and 64 characters each, and rebuilt from Markdown during a clean-storeai-memory reindex.
Entity lookup is project-scoped, ignores expired pages by default, and reportsentity_rank, its raw inverse-frequencyentity_weight,matched_entities,
and its RRF contribution undermemory_query(..., explain: true).

## LLM Providers

ai-memory runs without an LLM: hooks still capture sessions, search uses
FTS5 + declared entities + graph neighbors, and summaries fall back to
rule-based output. Add an LLM provider
when you want LLM consolidation (on PreCompact, on demand viamemory_consolidate, or opt-in at session end withAI_MEMORY_CONSOLIDATE_ON_SESSION_END), richer linting, and bootstrap.
Substantive session ends always write a rule-based summary page + handoff either
way. A session containing onlySessionStart/SessionEndboundaries is
closed without a page, handoff, or provider job. When that empty session had
accepted startup context, its session-bound handoff is returned to the open
pool for the next receiver instead of being lost.
When the session-end opt-in is enabled, provider work is durably queued after
those deterministic writes and handled by one bounded server worker, so hook
drain latency does not cancel it. Failed jobs retry with backoff and survive a
server restart. A resumed native session is ended again only after its
observation generation advances; the persisted generation watermark makes
duplicate SessionEnd delivery and system clock skew converge without repeated
provider work. The end watermark and automatic handoff commit atomically, and
an interrupted keyed replay finishes the wiki commit, queue insert, and key
completion without duplicating that handoff. On the next SessionStart, the
newest cwd-eligible automatic handoff wins; accepting it expires older eligible
automatic handoffs without consuming manual or sibling-directory work. A new
automatic handoff also expires prior open automatic handoffs from its exact
cwd, so repeated SessionEnds cannot accumulate there before a receiver starts.

To keep consolidation style project-specific, write_prompts/consolidation.mdin that project's wiki. Its body can express
preferences such as "prefer Portuguese titles" or "omit routine CI noise".
Automatic, single-page, and multi-page consolidation use the page; a manualmemory_consolidatecall can passinstructionsto override it once. ai-memory
sanitizes and caps the value at 2,000 characters, JSON-encodes it in the user
message, and treats it as untrusted advisory data. It cannot supply facts,
request tool use or disclosure, or override the consolidation schema and
faithfulness rules. TTL-expired preference pages are ignored. With no active
page or argument, no preference block is appended.

Recommended defaults:

Provider

Default

Use when

anthropic

claude-haiku-4-5

Best default for consolidation quality and rule classification.

anthropic-oauth

claude-sonnet-4-6

Use a Claude Pro/Max subscription via 
claude setup-token
, no API key.

openai

gpt-5.4-mini

Cheaper and faster hosted option.

openai-oauth

gpt-5.5

ChatGPT Pro/Plus/Codex backend via 
ai-memory auth login openai-oauth
; no Platform API key.

copilot

gpt-5.5

GitHub Copilot Chat backend via 
ai-memory auth login copilot
 or 
COPILOT_GITHUB_TOKEN
; requires a Copilot subscription.

gemini

gemini-2.5-flash

Google-hosted option with a generous free tier.

openai-compat

no default

OpenRouter, Atlas Cloud, Ollama, vLLM, LM Studio, and other compatible endpoints.

openai-oauthstores a refresh token in<data_dir>/auth.jsonand talks to
the ChatGPT/Codex Responses backend, notapi.openai.com. For Docker quick
starts, runai-memory auth login openai-oauthwith the wrapper so the token
lands in the sameai-memory-datavolume as the server.

anthropic-oauthhits the same/v1/messagesendpoint asanthropicbut
authenticates with an OAuth bearer token instead of an API key. Runclaude setup-tokenonce, then setAI_MEMORY_LLM_PROVIDER=anthropic-oauthandANTHROPIC_OAUTH_TOKEN=<token>(orCLAUDE_CODE_OAUTH_TOKEN, whichclaude setup-tokenwrites automatically). NoANTHROPIC_API_KEYis needed. The Docker
wrappers forward either token by name to short-lived helper commands such asllm-test; configure the long-lived server container separately as shown in the
installation guide.

For both Anthropic providers, ai-memory omitstemperaturefor Claude
4.7 and later models and Claude Mythos Preview because those models reject
non-default sampling parameters.llm-testsends the same representative 0.2
value as the normal pipeline before the provider applies that compatibility
rule.

⚠️Unofficial and against Anthropic's usage policies — use at your own risk;
it may get your account rate-limited or banned. Seethe warning indocs/install.md.

copilotstores a GitHub user token in the same auth file, exchanges it for a
short-lived Copilot API token via GitHub's/copilot_internal/v2/token, and
uses the Copilot Chat endpoint withvscode-chatintegration headers. You can
also setCOPILOT_GITHUB_TOKEN,GH_TOKEN, orGITHUB_TOKENon the server.

Tip

For the OAuth/subscription backends (anthropic-oauth,openai-oauth,copilot), pick a small, fast modelviaAI_MEMORY_LLM_MODEL— e.g.claude-haiku-4-5orgpt-5-mini. ai-memory's LLM work (consolidation,
lint, explore) is summarisation, not hard reasoning, so a Haiku/mini-class
model is plenty and is much easier on subscription rate limits. Save the
high-effort thinking models for your coding agent.

Tip

OpenAI-compatible structured output is schema-constrained by default.ai-memory sends each operation's JSON Schema throughresponse_format=json_schema, which recent Ollama, vLLM, LM Studio, and
llama.cpp releases honour. It falls back to the tolerant parser when an
endpoint explicitly rejects that field or returns a malformed shape. SetAI_MEMORY_LLM_COMPAT_STRICT=falseonly for an incompatible endpoint.

For small-context local models, configure both consolidation limits. The input
target accounts for the complete rendered prompt, including bounded slot and
current-page context plus the structured-output schema; the output limit is
sent to the provider. Their sum must fit the model context window, with extra
headroom because provider tokenizers differ:

[
consolidation
]

max_input_tokens
 = 
6500

max_output_tokens
 = 
1000

The equivalent environment variables areAI_MEMORY_CONSOLIDATION__MAX_INPUT_TOKENSandAI_MEMORY_CONSOLIDATION__MAX_OUTPUT_TOKENS. Provider failures during an
automatic PreCompact/PostCompaction checkpoint fall back to the deterministic
rule-based page; admission, storage, and scope errors still fail closed. The
validated minimums are 6,000 input and 1,000 output tokens.

Reranking is optional and off by default. With an LLM provider configured,AI_MEMORY_RERANKER=llmmakes project and explicit-scopememory_querycalls over-fetch from the hybrid stage, fuse scopes, and make at most one LLM
call to reorder the best candidates. This can promote a relevant page that
RRF ranked below the requested cut, at the cost of LLM latency and usage. The
request sends the query plus at most 30 bounded page titles and search snippets
to the configured provider; all values are JSON-encoded and treated as
untrusted data. A timeout, provider error, or incomplete/invalid score set
preserves the normal order.global=trueand supplemental global-preference
hits keep their existing non-RRF ranking. Concurrent provider calls are capped
at four; saturated queries keep their local ranking without waiting.

Embeddings are optional and separate from the LLM provider. SetAI_MEMORY_EMBEDDING_PROVIDER=openai,voyage,google/gemini, oropenai-compatwhen you want vector retrieval in addition to FTS5 + entity +
graph-neighbor retrieval.openai-compattargets self-hosted engines
(Ollama, LM Studio, vLLM): it needs no API key and requires explicitAI_MEMORY_EMBEDDING_BASE_URL,AI_MEMORY_EMBEDDING_MODEL, andAI_MEMORY_EMBEDDING_DIM. Both the FTS-only and hybrid paths apply the same
bounded page-authority adjustment after candidate generation; embeddings
improve relevance recall but do not decide which source is canonical.

Seedocs/install.md#llm-provider-tiersfor env vars and Ollama/OpenRouter/Atlas Cloud examples, anddocs/llm-provider-comparison.mdfor the empirical model comparison.

## Architecture

One Rust binary runs an MCP/HTTP server and owns one data directory:

<data_dir>/
├── wiki/ # markdown source of truth, git-versioned
├── raw/ # immutable sanitized managed-workstream transcript segments
├── db/ # SQLite indexes, including FTS5, entities, and embeddings
├── models/ # reserved for local embedding models
└── logs/ # rolling tracing output

Hooks POST observations to the server. The server serializes writes
through one SQLite writer, compiles session observations into markdown
pages, and serves retrieval through FTS5, entity-match and graph-neighbor RRF,
optional vector RRF, bounded source-authority adjustment, and bounded
raw-observation fallback for non-global searches.

Seedocs/ARCHITECTURE.mdfor the data-flow
diagram, crate breakdown, schema notes, and invariants.

## Docs

File

What it is

docs/install.md

Installation cookbook.
 Every agent CLI, every alternative (curl, source build, no-docker, no-auth), and the server-on-a-different-machine (homelab/LAN) walkthrough. Read after the Quick start if your setup doesn't match the happy path.

docs/usage.md

Handoffs, proactive memory queries, slim routing snippet + managed Agent Skills, migration from other memory tools, web UI, raw-wiki inspection, and rules-vs-facts workflow.

docs/managed-workstreams.md

Optional 
ai-memory run
 continuity across Claude Code, Codex, OpenCode, Pi, Crush, Kimi Code, Command Code, Kiro CLI v2/v3, OMP, Grok Build CLI, and Antigravity CLI: automatic harness selection, native resume, argument forwarding, ledger search, privacy, and recovery.

docs/managed-harness-contributions.md

Protocol and acceptance bar for contributors adding managed resume, read-only transcript import, and startup context delivery to another harness.

docs/marker-file.md

.ai-memory.toml
 workspace/project routing for multi-client trees, mono-repos, worktrees, and work/personal separation.

docs/auto-scope.md

[auto_scope]
 modes for shared servers: default single-slot routing, session-aware isolation, and multi-user 
per_actor
 behavior.

docs/macos.md

macOS install paths: native release binary (recommended), source build, the Docker wrapper, hook-platform notes, and current macOS limitations.

docs/windows.md

Windows install modes: full WSL2, native Windows with Docker Desktop, prebuilt native release zip, native source builds, and current hook/MCP harness caveats.

docs/mcp-install.md

Per-client MCP and lifecycle notes, handoff-injection limits, and community bridge guidance.

docs/deploy.md

Homelab deploy: bin/deploy, bearer-token auth, pointers to the TLS guide.

docs/users.md

Multi-user attribution (v0.8).
 Four-rung auth ladder, 
ai-memory user add/list/expire/revive/rotate-token
 walkthrough, backward-compat migration for pre-v0.8 installs, token storage rationale.

docs/https-via-proxy.md

HTTPS via a reverse proxy.
 When you need TLS (multi-user, non-loopback) and when you don't (loopback / stdio). Copy-paste docker compose templates for Caddy + Let's Encrypt, Caddy + internal CA (LAN-only), Cloudflare Tunnel (no open ports), and external cert files; plus native-Caddy + nginx recipes. The "thinking you're secure when you're not" failure modes explicitly called out.

docs/lifecycle-ops.md

Read before running purge / rename / backup / restore / reset / reindex / restore-page.
 Safety matrix for state-touching commands, per-project disk layout (how isolation actually works), checkpoint-based page recovery, and operator workflows for "fresh start", "snapshot before risky op", "drop one project", and rebuilding SQLite from wiki files.

docs/auto-improvement-loop.md

Auto-improvement design notes: Hermes-inspired scheduled review, auto-approval default, manual review opt-in, pending proposal storage, and curator work.

docs/companion-crates.md

Boundary and implementation plan for optional companion projects, including the standalone importer at 
companions/ai-memory-importer
, without widening core ai-memory.

docs/llm-provider-comparison.md

Empirical notes behind the recommended LLM defaults.

docs/ARCHITECTURE.md

Operational summary: data flow, crate layout, cross-cutting invariants, schema.

docs/design-decisions.md

The full v1 spec.

Research docs under 
docs/

Karpathy LLM Wiki notes, Hermes Agent, agentmemory / basic-memory / cognee deep-dives, lessons-learned from upstream issues.

## Influences and prior art

* Karpathy LLM Wiki- the compile-not-retrieve pattern.
* agentmemory- most of the right ideas; this project is the Rust successor.
* basic-memory- the markdown-on-disk source-of-truth model.
* cognee- pipeline composition and triplet embeddings.
* Hermes Agent- the self-improvement loop: post-turn review, approval gates, and curator boundaries.
* A-MEM- Zettelkasten-style atomic notes with link evolution.

## License

MIT - seeLICENSE.

## Acknowledgements

This codebase is being built collaboratively with Claude Code
(Anthropic Claude Opus 4.7) following the plan documented indocs/design-decisions.md.