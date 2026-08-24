---
title: 'GitHub - AgriciDaniel/claude-obsidian: Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy''s LLM Wiki pattern. · GitHub'
url: https://github.com/AgriciDaniel/claude-obsidian
site_name: github
content_file: github-github-agricidanielclaude-obsidian-self-organizing
fetched_at: '2026-08-24T11:25:12.893043'
original_url: https://github.com/AgriciDaniel/claude-obsidian
author: AgriciDaniel
description: Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy's LLM Wiki pattern. - AgriciDaniel/claude-obsidian
---

AgriciDaniel

 

/

claude-obsidian

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star11.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

243 Commits
243 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
.windsurf/
rules
.windsurf/
rules
 
 
agents
agents
 
 
assets
assets
 
 
bin
bin
 
 
claude_obsidian
claude_obsidian
 
 
config
config
 
 
docs
docs
 
 
examples/
sample-vault
examples/
sample-vault
 
 
hooks
hooks
 
 
scripts
scripts
 
 
skills
skills
 
 
templates/
vault
templates/
vault
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
ATTRIBUTION.md
ATTRIBUTION.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
RELEASE_MANIFEST.json
RELEASE_MANIFEST.json
 
 
SECURITY.md
SECURITY.md
 
 
SHA256SUMS
SHA256SUMS
 
 
WIKI.md
WIKI.md
 
 
View all files

## Repository files navigation

# claude-obsidian

Build an Obsidian knowledge base that becomes more useful every time you use it.Capture sources, create connected notes, retrieve grounded answers, and keep the vault healthy—without giving up ownership of your files.

See the workflow·Quick start·Explore the skills·Installation guide·Windows & WSL

claude-obsidian is a local-first knowledge system for Claude Code and compatibleAgent Skillshosts. It turns source material into
linked, source-cited Obsidian pages; answers from the evidence already in the
vault; and provides explicit workflows for research, retrieval, maintenance,
and visual mapping.

Your vault remains a normal directory of Markdown, JSON, and source files. It is
not hidden in a plugin cache, locked in a cloud database, or silently uploaded
to a model.

## From source to living knowledge

Most AI note workflows stop after saving text. claude-obsidian is organized
around a repeatable loop: retain the source, ground the claims, connect the
knowledge, then put it back to work.

* Capture with context.Bring local sources through a visible inbox and
preserve immutable, content-addressed copies before synthesis.
* Ground every important claim.Source and claim ledgers retain authority,
freshness, support, contradiction, confidence, and review state.
* Connect what you learn.Build linked pages, indexes, Maps of Content,
methodology-aware structures, and Obsidian Canvas views.
* Use the vault again.Query, research, retrieve, lint, and fold what is
already known instead of starting every conversation from zero.

## See the vault

The output is meant to remain useful with or without an agent: plain Markdown
for portability, Obsidian for navigation and visual exploration.

Linked knowledge in Graph view · A visual knowledge map in Obsidian Canvas

## Why it feels different

* Local by default.The vault is user-owned and works as ordinary files.
Network egress is a separate, explicit decision.
* Sources survive the summary.Notes point back to durable source evidence;
unsupported and contradictory claims remain visible.
* Knowledge compounds deliberately.Ingestion, querying, linting, retrieval,
research, and rollups share one provenance-aware model.
* Parallel agents cannot race the vault.Workers return drafts. One
orchestrator inspects and applies one recoverable transaction.
* Capabilities are stated honestly.Optional tools are detected, maturity
is declared, and missing adapters degrade clearly instead of being simulated.

This is not an automatic transcript recorder, a cloud sync service, a factual
oracle, or a substitute for backups and source control.

## Quick start

The safest first run uses a source checkout and a separate user vault. Every
mutating setup command previews its exact operation before it can apply.

### 1. Get the product

git clone https://github.com/AgriciDaniel/claude-obsidian.git

cd
 claude-obsidian

The checkout contains the product. It is not your knowledge vault.

### 2. Initialize a separate vault

export
 GENERATED_AT=
"
$(
date -u +%Y-%m-%dT%H:%M:%SZ
)
"

export
 OPERATION_ID=
"
init-reviewed
"

python3 scripts/claude-obsidian.py init 
"
$HOME
/Documents/MyKnowledgeVault
"
 \
 --generated-at 
"
$GENERATED_AT
"
 --operation-id 
"
$OPERATION_ID
"

Review the JSON plan and copy itsapproved_plan_sha256, then apply that exact
operation:

python3 scripts/claude-obsidian.py init 
"
$HOME
/Documents/MyKnowledgeVault
"
 \
 --generated-at 
"
$GENERATED_AT
"
 --operation-id 
"
$OPERATION_ID
"
 \
 --approved-plan-sha256 
"
<sha256-from-the-plan>
"
 --apply

For an existing Obsidian vault, use the non-destructiveadoptworkflow
described in theinstallation guide.

### 3. Start from the vault

Open the new directory in Obsidian, then run Claude Code from that directory
with the local plugin:

cd
 
"
$HOME
/Documents/MyKnowledgeVault
"

claude --plugin-dir /absolute/path/to/claude-obsidian

Start with:

/claude-obsidian:wiki

Then place a source ininbox/and invoke/claude-obsidian:wiki-ingest. Save an answer explicitly with/claude-obsidian:save; ask the vault with/claude-obsidian:wiki-query.

For Codex, OpenCode, or Gemini, preview and then apply the portable skill links
from the product checkout:

bash bin/setup-multi-agent.sh --host codex
bash bin/setup-multi-agent.sh --host codex --apply

Cursor and Windsurf use workspace-local skill discovery. Marketplace setup,
every supported host, vault adoption, upgrades, and uninstall steps are covered
in thefull installation guide.

## 15 skills, one system

The skills are small enough to invoke directly and coordinated enough to share
the same evidence, vault-selection, and mutation rules.

### Build and use the wiki

Skill

What it does

wiki

Initializes or adopts a vault, diagnoses readiness, and routes work

save

Saves one scoped answer or insight—never an automatic transcript

wiki-ingest

Turns captured sources into linked pages and provenance records

wiki-query

Answers read-only from relevant vault evidence

wiki-lint

Reports dead links, orphans, metadata gaps, stale indexes, and empty sections

### Extend the workflow

Skill

What it adds

autoresearch

Bounded web research with explicit egress and a separate canonical merge

canvas

Wiki-scoped Obsidian Canvas creation and maintenance

defuddle

Clean, readable web content before ingestion

wiki-fold

Extractive, traceable rollups of the operation log

wiki-mode

Generic, LYT, PARA, or Zettelkasten filing conventions

wiki-retrieve

Contextual prefixes, BM25, and optional cosine reranking

wiki-cli

Obsidian CLI reads and search with transaction-safe writes

### Reference skills

Skill

What it provides

obsidian-markdown

Correct Obsidian Flavored Markdown, links, embeds, and callouts

obsidian-bases

Native 
.base
 tables, cards, filters, formulas, and summaries

think

A structured observe, listen, connect, create, and grow review loop

Claude Code exposes namespaced invocations such as/claude-obsidian:wiki-lint; other hosts use their native Agent Skills
invocation. Trigger phrases and exact contracts live in eachskills/<name>/SKILL.md.

## Trust is part of the architecture

The product never treats a source checkout, plugin cache, or contributor state
as the default vault. A vault is selected explicitly, throughCLAUDE_OBSIDIAN_VAULT, by the nearest.claude-obsidian.json, or by one
unambiguous initialized ancestor. If selection is uncertain, the command exits
without writing.

One logical knowledge operation is one recoverable transaction:

1. Read every target and record its expected SHA-256.
2. Let parallel workers return drafts and evidence only.
3. Merge the complete change into one operation bundle.
4. Inspect the bundle, then apply it once.
5. Report the operation ID and exact changed paths.

The core holds one process-lifetime vault lock, journals backups, uses atomic
replacement, and restores the prior state if an apply cannot finish. A changed
target is a conflict, never a silent overwrite. Git checkpoints, destructive
repairs, network egress, and canonical research merges remain explicit
operations.

Read thetransaction contract,provenance contract, andCompound Vault architecturefor the
machine-facing detail.

## Honest capability boundaries

Input or capability

Current support

Local filesystem sources

Implemented bounded, content-addressed byte capture

Images

Metadata, hash, size, and bounded dimensions when available

PDF and EPUB

Metadata, hash, and size; no built-in semantic extraction

URL and YouTube

Validated consent plans; a configured external runner is required

OCR

Local-file consent plan; a configured external runner is required

BM25 retrieval

Local and deterministic

Contextual prefixes or remote models

Optional and gated by explicit egress consent

Obsidian CLI

Optional for reads/search; filesystem transport remains available

High-risk accepted claims require two independent sources. Unsupported or
contradictory evidence stays visible, and a grounded refusal is preferred over
an invented citation. Model-based retrieval falls back to deterministic BM25
when the embedding or reranking stage cannot be trusted.

## Shape the vault to the way you think

wiki-modecan route new notes using four methodologies without bulk-moving
existing knowledge:

Mode

Filing principle

Generic

Sources, concepts, entities, and sessions

LYT

Maps of Content and linked atomic notes

PARA

Projects, Areas, Resources, and Archives

Zettelkasten

Stable identifiers, atomic notes, and dense links

Generic is the default when no mode is configured. Switching modes changes how
new notes are routed; it does not silently reorganize old ones. See themethodology modes guide.

## Operator reference

Portable CLI

The wrapper ispython3 scripts/claude-obsidian.py.

Command

Effect

doctor --vault PATH

Show vault selection and readiness

init PATH [--approved-plan-sha256 HASH --apply]

Plan or create a separate vault

adopt PATH [--approved-plan-sha256 HASH --apply]

Plan or adopt an existing Obsidian vault

migrate --vault PATH [--approved-plan-sha256 HASH --apply]

Add v1 ledgers and configuration without rewriting legacy data

transaction inspect BUNDLE --vault PATH

Validate a write bundle without mutation

transaction apply BUNDLE --vault PATH --approved-plan-sha256 HASH

Apply one inspected, recoverable operation

transaction recover --vault PATH [--force-stale-lock]

Restore an interrupted operation

lint --vault PATH [--as-of YYYY-MM-DD]

Emit findings deterministic for the declared UTC date

contracts --verify --vault PATH

Execute capability readiness contracts

capture plan --vault PATH [SOURCE ...]

Run a local capture preflight without writes

capture apply --vault PATH [SOURCE ...]

Plan or create immutable content-addressed copies

checkpoint OPERATION_ID --vault PATH

Explicitly commit one completed operation

package validate

Check skills, hooks, manifests, and documentation coherence

release build --output FILE.zip

Build and self-audit a deterministic public artifact

release audit FILE.zip

Audit an artifact without extracting or publishing it

High-level mutating planners emitapproved_plan_sha256. Pin--generated-atand--operation-id, review the JSON operation, and pass that
exact hash with--apply. Filesystem or generated-bundle drift fails before a
vault write.

Repository and vault layout

product repository/ user vault/
├── claude_obsidian/ ├── .gitignore
├── skills/ ├── .claude-obsidian.json
├── hooks/ ├── inbox/
├── scripts/ ├── .raw/
├── templates/vault/ ├── wiki/
├── config/ ├── .obsidian/
├── assets/ └── .vault-meta/ # ignored runtime state
└── tests/

Public artifacts contain product code, deterministic templates, and reviewed
README assets. They reject contributor hot/log state, root raw sources, runtime
metadata, private paths, recognizable personal email addresses, secrets,
symlinks, unsafe archive entries, and unreviewed binaries.

The private development checkout deliberately has no marketplace catalog. The
release builder injects the reviewed catalog only into the distribution-clean
artifact. A public default branch must be populated from that audited tree,
never by pushing contributor-vault state.

Upgrade, rollback, and uninstall

Upgrade the product independently from the vault. For an older vault, first
preview the additive, idempotent migration:

python3 scripts/claude-obsidian.py migrate --vault /path/to/vault \
 --generated-at 
"
$GENERATED_AT
"
 --operation-id migrate-reviewed

Review its hash and rerun with--approved-plan-sha256 HASH --apply.
Migration preserves the legacy raw manifest byte-for-byte and does not infer
claims from prose.

After an interrupted operation, run:

python3 scripts/claude-obsidian.py transaction recover --vault /path/to/vault

Removing the plugin or host links never removes the vault. Delete only the
integration you installed; user notes, sources, ledgers, and Obsidian settings
remain yours.

## Requirements

* Python 3.11 or newer for the portable core
* Obsidian for the visual vault experience; plain Markdown remains usable
without it
* Bash for setup, optional extensions, and shell test suites
* Git only for development, releases, or an explicit knowledge checkpoint

CI exercises Linux and macOS, plus a native-Windows smoke job for the portable
surface. On native Windows (including Git Bash), read-only inspection and
dry-run commands work; vault writes require WSL and fail closed with anUNSUPPORTED_PLATFORMerror otherwise. Approval hashes bind to the reviewing
environment, so review inside WSL when the apply will happen there. Platform
details, the support matrix, and WSL troubleshooting (including hangs from
virtualization conflicts) live in theWindows and WSL guide. The bash setup scripts and shell
test suites remain POSIX-only. Optional tools such as Obsidian CLI, Ollama,
and defuddle are capability-detected and affect only their dependent workflow.

## Development and release

make 
test

The test target runs every hermetic Python and shell suite, product and
capability contracts, skill and hook validation, manifest checks, and package
boundaries. CI repeats the suite on supported Linux and macOS/Python
combinations and verifies a byte-reproducible release build.

Build and audit locally without publishing:

python3 scripts/claude-obsidian.py release build --output dist/claude-obsidian.zip
python3 scripts/claude-obsidian.py release audit dist/claude-obsidian.zip

No command pushes, tags, publishes, opens issues, or creates releases
automatically. SeeCONTRIBUTING.md,SECURITY.md, andCODE_OF_CONDUCT.md.

## Lineage, license, and attribution

The design followsAndrej Karpathy's LLM Wiki patternand useskepano/obsidian-skillsas the reference substrate for Obsidian Markdown, Bases, and JSON Canvas
syntax.

MIT licensed. SeeATTRIBUTION.mdandCITATION.cff.