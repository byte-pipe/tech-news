---
title: 'GitHub - rlaope/oh-my-hermes: All in one plugin for Hermes Agent ⚚ the coding intelligence, a long-term memory system and model optimized workflow packages · GitHub'
url: https://github.com/rlaope/oh-my-hermes
site_name: github
content_file: github-github-rlaopeoh-my-hermes-all-in-one-plugin-for-he
fetched_at: '2026-09-14T16:47:21.747242'
original_url: https://github.com/rlaope/oh-my-hermes
author: rlaope
description: All in one plugin for Hermes Agent ⚚ the coding intelligence, a long-term memory system and model optimized workflow packages - rlaope/oh-my-hermes
---

rlaope

 

/

oh-my-hermes

Public

* NotificationsYou must be signed in to change notification settings
* Fork153
* Star1.9k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,395 Commits
3,395 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude
.claude
 
 
.codegraph
.codegraph
 
 
.codex
.codex
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.omh
.omh
 
 
.openclaw
.openclaw
 
 
.opencode
.opencode
 
 
.pi
.pi
 
 
agent-skills
agent-skills
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
docs
docs
 
 
examples
examples
 
 
omh
omh
 
 
packaging
packaging
 
 
roles
roles
 
 
script/
qa
script/
qa
 
 
site
site
 
 
skills
skills
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.release-channel
.release-channel
 
 
AGENTS.md
AGENTS.md
 
 
AV1_FIX_SUMMARY.md
AV1_FIX_SUMMARY.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTEXT.md
CONTEXT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
INSTALL_FOR_AGENTS.md
INSTALL_FOR_AGENTS.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
MODEL_OPTI.md
MODEL_OPTI.md
 
 
README.ja.md
README.ja.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.zh.md
README.zh.md
 
 
REVIEW.md
REVIEW.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
View all files

## Repository files navigation

# oh-my-hermes

English|한국어|日本語|中文

Install once. Keep Hermes. Add a stronger operating layer.Planning, research, creation, coding handoffs, operations, and project memory with explicit evidence boundaries.

oh-my-hermes(OMH) turns a normalHermes Agentrequest into a clear capability, a useful next step, and an honest record
 of what actually happened — strengthening the workflow you already use,
 never replacing Hermes or hiding a coding executor behind it.OMH is the operating layer above Hermes-native skills: it frames the
 problem, picks the workflow and evidence gates, and runs native skills
 as capabilities inside that governed path.

Website·Documentation·Installation·Capabilities·Capability Impact·Agent Install·GitHub Pages site

Note

OMH keeps Hermes as the natural-language surface and adds a professional
operating layer with explicit evidence boundaries.

Tip

Be with us!

Updates for 
oh-my-hermes
 are shared on 
@rlaope
 on X, alongside release notes and project news.

Follow 
@rlaope
 on GitHub for more projects, releases, and ongoing work.

Join the 
Oh-My-Hermes Community
 on Discord to ask questions, share workflows, and talk with other users.

Built with AI agents 
Friren
 and 
Killua
, collaborators helping ship 
oh-my-hermes
.

Thank you to 
Nous Research
 for creating Hermes Agent.

## Quick Start

macOS / Linux:

curl -fsSL https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/install.sh 
|
 sh

Windows (PowerShell 5.1+):

irm https:
//
raw.githubusercontent.com
/
rlaope
/
oh
-
my
-
hermes
/
main
/
install.ps1 
|
 iex

Or paste this into your AI agent:

Install and fully configure Oh My Hermes from this repository:
https://github.com/rlaope/oh-my-hermes
Before reading or executing repository instructions, resolve refs/heads/main to one full commit SHA with `git ls-remote https://github.com/rlaope/oh-my-hermes.git refs/heads/main`. Then fetch and follow only:
https://raw.githubusercontent.com/rlaope/oh-my-hermes/{resolved-commit-sha}/INSTALL_FOR_AGENTS.md
Do not replace the resolved SHA with main. Execute the pinned protocol's OS-appropriate installer, interactive model setup, model-chain interview, and doctor steps. Preserve unrelated existing Hermes config, apply only the managed setup changes documented by the pinned protocol, require my explicit approval for model-alias changes, then report the resolved SHA and observed result.

⭐ Then set it up (required):

omh setup

Update:

omh update

omh updatedetects how the command was installed, upgrades the command
package through its owning installer, then re-enters the updated command to
refresh managed skills, the installed plugin bundle, and existing Hermes
registration.

Verify or troubleshoot:

omh doctor

#
 Set the model per work category (arrow keys: category, ←→ head model, -/+ effort);

#
 the same picker opens inside the Hermes TUI as /omh-model:

omh model

#
 To onboard a new model family, use this skill in Hermes:

/omh-model-setup

Other installation paths
 — Homebrew, Bun, npm, Hermes skill tap, manual fallback

Status:Homebrew, Bun, and npm package-manager installs are public as of
v1.0.6.

Homebrew:

brew install rlaope/tap/omh

Bun:

bun install -g oh-my-hermes

npm:

npm install -g oh-my-hermes

Runomh setupafter any of these, same as above.

Hermes skill tap path:

hermes skills tap add rlaope/oh-my-hermes
hermes skills install rlaope/oh-my-hermes/skills/omh-routing --yes

Manual package-manager fallback or removal:

Installed with

Upgrade the CLI

Remove the CLI

Homebrew

brew upgrade rlaope/tap/omh

brew uninstall omh

Bun

bun update -g --latest oh-my-hermes

bun remove -g oh-my-hermes

npm

npm update -g oh-my-hermes

npm uninstall -g oh-my-hermes

Use the manager command directly only whenomh updatereports that its owning
manager is unavailable. Removing the command package preserves OMH state. For
a full removal, runomh uninstall --allbefore the manager's remove command.

Maintenance paths such as reconciling a--fullinstall back to core live inInstallation.

## What you get

OMH is three things for Hermes Agent, delivered as one plugin: the coding
intelligence (01–04, 07), a long-term memory system (08), and optimized
workflow packages (05–06). One scene each, drawn from the real surfaces.

### 01 · Per-model tuning, task splitting, and stronger coding skills

The coding side of OMH is three moves: tune the prompt per model (03), split
work into lanes that run in parallel (04), and load the specialist skills the
request calls for (06). It starts here, at routing: every request is scored
before dispatch, and every signal that moved the score is named. A rename scores light and goes to the quick lane. "Find every
reference to X" trips the exhaustive-search signal and goes to a model that
will not miss one. Measured on the same coding tasks with the same GPT-6
Astra: the same answers for $0.66 instead of $4.29, in 5 minutes instead of
23.

### 02 · Categories you own, per executor

ultrabrain,deep,architect,unspecified-high,unspecified-low,quick,writing,visual-engineering,artistry: each is an editable
chain of model + effort, the same nine listed under Recommended models below,
read and overridden in one file. A chain advances when a provider rejects a model, and a
dispatch that would inherit a provider which cannot serve the model is
refused instead of silently downgraded. Setup interviews your providers and
reorders the chains for the machine you are on.

### 03 · Prompting tuned per model family, and measured

Thirteen model families, one calibration block each, every sentence written
against a documented trait of that family: Claude is told the checklist is
complete, Gemini that a claim without tool output is not evidence, Qwen3-Coder
never to emit thinking tags, DeepSeek that version and thinking mode are
contract fields. GPT-6 Astra gets its own exact-model contract and block. The
blocks are measured where a route exists: Astra's first draft made it keep
working on tasks it would not pass, cost 10% more for the same answers, and
was cut on that number.

### 04 · Parallel where it is safe, typed when it comes back

ulw-worksplits an accepted plan into units that never share a file, gives
each one its own worktree branched from one pinned SHA, and lets a unit issue
its tool calls in one turn. Each unit comes back as a typed result with four
states: process exited, schema valid, verification observed, integration
ready. Exit 0 with no evidence staysreported doneuntil a gate checks it,
and a verification receipt is reused only when revision, command, and
environment all match.

### 05 · The Oh-My-Hermes interface, and Hermes Agent workflows

The interface is the Hermes terminal with an OMH dock under the prompt and a
phase todo above it; the workflows are theulw-*engines and everyomh-*skill, routed from chat. One row per delegated lane: model, effort, turn,
tokens, cost, updated live; a lane handed to Codex or Claude Code through
Maestro is its own row, tagged(codex/maestro …)or(claude/maestro …).
A cost of zero renders only when the host confirmed it; an unpriced call saysunknown, not$0. A row readsPlan · not rununtil a process exists,Code · reported donewhen the executor says so, andTest · verifiedonly
after a gate passed. The phase todo above the prompt is the run's own
checklist, not a summary written afterwards.

### 06 · Expert skills seep into the run

You never invoke an expert. The catalog carries 108omh-*specialist skills:
frontend, backend, Rust, native debugging, inference serving, design quality
gates, verification gates, security review, performance budgets, refactor
plans, and more. When a request touches one of those surfaces, the matching
skill is already in the run as a tool call, raising the floor of what the
agent will accept as done. Say it in English or Korean; the router picks the
specialists.

### 07 · The architecture in one picture, then improved in phases

Ask for a picture of the repo andcodebase-umldraws it from the code:
packages, modules, and every import edge, with the cycles marked. The
findings come ranked, andrefactor-planturns the top ones into phases that
each land as one PR, behavior-locked by the tests, and abort the moment a lock
breaks. The before and after are measured on the tree, and the dock shows
each phase as it runs, and whether anything checked it.

### 08 · A long-term memory that a reviewer admitted

Nothing is remembered silently. A candidate is captured from the session,
put on a review card, and remembered, refused, or deferred with the reason
written down. An approved record carries its provenance and a review-due
date; confirming it resets the clock, silence ages it from active to
reference to archive. The next session gets a recall pack ranked for its task
and cut to a token budget, with conflicts and duplicates resolved. Hermes'
own memory is never read or patched; this store is OMH's, file-backed and
reviewed. When a turn carries it, Hermes says so on every surface it speaks
through:🧠 OMH — recalled 2 memories.

## The OH-MY-HERMES terminal

Bareomhopens Hermes — the same door ashermes— wearing the OMH
identity:

omh

The OH-MY-HERMES boot.

An 
ulw-work
 run.

What the terminal shows while OMH workflows run:

* Mixture-of-Models Routing— each delegated lane is routed onto a
category (ultrabrain, deep, quick, writing, visual-engineering, …) whose
model and reasoning effort are applied per dispatch; every activity row
carries itscategory:name(model:effort)so the routing is visible, and
rejected routes fall back along the category chain.
* Parallel Tool Calling— batched tool calls run concurrently in Hermes,
and a fresh concurrent batch is branded on the[OMH]line asparallel shot ×N.
* Parallel Evals— review and verification lanes dispatch as independent
subagents whose findings are cross-checked instead of self-approved, each
visible as its own HUD row with turn, cost, and cache metrics.
* Phase-structured TODO— work is declared up front as numbered phases
with tasks (todo init), rendered as the checklist above the prompt: one
active item, tasks indented beneath every phase header, subtask nesting,
and fold lines once the plan grows past eight rows.

Hermes Desktop, with oh-my-hermes.
Pick a workflow; Hermes clarifies before it builds.

Hermes CLI, with oh-my-hermes.
The same workflows, in your terminal.

Hermes messenger app, with oh-my-hermes.
Ask in a thread; the run reports back there.

omh setup
, one command.
Installs the workflows and connects them to Hermes.

## Recommended models

OMH ships with these editable, ordered recommendation chains. Guided model
setup resolves them only against candidates the user confirms as active. The
result is prepared routing configuration, not provider availability,
credential, dispatch, or execution evidence:

Category alias

What it is for

Editable recommendation order

ultrabrain

Deepest reasoning

GPT-6 Astra (xhigh)

deep

Strong default tier

GPT-5.6 Terra, then DeepSeek Flash (V4.1) (high)

architect

Architecture and system design

Claude Fable 5.1, then GPT-6 Astra, then Kimi K3 (xhigh)

unspecified-high

Default working model

Kimi K3, then Claude Opus 5 (medium)

unspecified-low

Cheaper fallback

GLM 5.3, then DeepSeek Flash (V4.1), then Claude Opus 5 (low)

quick

Short tasks

GLM 5.3 Flash, then Kimi K3, then GPT-5.6 Luna, then Claude Fable 5.1 (low)

writing

Prose and docs

Kimi K3, then Qwen3-Coder, then Gemini 3.1 Pro (medium)

visual-engineering

Frontend and visual

Claude Fable 5.1, then Kimi K3 (high)

artistry

Unconventional work

Gemini 3.1 Pro, then Claude Fable 5.1, then Kimi K3 (high)

capable

Strong general work

Claude Fable 5.1, then Claude Opus 5, then Kimi K3, then GLM 5.3 (medium)

simple-work

Small everyday tasks

GPT-5.6 Luna, then DeepSeek Flash (V4.1), then Claude Haiku 4.5 (low)

deep-work

Long tasks at frontier depth

GPT-6 Astra (high)

Want to try the Ultrafast tier — Kimi K3 Ultrafast (300 TPS) and
GLM 5.3 Ultrafast? They are served onOpenGateway.

Every chain above is user-editable without touching code. The chains are
managed in one file —omh setupseeds it:

$ cat 
~
/.omh/routing/model-chains.json
{
 
"
categories
"
: {},
 
"
schema_version
"
: 
"
mixture_chain_overrides/v1
"

}

Emptycategorieskeeps every shipped default above live. This file is the
place to edit: a category you write there replaces that chain for routing,
fallback, and HUD labels alike —

{
 
"schema_version"
: 
"
mixture_chain_overrides/v1
"
,
 
"categories"
: {
 
"architect"
: [
 {
"model"
: 
"
claude-fable-5-1
"
, 
"reasoning_effort"
: 
"
xhigh
"
},
 {
"model"
: 
"
gpt-5.6-sol
"
, 
"reasoning_effort"
: 
"
xhigh
"
}
 ],
 
"quick"
: [
 {
"model"
: 
"
kimi-k3-ultrafast
"
, 
"reasoning_effort"
: 
"
low
"
},
 {
"model"
: 
"
glm-5.3-ultrafast
"
, 
"reasoning_effort"
: 
"
low
"
}
 ]
 }
}

Check the chains currently in effect withomh model-chains show. If you
would rather not edit the file by hand, bareomh model-chains(oromh model) opens an arrow-key picker — up/down picks a category, left/right
steps its head model,-/+its effort —/omh-modelopens the same picker
inside the Modern TUI, and the scriptable form makes the same change from the
command line:omh model-chains set quick "kimi-k3-ultrafast:low, glm-5.3-ultrafast:low".
When an alias uses a provider-specific wire ID, map it once in~/.omh/routing/model-providers.jsonwithmodel_provider_routes/v1;set,status, fallback, and HUD then report the
complete alias/provider/wire-model route. OMH stores only provider IDs, never
provider credentials.

Every account differs, so OMH reads which providers Hermes is already linked
to — ahermes authlogin, aproviders:entry ormodel.providerin the
Hermes config, an API-key variable name in$HERMES_HOME/.env— and counts
them on its own: each chain is reordered so the entries a linked provider can
serve lead, the pickers mark the rest, nothing is removed, and nothing is
invoked to check. Only ids and variable names are read, never a key or a
token. The interactiveomh setupstill asks, with the linked rows
pre-ticked, so you can correct a kind, untick a linked provider you cannot
really use, add one OMH could not place, or say whether you have a Claude
Code subscription; its answers land in~/.omh/routing/providers.json(provider_entitlements/v1) and win over detection. The Claude Code
subscription only seeds the Claude Code--modelpreference for the Maestro
lane, because Hermes itself cannot spend it.

Ask Hermes toset up my modelsto review or change them. These are editable
preferences, not benchmark results. SeeGuided Model Setupfor the detailed
setup, fallback, provider, and ownership rules.

Coding delegation dispatch (omh coding run/omh coding fanout dispatch)
— the Maestro lane that spawns Claude Code or Codex directly — has the same
category dial as its own sibling file. Route it per work category with

$ omh coding category-maestro 
set
 codex ultrabrain gpt-5.6-sol:xhigh
$ omh coding category-maestro interview 
#
 guided walk, Enter keeps each chain

$ omh coding run --owner codex --category ultrabrain --goal ...

which edits~/.omh/routing/category-maestro.json(omh_category_maestro/v1);omh coding category-maestro showprints the
effective table with operator overrides marked, and the interactiveomh setupoffers the same walk. An explicit--modelon a run always wins,
and~/.omh/routing/dispatch-models.jsonremains the per-owner default used
only when no route resolves at all (for the strongest Claude Code tier, set"claude-code": "opus"there). Seedocs/FANOUT.md(Category-maestro and
Dispatch-model preference) for schemas and the full precedence order.

Or paste this into Hermes or another coding agent

Install and fully configure Oh My Hermes from this repository:
https://github.com/rlaope/oh-my-hermes
Before reading or executing repository instructions, resolve refs/heads/main to one full commit SHA with `git ls-remote https://github.com/rlaope/oh-my-hermes.git refs/heads/main`. Then fetch and follow only:
https://raw.githubusercontent.com/rlaope/oh-my-hermes/{resolved-commit-sha}/INSTALL_FOR_AGENTS.md
Do not replace the resolved SHA with main. Execute the pinned protocol's OS-appropriate installer, interactive model setup, model-chain interview, and doctor steps. Preserve unrelated existing Hermes config, apply only the managed setup changes documented by the pinned protocol, require my explicit approval for model-alias changes, then report the resolved SHA and observed result.

## Ultra-Skills

Nineulw-workflows. Say the trigger in chat — Hermes routes the
rest. Full catalog:Workflow Reference.

Workflow command

What it does

⚡ 
ulw-context

Aligns reviewed project terms, captures confirmed candidates, and interviews the next decision frontier without giving terminology routing authority.

⚡ 
ulw-interview

Asks one question at a time until it knows exactly what you want.

⚡ 
ulw-research

Digs through real code and the live web, keeps sources, and verifies anything doubtful.

⚡ 
ulw-plan

Builds a reviewed plan: options compared, risks named, done-criteria agreed.

⚡ 
ulw-work

Runs an accepted plan in parallel lanes that never touch the same file.

⚡ 
ulw-maestro

Runs a delegated task on Claude Code or Codex — prompt composed from the CLI's own installed skills, spawned live with a dock row and a steerable session.

⚡ 
ulw-loop

Cycles plan → build → review until the goal actually passes.

⚡ 
ulw-qa

Attacks the build with hostile scenarios and fixes what breaks.

⚡ 
ulw-perf

Measures where it is actually slow or expensive, then fixes one hot path at a time.

## What OMH Adds

Hermes Agent already runs the loop. OMH decides what goes into it: which
model and effort each lane gets, who owns the code change, which skills
apply, and what counts as done. Two rules hold everywhere — model choice
and coding ownership are separate decisions, and nothing prepared is ever
reported as executed. The generated catalog, triggers, and evidence rules
live inWorkflow Reference.

### The workflow

Understand → Research → Decide → Plan → Execute → Verify → Operate → Learn

Stage

What happens

Understand

Confirm the intent, constraints, project terms, and stop conditions.

Research

Replace assumptions with source-backed product, code, or operational context.

Decide

Make the options, tradeoffs, and decision owner explicit.

Plan

Turn accepted scope, coding ownership, tests, and done criteria into an executable plan.

Execute

Dispatch bounded work to the selected owner and track what actually runs; a prepared handoff is not execution evidence.

Verify

Base the verdict on observed test results, review findings, CI status, and runtime evidence.

Operate

Keep release health, incidents, rollback state, and follow-up work visible.

Learn

Promote reviewed, scoped lessons into project memory or workflow improvements.

Highlights

Intelligence

What OMH adds

🧭 
Mixture-of-models routing

Every delegated lane lands on a category (model + reasoning effort) at dispatch time. Chains fall through when a provider rejects a model, and a child that did no work shows 
failed
, never a green row.

🎛️ 
Per-family calibration

Prompting is tuned per model family and generation — GPT-6 Astra, GPT-5.6, Claude 5.1, GLM 5.3, Kimi, Gemini, Qwen, DeepSeek and more — and each tune is kept only while the benchmark pair says it helps.

🗂️ 
Categories you own

Nine shipped categories per executor, with 
omh model-chains set
 to reorder, an entitlement interview that reorders chains per machine, and a live view of what a request would route to before it runs.

🖥️ 
Native TUI surface

The OMH HUD (live rows with category, turns, cost, cache), the phase todo above the prompt, 
parallel shot ×N
, full-row diff bands, and managed skins — installed beside Hermes, never patching it.

⚡ 
Observed parallel work

Independent work splits into fanout units with disjoint file ownership, admission control under provider pressure, typed result sidecars, and verification gates that read what came back.

🎼 
Maestro handoffs

An explicit second lane for Codex, Claude Code, or another CLI: readiness probes, capability snapshots, owner-fit reports, and per-run model and effort — opt-in, and never the default path.

💸 
Priced cost telemetry

Token counts and dollar figures on every HUD row and run summary, priced from a rate table that cites its source; an unpriceable run reads 
unknown
, never 
$0
.

🧠 
Long-term project memory

A file-backed memory provider Hermes loads, admission and retention policies, reviewer-gated writes, and recall packs with freshness and budget — Hermes' own memory stays untouched.

🔎 
Structural code search

A measured 
ast-grep
 playbook (28 languages, grep fallback) and 
omh codegraph uml
 for a repo-wide architecture picture, injected where executors read code.

🛡️ 
Guardrails you write

Toolcall rules that block an off-script call with your own rule text, a completion-integrity gate that refuses stubs and skipped tests as evidence, and an approval tier for risky actions.

♾️ 
Ultra workflow engines

Parallel delivery lanes, measured goal loops with ledgers and real completion gates, and decision-frontier interviews before any engine runs — listed in Ultra-Skills above.

📦 
A deterministic catalog

A hundred-plus installable skills generated from one source, routing precision corpora with negative controls, and drift gates that fail CI on a single divergent byte.

## Evidence Before Claims

OMH never reports that work happened unless it watched it happen. Every status
you see has two parts: the stage, and how sure OMH is about it.

You see

It means

Plan · not run

A prompt or plan is ready. 
Nothing has run yet.

Code · running

An executor is running now, and OMH is watching it.

Code · reported done

The executor said it finished. Nobody checked the result.

Test · verified

A test, review, or CI gate actually passed.

The distinction that matters is the second row from the bottom: an executor
saying it is done is not the same as anything having been checked, and most
tools spell both "complete". Capability impact is reported across separate
dimensions rather than collapsed into one marketing score. SeeCapability Impact.

## Documentation

* Documentation map
* Installation and updates
* Product direction and boundaries
* Architecture
* Capability manifests
* Workflow reference
* Roles
* Application cases
* Model routing, fan-out contracts, and request scoring
* Fanout executor evidence: sessions, failure diagnostics, capacity (agent/operator reference)
* Agent board and native Kanban coordination (agent/operator reference)
* Per-model calibration map
* Evidence rules and capability impact
* Long-term memory model
* Processing a very large PDF with Hermes
* Live model benchmark and measured results
* Release and development

## Development

For a source checkout:

PYTHONPATH=tests uv run python -m unittest discover -s tests -v
uv run python -m compileall -q src tests
uv run python -m omh.cli docs workflows --check
git diff --check

OMH is developed in the open as part ofTeam Art & Engineering. Follow@rlaopefor project updates.

## Contributors

Thanks to everyone who has contributed to oh-my-hermes.