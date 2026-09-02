---
title: 'GitHub - superlinked/sie: Open-source inference server and production cluster for all the models your agent needs. · GitHub'
url: https://github.com/superlinked/sie
site_name: github
content_file: github-github-superlinkedsie-open-source-inference-server
fetched_at: '2026-09-03T07:20:24.478123'
original_url: https://github.com/superlinked/sie
author: superlinked
description: Open-source inference server and production cluster for all the models your agent needs. - superlinked/sie
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 superlinked

 

/

sie

Public

* NotificationsYou must be signed in to change notification settings
* Fork299
* Star3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

140 Commits
140 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
conformance
conformance
 
 
deploy
deploy
 
 
examples
examples
 
 
integrations
integrations
 
 
packages
packages
 
 
telemetry
telemetry
 
 
tools
tools
 
 
.coveragerc
.coveragerc
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
COMPATIBILITY.md
COMPATIBILITY.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
deny.toml
deny.toml
 
 
mise.toml
mise.toml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# SIE: Superlinked Inference Engine

Self-hosted inference for agents. Every open model your agents call, served from one cluster in your cloud.

Docs|Quickstart|API Reference|Models

⭐Help us reach more developers and grow the SIE community. Star this repo!

## About

SIE is an open-source inference engine that runs the models behind every agent task through one API: search and retrieval, document-to-markdown conversion, structured output, content safety, and the agent loop itself. It replaces the patchwork of a separate model server per task with one system that serves 100+ models, loading each on demand.

* OpenAI-compatible API for drop-in migration:/v1/embeddings,/v1/chat/completions,/v1/completions,/v1/responses
* Pre-configured model catalog: Stella, SPLADE, Qwen3, GLiNER, SigLIP, and more; embedding and retrieval models benchmarked on MTEB
* Serves multiple models simultaneously with on-demand loading and LRU eviction
* Ships Kubernetes and Helm deployment configs for the load-balancing gateway, KEDA autoscaling, and Grafana dashboards
* Integrates with LangChain, LlamaIndex, Haystack, DSPy, CrewAI, Chroma, Qdrant, Weaviate, and LanceDB

## Development

Installmise, then bootstrap the
versioned Python, Rust, Node.js, and Helm toolchains from the repository root:

./tools/init.sh

The common development checks and local server are available as mise tasks:

mise run 
test

mise run lint
mise run typecheck
mise run serve
mise run rust-check
mise run rust-test
mise run gateway-test
mise run server-sidecar-test

The Python workspace uses the committed root lock. Package membership is
explicit inpyproject.toml; a package joins the workspace only in the same
change that adds its complete source. Native audio is always an opt-in build:
install cmake, then runmise exec -- uv sync --frozen --project . --all-packages --all-extras.

## Tasks

One SIE cluster runs the inference behind a whole agent. Each task is a handful of swappable models; browsepackages/sie_server/models/for the full set.

Task

What it does

Models

Search

Embed, match, and rerank to retrieve the right context.

bge-m3
, 
splade-v3
, 
colbertv2
, 
qwen3-reranker

Document to markdown

PDFs, Office files, and scans become clean markdown.

lightonocr
, 
glm-ocr
, 
mineru
, 
paddleocr-vl
, 
docling

Structured output

Schema-valid JSON, extracted or generated.

gliner2
, 
nuner-zero
, 
qwen3.6-27b

Guard content

A safety verdict with a probability you threshold.

granite-guardian-2b

Run the agent loop

Plan steps and call tools with an open LLM, streaming included.

qwen3.6-27b

## Quickstart

1. Start the server

#
 macOS (Apple Silicon) or Linux, native (requires Python 3.12)

pip install 
"
sie-server[local]
"
 
&&
 sie-server serve

#
 Linux, NVIDIA GPU

docker run --gpus all -p 8080:8080 \
 -v sie-hf-cache:/app/.cache/huggingface \
 ghcr.io/superlinked/sie-server:latest-cuda12-default

#
 Linux, NVIDIA GPU — Transformers 5 OCR models (LightOnOCR and GLM-OCR)

docker run --gpus all -p 8080:8080 \
 -v sie-hf-cache:/app/.cache/huggingface \
 ghcr.io/superlinked/sie-server:latest-cuda12-transformers5

#
 Linux, CPU

docker run -p 8080:8080 \
 -v sie-hf-cache:/app/.cache/huggingface \
 ghcr.io/superlinked/sie-server:latest-cpu-default

Docker images are bundle-specific so dependency-incompatible model families stay isolated. Use thetransformers5image for LightOnOCR or GLM-OCR; thedefaultimage intentionally does not advertise them.

#
 in a second terminal

curl http://localhost:8080/readyz 
#
 expect: ok

The server speaks the OpenAI API out of the box, embeddings and generation alike (the cluster gateway serves/v1/chat/completions,/v1/completions, and/v1/responses). Your first call needs nothing but curl:

curl http://localhost:8080/v1/embeddings \
 -H 
'
Content-Type: application/json
'
 \
 -d 
'
{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}
'

#
 {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...

Each model's first call downloads its weights (progress appears in the server terminal). Later calls skip the
download; inference latency depends on the model, task, hardware, and batch size.

2. Install the SDK

pip install sie-sdk 
#
 Python

npm install @superlinked/sie-sdk 
#
 TypeScript (pnpm and yarn work too)

3. Generate embeddings, rerank, and extract entities

from
 
sie_sdk
 
import
 
SIEClient

from
 
sie_sdk
.
types
 
import
 
Item

client
 
=
 
SIEClient
(
"http://localhost:8080"
)

# Generate embeddings

result
 
=
 
client
.
encode
(
"sentence-transformers/all-MiniLM-L6-v2"
, 
Item
(
text
=
"Hello world"
))

print
(
result
[
"dense"
].
shape
) 
# (384,)

# Rerank search results

scores
 
=
 
client
.
score
(
 
"cross-encoder/ms-marco-MiniLM-L-6-v2"
,
 
Item
(
text
=
"What is machine learning?"
),
 [
Item
(
text
=
"ML learns from data."
), 
Item
(
text
=
"The weather is sunny."
)],
)

print
(
scores
[
"scores"
][
0
]) 
# {'item_id': 'item-0', 'score': -7.1, 'rank': 0}

# Extract entities

result
 
=
 
client
.
extract
(
 
"urchade/gliner_multi-v2.1"
,
 
Item
(
text
=
"Tim Cook is the CEO of Apple."
),
 
labels
=
[
"person"
, 
"organization"
],
)

print
(
result
[
"entities"
][
0
])

# {'text': 'Tim Cook', 'label': 'person', 'score': 0.992, 'start': 0, 'end': 8, ...}

Text generation runs on the GPU generation image; stop the first server, then start this one on the same port:

#
 Linux, NVIDIA GPU (for generation on Apple Silicon via MLX, see the docs below)

docker run --gpus all -p 8080:8080 \
 -v sie-hf-cache:/app/.cache/huggingface \
 ghcr.io/superlinked/sie-server:latest-cuda12-sglang

result
 
=
 
client
.
generate
(
 
"Qwen/Qwen3-0.6B"
,
 
"Reply with a single word: the capital of France."
,
 
max_new_tokens
=
16
,
 
temperature
=
0.0
,
)

print
(
result
[
"text"
]) 
# Paris

For generation on Apple Silicon (MLX), the TypeScript walkthrough, and every configuration in between, see thequickstart guide,TypeScript SDK docs, andSDK reference.

### Production

The same code works against a production cluster. SIE ships a load-balancing gateway and Kubernetes deployment surface, including Helm charts, KEDA autoscaling (scale to zero), and Grafana dashboards. Public Terraform modules are maintained separately forAlibaba Cloud ACK,EKS,AKS, andGKE. Not just the server, the whole stack. All Apache 2.0.

#
 pick one values overlay: values-ack.yaml / values-aws.yaml / values-aks.yaml / values-gke.yaml

#
 (pin a chart version for reproducible installs, e.g. --version 0.6.18)

helm upgrade --install sie-cluster oci://ghcr.io/superlinked/charts/sie-cluster \
 --namespace sie --create-namespace \
 --set hfToken.create=true \
 --set hfToken.value=YOUR_HF_TOKEN \
 -f https://raw.githubusercontent.com/superlinked/sie/main/deploy/helm/sie-cluster/values-gke.yaml

See thedeployment guide.

Telemetry: SIE collects anonymous usage data (version, OS, architecture, GPU type) to understand adoption. No IP addresses, hostnames, or request data are collected. Disable withSIE_TELEMETRY_DISABLED=1orDO_NOT_TRACK=1.

### Explore

Model catalog: every model is a config inpackages/sie_server/models/; pass its Hugging Face ID to the SDK.

Integrations: setup guides for all nine framework and vector-store integrations, in Python and TypeScript.

Examples: An end-to-end project gallery.

MCP edge: offload document work from Claude and other MCP clients to your cluster and save agent tokens.

Why we built SIE: The motivation, told at AI Engineer Europe 2026.

superlinked.com/docs| Apache 2.0