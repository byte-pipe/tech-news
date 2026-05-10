---
title: 'GitHub - withastro/flue: The sandbox agent framework. · GitHub'
url: https://github.com/withastro/flue
site_name: github
content_file: github-github-withastroflue-the-sandbox-agent-framework-g
fetched_at: '2026-05-10T19:58:44.088047'
original_url: https://github.com/withastro/flue
author: withastro
description: The sandbox agent framework. Contribute to withastro/flue development by creating an account on GitHub.
---

withastro

 

/

flue

Public

* NotificationsYou must be signed in to change notification settings
* Fork158
* Star3k

 
 
 
 
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

220 Commits
220 Commits
.github
.github
 
 
apps/
www
apps/
www
 
 
connectors
connectors
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.jsonc
biome.jsonc
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
prettier.config.js
prettier.config.js
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
turbo.jsonc
turbo.jsonc
 
 
View all files

## Repository files navigation

Experimental— Flue is under active development. APIs may change.

Looking forv0.0.x?See here.

# Flue

Flue isThe Agent Harness Framework.If you know how to use Claude Code (or Codex, OpenCode, Pi, etc)... then you already know the basics of how to build agents with Flue.

Flue is a TypeScript framework for building the next generation of agents, designed around a built-inagent harness. It's like Claude Code, but 100% headless and programmable. There's no baked-in assumption like requiring a human operator to function. No TUI. No GUI. Just TypeScript.

But using Flue feels like using Claude Code. The agents you build act autonomously to solve problems and complete tasks. They require very little code to run — most of the "logic" lives in Markdown: skills, context, andAGENTS.md.

Flue isn't another AI SDK. It's a proper runtime-agnostic framework — think Astro or Next.js, but for agents. Write once, build, and deploy your agents anywhere (Node.js, Cloudflare, GitHub Actions, GitLab CI/CD, etc).

## Packages

Package

Description

@flue/sdk

Core SDK: build system, sessions, tools

@flue/cli

CLI for building and running agents

## Examples

### Quickstart

The simplest agent — no container, no tools, just a prompt and a typed result.

Unless you opt-in to initializing a full container sandbox, Flue will default to a virtual sandbox for every agent, powered byjust-bash. A virtual sandbox is going to be dramatically faster, cheaper, and more scalable than running a full container for every agent, which makes it perfect for building high-traffic/high-scale agents.

// .flue/agents/hello-world.ts

import
 
type
 
{
 
FlueContext
 
}
 
from
 
'@flue/sdk/client'
;

import
 
*
 
as
 
v
 
from
 
'valibot'
;

// Every agent needs a trigger. This agent is invoked as an API endpoint, via HTTP.

export
 
const
 
triggers
 
=
 
{
 
webhook
: 
true
 
}
;

// The agent handler. Where the orchestration of the agent lives.

export
 
default
 
async
 
function
 
(
{
 init
,
 payload 
}
: 
FlueContext
)
 
{

 
// `agent` -- Your initialized agent runtime including sandbox, tools, skills, etc.

 
const
 
agent
 
=
 
await
 
init
(
{
 
model
: 
'anthropic/claude-sonnet-4-6'
 
}
)
;

 
const
 
session
 
=
 
await
 
agent
.
session
(
)
;

 
// prompt() sends a message in the session, triggering action.

 
const
 
{
 data 
}
 
=
 
await
 
session
.
prompt
(
`Translate this to 
${
payload
.
language
}
: "
${
payload
.
text
}
"`
,
 
{

 
// Pass a `schema` to get typed, schema-validated data back from your agent.

 
schema
: 
v
.
object
(
{

 
translation
: 
v
.
string
(
)
,

 
confidence
: 
v
.
picklist
(
[
'low'
,
 
'medium'
,
 
'high'
]
)
,

 
}
)
,

 
}
)
;

 
return
 
data
;

}

### Support Agent

A support agent can also run in a virtual sandbox, but we now add a file-system using an R2 bucket. The knowledge base is stored in R2 and mounted directly into the agent's filesystem — the agent searches it with its built-in tools (grep, glob, read). Skills are also defined in the bucket that help the agent perform its task.

Because this agent is deployed to Cloudflare, message history and session state are automatically persisted for you. So you (or your customer) can revisit this support session days, weeks, or years later and pick up exactly where you left off.

// .flue/agents/support.ts

import
 
{
 
getVirtualSandbox
 
}
 
from
 
'@flue/sdk/cloudflare'
;

import
 
type
 
{
 
FlueContext
 
}
 
from
 
'@flue/sdk/client'
;

import
 
*
 
as
 
v
 
from
 
'valibot'
;

export
 
const
 
triggers
 
=
 
{
 
webhook
: 
true
 
}
;

export
 
default
 
async
 
function
 
(
{
 init
,
 payload
,
 env 
}
: 
FlueContext
)
 
{

 
// Mount the R2 knowledge base bucket as the agent's filesystem.

 
// The agent can grep, glob, and read articles with bash, but

 
// without needing to spin up an entire container sandbox.

 
const
 
sandbox
 
=
 
await
 
getVirtualSandbox
(
env
.
KNOWLEDGE_BASE
)
;

 
const
 
agent
 
=
 
await
 
init
(
{
 sandbox
,
 
model
: 
'openrouter/moonshotai/kimi-k2.6'
 
}
)
;

 
const
 
session
 
=
 
await
 
agent
.
session
(
)
;

 
return
 
await
 
session
.
prompt
(

 
`You are a support agent. Search the knowledge base for articles

 relevant to this request, then write a helpful response.

 Customer: 
${
payload
.
message
}
`
,

 
{

 
// Provide roles (aka subagents) to guide your agent. Defined in .flue/roles/

 
role
: 
'triager'
,

 
}
,

 
)
;

}

### Issue Triage (CI)

A triage agent that runs in CI whenever an issue is opened on GitHub. The"local"sandbox gives the agent direct access to the host filesystem and shell — perfect for CI runners, wheregh,git, andnpmare already on$PATHand the runner itself is your isolation boundary.

// .flue/agents/triage.ts

import
 
{
 
type
 
FlueContext
 
}
 
from
 
'@flue/sdk/client'
;

import
 
*
 
as
 
v
 
from
 
'valibot'
;

// Because we are running this in CI, we don't need to expose this as an HTTP endpoint.

// The CLI can run any agent from the command line, `flue run triage ...`

export
 
const
 
triggers
 
=
 
{
}
;

export
 
default
 
async
 
function
 
(
{
 init
,
 payload 
}
: 
FlueContext
)
 
{

 
// 'local' gives the agent direct access to the host filesystem and

 
// shell. The agent's bash tool can run `gh`, `git`, `npm` directly.

 
// Skills and AGENTS.md are discovered from process.cwd().

 
//

 
// `model` sets the default model for every prompt/skill call in this

 
// agent. Override per-call with `{ model: '...' }` on prompt()/skill().

 
const
 
agent
 
=
 
await
 
init
(
{

 
sandbox
: 
'local'
,

 
model
: 
'anthropic/claude-opus-4-7'
,

 
}
)
;

 
const
 
session
 
=
 
await
 
agent
.
session
(
)
;

 
// Skills can be referenced either by their frontmatter `name:` (shown below)

 
// or by a relative path under `.agents/skills/` — e.g.

 
// `session.skill('triage/reproduce.md', ...)`. Path references are handy for

 
// skill packs that group multiple stages under one directory.

 
const
 
{
 data 
}
 
=
 
await
 
session
.
skill
(
'triage'
,
 
{

 
// Pass arguments to any prompt or skill.

 
args
: 
{
 
issueNumber
: 
payload
.
issueNumber
 
}
,

 
// Schemas are great for being able to act/orchestrate based on

 
// the structured `data` returned from your prompt or skill call.

 
schema
: 
v
.
object
(
{

 
severity
: 
v
.
picklist
(
[
'low'
,
 
'medium'
,
 
'high'
,
 
'critical'
]
)
,

 
reproducible
: 
v
.
boolean
(
)
,

 
summary
: 
v
.
string
(
)
,

 
fix_applied
: 
v
.
boolean
(
)
,

 
}
)
,

 
}
)
;

 
return
 
data
;

}

### Coding Agent (Remote Sandbox)

The examples above all run on a lightweight virtual sandbox — no container needed. But for a full coding agent, you want a real Linux environment with git, Node.js, a browser, and a cloned repo ready to go.

Daytona's declarative image builder lets you define the environment in code. The image is cached after the first build, so subsequent sessions start instantly.

Install the Daytona connector withflue add daytona | <your-agent>(e.g.claude,opencode,codex,cursor-agent). It writes a smallconnectors/daytona.tsadapter into your project that you import directly.

// .flue/agents/code.ts

import
 
{
 
Type
,
 
type
 
FlueContext
,
 
type
 
ToolDef
 
}
 
from
 
'@flue/sdk/client'
;

import
 
{
 
Daytona
 
}
 
from
 
'@daytona/sdk'
;

import
 
{
 
daytona
 
}
 
from
 
'../connectors/daytona'
;

export
 
const
 
triggers
 
=
 
{
 
webhook
: 
true
 
}
;

export
 
default
 
async
 
function
 
(
{
 init
,
 payload
,
 env 
}
: 
FlueContext
)
 
{

 
// Each agent gets a real container via Daytona. The container has

 
// a full Linux environment with persistent filesystem and shell.

 
//

 
// For simplicity, we always create a new sandbox here. You could also

 
// first check for an existing sandbox for the agent id, and reuse that

 
// instead to best pick up where you last left off in the conversation.

 
const
 
client
 
=
 
new
 
Daytona
(
{
 
apiKey
: 
env
.
DAYTONA_API_KEY
 
}
)
;

 
const
 
sandbox
 
=
 
await
 
client
.
create
(
)
;

 
const
 
setupAgent
 
=
 
await
 
init
(
{

 
sandbox
: 
daytona
(
sandbox
)
,

 
model
: 
'openai/gpt-5.5'
,

 
}
)
;

 
const
 
setup
 
=
 
await
 
setupAgent
.
session
(
)
;

 
// For simplicity, we clone the target repo into the sandbox here.

 
// You could also bake these into the container image snapshot for a

 
// faster / near-instant startup.

 
await
 
setup
.
shell
(
`git clone 
${
payload
.
repo
}
 /workspace/project`
)
;

 
await
 
setup
.
shell
(
'npm install'
,
 
{
 
cwd
: 
'/workspace/project'
 
}
)
;

 
// Start a second agent in the cloned repo. It shares the same sandbox, but

 
// discovers AGENTS.md and skills from /workspace/project.

 
const
 
projectAgent
 
=
 
await
 
init
(
{

 
id
: 
'project'
,

 
sandbox
: 
daytona
(
sandbox
)
,

 
cwd
: 
'/workspace/project'
,

 
model
: 
'openai/gpt-5.5'
,

 
}
)
;

 
const
 
session
 
=
 
await
 
projectAgent
.
session
(
)
;

 
// Coding agents don't hide the agent DX from the user, so no need to

 
// wrap the user's prompt in anything. Just send it to the agent directly

 
// and then stream back the progress and final results.

 
return
 
await
 
session
.
prompt
(
payload
.
prompt
)
;

}

### Remote MCP Tools

MCP is available as a runtime tool adapter. Connect to a remote MCP server in trusted code, pass its tools toinit(), and keep secrets inenvinstead of filesystem context or prompts.

// .flue/agents/assistant.ts

import
 
{
 
connectMcpServer
,
 
type
 
FlueContext
 
}
 
from
 
'@flue/sdk/client'
;

export
 
const
 
triggers
 
=
 
{
 
webhook
: 
true
 
}
;

export
 
default
 
async
 
function
 
(
{
 init
,
 payload
,
 env 
}
: 
FlueContext
)
 
{

 
const
 
github
 
=
 
await
 
connectMcpServer
(
'github'
,
 
{

 
url
: 
'https://mcp.github.com/mcp'
,

 
headers
: 
{

 
Authorization
: 
`Bearer 
${
env
.
GITHUB_TOKEN
}
`
,

 
}
,

 
}
)
;

 
try
 
{

 
const
 
agent
 
=
 
await
 
init
(
{

 
model
: 
'anthropic/claude-sonnet-4-6'
,

 
tools
: 
github
.
tools
,

 
}
)
;

 
const
 
session
 
=
 
await
 
agent
.
session
(
)
;

 
return
 
await
 
session
.
prompt
(
payload
.
prompt
)
;

 
}
 
finally
 
{

 
await
 
github
.
close
(
)
;

 
}

}

connectMcpServer()defaults to modern streamable HTTP. For legacy SSE servers, passtransport: 'sse'. Flue does not auto-detect transports, spawn local stdio MCP servers, or handle OAuth callbacks in this first version.

## Agents And Sessions

Every agent invocation runs inside an initialized agent runtime. For HTTP agents, the agent ID is the last path segment:

POST /agents/<agent-name>/<id>

By default,agent.session()opens the default session for that agent ID. Reuse the same agent ID to continue the same default conversation. Use a new agent ID to start fresh.

#
 Start a conversation (port 3583 is `flue dev`'s default)

curl http://localhost:3583/agents/hello/session-abc \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{"name": "Alice"}
'

#
 Continue that conversation

curl http://localhost:3583/agents/hello/session-abc \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{"name": "Alice"}
'

#
 Start a separate conversation

curl http://localhost:3583/agents/hello/session-xyz \
 -H 
"
Content-Type: application/json
"
 \
 -d 
'
{"name": "Alice"}
'

Agents own sandbox state such as files written during a run. Sessions persist message history and conversation metadata inside an agent. On Cloudflare, session data is backed by Durable Objects and survives across requests. On Node.js, sessions are stored in memory by default unless you provide a custom store.

In production, generate a stable agent ID for the sandbox/runtime scope you want to preserve. Useagent.session(threadId)when you need multiple conversations inside the same agent.

### Tasks

Usesession.task()to run a focused, one-shot child agent in a detached session. Tasks share the same sandbox/filesystem, but get their own message history and discoverAGENTS.mdplus.agents/skills/from their working directory. The sametasktool is also available to the LLM duringprompt()andskill()calls, so the agent can delegate parallel research or exploration work itself.

const
 
session
 
=
 
await
 
agent
.
session
(
)
;

const
 
research
 
=
 
await
 
session
.
task
(
'Research the auth flow and summarize the key files.'
,
 
{

 
cwd
: 
'/workspace/project'
,

 
role
: 
'researcher'
,

}
)
;

const
 
answer
 
=
 
await
 
session
.
prompt
(

 
`Use this research to draft the implementation plan:\n\n
${
research
.
text
}
`
,

)
;

Roles can be set at the agent, session, or call level. Precedence iscall role > session role > agent role. Role instructions are applied as call-scoped system prompt overlays, not injected into the persisted user message history.

const
 
agent
 
=
 
await
 
init
(
{
 
model
: 
'anthropic/claude-sonnet-4-6'
,
 
role
: 
'coder'
 
}
)
;

const
 
session
 
=
 
await
 
agent
.
session
(
'review-thread'
,
 
{
 
role
: 
'reviewer'
 
}
)
;

await
 
session
.
prompt
(
'Review the latest changes.'
)
;
 
// uses reviewer

await
 
session
.
task
(
'Research related issues.'
,
 
{
 
role
: 
'researcher'
 
}
)
;
 
// uses researcher

### Provider Settings

Useproviderswhen model traffic needs provider-specific runtime settings,
such as an enterprise API gateway, provider-compatible proxy, custom endpoint,
or gateway-specific credentials. This is common for managed credentials, audit
logging, traffic routing, or self-hosted OpenAI-compatible providers.

Configure these settings ininit()instead of mutating global model state. They
are runtime-scoped to that agent and apply to every model it resolves, including
agent defaults, role-level models, per-call model selections, tasks, and context
compaction.

const
 
agent
 
=
 
await
 
init
(
{

 
model
: 
'anthropic/claude-sonnet-4-6'
,

 
providers
: 
{

 
anthropic
: 
{

 
baseUrl
: 
env
.
ANTHROPIC_BASE_URL
,

 
headers
: 
{

 
'X-Custom-Auth'
: 
env
.
GATEWAY_KEY
,

 
}
,

 
// Use this when the proxy expects a synthetic or gateway-specific key.

 
apiKey
: 
'dummy'
,

 
}
,

 
}
,

}
)
;

### Custom Virtual Sandboxes

For most agents, use the built-in virtual sandbox orsandbox: 'local'. If you need to customize just-bash directly, pass a Bash factory. The factory must return a fresh Bash-like runtime each time; share the filesystem object in the closure to persist files across sessions and prompts.

import
 
{
 
Bash
,
 
InMemoryFs
 
}
 
from
 
'just-bash'
;

const
 
fs
 
=
 
new
 
InMemoryFs
(
)
;

const
 
agent
 
=
 
await
 
init
(
{

 
sandbox
: 
(
)
 
=>
 
new
 
Bash
(
{
 fs
,
 
cwd
: 
'/workspace'
,
 
python
: 
true
 
}
)
,

 
model
: 
'anthropic/claude-sonnet-4-6'
,

}
)
;

const
 
session
 
=
 
await
 
agent
.
session
(
)
;

## Connectors

Connectors adapt third-party services (sandbox providers, etc.) into Flue. They are not an npm package — they are markdown installation instructions hosted athttps://flueframework.com/cli/connectors/and applied to your project by your AI coding agent.

flue add 
#
 list available connectors

flue add daytona 
|
 claude 
#
 pipe to your coding agent (claude, opencode, codex, cursor-agent, ...)

flue add https://e2b.dev --category sandbox 
|
 claude 
#
 build one from scratch — pass the provider's docs URL as the agent's starting point

The CLI fetches the markdown for the named connector and prints it to stdout when run by an agent (or with--print), or shows a short copyableflue add ... | <agent>recipe when run by a human in a terminal. Your agent reads the markdown and writes a small TypeScript adapter into./.flue/connectors/<name>.ts(or./connectors/<name>.tsfor the root layout).

## Running Agents

### Local Development (flue dev)

Long-running watch-mode dev server. Rebuilds and reloads on file changes — edit an agent, re-runcurl, see your change.

flue dev --target node 
#
 Node.js dev server

flue dev --target cloudflare 
#
 Cloudflare Workers (via wrangler) dev server

Defaults to port3583("FLUE" on a phone keypad). Override with--port.

flue dev --target cloudflarerequireswrangleras a peer dependency in your project (npm install --save-dev wrangler).

#### Loading environment variables

Pass--env <path>to load a.env-format file. Works for both targets:

flue dev --target node --env .env
flue dev --target cloudflare --env .env

Repeatable; later files override earlier ones on key collision. Shell-set env vars win over file values. Edits to the file trigger a reload. Same flag works forflue run.

### Trigger From the CLI (flue run)

Build and run any agent locally, perfect for running in CI or for one-shot scripted invocations. Production-shaped — builds the deployable artifact and starts it once.

flue run hello --target node --id test-1 \
 --payload 
'
{"text": "Hello world", "language": "French"}
'

### Trigger From HTTP Endpoint (flue build)

Build and deploy your agents as a web server, perfect for hosted agents.

flue buildbuilds to a./distdirectory, which you can then deploy. Cloudflare and any Node.js host are supported today, with more coming in the future.

flue build --target node # Node.js server (single bundled .mjs)
flue build --target cloudflare # Cloudflare Workers + Durable Objects

For Cloudflare,flue buildproduces an unbundled TypeScript entry thatwrangler deploybundles itself — the same pathflue dev --target cloudflareuses. Dev and deploy go through the same bundler, so what works in dev will work in production.

## About

The sandbox agent framework.

www.flueframework.com

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

3k

 stars
 

### Watchers

7

 watching
 

### Forks

158

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript78.0%
* Astro12.1%
* JavaScript9.6%
* CSS0.3%