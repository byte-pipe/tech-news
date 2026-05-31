---
title: 'GitHub - nesquena/hermes-webui: Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! · GitHub'
url: https://github.com/nesquena/hermes-webui
site_name: github
content_file: github-github-nesquenahermes-webui-hermes-webui-the-best
fetched_at: '2026-06-01T04:17:15.716265'
original_url: https://github.com/nesquena/hermes-webui
author: nesquena
description: 'Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! - nesquena/hermes-webui'
---

nesquena

 

/

hermes-webui

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star9.8k

 
 
 
 
master
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

3,540 Commits
3,540 Commits
.github/
workflows
.github/
workflows
 
 
api
api
 
 
docs
docs
 
 
scripts
scripts
 
 
static
static
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.docker.example
.env.docker.example
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
BUGS.md
BUGS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
DESIGN.md
DESIGN.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SPRINTS.md
SPRINTS.md
 
 
TESTING.md
TESTING.md
 
 
THEMES.md
THEMES.md
 
 
bootstrap.py
bootstrap.py
 
 
ctl.sh
ctl.sh
 
 
docker-compose.three-container.yml
docker-compose.three-container.yml
 
 
docker-compose.two-container.yml
docker-compose.two-container.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
docker_init.bash
docker_init.bash
 
 
eslint.runtime-guard.config.mjs
eslint.runtime-guard.config.mjs
 
 
mcp_server.py
mcp_server.py
 
 
package.json
package.json
 
 
pytest.ini
pytest.ini
 
 
requirements.txt
requirements.txt
 
 
server.py
server.py
 
 
start.ps1
start.ps1
 
 
start.sh
start.sh
 
 
View all files

## Repository files navigation

# Hermes Web UI

Hermes Agentis a sophisticated autonomous agent that lives on your server, accessed via a terminal or messaging apps, that remembers what it learns and gets more capable the longer it runs.

Hermes WebUI is a lightweight, dark-themed web app interface in your browser forHermes Agent.
Full parity with the CLI experience - everything you can do from a terminal,
you can do from this UI. No build step, no framework, no bundler. Just Python
and vanilla JS.

Layout: three-panel. Left sidebar for sessions and navigation, center for chat,
right for workspace file browsing. Model, profile, and workspace controls live in
thecomposer footer— always visible while composing. A circular context ring
shows token usage at a glance. All settings and session tools are in theHermes Control Center(launcher at the sidebar bottom).

Light mode with full profile support

Customize your settings, configure a password

Workspace file browser with inline preview

Session projects, tags, and tool call cards

This gives you nearly1:1 parity with Hermes CLI from a convenient web UIwhich you can access securely through an SSH tunnel from your Hermes setup. Single command to start this up, and a single command to SSH tunnel for access on your computer. Every single part of the web UI uses your existing Hermes agent and existing models, without requiring any additional setup.

## Why Hermes

Most AI tools reset every session. They don't know who you are, what you worked on, or what
conventions your project follows. You re-explain yourself every time.

Hermes retains context across sessions, runs scheduled jobs while you're offline, and gets
smarter about your environment the longer it runs. It uses your existing Hermes agent setup,
your existing models, and requires no additional configuration to start.

What makes it different from other agentic tools:

* Persistent memory— user profile, agent notes, and a skills system that saves reusable
procedures; Hermes learns your environment and does not have to relearn it
* Self-hosted scheduling— cron jobs that fire while you're offline and deliver results to
Telegram, Discord, Slack, Signal, email, and more
* 10+ messaging platforms— the same agent available in the terminal is reachable from your phone
* Self-improving skills— Hermes writes and saves its own skills automatically from experience;
no marketplace to browse, no plugins to install
* Provider-agnostic— OpenAI, Anthropic, Google, DeepSeek, OpenRouter, and more
* Orchestrates other agents— can spawn Claude Code or Codex for heavy coding tasks and bring
the results back into its own memory
* Self-hosted— your conversations, your memory, your hardware

vs. the field(landscape is actively shifting — seedocs/why-hermes.mdfor the full breakdown):

OpenClaw

Claude Code

Codex CLI

OpenCode

Hermes

Persistent memory (auto)

Yes

Partial†

Partial

Partial

Yes

Scheduled jobs (self-hosted)

Yes

No‡

No

No

Yes

Messaging app access

Yes (15+ platforms)

Partial (Telegram/Discord preview)

No

No

Yes (10+)

Web UI (self-hosted)

Dashboard only

No

No

Yes

Yes

Self-improving skills

Partial

No

No

No

Yes

Python / ML ecosystem

No (Node.js)

No

No

No

Yes

Provider-agnostic

Yes

No (Claude only)

Yes

Yes

Yes

Open source

Yes (MIT)

No

Yes

Yes

Yes

† Claude Code has CLAUDE.md / MEMORY.md project context and rolling auto-memory, but not full automatic cross-session recall‡ Claude Code has cloud-managed scheduling (Anthropic infrastructure) and session-scoped/loop; no self-hosted cron

The closest competitor is OpenClaw— both are always-on, self-hosted, open-source agents
with memory, cron, and messaging. The key differences: Hermes writes and saves its own skills
automatically as a core behavior (OpenClaw's skill system centers on a community marketplace);
Hermes is more stable across updates (OpenClaw has documented release regressions and ClawHub
has had security incidents involving malicious skills); and Hermes runs natively in the Python
ecosystem. Seedocs/why-hermes.mdfor the full side-by-side.

## Quick start

Run the repo bootstrap:

git clone https://github.com/nesquena/hermes-webui.git hermes-webui

cd
 hermes-webui
python3 bootstrap.py

Or keep using the shell launcher:

./start.sh

For self-hosted VM or homelab installs,ctl.shwraps the common daemon lifecycle commands without requiringfuserorpkill:

./ctl.sh start 
#
 background daemon, PID at ~/.hermes/webui.pid

./ctl.sh status 
#
 PID, uptime, bound host/port, log path, /health

./ctl.sh logs --lines 100 
#
 tail ~/.hermes/webui.log

./ctl.sh restart
./ctl.sh stop

ctl.sh startruns the bootstrap in foreground/no-browser mode behind the daemon wrapper, writes logs to~/.hermes/webui.log, and respects.envplus inline overrides such asHERMES_WEBUI_HOST=0.0.0.0 ./ctl.sh start.

### Optional session recall prefill

WebUI can attach ephemeral prefill messages to new browser-originated
agent turns. This is useful when a deployment already has a local recall or
router script for Joplin, Obsidian, Notion, llm-wiki, or another third-party
notes source and wants browser chat to know where durable context lives.

Prefer a compact router-style prefill (for example, "Joplin has the durable
project context; use the available notes/search tools before answering
detail-dependent questions") instead of dumping the full note corpus into every
new browser session. The prefill should point the agent toward retrieval; the
notes/search tools should provide the specific facts on demand.

Static JSON remains supported throughprefill_messages_fileorHERMES_PREFILL_MESSAGES_FILE. For dynamic recall, opt in explicitly with a
WebUI-specific script hook:

webui_prefill_messages_script
:
 - 
python3

 - 
/path/to/notes_recall.py

webui_prefill_messages_script_timeout
: 
5

or:

HERMES_WEBUI_PREFILL_MESSAGES_SCRIPT=
"
python3 /path/to/notes_recall.py
"
 \
HERMES_WEBUI_PREFILL_MESSAGES_SCRIPT_TIMEOUT=5 \
./ctl.sh restart

The script may print either an OpenAI-style JSON message list, a JSON object with
amessageslist, or plain text; plain text is wrapped as oneuserprefill
message so dynamic recall text becomes ordinary context instead of an extra
system instruction. If the hook must provide system-level guidance, emit JSON
messages with an explicitrole: "system"entry instead. Script output is capped
at 256 KiB before parsing. Parsed prefill context is then bounded bywebui_prefill_context_max_charsorHERMES_WEBUI_PREFILL_CONTEXT_MAX_CHARS(default: 12,000 characters; set to0to disable). When a dynamic script
exceeds the budget and a compact static prefill file is configured, WebUI falls
back to that file. If no compact fallback is available, WebUI injects a short
retrieval instruction instead of sending the oversized note/body payload with
every new browser turn. The browser only receives a compact status event
(source,label, message count, compaction metadata, and redacted errors),
never the prefill message bodies.

### Optional Gateway-backed browser chat

By default, browser chat runs through WebUI's in-process legacy runtime. Advanced
self-hosted deployments can opt into routing new browser turns through a running
Hermes Gateway API server while preserving the existing WebUI/api/chat/startand/api/chat/streambrowser contract:

HERMES_WEBUI_CHAT_BACKEND=gateway \
HERMES_WEBUI_GATEWAY_BASE_URL=http://127.0.0.1:8642 \
HERMES_WEBUI_GATEWAY_API_KEY=... \
./ctl.sh restart

HERMES_WEBUI_CHAT_BACKENDis intentionally strict: onlygateway,api_server, orapi-serverenable the bridge. Generic truthy values such as1ortrueare ignored so existing deployments do not change execution
ownership accidentally. IfHERMES_WEBUI_GATEWAY_API_KEYis omitted, WebUI falls
back toAPI_SERVER_KEYwhen present. When Gateway returns HTTP 401, WebUI
reports agateway_auth_errorthat points at this WebUI↔Gateway key mismatch
rather than showing the Gateway's generic provider-style "Invalid API key" body./api/health/agentalso includes a redactedgateway_chatblock so operators can
see whether gateway mode, base URL, and API-key presence are configured without
exposing the key value. Thatgateway_chatfield is an operator diagnostic
payload only; it is not currently rendered as a user-facing health banner in the
browser UI.

The bridge is best used by operators who already run Hermes Gateway/API Server
locally and want browser-originated chat to use the same runtime/tool path as
messaging surfaces. Attachments, cancellation, approvals, and clarify prompts
still follow WebUI's current compatibility path and may not match every messaging
surface until the runtime-adapter migration is complete.

The bootstrap will:

1. Detect Hermes Agent and, if missing, attempt the official installer (curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash).
2. Find or create a Python environment with the WebUI dependencies.
3. Start the web server and wait for/health.
4. Open the browser unless you pass--no-browser.
5. Drop you into a first-run onboarding wizard inside the WebUI.

Native Windows is not supported for this bootstrap yet. Use Linux, macOS, or WSL2.
For Windows / WSL auto-start at login, seedocs/wsl-autostart.md.

A community-maintained native Windows setup is documented at@markwang2658/hermes-windows-native-guide(companion setup repo:@markwang2658/hermes-windows-native). Notes from the community report in#1952:

* Memory:community-measured ~330 MB native vs ~1080 MB with WSL2+Docker (varies by configuration).
* What works:chat, workspace browser, session management, all themes.
* Known limitations:some POSIX-style file paths surface in the workspace browser; bash-assuming agent tools may not work natively.
* Native Windows setup:install Python 3.11+, then from the hermes-agent root in PowerShell:python -m venv venv→pip install -r requirements.txt→pwsh .\start.ps1(it auto-discoversvenv\Scripts\python.exe).
* WSL2 relationship:not a prerequisite — a WSL2-built venv (venv/bin/python, ELF) isn't invokable by native Windows Python, so use the native setup above. WSL2 stays useful as a parallel install if you want the fullbootstrap.py+ Linux runtime.

If provider setup is still incomplete after install, the onboarding wizard will point you to finish it withhermes modelinstead of trying to replicate the full CLI setup in-browser.
For a step-by-step walkthrough of the wizard, provider choices, local model server Base URLs, and safe re-runs, seedocs/onboarding.md.
If an AI assistant is helping with install, reinstall, bootstrap, provider setup, or first-run support, have it readdocs/onboarding-agent-checklist.mdbefore running commands or inspecting logs.

## Docker

Pre-built images(amd64 + arm64) are published to GHCR on every release.

For a comprehensive setup guide covering all 3 compose files, common failure modes, and bind-mount migration, seedocs/docker.md. The README covers the 5-minute happy path.

### 5-minute quickstart (single container)

The simplest setup: one WebUI container that runs the agent in-process.

git clone https://github.com/nesquena/hermes-webui

cd
 hermes-webui
cp .env.docker.example .env

#
 Edit .env if your host UID isn't 1000 (e.g. macOS where UIDs start at 501)

docker compose up -d

#
 Open http://localhost:8787

Run Compose as the user who owns your Hermes home.sudo docker compose up -dcan make${HOME}expand to the root user's home, so Docker mounts the wrong.hermesdirectory instead of your real~/.hermesand the WebUI starts withconfig.yaml (not found, using defaults). Prefer adding your user to the Docker group and runningdocker compose up -d; if you must use sudo, set absolute paths first, for exampleHERMES_HOME=/home/you/.hermes HERMES_WORKSPACE=/home/you/workspace sudo -E docker compose up -d, then verify withdocker compose config.

The container auto-detects your UID/GID from the mounted~/.hermesvolume so files written by the agent stay readable by you on the host.

To enable password protection (required if you expose the port outside127.0.0.1):

echo
 
"
HERMES_WEBUI_PASSWORD=change-me-to-something-strong
"
 
>>
 .env
docker compose up -d --force-recreate

### Manualdocker run(no compose)

docker pull ghcr.io/nesquena/hermes-webui:latest
docker run -d \
 -e WANTED_UID=
$(
id -u
)
 -e WANTED_GID=
$(
id -g
)
 \
 -v 
~
/.hermes:/home/hermeswebui/.hermes \
 -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui \
 -v 
~
/workspace:/workspace \
 -p 127.0.0.1:8787:8787 \
 ghcr.io/nesquena/hermes-webui:latest

### Build locally

docker build -t hermes-webui 
.

docker run -d \
 -e WANTED_UID=
$(
id -u
)
 -e WANTED_GID=
$(
id -g
)
 \
 -v 
~
/.hermes:/home/hermeswebui/.hermes \
 -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui \
 -v 
~
/workspace:/workspace \
 -p 127.0.0.1:8787:8787 \
 hermes-webui

### Multi-container setups

If you want the agent and WebUI in separate containers (for isolation, or because you're already running an agent gateway elsewhere):

#
 Agent + WebUI

docker compose -f docker-compose.two-container.yml up -d

#
 Agent + Dashboard + WebUI

docker compose -f docker-compose.three-container.yml up -d

Both compose files usenamed Docker volumesby default, which solves the UID/GID problem by construction. If you need bind mounts to share an existing host directory, seedocs/docker.mdfor the full migration recipe.

Known limitation (#681): in the two-container setup, tools triggered from the WebUI run in theWebUI container, not the agent container. If you need git/node/etc. on the WebUI's filesystem, either use the single-container setup, extend the WebUI Dockerfile, or use the communityall-in-one image.

Source boundary note (#2453): the multi-container setup mountshermes-agent-srcread-only into the WebUI by default. This prevents WebUI-side source rewrites but is still an implementation-coupling bridge, not a stable Agent API boundary. Seedocs/rfcs/agent-source-boundary.mdfor the current source/API decoupling inventory.

### Common failure modes

Symptom

Likely cause

Fix

PermissionError
 at startup

UID mismatch on bind mount

Set 
UID=$(id -u)
 in 
.env

.env: permission denied
 (#1389)

fix_credential_permissions()
 enforced 0600

Set 
HERMES_SKIP_CHMOD=1
 in 
.env

Workspace appears empty

UID mismatch on 
/workspace
 mount

Set 
UID=$(id -u)
 in 
.env

git: command not found
 in chat

Two-container architectural limit (#681)

Use single-container or extend Dockerfile

WebUI can't find agent source

hermes-agent-src
 volume misconfigured

Use the named volumes from compose files as-is

Podman shared 
.hermes
 fails

Podman 3.4 
keep-id
 limitation

Use Podman 4+ or single-container

Host API at 
localhost
 fails from WebUI

Container 
localhost
 means the container, not your host (#3012)

Use 
http://host.docker.internal:<port>
 on Docker Desktop, or 
http://host.containers.internal:<port>
 on Podman

WebUI can't see 
~/.hermes
 after 
sudo docker compose

${HOME}
 expanded to the root user's home (#3006)

Run Compose as your user, or pass absolute 
HERMES_HOME
/
HERMES_WORKSPACE
 with 
sudo -E

For the deep dive on each of these, seedocs/docker.md.

Note:By default, Docker Compose binds to127.0.0.1(localhost only).
To expose on a network, change the port to"8787:8787"indocker-compose.ymland setHERMES_WEBUI_PASSWORDto enable authentication.

## What start.sh discovers automatically

Thing

How it finds it

Hermes agent dir

HERMES_WEBUI_AGENT_DIR
 env, then 
$HERMES_HOME/hermes-agent
 (Windows default 
%LOCALAPPDATA%\hermes\hermes-agent
, POSIX default 
~/.hermes/hermes-agent
), then sibling 
../hermes-agent

Python executable

Agent venv first, then 
.venv
 in this repo, then system 
python3

State directory

HERMES_WEBUI_STATE_DIR
 env, then 
$HERMES_HOME/webui
 (Windows default 
%LOCALAPPDATA%\hermes\webui
, POSIX default 
~/.hermes/webui
)

Default workspace

HERMES_WEBUI_DEFAULT_WORKSPACE
 env, then 
~/workspace
, then state dir

Port

HERMES_WEBUI_PORT
 env or first argument, default 
8787

If discovery finds everything, nothing else is required.

## Overrides (only needed if auto-detection misses)

export
 HERMES_WEBUI_AGENT_DIR=/path/to/hermes-agent

export
 HERMES_WEBUI_PYTHON=/path/to/python

export
 HERMES_WEBUI_PORT=9000

export
 HERMES_WEBUI_AUTO_INSTALL=1 
#
 enable auto-install of agent deps (disabled by default)

./start.sh

Or inline:

HERMES_WEBUI_AGENT_DIR=/custom/path ./start.sh 9000

Full list of environment variables:

Variable

Default

Description

HERMES_WEBUI_AGENT_DIR

auto-discovered

Path to the hermes-agent checkout

HERMES_WEBUI_PYTHON

auto-discovered

Python executable

HERMES_WEBUI_HOST

127.0.0.1

Bind address (
0.0.0.0
 for all IPv4, 
::
 for all IPv6, 
::1
 for IPv6 loopback)

HERMES_WEBUI_PORT

8787

Port

HERMES_WEBUI_STATE_DIR

$HERMES_HOME/webui
 (Windows default 
%LOCALAPPDATA%\hermes\webui
, POSIX default 
~/.hermes/webui
)

Where sessions and state are stored

HERMES_WEBUI_DEFAULT_WORKSPACE

~/workspace

Default workspace

HERMES_WEBUI_DEFAULT_MODEL

(provider default)

Optional model override; leave unset to use the active Hermes provider default

HERMES_WEBUI_PASSWORD

(unset)

Set to enable password authentication

HERMES_WEBUI_CSP_CONNECT_EXTRA

(unset)

Optional space-separated 
http(s)://
 or 
ws(s)://
 origins to append to the report-only CSP 
connect-src
 directive for reverse-proxy or tunnel deployments

HERMES_WEBUI_EXTENSION_DIR

(unset)

Optional local directory served at 
/extensions/
; must point to an existing directory before extension injection is enabled

HERMES_WEBUI_EXTENSION_SCRIPT_URLS

(unset)

Optional comma-separated same-origin script URLs to inject; see 
WebUI Extensions

HERMES_WEBUI_EXTENSION_STYLESHEET_URLS

(unset)

Optional comma-separated same-origin stylesheet URLs to inject; see 
WebUI Extensions

HERMES_HOME

Windows: 
%LOCALAPPDATA%\hermes
; POSIX: 
~/.hermes

Base directory for Hermes state (affects all paths)

HERMES_CONFIG_PATH

$HERMES_HOME/config.yaml

Path to Hermes config file

## Accessing from a remote machine

The server binds to127.0.0.1by default (loopback only). If you are running
Hermes on a VPS or remote server, use an SSH tunnel from your local machine:

ssh -N -L 
<
local-port
>
:127.0.0.1:
<
remote-port
>
 
<
user
>
@
<
server-host
>

Example:

ssh -N -L 8787:127.0.0.1:8787 user@your.server.com

Then openhttp://localhost:8787in your local browser.

start.shwill print this command for you automatically when it detects you
are running over SSH.

## Accessing on your phone with Tailscale

Tailscaleis a zero-config mesh VPN built on
WireGuard. Install it on your server and your phone, and they join the same
private network -- no port forwarding, no SSH tunnels, no public exposure.

The Hermes Web UI is fully responsive with a mobile-optimized layout
(hamburger sidebar, sidebar top tabs in the drawer, touch-friendly controls),
so it works well as a daily-driver agent interface from your phone.

Setup:

1. InstallTailscaleon your server and
your iPhone/Android.
2. Start the WebUI listening on all interfaces with password auth enabled:

HERMES_WEBUI_HOST=0.0.0.0 HERMES_WEBUI_PASSWORD=your-secret ./start.sh

1. Openhttp://<server-tailscale-ip>:8787in your phone's browser
(find your server's Tailscale IP in the Tailscale app or withtailscale ip -4on the server).

That's it. Traffic is encrypted end-to-end by WireGuard, and password auth
protects the UI at the application level. You can add it to your home screen
for an app-like experience.

### Community field report: ARM64 Android via AVF

A community report in#2364documents Hermes Agent + WebUI running on a mid-range ARM64 Android phone inside
a Debian 12 VM via Android Virtualization Framework (AVF). The reported setup
used a Xiaomi Redmi Note 13 Pro 4G, 3.8 GiB RAM allocated to the VM, 8 visible
CPU cores, Chrome on Android atlocalhost:8787, and cloud-hosted inference.

This is not an official support baseline or provider/model benchmark, but it is
a useful compatibility signal for mobile ARM64 experiments: the WebUI rendered
smoothly in Chrome, ARM64 Debian worked for the agent stack, and the total local
footprint was about 1.7 GB. Practical caveats from the report: first install can
take longer when dependencies compile from source, Android browser tabs may
reload when switching apps, and disabling battery optimization for the terminal
or VM host may be needed for longer-running sessions.

Tip:If using Docker, setHERMES_WEBUI_HOST=0.0.0.0in yourdocker-compose.ymlenvironment (already the default) and setHERMES_WEBUI_PASSWORD.

## Manual launch (without start.sh)

If you prefer to launch the server directly:

cd
 /path/to/hermes-agent 
#
 or wherever sys.path can find Hermes modules

HERMES_WEBUI_PORT=8787 venv/bin/python /path/to/hermes-webui/server.py

Note: use the agent venv Python (or any Python environment that has the Hermes agent dependencies installed). System Python will be missingopenai,httpx, and other required packages.

Health check:

curl http://127.0.0.1:8787/health

## Running tests

Tests discover the repo and the Hermes agent dynamically -- no hardcoded paths.

cd
 hermes-webui
pytest tests/ -v --timeout=60

Or using the agent venv explicitly:

/path/to/hermes-agent/venv/bin/python -m pytest tests/ -v

Tests run against an isolated server with a separate state directory.
Production data and real cron jobs are never touched. Current snapshot:5303 tests collectedacross488 test files.

## Features

### Chat and agent

* Streaming responses via SSE (tokens appear as they are generated)
* Multi-provider model support -- any Hermes API provider (OpenAI, Anthropic, Google, DeepSeek, Nous Portal, OpenRouter, MiniMax, Xiaomi MiMo, Z.AI); dynamic model dropdown populated from configured keys
* Send a message while one is processing -- it queues automatically
* Edit any past user message inline and regenerate from that point
* Retry the last assistant response with one click
* Cancel a running task directly from the composer footer (Stop button next to Send)
* Tool call cards inline -- each shows the tool name, args, and result snippet; expand/collapse all toggle for multi-tool turns
* Subagent delegation cards -- child agent activity shown with distinct icon and indented border
* Mermaid diagram rendering inline (flowcharts, sequence diagrams, gantt charts)
* Thinking/reasoning display -- collapsible gold-themed cards for Claude extended thinking and o3 reasoning blocks
* Approval card for dangerous shell commands (allow once / session / always / deny)
* SSE auto-reconnect on network blips (SSH tunnel resilience)
* File attachments persist across page reloads and are stored outside the active workspace by default (~/.hermes/webui/attachments/<session_id>/, orHERMES_WEBUI_ATTACHMENT_DIR/<session_id>/when configured)
* Message timestamps (HH:MM next to each message, full date on hover)
* Code block copy button with "Copied!" feedback
* Syntax highlighting via Prism.js (Python, JS, bash, JSON, SQL, and more)
* Safe HTML rendering in AI responses (bold, italic, code converted to markdown)
* rAF-throttled token streaming for smoother rendering during long responses
* Context usage indicator in composer footer -- token count, cost, and fill bar (model-aware)

### Sessions

* Create, rename, duplicate, delete, search by title and message content
* Session actions via⋯dropdown per session — pin, move to project, archive, duplicate, delete
* Pin/star sessions to the top of the sidebar (gold indicator)
* Archive sessions (hide without deleting, toggle to show)
* Session projects -- named groups with colors for organizing sessions
* Session tags -- add #tag to titles for colored chips and click-to-filter
* Grouped by Today / Yesterday / Earlier in the sidebar (collapsible date groups)
* Download as Markdown transcript, full JSON export, or import from JSON
* Sessions persist across page reloads and SSH tunnel reconnects
* Browser tab title reflects the active session name
* CLI session bridge -- CLI sessions from hermes-agent's SQLite store appear in the sidebar with a gold "cli" badge; click to import with full history and reply normally
* Token/cost display -- input tokens, output tokens, estimated cost shown per conversation (toggle in Settings or/usagecommand)

### Workspace file browser

* Directory tree with expand/collapse (single-click toggles, double-click navigates)
* Breadcrumb navigation with clickable path segments
* Preview text, code, Markdown (rendered), and images inline
* Chat links usingworkspace://path/to/fileopen files in the right-side preview pane
* Edit, create, delete, and rename files; create folders
* Binary file download (auto-detected from server)
* File preview auto-closes on directory navigation (with unsaved-edit guard)
* Git detection -- branch name and dirty file count badge in workspace header
* Right panel is drag-resizable
* Syntax highlighted code preview (Prism.js)

### Voice input

* Microphone button in the composer (Web Speech API)
* Tap to record, tap again or send to stop
* Live interim transcription appears in the textarea
* Auto-stops after ~2s of silence
* Appends to existing textarea content (doesn't replace)
* Hidden when browser doesn't support Web Speech API (Chrome, Edge, Safari)

### Profiles

* Profile chip in thecomposer footer-- dropdown showing all profiles with gateway status and model info
* Gateway status dots (green = running), model info, skill count per profile
* Profiles management panel -- create, switch, and delete profiles from the sidebar
* Clone config from active profile on create
* Optional custom endpoint fields on create -- Base URL and API key written into the profile'sconfig.yamlat creation time, so Ollama, LMStudio, and other local endpoints can be configured without editing files manually
* Seamless switching -- no server restart; reloads config, skills, memory, cron, models
* Per-session profile tracking (records which profile was active at creation)

### Authentication and security

* Optional password auth -- off by default, zero friction for localhost
* Enable viaHERMES_WEBUI_PASSWORDenv var or Settings panel
* Optional passkeys/WebAuthn -- register from Settings -> System after signing in with a password; the login page only shows passkey sign-in after at least one passkey exists
* After registering at least one passkey, Settings -> System can remove the password and keep passkey-only sign-in enabled. Password auth remains the bootstrap/recovery path until you choose to go passwordless; passkeys are same-origin and stored locally in the WebUI state directory
* Signed HMAC HTTP-only cookie with 24h TTL
* Minimal dark-themed login page at/login
* Security headers on all responses (X-Content-Type-Options, X-Frame-Options, Referrer-Policy)
* 20MB POST body size limit
* CDN resources pinned with SRI integrity hashes

### Themes

* Appearance is split into two axes: Theme (system,dark,light) and Skin
(default,ares,mono,slate,poseidon,sisyphus,charizard,sienna,catppuccin,nous,geist-contrast/ Geist Contrast)
* Switch via Settings -> Appearance (instant live preview) or/theme <theme-or-skin>
* Persists across reloads (server-side in settings.json + localStorage for flicker-free loading)
* Skins usedata-skinplus CSS variables; dark mode resolves through the.darkclass, not adata-themecustom-theme axis — seeTHEMES.md

### Settings and configuration

* Hermes Control Center(sidebar launcher button) -- Conversation tab (export/import/clear), Preferences tab (model, send key, theme, language, all toggles), System tab (version, password)
* Send key: Enter (default) or Ctrl/Cmd+Enter
* Show/hide CLI sessions toggle (enabled by default)
* Token usage display toggle (off by default, also via/usagecommand)
* Control Center always opens on the Conversation tab; resets on close
* Unsaved changes guard -- discard/save prompt when closing with unpersisted changes
* Cron completion alerts -- toast notifications and unread badge on Tasks tab
* Background agent error alerts -- banner when a non-active session encounters an error

### Slash commands

* Type/in the composer for autocomplete dropdown
* Built-in:/help,/clear,/compress [focus topic],/compact(alias),/model <name>,/workspace <name>,/new,/usage,/theme
* Arrow keys navigate, Tab/Enter select, Escape closes
* Unrecognized commands pass through to the agent

### Panels

* Chat-- session list, search, pin, archive, projects, new conversation
* Tasks-- view, create, edit, run, pause/resume, delete cron jobs; run history; completion alerts
* Skills-- list all skills by category, search, preview, create/edit/delete; linked files viewer
* Memory-- view and edit MEMORY.md and USER.md inline
* Profiles-- create, switch, delete agent profiles; clone config
* Todos-- live task list from the current session
* Spaces-- add, rename, remove workspaces; quick-switch from topbar

### Mobile responsive

* Hamburger sidebar -- slide-in overlay on mobile (<640px)
* Sidebar top tabs stay available on mobile; no fixed bottom nav stealing chat height
* Files slide-over panel from right edge
* Touch targets minimum 44px on all interactive elements
* Full-height chat/composer on phones without bottom-nav spacing
* Desktop layout completely unchanged

## Architecture

server.py HTTP routing shell + auth middleware (~446 lines)
api/
 auth.py Optional password authentication, signed cookies (~366 lines)
 config.py Discovery, globals, model detection, reloadable config (~4139 lines)
 helpers.py HTTP helpers, security headers (~302 lines)
 models.py Session model + CRUD + CLI bridge (~1927 lines)
 onboarding.py First-run onboarding wizard, OAuth provider support (~1002 lines)
 profiles.py Profile state management, hermes_cli wrapper (~1056 lines)
 routes.py All GET + POST route handlers (~9772 lines)
 state_sync.py /insights sync — message_count to state.db (~118 lines)
 streaming.py SSE engine, run_agent, cancel support (~4420 lines)
 updates.py Self-update check and release notes (~545 lines)
 upload.py Multipart parser, file upload handler (~284 lines)
 workspace.py File ops, workspace helpers, git detection (~810 lines)
static/
 index.html HTML template (~1323 lines)
 style.css All CSS incl. mobile responsive, themes (~3767 lines)
 ui.js DOM helpers, renderMd, tool cards, context indicator (~7216 lines)
 workspace.js File preview, file ops, git badge (~369 lines)
 sessions.js Session CRUD, collapsible groups, search, reload recovery (~3517 lines)
 messages.js send(), SSE handlers, live streaming, session recovery (~2301 lines)
 panels.js Cron, skills, memory, profiles, settings (~6480 lines)
 commands.js Slash command autocomplete (~1302 lines)
 boot.js Mobile nav, voice input, boot IIFE (~1607 lines)
tests/
 conftest.py Isolated test server/state fixtures
 488 test files 5303 tests collected
Dockerfile python:3.12-slim container image
docker-compose.yml Compose with named volume and optional auth
.github/workflows/ CI: multi-arch Docker build + GitHub Release on tag

State lives outside the repo at~/.hermes/webui/by default
(sessions, workspaces, settings, projects, last_workspace). Override withHERMES_WEBUI_STATE_DIR.

## Docs

* docs/why-hermes.md-- why Hermes, mental model, and detailed comparison to Claude Code / Codex / OpenCode / Cursor
* ROADMAP.md-- feature roadmap and sprint history
* ARCHITECTURE.md-- system design, all API endpoints, implementation notes
* TESTING.md-- manual browser test plan and automated coverage reference
* CHANGELOG.md-- release notes per sprint
* SPRINTS.md-- forward sprint plan with CLI + Claude parity targets
* THEMES.md-- theme system documentation, custom theme guide
* docs/CONTRACTS.md-- project contract/RFC/design index for contributors and agents
* docs/UIUX-GUIDE.md-- UI/UX principles sourced from existing design docs and visual inventories
* docs/docker.md-- Docker compose setup, common failures, and bind-mount migration
* docs/supervisor.md-- launchd, systemd, supervisord, runit, and s6 process-supervisor setup
* docs/onboarding.md-- first-run wizard, provider setup, local model server Base URLs, and safe re-runs
* docs/onboarding-agent-checklist.md-- safety rules, evidence commands, and pass/fail checks for assistant-led install or reinstall support
* docs/troubleshooting.md-- diagnostic flows for common failures (e.g. "AIAgent not available")
* docs/wsl-autostart.md-- WSL2 auto-start at Windows login
* docs/EXTENSIONS.md-- administrator-controlled WebUI extension injection
* docs/rfcs/README.md-- RFC index for larger architecture and durability proposals

## Contributors

Hermes WebUI is built with help from the open-source community. Every PR — whether merged directly, absorbed into a batch release, or salvaged from a larger proposal — shapes the project, and we're grateful to everyone who has taken the time to contribute.

137 contributors have shipped code that landed in a release tagas of v0.51.58. The full credit roll lives inCONTRIBUTORS.md. The highlights:

### Top contributors (by PR count, including absorbed/batch-released work)

#

Contributor

PRs

First → latest release

1

@franksong2702

117

v0.49.3
 → 
v0.51.58

2

@Michaelyklam

92

v0.50.240
 → 
v0.51.57

3

@bergeouss

62

v0.48.0
 → 
v0.51.46

4

@ai-ag2026

55

v0.50.279
 → 
v0.51.47

5

@dso2ng

23

v0.50.227
 → 
v0.51.51

6

@jasonjcwu

16

v0.50.227
 → 
v0.51.55

7

@Jordan-SkyLF

12

v0.50.18
 → 
v0.51.58

8

@aronprins

10

v0.44.0
 → 
v0.50.233

9

@JKJameson

10

v0.50.233
 → 
v0.51.31

10

@starship-s

10

v0.50.128
 → 
v0.51.58

SeeCONTRIBUTORS.mdfor the full ranked list of all 137 contributors, including everyone with one or two PRs and the special-thanks roll for design and architectural contributions.

### Notable contributions

@franksong2702— Most prolific external contributor (117 PRs,v0.49.3→v0.51.58)
Across the longest tenure of any external contributor: the session title guard (#301), breadcrumb workspace navigation (#302), embedded workspace terminal (#1099), worktree-backed session creation (#2053), onboarding documentation (#2052), composer footer container queries, streaming-session sidebar exemption (#1327), session sidecar repair, cron output preservation (#1295), profile default workspace persistence, manual/compressasync start/status endpoints (#2128), worktree status surface (#2109) + guarded remove (#2156) for the lifecycle umbrella #2057, session post-render dedup (#2166), native-WebUI fast path (#2170), tail-window response trim (#2171), stale-stream guard extension (#2158), CSP report collector (#2160), and a long tail of polish across mobile/responsive, the session sidebar, and the workspace state machine.

@Michaelyklam— Most prolific contributor of recent releases (92 PRs,v0.50.240→v0.51.57)
Production Docker hardening (#1921, drops sudo-capable staging user), profile-scoped skills endpoints (#1903), gateway PID resolution under profile-scoped HERMES_HOME (#1901), profile-aware AIAgent cache (#1898/#1904), backslash LaTeX delimiters (#1848), Codex quota error surfacing (#1770), shell-route HTML 503 (#1836), stale Kanban client recovery (#1828), context auto-compression toast lifetime (#1988),/goalcommand (#1866), Kanban detail-view scrolling (#1916), CLI session tool metadata preservation (#1778), Traditional Chinese kanban locale backfill (#1979), v0.51.51 mobile Insights bucketing/layout (#2120/#2121), Hermes run adapter RFC (#2105 for #1925), fork-from-here absolute index (#2198 for #2184), opencode-go custom-provider overlap routing (#2204 for #1894).

@bergeouss— Provider management UI + Docker hardening (62 PRs,v0.48.0→v0.51.46)
Provider management UI for adding/editing custom providers from Settings, OAuth provider status detection (#1552), two-container Docker setup, profile isolation hardening (per-profile.envsecrets), the bulk of what users see when they touch Settings → Providers, Reveal-in-Finder context menu (#1551), gateway status card (#1552), auto-assign session to active project filter (#1550), "What's new?" link in update banner (#1549), OpenRouter free-tier live fetch (#1548), credential pool 401 self-heal (#1553), inline provider chip + group model count in model picker (#1644).

@ai-ag2026— Session recovery + audit infrastructure (55 PRs,v0.50.279→v0.51.47)
Autonomous-AI contributor (Hermes Agent-driven) focused on durability:state.db-backed sidecar reconciliation (#2041), orphan.json.bakrecovery on startup (#2035), read-only session recovery audit endpoints (#2036, #2040), active run lifecycle in/health(#2039), crash-safe turn-journal RFC atdocs/rfcs/turn-journal.md(#2042), append-only turn-journal helper (#2059), lifecycle events layer (#2062),Content-Security-Policy-Report-Onlyheader (#2084), per-cron toast toggle (#2100), fork-session compression lineage isolation (#2014).

@dso2ng— Session lineage + diagnostics (23 PRs,v0.50.227→v0.51.51)/api/session/lineage-report/<sid>endpoint for bounded session graph diagnostics (#2012), stale Mermaid render error cleanup (#1337),session_source="fork"continuation-chain isolation (#2063), lazy lineage-report fetch on sidebar badge expand (#2130), and a long tail of frontend reliability fixes around session loading.

@jasonjcwu— Composer + transcript polish (16 PRs,v0.50.227→v0.51.55)
Sidebar collapse via active-rail click (#2054, fuses #1884 + #1924), composer chip lightbox (#1758), title fixes for tool-heavy first turns, silent compress-status during session switch (#2185), concurrent-send loss fix (#2186), in-transcript steer message badges (#2187), and a string of frontend polish fixes.

@Jordan-SkyLF— Live streaming + UX polish (12 PRs,v0.50.18→v0.51.58)
Original sprint of workspace fallback resolution, live reasoning cards (#366, #367, #394–#397), then a recent burst: manual "Refresh usage" button on the Provider quota card (#2150), cancelled-turn status classification (#2151), Firefox sidebar scroll stabilization (#2200), early provisional session titles (#2202), target-aware "What's new?" update-banner links (#2207), and MCP tools overflow fix in Settings (#2210).

@aronprins—v0.50.0UI overhaul (PR #242, plus 9 follow-ups)
The biggest single contribution to the project: a complete UI redesign that moved model/profile/workspace controls into the composer footer, replaced the gear-icon settings panel with the Hermes Control Center (tabbed modal), removed the activity bar in favor of inline composer status, redesigned the session list with a⋯action dropdown, and added the workspace panel state machine. Plus chat transcript redesign (#587), sidebar declutter (#584), three-column layout refactor (#899), light/dark theme + accent skins (#627), and sharedconfirm()/prompt()dialog replacement (PR #251 extracted from #242).

@iRonin— Security hardening sprint (PRs #196–#204)
Six consecutive, focused security PRs: session memory leak fix (expired token pruning), CSP + Permissions-Policy headers, 30-second slow-client connection timeout, optional HTTPS/TLS support via environment variables, upstream branch tracking fix for self-update, and CLI session support in the file-browser API. The kind of focused, high-quality security work that makes a self-hosted tool trustworthy.

@lucasrc— Auth-hardening trilogy (PRs #2191, #2192, #2193)
Three coordinated security PRs that all landed in v0.51.57: thread-safe login rate limiter with PBKDF2 key separation, password-hash cache invalidation on Settings save, and the full 64-char HMAC-SHA256 session signature with a backwards-compatible migration bridge. The kind of cleanly-decomposed security work that's reviewable as three independent pieces.

@LumenYoung— Streaming hot-path correctness (4 PRs,v0.51.47→v0.51.55)
The original stale-stream writeback guard (#2136 — the bug class the next two releases extended), gateway-state alive-null classification (#2075), compression-banner anchor alignment (#2182), and context-progress ring auto-refresh on compression complete (#2188). Each PR opened a small surgical fix in one of the most fragile subsystems in the codebase.

@dobby-d-elf— Frontend reliability + motion polish (6 PRs,v0.51.38→v0.51.58)
Workspace fallback on deleted directories (#2138), iPhone PWA bottom-scroll fix (#2143), the new "Activity: X tools" composer footer shimmer animation (#2203), and follow-up animation tuning (#2212).

@JKJameson— Composer + session polish (10 PRs)
Persistent composer draft per session (#1956), and a long tail of polish across the composer and session sidebar.

@gabogabucho— Spanish locale + onboarding wizard
Full Spanish (es) locale covering all UI strings, plus the one-shot bootstrap onboarding wizard that guides new users through provider setup on first launch.

@deboste— Reverse-proxy auth + mobile responsive layout (PRs #3, #4, #5)
Three of the very first community PRs: fixed EventSource/fetch to use URL origin for reverse-proxy setups, corrected model provider routing from config, and added mobile responsive layout with dvh viewport fix. Early foundation work.

@indigokarasu— Visual redesign proposal (PR #213)
A CSS-only redesign of the full UI — proper design tokens, an icon rail sidebar replacing the emoji tab strip, consistent form cards, breadcrumb nav, and 7 built-in themes as custom properties. The PR didn't merge as-is but shaped the design language and theme architecture that shipped in v0.50.0.

@zenc-cp— Anti-hallucination guard for the ReAct loop (PR #133)
A three-layer approach (ephemeral anti-hallucination prompt, live token filtering, session-history cleanup) that the streaming pipeline still uses.

@Hinotoi-agent— Profile + session security (PRs #351, #2048)
Profile.envsecret isolation fix (PR #351) preventing API key leakage between profiles, and session-import workspace validation (PR #2048) blocking a crafted-JSON file-read against/.

@Sanjays2402— Endless-scroll + Start-jump race fix (PR #1949)
A generation-token + mutex pair fixing the v0.51.30 race between endless-scroll prefetch and Start-jump's_ensureAllMessagesLoaded. The naive same-flag-check approach (proposed in #1942 and #1962) was a no-op for the post-await race — Sanjays2402's fix was the correct shape.

@fxd-jason— Real-time approval + clarify via SSE (PRs #1350, #1355)
Replaced 1.5s HTTP polling with SSE long-connections for both approval and clarify, cutting latency from up to 1.5s to near-instant. Got all the correctness details right (atomic subscribe + snapshot, notify-inside-lock, head-of-queue payload, trailing event re-emission).

@happy5318— Custom provider model dedup (PR #1947)
Fixed the same model from different named custom providers being silently deduplicated in the picker, with Opus catching a race in the original tests that needed augmentation.

@NocGeek— Streaming scroll + manual cron output persistence (7 PRs)
Streaming scroll viewport stability when tool/queue cards insert (#1360), manual cron-run output and metadata persistence (#1372, split from held #1352).

@DavidSchuchert— German translation (PR #190)
Complete German locale (de) covering all UI strings, settings labels, commands, and system messages — and stress-tested the i18n system, exposing several elements that weren't yet translatable and getting them fixed as part of the same PR.

@Bobby9228— Mobile Profiles button (PR #265)
Added the Profiles entry to the mobile navigation flow, making profile switching reachable on phones.

@kevin-ho— OLED theme (PR #168)
The 7th built-in theme: pure black backgrounds with warm accents tuned to reduce burn-in risk.

@andrewy-wizard— Chinese localization (PR #177)
Initial Simplified Chinese (zh) locale. One of the first non-English locales.

@DelightRun—session_searchfix for WebUI sessions (PR #356)
Tracked down the missingSessionDBinjection in the streaming path that was silently breaking the tool for every WebUI session.

@lawrencel1ng— Bandit security fixes (PR #354)
Systematic bandit-scan fixes: URL scheme validation beforeurlopen, MD5usedforsecurity=False, and 40+ bareexcept: passblocks replaced with proper logging.

@shaoxianbilly— Unicode filename downloads (PR #378)
ProperContent-Dispositionwith RFC 5987filename*=UTF-8''...encoding so non-ASCII filenames download without crashing.

@lx3133584— CSRF fix for reverse proxy (PR #360)
A real-world blocker for anyone hosting behind Nginx Proxy Manager or similar on a port other than 80/443.

@betamod— Security audit (PR #171)
A comprehensive CSRF / SSRF / XSS / env-race-condition audit that shipped in v0.39.0.

@TaraTheStar— Bot name + thinking blocks + login refactor (PRs #132, #176, #181)
Configurable assistant display name, thinking/reasoning block display, and a login page refactor.

## Repo

git@github.com:nesquena/hermes-webui.git

## About

Hermes WebUI: The best way to use Hermes Agent from the web or from your phone!

get-hermes.ai/

### Topics

 agent

 hermes

 ai-agents

 hermes-agent

 nous-research

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

9.8k

 stars
 

### Watchers

33

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases511

v0.51.188

 Latest

 

May 31, 2026

 

+ 510 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python72.9%
* JavaScript22.0%
* CSS3.1%
* HTML1.5%
* Shell0.4%
* PowerShell0.1%