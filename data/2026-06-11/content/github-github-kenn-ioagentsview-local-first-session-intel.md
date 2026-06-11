---
title: 'GitHub - kenn-io/agentsview: Local-first session intelligence and analytics for coding agents, supporting Claude Code, Codex, and more than 20 other agents. Also: 100x faster replacement for ccusage! · GitHub'
url: https://github.com/kenn-io/agentsview
site_name: github
content_file: github-github-kenn-ioagentsview-local-first-session-intel
fetched_at: '2026-06-11T19:53:03.072331'
original_url: https://github.com/kenn-io/agentsview
author: kenn-io
description: 'Local-first session intelligence and analytics for coding agents, supporting Claude Code, Codex, and more than 20 other agents. Also: 100x faster replacement for ccusage! - kenn-io/agentsview'
---

kenn-io

 

/

agentsview

Public

* NotificationsYou must be signed in to change notification settings
* Fork172
* Star1.6k

 
 
 
 
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

520 Commits
520 Commits
.github/
workflows
.github/
workflows
 
 
cmd
cmd
 
 
desktop
desktop
 
 
docs
docs
 
 
frontend
frontend
 
 
internal
internal
 
 
scripts
scripts
 
 
support/
launchd
support/
launchd
 
 
testdata/
ssh
testdata/
ssh
 
 
.air.toml
.air.toml
 
 
.custom-gcl.yml
.custom-gcl.yml
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.nilaway.yml
.golangci.nilaway.yml
 
 
.golangci.yml
.golangci.yml
 
 
.kata.toml
.kata.toml
 
 
.roborev.toml
.roborev.toml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.prod.yaml
docker-compose.prod.yaml
 
 
docker-compose.test.yml
docker-compose.test.yml
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
prek.toml
prek.toml
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

# agentsview

Browse, search, and track costs across all your AI coding agents. One binary, no
accounts, everything local.

## Install

#
 macOS / Linux

curl -fsSL https://agentsview.io/install.sh 
|
 bash

#
 Windows

powershell -ExecutionPolicy ByPass -c 
"
irm https://agentsview.io/install.ps1 | iex
"

Or download thedesktop app(macOS / Windows) fromGitHub Releasesor via
homebrew:brew install --cask agentsview

Or run the published Docker image:

docker run --rm -p 127.0.0.1:8080:8080 \
 -v agentsview-data:/data \
 -v 
"
$HOME
/.claude/projects:/agents/claude:ro
"
 \
 -v 
"
$HOME
/.forge:/agents/forge:ro
"
 \
 -e CLAUDE_PROJECTS_DIR=/agents/claude \
 -e FORGE_DIR=/agents/forge \
 ghcr.io/kenn-io/agentsview:latest

## Quick Start

agentsview serve 
#
 start server, open web UI

agentsview usage daily 
#
 print daily cost summary

On first run, agentsview discovers sessions from every supported agent on your
machine, syncs them into a local SQLite database, and opens a web UI athttp://127.0.0.1:8080.

## Remote / forwarded access

agentsview binds to loopback and validates the requestHostheader to guard
against DNS-rebinding attacks. When you reach it through SSH port-forwarding, a
reverse proxy, or a remote dev environment (exe.dev, Codespaces, Coder, WSL2),
the browser sends aHostthat the server does not recognize, so API requests
such as/api/v1/settingsare rejected with403 Forbidden.

To fix this, restart the server with--public-urlset to the exact origin you
open in the browser:

#
 Browser opens http://127.0.0.1:18080 via `ssh -L 18080:127.0.0.1:8080 host`

agentsview serve --public-url http://127.0.0.1:18080

#
 Browser opens a forwarded hostname

agentsview serve --public-url https://your-workspace.exe.dev

Use--public-origin(repeatable or comma-separated) to trust additional
browser origins. If you expose the UI beyond loopback, also enable--require-auth.

## Docker

The container image defaults to localagentsview serve. SetPG_SERVE=1to
switch the startup command toagentsview pg serveinstead.

docker-compose.prod.yamlis included as a production example:

docker compose -f docker-compose.prod.yaml up -d

The included compose file persists the agentsview data directory in a named
volume and mounts Claude, Codex, Forge, and OpenCode session roots read-only.
The container runs as root, so prefer a named volume for/dataover a host
bind mount; if you do bind-mount, pre-create the directory with the desired
ownership to avoid root-owned files in your home directory.

The examples publish the UI on loopback only (127.0.0.1). If you need to
expose it beyond localhost, enable--require-authand publish the port
intentionally.

Important: a containerized agentsview instance can only discover agent sessions
from directories you explicitly mount into the container. If you do not mount an
agent's session directory and point the matching env var at it, that agent will
not appear in the UI.

Example PostgreSQL-backed startup:

docker run --rm -p 127.0.0.1:8080:8080 \
 -e PG_SERVE=1 \
 -e AGENTSVIEW_PG_URL=
'
postgres://user:password@postgres.example.com:5432/agentsview?sslmode=require
'
 \
 ghcr.io/kenn-io/agentsview:latest

Example DuckDB mirror startup:

#
 Populate /data/sessions.duckdb from the mounted SQLite archive.

docker run --rm \
 -v agentsview-data:/data \
 -v 
"
$HOME
/.claude/projects:/agents/claude:ro
"
 \
 -e CLAUDE_PROJECTS_DIR=/agents/claude \
 ghcr.io/kenn-io/agentsview:latest duckdb push --full

#
 Serve the populated mirror read-only.

docker run --rm -p 127.0.0.1:8080:8080 \
 -v agentsview-data:/data \
 ghcr.io/kenn-io/agentsview:latest duckdb serve

Example Quack startup:

#
 Expose the local DuckDB mirror over Quack from the host/container.

QUACK_TOKEN=
"
$(
openssl rand -base64 32
)
"

docker run --rm -p 127.0.0.1:9494:9494 \
 -v agentsview-data:/data \
 ghcr.io/kenn-io/agentsview:latest \
 duckdb quack serve \
 --bind quack:0.0.0.0:9494 \
 --token 
"
$QUACK_TOKEN
"
 \
 --allow-insecure

#
 Serve the web UI from a remote Quack endpoint.

docker run --rm -p 127.0.0.1:8080:8080 \
 -e AGENTSVIEW_DUCKDB_URL=
'
quack:https://duckdb.example.com
'
 \
 -e AGENTSVIEW_DUCKDB_TOKEN=
"
$QUACK_TOKEN
"
 \
 ghcr.io/kenn-io/agentsview:latest duckdb serve

Keep Quack on loopback or behind TLS. Plain HTTP Quack on a non-loopback bind
requires--allow-insecureand should only be used behind a trusted tunnel or
reverse proxy.

## Token Usage and Cost Tracking

agentsview usageis a fast, local replacement for ccusage and similar tools.
It tracks token consumption and compute costs acrossallyour coding agents
-- not just Claude Code. Because session data is already indexed in SQLite,
queries are over 100x faster than tools that re-parse raw session files on every
run.

#
 Daily cost summary (default: last 30 days)

agentsview usage daily

#
 Per-model breakdown

agentsview usage daily --breakdown

#
 Filter by agent and date range

agentsview usage daily --agent claude --since 2026-04-01

#
 One-line summary for shell prompts / status bars

agentsview usage daily --all --json
agentsview usage statusline

Features:

* Automatic pricing via LiteLLM rates (with offline fallback)
* Prompt-caching-aware cost calculation (cache creation / read tokens)
* Per-model breakdown with--breakdown
* Date filtering (--since,--until,--all), agent filtering (--agent)
* JSON output (--json) for scripting
* Timezone-aware date bucketing (--timezone)
* Works standalone -- no server required, just run the command

## Per-Session Details

agentsview session usage <id>prints per-session token statistics plus a cost
estimate for a single session. The output reports the session's total output
tokens and peak context tokens, plus a cost estimate in USD (cost_usd) when
pricing is available for the session's model(s) (has_cost). Cost is computed
from input/output and cache tokens internally, but only the output-token and
peak-context totals are reported alongside the cost.

#
 Print token usage and cost for a specific session

agentsview session usage 
<
id
>

#
 JSON output for scripting

agentsview session usage 
<
id
>
 --format json

The same per-session usage data is available from the REST API:

GET /api/v1/sessions/{id}/usage

The response includes thesession_id,agent,project,total_output_tokens,peak_context_tokens,has_token_data,cost_usd,has_cost,models, andunpriced_modelsfields from the CLI JSON schema.
HTTP responses also includeserver_running: true. Existing sessions return200even when token or cost data is absent; missing sessions return404.

The deprecated aliasagentsview token-use <id>remains available for
compatibility and now also reports cost estimates.

## Session Stats

agentsview statsemits window-scoped analytics over recorded sessions: totals,
archetypes (automation vs. quick/standard/deep/marathon), distributions for
session duration, user-message count, peak context, and tools-per-turn, plus
cache economics, tool/model/agent mix, and a temporal hourly breakdown. The--format jsonoutput follows a versioned v1 schema (schema_version: 1)
suitable for downstream consumers.

By default,statsonly reads the local SQLite archive. Git-derived outcome
metrics are opt-in because they can be slow or brittle on large/missing repos:
use--include-git-outcomesfor commits/LOC/files changed, and--include-github-outcomesfor GitHub PR counts viagh(this also enables git
outcomes).

#
 Human-readable summary over the last 28 days

agentsview stats

#
 Machine-readable JSON over a fixed date range

agentsview stats --format json --since 2026-04-01 --until 2026-04-15

#
 Restrict to one agent and inspect the schema

agentsview stats --format json --agent claude 
|
 jq 
'
.schema_version
'

#
 Include expensive local git outcome metrics explicitly

agentsview stats --include-git-outcomes

## Session Browser

Dashboard

Session viewer

Search

Activity heatmap

* Full-text searchacross all message content (FTS5)
* Token usage and cost dashboard-- per-session and per-model cost
breakdowns, daily spend charts, all in the web UI
* Analytics dashboard-- activity heatmaps, tool usage, velocity metrics,
project breakdowns
* Live updatesvia SSE as active sessions receive new messages
* Keyboard-firstnavigation (j/k/[/],Cmd+Ksearch,?for all
shortcuts)
* Exportsessions as HTML or publish to GitHub Gist

## Supported Agents

agentsview auto-discovers sessions from all of these:

Agent

Session Directory

Claude Code

~/.claude/projects/

Codex

~/.codex/sessions/

Copilot CLI

~/.copilot/

Gemini CLI

~/.gemini/

OpenCode

~/.local/share/opencode/

OpenHands CLI

~/.openhands/conversations/

Cursor

~/.cursor/projects/

Amp

~/.local/share/amp/threads/

iFlow

~/.iflow/projects/

Zencoder

~/.zencoder/sessions/

Zed

~/Library/Application Support/Zed/
 (macOS)

VSCode Copilot

~/Library/Application Support/Code/User/
 (macOS)

Pi

~/.pi/agent/sessions/

Qwen Code

~/.qwen/projects/

OpenClaw

~/.openclaw/agents/

QClaw

~/.qclaw/agents/

Kimi

~/.kimi/sessions/

Kiro CLI

~/.kiro/sessions/cli/
, 
~/.local/share/kiro-cli/

Kiro IDE

~/Library/Application Support/Kiro/
 (macOS)

Cortex Code

~/.snowflake/cortex/conversations/

Hermes Agent

~/.hermes/sessions/

WorkBuddy

~/.workbuddy/projects/

Forge

~/.forge/

Piebald

~/.local/share/piebald/

Warp

~/.warp/
 (platform-dependent)

Positron Assistant

~/Library/Application Support/Positron/User/
 (macOS)

Antigravity

~/.gemini/antigravity/

Antigravity CLI

~/.gemini/antigravity-cli/
 (see note below)

Each directory can be overridden with an environment variable. See theconfiguration docsfor details.

### Antigravity CLI: high-resolution transcripts

Antigravity CLI sessions now appear in two on-disk formats. Newer releases store
conversation trajectories as SQLite.dbfiles, which agentsview indexes
directly. Older releases stored assistant turns and tool calls in
AES-GCM-encrypted.pbfiles; for those sessions, agentsview falls back tosummary modeusing your prompts fromhistory.jsonlplus any plain-text
artifacts underbrain/(plans, walkthroughs, checkpoints).

To unlock full transcripts for older.pbsessions, runagy-readeralongside agentsview.
agy-reader talks to the local Antigravity daemon, decrypts each conversation,
and writes a<uuid>.trajectory.jsonsidecar next to the encrypted.pbfile.
agentsview's file watcher detects the sidecar automatically and parses it in
place of summary mode -- no agentsview restart needed.

go install github.com/mjacobs/agy-reader@latest

#
 Generate sidecars for existing sessions...

agy-reader --sync

#
 ...or keep them fresh as you work.

agy-reader --watch

agy-reader auto-discovers the Antigravity daemon URL by parsing~/.gemini/antigravity-cli/cli.log. If discovery fails (e.g. the log has
rotated), the command prints platform-specific instructions for locating the
port and exportingANTIGRAVITY_DAEMON_URLmanually.

Sidecars stay on your machine. agentsview makes no outbound request to produce
or read them, and treats sidecars as untrusted structured input -- seeSECURITY.mdfor the trust model.

## PostgreSQL Sync

Push session data to a shared PostgreSQL instance for team dashboards:

agentsview pg push 
#
 push local data to PG

agentsview pg serve 
#
 serve web UI from PG (read-only)

### Automatic push (background service)

To keep a shared PostgreSQL database current without runningpg pushby hand,
run the auto-push daemon. It watches your session directories and pushes shortly
after new sessions are recorded, with a periodic floor as a safety net:

agentsview pg push --watch 
#
 foreground, Ctrl-C to stop

agentsview pg push --watch --debounce 1m 
#
 custom coalesce window

agentsview pg push --watch --interval 5m 
#
 custom floor interval

The daemon reads the same[pg]config aspg push, so the PostgreSQL DSN must
be set in your config file (or an environment variable it expands). Protect the
config file, since it holds credentials:

chmod 600 
~
/.agentsview/config.toml

To run it unattended as an OS service (launchd on macOS,systemd --useron
Linux):

agentsview pg service install 
#
 generate the unit, enable + start it

agentsview pg service status 
#
 show manager status

agentsview pg service logs -f 
#
 follow the service log

agentsview pg service uninstall 
#
 stop and remove

Linux headless machines:systemd--userservices stop at logout and do not
start at boot unless lingering is enabled for your user.installdetects this
and prints the command; you can also run it yourself:

loginctl enable-linger 
"
$USER
"

SeePostgreSQL docsfor setup and
configuration.

## DuckDB Mirror and Quack

DuckDB support is a mirror backend, not a replacement for the local SQLite
archive.agentsview servestill performs primary ingestion into SQLite. Use
DuckDB when you want a portable analytics file, read-only local serving from a
mirror, or remote read access through DuckDB's Quack protocol.

agentsview duckdb push 
#
 mirror SQLite into DuckDB

agentsview duckdb status 
#
 show mirror sync status

agentsview duckdb serve 
#
 serve web UI from DuckDB (read-only)

agentsview duckdb quack serve 
#
 expose the local DuckDB file over Quack

agentsview duckdb servereads[duckdb].pathorAGENTSVIEW_DUCKDB_PATH. To
serve from a remote Quack endpoint, setAGENTSVIEW_DUCKDB_URLandAGENTSVIEW_DUCKDB_TOKENinstead. Quack is still a new DuckDB protocol, so
agentsview keeps conservative defaults: local Quack serving binds to loopback,
requires a token, and rejects non-loopback plain HTTP unless--allow-insecureis explicit. For remote use, prefer a TLS URL or put Quack behind an
authenticated tunnel/proxy.

Backend modes:

* SQLite: primary local archive, file sync, FTS5 search, and writable UI.
* PostgreSQL: optional shared team backend; push from SQLite, serve read-only.
* DuckDB: optional mirror file or Quack endpoint; push from SQLite, serve
read-only.

Troubleshooting:

* Ifduckdb pushfails to open the mirror, confirm the binary was built with
the DuckDB Go driver for your platform and thatAGENTSVIEW_DUCKDB_PATHpoints to a writable file location.
* If Quack commands fail with extension errors, update the agentsview binary so
the embedded DuckDB runtime includes the Quack extension.
* If a remote attach fails, check the token, thequack:URL, TLS/proxy
termination, and whether the server was intentionally started with--allow-insecurefor plain non-loopback binds.
* DuckDB search currently uses substring/regex fallback behavior. SQLite FTS5
remains the indexed search path for primary local serving.

## Privacy

agentsview sends a limited anonymousdaemon_activetelemetry ping to PostHog
when the server starts and every 24 hours while it runs, using a stable random
install ID as the eventDistinctId. The event includesapplication=agentsview, app version, commit, OS, and CPU architecture, with$process_person_profile=falseand$geoip_disable=true. It does not include
session, project, prompt, file path, account, or machine identity. Disable
telemetry withAGENTSVIEW_TELEMETRY_ENABLED=0orTELEMETRY_ENABLED=0.
Telemetry is also hard-disabled in Go test binaries, regardless of environment.

All session data stays on your machine. The server binds to127.0.0.1by
default. The update check is optional and can be disabled with--no-update-check.

## Documentation

Full docs atagentsview.io:Quick Start--Usage Guide--CLI Reference--Configuration--Architecture

## Development

Requires Go 1.26+ (CGO), Node.js 22+.

make dev 
#
 Go server (dev mode)

make frontend-dev 
#
 Vite dev server (run alongside make dev)

make build 
#
 build binary with embedded frontend

make install 
#
 install to ~/.local/bin

make 
test
 
#
 Go tests (CGO_ENABLED=1 -tags "fts5,kit_posthog_disabled")

make bench-backends 
#
 compare SQLite, DuckDB, and PostgreSQL store reads

make lint 
#
 golangci-lint + NilAway

make nilaway 
#
 NilAway through custom golangci-lint

make e2e 
#
 Playwright E2E tests

make bench-backendsrequires Docker. It starts a PostgreSQL container with
testcontainers, mirrors the same SQLite fixture into DuckDB and PostgreSQL, and
benchmarks the shareddb.Storeread queries for relative comparison. The
default fixture is 1,000 sessions and 64,000 messages; useBENCH_BACKENDS_SESSIONSandBENCH_BACKENDS_MESSAGES_PER_SESSIONto scale it.
When the Docker CLI uses a non-default socket, exportDOCKER_HOSTfor that
socket before running the benchmark.

Pre-commit hooks viaprek: runmake lint-toolsandmake install-hooksafter cloning (requiresprekanduv).

### Project Layout

cmd/agentsview/ CLI entrypoint
internal/ Go packages (config, db, parser, server, sync, postgres)
frontend/ Svelte 5 SPA (Vite, TypeScript)
desktop/ Tauri desktop wrapper

## Acknowledgements

Inspired byclaude-history-toolby Andy Fischer andclaude-code-transcriptsby
Simon Willison.

## License

MIT

## About

Local-first session intelligence and analytics for coding agents, supporting Claude Code, Codex, and more than 20 other agents. Also: 100x faster replacement for ccusage!

agentsview.io

### Resources

 Readme

 

### License

 MIT license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.6k

 stars
 

### Watchers

4

 watching
 

### Forks

172

 forks
 

 Report repository

 

## Releases52

v0.32.1

 Latest

 

Jun 5, 2026

 

+ 51 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go75.5%
* TypeScript13.3%
* Svelte8.8%
* Rust1.0%
* Shell0.4%
* Python0.4%
* Other0.6%