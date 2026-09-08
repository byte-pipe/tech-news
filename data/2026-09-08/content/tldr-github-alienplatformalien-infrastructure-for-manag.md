---
title: 'GitHub - alienplatform/alien: Infrastructure for managed self-hosting · GitHub'
url: https://github.com/alienplatform/alien
site_name: tldr
content_file: tldr-github-alienplatformalien-infrastructure-for-manag
fetched_at: '2026-09-08T14:53:56.089465'
original_url: https://github.com/alienplatform/alien
date: '2026-09-08'
description: Infrastructure for managed self-hosting. Contribute to alienplatform/alien development by creating an account on GitHub.
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 alienplatform

 

/

alien

Public

* NotificationsYou must be signed in to change notification settings
* Fork9
* Star215

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

528 Commits
528 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.changeset
.changeset
 
 
.config
.config
 
 
.github
.github
 
 
.greptile
.greptile
 
 
client-sdks
client-sdks
 
 
crates
crates
 
 
docker
docker
 
 
examples
examples
 
 
infra
infra
 
 
packages
packages
 
 
scripts
scripts
 
 
tests/
e2e/
test-apps
tests/
e2e/
test-apps
 
 
.env.test.example
.env.test.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.release-plz.toml
.release-plz.toml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.json
biome.json
 
 
cliff.toml
cliff.toml
 
 
context7.json
context7.json
 
 
hk.pkl
hk.pkl
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
renovate.json
renovate.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# Alien

Alien provides infrastructure to deploy and operate software inside your users' environments, while retaining centralized control over updates, monitoring, and lifecycle management.

## Why Alien?

Self-hosting works -until someone starts paying for your software.

Customers run it in their own environment, but they don't actually know how to operate it. They might change something small like Postgres version, environment variables, IAM, firewall rules, and things start failing. From their perspective, your product is broken. And even if the root cause is on their side, it doesn't matter... the customer is always right, you're still the one expected to fix it.

But you can't. You don't have access to their environment. You don't have real visibility. You can't run anything yourself. So you're stuck debugging a system you don't control, through screenshots and copy-pasted logs on a Zoom call. You end up responsible for something you don't control.

Alien provides a better model:managed self-hosting.

## Quickstart

Install the CLI:

curl -fsSL https://alien.dev/install 
|
 sh -s -- --login

irm https:
//
alien.dev
/
install.ps1 
|
 iex

Create a project and start developing:

alien init

cd
 alien 
&&
 alien dev

Follow theQuickstartguide to build an AI worker, test it locally, and deploy it — no cloud account needed to start.

Ortry it with Claude Code, Codex, or Cursor.

### CLI automation

Every platform workflow has a non-interactive form. Link a directory once, then
commands use that project unless--projectis provided explicitly:

alien login
alien projects list
alien link --project my-project
alien projects describe --json

#
 Configure project capabilities.

alien projects capabilities 
enable
 models \
 --model byo/claude-opus-5 \
 --provider anthropic

#
 Create a least-privileged key and onboard a customer environment.

alien api-keys create --for ai-gateway --description production-backend --json
alien onboard acme --external-id customer_123 --setup-items models,keys --json

#
 Print an executable request for the active environment.

alien examples ai-gateway --protocol anthropic-messages

#
 Search structured gateway diagnostics without writing a raw query.

alien logs --source ai-gateway --status provider-error --provider anthropic --json

#
 Inspect live rollout state without parsing the raw stack state.

alien deployments status production/api
alien deployments resources production/api --json
alien deployments 
wait
 production/api --for ready --timeout 10m --json

#
 Read privacy-safe aggregate usage.

alien usage ai --range 7d --json

Resource detail commands acceptget,describe, andshow; list commands
accept bothlistandls. JSON mode never prompts and writes structured data
to stdout, making the same CLI suitable for humans, scripts, and coding agents.
The normalized resource view intentionally excludes resource configuration,
internal controller state, environment variables, and arbitrary provider
outputs.

## Features

* AWS, GCP, and Azure support- Deploy to all major clouds.
* TypeScript & Rust— First-class support for both. Python and arbitrary containers coming soon.
* Real-time Heartbeat— Know the instant a deployment goes down.
* Auto Updates & Rollbacks— Push a release and every remote environment picks it up automatically.
* Local-first Development— Build and test on your machine. Local equivalents for every cloud resource.
* Cloud-agnostic Infrastructure— Ship to AWS, GCP, and Azure customers without maintaining separate integrations. Alien maps a single API to each cloud's native services at deploy time.
* Remote Commands— Invoke code on remote deployments from your control plane. Zero inbound networking. Zero open ports. No VPC peering.
* Observability— Logs, metrics, and traces from every deployment. Full visibility without touching customer infrastructure.
* Least-privilege Permissions— Alien derives the exact IAM permissions required to deploy and manage your app.

## How deployment works

### Push model

Like sharing a Google Drive folder.The customer grants least-privilege access to an isolated area in their cloud. You runalien serveon your infrastructure and it manages everything through cloud APIs (e.g. AWSUpdateWorkerCode). No network connection to their environment needed.

alien serve

 ╔═ Customer's Cloud ══════════════════╗
 ║ ║
 ║ Their databases, services, infra ║
 ║ ║
╔═ alien serve ═══════════╗ ║ ┌─ Isolated Area ──────────────┐ ║
║ ║ cloud APIs ║ │ │ ║
║ Push updates ───────╬───────────────────╬─▶│ ┏━━━━━━━━━━┓ │ ║
║ Collect telemetry ◀────╬───────────────────╬──│ ┃ Worker ┃ │ ║
║ Run commands ───────╬───────────────────╬─▶│ ┗━━━━━━━━━━┛ │ ║
║ ║ ║ │ ┏━━━━━━━━━━┓ │ ║
║ ║ ║ │ ┃ Storage ┃ │ ║
╚═════════════════════════╝ ║ │ ┗━━━━━━━━━━┛ │ ║
 ║ └──────────────────────────────┘ ║
 ║ ║
 ╚═════════════════════════════════════╝

### Pull model

Like an app checking for updates.For customers that can't or won't allow a cross-account IAM role, they can runalien-operatorin their environment instead. It connects outbound to the Alien server, fetches releases, and deploys locally. No inbound connections, no open ports.

docker run ghcr.io/alienplatform/alien-operator \
 --sync-url https://alien.example.com \
 --sync-token 
<
token
>
 \
 --platform aws

 ╔═ Customer's Cloud ══════════════════╗
 ║ ║
 ║ Their databases, services, infra ║
 ║ ║
╔═ alien serve ═══════════╗ outbound ║ ┌─ Isolated Area ──────────────┐ ║
║ ║ HTTPS ║ │ │ ║
║ Releases ◀──────╬───────────────────╬──│── alien-operator │ ║
║ Telemetry ◀──────╬───────────────────╬──│── ┏━━━━━━━━━━┓ │ ║
║ Worker commands ◀──────╬───────────────────╬──│── ┃ Worker ┃ │ ║
║ ║ ║ │ ┗━━━━━━━━━━┛ │ ║
║ ║ ║ │ ┏━━━━━━━━━━┓ │ ║
╚═════════════════════════╝ ║ │ ┃ Storage ┃ │ ║
 ║ │ ┗━━━━━━━━━━┛ │ ║
 ║ └──────────────────────────────┘ ║
 ║ ║
 ╚═════════════════════════════════════╝

Both models give you the same capabilities: updates, telemetry, remote commands. SeeDeployment Models.

The Operator reconciles releases and relays pending Worker commands to the
targeted Worker runtime; the Worker never polls the command server. Containers
and Daemons run an app-owned pull receiver. Every command is scoped to one
target.

## One codebase, every cloud

Ship to AWS, GCP, and Azure customers without maintaining separate integrations. Alien maps your stack to each cloud's native services at deploy time.

import
 
*
 
as
 
alien
 
from
 
"@alienplatform/core"

const
 
data
 
=
 
new
 
alien
.
Storage
(
"data"
)
.
build
(
)

const
 
secrets
 
=
 
new
 
alien
.
Vault
(
"credentials"
)
.
build
(
)

const
 
api
 
=
 
new
 
alien
.
Worker
(
"api"
)

 
.
code
(
{
 
type
: 
"source"
,
 
src
: 
"./api"
,
 
toolchain
: 
{
 
type
: 
"typescript"
 
}
 
}
)

 
.
link
(
data
)

 
.
link
(
secrets
)

 
.
commandsEnabled
(
true
)

 
.
publicEndpoint
(
"api"
)

 
.
build
(
)

export
 
default
 
new
 
alien
.
Stack
(
"my-app"
)

 
.
add
(
api
,
 
"live"
)

 
.
add
(
data
,
 
"frozen"
)

 
.
add
(
secrets
,
 
"frozen"
)

 
.
build
(
)

At deploy time, each resource maps to the cloud's native service:

 ┏━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━┓
 ┃ Worker ┃ ┃ Storage ┃
 ┗━━━━━┯━━━━━━┛ ┗━━━━━┯━━━━━━┛
 │ │
 ├── AWS ───▶ Lambda ├── AWS ───▶ S3
 ├── GCP ───▶ Cloud Run ├── GCP ───▶ Google Cloud Storage
 └── Azure ─▶ Container App └── Azure ─▶ Azure Blob Storage

The same applies to queues, vaults, and KV stores. One codebase, all clouds. Drop to native SDKs whenever you need to.

Each resource documents itsguarantees, limits, and platform-specific behaviorso you know exactly what to expect across clouds.

## Releases

Push a release and every environment updates automatically.

alien release

Builds your code, pushes artifacts, and creates a release. Every active deployment picks up the new version.

## What you can build

* AI Worker— Operator harness in your cloud, tool execution in theirs. Read files, run commands, query data — all local. (example)
* Data Connector— Query Snowflake, Postgres, or any private database. No shared credentials, no exposed services. (example)
* Browser Automation— Headless browser inside their network. Navigate Jira, SAP, GitLab, on-prem wikis.
* Security Outpost— Scan IAM policies, storage, network configs from inside the perimeter. On a schedule or on-demand.
* Cloud Actions— API inside their network. Restart services, rotate credentials, react to infrastructure changes. (example)

## Remote commands

Invoke code inside the customer's environment from your control plane. Zero inbound networking, zero open ports.

Define a handler in the customer's environment:

import
 
{
 
command
,
 
storage
 
}
 
from
 
"@alienplatform/sdk"

const
 
files
 
=
 
storage
(
"files"
)

command
(
"read-file"
,
 
async
 
(
{
 path 
}
)
 
=>
 
{

 
const
 
data
 
=
 
await
 
files
.
get
(
path
)

 
return
 
{
 
content
: 
new
 
TextDecoder
(
)
.
decode
(
data
)
 
}

}
)

Invoke it from your backend:

import
 
{
 
CommandsClient
 
}
 
from
 
"@alienplatform/commands"

const
 
commands
 
=
 
new
 
CommandsClient
(
{
 managerUrl
,
 deploymentId
,
 token 
}
)

const
 
result
 
=
 
await
 
commands
.
target
(
"api"
)
.
invoke
(
"read-file"
,
 
{

 
path
: 
"report.csv"

}
)

SeeRemote Commands.

## Least-privilege permissions

You're deploying to someone else's cloud. Every permission needs justification. Alien derives exactly the permissions needed from your stack definition — for AWS, GCP, and Azure.

export
 
default
 
new
 
alien
.
Stack
(
"my-app"
)

 
.
add
(
data
,
 
"frozen"
)

 
.
add
(
api
,
 
"live"
)

 
.
permissions
(
{

 
profiles
: 
{

 
execution
: 
{

 
data
: 
[
"storage/data-read"
,
 
"storage/data-write"
]
,

 
}
,

 
}
,

 
}
)

 
.
build
(
)

From this definition, Alien derives three layers of permissions:

Provisioning— Creates all resources during initial setup. The customer's admin runsalien-deploy deployonce with their own credentials. Alien never holds these permissions.

Management— What Alien uses day-to-day to manage the deployment:

* 🧊Frozenresources: health checks only. No ability to modify, delete, or read data.
* 🔁Liveresources: push code, roll config, redeploy. But still no data access — Alien can calllambda:UpdateWorkerCodebut nevers3:GetObject. Management and data access are separate.

Application runtime— What the deployed code can access. Only what's declared in permission profiles. Theexecutionprofile above grantsstorage/data-readandstorage/data-writeon thedatabucket — nothing else. No declaration, no access.

Permission sets are portable across clouds:

storage/data-read

AWS

s3:GetObject
, 
s3:ListBucket

GCP

storage.objects.get
, 
storage.objects.list

Azure

Microsoft.Storage/.../blobs/read

For edge cases, define custom permission sets with cloud-specific actions:

const
 
assumeRole
: 
PermissionSet
 
=
 
{

 
id
: 
"assume-role"
,

 
platforms
: 
{

 
aws
: 
[
{

 
grant
: 
{
 
actions
: 
[
"sts:AssumeRole"
]
 
}
,

 
binding
: 
{
 
stack
: 
{
 
resources
: 
[
"*"
]
 
}
 
}

 
}
]

 
}

}

SeePermissionsandFrozen & Live.

## Production deployment

1. Generate a config template:

alien serve --init 
#
 creates alien-manager.toml

2. Provision cloud resources for push-mode platforms(optional — Terraform modules forAWS,GCP,Azure):

module
 
"alien_infra"
 {
 
source
 
=
 
"
github.com/aliendotdev/alien//infra/aws
"

 
name
 
=
 
"
my-project
"

 
principal_arn
 
=
 
aws_iam_role
.
manager
.
arn

}

Fill the Terraform outputs intoalien-manager.toml.

3. Run the server.The server must be reachable over HTTPS — deployments and agents connect back to it.

docker run -d -p 8080:8080 \
 -v alien-data:/data \
 -v ./alien-manager.toml:/app/alien-manager.toml \
 -e BASE_URL=https://manager.example.com \
 ghcr.io/alienplatform/alien-manager

See theSelf-Hosting Guidefor the full configuration reference and production checklist.

## Documentation

* Quickstart— build and deploy an AI worker
* How Alien Works— architecture and core concepts
* Stacks— defining your infrastructure
* Frozen and Live— the security/control tradeoff
* Deployment Models— push vs pull
* Remote Commands— invoking code in customer environments
* Permissions— least-privilege access control

## Community

* Slack— get help and share feedback
* GitHub Issues— bug reports and feature requests
* X— updates and announcements