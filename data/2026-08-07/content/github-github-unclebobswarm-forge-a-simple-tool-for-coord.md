---
title: 'GitHub - unclebob/swarm-forge: A simple tool for coordinating several AI agents. · GitHub'
url: https://github.com/unclebob/swarm-forge
site_name: github
content_file: github-github-unclebobswarm-forge-a-simple-tool-for-coord
fetched_at: '2026-08-07T11:43:58.047316'
original_url: https://github.com/unclebob/swarm-forge
author: unclebob
description: A simple tool for coordinating several AI agents. Contribute to unclebob/swarm-forge development by creating an account on GitHub.
---

unclebob

 

/

swarm-forge

Public

* NotificationsYou must be signed in to change notification settings
* Fork190
* Star1.7k

 
 
 
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

258 Commits
258 Commits
swarmforge
swarmforge
 
 
test/
swarmforge
test/
swarmforge
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
bb.edn
bb.edn
 
 
close-swarm
close-swarm
 
 
View all files

## Repository files navigation

Do not spend any money on a bankrbot SWARM token.

# SwarmForge

A disciplined tmux-based agent orchestration platform that turns swarms of AI agents into reliable, professional software engineers.

## Intent

Thismainbranch is documentary: it explains the system and carries the shared operational scripts and default constitution articles. The runnable workflow branches carry the project-facing configurations, role prompts, and local constitution articles that define specific workflows.

SwarmForge is an agent coordination system that facilitates communication between agents working in different git worktrees.

It provides a shared structure for role-specific prompts, worktree assignment, tmux sessions, and message passing so multiple agents can collaborate on the same project without stepping on each other.

## Branches

The runnable SwarmForge configurations live on dedicated branches. Each branch contains theswarmforge/swarmforge.conf, local constitution articles, and role prompts for one workflow. At startup, its./swarmwrapper copies the shared operational scripts and shared constitution articles frommainwhen they are not already present, then launches that branch's local configuration.

### two-pack

two-packis the quick backend workflow. Use it for small tasks that benefit from fast coding without the overhead of Gherkin and acceptance testing, while still preserving backend refactoring and hardening.

* coderimplements requested behavior with TDD and unit tests.
* cleanerbatches coder handoffs and performs cleanup, CRAP and DRY review, architectural review, encapsulation and separation-of-concerns fixes, and language mutation hardening.

The normal flow iscoder->cleaner->coder. Use this branch when you want a tight implementation/refinement loop without specification, QA, property-test, or acceptance-test roles.

### four-pack

four-packis the compact specification workflow. Use it for moderate projects that require Gherkin specification and some architectural consideration without splitting every quality gate into its own agent:

* specifierturns user intent into precise Gherkin acceptance specifications and asks for approval before handoff.
* coderimplements approved behavior slices with TDD, unit tests, and generated acceptance tests.
* refactorerperforms behavior-preserving cleanup, coverage improvement, CRAP and DRY review, mutation-site scans, and property-test support.
* architectowns high-level structure, dependency direction, mutation hardening, DRY review, soft Gherkin mutation, and final completion notification.

The normal flow isspecifier->coder->refactorer->architect->specifier. Use this branch when you want disciplined development without splitting cleanup, architecture, hardening, and QA into separate agents.

### six-pack

six-packis the full workflow. Use it for major projects that require full specification, up-front QA, backend verification, and significant architectural consideration. It separates each major quality gate into its own role:

* specifierturns user intent into accepted Gherkin specifications and end-to-end QA procedures.
* coderimplements approved behavior slices with TDD, unit tests, and generated acceptance tests.
* cleanerperforms local behavior-preserving cleanup, coverage improvement, CRAP and DRY review, and mutation-site scans.
* architectreviews module structure, boundaries, dependency direction, and property-test coverage.
* hardenderperforms mutation hardening, language mutation, CRAP and DRY verification, and soft Gherkin mutation.
* QAconverts the specifier's QA procedures into executable scripts, runs final user-interface verification, checks handoff consistency, and sends completion notifications.

The normal flow isspecifier->coder->cleaner->architect->hardender->QA-> completion. Use this branch when you want each review and verification concern owned by a separate agent.

## Prerequisites

SwarmForge runs locally. Before starting a runnable branch, make sure the target machine has:

* zsh
* git
* tmux
* Babashka (bb)
* At least one configured agent backend, such ascodex,claude,copilot, orgrok

## Getting Started

In the directory where you want to use SwarmForge, choose a runnable branch and pull its contents without creating a Git remote:

BRANCH=four-pack
curl -L 
"
https://github.com/unclebob/swarm-forge/archive/refs/heads/
${BRANCH}
.tar.gz
"
 
|
 tar -xz --strip-components=1

UseBRANCH=two-packfor the quick two-agent workflow,BRANCH=four-packfor the compact specification workflow, orBRANCH=six-packfor the full six-agent workflow. Do not usemainfor this command;mainis documentary and stores the shared operational scripts, while the runnable branches provide the configurations and prompts intended for projects.

After copying a runnable branch, start the swarm from the target project:

./swarm

The./swarmwrapper keeps the runnable branch small. On first use, ifswarmforge/scripts/is missing, it downloads themainbranch archive, copies the shared operational scripts fromswarmforge/scripts/, stages shared constitution articles fromswarmforge/constitution/articles/, and then launchesswarmforge/scripts/swarmforge.sh. Later runs reuse the existing local scripts directory instead of overwriting it.

The windows should open automatically.

To stop the swarm, close the first window listed inswarmforge/swarmforge.conf. That cleanup window shuts down the tmux sessions and closes the remaining tracked windows.

While a swarm is active, SwarmForge tries to prevent the host from sleeping. On macOS it usescaffeinate; on Linux it usessystemd-inhibitwhen available. Display lock or manual sleep can still interrupt agents depending on the OS. SetSWARMFORGE_PREVENT_SLEEP=0before./swarmto disable this behavior.

## What SwarmForge Does

SwarmForge is a lightweight, tmux-based orchestration layer that:

* Launches aconfig-driven swarmfrom a project-localswarmforge/swarmforge.conf
* Creates one tmux session per configured role and opens a terminal surface for each role when the selected backend supports it
* Reads behavior from project-localswarmforge/roles/<role>.promptfiles plus a layeredswarmforge/constitution.prompt
* Supports per-role backends such asclaude,codex,copilot, orgrok
* Puts the sharedswarmforge/scripts/directory on each agent'sPATH, including handoff helpers for active swarm communication
* Creates git worktrees under.worktrees/for roles assigned to dedicated worktree names
* Initializes a git repository in a new working directory when needed
* Keeps all swarm state local to the working directory in.swarmforge/

## Core Features

* Config-Driven Topology— The swarm shape comes fromswarmforge/swarmforge.conf, not hardcoded shell variables.
* Project-Local Roles— Each role is defined byswarmforge/roles/<role>.promptin the working tree being orchestrated.
* Layered Constitution—swarmforge/constitution.promptdirects agents to read article files underswarmforge/constitution/articles/.
* Backend Selection Per Role— A role can launchclaude,codex,copilot, orgrok.
* Observable Swarm— Open one Terminal window per role and watch the sessions in real time.
* Self-Hosted & Lightweight— Runs locally in tmux and Terminal with minimal machinery.

## Constitution Structure

Each runnable branch contains aswarmforge/directory with this general layout:

swarmforge/
 swarmforge.conf
 constitution.prompt
 constitution/
 articles/
 project.prompt
 local-engineering.prompt
 local-workflow.prompt
 ...
 roles/
 <role>.prompt
 ...

constitution.promptis the entry point. Runnable branches normally use it to tell agents to read every file inswarmforge/constitution/articles/.

Shared default articles live onmainunder:

swarmforge/constitution/articles/
 engineering.prompt
 handoffs.prompt
 workflow.prompt

At startup, SwarmForge installs missing shared articles into the runnable branch'sswarmforge/constitution/articles/directory before creating role worktrees. It also installs missing shared articles into each role worktree during script synchronization. Existing local files are skipped, so a runnable branch can override a shared article by committing an article with the same filename.

Pack-specific additions and exceptions should use explicit local filenames rather than editing shared articles. Current conventions are:

* project.promptfor the workflow's project shape and local topology.
* local-engineering.promptfor workflow-specific engineering rules.
* local-workflow.promptfor workflow-specific flow rules.

Thelocal-*.promptnaming convention means "add to or specialize the shared default article for this runnable branch." Use it when the shared article remains valid and the branch only needs extra requirements, exceptions, or narrower instructions. Do not uselocal-*.promptfor a full replacement; use the shared filename instead when the branch intentionally overrides the shared article.

For example,maincan provide a sharedworkflow.prompt, whilesix-packcan addlocal-workflow.promptfor QA-specific handoff behavior. If a branch needs to replace the shared workflow article completely, it can commit its ownworkflow.prompt; startup will treat that local file as an override and will not copy the shared one over it.

## Roles

Each role inswarmforge/swarmforge.confmaps to a correspondingswarmforge/roles/<role>.promptfile.

## How It Works

In a runnable branch:

1. SwarmForge readsswarmforge/swarmforge.conf.
2. The root./swarmwrapper copies shared helper scripts, terminal adapters, and shared constitution articles from themainbranch when they are not already present.
3. Startup installs missing shared constitution articles intoswarmforge/constitution/articles/, skipping any local article file that already exists.
4. Startup validates the configured role prompts, helper scripts, and terminal adapters.
5. If the target directory is not already a git repository, startup initializes one and creates the first commit.
6. Startup creates one git worktree per configured role under.worktrees/, unless the role is assigned tomasterornone.
7. Startup syncsswarmforge/scripts/and missing shared constitution articles into each role worktree and puts that local scripts directory on each agent'sPATH, so agents use local handoff helpers without reaching back into the master checkout.
8. SwarmForge creates tmux sessions, opens terminal windows, and launches each configured backend in its assigned worktree.
9. Startup starts an OS-specific sleep inhibitor when one is available, and cleanup stops it with the swarm.
10. Roles communicate through daemon-delivered handoff files. Agents create validated drafts withswarm_handoff.sh, accept work withready_for_next.sh, and complete work withdone_with_current.sh.

## Handoff Protocol

Startup syncs the shared helper scripts into every role worktree underswarmforge/scripts/and puts that local directory on the agent'sPATH. Agents do not send tmux messages directly. The launcher startshandoffd.bb, which owns tmux socket access, watches each agent outbox, copies validated handoff files into recipient inboxes, and sends only generic wake-up notifications.

Agents interact with handoffs through three helper scripts:

* swarm_handoff.sh <draft-file>validates and queues outbound handoffs.
* ready_for_next.shaccepts work using the role's configured receive mode.
* done_with_current.shcompletes the current task or batch using the role's configured receive mode.

Outbound drafts use one of two message types. A git handoff points the recipient at a committed state. The commit abbreviation must be exactly 10 hexadecimal characters;swarm_handoff.shvalidates that it resolves to a single commit and canonicalizes it before queuing the handoff.

type: git_handoff
to: <role>[,<role>...]
priority: NN
task: <short-stable-task-name>
commit: <10-character-commit-abbrev>

A note is one short freeform message:

type: note
to: <role>[,<role>...]
priority: NN
message: <one line, max 80 chars>

The helper generates the delivered payload. Agents do not write long handoff bodies, branch names, queue filenames, or tmux commands.

Recipient agents runready_for_next.shwhen notified or after restart. It dispatches to the task or batch helper configured for that role. If it printsNO_TASK, they stop waiting for work. If it printsTASK: <path>, they treat the printedTASK_NAMEandPAYLOADas the task. If it printsBATCH: <path>, they process the printedBATCH_ITEMentries in helper-delivered order. If a wake-up arrives while an agent is already working, it can ignore the wake-up;done_with_current.shchecks for the next task or batch after completing the current work.

The durable handoff files and lifecycle headers replace the old logbook and resend queue. Runtime handoff state lives under.swarmforge/handoffs/in each worktree, withoutbox,sent,failed, andinboxsubdirectories. Agents should not hand-edit, merge, stage, or commit handoff runtime state. Seeswarmforge/handoff-protocol.mdfor the full protocol.

## Theswarmforge.confFile

swarmforge/swarmforge.confdefines the swarm window-by-window. Each line has this form:

window <role> <agent> <worktree> [task|batch] [extra-cli-args...]

The optional receive mode defaults totask. Usebatchfor roles that should consume all currently queued equal-priority handoffs as one batch.

Any fields after the receive mode are passed directly to the agent CLI as additional arguments. If you omit the receive mode, extra arguments may start at the fifth field:

window coder copilot wt-coder --yolo
window architect claude wt-arch task --dangerously-skip-permissions

You can define as many windows as your project needs. Eachrolemaps to a corresponding prompt file atswarmforge/roles/<role>.prompt, so a config containingarchitect,coder,reviewer,research, andreleasewindows would expect:

* swarmforge/roles/architect.prompt
* swarmforge/roles/coder.prompt
* swarmforge/roles/reviewer.prompt
* swarmforge/roles/research.prompt
* swarmforge/roles/release.prompt

This lets each project choose its own swarm shape instead of being locked to a fixed set of roles.

Example config:

window coordinator codex master
window coder codex coder
window refactorer codex refactorer
window architect codex architect

In the example above, the agents run in these worktrees:

* coordinator-> main working directory onmaster, and is the cleanup window because it is listed first
* coder->.worktrees/coder
* refactorer->.worktrees/refactorer
* architect->.worktrees/architect

If a window usesmasteras its worktree name, SwarmForge does not create.worktrees/master; that role runs in the main working directory on themasterbranch.

## tmux Behavior

SwarmForge uses a project-specific tmux socket recorded in.swarmforge/tmux-socket, so each project swarm is isolated from other tmux sessions. It also honors tmuxbase-indexandpane-base-indexsettings when launching agents and sending notifications, so configurations that number windows or panes from1work without requiring users to change their tmux preferences.

## Terminal Behavior

SwarmForge opens trackable terminal windows or tabs through a small terminal backend adapter.

Default detection:

* If AppleScript is available, SwarmForge opens macOS Terminal.app windows.
* Otherwise, ifwt.exeis available, SwarmForge opens Windows Terminal windows.
* Otherwise, SwarmForge attaches the cleanup tmux session in the current shell.

After copying a runnable branch, setSWARMFORGE_TERMINALto override detection:

SWARMFORGE_TERMINAL=ghostty ./swarm
SWARMFORGE_TERMINAL=terminal-app ./swarm
SWARMFORGE_TERMINAL=windows-terminal ./swarm
SWARMFORGE_TERMINAL=none ./swarm

Useghosttywhen you want SwarmForge to open Ghostty tabs instead of the default Terminal.app windows. Usewindows-terminalwhen you want SwarmForge to open Windows Terminal windows from WSL. Usenonewhen you want SwarmForge to skip terminal automation and attach the cleanup tmux session in the current shell.

### Adding A Terminal Backend

The shared terminal backends are carried onmainunderswarmforge/scripts/terminal-adapters/. Runnable branches copy those scripts at startup. To add a new backend, updatemainby creating one file named after the backend:

swarmforge/scripts/terminal-adapters/wezterm.sh

The file must define this small contract:

terminal_backend_label
() {
 
echo
 
"
WezTerm
"

}

terminal_backend_can_open_sessions
() {
 
return
 0
}

terminal_backend_tracks_windows
() {
 
return
 0
}

terminal_open_session
() {
 
local
 session=
"
$1
"

 
local
 title=
"
$2
"

 
local
 sibling_id=
"
${3
:-
}
"

 
#
 Open a terminal surface that runs:

 
#
 cd "$WORKING_DIR" && exec tmux -S "$TMUX_SOCKET" attach-session -t "$session"

 
#

 
#
 Print a stable window/tab id to stdout.

}

terminal_window_exists
() {
 
local
 window_id=
"
$1
"

 
#
 Return 0 if the id from terminal_open_session still exists.

 
#
 Return nonzero otherwise.

}

terminal_close_window
() {
 
local
 window_id=
"
$1
"

 
#
 Close the id from terminal_open_session.

}

If the terminal can open sessions but cannot return stable ids for open/check/close, keepterminal_backend_can_open_sessionsasreturn 0and setterminal_backend_tracks_windowstoreturn 1. SwarmForge will open one surface per session and skip the watchdog for that backend.swarmforge/scripts/terminal-adapters/windows-terminal.shis an example of this launch-only style.

If the backend cannot open sessions at all, set both capability functions toreturn 1; SwarmForge will attach the cleanup tmux session in the current shell. Only editswarmforge/scripts/swarm-terminal-adapter.shwhen adding aliases or changing default auto-detection.

## Window Behavior

Each visible agent window is attached to a tmux session. That means terminal selection, copy, and paste may follow tmux and terminal-emulator rules rather than ordinary text-field behavior. If copy or paste feels unusual, check whether tmux copy mode is active before assuming the agent is stuck.

The first window inswarmforge.confis the cleanup window. Closing that top configured window is the intentional shutdown path: SwarmForge tears down the tmux sessions, closes the remaining tracked windows, and shuts down the swarm.

Closing any other tracked window is non-destructive. The watchdog reopens that window and attaches it back to the same tmux session, so the agent state and terminal history remain intact. This is often the simplest way to recover a window that has landed in an unfamiliar tmux mode or otherwise feels stuck.