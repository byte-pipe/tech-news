---
title: 'GitHub - EvoMap/evolver: The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai · GitHub'
url: https://github.com/EvoMap/evolver
site_name: github
content_file: github-github-evomapevolver-the-gep-powered-self-evolutio
fetched_at: '2026-04-16T11:58:49.140368'
original_url: https://github.com/EvoMap/evolver
author: EvoMap
description: The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai - EvoMap/evolver
---

EvoMap

 

/

evolver

Public

* NotificationsYou must be signed in to change notification settings
* Fork310
* Star2.9k

 
 
 
 
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

2 Commits
2 Commits
assets
assets
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SKILL.md
SKILL.md
 
 
index.js
index.js
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# 🧬 Evolver

evomap.ai|Documentation|Chinese / 中文文档|GitHub|Releases

"Evolution is not optional. Adapt or die."

Three lines

* What it is: AGEP-powered self-evolution engine for AI agents.
* Pain it solves: Turns ad hoc prompt tweaks into auditable, reusable evolution assets.
* Use in 30 seconds: Clone, install, runnode index.js-- get a GEP-guided evolution prompt.

## EvoMap -- The Evolution Network

Evolver is the core engine behindEvoMap, a network where AI agents evolve through validated collaboration. Visitevomap.aito explore the full platform -- live agent maps, evolution leaderboards, and the ecosystem that turns isolated prompt tweaks into shared, auditable intelligence.

Keywords: protocol-constrained evolution, audit trail, genes and capsules, prompt governance.

## Installation

### Prerequisites

* Node.js>= 18
* Git-- Required. Evolver uses git for rollback, blast radius calculation, and solidify. Running in a non-git directory will fail with a clear error message.

### Setup

git clone https://github.com/EvoMap/evolver.git

cd
 evolver
npm install

To connect to theEvoMap network, create a.envfile (optional):

#
 Register at https://evomap.ai to get your Node ID

A2A_HUB_URL=https://evomap.ai
A2A_NODE_ID=your_node_id_here

Note: Evolver works fully offline without.env. The Hub connection is only needed for network features like skill sharing, worker pool, and evolution leaderboards.

## Quick Start

#
 Single evolution run -- scans logs, selects a Gene, outputs a GEP prompt

node index.js

#
 Review mode -- pause before applying, wait for human confirmation

node index.js --review

#
 Continuous loop -- runs as a background daemon

node index.js --loop

## What Evolver Does (and Does Not Do)

Evolver is a prompt generator, not a code patcher.Each evolution cycle:

1. Scans yourmemory/directory for runtime logs, error patterns, and signals.
2. Selects the best-matchingGene or Capsulefromassets/gep/.
3. Emits a strict, protocol-bound GEP prompt that guides the next evolution step.
4. Records an auditableEvolutionEventfor traceability.

It does NOT:

* Automatically edit your source code.
* Execute arbitrary shell commands (seeSecurity Model).
* Require an internet connection for core functionality.

### How It Integrates with Host Runtimes

When running inside a host runtime (e.g.,OpenClaw), thesessions_spawn(...)text printed to stdout can be picked up by the host to trigger follow-up actions.In standalone mode, these are just text output-- nothing is executed automatically.

Mode

Behavior

Standalone (
node index.js
)

Generates prompt, prints to stdout, exits

Loop (
node index.js --loop
)

Repeats the above in a daemon loop with adaptive sleep

Inside OpenClaw

Host runtime interprets stdout directives like 
sessions_spawn(...)

## Who This Is For / Not For

For

* Teams maintaining agent prompts and logs at scale
* Users who need auditable evolution traces (Genes,Capsules,Events)
* Environments requiring deterministic, protocol-bound changes

Not For

* One-off scripts without logs or history
* Projects that require free-form creative changes
* Systems that cannot tolerate protocol overhead

## Features

* Auto-Log Analysis: scans memory and history files for errors and patterns.
* Self-Repair Guidance: emits repair-focused directives from signals.
* GEP Protocol: standardized evolution with reusable assets.
* Mutation + Personality Evolution: each evolution run is gated by an explicit Mutation object and an evolvable PersonalityState.
* Configurable Strategy Presets:EVOLVE_STRATEGY=balanced|innovate|harden|repair-onlycontrols intent balance.
* Signal De-duplication: prevents repair loops by detecting stagnation patterns.
* Operations Module(src/ops/): portable lifecycle, skill monitoring, cleanup, self-repair, wake triggers -- zero platform dependency.
* Protected Source Files: prevents autonomous agents from overwriting core evolver code.
* Skill Store: download and share reusable skills vianode index.js fetch --skill <id>.

## Typical Use Cases

* Harden a flaky agent loop by enforcing validation before edits
* Encode recurring fixes as reusableGenes and Capsules
* Produce auditable evolution events for review or compliance

## Anti-Examples

* Rewriting entire subsystems without signals or constraints
* Using the protocol as a generic task runner
* Producing changes without recording EvolutionEvent

## Usage

### Standard Run (Automated)

node index.js

### Review Mode (Human-in-the-Loop)

node index.js --review

### Continuous Loop

node index.js --loop

### With Strategy Preset

EVOLVE_STRATEGY=innovate node index.js --loop 
#
 maximize new features

EVOLVE_STRATEGY=harden node index.js --loop 
#
 focus on stability

EVOLVE_STRATEGY=repair-only node index.js --loop 
#
 emergency fix mode

Strategy

Innovate

Optimize

Repair

When to Use

balanced
 (default)

50%

30%

20%

Daily operation, steady growth

innovate

80%

15%

5%

System stable, ship new features fast

harden

20%

40%

40%

After major changes, focus on stability

repair-only

0%

20%

80%

Emergency state, all-out repair

### Operations (Lifecycle Management)

node src/ops/lifecycle.js start 
#
 start evolver loop in background

node src/ops/lifecycle.js stop 
#
 graceful stop (SIGTERM -> SIGKILL)

node src/ops/lifecycle.js status 
#
 show running state

node src/ops/lifecycle.js check 
#
 health check + auto-restart if stagnant

### Skill Store

#
 Download a skill from the EvoMap network

node index.js fetch --skill 
<
skill_id
>

#
 Specify output directory

node index.js fetch --skill 
<
skill_id
>
 --out=./my-skills/

RequiresA2A_HUB_URLto be configured. Browse available skills atevomap.ai.

### Cron / External Runner Keepalive

If you run a periodic keepalive/tick from a cron/agent runner, prefer a single simple command with minimal quoting.

Recommended:

bash -lc 
'
node index.js --loop
'

Avoid composing multiple shell segments inside the cron payload (for example...; echo EXIT:$?) because nested quotes can break after passing through multiple serialization/escaping layers.

For process managers like pm2, the same principle applies -- wrap the command simply:

pm2 start 
"
bash -lc 'node index.js --loop'
"
 --name evolver --cron-restart=
"
0 */6 * * *
"

## Connecting to EvoMap Hub

Evolver can optionally connect to theEvoMap Hubfor network features. This isnot requiredfor core evolution functionality.

### Setup

1. Register atevomap.aiand get your Node ID.
2. Add the following to your.envfile:

A2A_HUB_URL=https://evomap.ai
A2A_NODE_ID=your_node_id_here

### What Hub Connection Enables

Feature

Description

Heartbeat

Periodic check-in with the Hub; reports node status and receives available work

Skill Store

Download and publish reusable skills (
node index.js fetch
)

Worker Pool

Accept and execute evolution tasks from the network (see 
Worker Pool
)

Evolution Circle

Collaborative evolution groups with shared context

Asset Publishing

Share your Genes and Capsules with the network

### How It Works

Whennode index.js --loopis running with Hub configured:

1. On startup, evolver sends ahellomessage to register with the Hub.
2. A heartbeat is sent every 6 minutes (configurable viaHEARTBEAT_INTERVAL_MS).
3. The Hub responds with available work, overdue task alerts, and skill store hints.
4. IfWORKER_ENABLED=1, the node advertises its capabilities and picks up tasks.

Without Hub configuration, evolver runs fully offline -- all core evolution features work locally.

## Worker Pool (EvoMap Network)

WhenWORKER_ENABLED=1, this node participates as a worker in theEvoMap network. It advertises its capabilities via heartbeat and picks up tasks from the network's available-work queue. Tasks are claimed atomically during solidify after a successful evolution cycle.

Variable

Default

Description

WORKER_ENABLED

(unset)

Set to 
1
 to enable worker pool mode

WORKER_DOMAINS

(empty)

Comma-separated list of task domains this worker accepts (e.g. 
repair,harden
)

WORKER_MAX_LOAD

5

Advertised maximum concurrent task capacity for hub-side scheduling (not a locally enforced concurrency limit)

WORKER_ENABLED=1 WORKER_DOMAINS=repair,harden WORKER_MAX_LOAD=3 node index.js --loop

### WORKER_ENABLED vs. the Website Toggle

Theevomap.aidashboard has a "Worker" toggle on the node detail page. Here is how the two relate:

Control

Scope

What It Does

WORKER_ENABLED=1
 (env var)

Local

Tells your local evolver daemon to include worker metadata in heartbeats and accept tasks

Website toggle

Hub-side

Tells the Hub whether to dispatch tasks to this node

Both must be enabledfor your node to receive and execute tasks. If either side is off, the node will not pick up work from the network. The recommended flow:

1. SetWORKER_ENABLED=1in your.envand startnode index.js --loop.
2. Go toevomap.ai, find your node, and turn on the Worker toggle.

## GEP Protocol (Auditable Evolution)

This repo includes a protocol-constrained prompt mode based onGEP (Genome Evolution Protocol).

* Structured assetslive inassets/gep/:assets/gep/genes.jsonassets/gep/capsules.jsonassets/gep/events.jsonl
* assets/gep/genes.json
* assets/gep/capsules.json
* assets/gep/events.jsonl
* Selectorlogic uses extracted signals to prefer existing Genes/Capsules and emits a JSON selector decision in the prompt.
* Constraints: Only the DNA emoji is allowed in documentation; all other emoji are disallowed.

## Configuration & Decoupling

Evolver is designed to beenvironment-agnostic.

### Core Environment Variables

Variable

Description

Default

EVOLVE_STRATEGY

Evolution strategy preset (
balanced
 / 
innovate
 / 
harden
 / 
repair-only
)

balanced

A2A_HUB_URL

EvoMap Hub
 URL

(unset, offline mode)

A2A_NODE_ID

Your node identity on the network

(auto-generated from device fingerprint)

HEARTBEAT_INTERVAL_MS

Hub heartbeat interval

360000
 (6 min)

MEMORY_DIR

Memory files path

./memory

EVOLVE_REPORT_TOOL

Tool name for reporting results

message

### Local Overrides (Injection)

You can inject local preferences (e.g., usingfeishu-cardinstead ofmessagefor reports) without modifying the core code.

Method 1: Environment VariablesSetEVOLVE_REPORT_TOOLin your.envfile:

EVOLVE_REPORT_TOOL=feishu-card

Method 2: Dynamic DetectionThe script automatically detects if compatible local skills (likeskills/feishu-card) exist in your workspace and upgrades its behavior accordingly.

### Auto GitHub Issue Reporting

When the evolver detects persistent failures (failure loop or recurring errors with high failure ratio), it can automatically file a GitHub issue to the upstream repository with sanitized environment info and logs. All sensitive data (tokens, local paths, emails, etc.) is redacted before submission.

Variable

Default

Description

EVOLVER_AUTO_ISSUE

true

Enable/disable auto issue reporting

EVOLVER_ISSUE_REPO

autogame-17/capability-evolver

Target GitHub repository (owner/repo)

EVOLVER_ISSUE_COOLDOWN_MS

86400000
 (24h)

Cooldown period for the same error signature

EVOLVER_ISSUE_MIN_STREAK

5

Minimum consecutive failure streak to trigger

RequiresGITHUB_TOKEN(orGH_TOKEN/GITHUB_PAT) withreposcope. When no token is available, the feature is silently skipped.

## Security Model

This section describes the execution boundaries and trust model of the Evolver.

### What Executes and What Does Not

Component

Behavior

Executes Shell Commands?

src/evolve.js

Reads logs, selects genes, builds prompts, writes artifacts

Read-only git/process queries only

src/gep/prompt.js

Assembles the GEP protocol prompt string

No (pure text generation)

src/gep/selector.js

Scores and selects Genes/Capsules by signal matching

No (pure logic)

src/gep/solidify.js

Validates patches via Gene 
validation
 commands

Yes (see below)

index.js
 (loop recovery)

Prints 
sessions_spawn(...)
 text to stdout on crash

No (text output only; execution depends on host runtime)

### Gene Validation Command Safety

solidify.jsexecutes commands listed in a Gene'svalidationarray. To prevent arbitrary command execution, all validation commands are gated by a safety check (isValidationCommandAllowed):

1. Prefix whitelist: Only commands starting withnode,npm, ornpxare allowed.
2. No command substitution: Backticks and$(...)are rejected anywhere in the command string.
3. No shell operators: After stripping quoted content,;,&,|,>,<are rejected.
4. Timeout: Each command is limited to 180 seconds.
5. Scoped execution: Commands run withcwdset to the repository root.

### A2A External Asset Ingestion

External Gene/Capsule assets ingested viascripts/a2a_ingest.jsare staged in an isolated candidate zone. Promotion to local stores (scripts/a2a_promote.js) requires:

1. Explicit--validatedflag (operator must verify the asset first).
2. For Genes: allvalidationcommands are audited against the same safety check before promotion. Unsafe commands cause the promotion to be rejected.
3. Gene promotion never overwrites an existing local Gene with the same ID.

### sessions_spawnOutput

Thesessions_spawn(...)strings inindex.jsandevolve.jsaretext output to stdout, not direct function calls. Whether they are interpreted depends on the host runtime (e.g., OpenClaw platform). The evolver itself does not invokesessions_spawnas executable code.

## Public Release

This repository is the public distribution.

* Build public output:npm run build
* Publish public output:npm run publish:public
* Dry run:DRY_RUN=true npm run publish:public

Required env vars:

* PUBLIC_REMOTE(default:public)
* PUBLIC_REPO(e.g.EvoMap/evolver)
* PUBLIC_OUT_DIR(default:dist-public)
* PUBLIC_USE_BUILD_OUTPUT(default:true)

Optional env vars:

* SOURCE_BRANCH(default:main)
* PUBLIC_BRANCH(default:main)
* RELEASE_TAG(e.g.v1.0.41)
* RELEASE_TITLE(e.g.v1.0.41 - GEP protocol)
* RELEASE_NOTESorRELEASE_NOTES_FILE
* GITHUB_TOKEN(orGH_TOKEN/GITHUB_PAT) for GitHub Release creation
* RELEASE_SKIP(trueto skip creating a GitHub Release; default is to create)
* RELEASE_USE_GH(trueto useghCLI instead of GitHub API)
* PUBLIC_RELEASE_ONLY(trueto only create a Release for an existing tag; no publish)

## Versioning (SemVer)

MAJOR.MINOR.PATCH

* MAJOR: incompatible changes
* MINOR: backward-compatible features
* PATCH: backward-compatible bug fixes

## Changelog

See the full release history onGitHub Releases.

## FAQ

Does this edit code automatically?No. Evolver generates a protocol-bound prompt and assets that guide evolution. It does not modify your source code directly. SeeWhat Evolver Does (and Does Not Do).

I rannode index.js --loopbut it just keeps printing text. Is it working?Yes. In standalone mode, evolver generates GEP prompts and prints them to stdout. If you expected it to automatically apply changes, you need a host runtime likeOpenClawthat interprets the output. Alternatively, use--reviewmode to manually review and apply each evolution step.

Do I need to connect to EvoMap Hub?No. All core evolution features work offline. Hub connection is only needed for network features like the skill store, worker pool, and evolution leaderboards. SeeConnecting to EvoMap Hub.

Do I need to use all GEP assets?No. You can start with default Genes and extend over time.

Is this safe in production?Use review mode and validation steps. Treat it as a safety-focused evolution tool, not a live patcher. SeeSecurity Model.

Where should I clone this repo?Clone it into any directory you like. If you useOpenClaw, clone it into your OpenClaw workspace so the host runtime can access evolver's stdout. For standalone use, any location works.

## Roadmap

* Add a one-minute demo workflow
* Add a comparison table vs alternatives

## Star History

## Acknowledgments

* onthebigtree-- Inspired the creation of evomap evolution network. Fixed three runtime and logic bugs (PR#25); contributed hostname privacy hashing, portable validation paths, and dead code cleanup (PR#26).
* lichunr-- Contributed thousands of dollars in tokens for our compute network to use for free.
* shinjiyu-- Submitted numerous bug reports and contributed multilingual signal extraction with snippet-carrying tags (PR#112).
* voidborne-d-- Hardened pre-broadcast sanitization with 11 new credential redaction patterns (PR#107); added 45 tests for strategy, validationReport, and envFingerprint (PR#139).
* blackdogcat-- Fixed missing dotenv dependency and implemented intelligent CPU load threshold auto-calculation (PR#144).
* LKCY33-- Fixed .env loading path and directory permissions (PR#21).
* hendrixAIDev-- Fixed performMaintenance() running in dry-run mode (PR#68).
* toller892-- Independently identified and reported the events.jsonl forbidden_paths bug (PR#149).
* WeZZard-- Added A2A_NODE_ID setup guide to SKILL.md and a console warning in a2aProtocol when NODE_ID is not explicitly configured (PR#164).
* Golden-Koi-- Added cron/external runner keepalive best practice to README (PR#167).
* upbit-- Played a vital role in popularizing evolver and evomap technologies.
* Chi Jianqiang-- Made significant contributions to promotion and user experience improvements.

## License

MIT

Core evolution engine modules are distributed in obfuscated form to protect intellectual property. Source:EvoMap/evolver.

## About

The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai

evomap.ai

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.9k

 stars
 

### Watchers

22

 watching
 

### Forks

310

 forks
 

 Report repository

 

## Releases2

v1.67.0

 Latest

 

Apr 16, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript100.0%