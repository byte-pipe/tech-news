---
title: 'GitHub - superradcompany/microsandbox: 🧱 easy fast local-first microVM runtime and library · GitHub'
url: https://github.com/superradcompany/microsandbox
site_name: github
content_file: github-github-superradcompanymicrosandbox-easy-fast-local
fetched_at: '2026-08-18T11:22:56.795588'
original_url: https://github.com/superradcompany/microsandbox
author: superradcompany
description: 🧱 easy fast local-first microVM runtime and library - superradcompany/microsandbox
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 superradcompany

 

/

microsandbox

Public

* NotificationsYou must be signed in to change notification settings
* Fork406
* Star7.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

921 Commits
921 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.config
.config
 
 
.github
.github
 
 
assets
assets
 
 
crates
crates
 
 
docs
docs
 
 
examples
examples
 
 
mcp @ 4b021dc
mcp @ 4b021dc
 
 
packages
packages
 
 
packaging
packaging
 
 
scripts
scripts
 
 
sdk
sdk
 
 
skills @ b689317
skills @ b689317
 
 
vendor
vendor
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.rustfmt.toml
.rustfmt.toml
 
 
.taplo.toml
.taplo.toml
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
Dockerfile.agentd
Dockerfile.agentd
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
deny.toml
deny.toml
 
 
justfile
justfile
 
 
msb-entitlements.plist
msb-entitlements.plist
 
 
View all files

## Repository files navigation

——   easy, fast, local microVMs for untrusted workloads   ——

Microsandboxrunsuntrusted workloadsinside fast, local microVMs: AI agents, user code, plugins, CI jobs, dev environments, scrapers, and automation.

* Hardware Isolation: Hardware-level isolation with microVM technology.
* Cross Platform: Runs on Linux, macOS, and Windows.
* OCI Compatible: Runs standard container images from Docker Hub, GHCR, or any OCI registry.
* Docker-Like Workflows: Familiar image, command, shell, and volume workflows.
* Instant Startup: Average boot times1under 100 milliseconds.
* Embeddable: Spawn VMs right within your code. No setup server. No long-running daemon.
* Secrets That Can't Leak: Unexploitable secret keys that never enter the VM.
* Long-Running: Sandboxes can run in detached mode. Great for long-lived sessions.
* Agent-Ready: Your agents can create their own sandboxes with ourAgent SkillsandMCP server.

## Getting Started

#### Install the SDK

cargo add microsandbox 
#
 🦀 Rust

uv add microsandbox 
#
 🐍 Python

npm i microsandbox 
#
 🟦 TypeScript

go get github.com/superradcompany/microsandbox/sdk/go 
#
 🐹 Go

#### Install the CLI

Boot a microVM in a single command:

npx microsandbox run debian

Or install themsbcommand globally:

curl -fsSL https://install.microsandbox.dev 
|
 sh 
#
 🍎 macOS / 🐧 Linux

irm https:
//
install.microsandbox.dev
/
windows 
|
 iex 
#
 🪟 Windows

 We also support other package managers →

brew install superradcompany/tap/microsandbox

npm i -g microsandbox

uv tool install microsandbox

cargo install microsandbox

Then you can runmsbdirectly:

msb run debian

Requirements:

* macOS: Apple Silicon.
* Linux: KVM enabled.
* Windows: WHP enabled.

Warning: Microsandbox is stillbeta software. Expect breaking changes, missing features, and rough edges.

## SDK

The SDK lets you create and control sandboxes directly from your application.Sandbox::builder("...").create()boots a microVM as a child process. No infrastructure required.

#### Run Code in a Sandbox

use
 microsandbox
::
Sandbox
;

#
[
tokio
::
main
]

async
 
fn
 
main
(
)
 -> 
Result
<
(
)
,
 
Box
<
dyn
 std
::
error
::
Error
>
>
 
{

 
let
 sandbox = 
Sandbox
::
builder
(
"my-sandbox"
)

 
.
image
(
"python"
)

 
.
cpus
(
1
)

 
.
memory
(
512
)

 
.
create
(
)

 
.
await
?
;

 
let
 output = sandbox
 
.
exec
(
"python"
,
 
[
"-c"
,
 
"print('Hello from a microVM!')"
]
)

 
.
await
?
;

 
println
!
(
"{}"
,
 output
.
stdout
(
)
?
)
;

 sandbox
.
stop
(
)
.
await
?
;

 
Ok
(
(
)
)

}

 Python Example →

import
 
asyncio

from
 
microsandbox
 
import
 
Sandbox

async
 
def
 
main
():
 
sandbox
 
=
 
await
 
Sandbox
.
create
(
 
"my-sandbox"
,
 
image
=
"python"
,
 
cpus
=
1
,
 
memory
=
512
,
 )

 
output
 
=
 
await
 
sandbox
.
exec
(
"python"
, [
"-c"
, 
"print('Hello from a microVM!')"
])

 
print
(
output
.
stdout_text
)

 
await
 
sandbox
.
stop
()

asyncio
.
run
(
main
())

 Ruby Example →

require
 
"microsandbox"

sandbox
 
=
 
Microsandbox
::
Sandbox
.
create
(

 
"my-sandbox"
,

 
image
: 
"python"
,

 
cpus
: 
1
,

 
memory
: 
512
,

 
network
: 
{

 
allowed_hosts
: 
[
"api.openai.com"
]
,

 
allowed_ports
: 
[
443
]

 
}
,

 
secrets
: 
[
{

 
env
: 
"OPENAI_API_KEY"
,

 
value
: 
ENV
.
fetch
(
"OPENAI_API_KEY"
)
,

 
allowed_host
: 
"api.openai.com"

 
}
]

)

output
 
=
 
sandbox
.
exec
(
"python"
,
 
[
"-c"
,
 
"print('Hello from a microVM!')"
]
)

puts
 
output
.
stdout

sandbox
.
stop

See theRuby SDK guidefor installation, lifecycle,
networking, and backend details.

 TypeScript Example →

import
 
{
 
Sandbox
 
}
 
from
 
"microsandbox"
;

await
 using 
sandbox
 
=
 
await
 
Sandbox
.
builder
(
"my-sandbox"
)

 
.
image
(
"python"
)

 
.
cpus
(
1
)

 
.
memory
(
512
)

 
.
create
(
)
;

const
 
output
 
=
 
await
 
sandbox
.
exec
(
"python"
,
 
[

 
"-c"
,

 
"print('Hello from a microVM!')"
,

]
)
;

console
.
log
(
output
.
stdout
(
)
)
;

 Go Example →

package
 main

import
 (
 
"context"

 
"fmt"

 
"log"

 microsandbox 
"github.com/superradcompany/microsandbox/sdk/go"

)

func
 
main
() {
 
ctx
 
:=
 
context
.
Background
()

 
// Downloads the microsandbox runtime to ~/.microsandbox/ on first run.

 
if
 
err
 
:=
 
microsandbox
.
EnsureInstalled
(
ctx
); 
err
 
!=
 
nil
 {
 
log
.
Fatal
(
err
)
 }

 
sandbox
, 
err
 
:=
 
microsandbox
.
CreateSandbox
(
ctx
, 
"my-sandbox"
,
 
microsandbox
.
WithImage
(
"python"
),
 
microsandbox
.
WithCPUs
(
1
),
 
microsandbox
.
WithMemory
(
512
),
 )
 
if
 
err
 
!=
 
nil
 {
 
log
.
Fatal
(
err
)
 }
 
defer
 
sandbox
.
Stop
(
ctx
)

 
output
, 
err
 
:=
 
sandbox
.
Exec
(
ctx
, 
"python"
, []
string
{
"-c"
, 
"print('Hello from a microVM!')"
})
 
if
 
err
 
!=
 
nil
 {
 
log
.
Fatal
(
err
)
 }

 
fmt
.
Println
(
output
.
Stdout
())
}

The first call tocreate()pulls the image if it isn't cached locally, so it may take longer depending on your connection. Subsequent runs reuse the cache.

## CLI

ThemsbCLI provides a complete interface for managing sandboxes, images, and volumes.

#### Run a Command

msb run python -- python3 -c 
"
print('Hello from a microVM!')
"

#### Named Sandboxes

#
 Create and start a named sandbox

msb create --name app python

#
 Execute commands

msb 
exec
 app -- python -c 
"
import this
"

msb 
exec
 app -- curl https://example.com

#
 Lifecycle

msb stop app
msb start app
msb rm app

#### Image Management

msb pull python 
#
 Pull an image

msb image ls 
#
 List cached images

msb image rm python 
#
 Remove an image

#### Configuration File

msb run --conf sandbox.yaml -- octocat

#
 sandbox.yaml

image
: 
python:3.12

network
:
 
allow
:
 - 
api.github.com

scripts
:
 
octocat
: 
|

 python - <<'PY'

 import urllib.request

 request = urllib.request.Request(

 "https://api.github.com/octocat",

 headers={"User-Agent": "microsandbox-example"},

 )

 with urllib.request.urlopen(request) as response:

 print(response.read().decode())

 PY

#### Install & Uninstall Sandboxes

msb install ubuntu 
#
 Install ubuntu sandbox as 'ubuntu' command

ubuntu 
#
 Opens Ubuntu in a microVM

msb uninstall ubuntu 
#
 Uninstall the ubuntu sandbox

#### Status & Inspection

msb ls 
#
 List all sandboxes

msb ps app 
#
 Show sandbox status

msb inspect app 
#
 Detailed sandbox info

msb metrics app 
#
 Live CPU/memory/network stats

Tip

Run:·msb --helpfor quick help menu.·msb --treefor complete command hierarchy and descriptions.·msb <command> --treefor a specific command tree.

## Examples

Practical ways to put microsandbox to work:

•Docker in a Sandbox: Run Docker without touching the host daemon.•OpenCode: Give a coding agent an isolated project workspace.•Playwright: Run headless browser jobs inside a microVM.•Warm Workers: Snapshot a toolchain and launch clean workers.•Migration Rehearsal: Test a database migration, then restore the baseline.•GitHub Actions Runner: Run each self-hosted job in a disposable microVM.•Documents to PDF: Convert untrusted documents in a fresh offline worker.

## AI Agents

#### Agent Skills

Teach any AI coding agent how to use microsandbox by installing theAgent Skills. Works with Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, and more.

npx skills add superradcompany/skills

#### MCP Server

Connect any MCP-compatible agent to microsandbox with theMCP server. Provides structured tool calls for sandbox lifecycle, command execution, filesystem access, volumes, and monitoring.

#
 Claude Code

claude mcp add --transport stdio microsandbox -- npx -y microsandbox-mcp

## Projects using microsandbox

⏵Eve by Vercel⏵GSA TTS Agentic Coding Quickstart⏵agent-compose by Chaitin⏵ConduktandOnceby Tuist⏵h5i⏵Smithers⏵sandboxed-lit by LlamaIndex⏵Agentic Usability by PSPDFKit Labs⏵Agent VM by Wiren Board⏵Devsy

Built something with microsandbox?Share it with us on Discord. We’d love to feature it here.

## Documentation

For guides, API references, and examples, visit themicrosandbox documentation.

## Contributing

Interested in contributing tomicrosandbox? Check out ourCONTRIBUTING.mdfor guidelines andDEVELOPMENT.mdfor build, test, and release instructions.

## License

This project is licensed under theApache License 2.0.

## Acknowledgements

Special thanks to all our contributors, testers, and community members who help make microsandbox better every day! We'd like to thank the following projects and communities that mademicrosandboxpossible:libkrunandsmoltcp

## Footnotes

1. Boot time refers to guest boot on an M1 machine.↩