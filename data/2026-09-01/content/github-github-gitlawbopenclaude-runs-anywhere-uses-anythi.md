---
title: 'GitHub - Gitlawb/openclaude: runs anywhere. uses anything · GitHub'
url: https://github.com/Gitlawb/openclaude
site_name: github
content_file: github-github-gitlawbopenclaude-runs-anywhere-uses-anythi
fetched_at: '2026-09-01T15:24:53.970577'
original_url: https://github.com/Gitlawb/openclaude
author: Gitlawb
description: runs anywhere. uses anything. Contribute to Gitlawb/openclaude development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Gitlawb

 

/

openclaude

Public

* NotificationsYou must be signed in to change notification settings
* Fork8.9k
* Star31.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,195 Commits
1,195 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
bin
bin
 
 
docs
docs
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
vendor/
node-domexception-shim
vendor/
node-domexception-shim
 
 
vscode-extension/
openclaude-vscode
vscode-extension/
openclaude-vscode
 
 
web
web
 
 
.bun-version
.bun-version
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.npmignore
.npmignore
 
 
.nvmrc
.nvmrc
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
AGENTS.md
AGENTS.md
 
 
ANDROID_INSTALL.md
ANDROID_INSTALL.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
PLAYBOOK.md
PLAYBOOK.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bun.lock
bun.lock
 
 
knip.json
knip.json
 
 
package.json
package.json
 
 
release-please-config.json
release-please-config.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.type-tests.json
tsconfig.type-tests.json
 
 
View all files

## Repository files navigation

OpenClaude is an open-source coding-agent CLI for cloud and local model providers.

Use OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported backends while keeping one terminal-first workflow: prompts, tools, agents, MCP, slash commands, and streaming output.

OpenClaude is also mirrored to GitLawb:gitlawb.com/node/repos/z6MkqDnb/openclaude

Quick Start|Setup Guides|Providers|Development|VS Code Extension|Partners|Community

## Partners

GitLawb

Bankr.bot

Atomic Chat

Xiaomi MiMo

Atlas Cloud

AI/ML API

Novita AI

ApiSmart

Concentrate

Exa

## Why OpenClaude

* One CLI across cloud APIs and local model backends — no per-provider tooling
* Guided provider setup and saved profiles with/provider
* Coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools
* A bundled VS Code extension for launch integration and theme support
* A pixel-art hero companion who fires an arrow every time you press Enter (really — seeMeet your buddy)

## Quick Start

### Install

OpenClaude requires Node.js>=22.0.0for npm installs and runtime. Bun is
only needed for source builds and local development.

npm install -g @gitlawb/openclaude@latest

If you're on Arch Linux, you can install OpenClaude from the community-maintainedAUR package:

paru -S openclaude

If the install later reportsripgrep not found, install ripgrep system-wide and confirmrg --versionworks in the same terminal before starting OpenClaude.

Verify / troubleshoot installed version:

openclaude --version
npm view @gitlawb/openclaude dist-tags
npm install -g @gitlawb/openclaude@latest

### Start

openclaude

Inside OpenClaude:

* run/providerfor guided provider setup and saved profiles
* run/onboard-githubfor GitHub Models onboarding

Note:OpenClaude does not automatically load project.envfiles. We recommend using the/providercommand for setup, which saves provider profiles and credentials in.openclaude-profile.json. If you prefer environment variables, export them explicitly or runopenclaude --provider-env-file .envfor provider/setup variables. Export runtime/debug knobs from your shell or launcher.

### Resume or fork a conversation

Resume an existing conversation by session ID, or continue the most recent
conversation in the current directory:

openclaude --resume 
<
session-id
>

openclaude --continue

Add--fork-sessionto branch the conversation history into a new session ID
instead of reusing the original transcript:

openclaude --resume 
<
session-id
>
 --fork-session
openclaude --continue --fork-session

Forking is conversation branching only. It does not create filesystem isolation,
copy your working tree, or create a git worktree branch.

### Background sessions

Run long non-interactive prompts detached from the current terminal:

openclaude --bg 
"
fix failing tests
"

openclaude --bg --name auth-refactor 
"
refactor auth middleware
"

openclaude ps
openclaude logs auth-refactor
openclaude logs auth-refactor -f
openclaude 
kill
 auth-refactor

Background sessions are local child processes. OpenClaude does not start a daemon
or network service, and permission/provider/model/settings flags are passed to
the child process the same way they are for a foreground--printrun. Session
metadata and logs are stored under the resolved OpenClaude config directory,
usually~/.openclaude/bg-sessions/;OPENCLAUDE_CONFIG_DIRcan point
OpenClaude somewhere else.CLAUDE_CONFIG_DIRis ignored for OpenClaude
background-session storage. Session names can be reused after older sessions
reach a terminal state; use the session ID to inspect older logs with the same
name. A naturally finished session is recorded asexitedwhen its process
returns zero andfailedwhen it returns nonzero or handles a termination
signal.staleremains the conservative result when the process disappears
without an observed outcome; an explicit successfulopenclaude killis
recorded askilled, andkilledtakes precedence over a naturalexitedorfailedoutcome for the same process. Terminal outcomes are stored separately
underbg-sessions/terminal/; deleting that directory makes finished sessions
fall back to liveness-derived status. OpenClaude does not infer POSIX signal
names on Windows.
Unobservable force termination, host crashes, and power loss remainstaleon
every platform.

openclaude attach <id-or-name>currently reports the matching session and
points toopenclaude logs <id> -f; full terminal reattach is not implemented
for local background sessions yet.

### OpenClaude config cutover

OpenClaude stores its own config under~/.openclaudeand~/.openclaude.jsonby default. It does not read~/.claude, project.claude/directories, orCLAUDE_CONFIG_DIR; new users can start with an empty OpenClaude config and do
not need Claude Code installed.

If you previously used OpenClaude with.claudepaths, migrate intentionally:
copy only the settings, commands, agents, skills, scheduled tasks, or other files
you personally created for OpenClaude into the matching.openclaudelocation.
Do not blanket-copy.claude, and do not copy Claude Code credentials or auth
files. For provider authentication, prefer running OpenClaude's provider setup
again or exporting provider-specific environment variables.

### Fastest OpenAI setup

macOS / Linux:

export
 CLAUDE_CODE_USE_OPENAI=1

export
 OPENAI_API_KEY=sk-your-key-here

export
 OPENAI_MODEL=gpt-4o

openclaude

Windows PowerShell:

$
env:
CLAUDE_CODE_USE_OPENAI
=
"
1
"

$
env:
OPENAI_API_KEY
=
"
sk-your-key-here
"

$
env:
OPENAI_MODEL
=
"
gpt-4o
"

openclaude

### Fastest local Ollama setup

macOS / Linux:

export
 CLAUDE_CODE_USE_OPENAI=1

export
 OPENAI_BASE_URL=http://localhost:11434/v1

export
 OPENAI_MODEL=qwen2.5-coder:7b

openclaude

Windows PowerShell:

$
env:
CLAUDE_CODE_USE_OPENAI
=
"
1
"

$
env:
OPENAI_BASE_URL
=
"
http://localhost:11434/v1
"

$
env:
OPENAI_MODEL
=
"
qwen2.5-coder:7b
"

openclaude

For Ollama, OpenClaude uses Ollama's native chat API and requests a 32768-token
context window on each chat request so same-session history is not silently
truncated by Ollama's OpenAI-compatible shim. SetOPENCLAUDE_OLLAMA_NUM_CTXorOLLAMA_CONTEXT_LENGTHif you need a different request-level context size.
SeeAdvanced Setupfor
verification withollama ps.

## Setup Guides

Beginner-friendly guides:

* Non-Technical Setup
* Windows Quick Start
* macOS / Linux Quick Start

Advanced and source-build guides:

* Advanced Setup
* Smart Auto-Routing
* Agent Routing and Step Limits
* Headless gRPC Server
* Repo Map (codebase intelligence)
* Android Install

## Supported Providers

Provider

Setup Path

Notes

OpenAI-compatible

/provider
 or env vars

Works with OpenAI, OpenRouter, DeepSeek, Groq, Mistral, LM Studio, and other compatible 
/v1
 servers

Z.AI GLM Coding Plan

/provider
 or OpenAI-compatible env vars

Uses 
OPENAI_API_KEY
 at 
https://api.z.ai/api/coding/paas/v4
 and defaults to 
glm-5.2

AI/ML API

/provider
 or 
AIMLAPI_API_KEY
 (
setup guide
)

Uses 
https://api.aimlapi.com/v1
, auto-detects the OpenAI-compatible route from 
AIMLAPI_API_KEY
, sends OpenClaude attribution headers, and discovers chat-capable models from the public 
/models
 catalog

Concentrate

/provider
 or 
CONCENTRATE_API_KEY

Unified OpenAI-compatible gateway at 
https://api.concentrate.ai/v1
; defaults to 
deepseek-v4-flash
 and auto-discovers the chat model catalog

LLMTR

/provider
 or OpenAI-compatible env vars

Multi-model gateway at 
https://llmtr.com/v1
; 
/provider
 and 
--provider llmtr
 default to 
deepseek/deepseek-v4-flash
, while raw env setup must set 
OPENAI_BASE_URL=https://llmtr.com/v1
 and 
OPENAI_MODEL
; accepts 
LLMTR_API_KEY
 or 
OPENAI_API_KEY
 after the route is selected and discovers tool-capable Chat Completions models from the public catalog

ApiSmart

/provider
 or 
APISMART_API_KEY

Uses 
https://gw.apismart.ai/v1
, defaults to 
DEEPSEEK_V4_FLASH
, and supports optional 
APISMART_MODEL
 plus authenticated model discovery

Hicap

/provider
 or OpenAI-compatible env vars

Uses 
api-key
 auth, discovers models from unauthenticated 
/models
, and supports Responses mode for 
gpt-
 models

Fireworks AI

/provider
 or env vars

First-class provider with 276 curated models (DeepSeek, Qwen, Llama, Gemma, and more); uses 
FIREWORKS_API_KEY

LongCat

/provider
 or env vars

Meituan LongCat OpenAI-compatible API at 
https://api.longcat.chat/openai/v1
; uses 
LONGCAT_API_KEY
 and defaults to 
LongCat-2.0

ClinePass

/provider
 or env vars

AI model gateway with usage limits (5hr, weekly, monthly); uses 
CLINE_API_KEY
 at 
https://api.cline.bot/api/v1

Gemini

/provider
 or env vars

Supports API key only

GitHub Models

/onboard-github

Interactive onboarding with saved credentials

Codex OAuth

/provider

Opens ChatGPT sign-in in your browser and stores Codex credentials securely

Codex

/provider

Uses existing Codex CLI auth, OpenClaude secure storage, or env credentials

Gitlawb Opengateway

Startup default, 
/provider
, or env vars

Smart gateway at 
https://opengateway.gitlawb.com/v1
; requires an API key from 
https://gitlawb.com/opengateway/keys
 and routes Xiaomi MiMo and GMI Cloud partner models by 
OPENAI_MODEL

OpenCode Zen

/provider
 or env vars

Pay-as-you-go AI gateway (48 models); uses 
OPENCODE_API_KEY
 via 
https://opencode.ai/zen/v1
; shared key with OpenCode Go

OpenCode Go

/provider
 or env vars

$10/mo subscription for open models (13 models); uses 
OPENCODE_API_KEY
 via 
https://opencode.ai/zen/go/v1
; shared key with OpenCode Zen

Xiaomi MiMo

/provider
 or env vars

OpenAI-compatible API at 
https://mimo.mi.com
; uses 
MIMO_API_KEY
 and defaults to 
mimo-v2.5-pro

NEAR AI

/provider
 or env vars

Unified gateway (Claude, GPT, Gemini + TEE open models); uses 
NEARAI_API_KEY
 at 
https://cloud-api.near.ai/v1

Cloudflare Workers AI

/provider
 or env vars

OpenAI-compatible API at 
https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1
; uses 
CLOUDFLARE_API_TOKEN
. Replace 
<ACCOUNT_ID>
 with your Cloudflare account id.

Ollama

/provider
 or env vars

Local inference with no API key

Atomic Chat

/provider
, env vars, or 
bun run dev:atomic-chat

Local Model Provider; auto-detects loaded models

Bedrock / Vertex / Foundry

env vars

Anthropic-family cloud routes; Vertex is for Claude on Vertex AI, not arbitrary Model Garden models

## What Works

* Tool-driven coding workflows: Bash, file read/write/edit, grep, glob, agents, tasks, MCP, and slash commands
* Streaming responses: Real-time token output and tool progress
* Tool calling: Multi-step tool loops with model calls, tool execution, and follow-up responses
* Images: URL and base64 image inputs for providers that support vision
* Provider profiles: Guided setup plus saved user-level provider profile support
* Local and remote model backends: Cloud APIs, local servers, and Apple Silicon local inference
* Codebase intelligence (repo map): Structural map of the repository ranked by PageRank importance, auto-injected into context when theREPO_MAPflag is enabled or theREPO_MAPenvironment variable is set. Inspect with/repomap(2048-token default). Seedocs/repo-map.mdfor details.
* A companion with signature moves: A truecolor pixel-art hero who lives beside your prompt and reacts when you work. See below.

## Meet Your Buddy

Run/buddyto hatch a companion — a truecolor pixel-art hero who stands
beside your prompt, idles, blinks, and fires their signature move every time
you submit a message:

/buddy hatch (first run) or pet your companion
/buddy set robinhood the green archer — arrow shot on every Enter
/buddy set kaio gold-haired warrior — charges a full-width energy wave
/buddy set strawhat stretchy punch that snaps back
/buddy set merlin twinkling sparkle stream
/buddy set kage spinning shuriken
/buddy set ember dragon fire with a real heat gradient
/buddy set corsair cannonball with smoke trail
/buddy name Robin rename your companion
/buddy set random back to your rolled hero

Companions respectprefersReducedMotion, degrade gracefully to line art in
low-color terminals, and can be silenced with/buddy mute. Requires a
terminal at least 100 columns wide for the full sprite.

## Provider Notes

OpenClaude supports multiple providers, but behavior is not identical across all of them.

* Anthropic-specific features may not exist on other providers
* Tool quality depends heavily on the selected model
* Smaller local models can struggle with long multi-step tool flows
* Some providers impose lower output caps than the CLI defaults, and OpenClaude adapts where possible
* AI/ML API uses the OpenAI-compatible route, defaults togpt-4o, and only surfaces chat-capable models from its public catalog
* Gitlawb Opengateway is the fresh-install startup default and requires an API key fromhttps://gitlawb.com/opengateway/keys. It uses one OpenAI-compatible base URL; switch betweenmimo-*andgoogle/gemini-3.1-flash-lite-previewwith/model, and do not pin the base URL to/v1/xiaomi-mimo.
* Z.AI GLM Coding Plan useshttps://api.z.ai/api/coding/paas/v4withglm-5.2by default. GLM-5.3 is selectable asglm-5.3; useglm-5.3?reasoning=low,glm-5.3?reasoning=high, orglm-5.3?reasoning=xhighto request its documented low, high, or maximum effort. The existing GLM-5.2 query controls remain supported.
* Xiaomi MiMo usesapi-keyheader auth on the direct OpenAI-compatible route and currently does not support/usagereporting in OpenClaude
* GitHub Copilot serializes sub-agent execution by default to reduce Premium Request consumption — seeAgent Routing and Step Limitsfor tuning

For best results, use models with strong tool/function calling support.

## Agents

Route different agents to different models (cost optimization, splitting work
by model strength), cap sub-agent tool steps withmaxSteps, and tune GitHub
Copilot sub-agent behavior. Configured via settings, agent frontmatter, and
environment variables:

* per-agent provider/model overrides viaagentModels+agentRoutingin~/.openclaude/settings.json
* model-only routes that reuse your current provider's credentials
* built-in agents (ExploreandPlan[feature-gated],verification[feature-gated: requiresVERIFICATION_AGENT+tengu_hive_evidence],code-reviewer[requires diff inline]) routable by type name

SeeAgent Routing and Step Limitsfor the full guide.

## Web Search and Fetch

By default,WebSearchworks on non-Anthropic models using DuckDuckGo. This gives GPT-4o, DeepSeek, Gemini, Ollama, and other OpenAI-compatible providers a free web search path out of the box.

Note:DuckDuckGo fallback works by scraping search results and may be rate-limited, blocked, or subject to DuckDuckGo's Terms of Service. If you want a more reliable supported option, configure Firecrawl.

For Anthropic-native backends and Codex responses, OpenClaude keeps the native provider web search behavior.

WebFetchworks, but its basic HTTP plus HTML-to-markdown path can still fail on JavaScript-rendered sites or sites that block plain HTTP requests.

Set aFirecrawlAPI key if you want Firecrawl-powered search/fetch behavior:

export
 FIRECRAWL_API_KEY=your-key-here

With Firecrawl enabled:

* WebSearchcan use Firecrawl's search API while DuckDuckGo remains the default free path for non-Claude models
* WebFetchuses Firecrawl's scrape endpoint instead of raw HTTP, handling JS-rendered pages correctly

Free tier atfirecrawl.devincludes 500 credits. The key is optional.

## Headless gRPC Server

OpenClaude can run as a headless gRPC service with bidirectional streaming —
integrate its agentic capabilities into other applications, CI/CD pipelines,
or custom UIs. Start it withnpm run dev:grpc; a test CLI client ships with
the repo. SeeHeadless gRPC Serverfor configuration
and client generation fromsrc/proto/openclaude.proto.

## Development

Use Node.js>=22.0.0and Bun1.3.13or newer for source builds.

bun install
bun run build
node dist/cli.mjs

Day-to-day commands:

* bun run dev— build and launch from source
* bun test— full unit suite (Bun's built-in runner)
* bun test path/to/file.test.ts— focused runs for the areas you touch
* bun run test:coverage— coverage tocoverage/lcov.infoplus a visual report atcoverage/index.html(bun run test:coverage:uirebuilds just the UI)
* bun run smoke— smoke checks
* bun run doctor:runtime,bun run verify:privacy; for PR intent scanning, use the fresh-upstream, explicit-ref workflow in thelocal pre-push validation contract

Focused suites:bun run test:provider,bun run test:provider-recommendation.

To benchmark the launcher module compile cache, build the CLI and run:

bun run build
bun run benchmark:startup

The benchmark requires Node>=22.8.0, where the compile-cache API was added;
the built OpenClaude launcher continues to support the declared Node>=22.0.0runtime range.

The benchmark defaults to 30 separate-process warm runs and 10 isolated
empty-cache runs. It reports the median, IQR, MAD, first cache-populating run,
first warm-up, Node/OS/CPU details, bundle size, and commit. Direct bundle
timings are included only as a secondary diagnostic; the full launcher result
is the decision signal. Usebun run benchmark:startup -- --warm-runs 40 --cold-runs 10to request a
larger sample set. The benchmark records results without enforcing a timing
threshold in CI.

OpenClaude leaves Node's standard compile-cache controls authoritative. SetNODE_DISABLE_COMPILE_CACHE=1to disable the optimization, including for V8
coverage runs that require uncached compilation.

Before opening or updating a PR, run the authoritativelocal pre-push validation contract. The commands below are useful for narrow iteration, but they do not replace that required preflight:

* bun run build
* bun run smoke
* bun run test:coveragewhen your change affects shared runtime or provider logic
* focusedbun test ...runs for the files and flows you changed

## Repository Structure

* src/- core CLI/runtime
* scripts/- build, verification, and maintenance scripts
* docs/- setup, contributor, and project documentation
* vscode-extension/openclaude-vscode/- VS Code extension
* .github/- repo automation, templates, and CI configuration
* bin/- CLI launcher entrypoints

## VS Code Extension

The repo includes a VS Code extension invscode-extension/openclaude-vscodefor OpenClaude launch integration, provider-aware Control Center, in-editor chat, theme support, and optionalMicrosoft Foundry / Azure OpenAIconfiguration (endpoint, API version, deployment, API key via Secret Storage) injected into launched terminals. See that folder'sREADME.

## Security

If you believe you found a security issue, seeSECURITY.md.

## Community

* UseGitHub Discussionsfor Q&A, ideas, and community conversation
* UseGitHub Issuesfor confirmed bugs and actionable feature work
* Join theDiscordto chat with the community in real time
* Follow@gitlawb on Xfor updates and announcements

## Contributing

Contributions are welcome. For larger changes, open an issue first so the
scope is clear before implementation. SeeDevelopmentfor the
build, test, and pre-PR validation commands.

## Disclaimer

OpenClaude is an independent community project and is not affiliated with, endorsed by, or sponsored by Anthropic.

OpenClaude originated from the Claude Code codebase and has since been substantially modified to support multiple providers and open use. "Claude" and "Claude Code" are trademarks of Anthropic PBC. SeeLICENSEfor details.

## License

MIT for OpenClaude contributors' modifications; the derived Claude Code remains Anthropic's.See more.