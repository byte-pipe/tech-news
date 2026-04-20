---
title: 'GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub'
url: https://github.com/openai/openai-agents-python
site_name: github
content_file: github-github-openaiopenai-agents-python-a-lightweight-po
fetched_at: '2026-04-16T11:58:46.426304'
original_url: https://github.com/openai/openai-agents-python
author: openai
description: A lightweight, powerful framework for multi-agent workflows - openai/openai-agents-python
---

openai



/

openai-agents-python

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.4k
* Star20.9k




 
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

1,338 Commits
1,338 Commits
.agents/
skills
.agents/
skills
 
 
.codex
.codex
 
 
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
examples
examples
 
 
src/
agents
src/
agents
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
PLANS.md
PLANS.md
 
 
README.md
README.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# OpenAI Agents SDK

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses and Chat Completions APIs, as well as 100+ other LLMs.

Note

Looking for the JavaScript/TypeScript version? Check outAgents SDK JS/TS.

### Core concepts:

1. Agents: LLMs configured with instructions, tools, guardrails, and handoffs
2. Sandbox Agents: Agents preconfigured to work with a container to perform work over long time horizons.
3. Agents as tools/Handoffs: Delegating to other agents for specific tasks
4. Tools: Various Tools let agents take actions (functions, MCP, hosted tools)
5. Guardrails: Configurable safety checks for input and output validation
6. Human in the loop: Built-in mechanisms for involving humans across agent runs
7. Sessions: Automatic conversation history management across agent runs
8. Tracing: Built-in tracking of agent runs, allowing you to view, debug and optimize your workflows
9. Realtime Agents: Build powerful voice agents withgpt-realtime-1.5and full agent features

Explore theexamplesdirectory to see the SDK in action, and read ourdocumentationfor more details.

## Get started

To get started, set up your Python environment (Python 3.10 or newer required), and then install OpenAI Agents SDK package.

### venv

python -m venv .venv

source
 .venv/bin/activate
#
 On Windows: .venv\Scripts\activate

pip install openai-agents

For voice support, install with the optionalvoicegroup:pip install 'openai-agents[voice]'. For Redis session support, install with the optionalredisgroup:pip install 'openai-agents[redis]'.

### uv

If you're familiar withuv, installing the package would be even easier:

uv init
uv add openai-agents

For voice support, install with the optionalvoicegroup:uv add 'openai-agents[voice]'. For Redis session support, install with the optionalredisgroup:uv add 'openai-agents[redis]'.

## Run your first Sandbox Agent

Sandbox Agentsare new in version 0.14.0. A sandbox agent is an agent that uses a computer environment to perform real work with a filesystem, in an environment you configure and control. Sandbox agents are useful when the agent needs to inspect files, run commands, apply patches, or carry workspace state across longer tasks.

from

agents

import

Runner

from

agents
.
run

import

RunConfig

from

agents
.
sandbox

import

Manifest
,
SandboxAgent
,
SandboxRunConfig

from

agents
.
sandbox
.
entries

import

GitRepo

from

agents
.
sandbox
.
sandboxes

import

UnixLocalSandboxClient

agent

=

SandboxAgent
(

name
=
"Workspace Assistant"
,

instructions
=
"Inspect the sandbox workspace before answering."
,

default_manifest
=
Manifest
(

entries
=
{

"repo"
:
GitRepo
(
repo
=
"openai/openai-agents-python"
,
ref
=
"main"
),
 }
 ),
)

result

=

Runner
.
run_sync
(

agent
,

"Inspect the repo README and summarize what this project does."
,

# Run this agent on the local filesystem


run_config
=
RunConfig
(
sandbox
=
SandboxRunConfig
(
client
=
UnixLocalSandboxClient
())),
)

print
(
result
.
final_output
)

# This project provides a Python SDK for building multi-agent workflows.

(If running this, ensure you set theOPENAI_API_KEYenvironment variable)

(For Jupyter notebook users, seehello_world_jupyter.ipynb)

Explore theexamplesdirectory to see the SDK in action, and read ourdocumentationfor more details.

## Acknowledgements

We'd like to acknowledge the excellent work of the open-source community, especially:

* Pydantic
* Requests
* MCP Python SDK
* Griffe

This library has these optional dependencies:

* websockets
* SQLAlchemy
* any-llmandLiteLLM

We also rely on the following tools to manage the project:

* uvandruff
* mypyandPyright
* pytestandCoverage.py
* MkDocs

We're committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.

## About

A lightweight, powerful framework for multi-agent workflows

openai.github.io/openai-agents-python/

### Topics

 python

 framework

 ai

 openai

 agents

 llm

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

20.9k

 stars


### Watchers

191

 watching


### Forks

3.4k

 forks


 Report repository



## Releases83

v0.14.1

 Latest



Apr 15, 2026



+ 82 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python99.7%
* Other0.3%
