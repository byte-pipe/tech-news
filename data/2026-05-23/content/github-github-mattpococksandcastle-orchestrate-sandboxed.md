---
title: 'GitHub - mattpocock/sandcastle: Orchestrate sandboxed coding agents in TypeScript with sandcastle.run() · GitHub'
url: https://github.com/mattpocock/sandcastle
site_name: github
content_file: github-github-mattpococksandcastle-orchestrate-sandboxed
fetched_at: '2026-05-23T11:28:39.096912'
original_url: https://github.com/mattpocock/sandcastle
author: mattpocock
description: Orchestrate sandboxed coding agents in TypeScript with sandcastle.run() - mattpocock/sandcastle
---

mattpocock

 

/

sandcastle

Public

* NotificationsYou must be signed in to change notification settings
* Fork512
* Star4.8k

 
 
 
 
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

944 Commits
944 Commits
.changeset
.changeset
 
 
.claude
.claude
 
 
.factory
.factory
 
 
.github/
workflows
.github/
workflows
 
 
.husky
.husky
 
 
.out-of-scope
.out-of-scope
 
 
.sandcastle
.sandcastle
 
 
docs
docs
 
 
ideas
ideas
 
 
research
research
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.mailmap
.mailmap
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTEXT.md
CONTEXT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.build.json
tsconfig.build.json
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

## What Is Sandcastle?

A TypeScript library for orchestrating AI coding agents in isolated sandboxes:

1. You invoke agents with a singlesandcastle.run().
2. Sandcastle handles sandboxing the agent with a configurable branch strategy.
3. The commits made on the branches get merged back.

Sandcastle is provider-agnostic — it ships with built-in providers for Docker, Podman, and Vercel, and you can create your own. Great for parallelizing multiple AFK agents, creating review pipelines, or even just orchestrating your own agents.

## Prerequisites

* Git
* A sandbox provider — Sandcastle needs an isolated environment to run agents in. Built-in options:Docker Desktop— most common for local developmentPodman— rootless alternative to DockerVercel— cloud-based Firecracker microVMs via@vercel/sandboxOrcreate your ownusingcreateBindMountSandboxProviderorcreateIsolatedSandboxProvider
* Docker Desktop— most common for local development
* Podman— rootless alternative to Docker
* Vercel— cloud-based Firecracker microVMs via@vercel/sandbox
* Orcreate your ownusingcreateBindMountSandboxProviderorcreateIsolatedSandboxProvider

## Quick start

1. Install the package:

npm install --save-dev @ai-hero/sandcastle

1. Runsandcastle init. This scaffolds a.sandcastledirectory with all the files needed.

npx sandcastle init

1. Edit.sandcastle/.envand fill in your default values forANTHROPIC_API_KEY. If you want to use your Claude subscription instead of an API key, see#191.

cp .sandcastle/.env.example .sandcastle/.env

1. Run the.sandcastle/main.ts(ormain.mts) file withnpx tsx

npx tsx .sandcastle/main.ts

// 3. Run the agent via the JS API

import
 
{
 
run
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,
 
// or podman(), vercel(), or your own provider

 
promptFile
: 
".sandcastle/prompt.md"
,

}
)
;

## Sandbox Providers

Sandcastle uses aSandboxProviderto create isolated environments. Thesandboxoption onrun(),interactive(), andcreateSandbox()accepts any provider, includingnoSandbox()— opt in to running the agent directly on the host when container isolation is undesired. Built-in providers:

Provider

Import path

Type

Accepted by

Docker

@ai-hero/sandcastle/sandboxes/docker

Bind-mount

run()
, 
createSandbox()
, 
interactive()

Podman

@ai-hero/sandcastle/sandboxes/podman

Bind-mount

run()
, 
createSandbox()
, 
interactive()

Vercel

@ai-hero/sandcastle/sandboxes/vercel

Isolated

run()
, 
createSandbox()
, 
interactive()

No-sandbox

@ai-hero/sandcastle/sandboxes/no-sandbox

None

run()
, 
createSandbox()
, 
interactive()

Worktree methods (wt.run(),wt.interactive(),wt.createSandbox()) accept the same providers as their top-level counterparts.wt.interactive()defaults tonoSandbox()when no sandbox is specified.

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

import
 
{
 
podman
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/podman"
;

import
 
{
 
vercel
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/vercel"
;

import
 
{
 
noSandbox
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/no-sandbox"
;

// Docker, Podman, and Vercel are interchangeable in run() and createSandbox():

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
prompt
: 
"..."
,

}
)
;

// No-sandbox runs the agent directly on the host — accepted by run(),

// createSandbox(), and interactive(). Skips container isolation entirely:

await
 
interactive
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
noSandbox
(
)
,

 
prompt
: 
"..."
,
 
// optional — omit to launch the TUI with no initial prompt

 
cwd
: 
"/path/to/other-repo"
,
 
// optional — defaults to process.cwd()

}
)
;

You can alsocreate your own providerusingcreateBindMountSandboxProviderorcreateIsolatedSandboxProvider.

## API

Sandcastle exports a programmaticrun()function for use in scripts, CI pipelines, or custom tooling. The examples below usedocker(), but anySandboxProviderworks in its place.

import
 
{
 
run
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

const
 
result
 
=
 
await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
promptFile
: 
".sandcastle/prompt.md"
,

}
)
;

console
.
log
(
result
.
iterations
.
length
)
;
 
// number of iterations executed

console
.
log
(
result
.
iterations
)
;
 
// per-iteration results with optional sessionId

console
.
log
(
result
.
commits
)
;
 
// array of { sha } for commits created

console
.
log
(
result
.
branch
)
;
 
// target branch name

### All options

import
 
{
 
run
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

const
 
result
 
=
 
await
 
run
(
{

 
// Agent provider — required. Pass a model string to claudeCode().

 
// Optional second arg for provider-specific options like effort level.

 
agent
: 
claudeCode
(
"claude-opus-4-7"
,
 
{
 
effort
: 
"high"
 
}
)
,

 
// Sandbox provider — required. Any SandboxProvider works (docker, podman, vercel, or custom).

 
// Provider-specific config (like imageName, mounts) lives inside the provider factory call.

 
sandbox
: 
docker
(
{

 
imageName
: 
"sandcastle:local"
,

 
// Optional: override the UID/GID used for --user flag (defaults to host UID/GID).

 
// Must match the UID baked into the image. Pre-flight check catches mismatches.

 
// containerUid: 1000,

 
// containerGid: 1000,

 
// Optional: mount host directories into the sandbox (e.g. package manager caches)

 
// hostPath supports absolute, tilde-expanded (~), and relative paths (resolved from cwd).

 
// sandboxPath supports absolute and relative paths (resolved from the sandbox repo directory).

 
mounts
: 
[

 
{
 
hostPath
: 
"~/.npm"
,
 
sandboxPath
: 
"/home/agent/.npm"
,
 
readonly
: 
true
 
}
,

 
{
 
hostPath
: 
"data"
,
 
sandboxPath
: 
"data"
 
}
,
 
// mounts <cwd>/data → <sandbox-repo>/data

 
]
,

 
// Optional: SELinux volume label — "z" (default, shared), "Z" (private), or false (none).

 
// No-op on non-SELinux systems (Docker Desktop on macOS/Windows, Linux without SELinux).

 
selinuxLabel
: 
"z"
,

 
// Optional: provider-level env vars merged at launch time

 
env
: 
{
 
DOCKER_SPECIFIC
: 
"value"
 
}
,

 
// Optional: attach container to Docker network(s) — string or string[]

 
network
: 
"my-network"
,

 
}
)
,

 
// Host repo directory — replaces process.cwd() as the anchor for

 
// .sandcastle/ artifacts (worktrees, logs, env, patches) and git operations.

 
// Relative paths resolve against process.cwd(). Defaults to process.cwd().

 
cwd
: 
"../other-repo"
,

 
// Branch strategy — controls how the agent's changes relate to branches.

 
// Defaults to { type: "head" } for bind-mount and { type: "merge-to-head" } for isolated providers.

 
branchStrategy
: 
{
 
type
: 
"branch"
,
 
branch
: 
"agent/fix-42"
 
}
,

 
// Prompt source — provide one of these, not both.

 
// Note: promptFile resolves against process.cwd(), NOT cwd.

 
promptFile
: 
".sandcastle/prompt.md"
,
 
// path to a prompt file

 
// prompt: "Fix issue #42 in this repo", // OR an inline prompt string

 
// Values substituted for {{KEY}} placeholders in the prompt.

 
promptArgs
: 
{

 
ISSUE_NUMBER
: 
"42"
,

 
}
,

 
// Maximum number of agent iterations to run before stopping. Default: 1

 
maxIterations
: 
5
,

 
// Display name for this run, shown as a prefix in log output.

 
name
: 
"fix-issue-42"
,

 
// Lifecycle hooks grouped by where they run: host or sandbox.

 
hooks
: 
{

 
host
: 
{

 
onWorktreeReady
: 
[
{
 
command
: 
"cp .env.example .env"
 
}
]
,

 
onSandboxReady
: 
[
{
 
command
: 
"echo setup done"
 
}
]
,

 
}
,

 
sandbox
: 
{

 
onSandboxReady
: 
[
{
 
command
: 
"npm install"
 
}
]
,

 
}
,

 
}
,

 
// Host-relative file paths to copy into the sandbox before the container starts.

 
// Not supported with branchStrategy: { type: "head" }.

 
copyToWorktree
: 
[
".env"
]
,

 
// Override default timeouts for built-in lifecycle steps.

 
// Unset keys keep their defaults.

 
timeouts
: 
{

 
copyToWorktreeMs
: 
120_000
,
 
// default: 60_000

 
}
,

 
// How to record progress. Default: write to a file under .sandcastle/logs/

 
logging
: 
{

 
type
: 
"file"
,

 
path
: 
".sandcastle/logs/my-run.log"
,

 
// Optional: forward the agent's output stream to your own observability system.

 
// Fires for each text chunk and tool call the agent produces. Errors thrown

 
// by the callback are swallowed so a broken forwarder cannot kill the run.

 
onAgentStreamEvent
: 
(
event
)
 
=>
 
{

 
// event is { type: "text" | "toolCall", iteration, timestamp, ... }

 
myLogger
.
info
(
event
)
;

 
}
,

 
}
,

 
// logging: { type: "stdout" }, // OR render an interactive UI in the terminal

 
// String (or array of strings) the agent emits to end the iteration loop early.

 
// Default: "<promise>COMPLETE</promise>"

 
completionSignal
: 
"<promise>COMPLETE</promise>"
,

 
// Idle timeout in seconds — resets whenever the agent produces output. Default: 600 (10 minutes)

 
idleTimeoutSeconds
: 
600
,

 
// Structured output — extract a typed payload from the agent's stdout.

 
// Requires maxIterations === 1 and the tag must appear in the prompt.

 
// output: Output.object({ tag: "result", schema: z.object({ answer: z.number() }) }),

 
// output: Output.string({ tag: "summary" }),

}
)
;

console
.
log
(
result
.
iterations
.
length
)
;
 
// number of iterations executed

console
.
log
(
result
.
completionSignal
)
;
 
// matched signal string, or undefined if none fired

console
.
log
(
result
.
commits
)
;
 
// array of { sha } for commits created

console
.
log
(
result
.
branch
)
;
 
// target branch name

### createSandbox()— reusable sandbox

UsecreateSandbox()when you need to run multiple agents (or multiple rounds of the same agent) inside a single sandbox. It creates the sandbox once, and you callsandbox.run()as many times as you need. This avoids repeated container startup costs and keeps all runs on the same branch.

Userun()instead when you only need a single one-shot invocation — it handles sandbox lifecycle automatically.

#### Basic single-run usage

import
 
{
 
createSandbox
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

await
 using 
sandbox
 
=
 
await
 
createSandbox
(
{

 
branch
: 
"agent/fix-42"
,

 
sandbox
: 
docker
(
)
,

}
)
;

const
 
result
 
=
 
await
 
sandbox
.
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
prompt
: 
"Fix issue #42 in this repo."
,

}
)
;

console
.
log
(
result
.
commits
)
;
 
// [{ sha: "abc123" }]

#### Multi-run implement-then-review

import
 
{
 
createSandbox
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

await
 using 
sandbox
 
=
 
await
 
createSandbox
(
{

 
branch
: 
"agent/fix-42"
,

 
sandbox
: 
docker
(
)
,

 
hooks
: 
{
 
sandbox
: 
{
 
onSandboxReady
: 
[
{
 
command
: 
"npm install"
 
}
]
 
}
 
}
,

}
)
;

// Step 1: implement

const
 
implResult
 
=
 
await
 
sandbox
.
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
promptFile
: 
".sandcastle/implement.md"
,

 
maxIterations
: 
5
,

}
)
;

// Step 2: review on the same branch, same container

const
 
reviewResult
 
=
 
await
 
sandbox
.
run
(
{

 
agent
: 
claudeCode
(
"claude-sonnet-4-6"
)
,

 
prompt
: 
"Review the changes and fix any issues."
,

}
)
;

Commits from allrun()calls accumulate on the same branch. The sandbox container stays alive between runs, so installed dependencies and build artifacts persist.

#### Automatic cleanup withawait using

await usingcallssandbox.close()automatically when the block exits. If the sandbox has uncommitted changes, the worktree is preserved on disk; if clean, both container and worktree are removed.

#### Manualclose()withCloseResult

const
 
sandbox
 
=
 
await
 
createSandbox
(
{

 
branch
: 
"agent/fix-42"
,

 
sandbox
: 
docker
(
)
,

}
)
;

// ... run agents ...

const
 
closeResult
 
=
 
await
 
sandbox
.
close
(
)
;

if
 
(
closeResult
.
preservedWorktreePath
)
 
{

 
console
.
log
(
`Worktree preserved at 
${
closeResult
.
preservedWorktreePath
}
`
)
;

}

#### CreateSandboxOptions

Option

Type

Default

Description

branch

string

—

Required.
 Explicit branch for the sandbox

sandbox

SandboxProvider

—

Required.
 Sandbox provider (e.g. 
docker()
, 
podman()
)

cwd

string

process.cwd()

Host repo directory — relative paths resolve against 
process.cwd()

hooks

SandboxHooks

—

Lifecycle hooks (
host.*
, 
sandbox.*
) — run once at creation time

copyToWorktree

string[]

—

Host-relative file paths to copy into the sandbox at creation time

timeouts

Timeouts

—

Override default timeouts (e.g. 
{ copyToWorktreeMs: 120_000 }
)

#### Sandbox

Property / Method

Type

Description

branch

string

The branch the sandbox is on

worktreePath

string

Host path to the worktree

run(options)

(SandboxRunOptions) => Promise<SandboxRunResult>

Invoke an agent inside the existing sandbox

interactive(options)

(SandboxInteractiveOptions) => Promise<SandboxInteractiveResult>

Launch an interactive session in the sandbox

close()

() => Promise<CloseResult>

Tear down the container and sandbox

[Symbol.asyncDispose]

() => Promise<void>

Auto teardown via 
await using

#### SandboxRunOptions

Option

Type

Default

Description

agent

AgentProvider

—

Required.
 Agent provider (e.g. 
claudeCode("claude-opus-4-7")
)

prompt

string

—

Inline prompt (mutually exclusive with 
promptFile
)

promptFile

string

—

Path to prompt file (mutually exclusive with 
prompt
)

promptArgs

PromptArgs

—

Key-value map for 
{{KEY}}
 placeholder substitution

maxIterations

number

1

Maximum iterations to run

completionSignal

string | string[]

<promise>COMPLETE</promise>

String(s) the agent emits to stop the iteration loop early

idleTimeoutSeconds

number

600

Idle timeout in seconds — resets on each agent output event

name

string

—

Display name for the run

logging

object

file (auto-generated)

{ type: 'file', path }
 or 
{ type: 'stdout' }

signal

AbortSignal

—

Cancels the run when aborted; handle stays usable afterward

#### SandboxRunResult

Field

Type

Description

iterations

IterationResult[]

Per-iteration results (use 
.length
 for the count)

completionSignal

string?

The matched completion signal string, or 
undefined
 if none fired

stdout

string

Combined agent output from all iterations

commits

{ sha }[]

Commits created during the run

logFilePath

string?

Path to the log file (only when logging to a file)

#### CloseResult

Field

Type

Description

preservedWorktreePath

string?

Host path to the preserved worktree, set when it had uncommitted changes

### createWorktree()— independent worktree lifecycle

UsecreateWorktree()when you need a worktree (git worktree) as an independent, first-class concept — separate from any sandbox. This is useful when you want to run an interactive session first and then hand the same worktree to a sandboxed AFK agent.

Onlybranchandmerge-to-headstrategies are accepted;headis a compile-time type error since it means no worktree.

Passcwdto target a repo other thanprocess.cwd(). Relative paths resolve againstprocess.cwd(); absolute paths pass through. ACwdErroris thrown if the path does not exist or is not a directory.

import
 
{
 
createWorktree
 
}
 
from
 
"@ai-hero/sandcastle"
;

await
 using 
wt
 
=
 
await
 
createWorktree
(
{

 
branchStrategy
: 
{
 
type
: 
"branch"
,
 
branch
: 
"agent/fix-42"
 
}
,

 
copyToWorktree
: 
[
"node_modules"
]
,

 
cwd
: 
"/path/to/other-repo"
,
 
// optional — defaults to process.cwd()

}
)
;

console
.
log
(
wt
.
worktreePath
)
;
 
// host path to the worktree

console
.
log
(
wt
.
branch
)
;
 
// "agent/fix-42"

// Run an interactive session in the worktree (defaults to noSandbox)

await
 
wt
.
interactive
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
prompt
: 
"Explore the codebase and understand the bug."
,

}
)
;

// Run an AFK agent in the worktree (sandbox is required)

const
 
result
 
=
 
await
 
wt
.
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
{
 
imageName
: 
"sandcastle:myrepo"
 
}
)
,

 
prompt
: 
"Fix issue #42."
,

 
maxIterations
: 
3
,

}
)
;

console
.
log
(
result
.
commits
)
;
 
// commits made during the run

// Create a long-lived sandbox from the worktree

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

await
 using 
sandbox
 
=
 
await
 
wt
.
createSandbox
(
{

 
sandbox
: 
docker
(
)
,

 
hooks
: 
{
 
sandbox
: 
{
 
onSandboxReady
: 
[
{
 
command
: 
"npm install"
 
}
]
 
}
 
}
,

}
)
;

// sandbox.close() tears down the container only — the worktree stays

await
 
sandbox
.
close
(
)
;

// wt.close() cleans up the worktree

wt.close()checks for uncommitted changes: if the worktree is dirty, it's preserved on disk; if clean, it's removed.await usingcallsclose()automatically. The worktree persists afterrun(),interactive(), andcreateSandbox()complete, so you can hand it to another agent or inspect it.

Split ownership: When a sandbox is created viawt.createSandbox(),sandbox.close()tears down the container only — the worktree remains.wt.close()is responsible for worktree cleanup. This differs from the top-levelcreateSandbox(), wheresandbox.close()owns both container and worktree.

#### CreateWorktreeOptions

Option

Type

Default

Description

branchStrategy

WorktreeBranchStrategy

—

Required.
 
{ type: "branch", branch }
 or 
{ type: "merge-to-head" }

copyToWorktree

string[]

—

Host-relative file paths to copy into the worktree at creation time

timeouts

Timeouts

—

Override default timeouts (e.g. 
{ copyToWorktreeMs: 120_000 }
)

#### Worktree

Property / Method

Type

Description

branch

string

The branch the worktree is on

worktreePath

string

Host path to the worktree

run(options)

(options: WorktreeRunOptions) => Promise<WorktreeRunResult>

Run an AFK agent in the worktree (sandbox required)

interactive(options)

(options: WorktreeInteractiveOptions) => Promise<InteractiveResult>

Run an interactive agent session in the worktree

createSandbox(options)

(options: WorktreeCreateSandboxOptions) => Promise<Sandbox>

Create a long-lived sandbox backed by this worktree

close()

() => Promise<CloseResult>

Clean up the worktree (preserves if dirty)

[Symbol.asyncDispose]

() => Promise<void>

Auto cleanup via 
await using

#### WorktreeInteractiveOptions

Option

Type

Default

Description

agent

AgentProvider

—

Required.
 Agent provider

sandbox

AnySandboxProvider

noSandbox()

Sandbox provider (defaults to no sandbox)

prompt

string

—

Inline prompt (mutually exclusive with 
promptFile
)

promptFile

string

—

Path to prompt file

name

string

—

Optional session name

hooks

SandboxHooks

—

Lifecycle hooks (
host.*
, 
sandbox.*
)

promptArgs

PromptArgs

—

Key-value map for 
{{KEY}}
 placeholder substitution

env

Record<string, string>

—

Environment variables to inject into the sandbox

signal

AbortSignal

—

Cancel the session when aborted. The worktree is preserved on disk. Rejects with 
signal.reason
.

#### WorktreeRunOptions

Option

Type

Default

Description

agent

AgentProvider

—

Required.
 Agent provider

sandbox

SandboxProvider

—

Required.
 Sandbox provider (AFK agents must be sandboxed)

prompt

string

—

Inline prompt (mutually exclusive with 
promptFile
)

promptFile

string

—

Path to prompt file

maxIterations

number

1

Maximum iterations to run

completionSignal

string | string[]

—

Substring(s) to stop the iteration loop early

idleTimeoutSeconds

number

600

Idle timeout in seconds

name

string

—

Optional run name

logging

LoggingOption

file

Logging mode

hooks

SandboxHooks

—

Lifecycle hooks (
host.*
, 
sandbox.*
)

promptArgs

PromptArgs

—

Key-value map for 
{{KEY}}
 placeholder substitution

env

Record<string, string>

—

Environment variables to inject into the sandbox

resumeSession

string

—

Resume a prior Claude Code session by ID. Incompatible with 
maxIterations > 1
. Session file must exist on host.

signal

AbortSignal

—

Cancel the run when aborted. Kills the in-flight agent subprocess; the worktree is preserved on disk. Rejects with 
signal.reason
.

#### WorktreeRunResult

Property

Type

Description

iterations

IterationResult[]

Per-iteration results (use 
.length
 for the count)

completionSignal

string

The matched completion signal, or undefined

stdout

string

Combined stdout output from all agent iterations

commits

{ sha: string }[]

List of commits made by the agent during the run

branch

string

The branch name the agent worked on

logFilePath

string

Path to the log file, if logging was drained to a file

#### WorktreeCreateSandboxOptions

Option

Type

Default

Description

sandbox

SandboxProvider

—

Required.
 Sandbox provider (e.g. 
docker()
)

hooks

SandboxHooks

—

Lifecycle hooks (
host.*
, 
sandbox.*
)

copyToWorktree

string[]

—

Host-relative file paths to copy into the worktree at creation time

timeouts

Timeouts

—

Override default timeouts (e.g. 
{ copyToWorktreeMs: 120_000 }
)

## How it works

Sandcastle uses abranch strategyconfigured on the sandbox provider to control how the agent's changes relate to branches. There are three strategies:

* Head({ type: "head" }) — The agent writes directly to the host working directory. No worktree, no branch indirection. This is the default for bind-mount providers likedocker().
* Merge-to-head({ type: "merge-to-head" }) — Sandcastle creates a temporary branch in a git worktree. The agent works on the temp branch, and changes are merged back to HEAD when done. The temp branch is cleaned up after merge.
* Branch({ type: "branch", branch: "foo" }) — Commits land on an explicitly named branch in a git worktree.

For bind-mount providers (like Docker), the worktree directory is bind-mounted into the container — the agent writes directly to the host filesystem through the mount, so no sync is needed.

From your point of view, you just configurebranchStrategy: { type: 'branch', branch: 'foo' }onrun(), and get a commit on branchfooonce it's complete. All 100% local.

## Prompts

Sandcastle uses a flexible prompt system. You write the prompt, and the engine executes it — no opinions about workflow, task management, or context sources are imposed.

### Prompt resolution

You must provide exactly one of:

1. prompt: "inline string"— pass an inline prompt directly viaRunOptions
2. promptFile: "./path/to/prompt.md"— point to a specific file viaRunOptions

promptandpromptFileare mutually exclusive — providing both is an error. If neither is provided,run()throws an error asking you to supply one.

Inline prompts (prompt: "...") are passed to the agent literally.No{{KEY}}substitution, no!`command`expansion, no built-in{{SOURCE_BRANCH}}/{{TARGET_BRANCH}}injection. If you need values interpolated into an inline prompt, build the string in JavaScript (`Work on ${branch}…`). PassingpromptArgsalongside an inline prompt is an error — switch topromptFileto use substitution.

The substitution and expansion features below applyonlyto prompts sourced frompromptFile.

Convention:sandcastle initscaffolds.sandcastle/prompt.mdand all templates explicitly reference it viapromptFile: ".sandcastle/prompt.md". This is a convention, not an automatic fallback — Sandcastle does not read.sandcastle/prompt.mdunless you pass it aspromptFile.

### Dynamic context with!`command`

Use!`command`expressions in your prompt to pull in dynamic context. Each expression is replaced with the command's stdout before the prompt is sent to the agent. All expressions in a prompt runin parallelfor faster expansion.

Commands runinside the sandboxaftersandbox.onSandboxReadyhooks complete, so they see the same repo state the agent sees (including installed dependencies).

# 
Open issues

!
`
gh issue list --state open --label Sandcastle --json number,title,body,comments,labels --limit 20
`

# 
Recent commits

!
`
git log --oneline -10
`

If any command exits with a non-zero code, the run fails immediately with an error.

### Prompt arguments with{{KEY}}

Use{{KEY}}placeholders in your prompt to inject values from thepromptArgsoption. This is useful for reusing the same prompt file across multiple runs with different parameters.

import
 
{
 
run
 
}
 
from
 
"@ai-hero/sandcastle"
;

await
 
run
(
{

 
promptFile
: 
"./my-prompt.md"
,

 
promptArgs
: 
{
 
ISSUE_NUMBER
: 
42
,
 
PRIORITY
: 
"high"
 
}
,

}
)
;

In the prompt file:

Work on issue #{{ISSUE_NUMBER}} (priority: {{PRIORITY}}).

Prompt argument substitution runs on the host before shell expression expansion, so{{KEY}}placeholders inside!`command`expressions are replaced first:

!
`
gh issue view {{ISSUE_NUMBER}} --json body -q .body
`

A{{KEY}}placeholder with no matching prompt argument is an error. Unused prompt arguments produce a warning.

!`command`expansion only runs on shell blocks written in the prompt file itself. Any!`…`pattern that appears inside an argument value is treated as inert text — it won't be executed against the host shell. This makes it safe to pass user-authored content (issue titles, PR descriptions, docs excerpts) throughpromptArgs.

### Built-in prompt arguments

Sandcastle automatically injects two built-in prompt arguments into every prompt:

Placeholder

Value

{{SOURCE_BRANCH}}

The branch the agent works on (determined by the branch strategy)

{{TARGET_BRANCH}}

The host's active branch at 
run()
 time

Use them in your prompt without passing them viapromptArgs:

You are working on {{SOURCE_BRANCH}}. When diffing, compare against {{TARGET_BRANCH}}.

PassingSOURCE_BRANCHorTARGET_BRANCHinpromptArgsis an error — built-in prompt arguments cannot be overridden.

### Early termination with<promise>COMPLETE</promise>

When the agent outputs<promise>COMPLETE</promise>, the orchestrator stops the iteration loop early. This is a convention you document in your prompt for the agent to follow — the engine never injects it.

This is useful for task-based workflows where the agent should stop once it has finished, rather than running all remaining iterations.

You can override the default signal by passingcompletionSignaltorun(). It accepts a single string or an array of strings:

await
 
run
(
{

 
// ...

 
completionSignal
: 
"DONE"
,

}
)
;

// Or pass multiple signals — the loop stops on the first match:

await
 
run
(
{

 
// ...

 
completionSignal
: 
[
"TASK_COMPLETE"
,
 
"TASK_ABORTED"
]
,

}
)
;

Tell the agent to output your chosen string(s) in the prompt, and the orchestrator will stop when it detects any of them. The matched signal is returned asresult.completionSignal.

### Structured output

UseOutput.object()to extract a typed, schema-validated JSON payload from the agent's stdout. The agent emits its answer inside an XML tag you specify, and Sandcastle parses, validates, and returns it onresult.output. SeeADR 0010for design rationale.

import
 
{
 
run
,
 
Output
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

import
 
{
 
z
 
}
 
from
 
"zod"
;

const
 
result
 
=
 
await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
prompt
: 
`Analyze the code, and output the result as JSON inside <result> tags.

 The result must match this schema:

 { summary: string; score: string }

 `
,

 
output
: 
Output
.
object
(
{

 
tag
: 
"result"
,

 
schema
: 
z
.
object
(
{
 
summary
: 
z
.
string
(
)
,
 
score
: 
z
.
number
(
)
 
}
)
,

 
}
)
,

}
)
;

console
.
log
(
result
.
output
.
summary
)
;
 
// typed as string

console
.
log
(
result
.
output
.
score
)
;
 
// typed as number

Output.string({ tag })extracts the tag contents as a plain string (trimmed, no JSON parsing). Both helpers requiremaxIterationsto be1(the default). The resolved prompt must contain the configured opening tag literal.

### Templates

sandcastle initprompts you to choose a sandbox provider (Docker or Podman), a backlog manager (GitHub Issues or Beads), and a template, which scaffolds a ready-to-use prompt andmain.mtssuited to a specific workflow. If your project'spackage.jsonhas"type": "module", the file will be namedmain.tsinstead. Five templates are available:

Template

Description

blank

Bare scaffold — write your own prompt and orchestration

simple-loop

Picks issues one by one and closes them

sequential-reviewer

Implements issues one by one, with a code review step after each

parallel-planner

Plans parallelizable issues, executes on separate branches, then merges

parallel-planner-with-review

Plans parallelizable issues, executes with per-branch review, then merges

Select a template duringsandcastle initwhen prompted, or re-run init in a fresh repo to try a different one.

## CLI commands

### sandcastle init

Scaffolds the.sandcastle/config directory and builds the container image. This is the first command you run in a new repo. You choose a sandbox provider (Docker or Podman) during init — selecting Podman writes aContainerfileinstead ofDockerfileand usessandcastle podman build-imagefor the build step.

Option

Required

Default

Description

--image-name

No

sandcastle:<repo-dir-name>

Docker image name

--agent

No

Interactive prompt

Agent to use (
claude-code
, 
pi
, 
codex
, 
opencode
)

--model

No

Agent's default model

Model to use (e.g. 
claude-sonnet-4-6
). Defaults to agent's default

--template

No

Interactive prompt

Template to scaffold (e.g. 
blank
, 
simple-loop
)

Creates the following files:

.sandcastle/
├── Dockerfile # Sandbox environment (customize as needed)
├── prompt.md # Agent instructions
├── .env.example # Token placeholders
└── .gitignore # Ignores .env, logs/

Errors if.sandcastle/already exists to prevent overwriting customizations.

### sandcastle docker build-image

Rebuilds the Docker image from an existing.sandcastle/directory. Use this after modifying the Dockerfile. On Linux/macOS, the build automatically passes--build-arg AGENT_UID=$(id -u)andAGENT_GID=$(id -g)so the image'sagentuser matches the host UID — this prevents permission errors on image-built files without runtime chown.

Option

Required

Default

Description

--image-name

No

sandcastle:<repo-dir-name>

Docker image name

--dockerfile

No

—

Path to a custom Dockerfile (build context will be the current working directory)

### sandcastle docker remove-image

Removes the Docker image.

Option

Required

Default

Description

--image-name

No

sandcastle:<repo-dir-name>

Docker image name

### sandcastle podman build-image

Builds the Podman image from an existing.sandcastle/directory. Use this after modifying the Containerfile.

Option

Required

Default

Description

--image-name

No

sandcastle:<repo-dir-name>

Podman image name

--containerfile

No

—

Path to a custom Containerfile (build context will be the current working directory)

### sandcastle podman remove-image

Removes the Podman image.

Option

Required

Default

Description

--image-name

No

sandcastle:<repo-dir-name>

Podman image name

### RunOptions

Option

Type

Default

Description

agent

AgentProvider

—

Required.
 Agent provider (e.g. 
claudeCode("claude-opus-4-7")
, 
pi("claude-sonnet-4-6")
, 
codex("gpt-5.4-mini")
, 
opencode("opencode/big-pickle")
)

sandbox

SandboxProvider

—

Required.
 Sandbox provider (e.g. 
docker()
, 
podman()
, 
docker({ imageName: "sandcastle:local" })
)

cwd

string

process.cwd()

Host repo directory — anchor for 
.sandcastle/
 artifacts and git operations. Relative paths resolve against 
process.cwd()
.

prompt

string

—

Inline prompt (mutually exclusive with 
promptFile
)

promptFile

string

—

Path to prompt file (mutually exclusive with 
prompt
). Resolves against 
process.cwd()
, 
not
 
cwd
.

maxIterations

number

1

Maximum iterations to run

hooks

SandboxHooks

—

Lifecycle hooks (
host.*
, 
sandbox.*
)

name

string

—

Display name for the run, shown as a prefix in log output

promptArgs

PromptArgs

—

Key-value map for 
{{KEY}}
 placeholder substitution

branchStrategy

BranchStrategy

per-provider default

Branch strategy: 
{ type: 'head' }
, 
{ type: 'merge-to-head' }
, or 
{ type: 'branch', branch: '…' }

copyToWorktree

string[]

—

Host-relative file paths to copy into the sandbox before start (not supported with 
branchStrategy: { type: 'head' }
)

logging

object

file (auto-generated)

{ type: 'file', path }
 or 
{ type: 'stdout' }

completionSignal

string | string[]

<promise>COMPLETE</promise>

String or array of strings the agent emits to stop the iteration loop early

idleTimeoutSeconds

number

600

Idle timeout in seconds — resets on each agent output event

resumeSession

string

—

Resume a prior Claude Code session by ID. Incompatible with 
maxIterations > 1
. Session file must exist on host.

signal

AbortSignal

—

Cancel the run when aborted. Kills the in-flight agent subprocess and cancels lifecycle hooks; the worktree is preserved on disk. Rejects with 
signal.reason
.

timeouts

Timeouts

—

Override default timeouts for built-in lifecycle steps. Currently supports 
{ copyToWorktreeMs?: number }
 (default: 60 000).

output

OutputDefinition

—

Structured output definition (
Output.object(…)
 or 
Output.string(…)
). Requires 
maxIterations === 1
. See 
Structured output
.

### RunResult

Field

Type

Description

iterations

IterationResult[]

Per-iteration results (use 
.length
 for the count)

completionSignal

string?

The matched completion signal string, or 
undefined
 if none fired

stdout

string

Agent output

commits

{ sha }[]

Commits created during the run

branch

string

Target branch name

logFilePath

string?

Path to the log file (only when logging to a file)

output

T?

Typed structured output (only present when 
output
 option is set)

### IterationResult

Field

Type

Description

sessionId

string?

Claude Code session ID from the init line, or 
undefined
 for non-Claude agents

sessionFilePath

string?

Absolute host path to the captured session JSONL, or 
undefined
 when capture is off

usage

IterationUsage
?

Token usage snapshot from the last assistant message, or 
undefined
 when capture is off or provider does not support usage parsing

### IterationUsage

Field

Type

Description

inputTokens

number

Input tokens consumed

cacheCreationInputTokens

number

Tokens used to create prompt cache entries

cacheReadInputTokens

number

Tokens read from prompt cache

outputTokens

number

Output tokens generated

### Session capture

After each Claude Code iteration, Sandcastle automatically captures the agent's session JSONL from the sandbox to the host at~/.claude/projects/<encoded-path>/sessions/<session-id>.jsonl. Thecwdfields inside each JSONL entry are rewritten to match the host repo root, soclaude --resumeworks natively.

Session capture is enabled by default forclaudeCode()and can be opted out viacaptureSessions: false. Non-Claude agent providers never attempt capture. Capture failure fails the run.

### Session resume

PassresumeSessiontorun()to continue a prior Claude Code conversation inside a new sandbox:

const
 
result
 
=
 
await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
prompt
: 
"Continue where you left off"
,

 
resumeSession
: 
"abc-123-def"
,

}
)
;

Before the sandbox starts, Sandcastle validates that the session file exists on the host and transfers it into the sandbox withcwdfields rewritten to match the sandbox-side path. The Claude Code agent receives--resume <id>on its print command for iteration 1.

Constraints:

* resumeSessionis incompatible withmaxIterations > 1(throws before sandbox creation).
* The session file must exist at~/.claude/projects/<encoded-path>/sessions/<id>.jsonl(throws before sandbox creation).
* Only iteration 1 receives the resume flag; subsequent iterations (if any) start fresh.
* Non-Claude agent providers ignoreresumeSession.

### ClaudeCodeOptions

TheclaudeCode()factory accepts an optional second argument for provider-specific options:

agent: 
claudeCode
(
"claude-opus-4-7"
,
 
{
 
effort
: 
"high"
 
}
)
;

Option

Type

Default

Description

effort

"low"
 | 
"medium"
 | 
"high"
 | 
"max"

—

Claude Code reasoning effort level (
max
 is Opus only)

env

Record<string, string>

{}

Environment variables injected by this agent provider

captureSessions

boolean

true

Capture agent session JSONL to host for 
claude --resume

### CodexOptions

Thecodex()factory accepts an optional second argument for provider-specific options:

agent: 
codex
(
"gpt-5.4"
,
 
{
 
effort
: 
"high"
 
}
)
;

Option

Type

Default

Description

effort

"low"
 | 
"medium"
 | 
"high"
 | 
"xhigh"

—

Codex reasoning effort level via 
model_reasoning_effort

env

Record<string, string>

{}

Environment variables injected by this agent provider

### Providerenv

Bothagent providersandsandbox providersaccept an optionalenv: Record<string, string>in their options. These environment variables are merged with the.sandcastle/.envresolver output at launch time:

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
,
 
{

 
env
: 
{
 
ANTHROPIC_API_KEY
: 
"sk-ant-..."
 
}
,

 
}
)
,

 
sandbox
: 
docker
(
{

 
env
: 
{
 
DOCKER_SPECIFIC_VAR
: 
"value"
 
}
,

 
}
)
,

 
prompt
: 
"Fix issue #42"
,

}
)
;

Merge rules:

* Provider env (agent + sandbox) overrides.sandcastle/.envresolver output for shared keys
* Agent provider env and sandbox provider envmust not overlap— if they share any key,run()throws an error
* Whenenvis not provided, it defaults to{}

Environment variables are also resolved automatically from.sandcastle/.envandprocess.env— no need to pass them to the API. The required variables depend on theagent provider(seesandcastle initoutput for details).

## Custom Sandbox Providers

Sandcastle ships with built-in providers for Docker, Podman, and Vercel, but you can create your own. A sandbox provider tells Sandcastle how to execute commands in an isolated environment. There are two kinds:

* Bind-mount— the sandbox can mount a host directory. Sandcastle creates a worktree on the host and the provider mounts it in. No file sync needed. Use this for Docker, Podman, or any local container runtime.
* Isolated— the sandbox has its own filesystem (e.g. a cloud VM). The provider handles syncing code in and out viacopyInandcopyFileOut. Use this when the sandbox cannot access the host filesystem.

### The sandbox handle contract

Both provider types return asandbox handlefrom theircreate()function. The handle exposes:

Method

Required

Description

exec

Both

Run a command, optionally streaming stdout line-by-line via 
options.onLine

close

Both

Tear down the sandbox

copyFileIn

Bind-mount

Copy a single file from the host into the sandbox

copyFileOut

Both

Copy a single file from the sandbox to the host

copyIn

Isolated

Copy a file or directory from the host into the sandbox

worktreePath

Both

Absolute path to the repo directory inside the sandbox

### ExecResult

Everyexeccall returns anExecResult:

interface
 
ExecResult
 
{

 
readonly
 
stdout
: 
string
;

 
readonly
 
stderr
: 
string
;

 
readonly
 
exitCode
: 
number
;

}

### Bind-mount provider example

A minimal bind-mount provider that shells out to local processes (no container):

import
 
{

 
createBindMountSandboxProvider
,

 
type
 
BindMountCreateOptions
,

 
type
 
BindMountSandboxHandle
,

 
type
 
ExecResult
,

}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
execFile
,
 
spawn
 
}
 
from
 
"node:child_process"
;

import
 
{
 
copyFile
 
as
 
fsCopyFile
,
 
mkdir
 
as
 
fsMkdir
 
}
 
from
 
"node:fs/promises"
;

import
 
{
 
dirname
 
}
 
from
 
"node:path"
;

import
 
{
 
createInterface
 
}
 
from
 
"node:readline"
;

const
 
localProcess
 
=
 
(
)
 
=>

 
createBindMountSandboxProvider
(
{

 
name
: 
"local-process"
,

 
create
: 
async
 
(

 
options
: 
BindMountCreateOptions
,

 
)
: 
Promise
<
BindMountSandboxHandle
>
 
=>
 
{

 
const
 
worktreePath
 
=
 
options
.
worktreePath
;

 
return
 
{

 worktreePath
,

 
exec
: 
(

 
command
: 
string
,

 
opts
?: 
{
 
onLine
?: 
(
line
: 
string
)
 
=>
 
void
;
 
cwd
?: 
string
 
}
,

 
)
: 
Promise
<
ExecResult
>
 
=>
 
{

 
if
 
(
opts
?.
onLine
)
 
{

 
const
 
onLine
 
=
 
opts
.
onLine
;

 
return
 
new
 
Promise
(
(
resolve
,
 
reject
)
 
=>
 
{

 
const
 
proc
 
=
 
spawn
(
"sh"
,
 
[
"-c"
,
 
command
]
,
 
{

 
cwd
: 
opts
?.
cwd
 
??
 
worktreePath
,

 
stdio
: 
[
"ignore"
,
 
"pipe"
,
 
"pipe"
]
,

 
}
)
;

 
const
 
stdoutChunks
: 
string
[
]
 
=
 
[
]
;

 
const
 
stderrChunks
: 
string
[
]
 
=
 
[
]
;

 
const
 
rl
 
=
 
createInterface
(
{
 
input
: 
proc
.
stdout
!
 
}
)
;

 
rl
.
on
(
"line"
,
 
(
line
)
 
=>
 
{

 
stdoutChunks
.
push
(
line
)
;

 
onLine
(
line
)
;
 
// forward each line to Sandcastle

 
}
)
;

 
proc
.
stderr
!
.
on
(
"data"
,
 
(
chunk
: 
Buffer
)
 
=>
 
{

 
stderrChunks
.
push
(
chunk
.
toString
(
)
)
;

 
}
)
;

 
proc
.
on
(
"error"
,
 
(
err
)
 
=>
 
reject
(
err
)
)
;

 
proc
.
on
(
"close"
,
 
(
code
)
 
=>
 
{

 
resolve
(
{

 
stdout
: 
stdoutChunks
.
join
(
"\n"
)
,

 
stderr
: 
stderrChunks
.
join
(
""
)
,

 
exitCode
: 
code
 
??
 
0
,

 
}
)
;

 
}
)
;

 
}
)
;

 
}

 
return
 
new
 
Promise
(
(
resolve
,
 
reject
)
 
=>
 
{

 
execFile
(

 
"sh"
,

 
[
"-c"
,
 
command
]
,

 
{
 
cwd
: 
opts
?.
cwd
 
??
 
worktreePath
,
 
maxBuffer
: 
10
 
*
 
1024
 
*
 
1024
 
}
,

 
(
error
,
 
stdout
,
 
stderr
)
 
=>
 
{

 
if
 
(
error
 
&&
 
error
.
code
 
===
 
undefined
)
 
{

 
reject
(
new
 
Error
(
`exec failed: 
${
error
.
message
}
`
)
)
;

 
}
 
else
 
{

 
resolve
(
{

 
stdout
: 
stdout
.
toString
(
)
,

 
stderr
: 
stderr
.
toString
(
)
,

 
exitCode
: 
typeof
 
error
?.
code
 
===
 
"number"
 ? 
error
.
code
 : 
0
,

 
}
)
;

 
}

 
}
,

 
)
;

 
}
)
;

 
}
,

 
copyFileIn
: 
async
 
(
hostPath
: 
string
,
 
sandboxPath
: 
string
)
 
=>
 
{

 
await
 
fsMkdir
(
dirname
(
sandboxPath
)
,
 
{
 
recursive
: 
true
 
}
)
;

 
await
 
fsCopyFile
(
hostPath
,
 
sandboxPath
)
;

 
}
,

 
copyFileOut
: 
async
 
(
sandboxPath
: 
string
,
 
hostPath
: 
string
)
 
=>
 
{

 
await
 
fsMkdir
(
dirname
(
hostPath
)
,
 
{
 
recursive
: 
true
 
}
)
;

 
await
 
fsCopyFile
(
sandboxPath
,
 
hostPath
)
;

 
}
,

 
close
: 
async
 
(
)
 
=>
 
{

 
// nothing to tear down for a local process

 
}
,

 
}
;

 
}
,

 
}
)
;

### Isolated provider example

A minimal isolated provider using a temp directory:

import
 
{

 
createIsolatedSandboxProvider
,

 
type
 
IsolatedSandboxHandle
,

 
type
 
ExecResult
,

}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
execFile
,
 
spawn
 
}
 
from
 
"node:child_process"
;

import
 
{
 
copyFile
,
 
mkdir
,
 
mkdtemp
,
 
rm
 
}
 
from
 
"node:fs/promises"
;

import
 
{
 
tmpdir
 
}
 
from
 
"node:os"
;

import
 
{
 
dirname
,
 
join
 
}
 
from
 
"node:path"
;

import
 
{
 
createInterface
 
}
 
from
 
"node:readline"
;

const
 
tempDir
 
=
 
(
)
 
=>

 
createIsolatedSandboxProvider
(
{

 
name
: 
"temp-dir"
,

 
create
: 
async
 
(
)
: 
Promise
<
IsolatedSandboxHandle
>
 
=>
 
{

 
const
 
root
 
=
 
await
 
mkdtemp
(
join
(
tmpdir
(
)
,
 
"sandbox-"
)
)
;

 
const
 
worktreePath
 
=
 
join
(
root
,
 
"workspace"
)
;

 
await
 
mkdir
(
worktreePath
,
 
{
 
recursive
: 
true
 
}
)
;

 
return
 
{

 worktreePath
,

 
exec
: 
(

 
command
: 
string
,

 
opts
?: 
{
 
onLine
?: 
(
line
: 
string
)
 
=>
 
void
;
 
cwd
?: 
string
 
}
,

 
)
: 
Promise
<
ExecResult
>
 
=>
 
{

 
if
 
(
opts
?.
onLine
)
 
{

 
const
 
onLine
 
=
 
opts
.
onLine
;

 
return
 
new
 
Promise
(
(
resolve
,
 
reject
)
 
=>
 
{

 
const
 
proc
 
=
 
spawn
(
"sh"
,
 
[
"-c"
,
 
command
]
,
 
{

 
cwd
: 
opts
?.
cwd
 
??
 
worktreePath
,

 
stdio
: 
[
"ignore"
,
 
"pipe"
,
 
"pipe"
]
,

 
}
)
;

 
const
 
stdoutChunks
: 
string
[
]
 
=
 
[
]
;

 
const
 
stderrChunks
: 
string
[
]
 
=
 
[
]
;

 
const
 
rl
 
=
 
createInterface
(
{
 
input
: 
proc
.
stdout
!
 
}
)
;

 
rl
.
on
(
"line"
,
 
(
line
)
 
=>
 
{

 
stdoutChunks
.
push
(
line
)
;

 
onLine
(
line
)
;

 
}
)
;

 
proc
.
stderr
!
.
on
(
"data"
,
 
(
chunk
: 
Buffer
)
 
=>
 
{

 
stderrChunks
.
push
(
chunk
.
toString
(
)
)
;

 
}
)
;

 
proc
.
on
(
"error"
,
 
(
err
)
 
=>
 
reject
(
err
)
)
;

 
proc
.
on
(
"close"
,
 
(
code
)
 
=>
 
{

 
resolve
(
{

 
stdout
: 
stdoutChunks
.
join
(
"\n"
)
,

 
stderr
: 
stderrChunks
.
join
(
""
)
,

 
exitCode
: 
code
 
??
 
0
,

 
}
)
;

 
}
)
;

 
}
)
;

 
}

 
return
 
new
 
Promise
(
(
resolve
,
 
reject
)
 
=>
 
{

 
execFile
(

 
"sh"
,

 
[
"-c"
,
 
command
]
,

 
{
 
cwd
: 
opts
?.
cwd
 
??
 
worktreePath
,
 
maxBuffer
: 
10
 
*
 
1024
 
*
 
1024
 
}
,

 
(
error
,
 
stdout
,
 
stderr
)
 
=>
 
{

 
if
 
(
error
 
&&
 
error
.
code
 
===
 
undefined
)
 
{

 
reject
(
new
 
Error
(
`exec failed: 
${
error
.
message
}
`
)
)
;

 
}
 
else
 
{

 
resolve
(
{

 
stdout
: 
stdout
.
toString
(
)
,

 
stderr
: 
stderr
.
toString
(
)
,

 
exitCode
: 
typeof
 
error
?.
code
 
===
 
"number"
 ? 
error
.
code
 : 
0
,

 
}
)
;

 
}

 
}
,

 
)
;

 
}
)
;

 
}
,

 
copyIn
: 
async
 
(
hostPath
: 
string
,
 
sandboxPath
: 
string
)
 
=>
 
{

 
const
 
info
 
=
 
await
 
stat
(
hostPath
)
;

 
if
 
(
info
.
isDirectory
(
)
)
 
{

 
await
 
cp
(
hostPath
,
 
sandboxPath
,
 
{
 
recursive
: 
true
 
}
)
;

 
}
 
else
 
{

 
await
 
mkdir
(
dirname
(
sandboxPath
)
,
 
{
 
recursive
: 
true
 
}
)
;

 
await
 
copyFile
(
hostPath
,
 
sandboxPath
)
;

 
}

 
}
,

 
copyFileOut
: 
async
 
(
sandboxPath
: 
string
,
 
hostPath
: 
string
)
 
=>
 
{

 
await
 
mkdir
(
dirname
(
hostPath
)
,
 
{
 
recursive
: 
true
 
}
)
;

 
await
 
copyFile
(
sandboxPath
,
 
hostPath
)
;

 
}
,

 
close
: 
async
 
(
)
 
=>
 
{

 
await
 
rm
(
root
,
 
{
 
recursive
: 
true
,
 
force
: 
true
 
}
)
;

 
}
,

 
}
;

 
}
,

 
}
)
;

### Branch strategies

A branch strategy controls where the agent's commits land. Configure it when constructing the provider:

Strategy

Behavior

Bind-mount

Isolated

head

Agent writes directly to the host working directory. No worktree created

Default

N/A

merge-to-head

Sandcastle creates a temp branch, merges back to HEAD when done

Supported

Default

branch

Commits land on an explicit named branch you provide

Supported

Supported

When to use each:

* head— fast iteration during development. No branch indirection, no merge step. Only works with bind-mount providers since the agent needs direct host filesystem access.
* merge-to-head— safe default for automation. The agent works on a throwaway branch; if something goes wrong, HEAD is untouched. Use this for CI or unattended runs.
* branch— when you want commits on a specific branch (e.g. for a PR). Pass{ type: "branch", branch: "agent/fix-42" }.

Branch strategy is now configured onrun(), not on the provider:

import
 
{
 
run
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

import
 
{
 
docker
 
}
 
from
 
"@ai-hero/sandcastle/sandboxes/docker"
;

// head — direct write, bind-mount only (default for bind-mount providers)

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
prompt
: 
"…"
,

}
)
;

// merge-to-head — temp branch, merge back (default for isolated providers)

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
tempDir
(
)
,

 
prompt
: 
"…"
,

}
)
;

// branch — explicit named branch

await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
docker
(
)
,

 
branchStrategy
: 
{
 
type
: 
"branch"
,
 
branch
: 
"agent/fix-42"
 
}
,

 
prompt
: 
"…"
,

}
)
;

### Passing torun()

Pass your custom provider via thesandboxoption — it works the same as the built-indocker()provider:

import
 
{
 
run
,
 
claudeCode
 
}
 
from
 
"@ai-hero/sandcastle"
;

const
 
result
 
=
 
await
 
run
(
{

 
agent
: 
claudeCode
(
"claude-opus-4-7"
)
,

 
sandbox
: 
localProcess
(
)
,
 
// your custom provider

 
prompt
: 
"Fix issue #42 in this repo."
,

}
)
;

### Reference implementations

For real-world examples, see:

* src/sandboxes/docker.ts— bind-mount provider using Docker containers (with SELinux label support)
* src/sandboxes/vercel.ts— isolated provider using Vercel Firecracker microVMs via@vercel/sandbox
* src/sandboxes/podman.ts— bind-mount provider using Podman containers (with SELinux label support)
* src/sandboxes/test-isolated.ts— isolated provider using temp directories (used in tests)

## Configuration

### Config directory (.sandcastle/)

All per-repo sandbox configuration lives in.sandcastle/. Runsandcastle initto create it.

### Custom Dockerfile

The.sandcastle/Dockerfilecontrols the sandbox environment. The default template installs:

* Node.js 22(base image)
* git,curl,jq(system dependencies)
* GitHub CLI(gh)
* Claude Code CLI
* A non-rootagentuser (required — Claude runs as this user)

When customizing the Dockerfile, ensure you keep:

* A non-root user (the defaultagentuser) for Claude to run as
* git(required for commits and branch operations)
* gh(required for issue fetching)
* Claude Code CLI installed and on PATH

Add your project-specific dependencies (e.g., language runtimes, build tools) to the Dockerfile as needed.

### Hooks

Hooks are grouped bywherethey run —host(on the developer's machine) orsandbox(inside the container):

hooks: 
{

 
host
: 
{

 
onWorktreeReady
: 
[
{
 
command
: 
"cp .env.example .env"
 
}
]
,

 
onSandboxReady
: 
[
{
 
command
: 
"echo sandbox is up"
 
}
]
,

 
}
,

 
sandbox
: 
{

 
onSandboxReady
: 
[

 
{
 
command
: 
"npm install"
,
 
timeoutMs
: 
300_000
 
}
,

 
{
 
command
: 
"apt-get install -y ffmpeg"
,
 
sudo
: 
true
 
}
,

 
]
,

 
}
,

}

Hook

Runs on

When

Working directory

host.onWorktreeReady

Host

After 
copyToWorktree
, before sandbox start

Worktree path (host repo root under 
head
)

host.onSandboxReady

Host

After sandbox is up

Worktree path (host repo root under 
head
)

sandbox.onSandboxReady

Sandbox

After sandbox is up

Sandbox repo directory

Ordering:copyToWorktree->host.onWorktreeReady(sequential) -> sandbox created ->host.onSandboxReady+sandbox.onSandboxReady(parallel).

* Host hooksaccept{ command: string; timeoutMs?: number }— nosudo, nocwd. Usecdor inline env in the command string.
* Sandbox hooksaccept{ command: string; sudo?: boolean; timeoutMs?: number }— setsudo: truefor elevated privileges.
* timeoutMsoverrides the default 60 s per-hook timeout. Useful for long-running setup commands like dependency installs (e.g.timeoutMs: 300_000for 5 minutes).
* Within each hook point, sandbox hooks run in parallel; host hooks withinonSandboxReadyalso run in parallel with sandbox hooks.host.onWorktreeReadyhooks run sequentially in declared order.
* If any hook exits non-zero, setup fails fast.
* When asignalis passed torun(), it is threaded to all hooks — aborting the signal cancels any in-flight hook commands.

## Development

npm install
npm run build 
#
 Build with tsgo

npm 
test
 
#
 Run tests with vitest

npm run typecheck 
#
 Type-check

## License

MIT

## About

Orchestrate sandboxed coding agents in TypeScript with sandcastle.run()

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.8k

 stars
 

### Watchers

12

 watching
 

### Forks

512

 forks
 

 Report repository

 

## Releases30

v0.5.11

 Latest

 

May 20, 2026

 

+ 29 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript99.8%
* Other0.2%