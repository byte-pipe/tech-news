---
title: 'GitHub - izeigerman/claude-thermos: Keeps your Claude session warm for you · GitHub'
url: https://github.com/izeigerman/claude-thermos
site_name: tldr
content_file: tldr-github-izeigermanclaude-thermos-keeps-your-claude
fetched_at: '2026-07-27T12:06:44.965449'
original_url: https://github.com/izeigerman/claude-thermos
date: '2026-07-27'
description: Keeps your Claude session warm for you. Contribute to izeigerman/claude-thermos development by creating an account on GitHub.
tags:
- tldr
---

izeigerman

 

/

claude-thermos

Public

* NotificationsYou must be signed in to change notification settings
* Fork7
* Star168

 
 
 
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

43 Commits
43 Commits
.github/
workflows
.github/
workflows
 
 
src/
claude_thermos
src/
claude_thermos
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# claude-thermos

Stop paying to rebuild your Claude Code cache.When your main agent waits on a subagent for more than 5 minutes, its prompt cache silently expires, and the next turn re-encodes your entire conversation at the write rate instead of reading it back cheap. On long sessions with many subagents that's roughly 20% of your bill.claude-thermoskeeps the cache warm so you never pay that tax.

## Use

Run Claude Code exactly as you normally would, but throughclaude-thermoswithuvx:

uvx claude-thermos 
#
 instead of: claude

uvx claude-thermos -p 
"
fix the bug
"
 
#
 any claude args pass straight through

Requires Python 3.11+ and theclaudeCLI on yourPATH.

That's it. Warming runs automatically in the background. To disable it for a run without changing the command, setCLAUDE_THERMOS_DISABLE=1.

Tuning (all optional):

Flag

Default

Meaning

--idle

270

Seconds the main agent must be idle before warming kicks in

--interval

270

Seconds between warming cycles

--max-cycles

4

Max warms per idle episode (
auto
 for unlimited)

--subagent-window

540

Seconds a subagent counts as "still active"

## Daemon mode (shared proxy for the IDE and multiple terminals)

The default command warms only theclaudeprocess it launches. Clients that
launchclaudethemselves — theVSCode/Claude Code extension, which spawns
its own bundled binary — never go through it, and neither do other terminals.

claude-thermos serveruns the warming proxy as astandalone daemonon a
fixed loopback port. Point any client at it and they all share one warmer:

claude-thermos serve --port 8787 
#
 run the daemon (Ctrl-C / SIGTERM to stop)

#
 then, for any client:

export
 ANTHROPIC_BASE_URL=http://127.0.0.1:8787
claude -p 
"
fix the bug
"
 
#
 terminal — warmed by the daemon

For the VSCode extension, make sure its process inherits that environment
variable (on macOS,launchctl setenv ANTHROPIC_BASE_URL http://127.0.0.1:8787before launching the app; or export it in the shell you start the editor from).
The extension honorsANTHROPIC_BASE_URL, so its traffic then flows through the
daemon and its main agent stays warm while subagents run.

The daemon observes traffic exactly like the launcher and already tracks many
sessions at once, so a single daemon serves every client on the machine. It
evicts sessions idle longer than--session-ttl(default3600s) so it can run
indefinitely.

Tuning:serveaccepts the same--idle/--interval/--max-cycles/--subagent-windowflags as the default command, plus:

Flag

Default

Meaning

--port

8787

Loopback port the daemon listens on

--upstream

https://api.anthropic.com

Real API the proxy reverse-proxies to

--session-ttl

3600

Seconds a session may sit idle before eviction

Caveat:--upstreammust be the real API, never the daemon's own loopback
address — otherwise the proxy would forward to itself.serverejects a
loopback upstream, so if you exportANTHROPIC_BASE_URLglobally, still start
the daemon with an explicit--upstream https://api.anthropic.com.

## Why your cache keeps expiring

Claude Code's prompt cache uses a5-minute TTL. Every turn, your whole conversation history is served from cache at0.1xthe input price instead of being re-sent at full price, as long as the cache stays alive.

The cache expires if more than 5 minutes pass between requests on the same prefix. The dominant trigger for that gap is not you thinking. It's the main agentblocked on a subagent that runs longer than 5 minutes. A subagent has a different system prompt and tool set, so its requests have adifferentcache prefix and never refresh the main agent's. While the subagent works, the main agent's cached history ages untouched; past 5 minutes it's gone. When the subagent returns, the main agent resumes with a byte-identical, append-only history, and finds its cache missing, forcing a full re-encode at the1.25xwrite rate.

By then the history is large, so the re-encode is expensive: individual collapses re-write 200K to 500K tokens. Measured across roughly 185 local sessions, these rebuilds accounted for about22% of the total bill, money spent re-encoding content that was already cached moments earlier.

## How it works

claude-thermoslaunches Claude Code behind a small local reverse proxy (it pointsANTHROPIC_BASE_URLat a loopback port; all traffic still goes to the real Anthropic API).

1. Observe.The proxy watches/v1/messagestraffic and groups it into sessions andlineages, a lineage being one cache prefix, keyed by model + tool set + system text. The first tool-bearing lineage is themainagent; the rest are subagents.
2. Detect the danger window.When the main lineage goes idleanda subagent is actively running, the main prefix is at risk of expiring.
3. Warm.On an interval under the 5-minute TTL, it replays the main agent's last real request as awarm request: identical cacheable prefix, butmax_tokens: 1and no streaming. The single token is thrown away; the point is the prefill, which reads and refreshes the full cached prefix. Warm requests godirectlyto the API, never through the proxy, so they can't disturb real traffic.
4. Result.When the subagent finishes, the main agent's cache is still warm. It pays a cheap read instead of a full rewrite.

Each warm costs a cache read (0.1x); each rewrite it prevents would have cost a write (1.25x) on a much larger prefix, so the trade is heavily in your favor.

## Event logs & savings

Every session writes to:

~/.claude-thermos/logs/<session_id>/
├── events.jsonl # append-only structured event stream
└── summary.json # rollup totals, written when the session ends

events.jsonlrecords each request/response's token usage plus every warming decision (warm_fired,warm_result,cap_reached,resume_detected, and so on).summary.jsonis the rollup you'll usually read:

Field

Meaning

warms_fired

Warm requests sent

cache_read_total

Tokens read back by those warms

episodes

Idle-with-subagent episodes that ended in a successful resume (a rewrite actually avoided)

rewrite_avoided_tokens

Tokens that 
would have
 been re-written, summed across episodes

warm_cost

What warming cost you: 
0.1 × cache_read_total

rewrite_avoided_cost

What it saved: 
1.25 × rewrite_avoided_tokens

net_savings

rewrite_avoided_cost − warm_cost

All three cost figures are inbase-input-token units(token counts already weighted by their cache multiplier). To turnnet_savingsinto dollars,multiply it by your model's price per input token:

dollars saved ≈ net_savings × (input token price)

For example, at an input price of $3 / 1M tokens, anet_savingsof1_200_000is about1_200_000 × $3 / 1_000_000 = $3.60saved that session.