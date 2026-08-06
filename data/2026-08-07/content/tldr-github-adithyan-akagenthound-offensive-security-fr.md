---
title: 'GitHub - adithyan-ak/AgentHound: Offensive security framework for AI agent infrastructure - recon, credential looting, model exfiltration, poisoning, and attack-path analysis across MCP, A2A, gateways, and AI services. BloodHound for the agentic stack. · GitHub'
url: https://github.com/adithyan-ak/agenthound
site_name: tldr
content_file: tldr-github-adithyan-akagenthound-offensive-security-fr
fetched_at: '2026-08-07T06:00:31.161657'
original_url: https://github.com/adithyan-ak/agenthound
date: '2026-08-07'
description: Offensive security framework for AI agent infrastructure - recon, credential looting, model exfiltration, poisoning, and attack-path analysis across MCP, A2A, gateways, and AI services. BloodHound for the agentic stack. - adithyan-ak/AgentHound
tags:
- tldr
---

adithyan-ak

 

/

AgentHound

Public

* NotificationsYou must be signed in to change notification settings
* Fork53
* Star232

 
 
 
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

366 Commits
366 Commits
.claude/
rules
.claude/
rules
 
 
.github
.github
 
 
collector
collector
 
 
docker
docker
 
 
docs
docs
 
 
modules
modules
 
 
scripts
scripts
 
 
sdk
sdk
 
 
server
server
 
 
test-infra
test-infra
 
 
testdata
testdata
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
mkdocs.yml
mkdocs.yml
 
 
View all files

## Repository files navigation

### The offensive security framework for AI agent infrastructure

MCP · A2A · model gateways · inference servers · vector stores · MLOps · notebooks · 12 agent clients

Quickstart·Capabilities·Lifecycle·Graph Model·Docs·Safety

Authorized use only.AgentHound ships read-only discoveryandactive exploitation modules. Run it only against infrastructure you own or are written-authorized to assess. SeeSafety & Authorization.

AgentHound is an open-source offensive security framework for AI agent infrastructure.It runs the full engagement - recon, fingerprinting, credential looting,modelfile / system-prompt / fine-tune inventory, model inversion, tool and instruction poisoning, and config-implant persistence - across every layer of the modern agentic stack, then merges every fact into one Neo4j graph and proves the attack paths that tie it all together. Agenthound is BloodHound for the agentic stack.

## ⚡ Capabilities

🌐Full-spectrum agentic attack surfaceOne framework attacks every layer - MCP, A2A, model gateways, inference servers, vector stores, MLOps, notebooks, and 12 agent clients. The whole estate is one target set.

🔓Credential inventory across the gateway & service planeSupply a LiteLLM master key to inventory masked upstream-provider references
and hashed virtual-key references with spend metadata. Only actual credential
values available to AgentHound participate in cross-service correlation.

🧬Modelfile, system-prompt & fine-tune inventoryEnumerate every model on an unauthenticated Ollama - names, digests, sizes,
stable modelfile hashes, system-prompt presence, and fine-tune signals. Raw
modelfiles, templates, and system prompts are available through an explicit
opt-in.

🔬Model inversion / training-data residue extractionA pure-Go GGUF parser runs statistical inversion on the embedding matrix of any weight file you feed it to recover likelyfine-tune vocabulary tokens- surfacing what a model was trained on as graph nodes.

☠️Active exploitation - tool/instruction poisoning + config implantRewrite a ContextForge-managed MCP tool description, injectCLAUDE.md/.cursorrules, or implant a malicious MCP server for persistence. Every mutation is dry-run by default and carries provider-specific recovery state.

🗄️RAG, vector-store & notebook attack surfaceInventory Qdrant collections and Jupyter sessions and notebook trees. Jupyter protected operations are tried without credentials first and retried with an operator-supplied bearer value only after a 401/403, so anonymous access is recorded only when it actually succeeds; bounded tree truncation is published as partial inventory.

🕸️Cross-protocol & credential-chain attack paths15 post-processors compute the routes raw facts can't show - credential chains, cross-protocol pivots, and exfiltration paths across MCP and A2A.

🧪Indirect prompt injection, modeled as data-flowPrompt injection treated as taint propagation: untrusted-input tools → tainted siblings → high-impact sinks, traced as real graph edges.

📊Detection & standards intelligence19 prebuilt attack-path queries, 35 detection rules, 0–100 risk scoring, and retest-as-diff - crosswalked to OWASP MCP / Agentic Top 10 and MITRE ATLAS.

🧩Write your own attacksA new attack against a new AI service is one module away - implement an action interface, drop aregister.go, blank-import it. Same SDK, same lifecycle, same graph.

## 🎯 Every plane of the stack is a target

Surface

Discovery & inventory

Validation / active operations

Agent clients

12 MCP client config formats plus instruction files (
CLAUDE.md
, 
AGENTS.md
, 
.cursorrules
)

Instruction poisoning and reversible malicious-server config implants

MCP

Stdio and HTTP/SSE servers, tools, resources, prompts, and authentication

Credential-reach verification; ContextForge tool-description poisoning and round-trip validation

A2A

Agent cards, JWS verification, skills, delegation, and authentication

Cross-protocol and delegation-path analysis

LiteLLM

Operator-supplied master-key record, masked provider references, and hashed virtual-key metadata with spend context

Cross-service credential correlation and path analysis

Ollama / vLLM

Ollama model metadata, stable modelfile hashes, system-prompt presence, and fine-tune signals; vLLM fingerprinting

Optional raw modelfile, template, and system-prompt capture; local GGUF extraction

Qdrant

Collections, point counts, and optional bounded payload samples

Read-only exposure analysis

MLflow

Experiments, runs, registered models, artifact/storage URIs, and verified anonymous-exposure evidence

Read-only exposure analysis

Jupyter

Sessions and bounded notebook trees

Read-only anonymous-versus-authenticated exposure analysis

Open WebUI / LangServe

Open WebUI authentication posture plus authenticated upstream/RAG credential inventory and observed exposure evidence; LangServe fingerprinting

Read-only credential inventory and exposure evidence

## 📦 By the numbers

* 8 lifecycle CLI commands-scan·discover·loot·extract·poison·implant·revert·campaign(enumerate+fingerprintrun insidescan)
* 8 fingerprinters · 6 looters · 1 model-inversion extractor · 2 poisoners · 1 implanter
* Graph:23 node labels · 32 edge kinds (20 raw + 12 composite) ·15 post-processors
* Intelligence:35 text-detection rules + 7 YAML fingerprint rules + 1 code-backed Jupyter detector · 19 prebuilt attack-path queries · OWASP MCP Top 10 + OWASP Agentic Top 10 + MITRE ATLAS mappings
* One static collector binary with no DB/UI/server dependencies.Config-only discovery can run offline. Apache-2.0 releases include a Cosign-signed checksum manifest and per-archive SPDX SBOMs.

## 🚀 Quick start

Default path prerequisites: Docker + Compose v2. No Go, no Node, nogit clone.

1. Start the analysis server- Neo4j + Postgres + UI, binds127.0.0.1:8080:

curl -sSfL https://raw.githubusercontent.com/adithyan-ak/agenthound/main/docker/docker-compose.public.yml 
|
 docker compose -f - -p agenthound up -d --wait

2. Install the collector- single static binary →~/.local/bin:

curl -sSfL https://raw.githubusercontent.com/adithyan-ak/agenthound/main/install.sh 
|
 sh

export
 PATH=
"
$HOME
/.local/bin:
$PATH
"

Or choose one of these package-manager alternatives:

#
 Homebrew (macOS or Linux; adds the tap automatically)

brew install adithyan-ak/agenthound/agenthound

#
 Go 1.25.12+

go install github.com/adithyan-ak/agenthound/collector/cmd/agenthound@1.0.0

Go installs intoGOBINor, by default,$(go env GOPATH)/bin; ensure that
directory is onPATH.

3. Scan local configs- offline, read-only, raw credential values omitted.
Choose one coverage level and ingest the saved artifact.

Normal scan — recommended first run:

agenthound scan --config --ingest http://127.0.0.1:8080

Deep scan — adds bounded nested-project instruction discovery:

agenthound scan --config --deep --ingest http://127.0.0.1:8080

Both commands check registered instruction sources at your home and selected
project roots. Add--project-dir /path/to/projectwhen the target is not the
current directory. Deep discovery keeps that selected project independently
covered even inside a normally pruned home subtree.

The collector saves./scan-<scan_id>.jsonbefore upload, then prints a compact
ingest receipt. Use--jsonfor the full receipt.

4. Open the graph athttp://127.0.0.1:8080.

The standalone server binary is also available asadithyan-ak/agenthound/agenthound-serverthrough Homebrew. Both binaries are
available from release archives, or from Go at the explicit@1.0.0revision. Release archives include a Cosign-signed checksum manifest
and per-archive SPDX SBOMs - see theinstallation guide.

## 🔪 The offensive lifecycle

Collection commands write ingest-ready JSON. The quickstart above shows the
ingest pattern once.

1. Recon- find the AI estate:

Scan common AI-service ports and fingerprint what responds:

agenthound scan 10.0.0.0/24

Probe likely web ports for MCP and A2A protocol shapes:

agenthound discover 10.0.0.0/24

2. Loot- inventory credential evidence and model metadata:

WithLITELLM_MASTER_KEYset, inventory LiteLLM credential references and
spend metadata:

agenthound loot 10.0.0.20:4000 --type litellm \
 --master-key 
"
$LITELLM_MASTER_KEY
"

Opt in to raw Ollama modelfiles, templates, and system prompts:

agenthound loot 10.0.0.10:11434 --type ollama \
 --include-credential-values

Looter types:litellm,ollama,openwebui,mlflow,qdrant,jupyter.

3. Extract- withAI_MODEL_IDset to an AIModel ID from the graph, invert
a locally-available GGUF weight file to recover fine-tune residue:

agenthound extract 
"
$AI_MODEL_ID
"
 --type embedding-invert \
 --artifact /path/to/model.gguf --commit --engagement-id ENG-1

4. Validate, exploit, persist + revert- run sanctioned, reversible
offensive actions:

With ContextForge authentication configured, run a reversible
poison-and-restore round trip against a managed MCP tool:

agenthound campaign \
 https://gateway.example/servers/0123456789abcdef0123456789abcdef/mcp \
 --scenario mcp-poison-roundtrip --adapter contextforge \
 --target-id support-lookup --engagement-id ENG-ROUNDTRIP --commit

Commit a targeted tool-description poison:

agenthound poison \
 https://gateway.example/servers/0123456789abcdef0123456789abcdef/mcp \
 --type mcp.tool.description --adapter contextforge \
 --target-id support-lookup --inject-file payload.txt \
 --commit --engagement-id ENG-1

Implant a malicious MCP server entry, then roll the engagement back:

agenthound implant localhost --type mcp.config.malicious-server \
 --file 
"
$HOME
/.cursor/mcp.json
"
 --inject-file server-entry.json \
 --commit --engagement-id ENG-1

agenthound revert ENG-1

5. Analyze- pathfind and review:

curl -sSf http://127.0.0.1:8080/api/v1/analysis/prebuilt/credential-chain
curl -sSf 
'
http://127.0.0.1:8080/api/v1/analysis/findings?severity=critical
'

See the fullCLI referencefor
every verb, flag, and module.

## 🔎 What AgentHound finds

AgentHound's findings are built around the questions red teams and defenders ask when they need to understand reachability, blast radius, and pathing risk.

Finding

What it means

Question it answers

Credential-chain paths

The same secret appears in multiple contexts, letting trust cross service boundaries.

Which reused credential gives an agent access it never explicitly had?

Reachability

Agents, MCP servers, tools, resources, prompts, A2A skills, and AI services are joined into one graph.

What can this agent actually reach if trust edges are followed?

Execution paths

An agent can reach shell-like, database, network, or other high-impact tools.

Which agents have a path to command execution, data-plane control, or production impact?

Exfiltration paths

An agent can read sensitive data and also reach an outbound channel.

Where can sensitive data leave the environment?

Cross-protocol pivots

MCP, A2A, host context, and AI-service infrastructure combine into one reachable path.

Can one agent protocol become a bridge into another trust domain?

Tool poisoning

Tool descriptions, prompts, or instruction files contain suspicious model-steering content.

Which tools or instructions could influence model behavior in unsafe ways?

Tool shadowing

A lookalike tool mimics a trusted capability or name.

Which tool could intercept or hijack an expected action?

Rug pulls

A tool's description, schema, or server instructions changed between scans.

What changed since the last known-good graph, and did it create a new risk path?

Unauthenticated servers or agents

MCP servers or A2A protocol handlers affirmatively accepted a credential-free probe; A2A uses a bounded read-only nonexistent-task lookup and never submits a message.

Which exposed agent surfaces need immediate review?

Risk hotspots

Nodes and paths are prioritized with risk scores and prebuilt graph queries.

Where should investigation or remediation start first?

SeeDetection RulesandRisk Scoringfor the full catalog.

## 🔗 Path primitives

AgentHound doesn't just list findings - it creates graph edges you can chain, query, and report:

* CAN_REACH: an agent can traverse trust, credential, host, or protocol relationships to reach a target.
* CAN_EXECUTE: an agent can reach a tool capable of command, database, network, or code execution.
* CAN_EXFILTRATE_VIA: an agent can read sensitive data and send it through an outbound channel.
* CAN_IMPERSONATE: an A2A agent can act as another A2A agent.
* SHADOWS: a tool mimics a trusted tool closely enough to hijack expected behavior.
* POISONED_DESCRIPTION/POISONED_INSTRUCTIONS: tool or instruction text contains model-steering content.

These edges turn AI-agent infrastructure into something you can pathfind instead of manually reason about.

## 🗺️ Example path

flowchart LR
 Agent["AgentInstance<br/>claude-desktop"]
 Notes["MCPServer<br/>internal-notes"]
 Identity["Identity<br/>configured auth"]
 ConfigCred["Credential<br/>configured secret<br/>value_hash: a3f9..."]
 Gateway["LiteLLMGateway<br/>prod"]
 MasterCred["Credential<br/>gateway master key<br/>value_hash: a3f9..."]
 ProviderRef["Credential<br/>masked provider reference<br/>material not observed"]

 Agent -- TRUSTS_SERVER --> Notes
 Notes -- AUTHENTICATES_WITH --> Identity
 Identity -- USES_CREDENTIAL --> ConfigCred
 ConfigCred -. "same value_hash<br/>correlation evidence, not a stored edge" .-> MasterCred
 Gateway -- EXPOSES_CREDENTIAL --> MasterCred
 Gateway -- EXPOSES_CREDENTIAL --> ProviderRef
 Agent -- "CAN_REACH<br/>(derived)" --> ProviderRef

 
Loading

No single config file declares this path. AgentHound hashes the supplied
LiteLLM master key, correlates it with the matching client-config credential byvalue_hash, and computes the derived reachability edge once both outputs land
in the same graph. The dotted correlation is explanatory, not a stored
relationship. The provider target remains a reference-only finding: it does not
assert that AgentHound obtained usable upstream provider secret material.

## 🛡️ Safety & authorization

Built to be run under authorization, with the controls this audience checks for:

* Read-only looter contract- GET/HEAD by default, with documented lookup/search POSTs for APIs that expose no read equivalent and an opt-in Ollama embeddings compute POST via--include-embeddings; each looter is guarded by aget_only_test.goregression test.
* Mutating verbs dry-run by default-poison,implant, and mutation campaigns do not modify a target without--commit.extractperforms its local analysis in dry-run and uses--commitonly to emit ingest data.
* Compile-time-mandatory recovery path-Poisoner/ImplanterembedReverter; every destructive module must implement recovery. Runtime restoration is verified, not guaranteed across provider policy changes, conflicts, or unavailable targets.
* Receipt before mutation- the undo receipt is persisted to diskbeforethe write lands.
* AUTHORIZED gates +--engagement-id- interactive first-run prompts for looting and offensive actions. IDs are required forextract,poison,implant, andcampaign, optional forloot, and recorded on the evidence or receipts those commands emit.
* Recon guardrails- public-IP targets require--allow-public-targetsplus interactiveAUTHORIZED;--authorization-fileoptionally records a path + SHA-256 watermark. Link-local and multicast targets are refused, except for the explicit cloud-metadata address169.254.169.254.

It is explicitly nota C2, a stealth/evasion implant, or a multi-user SaaS. It is transparent, single-user authorized-assessment tooling, and the design says so.

Read thesecurity posture guideandoffensive actions guide.

## 📚 Docs · Contributing · License

Quickstart·CLI·Graph Model·Detection Rules·Security

Write your own attack: implement an action interface, drop aregister.go, blank-import it - seeCONTRIBUTING.mdand themodule authoring guide. Found a vulnerability in AgentHound itself? SeeSECURITY.md.

AgentHound is licensed under theApache License 2.0.