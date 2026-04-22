---
title: 'GitHub - langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 · GitHub'
url: https://github.com/langfuse/langfuse
site_name: github
content_file: github-github-langfuselangfuse-open-source-llm-engineerin
fetched_at: '2026-04-22T20:04:26.646330'
original_url: https://github.com/langfuse/langfuse
author: langfuse
description: '🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 - GitHub - langfuse/langfuse: 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23'
---

langfuse

 

/

langfuse

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.6k
* Star25.5k

 
 
 
 
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

6,857 Commits
6,857 Commits
.agents
.agents
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
ee
ee
 
 
fern
fern
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
specs
specs
 
 
web
web
 
 
worker
worker
 
 
.codespellrc
.codespellrc
 
 
.dockerignore
.dockerignore
 
 
.env.dev-azure.example
.env.dev-azure.example
 
 
.env.dev-oci.example
.env.dev-oci.example
 
 
.env.dev-redis-cluster.example
.env.dev-redis-cluster.example
 
 
.env.dev.example
.env.dev.example
 
 
.env.prod.example
.env.prod.example
 
 
.env.test.example
.env.test.example
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.cn.md
README.cn.md
 
 
README.ja.md
README.ja.md
 
 
README.kr.md
README.kr.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.build.yml
docker-compose.build.yml
 
 
docker-compose.dev-azure.yml
docker-compose.dev-azure.yml
 
 
docker-compose.dev-redis-cluster.yml
docker-compose.dev-redis-cluster.yml
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
prettier.config.cjs
prettier.config.cjs
 
 
turbo.json
turbo.json
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
View all files

## Repository files navigation

### Langfuse Is Doubling Down On Open SourceLangfuse Cloud·Self Host·Demo

Docs
 ·
 
Report Bug
 ·
 
Feature Request
 ·
 
Changelog
 ·
 
Roadmap
 ·
 

Langfuse uses 
GitHub Discussions
 for Support and Feature Requests.

We're hiring.
 
Join us
 in product engineering and technical go-to-market roles.

Proudly made with ClickHouse open source database

Langfuse is anopen source LLM engineeringplatform. It helps teams collaborativelydevelop, monitor, evaluate,anddebugAI applications. Langfuse can beself-hosted in minutesand isbattle-tested.

## ✨ Core Features

* LLM Application Observability: Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions. Try the interactivedemoto see this in action.
* Prompt Managementhelps you centrally manage, version control, and collaboratively iterate on your prompts. Thanks to strong caching on server and client side, you can iterate on prompts without adding latency to your application.
* Evaluationsare key to the LLM application development workflow, and Langfuse adapts to your needs. It supports LLM-as-a-judge, user feedback collection, manual labeling, and custom evaluation pipelines via APIs/SDKs.
* Datasetsenable test sets and benchmarks for evaluating your LLM application. They support continuous improvement, pre-deployment testing, structured experiments, flexible evaluation, and seamless integration with frameworks like LangChain and LlamaIndex.
* LLM Playgroundis a tool for testing and iterating on your prompts and model configurations, shortening the feedback loop and accelerating development. When you see a bad result in tracing, you can directly jump to the playground to iterate on it.
* Comprehensive API: Langfuse is frequently used to power bespoke LLMOps workflows while using the building blocks provided by Langfuse via the API. OpenAPI spec, Postman collection, and typed SDKs for Python, JS/TS are available.

## 📦 Deploy Langfuse

### Langfuse Cloud

Managed deployment by the Langfuse team, generous free-tier, no credit card required.

### Self-Host Langfuse

Run Langfuse on your own infrastructure:

* Local (docker compose): Run Langfuse on your own machine in 5 minutes using Docker Compose.#Get a copy of the latest Langfuse repositorygit clone https://github.com/langfuse/langfuse.gitcdlangfuse#Run the langfuse docker composedocker compose up
* VM: Run Langfuse on a single Virtual Machine using Docker Compose.
* Kubernetes (Helm): Run Langfuse on a Kubernetes cluster using Helm. This is the preferred production deployment.
* Terraform Templates:AWS,Azure,GCP

Seeself-hosting documentationto learn more about architecture and configuration options.

## 🔌 Integrations

### Main Integrations:

Integration

Supports

Description

SDK

Python, JS/TS

Manual instrumentation using the SDKs for full flexibility.

OpenAI

Python, JS/TS

Automated instrumentation using drop-in replacement of OpenAI SDK.

Langchain

Python, JS/TS

Automated instrumentation by passing callback handler to Langchain application.

LlamaIndex

Python

Automated instrumentation via LlamaIndex callback system.

Haystack

Python

Automated instrumentation via Haystack content tracing system.

LiteLLM

Python, JS/TS (proxy only)

Use any LLM as a drop in replacement for GPT. Use Azure, OpenAI, Cohere, Anthropic, Ollama, VLLM, Sagemaker, HuggingFace, Replicate (100+ LLMs).

Vercel AI SDK

JS/TS

TypeScript toolkit designed to help developers build AI-powered applications with React, Next.js, Vue, Svelte, Node.js.

Mastra

JS/TS

Open source framework for building AI agents and multi-agent systems.

API

Directly call the public API. OpenAPI spec available.

### Packages integrated with Langfuse:

Name

Type

Description

Instructor

Library

Library to get structured LLM outputs (JSON, Pydantic)

DSPy

Library

Framework that systematically optimizes language model prompts and weights

Mirascope

Library

Python toolkit for building LLM applications.

Ollama

Model (local)

Easily run open source LLMs on your own machine.

Amazon Bedrock

Model

Run foundation and fine-tuned models on AWS.

AutoGen

Agent Framework

Open source LLM platform for building distributed agents.

Flowise

Chat/Agent UI

JS/TS no-code builder for customized LLM flows.

Langflow

Chat/Agent UI

Python-based UI for LangChain, designed with react-flow to provide an effortless way to experiment and prototype flows.

Dify

Chat/Agent UI

Open source LLM app development platform with no-code builder.

OpenWebUI

Chat/Agent UI

Self-hosted LLM Chat web ui supporting various LLM runners including self-hosted and local models.

Promptfoo

Tool

Open source LLM testing platform.

LobeChat

Chat/Agent UI

Open source chatbot platform.

Vapi

Platform

Open source voice AI platform.

Inferable

Agents

Open source LLM platform for building distributed agents.

Gradio

Chat/Agent UI

Open source Python library to build web interfaces like Chat UI.

Goose

Agents

Open source LLM platform for building distributed agents.

smolagents

Agents

Open source AI agents framework.

CrewAI

Agents

Multi agent framework for agent collaboration and tool use.

## 🚀 Quickstart

Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls and other relevant logic in your app such as retrieval, embedding, or agent actions. Inspect and debug complex logs and user sessions.

### 1️⃣ Create new project

1. Create Langfuse accountorself-host
2. Create a new project
3. Create new API credentials in the project settings

### 2️⃣ Log your first LLM call

The@observe()decoratormakes it easy to trace any Python LLM application. In this quickstart we also use the LangfuseOpenAI integrationto automatically capture all model parameters.

Tip

Not using OpenAI? Visitour documentationto learn how to log other models and frameworks.

pip install langfuse openai

LANGFUSE_SECRET_KEY=
"
sk-lf-...
"

LANGFUSE_PUBLIC_KEY=
"
pk-lf-...
"

LANGFUSE_BASE_URL=
"
https://cloud.langfuse.com
"
 
#
 🇪🇺 EU region

#
 LANGFUSE_BASE_URL="https://us.cloud.langfuse.com" # 🇺🇸 US region

from
 
langfuse
 
import
 
observe

from
 
langfuse
.
openai
 
import
 
openai
 
# OpenAI integration

@
observe
()

def
 
story
():
 
return
 
openai
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
"What is Langfuse?"
}],
 ).
choices
[
0
].
message
.
content

@
observe
()

def
 
main
():
 
return
 
story
()

main
()

### 3️⃣ See traces in Langfuse

See your language model calls and other application logic in Langfuse.

Public example trace in Langfuse

Tip

Learn moreabout tracing in Langfuse or play with theinteractive demo.

## ⭐️ Star Us

## 💭 Support

Finding an answer to your question:

* Ourdocumentationis the best place to start looking for answers. It is comprehensive, and we invest significant time into maintaining it. You can also suggest edits to the docs via GitHub.
* Langfuse FAQswhere the most common questions are answered.
* Use "Ask AI" to get instant answers to your questions.

Support Channels:

* Ask any question in ourpublic Q&Aon GitHub Discussions.Please include as much detail as possible (e.g. code snippets, screenshots, background information) to help us understand your question.
* Request a featureon GitHub Discussions.
* Report a Bugon GitHub Issues.
* For time-sensitive queries, ping us via the in-app chat widget.

## 🤝 Contributing

Your contributions are welcome!

* Vote onIdeasin GitHub Discussions.
* Raise and comment onIssues.
* Open a PR - seeCONTRIBUTING.mdfor details on how to setup a development environment.

## 🥇 License

This repository is MIT licensed, except for theeefolders. SeeLICENSEanddocsfor more details.

## Dependencies

We deploy this code base in Docker containers based on the Linux Alpine Image (source). You may find the Dockerfiles inweb/Dockerfileandworker/Dockerfile.

## ⭐️ Star History

## ❤️ Open Source Projects Using Langfuse

Top open-source Python projects that use Langfuse, ranked by stars (Source):

Repository

Stars

   
langflow-ai
 / 
langflow

116251

   
open-webui
 / 
open-webui

109642

   
abi
 / 
screenshot-to-code

70877

   
lobehub
 / 
lobe-chat

65454

   
infiniflow
 / 
ragflow

64118

   
firecrawl
 / 
firecrawl

56713

   
run-llama
 / 
llama_index

44203

   
FlowiseAI
 / 
Flowise

43547

   
QuivrHQ
 / 
quivr

38415

   
microsoft
 / 
ai-agents-for-beginners

38012

   
chatchat-space
 / 
Langchain-Chatchat

36071

   
mindsdb
 / 
mindsdb

35669

   
danny-avila
 / 
LibreChat

33142

   
BerriAI
 / 
litellm

28726

   
onlook-dev
 / 
onlook

22447

   
NixOS
 / 
nixpkgs

21748

   
kortix-ai
 / 
suna

17976

   
anthropics
 / 
courses

17057

   
mastra-ai
 / 
mastra

16484

   
langfuse
 / 
langfuse

16054

   
Canner
 / 
WrenAI

11868

   
promptfoo
 / 
promptfoo

8350

   
The-Pocket
 / 
PocketFlow

8313

   
OpenPipe
 / 
ART

7093

   
topoteretes
 / 
cognee

7011

   
awslabs
 / 
agent-squad

6785

   
BasedHardware
 / 
omi

6231

   
hatchet-dev
 / 
hatchet

6019

   
zenml-io
 / 
zenml

4873

   
refly-ai
 / 
refly

4654

   
coleam00
 / 
ottomator-agents

4165

   
JoshuaC215
 / 
agent-service-toolkit

3557

   
colanode
 / 
colanode

3517

   
VoltAgent
 / 
voltagent

3210

   
bragai
 / 
bRAG-langchain

3010

   
pingcap
 / 
autoflow

2651

   
sourcebot-dev
 / 
sourcebot

2570

   
open-webui
 / 
pipelines

2055

   
YFGaia
 / 
dify-plus

1734

   
TheSpaghettiDetective
 / 
obico-server

1687

   
MLSysOps
 / 
MLE-agent

1387

   
TIGER-AI-Lab
 / 
TheoremExplainAgent

1385

   
trailofbits
 / 
buttercup

1223

   
wassim249
 / 
fastapi-langgraph-agent-production-ready-template

1200

   
alishobeiri
 / 
thread

1098

   
dmayboroda
 / 
minima

1010

   
zstar1003
 / 
ragflow-plus

993

   
openops-cloud
 / 
openops

939

   
dynamiq-ai
 / 
dynamiq

927

   
xataio
 / 
agent

857

   
plastic-labs
 / 
tutor-gpt

845

   
trendy-design
 / 
llmchat

829

   
hotovo
 / 
aider-desk

781

   
opslane
 / 
opslane

719

   
wrtnlabs
 / 
autoview

688

   
andysingal
 / 
llm-course

643

   
theopenconversationkit
 / 
tock

587

   
sentient-engineering
 / 
agent-q

487

   
NicholasGoh
 / 
fastapi-mcp-langgraph-template

481

   
i-am-alice
 / 
3rd-devs

472

   
AIDotNet
 / 
koala-ai

470

   
phospho-app
 / 
text-analytics-legacy

439

   
inferablehq
 / 
inferable

403

   
duoyang666
 / 
ai_novel

397

   
strands-agents
 / 
samples

385

   
FranciscoMoretti
 / 
sparka

380

   
RobotecAI
 / 
rai

373

   
ElectricCodeGuy
 / 
SupabaseAuthWithSSR

370

   
souzatharsis
 / 
tamingLLMs

323

   
aws-samples
 / 
aws-ai-ml-workshop-kr

295

   
weizxfree
 / 
KnowFlow

285

   
zenml-io
 / 
zenml-projects

276

   
wxai-space
 / 
LightAgent

275

   
Ozamatash
 / 
deep-research-mcp

269

   
sql-agi
 / 
DB-GPT

241

   
guyernest
 / 
advanced-rag

238

   
bklieger-groq
 / 
mathtutor-on-groq

233

   
plastic-labs
 / 
honcho

224

   
OVINC-CN
 / 
OpenWebUI

202

   
zhutoutoutousan
 / 
worldquant-miner

202

   
iceener
 / 
ai

186

   
giselles-ai
 / 
giselle

181

   
ai-shifu
 / 
ai-shifu

181

   
aws-samples
 / 
sample-serverless-mcp-servers

175

   
celerforge
 / 
freenote

171

   
babelcloud
 / 
LLM-RGB

164

   
8090-inc
 / 
xrx-sample-apps

163

   
deepset-ai
 / 
haystack-core-integrations

163

   
codecentric
 / 
c4-genai-suite

152

   
XSpoonAi
 / 
spoon-core

150

   
chatchat-space
 / 
LangGraph-Chatchat

144

   
langfuse
 / 
langfuse-docs

139

   
piyushgarg-dev
 / 
genai-cohort

135

   
i-dot-ai
 / 
redbox

132

   
bmd1905
 / 
ChatOpsLLM

127

   
Fintech-Dreamer
 / 
FinSynth

121

   
kenshiro-o
 / 
nagato-ai

119

## 🔒 Security & Privacy

We take data security and privacy seriously. Please refer to ourSecurity and Privacypage for more information.

### Telemetry

By default, Langfuse automatically reports basic usage statistics of self-hosted instances to a centralized server (PostHog).

This helps us to:

1. Understand how Langfuse is used and improve the most relevant features.
2. Track overall usage for internal and external (e.g. fundraising) reporting.

The telemetry does not include raw traces, prompts, observations, scores, or dataset contents. We document the exact fields that are collected, where they are sent, and the implementation reference in ourtelemetry docs.

For Langfuse OSS, you can opt out by settingTELEMETRY_ENABLED=false.

## About

🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23

langfuse.com/docs

### Topics

 open-source

 playground

 monitoring

 analytics

 evaluation

 self-hosted

 ycombinator

 openai

 observability

 autogen

 large-language-models

 llm

 prompt-engineering

 langchain

 llmops

 llama-index

 prompt-management

 llm-evaluation

 llm-observability

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

25.5k

 stars
 

### Watchers

88

 watching
 

### Forks

2.6k

 forks
 

 Report repository

 

## Releases555

v3.169.0

 Latest

 

Apr 17, 2026

 

+ 554 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors165

+ 151 contributors

## Languages

* TypeScript98.8%
* Other1.2%