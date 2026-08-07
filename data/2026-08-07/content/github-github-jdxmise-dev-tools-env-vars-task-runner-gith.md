---
title: 'GitHub - jdx/mise: dev tools, env vars, task runner · GitHub'
url: https://github.com/jdx/mise
site_name: github
content_file: github-github-jdxmise-dev-tools-env-vars-task-runner-gith
fetched_at: '2026-08-07T11:43:55.694642'
original_url: https://github.com/jdx/mise
author: jdx
description: dev tools, env vars, task runner. Contribute to jdx/mise development by creating an account on GitHub.
---

jdx

 

/

mise

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star32k

 
 
 
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

8,059 Commits
8,059 Commits
.cargo
.cargo
 
 
.claude/
agents
.claude/
agents
 
 
.codex
.codex
 
 
.config
.config
 
 
.cursor
.cursor
 
 
.entire
.entire
 
 
.github
.github
 
 
.idea
.idea
 
 
benchmarks
benchmarks
 
 
cloudflare/
workers
cloudflare/
workers
 
 
completions
completions
 
 
crates
crates
 
 
docs
docs
 
 
e2e-win
e2e-win
 
 
e2e
e2e
 
 
licenses
licenses
 
 
man/
man1
man/
man1
 
 
packaging
packaging
 
 
registry
registry
 
 
schema
schema
 
 
scripts
scripts
 
 
share/
fish/
vendor_conf.d
share/
fish/
vendor_conf.d
 
 
src
src
 
 
test
test
 
 
vendor/
aqua-registry
vendor/
aqua-registry
 
 
xtasks
xtasks
 
 
.cliffignore
.cliffignore
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.markdown-link-check.json
.markdown-link-check.json
 
 
.markdownlint.json
.markdownlint.json
 
 
.markdownlintignore
.markdownlintignore
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.toml
.prettierrc.toml
 
 
.release-skip-e2e
.release-skip-e2e
 
 
.shellcheckrc
.shellcheckrc
 
 
.taplo.toml
.taplo.toml
 
 
.yamllint.yml
.yamllint.yml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Cross.toml
Cross.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
age.pub
age.pub
 
 
build.rs
build.rs
 
 
bun.lock
bun.lock
 
 
cliff.toml
cliff.toml
 
 
clippy.toml
clippy.toml
 
 
communique.toml
communique.toml
 
 
default.nix
default.nix
 
 
deny.toml
deny.toml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
greptile.json
greptile.json
 
 
hk.pkl
hk.pkl
 
 
llms.txt
llms.txt
 
 
minisign.key.age
minisign.key.age
 
 
minisign.pub
minisign.pub
 
 
mise.code-workspace
mise.code-workspace
 
 
mise.lock
mise.lock
 
 
mise.toml
mise.toml
 
 
mise.usage.kdl
mise.usage.kdl
 
 
package.json
package.json
 
 
pitchfork.toml
pitchfork.toml
 
 
settings.toml
settings.toml
 
 
snapcraft.yaml
snapcraft.yaml
 
 
tak.toml
tak.toml
 
 
tasks.md
tasks.md
 
 
tasks.toml
tasks.toml
 
 
tsconfig.json
tsconfig.json
 
 
zipsign.pub
zipsign.pub
 
 
View all files

## Repository files navigation

# mise-en-place

Dev tools, env vars, and tasks in one CLI

Getting Started•Documentation•Dev Tools•Environments•Tasks

Sponsored byentire.ioand37signals.View all sponsors.

Tip

My latest project,aubejust hit stable! It's the fastest Node.js package manager with strong security defaults and is compatible with npm/pnpm/yarn lockfiles!

## What is it?

miseprepares your development environment before each command runs. It keeps
project tools, environment variables, and tasks in onemise.tomlfile so new
shells, checkouts, and CI jobs all start from the same setup.

* Install and switch betweendev toolslike node, python, cmake, terraform, andhundreds more.
* Loadenvironment variablesper project directory, including values from.envfiles and other sources.
* Define and runtasksfor building, testing, linting, and deploying projects.

## Demo

The following demo shows how to install and usemiseto manage multiple versions ofnodeon the same system.
Note that callingwhich nodegives us a real path to node, not a shim.

It also shows that you can usemiseto install and many other tools such asjq,terraform, orgo.

Seedemo transcript.

## Quickstart

### Install mise

SeeGetting startedfor more options.

$ 
curl https://mise.run 
|
 sh

$ 
~
/.local/bin/mise --version

 _ __

 ____ ___ (_)_______ ___ ____ ____ / /___ _________

 / __ `__ \/ / ___/ _ \______/ _ \/ __ \______/ __ \/ / __ `/ ___/ _ \

 / / / / / / (__ ) __/_____/ __/ / / /_____/ /_/ / / /_/ / /__/ __/

/_/ /_/ /_/_/____/\___/ \___/_/ /_/ / .___/_/\__,_/\___/\___/

 /_/ by @jdx

2026.8.2 macos-arm64 (2026-08-04)

Hook mise into your shell (pick the right one for your shell):

# 
note this assumes mise is located at 
~
/.local/bin/mise

# 
which is what https://mise.run does by default

echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc

echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc

echo '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish

echo '~/.local/bin/mise activate pwsh | Out-String | Invoke-Expression' >> ~/.config/powershell/Microsoft.PowerShell_profile.ps1

### Execute commands with specific tools

$ 
mise 
exec
 node@26 -- node -v

mise node@26.x.x ✓ installed

v26.x.x

### Install tools

$ 
mise use --global node@26 go@1

$ 
node -v

v26.x.x

$ 
go version

go version go1.x.x macos/arm64

Seedev toolsfor more examples.

### Manage environment variables

#
 mise.toml

[
env
]

SOME_VAR
 = 
"
foo
"

$ 
mise 
set
 SOME_VAR=bar

$ 
echo
 
$SOME_VAR

bar

Note thatmisecan alsoload.envfiles.

### Run tasks

#
 mise.toml

[
tasks
.
build
]

description
 = 
"
build the project
"

run
 = 
"
echo building...
"

$ 
mise run build

building...

Seetasksfor more information.

### Example mise project

Here is a combined example to give you an idea of how you can use mise to manage your a project's tools, environment, and tasks.

#
 mise.toml

[
tools
]

terraform
 = 
"
1
"

aws-cli
 = 
"
2
"

[
env
]

TF_WORKSPACE
 = 
"
development
"

AWS_REGION
 = 
"
us-west-2
"

AWS_PROFILE
 = 
"
dev
"

[
tasks
.
plan
]

description
 = 
"
Run terraform plan with configured workspace
"

run
 = 
"""

terraform init

terraform workspace select $TF_WORKSPACE

terraform plan

"""

[
tasks
.
validate
]

description
 = 
"
Validate AWS credentials and terraform config
"

run
 = 
"""

aws sts get-caller-identity

terraform validate

"""

[
tasks
.
deploy
]

description
 = 
"
Deploy infrastructure after validation
"

depends
 = [
"
validate
"
, 
"
plan
"
]

run
 = 
"
terraform apply -auto-approve
"

Run it with:

mise install # install tools specified in mise.toml

mise run deploy

Find more examples in themise cookbook.

## Full Documentation

Seemise.jdx.dev

## GitHub Issues & Discussions

Due to the volume of issue submissions mise received, using GitHub Issues became unsustainable for
the project. Instead, mise uses GitHub Discussions which provide a more community-centric platform
for communication and require less management on the part of the maintainers.

Please note the following discussion categories, which match how issues are often used:

* Announcements
* Ideas: for feature requests, etc.
* Troubleshooting & Bug Reports

## Special Thanks

Thanks toNamespacefor providing CI services for mise.

## Contributors