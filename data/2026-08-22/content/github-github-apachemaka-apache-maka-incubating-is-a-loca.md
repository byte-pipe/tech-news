---
title: 'GitHub - apache/maka: Apache Maka (Incubating) is a local-first AI agent workspace. Model messages, tool calls, tool results, permission decisions, and termination events are recorded as an append-only log. · GitHub'
url: https://github.com/apache/maka
site_name: github
content_file: github-github-apachemaka-apache-maka-incubating-is-a-loca
fetched_at: '2026-08-22T11:19:17.933038'
original_url: https://github.com/apache/maka
author: apache
description: Apache Maka (Incubating) is a local-first AI agent workspace. Model messages, tool calls, tool results, permission decisions, and termination events are recorded as an append-only log. - apache/maka
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 apache

 

/

maka

Public

* NotificationsYou must be signed in to change notification settings
* Fork248
* Star2.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,676 Commits
3,676 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude
.claude
 
 
.github
.github
 
 
.maka-shots
.maka-shots
 
 
apps/
desktop
apps/
desktop
 
 
docs
docs
 
 
experiments/
windows-sandbox
experiments/
windows-sandbox
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
skills/
maka-architecture-docs
skills/
maka-architecture-docs
 
 
.asf.yaml
.asf.yaml
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mailmap
.mailmap
 
 
.pr_agent.toml
.pr_agent.toml
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
ARCHITECTURE.zh-CN.md
ARCHITECTURE.zh-CN.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTING.zh-CN.md
CONTRIBUTING.zh-CN.md
 
 
DESIGN.md
DESIGN.md
 
 
DISCLAIMER-WIP
DISCLAIMER-WIP
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.jsonc
biome.jsonc
 
 
knip.json
knip.json
 
 
maka-proposal-zh-review.txt
maka-proposal-zh-review.txt
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.lib.json
tsconfig.lib.json
 
 
View all files

## Repository files navigation

# Apache Maka (Incubating)

A local-first Agent workspace built for real work.

Maka does more than answer questions. With controlled permissions, it can inspect projects, execute tools, produce artifacts, and preserve model messages and tool calls as recoverable execution facts. Desktop, the terminal TUI, the non-interactive CLI, and Maka evaluation subjects all execute through Runtime Host.

Note

Apache Maka (Incubating) is an effort undergoing incubation at The Apache Software Foundation (ASF), sponsored by the Apache Incubator PMC. Incubation is required of all newly accepted projects until a further review indicates that the infrastructure, communications, and decision-making process have stabilized in a manner consistent with other successful ASF projects. While incubation status is not necessarily a reflection of the completeness or stability of the code, it does indicate that the project has yet to be fully endorsed by the ASF.DISCLAIMER-WIPrecords the issues the project is currently aware of.

Important

Maka is under active development. The macOS Apple Silicon desktop build is an early public release; data formats, CLI commands, and experimental capabilities may still change.

## Why Maka

* Local-first instead of hosted-first: sessions, settings, and run records stay on your machine by default. You choose the model connection: cloud API, local model, or compatible gateway.
* Log is the Runtime: model messages, Tool Calls, Tool Results, and termination facts enter Runtime Event Log. Sessions, UI, model context, and recovery are projections over that log.
* Context is not history: Tool Result pruning and LLM Compaction change what the next inference sees without treating recorded evidence as disposable context.
* One execution authority: Runtime Host owns Session, Turn, agent lifecycle, continuation, tools, and events. Eval owns only experiment semantics and results.

ReadMaka Backend Architecturefor the complete design.

## Surfaces

Entry point

Best for

Current capability

Desktop

Daily interaction, file and Artifact workflows, model and permission setup

Electron + React with streaming sessions, tool timelines, branching, search, and recovery

TUI / CLI

Using Maka in the current project directory or running one non-interactive Turn

maka
, 
maka run
; shares workspace and model connections with Desktop

Eval

Reproducible benchmark experiments across Maka and external subjects

maka eval run <spec> --out <directory>

## Current capabilities

### Agent Runtime

* Multiple model connections, streaming output, thinking, usage accounting, and provider-error normalization;
* Local tools includingRead,Write,Edit,Bash,Glob, andGrep;
* Tool schema validation, dynamic availability, permission policy, watchdogs, abort, and error classification;
* Runtime Event Log, AgentRun ledger, startup recovery, Turn Evidence, active Tool Result pruning, and history compaction.

### Desktop workspace

* Create, archive, search, rename, retry, regenerate, and branch sessions from a Turn;
* Artifact lists and previews, workspace instructions, model settings, and permission settings;
* Local memory, web search, and bot entry points;
* Integrations are configured independently, and not every experimental entry is available by default.

### Evaluation

* Declarative multi-arm experiments expanded into task × repetition × subject cells;
* Immutable per-cell attempts with targeted infrastructure replacement and earliest-valid selection;
* A small result kernel for score, normalized usage, attributable cost, duration, status, failure reason, and artifacts;
* Maka subjects execute only through Runtime Host; external subjects use generic external subject adapters.

## Quick start

### Releases and downloads

Apache Maka has not made an Apache release yet. Everything currently published from this repository or from a package registry was produced before or during incubation, is not an Apache Software Foundation release, and has not been reviewed or voted on by the Incubator PMC.

Once Apache releases exist, the official release is the source release published by the ASF and approved by the podling PPMC and the Incubator PMC. A package built from that source and distributed elsewhere, for example through a package registry or as a Desktop installer, is a convenience artifact rather than the release itself, and it is valid only when it is built from an approved source release..github/ASF_SOURCE_RELEASE.mdholds the candidate contract, signing path, and verification steps.

Until an approved source release exists, this README recommends no prebuilt download. Build and run Maka from source as described below. Desktop currently targets Apple Silicon Macs (arm64); Intel Macs and Linux are not supported yet, andWindows supportremains an unsigned preview rather than a supported release tier.

### Requirements

* Node.js 22.19 or newer (CI uses Node.js 24);
* npm (the lockfile and scripts use npm; the currentpackageManageris npm 11);
* Git;
* ripgrep, used by Runtime'sGreptool.

### Start Desktop

git clone https://github.com/apache/maka.git

cd
 maka
npm ci
npm run dev

npm run devstarts the Desktop development environment with HMR. To build every workspace before starting Electron, use:

npm run dev:full

If dependencies were installed withELECTRON_SKIP_BINARY_DOWNLOAD=1, install the Electron platform binary before starting:

node node_modules/electron/install.js

### First run

Maka does not bundle a shared model account. On first launch:

1. OpenSettings → Models;
2. Add an API, local-model, or supported account connection;
3. Test it and choose a default model;
4. Return to the workspace and start a task.

The app distinguishes configured, send-ready, and experimental connection states. An account flow that is not wired into Runtime is not presented as a usable model.

## Terminal entry points

For the public npm package, see theCLI installation and usage guide.
The commands below run the development CLI from a source checkout.

Build the workspaces first:

npm run build

Then start the TUI or run one Turn:

npm run cli:dev
npm run cli:dev -- run 
"
Summarize this repository and identify its most important risk
"

npm run cli:dev -- run --graph 
"
Implement two independent slices, integrate them, then review the result
"

npm run cli:dev -- --help

The TUI also accepts/graph on,/graph off, and/graph <task>. Non-interactive--graphruns wait for the durable Graph to finish before printing the final
supervisor output. Graph implementation operators use isolated Git worktrees, so
the source project must be a clean Git worktree.

The repository CLI uses the sameMaka Devprofile as a development Desktop build. The
releasedmakabinary continues to use theMakaprofile; the two profiles are not copied or
synchronized automatically. Evaluation specs and adapters live inpackages/eval.

## Architecture

The backend spine is:

Desktop / TUI / CLI → Runtime Host → SessionManager → AgentRun
 ↓
 Model + Tool Runtime → Runtime Event Log
 ↓
 Context / Session / UI projections

Experiment → Cells → Attempts → Results
 ↓
 Runtime Host executes Maka subjects

Start withARCHITECTURE.md. It provides the system map, code boundaries, problem-oriented reading paths, and six bilingual deep dives.

## Repository layout

apps/desktop/ Electron main / preload / React renderer

packages/core/ Pure contracts for Sessions, Events, Permissions, and Connections
packages/storage/ SQLite operational state, configuration, and payload stores
packages/runtime/ AgentRun, model adapters, tools, context, and recovery
packages/eval/ Experiment cells, attempts, results, and executor/subject adapters
packages/cli/ TUI and non-interactive CLI
packages/ui/ Shared conversation, Markdown, Artifact, and UI primitives

docs/ Architecture, product, security, privacy, and test contracts
scripts/ Build hygiene, visual checks, smoke tests, and release helpers

## Local data and security boundary

Maka stores workspace data under ElectronuserDataby default:

<Electron userData>/workspaces/default/
 runtime.sqlite
 connection-catalog.json
 credential-vault.json
 settings.json
 artifacts/

Current boundaries that matter:

* The current connection catalog isconnection-catalog.json. Existingllm-connections.jsonfiles stay on disk and are not imported;
* Sessions, messages, execution ledgers, workflows, usage, Automations, and Daily Review live inruntime.sqlite;
* Runtime Policy credentials, including Connection API/OAuth material, request headers, web-search keys, and proxy passwords, live in local plaintextcredential-vault.json, behind the OS account boundary, with POSIX directory mode0700and file mode0600enforced;
* Runtime Host client profile access credentials are separate and live under<Electron userData>/runtime-host-client/credentials.json. Pre-existing ElectronsafeStoragecredential/token files are not imported; affected users must re-authenticate;
* Renderer does not receive plaintext credentials. File writes, Shell, and dangerous tool calls pass through the permission engine;
* Eval does not construct Runtime or read Runtime storage. Maka subjects connect to an existing Runtime Host.

ReadSECURITY.mdfor security reporting and policy, anddocs/README.mdfor current privacy and sandbox contracts.

## Runtime storage and recovery

runtime.sqliteis the sole operational authority. It owns RuntimeEvents,
session metadata and message history, Agent Graph control, core execution state,
workflow state, usage and pricing, Artifact metadata, Automations, Daily Review,
and Runtime continuation records. Artifact payload bytes remain regular files underartifacts/; connections, credentials, settings, MCP configuration, skills,
and device identity remain configuration files.

This storage generation does not import earlier File/JSONL authorities. On
upgrade, legacy session titles may still be discoverable through current
metadata, but conversation history that exists only in legacy transcript files
is not copied intosession_messagesand opens as an empty thread. Likewise,
pre-version orsafeStorage-encrypted credential/token files are not migrated;
users with only those copies must re-authenticate. This data-loss boundary is
intentional for this release and must be considered before upgrading an
existing workspace.

Full operational backup uses the database owner's online SQLite backup API and
copies canonical Artifact payloads under the Artifact writer lock. Its manifest
binds every file by size and SHA-256. Validation checks the standalone SQLite
snapshot's integrity, foreign keys, schema registry and required tables,
decodes canonical session-message and Artifact records, and verifies Artifact
payload sizes against SQLite metadata before restore. Backup and restore use
owner-only file modes, file and directory synchronization, staging, and atomic
publication.

Runtime continuation remains opt-in:

* MAKA_RUNTIME_SAFE_BOUNDARY_RESUME=1enables the Desktop interrupted-turnSafe resumeaction, CLI/TUI/resume, and Desktop startup auto-resume.
These paths may call the configured model provider and consume tokens. Enable
the flag only when that behavior is explicitly desired.

Phase 2 provides the durable write-side boundary and fail-closed safe-boundary
continuation. Phase 3 reconciliation for indeterminate tool side effects is not
implemented yet; ambiguous tool outcomes remain parked rather than retried.

## Development and verification

Before sending a change, readCONTRIBUTING.md.

Common repository-level commands:

npm run build
npm run typecheck
npm 
test

npm run check:release

Run one workspace in isolation:

npm --workspace @maka/runtime 
test

npm --workspace @maka/eval 
test

npm --workspace @maka/desktop 
test

Use the following commands to updatepackages/core/src/model-metadata.generated.tsfrom models.dev and run the focused tests. Keep access-path-specific overrides inmodel-metadata.ts; do not edit the generated file by hand.

npm run sync:model-metadata
npm --workspace @maka/core 
test

Desktop real-window and visual verification:

npm --workspace @maka/desktop run e2e
npm --workspace @maka/desktop run smoke:real-window

Before submitting code, run typecheck, build, and focused tests proportionate to the change, followed bygit diff --check.

## Documentation

* Documentation index and authority map
* Backend architecture
* Product design
* Contributing guide
* Security policy

## License

Maka is licensed under theApache License 2.0. SeeNOTICEfor attribution information. Third-party components remain
subject to their respective licenses and notices.

Apache Maka, Maka, Apache, the Apache feather, and the Apache Maka project logo are either registered trademarks or trademarks of The Apache Software Foundation.