---
title: 'GitHub - coder/coder: Secure environments for developers and their agents · GitHub'
url: https://github.com/coder/coder
site_name: github
content_file: github-github-codercoder-secure-environments-for-develope
fetched_at: '2026-09-17T15:26:50.243940'
original_url: https://github.com/coder/coder
author: coder
description: Secure environments for developers and their agents - coder/coder
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 coder

 

/

coder

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star14.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

16,492 Commits
16,492 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
agent
agent
 
 
aibridge
aibridge
 
 
apiversion
apiversion
 
 
archive
archive
 
 
buildinfo
buildinfo
 
 
cli
cli
 
 
cmd
cmd
 
 
coderd
coderd
 
 
codersdk
codersdk
 
 
cryptorand
cryptorand
 
 
docs
docs
 
 
dogfood
dogfood
 
 
enterprise
enterprise
 
 
examples
examples
 
 
helm
helm
 
 
httpmw
httpmw
 
 
offlinedocs
offlinedocs
 
 
provisioner
provisioner
 
 
provisionerd
provisionerd
 
 
provisionersdk
provisionersdk
 
 
pty
pty
 
 
scaletest
scaletest
 
 
scripts
scripts
 
 
site
site
 
 
support
support
 
 
tailnet
tailnet
 
 
testutil
testutil
 
 
vpn
vpn
 
 
.cursorrules
.cursorrules
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yaml
.golangci.yaml
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
.markdownlint.jsonc
.markdownlint.jsonc
 
 
.mcp.json
.mcp.json
 
 
.swaggo
.swaggo
 
 
.vale.ini
.vale.ini
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
LICENSE.enterprise
LICENSE.enterprise
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.jsonc
biome.jsonc
 
 
catalog-info.yaml
catalog-info.yaml
 
 
coder.env
coder.env
 
 
compose.dev.yaml
compose.dev.yaml
 
 
compose.yaml
compose.yaml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
mise.lock
mise.lock
 
 
mise.toml
mise.toml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
release.key
release.key
 
 
server.json
server.json
 
 
shell.nix
shell.nix
 
 
View all files

## Repository files navigation

# Self-Hosted Cloud Development Environments and AI Agents

Quickstart|Docs|Why Coder|Premium

Coderis a self-hosted platform for cloud development environments and AI coding agents. Workspaces are defined with Terraform, connected through a secure Wireguard® tunnel, and automatically shut down when not used. Coder Agents runs a native AI coding agent whose loop executes in the control plane on your infrastructure, with no API keys in workspaces.

* Define cloud development environments in TerraformEC2 VMs, Kubernetes Pods, Docker Containers, etc.
* EC2 VMs, Kubernetes Pods, Docker Containers, etc.
* Automatically shutdown idle resources to save on costs
* Onboard developers in seconds instead of days
* Delegate coding work to AI agents on your infrastructureBring any model (Anthropic, OpenAI, Google, Bedrock, self-hosted)No LLM credentials in workspaces, user identity on every actionCentralized model governance, cost tracking, and audit logging
* Bring any model (Anthropic, OpenAI, Google, Bedrock, self-hosted)
* No LLM credentials in workspaces, user identity on every action
* Centralized model governance, cost tracking, and audit logging

## Quickstart

Check out ourinstall guidesfor other methods and a complete tutorial.

Try Coder with theinstall scripton Linux and macOS, or grab the latest binary or installer fromGitHub Releaseson Windows:

curl -L https://coder.com/install.sh 
|
 sh

Start the server and openhttp://localhost:3000to create your initial user, create a Docker template, and provision your first workspace:

coder server

For a production deployment, add a PostgreSQL database (version 13 or later) and an external access URL, and see ourvalidated architecturesfor sizing and infrastructure guidance:

coder server --postgres-url 
<
url
>
 --access-url 
<
url
>

Without these flags, Coder uses a built-in database and sets up a*.try.coder.appaccess URL for evaluation. Usecoder --helpfor the full list of flags and environment variables.

## Documentation

Browse thedocumentationor visit a specific section below:

* Workspaces: Workspaces contain the IDEs, dependencies, and configuration information needed for software development
* Templates: Templates are written in Terraform and describe the infrastructure for workspaces
* Coder Agents: Delegate coding work to AI agents running on your self-hosted infrastructure
* AI Gateway: Centralize authentication, auditing, and cost controls for AI tooling
* Administration: Learn how to operate Coder
* Premium: Learn about paid features built for large teams
* IDEs: Connect your existing editor to a workspace

## Support

Open an issuefor bugs and feature requests.

For community support, showcasing what you built, and feedback on in-progress features, join ourDiscordorGitHub Discussions.

Dedicated support is included in Coder Premium. For more information, visitcoder.com/pricing.

## Integrations

New integrations are always in progress. Open an issue to request one. Contributions are welcome in any official or community repository.

### Official

* Coder Registry: Templates, modules, and integrations for common development environments
* Coding Agents: Run agents like Claude Code, Codex, and OpenCode isolated in Coder workspaces
* coderd Terraform Provider: Declaratively manage your Coder deployment configuration as code
* VS Code Extension: Open any Coder workspace in VS Code with a single click
* JetBrains Toolbox Plugin: Open any Coder workspace from JetBrains Toolbox with a single click
* Dev Containers: Build development environments usingdevcontainer.jsonon Docker, Kubernetes, and OpenShift
* Kubernetes Log Stream: Stream Kubernetes Pod events to the Coder startup logs
* Self-Hosted VS Code Extension Marketplace: A private extension marketplace that works in restricted or airgapped networks integrating withcode-server.
* GitHub Actions: An action to set up the Coder CLI in GitHub workflows

### Community

* Coder Discord: Chat with the community, get support, and hear about new product updates first
* Community Templates: Community-contributed workspace templates in the Coder Registry
* Community Modules: Community-contributed modules to extend Coder templates
* Coder Template GitHub Action: A GitHub Action that updates Coder templates
* Coder Agents Chat Action: A GitHub Action that starts a Coder Agents chat against a GitHub issue or pull request

## Contributing

New contributors are always welcome. If you are new to the Coder codebase, seethe contribution guideto get started.

## Hiring

Apply on thecareers pageif you are interested in joining the team.