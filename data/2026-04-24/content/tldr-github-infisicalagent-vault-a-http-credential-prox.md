---
title: 'GitHub - Infisical/agent-vault: A HTTP credential proxy and vault for AI agents · GitHub'
url: https://github.com/Infisical/agent-vault
site_name: tldr
content_file: tldr-github-infisicalagent-vault-a-http-credential-prox
fetched_at: '2026-04-24T19:51:23.298321'
original_url: https://github.com/Infisical/agent-vault
date: '2026-04-24'
description: A HTTP credential proxy and vault for AI agents. Contribute to Infisical/agent-vault development by creating an account on GitHub.
tags:
- tldr
---

Infisical

 

/

agent-vault

Public

* NotificationsYou must be signed in to change notification settings
* Fork28
* Star626

 
 
 
 
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

129 Commits
129 Commits
.claude
.claude
 
 
.github
.github
 
 
assets
assets
 
 
cmd
cmd
 
 
docs
docs
 
 
internal
internal
 
 
scripts
scripts
 
 
sdks/
sdk-typescript
sdks/
sdk-typescript
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.goreleaser
Dockerfile.goreleaser
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
fly.toml
fly.toml
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
main.go
main.go
 
 
skills-lock.json
skills-lock.json
 
 
View all files

## Repository files navigation

HTTP credential proxy and vault

An open-source credential broker byInfisicalthat sits between your agents and the APIs they call.Agents should not possess credentials. Agent Vault eliminates credential exfiltration risk with brokered access.

New here? Thelaunch blog posthas the full story behind Agent Vault.

Documentation|Installation|CLI Reference|Slack

## Why Agent Vault

Traditional secrets management relies on returning credentials directly to the caller. This breaks down with AI agents, which are non-deterministic systems vulnerable to prompt injection that can be fooled into leaking its secrets.

Agent Vault takes a different approach:Agent Vault never reveals vault-stored credentials to agents. Instead, agents route HTTP requests through a local proxy that injects the right credentials at the network layer.

* Brokered access, not retrieval- Your agent gets a scoped session and a localHTTPS_PROXY. It calls target APIs normally, and Agent Vault injects the right credential at the network layer. Credentials are never returned to the agent.
* Works with any agent- Custom Python/TypeScript agents, sandboxed processes, and coding agents like Claude Code, Cursor, and Codex. Anything that speaks HTTP.
* Encrypted at rest- Credentials are encrypted with AES-256-GCM using a random data encryption key (DEK). An optional master password wraps the DEK via Argon2id, so rotating the password does not re-encrypt credentials. A passwordless mode is available for PaaS deploys.
* Request logs- Every proxied request is persisted per vault with method, host, path, status, latency, and the credential key names involved. Bodies, headers, and query strings are not recorded. Retention is configurable per vault.

## Installation

See theinstallation guidefor full details.

### Script (macOS / Linux)

curl -fsSL https://get.agent-vault.dev 
|
 sh
agent-vault server -d

Supports macOS (Intel + Apple Silicon) and Linux (x86_64 + ARM64).

### Docker

docker run -it -p 14321:14321 -p 14322:14322 -v agent-vault-data:/data infisical/agent-vault

For non-interactive environments (Docker Compose, CI, detached mode), pass the master password as an env var:

docker run -d -p 14321:14321 -p 14322:14322 \
 -e AGENT_VAULT_MASTER_PASSWORD=your-password \
 -v agent-vault-data:/data infisical/agent-vault

### From source

RequiresGo 1.25+andNode.js 22+.

git clone https://github.com/Infisical/agent-vault.git

cd
 agent-vault
make build
sudo mv agent-vault /usr/local/bin/
agent-vault server -d

The server starts the HTTP API on port14321and a TLS-encrypted transparent HTTPS proxy on port14322. A web UI is available athttp://localhost:14321.

## Quickstart

### CLI — local agents (Claude Code, Cursor, Codex, OpenClaw, Hermes, OpenCode)

Wrap any local agent process withagent-vault run(long form:agent-vault vault run). Agent Vault creates a scoped session, setsHTTPS_PROXYand CA-trust env vars, and launches the agent — all HTTPS traffic is transparently proxied and authenticated:

agent-vault run -- claude
agent-vault vault run -- agent
agent-vault vault run -- codex
agent-vault vault run -- opencode

The agent calls APIs normally (e.g.fetch("https://api.github.com/...")). Agent Vault intercepts the request, injects the credential, and forwards it upstream. The agent never sees secrets.

Fornon-cooperativesandboxing — where the child physically cannot reach anything except the Agent Vault proxy, regardless of what it tries — launch it in a Docker container with egress locked down by iptables:

agent-vault run --sandbox=container --share-agent-dir -- claude

--share-agent-dirbind-mounts your host's~/.claudeinto the container so the sandboxed agent reuses your existing login. Currently Claude-only; support for other agents is coming soon.

SeeContainer sandboxfor the threat model and flags.

### SDK — sandboxed agents (Docker, Daytona, E2B)

For agents running inside containers, use the SDK from your orchestrator to mint a session and pass proxy config into the sandbox:

npm install @infisical/agent-vault-sdk

import
 
{
 
AgentVault
,
 
buildProxyEnv
 
}
 
from
 
"@infisical/agent-vault-sdk"
;

const
 
av
 
=
 
new
 
AgentVault
(
{

 
token
: 
"YOUR_TOKEN"
,

 
address
: 
"http://localhost:14321"
,

}
)
;

const
 
session
 
=
 
await
 
av

 
.
vault
(
"default"
)

 
.
sessions
.
create
(
{
 
vaultRole
: 
"proxy"
 
}
)
;

// certPath is where you'll mount the CA certificate inside the sandbox.

const
 
certPath
 
=
 
"/etc/ssl/agent-vault-ca.pem"
;

// env: { HTTPS_PROXY, NO_PROXY, NODE_USE_ENV_PROXY, SSL_CERT_FILE,

// NODE_EXTRA_CA_CERTS, REQUESTS_CA_BUNDLE, CURL_CA_BUNDLE,

// GIT_SSL_CAINFO
, DENO_CERT 
}

const
 
env
 
=
 
buildProxyEnv
(
session
.
containerConfig
!
,
 
certPath
)
;

const
 
caCert
 
=
 
session
.
containerConfig
!
.
caCertificate
;

// Pass `env` as environment variables and mount `caCert` at `certPath`

// in your sandbox — Docker, Daytona, E2B, Firecracker, or any other runtime.

// Once configured, the agent inside just calls APIs normally:

// fetch("https://api.github.com/...") — no SDK, no credentials needed.

See theTypeScript SDK READMEfor full documentation.

## Development

make build 
#
 Build frontend + Go binary

make 
test
 
#
 Run tests

make web-dev 
#
 Vite dev server with hot reload (port 5173)

make dev 
#
 Go + Vite dev servers with hot reload

make docker 
#
 Build Docker image

## Open-source vs. paid

This repo available under theMIT expat license, with the exception of theeedirectory which will contain premium enterprise features requiring a Infisical license.

If you are interested in Infisical or exploring a more commercial path for Agent Vault, take a look atour websiteorbook a meeting with us.

## Contributing

Whether it's big or small, we love contributions. Agent Vault follows the same contribution guidelines as Infisical.

Check out our guide to see how toget started.

Not sure where to get started? You can:

* Join ourSlack, and ask us any questions there.

## We are hiring!

If you're reading this, there is a strong chance you like the products we created.

You might also make a great addition to our team. We're growing fast and would love for you tojoin us.

Preview.Agent Vault is in active development and the API is subject to change. Please review thesecurity documentationbefore deploying.

## About

A HTTP credential proxy and vault for AI agents

docs.agent-vault.dev

### Topics

 agents

 ai-agents

 secrets-management

### Resources

 Readme

 

### License

 View license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

626

 stars
 

### Watchers

0

 watching
 

### Forks

28

 forks
 

 Report repository

 

## Releases15

v0.10.0

 Latest

 

Apr 23, 2026

 

+ 14 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go71.0%
* TypeScript27.0%
* HTML0.9%
* Shell0.7%
* CSS0.2%
* Dockerfile0.1%
* Makefile0.1%