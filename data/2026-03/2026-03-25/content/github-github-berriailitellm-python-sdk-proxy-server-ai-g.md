---
title: 'GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM] · GitHub'
url: https://github.com/BerriAI/litellm
site_name: github
content_file: github-github-berriailitellm-python-sdk-proxy-server-ai-g
fetched_at: '2026-03-25T11:19:45.395848'
original_url: https://github.com/BerriAI/litellm
author: BerriAI
description: Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM] - BerriAI/litellm
---

BerriAI

 

/

litellm

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork6.7k
* Star40.4k

 
 
 
 
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

36,173 Commits
36,173 Commits
.circleci
.circleci
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.semgrep/
rules
.semgrep/
rules
 
 
ci_cd
ci_cd
 
 
cookbook
cookbook
 
 
db_scripts
db_scripts
 
 
deploy
deploy
 
 
dist
dist
 
 
docker
docker
 
 
docs/
my-website
docs/
my-website
 
 
enterprise
enterprise
 
 
litellm-js
litellm-js
 
 
litellm-proxy-extras
litellm-proxy-extras
 
 
litellm
litellm
 
 
scripts
scripts
 
 
tests
tests
 
 
ui/
litellm-dashboard
ui/
litellm-dashboard
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.flake8
.flake8
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitguardian.yaml
.gitguardian.yaml
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.trivyignore
.trivyignore
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
codecov.yaml
codecov.yaml
 
 
dev_config.yaml
dev_config.yaml
 
 
docker-compose.hardened.yml
docker-compose.hardened.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
index.yaml
index.yaml
 
 
license_cache.json
license_cache.json
 
 
mcp_servers.json
mcp_servers.json
 
 
model_prices_and_context_window.json
model_prices_and_context_window.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
poetry.lock
poetry.lock
 
 
policy_templates.json
policy_templates.json
 
 
prometheus.yml
prometheus.yml
 
 
provider_endpoints_support.json
provider_endpoints_support.json
 
 
proxy_server_config.yaml
proxy_server_config.yaml
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
render.yaml
render.yaml
 
 
requirements.txt
requirements.txt
 
 
ruff.toml
ruff.toml
 
 
schema.prisma
schema.prisma
 
 
security.md
security.md
 
 
taplo.toml
taplo.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# 🚅 LiteLLM

Call 100+ LLMs in OpenAI format. [Bedrock, Azure, OpenAI, VertexAI, Anthropic, Groq, etc.]

#### LiteLLM Proxy Server (AI Gateway)|Hosted Proxy|Enterprise Tier

## Use LiteLLM for

LLMs
 - Call 100+ LLMs (Python SDK + AI Gateway)

All Supported Endpoints-/chat/completions,/responses,/embeddings,/images,/audio,/batches,/rerank,/a2a,/messagesand more.

### Python SDK

pip install litellm

from
 
litellm
 
import
 
completion

import
 
os

os
.
environ
[
"OPENAI_API_KEY"
] 
=
 
"your-openai-key"

os
.
environ
[
"ANTHROPIC_API_KEY"
] 
=
 
"your-anthropic-key"

# OpenAI

response
 
=
 
completion
(
model
=
"openai/gpt-4o"
, 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"Hello!"
}])

# Anthropic 

response
 
=
 
completion
(
model
=
"anthropic/claude-sonnet-4-20250514"
, 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"Hello!"
}])

### AI Gateway (Proxy Server)

Getting Started - E2E Tutorial- Setup virtual keys, make your first request

pip install 
'
litellm[proxy]
'

litellm --model gpt-4o

import
 
openai

client
 
=
 
openai
.
OpenAI
(
api_key
=
"anything"
, 
base_url
=
"http://0.0.0.0:4000"
)

response
 
=
 
client
.
chat
.
completions
.
create
(
 
model
=
"gpt-4o"
,
 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"Hello!"
}]
)

Docs: LLM Providers

Agents
 - Invoke A2A Agents (Python SDK + AI Gateway)

Supported Providers- LangGraph, Vertex AI Agent Engine, Azure AI Foundry, Bedrock AgentCore, Pydantic AI

### Python SDK - A2A Protocol

from
 
litellm
.
a2a_protocol
 
import
 
A2AClient

from
 
a2a
.
types
 
import
 
SendMessageRequest
, 
MessageSendParams

from
 
uuid
 
import
 
uuid4

client
 
=
 
A2AClient
(
base_url
=
"http://localhost:10001"
)

request
 
=
 
SendMessageRequest
(
 
id
=
str
(
uuid4
()),
 
params
=
MessageSendParams
(
 
message
=
{
 
"role"
: 
"user"
,
 
"parts"
: [{
"kind"
: 
"text"
, 
"text"
: 
"Hello!"
}],
 
"messageId"
: 
uuid4
().
hex
,
 }
 )
)

response
 
=
 
await
 
client
.
send_message
(
request
)

### AI Gateway (Proxy Server)

Step 1.Add your Agent to the AI Gateway

Step 2.Call Agent via A2A SDK

from
 
a2a
.
client
 
import
 
A2ACardResolver
, 
A2AClient

from
 
a2a
.
types
 
import
 
MessageSendParams
, 
SendMessageRequest

from
 
uuid
 
import
 
uuid4

import
 
httpx

base_url
 
=
 
"http://localhost:4000/a2a/my-agent"
 
# LiteLLM proxy + agent name

headers
 
=
 {
"Authorization"
: 
"Bearer sk-1234"
} 
# LiteLLM Virtual Key

async
 
with
 
httpx
.
AsyncClient
(
headers
=
headers
) 
as
 
httpx_client
:
 
resolver
 
=
 
A2ACardResolver
(
httpx_client
=
httpx_client
, 
base_url
=
base_url
)
 
agent_card
 
=
 
await
 
resolver
.
get_agent_card
()
 
client
 
=
 
A2AClient
(
httpx_client
=
httpx_client
, 
agent_card
=
agent_card
)

 
request
 
=
 
SendMessageRequest
(
 
id
=
str
(
uuid4
()),
 
params
=
MessageSendParams
(
 
message
=
{
 
"role"
: 
"user"
,
 
"parts"
: [{
"kind"
: 
"text"
, 
"text"
: 
"Hello!"
}],
 
"messageId"
: 
uuid4
().
hex
,
 }
 )
 )
 
response
 
=
 
await
 
client
.
send_message
(
request
)

Docs: A2A Agent Gateway

MCP Tools
 - Connect MCP servers to any LLM (Python SDK + AI Gateway)

### Python SDK - MCP Bridge

from
 
mcp
 
import
 
ClientSession
, 
StdioServerParameters

from
 
mcp
.
client
.
stdio
 
import
 
stdio_client

from
 
litellm
 
import
 
experimental_mcp_client

import
 
litellm

server_params
 
=
 
StdioServerParameters
(
command
=
"python"
, 
args
=
[
"mcp_server.py"
])

async
 
with
 
stdio_client
(
server_params
) 
as
 (
read
, 
write
):
 
async
 
with
 
ClientSession
(
read
, 
write
) 
as
 
session
:
 
await
 
session
.
initialize
()

 
# Load MCP tools in OpenAI format

 
tools
 
=
 
await
 
experimental_mcp_client
.
load_mcp_tools
(
session
=
session
, 
format
=
"openai"
)

 
# Use with any LiteLLM model

 
response
 
=
 
await
 
litellm
.
acompletion
(
 
model
=
"gpt-4o"
,
 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"What's 3 + 5?"
}],
 
tools
=
tools

 )

### AI Gateway - MCP Gateway

Step 1.Add your MCP Server to the AI Gateway

Step 2.Call MCP tools via/chat/completions

curl -X POST 
'
http://0.0.0.0:4000/v1/chat/completions
'
 \
 -H 
'
Authorization: Bearer sk-1234
'
 \
 -H 
'
Content-Type: application/json
'
 \
 -d 
'
{

 "model": "gpt-4o",

 "messages": [{"role": "user", "content": "Summarize the latest open PR"}],

 "tools": [{

 "type": "mcp",

 "server_url": "litellm_proxy/mcp/github",

 "server_label": "github_mcp",

 "require_approval": "never"

 }]

 }
'

### Use with Cursor IDE

{
 
"mcpServers"
: {
 
"LiteLLM"
: {
 
"url"
: 
"
http://localhost:4000/mcp/
"
,
 
"headers"
: {
 
"x-litellm-api-key"
: 
"
Bearer sk-1234
"

 }
 }
 }
}

Docs: MCP Gateway

## How to use LiteLLM

You can use LiteLLM through either the Proxy Server or Python SDK. Both gives you a unified interface to access multiple LLMs (100+ LLMs). Choose the option that best fits your needs:

LiteLLM AI Gateway

LiteLLM Python SDK

Use Case

Central service (LLM Gateway) to access multiple LLMs

Use LiteLLM directly in your Python code

Who Uses It?

Gen AI Enablement / ML Platform Teams

Developers building LLM projects

Key Features

Centralized API gateway with authentication and authorization, multi-tenant cost tracking and spend management per project/user, per-project customization (logging, guardrails, caching), virtual keys for secure access control, admin dashboard UI for monitoring and management

Direct Python library integration in your codebase, Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - 
Router
, application-level load balancing and cost tracking, exception handling with OpenAI-compatible errors, observability callbacks (Lunary, MLflow, Langfuse, etc.)

LiteLLM Performance:8ms P95 latencyat 1k RPS (See benchmarkshere)

Jump to LiteLLM Proxy (LLM Gateway) DocsJump to Supported LLM Providers

Stable Release:Use docker images with the-stabletag. These have undergone 12 hour load tests, before being published.More information about the release cycle here

Support for more providers. Missing a provider or LLM Platform, raise afeature request.

## OSS Adopters

## Netflix

## Supported Providers (Website Supported Models|Docs)

Provider

/chat/completions

/messages

/responses

/embeddings

/image/generations

/audio/transcriptions

/audio/speech

/moderations

/batches

/rerank

Abliteration (
abliteration
)

✅

AI/ML API (
aiml
)

✅

✅

✅

✅

✅

AI21 (
ai21
)

✅

✅

✅

AI21 Chat (
ai21_chat
)

✅

✅

✅

Aleph Alpha

✅

✅

✅

Amazon Nova

✅

✅

✅

Anthropic (
anthropic
)

✅

✅

✅

✅

Anthropic Text (
anthropic_text
)

✅

✅

✅

✅

Anyscale

✅

✅

✅

AssemblyAI (
assemblyai
)

✅

✅

✅

✅

Auto Router (
auto_router
)

✅

✅

✅

AWS - Bedrock (
bedrock
)

✅

✅

✅

✅

✅

AWS - Sagemaker (
sagemaker
)

✅

✅

✅

✅

Azure (
azure
)

✅

✅

✅

✅

✅

✅

✅

✅

✅

Azure AI (
azure_ai
)

✅

✅

✅

✅

✅

✅

✅

✅

✅

Azure Text (
azure_text
)

✅

✅

✅

✅

✅

✅

✅

Baseten (
baseten
)

✅

✅

✅

Bytez (
bytez
)

✅

✅

✅

Cerebras (
cerebras
)

✅

✅

✅

Clarifai (
clarifai
)

✅

✅

✅

Cloudflare AI Workers (
cloudflare
)

✅

✅

✅

Codestral (
codestral
)

✅

✅

✅

Cohere (
cohere
)

✅

✅

✅

✅

✅

Cohere Chat (
cohere_chat
)

✅

✅

✅

CometAPI (
cometapi
)

✅

✅

✅

✅

CompactifAI (
compactifai
)

✅

✅

✅

Custom (
custom
)

✅

✅

✅

Custom OpenAI (
custom_openai
)

✅

✅

✅

✅

✅

✅

✅

Dashscope (
dashscope
)

✅

✅

✅

Databricks (
databricks
)

✅

✅

✅

DataRobot (
datarobot
)

✅

✅

✅

Deepgram (
deepgram
)

✅

✅

✅

✅

DeepInfra (
deepinfra
)

✅

✅

✅

Deepseek (
deepseek
)

✅

✅

✅

ElevenLabs (
elevenlabs
)

✅

✅

✅

✅

✅

Empower (
empower
)

✅

✅

✅

Fal AI (
fal_ai
)

✅

✅

✅

✅

Featherless AI (
featherless_ai
)

✅

✅

✅

Fireworks AI (
fireworks_ai
)

✅

✅

✅

FriendliAI (
friendliai
)

✅

✅

✅

Galadriel (
galadriel
)

✅

✅

✅

GitHub Copilot (
github_copilot
)

✅

✅

✅

✅

GitHub Models (
github
)

✅

✅

✅

Google - PaLM

✅

✅

✅

Google - Vertex AI (
vertex_ai
)

✅

✅

✅

✅

✅

Google AI Studio - Gemini (
gemini
)

✅

✅

✅

GradientAI (
gradient_ai
)

✅

✅

✅

Groq AI (
groq
)

✅

✅

✅

Heroku (
heroku
)

✅

✅

✅

Hosted VLLM (
hosted_vllm
)

✅

✅

✅

Huggingface (
huggingface
)

✅

✅

✅

✅

✅

Hyperbolic (
hyperbolic
)

✅

✅

✅

IBM - Watsonx.ai (
watsonx
)

✅

✅

✅

✅

Infinity (
infinity
)

✅

Jina AI (
jina_ai
)

✅

Lambda AI (
lambda_ai
)

✅

✅

✅

Lemonade (
lemonade
)

✅

✅

✅

LiteLLM Proxy (
litellm_proxy
)

✅

✅

✅

✅

✅

Llamafile (
llamafile
)

✅

✅

✅

LM Studio (
lm_studio
)

✅

✅

✅

Maritalk (
maritalk
)

✅

✅

✅

Meta - Llama API (
meta_llama
)

✅

✅

✅

Mistral AI API (
mistral
)

✅

✅

✅

✅

Moonshot (
moonshot
)

✅

✅

✅

Morph (
morph
)

✅

✅

✅

Nebius AI Studio (
nebius
)

✅

✅

✅

✅

NLP Cloud (
nlp_cloud
)

✅

✅

✅

Novita AI (
novita
)

✅

✅

✅

Nscale (
nscale
)

✅

✅

✅

Nvidia NIM (
nvidia_nim
)

✅

✅

✅

OCI (
oci
)

✅

✅

✅

Ollama (
ollama
)

✅

✅

✅

✅

Ollama Chat (
ollama_chat
)

✅

✅

✅

Oobabooga (
oobabooga
)

✅

✅

✅

✅

✅

✅

✅

OpenAI (
openai
)

✅

✅

✅

✅

✅

✅

✅

✅

✅

OpenAI-like (
openai_like
)

✅

OpenRouter (
openrouter
)

✅

✅

✅

OVHCloud AI Endpoints (
ovhcloud
)

✅

✅

✅

Perplexity AI (
perplexity
)

✅

✅

✅

Petals (
petals
)

✅

✅

✅

Predibase (
predibase
)

✅

✅

✅

Recraft (
recraft
)

✅

Replicate (
replicate
)

✅

✅

✅

Sagemaker Chat (
sagemaker_chat
)

✅

✅

✅

Sambanova (
sambanova
)

✅

✅

✅

Snowflake (
snowflake
)

✅

✅

✅

Text Completion Codestral (
text-completion-codestral
)

✅

✅

✅

Text Completion OpenAI (
text-completion-openai
)

✅

✅

✅

✅

✅

✅

✅

Together AI (
together_ai
)

✅

✅

✅

Topaz (
topaz
)

✅

✅

✅

Triton (
triton
)

✅

✅

✅

V0 (
v0
)

✅

✅

✅

Vercel AI Gateway (
vercel_ai_gateway
)

✅

✅

✅

VLLM (
vllm
)

✅

✅

✅

Volcengine (
volcengine
)

✅

✅

✅

Voyage AI (
voyage
)

✅

WandB Inference (
wandb
)

✅

✅

✅

Watsonx Text (
watsonx_text
)

✅

✅

✅

xAI (
xai
)

✅

✅

✅

Xinference (
xinference
)

✅

Read the Docs

## Run in Developer mode

### Services

1. Setup .env file in root
2. Run dependant servicesdocker-compose up db prometheus

### Backend

1. (In root) create virtual environmentpython -m venv .venv
2. Activate virtual environmentsource .venv/bin/activate
3. Install dependenciespip install -e ".[all]"
4. pip install prisma
5. prisma generate
6. Start proxy backendpython litellm/proxy/proxy_cli.py

### Frontend

1. Navigate toui/litellm-dashboard
2. Install dependenciesnpm install
3. Runnpm run devto start the dashboard

# Enterprise

For companies that need better security, user management and professional support

Talk to founders

This covers:

* ✅Features under theLiteLLM Commercial License:
* ✅Feature Prioritization
* ✅Custom Integrations
* ✅Professional Support - Dedicated discord + slack
* ✅Custom SLAs
* ✅Secure access with Single Sign-On

# Contributing

We welcome contributions to LiteLLM! Whether you're fixing bugs, adding features, or improving documentation, we appreciate your help.

## Quick Start for Contributors

This requires poetry to be installed.

git clone https://github.com/BerriAI/litellm.git

cd
 litellm
make install-dev 
#
 Install development dependencies

make format 
#
 Format your code

make lint 
#
 Run all linting checks

make test-unit 
#
 Run unit tests

make format-check 
#
 Check formatting only

For detailed contributing guidelines, seeCONTRIBUTING.md.

## Code Quality / Linting

LiteLLM follows theGoogle Python Style Guide.

Our automated checks include:

* Blackfor code formatting
* Rufffor linting and code quality
* MyPyfor type checking
* Circular import detection
* Import safety checks

All these checks must pass before your PR can be merged.

# Support / talk with founders

* Schedule Demo 👋
* Community Discord 💭
* Community Slack 💭
* Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
* Our emails ✉️ishaan@berri.ai/krrish@berri.ai

# Why did we build this

* Need for simplicity: Our code started to get extremely complicated managing & translating calls between Azure, OpenAI and Cohere.

# Contributors

## About

Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM]

docs.litellm.ai/docs/

### Topics

 gateway

 bedrock

 openai

 vertex-ai

 azure-openai

 llm

 langchain

 llmops

 anthropic

 openai-proxy

 litellm

 ai-gateway

 llm-gateway

 mcp-gateway

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

40.4k

 stars
 

### Watchers

173

 watching
 

### Forks

6.7k

 forks
 

 Report repository

 

## Releases1,289

v1.82.3-stable.patch.2

 Latest

 

Mar 24, 2026

 

+ 1,288 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://buy.stripe.com/9AQ03Kd3P91o0Q8bIS

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by19.3k

 + 19,242
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python82.5%
* TypeScript15.7%
* HTML1.3%
* JavaScript0.4%
* Shell0.1%
* Makefile0.0%