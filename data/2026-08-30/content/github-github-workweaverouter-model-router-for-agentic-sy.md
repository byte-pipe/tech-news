---
title: 'GitHub - workweave/router: Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint change. · GitHub'
url: https://github.com/workweave/router
site_name: github
content_file: github-github-workweaverouter-model-router-for-agentic-sy
fetched_at: '2026-08-30T06:00:15.883978'
original_url: https://github.com/workweave/router
author: workweave
description: Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint change. - workweave/router
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 workweave

 

/

router

Public

* NotificationsYou must be signed in to change notification settings
* Fork75
* Star2.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

899 Commits
899 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude/
skills
.claude/
skills
 
 
.conductor
.conductor
 
 
.github/
workflows
.github/
workflows
 
 
cmd
cmd
 
 
db
db
 
 
docs
docs
 
 
frontend
frontend
 
 
install
install
 
 
internal
internal
 
 
scripts
scripts
 
 
sidecars/
hmm
sidecars/
hmm
 
 
smoke
smoke
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
docker-compose.yml
docker-compose.yml
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

One endpoint. Every model. Always the right one.

A drop-in proxy for Anthropic, OpenAI, and Gemini that picks the best model
foreveryrequest: using a tiny on-box embedder, not a vibes-based prompt.

Built byWeave: The #1 engineering intelligence platform,
loved by Robinhood, PostHog, Reducto, and hundreds of others.

## What it does

Point Claude Code, Codex, Cursor, or your own app atlocalhost:8080. The router:

* 🎯Routes per action.A cluster scorer derived fromAvengers-Pro1picks the right
model from your enabled providers, for every upstream API request.
(Seedocs/SEMANTICS.mdfor the canonical terminology:
the router routes peraction, not perturn.)
* 🔌Speaks everyone's API.Anthropic Messages, OpenAI Chat Completions,
Gemini native. Streaming, tools, vision, the works.
* 🧠Knows OSS too.DeepSeek, Kimi, GLM, Qwen, Llama, Mistral via
OpenRouter (or any OpenAI-compatible endpoint).
* 🔒BYOK by default.Provider keys stay on your box, encrypted at rest.
* 📊Observable.OTLP traces out of the box. See them in the Weave dashboard (http://localhost:8080/ui/dashboard) or drop in Honeycomb, Datadog,
Grafana, whatever.

## 30-second quickstart

The fastest way: point Claude Code, Codex, opencode, or pi at thehostedWeave Router with one command. No clone, no Docker, no Postgres.

npx @workweave/router

That's it. The installer asks which tool (Claude Code, Codex, opencode, or pi),
walks you through scope (user vs. project), grabs a router key, and wires
the right config file. Other flavors:

npx @workweave/router --claude 
#
 skip the picker, Claude Code

npx @workweave/router --codex 
#
 skip the picker, OpenAI Codex CLI

npx @workweave/router --opencode 
#
 skip the picker, opencode

npx @workweave/router --pi 
#
 skip the picker, pi + Loom UI

npx @workweave/router --scope project 
#
 per-repo, commits settings.json (or .codex/ / opencode.json)

npx @workweave/router --local 
#
 self-hosted localhost:8080

npx @workweave/router --base-url https://router.acme.internal
npx @workweave/router@0.1.0 
#
 pin a version

Requires Node ≥ 18 (Claude Code, opencode, and pi paths also needjq). Full
flag reference:install/npm/README.md.

### Or: self-host the whole stack

If you want the router (and dashboard) running on your own box:

#
 1. Drop a provider key in. OpenRouter is the recommended baseline.

echo
 
"
OPENROUTER_API_KEY=sk-or-v1-...
"
 
>>
 .env.local

#
 2. Boot Postgres + router on :8080 and seed an rk_ key.

make full-setup

The router is up athttp://localhost:8080, the dashboard athttp://localhost:8080/ui/(password:admin), and yourrk_...key
prints in the logs.

#
 Call it like Anthropic

curl -sS http://localhost:8080/v1/messages \
 -H 
"
Authorization: Bearer rk_...
"
 \
 -d 
'
{"model":"claude-sonnet-4-5","max_tokens":256,

 "messages":[{"role":"user","content":"hi"}]}
'

#
 ...or like OpenAI

curl -sS http://localhost:8080/v1/chat/completions \
 -H 
"
Authorization: Bearer rk_...
"
 \
 -d 
'
{"model":"gpt-4o-mini",

 "messages":[{"role":"user","content":"hi"}]}
'

#
 Peek at the routing decision without proxying

curl -sS http://localhost:8080/v1/route -H 
"
Authorization: Bearer rk_...
"
 -d 
'
...
'

### What that stack looks like

Only the grey boxes are off your machine. The router, the scorer, Postgres, and
your provider keys all stay local; prompts go from the router straight to the
provider you configured, never to Weave.

flowchart LR
 client["Claude Code, Codex, opencode,<br/>pi, Cursor, your own app"]
 router["Router :8080<br/>/v1/messages · /v1/chat/completions<br/>/v1beta/models · /v1/route"]
 scorer["Cluster scorer<br/>in-process ONNX embedder"]
 hmm["HMM policy sidecar :8093<br/>optional, make up-hmm"]
 pg[("Postgres<br/>installations, rk_ keys,<br/>encrypted BYOK keys, usage")]
 ui["Dashboard /ui<br/>selfhosted mode only"]
 providers["Anthropic · OpenAI · Gemini<br/>OpenRouter and any<br/>OpenAI-compatible endpoint"]
 otel["Your OTLP collector<br/>Honeycomb, Datadog, Grafana"]

 client -->|"rk_… bearer token,<br/>streamed response back"| router
 router -->|"embed and score the action"| scorer
 router -.->|"ROUTER_DEFAULT_STRATEGY=hmm"| hmm
 router -->|"auth, config, usage"| pg
 pg --> ui
 router -->|"provider key from env or BYOK"| providers
 router -.->|"spans and usage logs"| otel

 classDef external fill:#f4f4f5,stroke:#a1a1aa,color:#3f3f46
 class providers,otel external

 
Loading

Multi-replica deployments also need Pub/Sub (PUBSUB_*) for cache
invalidation;docker composeruns the emulator for you.

### Optional: self-host the frozen HMM policy

The default stack uses the in-process cluster scorer. To run the frozen HMM
policy as a companion container, add a Google API key and use the opt-in target:

echo
 
'
GOOGLE_API_KEY=...
'
 
>>
 .env.local
make up-hmm

This does not change the default strategy. Seesidecars/hmm/README.mdfor artifact verification,
embedding compatibility, and explicit HMM selection.

## Wire it into your tools

Claude Code.Runmake install-ccto wire Claude Code at the local
self-hosted router (it's also invoked automatically at the end ofmake full-setup). For the hosted router, usenpx @workweave/routerabove.

Codex(OpenAI CLI).npx @workweave/router --codexpatches~/.codex/config.toml(or<repo>/.codex/config.tomlwith--scope project)
with a managed[model_providers.weave]block and setsmodel_provider = "weave".
The provider preserves Codex's existing ChatGPT OAuth login while the router
key rides in anX-Weave-Router-KeyHTTP header and the installer selects the
HMM strategy for the public hosted endpoint.--codex --localand custom
self-hosted URLs keep their router's configured default because the HMM
sidecar is optional. HMM and forced selections in the native Codex family
(gpt-5.6-sol,gpt-5.6-terra,gpt-5.6-luna) use that OAuth credential;
every other selected model uses its WorkWeave deployment or BYOK credential,
matching the Claude Code plugin's model-to-credential dispatch.
Codex does not load third-party slash-command files, so the installer ships the
router directives as native Codex skills:$force-model <model-id>(alias$fm <model-id>),$unforce-model(alias$ufm), and$router-feedback <text>(alias$rf <text>). Each skill runs a localscripts/emit.shthat prints the leading-space directive (for example,/force-model gpt-5.6-terra); the router intercepts that exec output.
You can type that form directly instead. Re-install
and--uninstall --codexrewrite/remove only the managed block, leaving the
rest of your Codex config untouched. Codex also gets$router-status,$router-off,$router-on, and$router-modelsas skills that call this
installer's own verbs. Invoke$disable-routing(or$router-off) to switch the
next Codex session back to its normal provider, or runnpx @workweave/router disable-routingin a shell; a literal/disable-routingis not a third-party extension point in Codex.

opencode.npx @workweave/router --opencodemerges aprovider.weaveentry into~/.config/opencode/opencode.json(or<repo>/opencode.jsonwith--scope project). It uses opencode's bundled@ai-sdk/anthropicprovider pointed at the router's/v1endpoint — the router speaks the
Anthropic Messages API natively, so opencode works unmodified. The router
key and identity headers ride alongside the provider config; re-install
rewrites only the managed block and--uninstall --opencodestrips it.

pi.npx @workweave/router --pikeeps stock pi as the runtime and installs
the router's pi extension. It adds the Loom header, Wooly's animated terminal
mascot, a persistentWEAVE ROUTERroute/savings line,/fm+/ufmmodel-pin commands with a[forced]status, and context-isolated subagents
without shipping or maintaining a forked pi binary.

Cursor(early beta, performance may not be the best).Settings →
Models →Override OpenAI Base URL→http://localhost:8080/v1, pasterk_...as the API key.

Switching on/off.After installing,npx @workweave/router off --claude(or--codex/--opencode) routes that client straight to its provider
again without discarding the router config;onflips it back, andstatusreports which way it's pointing. Claude Code also gets/router-off,/router-on, and/router-statusslash commands. Cursor toggles via the same
Settings → Models override above. Seeinstall/README.md.

Choosing which models the router may pick.npx @workweave/router models --claudelists every deployed model with its on/off state, andmodels enable/models disablechange it — the same setting as the dashboard's settings
page, edited from the terminal. Claude Code gets this as/router-models(alias/models). Requires a router that serves the model-selection API;
against the Weave-hosted router the list still prints and points you at the
dashboard, where selection is an organization-wide setting. Seeinstall/README.md.

Two keys, don't mix them up:

* sk-or-.../sk-ant-.../sk-...= yourupstreamprovider key. Lives in.env.local.
* rk_...= yourrouterkey. Clients send this as a Bearer token.

## Endpoints

Endpoint

Format

POST /v1/messages

Anthropic Messages, routed

POST /v1/chat/completions

OpenAI Chat Completions, routed

POST /v1beta/models/:action

Gemini 
generateContent
, routed

POST /v1/route

Returns the decision, no upstream call

GET /v1/models
  ·  
POST /v1/messages/count_tokens

Anthropic passthrough

GET /health
  ·  
GET /readyz
  ·  
GET /validate

liveness + dependency readiness + key check

GET /v1/analytics/routing-decisions

Raw routing decisions as cursor-paginated NDJSON (
docs
)

GET /v1/analytics/schema
  ·  
GET /v1/analytics/models

Export field dictionary + price book

Keep liveness probes on/health. Point startup or readiness probes at/readyzwhen configured policy sidecars must be ready before traffic arrives.

## Deeper docs

* 📐Configuration reference: every env var,
BYOK encryption, OTel knobs, cluster routing.
* 🧭Semantics and terminology: canonical definitions
for session, round, turn, action, and step.
* 📊Analytics export: pulling raw routing
decisions into your own warehouse with a read-only key.
* Policy router harness: contract and
rollout checklist for adding an out-of-process policy model.
* 🛠️Contributing: layering rules, hot-reload dev,
migrations, tests, the whole engineering loop.
* 🏗️Architecture: package layout, import contracts,
recipes for adding endpoints / providers / strategies.

## Footnotes

1. Zhang, Y. et al.Beyond GPT-5: Making LLMs Cheaper and Better via
Performance–Efficiency Optimized Routing(Avengers-Pro).
arXiv:2508.12631, 2025.https://arxiv.org/abs/2508.12631↩