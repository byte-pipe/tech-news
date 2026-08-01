---
title: 'GitHub - yc-software/qm: Multiplayer agent harness for work · GitHub'
url: https://github.com/yc-software/qm
site_name: hackernews_api
content_file: hackernews_api-github-yc-softwareqm-multiplayer-agent-harness-for
fetched_at: '2026-08-01T11:29:55.427835'
original_url: https://github.com/yc-software/qm
author: tosh
date: '2026-07-31'
description: Multiplayer agent harness for work. Contribute to yc-software/qm development by creating an account on GitHub.
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 yc-software

 

/

qm

Public

* NotificationsYou must be signed in to change notification settings
* Fork323
* Star3.5k

 
 
 
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

40 Commits
40 Commits
.claude
.claude
 
 
.codex/
skills
.codex/
skills
 
 
.github/
workflows
.github/
workflows
 
 
adrs
adrs
 
 
aws/
microvm-agent
aws/
microvm-agent
 
 
cli
cli
 
 
deploy
deploy
 
 
docs
docs
 
 
fly
fly
 
 
local
local
 
 
plugins
plugins
 
 
scripts
scripts
 
 
skills-seed
skills-seed
 
 
src
src
 
 
test
test
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.npmrc
.npmrc
 
 
.oxlintrc.json
.oxlintrc.json
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.json
.prettierrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
deployment.md
deployment.md
 
 
eslint.config.mjs
eslint.config.mjs
 
 
knip.json
knip.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.contract.json
tsconfig.contract.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# qm

A multiplayer agent harness for work. In Slack and on the web.

## What is QM?

Most agents are designed like personal assistants. You can make one work for a whole
company, but it quickly gets complex. QM is designed for startups. Employees each get
their own isolated workspace and work independently without affecting each other, and
they can also collaborate with the agent in channels, group messages, and projects.

Each person and each room has its own scoped memory, files, keychain view, permissions,
crons, web apps, and durable sandbox.

It's built with open source in mind. Pick your own harness and model and switch between
them — Pi, OpenCode, Codex, and Claude Code all drive the same core, so a deployment
isn't tied to any single vendor.

## Features

* Personal and shared scopes.People customize the agent to betheirs, and still
work with it collaboratively in Slack channels and projects.
* Slack and web.The same identity and configuration carries between Slack and the
web app.
* Admin control.Set org-level configuration, a security posture, and which
harnesses and models are available.
* Web apps.Spin up custom internal apps and publish them to the right people.
* Shared skills.Skills are scope-owned and shareable by grant, with admin-gated
promotion to the whole org and skill packs imported from git repositories.
* Background work.Crons and watches run work while nobody's watching.

## What you can do with it

* Search internal notes, email, documents, databases, and the web together
* Retrieve information from your company brain
* Build internal apps, publish them to the right people, and keep their data current
* Learn your writing voice from past sends, then triage your inbox on a schedule —
labels and reply drafts included
* Work in an existing repository: run tests, open PRs, monitor CI, check system logs
* Track a project in a shared channel and post updates and follow-ups

## Architecture

flowchart LR
 DB[("Postgres<br/>sessions · memory · queue")]

 subgraph CORE["Headless core"]
 API["API · identity · policy · scheduler"]
 LOOP["Agent loop<br/>(Pi, OpenCode, Claude Code)"]
 API <--> LOOP
 end

 SBX["Per-scope sandbox<br/>files · tools · logged-in services"]

 DB <--> API
 LOOP <--> SBX

 
Loading

Every turn runs through a central core, which can use a variety of models and harnesses
to generate the response. A Postgres persistence layer holds user data, session history,
and other durable state. The agent has a small, fixed tool surface; one of those tools isexecute, which runs commands in the scope's own isolated sandbox — its durable computer,
where installed tools stay installed. The web UI, the admin panel, and the public portal
are optional plugins over the core's HTTP API;
Slack is an optional in-process plugin that core starts
and supervises through a direct service client.

The core runs TypeScript directly on Node and uses Fastify for HTTP. The Slack plugin
uses Bolt; the web UI builds with Vite and renders with Lit.

The core itself is generic. Everything specific to one company — org config, custom tools
and skills, sandbox image, infrastructure — lives in adeployment directorythat theqmCLIvalidates and deploys. Every substrate (harness, session
store, sandbox, memory) sits behind an interface, so production implementations swap in
via one wiring file.

## Security and secrets

QM's approach follows local coding agents like OpenCode, Codex, and Claude Code: the
agent acts as the person it's working for, with their credentials and permissions, and
everything it does is audited. An org picks one security posture, which narrower scopes
can only tighten:

* Strict— every harness tool call pauses for human approval, except the two
no-effect turn enders.
* Auto(default) — a classifier screens provenance-labelled external data and tool
results before they reach the model; a deployment can point that at its own screening
proxy.
* Dangerous— no content screening, no pauses between tool calls.

The predeclared command policy — approval rules and hard denials for things like
recursive deletes or destructive SQL — applies in every posture, Dangerous included.

SECURITY.mdhas the threat model, the operator assumptions, and the
known limitations.

## Deploy it for your org

Create an organization-owned deployment repository that depends on@yc-software/qm:

npm 
exec
 --yes --package=@yc-software/qm@latest -- \
 qm init 
.
 --org 
<
slug
>
 --target 
<
fly-or-aws
>

npm install

Initialization materializes a deployment skill for an agent and walks through
infrastructure, web sign-in, connector credentials, optional Slack access, deployment,
and live verification — no source checkout required. Each deployment runs in the
operator's own cloud account; initialization does not generate or enable deployment CI,
and this repository has no production deployment workflow. Seedeployment.mdfor the details.

## Contributing

We take contributions ashuman-writtentext, not code — seeCONTRIBUTING.md. Describe the change you'd like informally in a.txtor.mdfile inadrs/, and if we're aligned we'll handle the
implementation. Report vulnerabilities privately — seeSECURITY.md,
not a public issue.

## Customize your instance

The deployment repository above carries config and a sandbox layer, and never needs a
source checkout. Some organizations want the opposite trade: the whole codebase in one
place, so engineers and coding agents read core and customizations together, while the
customizations themselves stay private. For that, keep aprivate fork: a standalone
private repository whose history begins as a clone of qm and whose core stays identical
to upstream.

Populate it once, then clone it to work in:

gh repo create 
<
org
>
/qm-private --private

git clone --bare git@github.com:yc-software/qm qm-seed.git
git -C qm-seed.git push --mirror git@github.com:
<
org
>
/qm-private
rm -rf qm-seed.git

git clone git@github.com:
<
org
>
/qm-private
git -C qm-private remote add upstream git@github.com:yc-software/qm

Create the private fork with a plain clone, as shown above, and never with GitHub's fork
feature. The word "fork" here names the concept — a downstream copy that diverges
deliberately and merges from upstream — not GitHub's Fork button. A GitHub fork inherits
the visibility of the repository it came from, so a fork of a public repository cannot be
made private. A GitHub fork also shares one object network with the repository it came
from, so commits pushed to the fork stay fetchable by SHA from the public side. Many
organizations disallow forking private repositories as well. A plain clone has none of
these problems, and it costs one thing: the clone is an ordinary repository, so upstream's
CI workflows run live in your own account. Expect to supply the secrets those workflows
need, or disable the ones you do not want running.

Everything specific to your organization goes indeploy/layers/<org>/— config, sandbox
tools and skills, plugin images, infrastructure — in the same shapeqm initproduces. Seedeploy/layers/README.md. Core stays byte-identical to
upstream, which is what keeps merges small.

Two skills maintain the boundary in both directions.update-qmmerges upstream qm into
the private fork and opens the sync PR;upstream-prsends an organization-agnostic fix back to
qm, cutting the branch fromupstream/mainand checking the outgoing diff, commit
messages, and screenshots for organization identifiers before it pushes. Nothing underdeploy/layers/ever travels upstream.

## Going deeper

* docs/getting-started.md— first run, end to end
* cli/README.md— theqmCLI and the deployment directory contract
* docs/deploy-directory.md— the deployment directory in full
* .env.example— every knob, documented in place
* plugins/— the surfaces (Slack, web UI, admin, portal)

## License

Except where otherwise noted, QM is available under theMIT License.