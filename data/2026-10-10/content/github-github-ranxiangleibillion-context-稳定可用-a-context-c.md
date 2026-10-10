---
title: 'GitHub - ranxianglei/billion-context: 稳定可用 A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single sessions (billions of tokens).上下文压缩插件，兼顾小窗口(100k上下文足矣)省token(省5倍token)和超长会话(数月级别几十亿token单会话)。billion-context is all you need · GitHub'
url: https://github.com/ranxianglei/billion-context
site_name: github
content_file: github-github-ranxiangleibillion-context-稳定可用-a-context-c
fetched_at: '2026-10-10T16:07:51.455590'
original_url: https://github.com/ranxianglei/billion-context
author: ranxianglei
description: 稳定可用 A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single sessions (billions of tokens).上下文压缩插件，兼顾小窗口(100k上下文足矣)省token(省5倍token)和超长会话(数月级别几十亿token单会话)。billion-context is all you need - ranxianglei/billion-context
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,996 Commits
3,996 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
advisories
advisories
 
 
commands
commands
 
 
devlog
devlog
 
 
docs
docs
 
 
hermes-plugin
hermes-plugin
 
 
kernel
kernel
 
 
paper
paper
 
 
pi-subagents
pi-subagents
 
 
proof
proof
 
 
reference
reference
 
 
release-notes
release-notes
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
website
website
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
AUTO-MERGE-GUARDRAILS.md
AUTO-MERGE-GUARDRAILS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLIENTS.md
CLIENTS.md
 
 
CLIENTS.zh-CN.md
CLIENTS.zh-CN.md
 
 
CONFIGURATION.md
CONFIGURATION.md
 
 
CONFIGURATION.zh-CN.md
CONFIGURATION.zh-CN.md
 
 
LICENSE
LICENSE
 
 
MESSAGE-IDENTITY.md
MESSAGE-IDENTITY.md
 
 
MESSAGE-IDENTITY.zh-CN.md
MESSAGE-IDENTITY.zh-CN.md
 
 
PLUGIN.md
PLUGIN.md
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SESSION-IDENTITY.md
SESSION-IDENTITY.md
 
 
SESSION-IDENTITY.zh-CN.md
SESSION-IDENTITY.zh-CN.md
 
 
TECHNICAL-NOTES.md
TECHNICAL-NOTES.md
 
 
TECHNICAL-NOTES.zh-CN.md
TECHNICAL-NOTES.zh-CN.md
 
 
UNIFIED_LOOP_SPEC.md
UNIFIED_LOOP_SPEC.md
 
 
dsh.bundle.patch.yml
dsh.bundle.patch.yml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.build.json
tsconfig.build.json
 
 
tsconfig.json
tsconfig.json
 
 
tsup.config.ts
tsup.config.ts
 
 
View all files

## Repository files navigation

# billion-context

English|中文

Context-compression plugin—billion-context is all you need.

small context windows (100K is enough) ·5× fewer tokens· month-long single sessions (billions of tokens) · high compression quality

npm install -g billion-context --prefix=~/.local

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Cache health at a glance:a healthy session keeps a95–97%prefix-cache hit rate — compression itself costs ≤2%. Sustained lower? Check attribution with/acpor/acp-cache(seeFAQ); usual causes, in order: upstream cache TTL expiry · model switch · a bili bug (please report) · other/unknown.

## Community

QQ Group:
1056132097 (full)
1108730198 (open)

## 📄 Paper / Preprint

* Model-Driven Incremental Hierarchical Compression: Training-Free Multi-Generational Context Management for Long-Lived Coding Agents(English, v0.2)

📝The paper itself is open-sourced under the MIT License as part of the codebase (paper/). It is a living document — anyone may edit it; improvements are welcome via pull request.

A production-scale longitudinal study: 4.5 months, three hosts, 174,327 model calls, 18.76B cumulative input tokens (~24.7B across all hosts), zero window violations on 204,800-token models, marathon sessions of 8,584–12,049 calls.

billion-contextsits betweenanyagent and its model API, rewriting Anthropic/OpenAI streams withacp-kernelcompression. The model decideswhenandwhatto compress into high-fidelity summaries — not a hard truncation limit.

## Why

Long coding sessions blow up context. Each provider charges per token, and once you pass the context window the session degrades or dies.billion-contextcompresses consumed conversation into layered summaries so you can run a single session for days — billions of tokens through one context window.

Unlike a host's built-in summarizer, compression here isincremental, reversible, and prefix-cache friendly: summaries are written in small ranges, can be decompressed on demand, and the cache prefix stays intact.

## How it works

Agent (Claude Code / Codex / Cursor / Aider ...)
 │ you point the agent's base URL at the proxy
 ▼
┌─────────────────┐
│ billion-context│ 1. parse the request (Anthropic or OpenAI shape)
│ proxy │ 2. run acp-kernel compression on the conversation
│ │ 3. inject a `compress` tool + compression philosophy
│ │ 4. forward to the real model API
│ │ 5. rewrite the streaming response
└─────────────────┘
 │
 ▼
 real model API (Anthropic / OpenAI / compatible)

### Context-management tools

The proxy injects four context-management tools into the conversation; the model calls them itself as context grows, and the proxy executescompressserver-side so folded ranges stay summarized in history until restored:

* compress— fold a message range into a detailed summary.
* decompress— restore a compressed range when exact details are needed again.
* search_context— keyword search over compressed summaries and visible messages.
* acp_status— context-usage overview plus which ranges are still compressible.

## Which do I need?

Pick by your client:

Client

Use

pi

billion-context
 — 
bili pi
 (launcher) or 
bili plugin install pi
 (native); standalone 
billion-context-pi
 remains usable — details: 
CLIENTS.md

opencode
 (1.x / 2.x)

billion-context
 — 
bili opencode
 (launcher) or 
bili plugin install opencode
 (native); standalone 
opencode-acp
 remains usable on 1.x — full guide: 
OpenCode

omp

billion-context
 via 
bili omp
 (built-in plugin) or 
bili plugin install omp
 (self-spawning native plugin, no launcher)

dsh

bili dsh
 (launcher — full native plugin via 
--patch
) or 
bili plugin install dsh
 ≡ 
dsh plugin --profile <name> add billion-context
 (one unified lane) — details: 
CLIENTS.md

kimi

bili plugin install kimi
 (self-spawning native, Kimi Code ≥ 2.0.0) or 
bili kimi
 (cert-MITM) or 
/bili/
 prefix — details: 
CLIENTS.md

hermes

bili plugin install hermes
 (self-spawning native, Python plugin #958) or 
bili hermes
 (cert-MITM)

zcode
 (Z.ai / bigmodel coding plan)

bili plugin install zcode
 (self-spawning native, #1145) or cert-MITM via the GUI's Settings → Network or 
/bili/
 prefix — details: 
CLIENTS.md

claude

bili claude
 (launcher) or 
bili plugin install claude
 (native posture, #964 — managed settings block + session-owned proxy; see the notes below)

codex

bili codex
 (launcher — the full zero-config posture) or 
bili plugin install codex
 (MCP-shell tools companion: 
start bili first
 — the shell never spawns a proxy and never routes codex's own traffic) — details: 
CLIENTS.md

jcode

billion-context
 via 
bili jcode
 (cert-MITM) or 
/bili/
 prefix — no native mode (compiled Rust binary, no plugin seam, 
#962
)

gemini
 (Gemini CLI)

bili gemini
 (launcher, 
GOOGLE_GEMINI_BASE_URL
 
/bili/
 rewrite) or 
/bili/
 prefix — launcher-only (no in-loop tool seam, #1043)

iflow
 (iFlow CLI)

bili iflow
 (launcher, 
IFLOW_BASE_URL
 
/bili/
 rewrite) or 
/bili/
 prefix

qwen
 (Qwen Code)

bili qwen
 (launcher, cert-MITM) or 
/bili/
 prefix

antigravity
 (Antigravity CLI / agy, Google)

bili antigravity
 (launcher, 
CLOUD_CODE_URL
 
/bili/
 rewrite of cloudcode-pa.googleapis.com) or 
/bili/
 prefix — no plugin seam (closed Go language_server; its user-plugin surface is additive-only, #2115) — details: 
CLIENTS.md

mcode
 (MiniMax Code)

billion-context
 via 
bili mcode
 (cert-MITM) or 
/bili/
 prefix — no native mode (event hooks only, no model-request seam, 
#1050
)

aider

billion-context
 via 
bili aider
 (cert-MITM) or 
/bili/
 prefix — no native mode (shell-command-only hooks, no tool-injection seam, 
#1048
)

copilot
 (GitHub Copilot CLI)

bili copilot
 (launcher, cert-MITM) — closed Go binary, no plugin seam (#1049)

amp
 (Amp CLI)

bili amp
 (launcher, cert-MITM) — closed Go binary, no plugin seam (#1049)

crush
 (Charm Crush)

bili crush
 (launcher, cert-MITM) — open-source Go binary, no plugin seam; built-in provider hosts whitelisted, custom 
base_url
s auto-discovered from crush.json (#2340)

zed
 (Zed editor)

bili zed
 (launcher, cert-MITM) — open-source Rust editor, no plugin seam; reqwest honors HTTPS_PROXY, CA via SSL_CERT_FILE (Linux env probing); built-in provider hosts whitelisted, custom 
api_url
s auto-discovered from settings.json; loopback providers (ollama/lmstudio) stay direct via NO_PROXY (#2340)

goose
 (Goose CLI)

bili goose
 (launcher) — rustls trusts no CA file, so no cert-MITM: openai/anthropic legs via 
OPENAI_HOST
/
ANTHROPIC_HOST
, custom providers via a regenerated 
GOOSE_PATH_ROOT
 overlay (#1049)

everything else
 (no context hook)

billion-context
 — 
bili <client>
 (launcher, preferred) or 
/bili/
 prefix

Native mode vs standalone extensions.The host-native plugins (bili plugin install …) and the standalone in-process extensions (billion-context-pi,opencode-acp) aremutually exclusive— both active means double compression. The installer makes the switch: it replaces the legacy entries (bare name,npm:alias, versioned, path form; array or object shape) and snapshots the original config to.bili-bakonce; aproject-localinstall is not touched — remove that one by hand. As a runtime safety net for manual installs, the native entries setBILLION_CONTEXT_NATIVE=<host>synchronously at load so a standalone extension can stand down at action time. On the pi side the marker needsbillion-context-pi0.1.72+, and the pi-native entry scans both pi settings files once its proxy is up and warns loudly when it spots a co-resident legacy entry the installer never saw — that warning is the only visible signal while an oldbillion-context-pisilently double-compresses.

## Install

Linux / macOS — install with a user-level prefix (nosudo, no npm config
changes, andbili's self-update never hits permission errors):

npm install -g billion-context --prefix=
~
/.local

Thebilicommand lands in~/.local/bin— already on PATH in most distros;
if not, addexport PATH="$HOME/.local/bin:$PATH"to~/.bashrcor~/.zshrc. On nvm or Homebrew Node the default prefix is already user-owned —
a plainnpm install -g billion-contextworks as-is. On Windows the default
prefix (%APPDATA%\npm) is also user-writable — plainnpm install -g billion-context.

This installs thebilicommand (bili-proxyis kept as an alias). HittingEACCESwith an old root-owned prefix? Reinstall with--prefix=~/.local(pass the flag again on any future npm reinstall ofbili) — that is the
permanent fix; avoidsudo.

## Quickstart

Three ways to use it — pick one:

* Native plugin (most native):bili plugin install <client>— bili
becomes a plugin inside the client; start the client as usual.
* Launcher (config-free):onebili <client>command brings up the proxy and
the client together — no real config file is ever touched.
* URL change (most universal):prefix your client's baseURL with the proxy
origin +/bili/.

Mechanism details behind these three options (plugin lifecycle, runtime-info
protocol, injection priority) live inTECHNICAL-NOTES.md.

Ports, briefly (#1660):bili start(manual) owns8787. Everything a lane
spawns for you (native hooks, launcher lanes) lives in a separate
self-managed zone starting at18787— collisions hop +1 and each lane
remembers its drift, so zero-config installs never fight you for a port,
and a deliberatebili startdaemon is attached by default. An
upgrade-restart that finds the previous build still draining on the lane's
port waits for it to release (up to 5s) and rebinds the SAME port instead of
drifting (#1723); only a genuinely occupied port hops +1 — and that hop is
now logged loudly.

### Option 1 — Native plugin (bili plugin install pi/omp/opencode/dsh/kimi/hermes/zcode)

The proxy lives inside the client: install once, then start the client
exactly as you always do — no launcher command, no env vars, no fixed port,
no URL edits. Supported today forpi,omp,opencode(1.x and
2.x),dsh,kimi,hermesandzcode:

bili plugin install pi 
#
 registers a "billion-context" entry in pi's settings (npm form when bili itself was npm-installed)

bili plugin install omp 
#
 registers an extensions entry in omp's config.yml (~/.omp/agent/config.yml)

bili plugin install opencode 
#
 registers the plugin in opencode's real config + disables native auto-compaction

bili plugin install dsh 
#
 runs 'dsh plugin --profile <name> add billion-context' for every existing profile

bili plugin install kimi 
#
 writes $KIMI_CODE_HOME/plugins/managed/billion-context/kimi.plugin.json (+ installed.json record); per-session routing block lands in config.toml on first start (Kimi Code >= 2.0.0)

bili plugin install hermes 
#
 copies the Python plugin into ~/.hermes/plugins/billion-context/ (+ machine-owned bili.json sidecar) and enables it via `hermes plugins enable billion-context`

bili plugin install zcode 
#
 writes hooks.enabled + a SessionStart hook + mcp.servers.bili into ~/.zcode/cli/config.json; per-session routing lands in the bigmodel provider store on first start

bili plugin remove 
<
client
>
 
#
 undo (dsh removes through the same channel; config snapshots go to .bili-bak)

Where a client has its own plugin channel you can also install natively,
skipping bili commands entirely:

* dsh:dsh plugin --profile <name> add billion-contextis the very
commandbili plugin install dshdrives per profile (npm form only; a git
checkout has no published entry — pasting a GitHub address installs source
withoutdist/and the bundle never loads) — same end state either way
(pnpm into the profile, bundled patch layer mounted by dsh itself); remove
through the same channel. See the dsh section below.
* opencode:add the bare npm name to your real config's plugin list —"plugin": ["billion-context"](npm form only; a git checkout has no
published entry). The package publishesexports["./server"]→dist/agent/opencode-native.js, so opencode loads it through its own
Npm.add machinery and the plugin self-spawns exactly like the
bili-installed form. Do the two things the bili installer would have done
for you too: set"compaction": { "auto": false }in the same config
(otherwise OpenCode's native auto-compaction double-compresses) and keep a
manual backup of the file first.
* claude:this repository doubles as a Claude Code plugin marketplace —/plugin marketplace add ranxianglei/billion-context, then/plugin install billion-context@billion-context, then run/billion-context:bili-setup(it drivesbili plugin install claudefor
you and tells you to restart). Same end state as the bili installer; the
plugin ships no hooks or MCP entries of its own, so nothing
double-registers.

For pi / omp / kimi / claude there is no client-side channel —bili plugin install <client>writes their config entries for you (kimi's declarativekimi.plugin.json+ registry record, claude's managed settings block, …).

Notes:

* Native mode ismutually exclusivewith the standalone in-process extensions (billion-context-pi,opencode-acp) — the installer swaps the entries and snapshots the original config (.bili-bak).
* pi:native installs wire in built-in subagents by default (acp_delegate/acp_delegate_wait/acp_delegate_cancel) — how to disable them while keeping context compression:Pi built-in subagents.
* OpenCode legacy sessions, V1/V2 shapes and caveats:OpenCode.
* kimireports runtime-info at bootstrap only (static headers can't carry per-request window/model values); subagent tool calls are routed by the proxy's outbound tool-use witness ring (#1685) — no model-visible conversation id.
* hermes's native plugin is Python: it points hermes' httpx stack at the proxy via env vars after a health check and stamps per-request headers through anllm_requestmiddleware.
* codexis the one client a plugin install cannot make self-sufficient: codex routes model traffic via env only (no config-file routing seam for the default ChatGPT-login provider — a managedmodel_providersblock would force API-key auth and drop subscription login), and an MCP server cannot inject env into its parent.bili plugin install codexwrites a single[mcp_servers.bili]block into~/.codex/config.toml(command = node, args = dist/mcp.js) exposing the four ACP tools; at session start the shell resolves a proxy — envBILI_MCP_PROXY> the live-instance record (any lane's proxy or abili startdaemon) > the 8787 user-zone default (#1660 removed the install-time origin bake, #403) — nothing reachable →tools/listfails with -32003. So: start bili first (bili startor any client's lane proxy), export HTTPS_PROXY yourself if you also want compression, or usebili codexfor the zero-config full posture. Mechanics:CLIENTS.md.
* claudehas a native posture (#964): managed settings block +SessionStarthook + MCP shell; the hook rides the self-managed port zone (#1660) and re-pins the managed URL to the live origin each session, so port drift self-heals. Opt out withBILI_NATIVE_CLAUDE=0(passthrough). Mechanics:TECHNICAL-NOTES.md.Known limitation (#2290):the Claude Desktop app's Code tab (CLAUDE_CODE_ENTRYPOINT=claude-desktop) sets its ownANTHROPIC_BASE_URLon its embedded Claude Code, overriding the managed one — desktop sessions bypass the proxy entirely while the managed block'sDISABLE_AUTO_COMPACT=1still applies, so they get neither bili compression nor native auto-compaction. The hook warns loudly at session start (and records it forbili doctor, which also flags machines where Claude Desktop is installed alongside the native lane); terminal sessions are unaffected.Field-tested 2026-10-06 (#2290):puttingHTTPS_PROXYin the settingsenvblock produced zero CONNECT traffic to a live MITM-enabled proxy on Claude Desktop 2.19675.1 / embedded CC 2.1.288 (Windows 11) — the variable reaches no network stack there, consistent with the CLI finding that CC's undici ignores proxy env vars (whybili claudeuses the/bili/base-URL rewrite instead). As of that version there is no usable routing seam on the desktop Code tab; the lane stays tracked in#2290in case upstream changes behavior. Desktop-only users can restore native auto-compact withbili plugin remove claude.
* zcodehas a native posture (#1145): managed~/.zcode/cli/config.jsonblock + per-session providerbaseURLrewrite. Full mechanics:CLIENTS.md.
* jcodeandaiderhave no native mode (no plugin/MCP/tool-injection seam: #962, #1048) — usebili jcode/bili aider.
* copilot,ampandgooseare launcher-only (#1049); goose cannot be cert-MITMed (rustls trusts no CA file) and rides plain-HTTP base-URL redirects instead.

### Option 2 — Launcher (bili pi/bili codex/bili claude/bili omp/bili opencode/bili hermes/bili dsh/bili codebuddy/bili qoder/bili trae/bili jcode/bili kimi/bili gemini/bili iflow/bili qwen/bili antigravity/bili mcode/bili aider/bili copilot/bili amp/bili goose)

The launcher wraps a client in one command: it starts a proxy on an
independent port (a fresh instance is always spawned — a port is never
reused), then points the client at it —certificate-based MITMwhere the
client honors proxy/CA env vars, or an isolated/bili/config rewritewhere it doesn't. No real config file is ever edited; the client's own
config is READ to discover which HTTPS upstream hosts it talks to, and those
hosts are whitelisted for MITM so the proxy can TLS-terminate exactly them
and blind-tunnel everything else.

bili pi 
#
 launch pi through the proxy — file-free (#535): env + extension registerProvider, real ~/.pi untouched

bili codex 
#
 launch codex through the proxy

bili claude 
#
 launch claude through the proxy

bili omp 
#
 pi-style, file-free (#535): env + extension registerProvider + compaction cancel, real ~/.omp untouched

bili opencode 
#
 OpenCode (1.x & 2.x): full guide in the [OpenCode](CLIENTS.md#opencode) section below

bili hermes 
#
 file-free (#535): hermes proxy env (HTTPS_PROXY + combined CA bundle via SSL_CERT_FILE) — https via CONNECT MITM, http via absolute-form forward proxy; real ~/.hermes untouched

bili dsh 
#
 deepseek-harness: full native plugin injected via --patch (#941) — real dsh tools, session-bound /acp + /acp-cache (plugin mode); non-loopback upstreams ride proxy envs, loopback keeps the overlay DSH_HOME rewrite (#535); dsh auto-compaction off outside web profiles, and switchable off there via a profile-level full-snapshot override of preset-standard (#1772/#2474)

bili codebuddy 
#
 Tencent CodeBuddy Code CLI: CODEBUDDY_BASE_URL /bili/ rewrite (OpenAI chat completions wire), budget aligned via CODEBUDDY_AUTO_COMPACT_WINDOW; real ~/.codebuddy untouched

bili qoder 
#
 qoder: model endpoint is hardcoded https (no /bili/ rewrite possible) — cert-MITM via HTTPS_PROXY + NODE_EXTRA_CA_CERTS, default model hosts whitelisted (#653)

bili trae 
#
 Trae CLI (ByteDance, closed Go binary, no base-URL override) — cert-MITM via HTTPS_PROXY + SSL_CERT_FILE, model host from TRAE_CLI_API_HOST or the default enterprise gateway (#655)

bili jcode 
#
 jcode (Rust agent harness) — env-only cert-MITM launch: HTTPS_PROXY + SSL_CERT_FILE, model host api.z.ai whitelisted, local loopback providers stay direct via NO_PROXY

bili kimi 
#
 Kimi Code CLI (Moonshot): standard proxy envs except an unconditional loopback bypass — https via cert-MITM, http via absolute-form forward proxy; loopback endpoints inventoried with a manual /bili/ hint (#757)

bili gemini 
#
 Gemini CLI (Google): GOOGLE_GEMINI_BASE_URL /bili/ rewrite to generativelanguage.googleapis.com (Google native wire), real ~/.gemini untouched

bili iflow 
#
 iFlow CLI: IFLOW_BASE_URL /bili/ rewrite to apis.iflow.cn/v1 (OpenAI chat-completions wire), real ~/.iflow untouched

bili qwen 
#
 Qwen Code (multi-protocol gemini-cli fork, no base-URL hook): cert-MITM via HTTPS_PROXY + NODE_EXTRA_CA_CERTS, default DashScope/Qwen model hosts whitelisted, custom relays via --mitm-domain

bili antigravity 
#
 Antigravity CLI (agy, Google): CLOUD_CODE_URL /bili/ rewrite of cloudcode-pa.googleapis.com (undocumented language-server env override, v2.19.1 binary-verified); wire recognized as Google native by path (#2115)

bili mcode 
#
 MiniMax Code CLI: same shape as kimi (proxy envs, unconditional loopback bypass, cert-MITM/absolute-form); session bound via X-Mavis-Session-Id (#1050)

bili aider 
#
 Aider (Python pair programmer): cert-MITM via HTTPS_PROXY + SSL_CERT_FILE/REQUESTS_CA_BUNDLE; endpoint from OPENAI_API_BASE / ANTHROPIC_BASE_URL / --openai-api-base / .aider.conf.yml (#1048)

bili copilot 
#
 Copilot CLI (GitHub, closed Go binary) — cert-MITM via HTTPS_PROXY + SSL_CERT_FILE, api.githubcopilot.com + per-plan subdomains whitelisted (#1049)

bili amp 
#
 Amp CLI (Sourcegraph, closed Go binary) — cert-MITM via HTTPS_PROXY + SSL_CERT_FILE, ampcode.com whitelisted (#1049)

bili goose 
#
 Goose (Block, Rust/reqwest): rustls release builds trust no CA file — openai/anthropic legs via OPENAI_HOST/ANTHROPIC_HOST, custom providers via a regenerated GOOSE_PATH_ROOT overlay (/bili/ rewrites, real config untouched) (#1049)

bili pi --mitm-domain api.foo.com 
#
 add a domain to the MITM whitelist

### Option 3 — URL change (/bili/prefix)

Start the proxy:

bili

Then just prefix your client's existing baseURL withhttp://localhost:8787/bili/.
The full upstream URL is embedded in the path, so the proxy knows where to
forward without any config:

client baseURL before: https://api.openai.com/v1
client baseURL after: http://localhost:8787/bili/https://api.openai.com/v1

For more per-client configuration examples, see the web UI guide athttp://localhost:8787.

Verify.With the proxy running and your config saved, check it answers
and that your first real request shows compression activity in the log:

#
 Health check (proxy up + where it forwards)

curl -s http://localhost:8787/__bili/health

#
 → {"ok":true,"upstream":"https://api.anthropic.com"}

#
 Live session stats (after a real request)

curl -s http://localhost:8787/__bili/stats

Then send one message from your client and watch the log
(~/.local/state/billion-context/bili.log, also printed to stderr). You
should see aprocessTurnline per request, and once the conversation grows,[acp-usage] round N input=X cached=Y (cache hit Z%)+ acompressevent.

### Client deep dives

Everything that doesn't fit in one Quickstart line — how each client's lanes attach, what gets written where, and known limitations — lives inCLIENTS.md: dsh · Kimi Code · Hermes · ZCode · Gemini family (Gemini CLI / iFlow CLI / Qwen Code / Antigravity) · cert-MITM clients that never compress (CONNECT blind tunnels, #897) · unrecognized endpoints going direct (#1290) · OpenCode (launcher / native / pure proxy,/acpstatus & rules, legacy opencode-acp sessions #920).

## FAQ

How do I check my cache hit rate?Don't dig through logs —/acp-cacheprints atext summary report right in the client, headed by a clickableWeb UI link: open it for the web version of the session page — the cache
hit-rateline chartplus per-breakattribution:

The report has four
blocks that pin things down at a glance:GRAND LEDGER(totals + hit% with
an explicitHEALTHYverdict; misses decomposed into new content /
compress re-pay / upstream-ttl-or-client-rewrite) ·FOLD ECONOMICS(per-fold
economics: net tokens saved, paid-back verdicts) ·LINE ITEMS(anomalies
only: hit<85% or miss≥5000). Rule of thumb:compression itself costs ≤2%—
a healthy session sits at95–97%. When you see less, the attribution tells
you which of the usual suspects it was, in this order: ① upstream cache TTL
expiry (shows up as stable-prefix misses — the top-spikes line names idle
times), ② a model switch, ③ a bili bug (report it with the page attached),
④ other/unknown./acp-cache [full]lists every fold & line; same report over
Since #1535 the report ends with aMODEL SWITCHESsection: a mid-session
model change invalidates the provider's prefix cache, so the whole stable
prefix is re-billed on the next request — each switch's unexplained residual
(itsttlbucket minus new content) is charged to the switch instead of
masquerading as TTL expiry; per-eventfrom → to, hit %, and attributed
tokens are listed (fulllists every event, the summary the last 8), and
the web sessions table gains a matching model-switch column. Since #2131 the
same machinery fingerprints the outbound credential (a 12-hex sha256 of theauthorization/x-api-key-family headers — the raw key is never stored) and
attributes akey switch— the relay behind a stable URL rotated to a
different account — in a dedicatedKEY SWITCHESsection, akey switch:line inCACHE INVALIDATION, and a 🔑 badge in the web sessions column.
HTTP:GET /__bili/cache-report; the raw per-request[acp-usage]lines still
land in the log file for deep dives.

What does/acpshow?In clients with the native plugin (opencode, dsh),/acprenders the ACP status panel of the current conversation straight from
the proxy (session, blocks, compressible ranges, usage); before the first model
request it shows an idle notice instead./acp-cache [full]prints the cache
report above.

Can I query sessions and config over the web?Yes — openhttp://localhost:8787: an overview dashboard, session
list with per-session detail, live logs, a config editor, and an upstream
connectivity test. Everything is also plain JSON for scripting
(/__bili/stats,/__bili/sessions,/__bili/config, …).

When does compression happen?It is model-driven: the injected context
tools are called by the model as context grows, gentle growth nudges
(~50K-token steps by design, adjustable viacompress.nudgeGrowthTokens)
prompt it along the way, and preflight fires as a hard backstop when the input
alone exceeds the window (#470). Watch it live with/acpor the web UI.

Why does the first compaction wait until ~200k?Compaction does not
trigger on absolute window position but on growth intervals: by default the
first soft compaction fires 50k tokens past the boot content
(compress.nudgeGrowthTokens, flat and window-independent). With a boot around
100k — or with the growth step set to ~100k — the first compaction may wait
until ~200k. To make it fire earlier: 1) trim the system prompt, disable
unneeded tools, prune skills; 2) lowercompress.nudgeGrowthTokensto ~50k;
3) enable lean mode. Worked example inCONFIGURATION.md.

Is bili transparent? How do I turn it off?Unrecognized endpoints forward
unchanged (CLIENTS.md), and every mode reverses cleanly:bili plugin remove <client>for native installs, stop using the launcher
command / env vars //bili/prefix for the other two — traffic goes direct
again immediately.

Where are logs and session data stored?Log:~/.local/state/billion-context/bili.log(also mirrored to stderr); session
state:~/.local/share/billion-context/(XDG-overridable; Windows AV exclusion
#362, opt-in cleanup #1082) — full paths inCONFIGURATION.md.

## Running the proxy

### Flags

bili --port 9000 
#
 change listen port

bili --host 0.0.0.0 
#
 listen on all interfaces (see host note below)

bili --debug 
#
 verbose logging (also: set "debug": true in config)

bili --passthrough 
#
 forward without compression (smoke-test mode)

bili --config 
~
/my-bili.json 
#
 use a different config file

bili update 
#
 check & install a newer version now (bypasses throttle)

bili --no-auto-update 
#
 disable self-update for this run

bili --auto-restart-on-update 
#
 self-restart when a new version is installed (default off)

bili --bin /path/to/client 
#
 launcher: spawn this exact client binary instead of auto-detecting (env BILI_CLIENT_BIN)

Flags override env vars and the config file.bili --helplists them all.

### Remote agents (--host)

By default the proxy binds127.0.0.1and only accepts loopback connections. To serve agents on other machines:bili --host 0.0.0.0(or your LAN IP); remote agents point their modelbaseURLathttp://<this-host>:<port>/bili/….

* MITM-modeCONNECTthen also accepts remote clients — forwhitelisted model hosts only. Blind tunnels to arbitrary hosts stay loopback-only, so the proxy can never be used as an open relay.
* /bili/<absolute-url>destination admission (#409): the proxy itself and link-local/metadata addresses are always denied; loopback/private destinations are allowed for local clients (self-hosted upstreams) and denied for remote clients unless listed inBILI_TUNNEL_ALLOWED_HOSTS(hostorhost:port, comma-separated). One exception (#1073): alocalclient relaying a management path (/__bili/*,/__acp/*) to aloopback IP-literaldestination is forwarded unmarked; remote peers and hostname destinations keep the internal tunnel marker unconditionally, and management paths stay unreachable through the tunnel even via NAT hairpin. An absolute-form request addressed to the instance's own endpoint on a management path is served locally instead of tunneled (a forward-proxy-style health probe gets a real answer).
* There isno authentication: only do this on a trusted LAN or behind a firewall. The/__bili/management endpoints remain loopback-only. A startup[security]warning reminds you of the above.

### Debugging

bili --debug(or envACP_DEBUG=1, or"debug": truein config — flag > env > config) logs everyprocessTurn(tag counts, token usage), the nudge decision (growth/usage/pendingT1/shouldInject), client headers, and SSE rewrites.

### Log file

All logs tee to~/.local/state/billion-context/bili.logby default (XDG state dir) and still print to stderr. Override with"logFile"in config orACP_LOG_FILE(offdisables the file). Auto-rotates at 10 MB (bili.log.old). Per-request cache-hit stats log as[acp-usage] round N input=X cached=Y (cache hit Z%)so you can measure prefix-cache health directly from the log.

### Connection lifecycle tuning (#1982)

Client-facing connections close gracefully after the final response: when the proxy initiates the close (Connection: close), it waits up toBILI_POST_RESPONSE_LINGER_MS(default5000) for the client's close signal before releasing the socket, so pooled clients see a clean EOF instead of a possible RST from racing bytes. Related knobs:BILI_KEEP_ALIVE_TIMEOUT_MS(idle-reap budget, default5000) andBILI_CLIENT_ERROR_BACKSTOP_MS(terminal backstop for the error-drain path, default30000) — full semantics inCONFIGURATION.md.

### Self-update

The proxy checks npm on startup and every 3 minutes; a newer version is installed in place and a notice is logged —restartbilito pick it up, unless you enable opt-in self-restart (--auto-restart-on-updateflag, envACP_AUTO_RESTART_ON_UPDATE=1, or"autoRestartOnUpdate": truein config — default OFF): with zero in-flight requests it verifies the new install, stops accepting connections, drains, spawns a replacement on the same port, and exits once it accepts connections (clients reconnect automatically; session state survives on disk). Safety gates: zero in-flight through the drain window, an install sanity check before re-exec, and a 10-minute cooldown marker so a flapping version can never loop-restart; any failure resumes the original listener and falls back to the plain reminder.

While the running process is behind the on-disk install ("stale"), the web UI shows a banner (running vs installed version, auto-restart state) andGET /__bili/statusreturns{version, diskVersion, stale, autoRestartOnUpdate, advisory, inFlight}for scripting (advisoryis the active critical-defect entry ornull, see below). Disable permanently via"autoUpdate": falsein config orACP_AUTO_UPDATE=0.

Inplugin mode(bili opencode/bili pi/bili dsh— the proxy runs embedded in a long-lived host), "restart bili" means restarting thehost: the embedded process cannot exit on its own, so a host left open keeps serving whatever code it started with, silently missing every fix auto-update reports as installed (#1603). Enable--auto-restart-on-updateto have it self-restart at a safe point, or run/acp(OpenCode hosts today — pi/dsh coverage tracked in #2084) — the status panel appends a one-line staleness warning (running vs installed version) whenever the on-disk install is ahead of the live process.

Update visibility is silent by default since v0.1.183 (#1977):routine/recommended releases no longer render an update line on the/acppanel footer or inacp_status— only acritical-tier release surfaces there (CRITICAL UPDATE READY/AVAILABLE). The standing ways to check an installed-but-not-restarted release are the stale cues above: web UI banner, the/acpone-line warning, andGET /__bili/status. Deliberately no always-on nag; the advisory channel (#1481) remains the only auto-visible critical path.

When an install keeps failing (unwritable or host-managed dir, network error, …), auto-update no longer re-downloads and retries on every 3-minute cycle forever. After three consecutive failures it backs off exponentially (5 min → 10 → 20 …, capped at 6 h), logs a one-time actionable hint (fix permissions / npm prefix, reinstall user-level, or disable via"autoUpdate": false/ACP_AUTO_UPDATE=0), and logs nothing further about the failure while cooling down (no download, no retry line); it resumes as soon as the failure clears or a different version is targeted (#1603).

The same bounded retry now covers theowner-managed lanesthe global self-update drives instead of writing the copy itself — the dsh desktop in-place copy, the dsh profile bundles, and pi's npm copy (#2192). Each lane keeps its own failure streak keyed by lane + target version, so a persistently broken desktop layout no longer re-downloads the full tarball every cycle (up to ~480 downloads/day per affected machine before the fix); three strikes arms the same exponential cooldown, and the one-time hint names the failing lane and its manual fix (dsh plugin --profile <name> add …,pi update --extension …, or recreate the desktop profile). Host-managed instances additionally check on their own slower cadence — 30 minutes plus up to 15 minutes of jitter, tracked under a separate throttle marker — instead of consuming the global 3-minute budget. Failure streaks are shared across every bili process on the machine through a small state file in the cache dir (.install-backoff.json), so several running instances don't each burn their own retry budget; a cleanbili plugin updatedisarms the dsh profile lane immediately. The file is written atomically (tmp+rename) and every writer merges with what is already on disk, so concurrent instances cooperate instead of overwriting each other's streaks; long-lived processes re-read it when it changes, so a manual disarm by one copy is visible to the others on their next check. It is fail-safe in the retry direction — a corrupt file or jumped clock is dropped, never allowed to silence a lane for long.bili plugin updateclears the dsh-profile lane's key; a repaired desktop lane clears its own key on its next successful in-place refresh.

### Critical-defect advisories (forced updates)

Independent of auto-update (#1481): even withautoUpdateoff, the proxy polls a small companion npm package (billion-context-advisories, published by CI from this repo'sadvisories/directory) on the same 3-minute cadence. Each advisory names a semver range of broken versions (affected), the exact version to install (target— which may beolderthan the current one, i.e. a rollback), and a user-facingreason. When the local version falls insideaffected, bili force-installstargetthrough the self-updater's full safety chain (cross-process lock, backup + verify + rollback; source checkouts and host-managed installs are refused with manual instructions instead) and warns prominently: a one-time[advisory] ⚠️ …log line per process per advisory id, a banner on the web UI showing the reason and the exact manual upgrade command, and the active entry underadvisoryin/__bili/status. The check is fail-open by design: an unreachable or malformed advisory source only produces a warning — model traffic is never blocked by it. Disable via config ("advisoryCheck": false) or env (BILI_ADVISORY_CHECK=0); point at a custom document with"advisoryUrl"/BILI_ADVISORY_URL.

## Configuration

The full configuration reference — config file location, top-level keys,
providers, compression tuning, environment variables — lives inCONFIGURATION.md.

### Config file

One JSON document at~/.config/billion-context/billion-context.json($XDG_CONFIG_HOME/billion-context/; override the path withBILI_CONFIG_FILE).
Precedence when several sources set the same knob:CLI flag (where one exists) > env var > config file > built-in default— every env var keeps working as the override tier.

What's inside (details in CONFIGURATION.md):

* providers— per-provider routing table: upstream override, model context windows, per-provider/model compress tuning, wire-protocol declaration, compaction opt-in.
* compress— three-level compression tuning (global → provider → model): thresholds, nudge cadence, preservation rules, prompts, tiers.
* Server-level blocks — process-wide behavior, including the #2030 additions:network(timeouts / retry / keep-alive / preflight cadence),persist(session persistence format + tail),sessions(cap + GC policy),update(registry mirror + check interval),diagnostics(dumps, render-tag mode, injection switches),fakeCompletion, plus scalarscodexCompact/ccrRetrievalTtlMs/decompressTmpCapand extensionsmitm.handshakeTimeoutMs,compat.noCacheControl,compat.keepResponseId.

Minimal example:

{
 
"network"
: { 
"upstreamTimeoutMs"
: 
900000
 },
 
"persist"
: { 
"zstd"
: 
true
 },
 
"sessions"
: { 
"gc"
: { 
"enabled"
: 
true
, 
"maxAgeDays"
: 
14
 } }
}

Knobs people look for first:

* Upstream proxy (firewall/GFW)— routing the proxy's own outbound traffic through v2rayA/clash: full resolution order, empty-string = explicit direct, SOCKS5 rejection, both egress paths, and themitm://vshttps://key schemes live inCONFIGURATION.md(Server Settings →proxy; Providers → key schemes).
* Wire-compat role rewrite (compat.roles)— an upstream that rejects thedeveloperrole? Covered byCONFIGURATION.md(Server Settings →compat) — including the learn-on-failure auto-fix that needs no configuration at all.
* Signed upstreams (body-covering signatures)— a gateway whose requests carry a body-covering signature (CodeArts APIG'sSDK-HMAC-SHA256, or gateway-invented headers likex-ofm-signature): the built-in scheme re-signs transparently on dsh; every other detected scheme is ALWAYS refused locally — signed requests are either re-signed+compressed or refused, never passed through unsigned — and bili keeps reminding at startup and in the web UI until it ships the scheme's re-signer (#1884/#2090). Detection rules, per-scheme overrides, andBILI_RESIGN/BILI_RESIGN_PASSTHROUGH/BILI_CODEARTS_REFlive inCONFIGURATION.md(Server Settings →resign).

### Pi built-in subagents

Usingbili pior the native pi plugin (bili plugin install pi) includes built-in subagent support, enabled by default:acp_delegate,acp_delegate_wait, andacp_delegate_cancel. This additional tool surface is specific to pi.

Keep only one subagent implementation enabled.If you use the built-in support, remove or disable other pi subagent plugins (for example,pi-subagentsor a separately installedbillion-context-pi-subagents) in both user and project settings to avoid overlapping tools, prompts, or behavior. If you prefer another subagent plugin, disable the built-in support instead. A project-scopepi-subagentsinstall makes the built-in delegate stand down by default, but a user-scope-only install does not; do not rely on that guard for every installation.

To disable the built-in subagents while keeping context compression, merge this into~/.config/billion-context/billion-context.json(or the file selected byBILI_CONFIG_FILE), preserving your other settings:

{
 
"pi"
: {
 
"subagents"
: 
false

 }
}

Restart pi and start a new session for the change to take effect. This disables the three delegate tools, their system-prompt section, and the fleet keyboard shortcut; context compression remains enabled. It does not disable independently installed subagent plugins. More options:subagent configuration.

## How sessions work

The proxy keys compression state onthe conversation value the client itself provides, verbatim(src/session-id.ts) — no hashing, no protocol/upstream/API-key dimensions (those mutate mid-conversation and orphaned state exactly when users kept talking, #280/#286). The id stays inside the proxy (state store, persistence, UI label); it is never sent upstream.

Where the value comes from, first hit wins: the plugin'sx-bili-plugin-conversation(honored only alongside thex-bili-pluginmarker header), then per-client headers (x-claude-code-session-id,x-grok-session-id/x-grok-conv-id,x-mavis-session-id), then generic
headers (x-session-affinity,x-acp-session,x-session-id,x-opencode-session,session-id/session_id), then body fields:session_id/metadata.session_idon the Responses wire, andprompt_cache_keypromoted over the content-fingerprint fallback on the
Responses/OpenAI/Anthropic wires.

Client

Sends conversation id?

Source

Codex

✅ yes

body.session_id
 / turn-metadata thread id

OpenCode

✅ yes

x-session-affinity
 / 
x-opencode-session
 header (
ses_…
)

Claude Code

✅ yes

x-claude-code-session-id
 header

omp
 (via plugin)

✅ yes

prompt_cache_key
 promoted over any fingerprint (#268)

pi
 (bare)

❌ no

nothing → anonymous prefix affinity below

Header-less clients (pi-like): anonymous prefix affinity.With no conversation signal at all, the proxy resolves the session from the replayed history itself (src/prefix-affinity.ts, #309): a request reattaches to a stored session only when its history reproduces that session's message chain byte-exactly from position 0; otherwise it gets its own deterministicpfa-…session. Consequences (#1262): aresumedconversation reattaches to its own session (even after a proxy restart, #499); anew task with an identical opener does NOT inheritanother conversation's blocks — it mints a fresh, fully separate session; a request with no usable signal at all gets an explicit 400 instead of silently colliding.

Design record and threat model:SESSION-IDENTITY.md. The
message-granularity sibling (why identity is content-derived, not an
assigned id) isMESSAGE-IDENTITY.md.

For upstream sticky-routing, the proxy forwards only identity values the
client already supplied (e.g. a bodysession_idis forwarded upstream asx-session-id); it never synthesizes one itself.

Recommendation:explicit-id clients are safe to run concurrently. For header-less multi-agent use, prefer the client plugin (stamps a stable id per conversation) or pass an explicitx-acp-sessionheader — otherwise prefix affinity still keeps distinct tasks apart (a diverged fork costs one raw resend plus a compression-ladder restart).

### Derived (child) sessions inherit the parent's compressed context (#1333, #1362)

A child session (subagent/fork starting from an empty history) reports its lineage at birth — its identity registration carriesparentConversationIdand the proxy records a read-onlyderivedFromlink — sodecompress/search_contextfall back along the parent chain for content the child never saw itself (cycle-guarded, depth cap 8). Nothing is copied into the child, the parent is never modified; if the parent is unknown the child simply starts fresh. Per-lane parent signals (pi/ompparentSessionheader, OpenCode V1/V2parentID):SESSION-IDENTITY.md. claude/codex/dsh need nothing here: they share one session id across subagents or have no child-session concept at all.

### Windows: exclude the sessions dir from antivirus (#362)

The proxy rewrites each session's state file every turn of a long session; on Windows, real-time AV (Defender), the search indexer, or a sync tool (OneDrive) can lock the sessions dir mid-write, so persists fail withEPERMuntil the lock clears. Fix at the root: add%USERPROFILE%\.local\share\billion-context\to your antivirus exclusions (Defender steps included) and keep sync tools off that path —CONFIGURATION.md.

### Session file cleanup (#1082)

Short-lived sessions leave small state files behind that are never resumed. Cleanup isopt-in(BILI_SESSION_GC=1; off by default — session files are user data, no silent deletion policy): when enabled, bili sweeps the sessions dir at boot and hourly and deletes a file only when BOTH hold — older thanBILI_SESSION_GC_MAX_AGE_DAYS(default 7 days) AND never compressed with its newest request body ≤BILI_SESSION_GC_MAX_TOKENStokens (default 1M) — so deletion loses nothing but bytes. CCR content stores follow their session file's lifecycle; compressed sessions are never deleted; every deletion is audit-logged. Full policy:CONFIGURATION.md.

## Status

Early. Protocol handling and compression work against mock tests (500+ passing). Real-model integration testing is the next milestone. Expect rough edges.

Client-side plugins for pi / omp / opencode ship insidebillion-context(dist/agent/*.js) for the cooperative-proxy path. See the"Which do I need?"section above for howbillion-context, the standalonebillion-context-pi, andopencode-acprelate.

## Attribution requirement (one term on top of MIT)

This project is MIT-licensedplus one additional term: any product or service (commercial or open source) whose users can see or interact with it and which uses this software must attribute it — stating that it uses billion-context with a link back to this repository — on its home page, documentation, or About/Credits page. Pure server-side/embedded use satisfies this via shipped documentation. See theAdditional Termat the end ofLICENSE.

If you build on this project, we'd love to hear about it: open an issue (no obligation) so we can track where it's used.

## License

MIT