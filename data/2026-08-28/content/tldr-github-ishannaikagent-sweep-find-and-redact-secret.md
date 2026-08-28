---
title: 'GitHub - Ishannaik/agent-sweep: Find and redact secrets in AI coding agent histories (Claude Code, and more). · GitHub'
url: https://github.com/Ishannaik/agent-sweep
site_name: tldr
content_file: tldr-github-ishannaikagent-sweep-find-and-redact-secret
fetched_at: '2026-08-28T21:21:10.091462'
original_url: https://github.com/Ishannaik/agent-sweep
date: '2026-08-28'
description: Find and redact secrets in AI coding agent histories (Claude Code, and more). - Ishannaik/agent-sweep
tags:
- tldr
---

Ishannaik

 

/

agent-sweep

Public

* NotificationsYou must be signed in to change notification settings
* Fork43
* Star67

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

219 Commits
219 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
scripts
scripts
 
 
src/
agentsweep
src/
agentsweep
 
 
tests
tests
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.gitguardian.yaml
.gitguardian.yaml
 
 
.gitignore
.gitignore
 
 
.pre-commit-hooks.yaml
.pre-commit-hooks.yaml
 
 
.vulture_whitelist.py
.vulture_whitelist.py
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
EXPERIMENTS.md
EXPERIMENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# AgentSweep

Find and redact secrets in your AI coding agent's local history. Fully offline.

Watch the full clip with sound

Prevention:Don't paste API keys into cloud-backed AI agents at all. The key transits the provider's servers before it ever hits your disk.

If you already did:agentsweep removes the remaining local attack vector: supply-chain malware and compromised packages that scan your disk for credentials. Your files never leave your machine.

31 agents supported:Claude Code · Codex · OpenCode · Cursor · Windsurf · Aider · Cline · Kilo Code · Roo Code · PearAI · Trae · Void · Gemini CLI · Qwen Code · Continue · Open Interpreter · GitHub Copilot Chat · OpenClaw · Hermes · Goose · llm (Datasette) · Warp · Crush · Grok CLI · Kiro CLI · Zed · Codebuff · Plandex · Junie · Mentat · JetBrains AI

Experimental sources(Warp, Crush, Grok CLI, Kiro CLI, Zed, Codebuff, Plandex, Qwen Code, PearAI, Trae, Void, Junie, Mentat, JetBrains AI) have storage paths/formats derived from research butnot yet verified against a real install. Scanning is safe: a wrong path finds nothing. They may under-report until confirmed. They're tagged(experimental)in the picker and print a notice on scan.

206 regex rules + seed-phrase detection:AWS, GitHub, Stripe, OpenAI, Anthropic, Google, Slack, Discord, HuggingFace, Supabase sensitive tokens, JWT, PEM keys, DB URLs, BIP-39 seed phrases, andmany more

Alpha:every destructive step is gated, backed up, and reversible with one command

## The problem

Claude Code (and every other AI coding CLI) stores your full conversation history as plain-text JSONL on disk, under~/.claude/projects/for Claude Code and~/.codex/sessions/for OpenAI Codex. Anything you paste, whether an AWS key, a.envfile, or a database URL, sits in clear text indefinitely. A typical dev's history accumulates dozens of secrets over months, usually unnoticed.

agentsweepscans that history, tells you what leaked, and can redact the secret values in place while preserving the JSONL structure byte-for-byte. It also tells you which keys to rotate, with the right revocation URL for each provider.

Scope of protection:agentsweep is fully local and offline. It reads and writes only files on your machine and makes zero network calls. It removes one attack vector: secrets sitting in local history files. It does not affect what your AI provider already received. When you paste a key into Claude Code, Cursor, or any cloud-backed agent, that key already transited the provider's servers before it hit disk. If that concerns you, consider a locally-hosted model (Ollama, LM Studio, OpenCode) where nothing leaves your machine, which pairs well with agentsweep.

## Why this matters right now

Supply chain attacks are accelerating. In 2024 and 2025, a wave of malicious npm and PyPI packages (sha256-universal,shailulid, hundreds of typosquats) were caughtexfiltrating developer credentials off the machine that installed them. They target environment variables,.envfiles, shell history, SSH keys, and now AI agent history files.

AI coding assistants have created a new category of credential exposure that didn't exist two years ago:

* You paste a production API key into Claude Code to debug something → it's now in~/.claude/projects/*/conversations/*.jsonlforever
* A compromised npm package runspostinstall→ scans common paths → finds your JSONL history → exfiltrates 50 API keys in one request
* You rotate the key you used in public but forget the dozen others in your history
* Meanwhile your history grows: every.envyou asked an AI to help with, every DB URL you shared for debugging, every token you pasted for a one-liner

AI agent history holds full context, not just the commands a shell history keeps. Attackers already scan for it.agentsweepcleans it up before that happens.

## Quick start

pip install uv 
#
 get uv (skip if you already have it)

uv tool install agentsweep 
#
 install — adds `agentsweep` and `asweep` to PATH

asweep 
#
 run — interactive menu guides you through everything

No virtualenv to activate and no PATH fiddling.uv tool installgives the command its own isolated environment.

## How it works

agentsweep runs a fixed 5-stage pipeline.scanstops after stage 3;fixcontinues through redaction.

flowchart LR
 A("🔍 DISCOVER\nwalk history dirs\nstream file list") --> B("⚡ SCAN\nAho-Corasick pre-filter\n206 regex rules + BIP-39")
 B --> C{"secrets\nfound?"}
 C -- "none" --> D("✅ CLEAN\nexit 0")
 C -- "found" --> E("📋 FINDINGS\nshow report\nexit 1")
 E -. "scan only" .-> F("⚠️ ROTATE\nkeys still live")
 E -- "type REDACT" --> G("✏️ REDACT\natomic write · .bak backup\npost-write JSON validation")
 G --> H("🔑 ROTATE\nper-provider\nrevocation links")

 style A fill:#1e3a5f,color:#fff,stroke:#2d5986
 style B fill:#1e3a5f,color:#fff,stroke:#2d5986
 style C fill:#4a3728,color:#fff,stroke:#7a5c3f
 style D fill:#1a4731,color:#fff,stroke:#2d7a52
 style E fill:#4a3a1e,color:#fff,stroke:#7a6030
 style F fill:#4a2020,color:#fff,stroke:#8b3a3a
 style G fill:#1e3a5f,color:#fff,stroke:#2d5986
 style H fill:#2d1e4a,color:#fff,stroke:#5a3a8b

 
Loading

Eight safety invariants protect every write: atomic replace, mandatory.bakbackup, symlink rejection, mtime and process gates, and post-write JSONL validation.agentsweep undorestores from backups.

## Install

agentsweep is a command-line tool, so install it in its own isolated environment. Both recommended options set that up.

uv (recommended):

uv tool install agentsweep 
#
 install

uv tool upgrade agentsweep 
#
 update

uvx agentsweep@latest 
#
 or run once without installing

### Optional native acceleration

The default install is portable and uses Python's built-inreengine. On
platforms with agoogle-re2wheel, install the optionalfastextra to use
the mixed engine:

uv tool install 
'
agentsweep[fast]
'

#
 or, in a virtual environment:

pip install 
'
agentsweep[fast]
'

This is an acceleration only: unsupported patterns, non-ASCII semantic edge
cases, short strings, and extremely dense matches retain the exact Pythonrepath. If the optional wheel is unavailable, AgentSweep remains fully
functional. Seeperformance notesand thecompatibility audit.

pipx:

pipx install agentsweep
pipx upgrade agentsweep

pipworks too, but keep it inside a virtual environment. Modern Linux and macOS blockpip installinto the system Python (PEP 668), and a CLI has no business there anyway:

python -m venv .venv

source
 .venv/bin/activate 
#
 Windows: .venv\Scripts\activate

pip install agentsweep

You do not need conda. It exists for heavy binary and scientific stacks, and agentsweep is pure Python with three small dependencies.

Android (Termux):

pkg install python clang
pip install agentsweep

Theclangpackage lets the one native dependency build against Android's libc.

Nouv?pip install uvor seeastral.sh/uv. Requires Python 3.11+.

### Docker

Build the image from the repo root:

docker build -t agentsweep 
.

agentsweep scans files under a source's history root (e.g.~/.claude), so
mount your real home directory (or just the relevant agent folder) into the
container and point--rootat it.-u $(id -u):$(id -g)keeps files
written back to the mount (like.bakbackups) owned by you, not root:

docker run --rm -it -u 
$(
id -u
)
:
$(
id -g
)
 \
 -v 
"
$HOME
/.claude:/home/sweeper/.claude:rw
"
 \
 agentsweep scan --source claude-code

Foragentsweep fix, keep the same mount read-write so it can write
redactions and.bakbackups back to your real history directory.

### Shell completions

agentsweepsupports tab-completion for subcommands, flags, and dynamically lists source names for the--sourceoption.

#### Bash

To activate completions for the current session:

eval
 
"
$(
agentsweep completion bash
)
"

#
 Or using the register-python-argcomplete utility:

eval
 
"
$(
register-python-argcomplete agentsweep
)
"

To make it permanent, add the eval line to your~/.bashrc(or equivalent).

#### Zsh

Zsh uses thebashcompinitcompatibility layer. Add the following to your~/.zshrc:

#
 Initialize shell completion if not already done

autoload -U +X compinit 
&&
 compinit
autoload -U +X bashcompinit 
&&
 bashcompinit

eval
 
"
$(
agentsweep completion zsh
)
"

#
 Or using the register-python-argcomplete utility:

eval
 
"
$(
register-python-argcomplete agentsweep
)
"

#### Fish

To activate completions for the current session:

agentsweep completion fish 
|
 source

To make it permanent, save the completion script:

agentsweep completion fish 
>
 ~/.config/fish/completions/agentsweep.fish

#
 Or using the register-python-argcomplete utility:

register-python-argcomplete 
--shell
 fish agentsweep 
>
 ~/.config/fish/completions/agentsweep.fish

#### PowerShell

Works in both Windows PowerShell 5.1 and PowerShell 7+. To activate completions for the current session:

agentsweep completion powershell 
|
 
Out-String
 
|
 
Invoke-Expression

To make it permanent, append the completion script to your profile:

if
 (
-not
 (
Test-Path
 
$PROFILE
)) { 
New-Item
 
-
ItemType File 
-
Path 
$PROFILE
 
-
Force }
agentsweep completion powershell 
|
 
Out-String
 
|
 
Add-Content
 
$PROFILE

If your profile blocks script execution, allow local scripts first withSet-ExecutionPolicy -Scope CurrentUser RemoteSigned.

## Usage

### Interactive mode

Run with no arguments in a terminal and you get the banner, a numbered menu,
typed confirmations before anything destructive, and one-key undo (restores the.bakbackups). Any interactive scan that finds secrets ends with an offer to
redact them on the spot (typeREDACTto confirm):

agentsweep

Scripting is unaffected: any flag, or a piped/redirected stream, skips the
menu and behaves as documented below.

### Verbs

Command

What it does

agentsweep scan

Scan only: read-only, no files are modified (default when no verb given)

agentsweep fix

Scan, then offer to redact findings in place (type 
REDACT
 to confirm)

agentsweep undo

Restore all 
.bak
 backups, reverting any previous redaction

agentsweep purge

Delete all 
.bak
 backups once the leaked keys are rotated (permanent, 
undo
 stops working)

agentsweep list-sources

List every supported agent and show which ones have history on this machine (read-only)

agentsweep explain <rule-id>

Print one detection rule's pattern and its rotation guidance (read-only)

agentsweep --version
 / 
-V

Print the installed version

agentsweep --update

Check PyPI for a newer release

The legacy flag formagentsweep --fixis still accepted and behaves identically toagentsweep fix.

### Source selection

Pick which agent's history to target with--source. The default isclaude-code.

agentsweep scan --source claude-code 
#
 ~/.claude/projects/ or $CLAUDE_CONFIG_DIR/projects/

agentsweep scan --source codex 
#
 ~/.codex/ or $CODEX_HOME/

agentsweep scan --source opencode 
#
 OpenCode SQLite store

agentsweep scan --source cursor 
#
 Cursor history

agentsweep scan --source windsurf 
#
 Windsurf history

agentsweep scan --source aider 
#
 per-repo .aider.chat.history.md under $HOME

agentsweep scan --source crush 
#
 per-project .crush/crush.db under $HOME

agentsweep scan --source cline 
#
 Cline history

agentsweep scan --source gemini-cli 
#
 Gemini CLI history

agentsweep scan --source continue-vscode 
#
 Continue (VS Code) history

agentsweep scan --source github-copilot-chat 
#
 GitHub Copilot Chat history

agentsweep scan --source openclaw 
#
 OpenClaw ~/.openclaw/

agentsweep scan --source hermes 
#
 Hermes Agent ~/.hermes/state.db

agentsweep scan --source goose 
#
 Goose ~/.local/share/goose/

agentsweep scan --source llm 
#
 Datasette llm CLI logs.db (io.datasette.llm/)

Running Claude Code under a custom profile? SetCLAUDE_CONFIG_DIR(the same variable Claude Code honors) and agentsweep scans that profile'sprojects/instead of~/.claude. To scan several profiles at once, for example a personal side-project profile alongside your work one, list them comma-separated and agentsweep scans all of them:

CLAUDE_CONFIG_DIR=
~
/.claude,~/.claude-personal agentsweep scan --source claude-code

Not sure which agents you have installed?list-sourcesprints every supported
source, its history location, and whether that history exists on this machine,
so you know which--sourcevalues are worth scanning. It reads nothing and
writes nothing.

agentsweep list-sources 
#
 all 31 sources + which are on disk

agentsweep list-sources --detected 
#
 only the ones found on this machine

agentsweep list-sources --json 
#
 machine-readable (for scripts/CI)

Wondering why a finding fired, or how to revoke the key it caught?explainprints a rule's pattern and its rotation guidance without scanning anything:

agentsweep explain stripe-live 
#
 pattern + where to roll the key

agentsweep explain --list 
#
 every rule id, one per line

Scaneveryregistered agent in one pass (aggregated findings; redaction stays per-source):

agentsweep scan --all 
#
 all registered sources

agentsweep scan --all --detected 
#
 only sources with a history root on disk

agentsweep scan --all --json 
#
 aggregated JSON (each finding has "source")

agentsweep scan --all --json -o out.json

Claude Code and Codex relocated homes are detected automatically when--rootis omitted:

CLAUDE_CONFIG_DIR=
"
$HOME
/.claude-work
"
 agentsweep scan --source claude-code
CODEX_HOME=
"
$HOME
/.codex-work
"
 agentsweep scan --source codex

An explicit--roottakes precedence over these defaults and can target any
arbitrary folder:

agentsweep scan --source claude-code --root 
~
/backups/claude-history
agentsweep fix --source codex --root /tmp/codex-history-copy

### Scan / fix flags

#
 Machine-readable JSON to stdout (exit 0 = clean, 1 = findings found, 2 = error)

agentsweep scan --json

#
 Write findings JSON to a file instead of stdout

agentsweep scan --json -o findings.json
agentsweep scan --json --output /tmp/report.json

#
 SARIF 2.1.0 for GitHub code scanning / VS Code SARIF viewer (scan only)

agentsweep scan --format sarif -o agentsweep.sarif
agentsweep scan --all --format sarif -o agentsweep.sarif

#
 Skip .agentsweepignore files

agentsweep scan --no-ignore

#
 Plain output with no ANSI colors/styling (also honored via NO_COLOR=1)

agentsweep scan --no-color
NO_COLOR=1 agentsweep scan

#### SARIF in CI

--format sarifemitsSARIF 2.1.0, so findings show up as code-scanning annotations instead of something you have to parse. Rotation guidance rides along in each rule'shelptext, and only the masked preview is included. The secret itself is never written to the report.

- 
name
: 
Scan agent history for secrets

 
run
: 
|

 pipx run agentsweep scan --all --format sarif -o agentsweep.sarif || 
true

- 
uses
: 
github/codeql-action/upload-sarif@v3

 
with
:
 
sarif_file
: 
agentsweep.sarif

|| truekeeps the upload step reachable.scanexits 1 when it finds something, and you want the SARIF to report that rather than the step failing.

### Use with pre-commit

Stop yourself from committing while your agent history holds a live key. Add this to your repo's.pre-commit-config.yaml:

repos
:
 - 
repo
: 
https://github.com/Ishannaik/agent-sweep

 
rev
: 
v0.1.9 
#
 pin to a released tag

 
hooks
:
 - 
id
: 
agentsweep

Thenpre-commit install. The hook runsagentsweep scan --all --detectedon every commit and blocks it (exit 1) if any detected agent history contains a secret. It scans yourhistory roots(~/.claude,~/.codex, ...) rather than the repo's staged files, so it runs once per commit no matter what changed. It works as a per-commit checkpoint. With no agent history on the machine it exits 0 and does nothing.

### Fix-only flags

#
 Redact Claude Code history in place (--allow-production required for default roots during alpha)

agentsweep fix --allow-production

#
 Skip creating .bak backups (not recommended)

agentsweep fix --allow-production --no-backup

#
 Bypass soft safety checks: mtime gate (files modified <60 s ago) and running-process gate

agentsweep fix --allow-production --force

#
 Customize the redaction placeholder (default: [REDACTED:{rule}]); {rule} is

#
 optional. Rejected up front if it contains a path separator or a control

#
 character, or if {rule} substitution would fail.

agentsweep fix --allow-production --redact-with 
"
***{rule}***
"

#
 Combine: non-interactive JSON-mode redaction against a custom root

agentsweep fix --root 
~
/history-copy --json

### Undo flags

#
 Undo redactions for a specific source

agentsweep undo --source codex

#
 Undo against a custom root

agentsweep undo --root 
~
/history-copy

## Corruption-prevention guarantees

A redactor that corrupts your history leaves you worse off than the leak it's fixing. agentsweep enforces these invariants on every--fix:

1. Redaction happens in parsed JSON, not on raw bytes.Secrets are replaced as stringvaluesinside the parsed structure, then re-serialized. Structural damage is impossible by construction.
2. Atomic writes.Every rewrite goes: temp file →fsync()→os.replace()over the original. A crash at any instant leaves either the complete old file or the complete new file, never a torn write.
3. Post-write validation.Before committing, the new content must pass a format-aware check. JSONL: every non-empty line parses as JSON and the line count matches the original. Whole-file JSON: the document parses. Markdown/plaintext: the line count matches the original. SQLite: the rewritten copy passesPRAGMA integrity_check. If the check fails, the write aborts and the original is untouched.
4. .bakbackup by default.Created owner-readable only (mode0600) since it holds the pre-redaction secrets; refuses to run if a.bakalready exists (so prior backups can't be clobbered).
5. Path containment.Refuses any target that doesn't resolve inside one of the source's history trees (e.g. Windsurf's User dir and its~/.codeium/windsurf/memories/).
6. Symlink rejection.Refuses symlinks outright.
7. mtime window.Refuses files modified in the last 60 seconds (likely an active session).--forceoverrides.
8. Running-process check.Refuses if a Claude Code process appears to be running.--forceoverrides.
9. Alpha-stage production gate.--fixagainst the default~/.claude/projects/root requires--allow-productionuntil v1.0.
10. Audit log.Every write appends SHA256 before/after and path to~/.agentsweep/audit.jsonl.

## Recovery

Every redacted file has a sibling*.bakwith the original bytes. The easiest way to undo all redactions for a source is:

agentsweep undo 
#
 undo Claude Code (default)

agentsweep undo --source codex 
#
 undo a specific source

agentsweep undo --root 
~
/history-copy 
#
 undo against a custom root

If you need to restore a single file manually (e.g. you deleted the undo command's source):

mv session.jsonl.bak session.jsonl

The backups hold thepre-redaction originals, plaintext secrets and all, so a sweep isn't finished until the leaked keys are rotated and the backups are gone. Once you've rotated:

agentsweep purge 
#
 delete Claude Code backups (asks first)

agentsweep purge --source windsurf 
#
 delete a specific source's backups

agentsweep purge --yes 
#
 non-interactive (scripts / CI)

## What's detected

206 high-confidence patterns,plus a checksum-validated crypto seed-phrase detector. It confirms BIP-39 mnemonics (12/15/18/21/24 words, the wallet format behind BTC, ETH, SOL, BNB, ADA, DOGE, LTC, DOT, AVAX and most major chains) and Electrum seeds cryptographically (BIP-39 checksum or Electrum version tag), so English prose that happens to use wallet words won't trigger a false positive.

The patterns: AWS access keys, GitHub tokens (PAT/OAuth/App/fine-grained), Stripe live/test, OpenAI, Anthropic, Google API, Slack bot/user/webhook, Hugging Face, Supabase sensitive tokens, JWT, PEM private keys, DB URLs with embedded passwords, and npm/PyPI/SendGrid/Twilio tokens. On top of those sit 187 rules mapped to thegitleakspack covering GitLab, Grafana, HashiCorp Vault/Terraform, DigitalOcean, Shopify, PlanetScale, Databricks, Atlassian, Azure AD, 1Password, Sentry, New Relic, Mailgun, Datadog, Twilio, Twitter/X, Twitch, Yandex, JFrog, Snyk, Mailchimp, curl credentials on the command line, and many more. The patterns run high-precision: false positives are rare, and provider-context rules are keyword-gated so large pastes stay fast.

## .agentsweepignore— suppress false positives

A false positive you already understand should not keep showing up. Put an.agentsweepignorefile in thescan rootor yourcurrent working
directory(both are read; entries merge). Each non-comment line is one of
four forms:

Form

What it suppresses

rule:<rule-id>

Every finding from that rule

path:<pattern>

Every finding whose relative file path matches the pattern

<relpath>:<line>:<rule>

One exact finding — the fingerprint agentsweep prints next to each hit

a bare literal

Any finding whose secret value matches

Example:

# never flag the demo AWS key
AKIAIOSFODNN7EXAMPLE
# ignore the whole slack-webhook rule
rule:slack-webhook
# ignore findings in nested fixture directories
path:*/fixtures/*
# one exact false positive in a fixture
tests/fixtures/claude/sample.jsonl:42:aws-access-key-id

Path entries use Pythonfnmatchsemantics, where*matches across/and**has no special recursive meaning. For example, usepath:*/fixtures/*rather thanpath:**/fixtures/**.

Copy-paste path: run a scan, copy the fingerprint printed beside the false
positive, paste it into.agentsweepignore, re-scan — it will be gone. Use--no-ignoreto bypass both files when you want a completely fresh pass.

## Config file — persistent default flags

Repeating the same flags on every invocation gets old. agentsweep reads an
optional config file for four flags that are safe to default silently. TOML
keys drop the CLI flag's leading--and use underscores instead of hyphens:

CLI flag

TOML key

--source

source

--no-color

no_color

--format

format

--no-ignore

no_ignore

#
 agentsweep.toml (or .agentsweeprc, same format) in the current directory

source
 = 
"
codex
"

no_color
 = 
true

format
 = 
"
sarif
"

no_ignore
 = 
false

Lookup order (first file found wins, values are never merged across files):

1. ./agentsweep.toml
2. ./.agentsweeprc
3. ~/.config/agentsweep/config.toml

Precedence:CLI flag > config file > built-in default, applied per option.A flag you pass on the command line always overrides the config file's value
forthat same option— it does not clear other configured options. A
configuredformat = "sarif"is skipped entirely (not merged, not erroring)
onfix,--json, or--reportinvocations, since those are incompatible
with SARIF output; it only ever applies to a plainscan.

--allow-production,--force, and--no-backupcanneverbe set from
a config file, even if present in one (agentsweep drops them with a warning)
— those safety gates must stay explicit on every invocation so a stale or
shared config file can't silently weaken a redaction safety check.

## What's NOT detected

* Custom/proprietary secrets without a recognizable prefix.
* Monero seed phrases (25 words from Monero's own wordlist; planned).
* Unknown tokens that look like arbitrary base64.
* Secrets split across multiple messages.
* Anything inside a binary/non-UTF-8 file.

For deeper detection, rungitleaksortrufflehogalongside agentsweep, since their rule packs are more exhaustive. agentsweep earns its keep by covering theagent-history-specific surfacethose tools skip.

## agentsweep vs gitleaks vs trufflehog

They solve different problems and compose well together. agentsweep covers the surface a git-repo scanner was never built for: the local AI-agent history files where pasted keys accumulate.

agentsweep

gitleaks

trufflehog

Primary target

AI agent history (
~/.claude/
, 
~/.codex/
, Cursor, 31 agents)

git repos & commits

git repos, filesystems, cloud, CI

Redacts in place

✅ structure-preserving, atomic, reversible (
undo
)

❌ detection only

❌ detection only

Rotation guidance

✅ per-provider revocation links

❌

❌

Verifies live keys

❌

❌

✅ (network)

Rules

206 (187 mapped to gitleaks rules)

~150

800+ verified

Runs fully offline

✅ zero network calls

✅

⚠️
 verification needs network

Scan your codebase and CI with gitleaks or trufflehog, then scan the agent-history surface they don't touch with agentsweep. Running both is the intent: they overlap and cover each other's blind spots.

## Troubleshooting — “no history found” / permissions / paths

Iflist-sourcesshows a source asnot detectedor a scan finds nothing,
work through this before assuming there are no secrets:

1. Confirm the source is actually installed and detected.agentsweep list-sourcesA missing tool is fine; a tool you use daily should not be missing.
2. Check a non-default profile.Claude Code (and some other agents) can
store history outside the default config dir. Point at the profile you
actually use:CLAUDE_CONFIG_DIR=~/.claude-work agentsweep list-sources --detected
agentsweep scan --root~/.claude-work/projects(Other sources have their own env overrides — see the source table.)
3. Point--rootat a specific directoryto isolate whether default root
resolution is the problem:agentsweep scan --root /path/to/history

## FAQ

How do I remove secrets (API keys) from my Claude Code history?Install withuv tool install agentsweep, runasweep, and the interactive menu scans~/.claude/projects/. When it finds secrets it offers to redact them in place (typeREDACTto confirm). It replaces the values, preserves the JSONL structure byte-for-byte, and keeps a.bakbackup so you canagentsweep undo. The same flow works for Codex, Cursor, and 27 other agents via--source.

Is it safe to run on my real agent history?Yes. Scanning is read-only. Redaction is gated behind a typedREDACTconfirmation, writes atomically (temp file → fsync →os.replace), keeps an owner-only.bakbackup, validates the rewritten file parses before committing, and is fully reversible withagentsweep undo. Nine safety invariants guard every write. SeeCorruption-prevention guarantees.

Which AI coding agents does it support?31, including Claude Code, OpenAI Codex, Cursor, Windsurf, Aider, Cline, Gemini CLI, GitHub Copilot Chat, Continue, and OpenCode. Runagentsweep list-sourcesto see the full list and which ones have history on your machine.

Why doesuvx agentsweepshow an old version?uvx caches tools locally. Useuvx agentsweep@latestto always run the newest version (recommended), or force a cache refresh withuvx --reinstall agentsweep.

Where is OpenCode in the menu?OpenCode support was added in v0.1.1. Runpip install --upgrade agentsweeporuvx agentsweep@latestto get it.

Does agentsweep send my data anywhere?No. It is fully offline, with zero network calls during scanning or redacting. The only optional network call is the background update check, which fetches the latest version number from PyPI.

## Contribution security

agentsweep runs against your most sensitive data, so a malicious contribution would be worth more to an attacker than one to an ordinary tool. Every pull request gets a line-by-line review for backdoors and supply-chain risk before it merges, on top of the usual correctness check. A PR is rejected if it:

* Adds a network call.agentsweep is offline by design, and the only permitted outbound request is the optional PyPI version check. Any new socket /urllib/requests/ webhook call is a hard no.
* Introduces obfuscated or dynamic code:eval/exec/compileon runtime data,base64/hex-decoded payloads, dynamic__import__,pickle/marshalof untrusted input.
* Weakens a safety invariant: anything that writes outsidesafe_write(), drops a post-write validation, skips the.bakbackup, or logs/prints a raw secret value. SeeSafety-first review.
* Pulls in an unvetted dependencyor repins an existing one to an unexpected source/version.
* Edits CI/workflows to exfiltrate secrets or tokens(e.g. printingGITHUB_TOKEN, adding a step that phones home, or touching the PyPI Trusted-Publisher release path).

Every PR also runs GitGuardian and abanditSAST scan in CI (seeSecurity linting), and workflows from first-time contributors require maintainer approval before they execute. Maintainers merge only after this review. A green checkmark on its own is never enough.

## Contributors

Thanks to everyone who has contributed code, bug reports, and ideas. Ask questions or get help in theDiscord server.

## Star Gazers

## License

MIT. See LICENSE.