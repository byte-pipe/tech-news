---
title: 'GitHub - alexzhang13/rlm: General plug-and-play inference library for Recursive Language Models (RLMs), supporting various sandboxes. · GitHub'
url: https://github.com/alexzhang13/rlm
site_name: github
content_file: github-github-alexzhang13rlm-general-plug-and-play-infere
fetched_at: '2026-06-17T19:45:28.599679'
original_url: https://github.com/alexzhang13/rlm
author: alexzhang13
description: General plug-and-play inference library for Recursive Language Models (RLMs), supporting various sandboxes. - alexzhang13/rlm
---

alexzhang13

 

/

rlm

Public

* NotificationsYou must be signed in to change notification settings
* Fork820
* Star4.9k

 
 
 
 
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

135 Commits
135 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
examples
examples
 
 
media
media
 
 
rlm
rlm
 
 
tests
tests
 
 
training
training
 
 
visualizer
visualizer
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.IN
MANIFEST.IN
 
 
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

# Recursive Language Models (RLMs)

Full Paper•Blogpost•Documentation•RLM Minimal

## Overview

Recursive Language Models (RLMs) are a task-agnostic inference paradigm for language models (LMs) to handle near-infinite length contexts by enabling the LM toprogrammaticallyexamine, decompose, and recursively call itself over its input. RLMs replace the canonicalllm.completion(prompt, model)call with arlm.completion(prompt, model)call, acting as a "language model". RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of.

RLMs are a bet on future "language model" design choices. We argue for aCodeAct-style harness (i.e. all language models should have access to a code environment) with sub-(R)LM calls as functions in code, and context / prompts as objects in code. RLMs explicitly defer code execution with sub-calls as functions to the language model itself, which is incredibly flexible and lends itself well to scale if trained correctly. We want to move away from the JSON tool-calling standard for both sub-agents and generic tool calls. The naming comes from the fact that such a system is itself a "language model" (a probabilistic mapping from text to text) that builds around and relies on recursive sub-LLM calls.

This repository provides both an extensible inference engine and training environment for using RLMs around standard API-based and local LLMs. The initial experiments and idea were proposed in ablogpostin 2025, with expanded results in anarXiv preprint.

We now also include averifierstraining environment based on Prime Intellect'sprime-rlin thetraining/folder. Train your own RLMs, which directly can be plugged into our inference engine!

Note

This repository contains inference code for RLMs with support for various sandbox environments. Open-source contributions are welcome. This repository is maintained by the authors of the paper from the MIT OASYS lab.

## Quick Setup

Note

rlmsrequiresPython 3.11 or later.

You can try out RLMs quickly by installing from PyPi:

pip install rlms

The default RLM client uses a REPL environment that runs on the host process through Pythonexeccalls. It uses the same virtual environment as the host process (i.e. it will have access to the same dependencies), but with some limitations in its available global modules. As an example, we can call RLM completions using GPT-5-nano:

from
 
rlm
 
import
 
RLM

rlm
 
=
 
RLM
(
 
backend
=
"openai"
,
 
backend_kwargs
=
{
"model_name"
: 
"gpt-5-nano"
},
 
verbose
=
True
, 
# For printing to console with rich, disabled by default.

)

print
(
rlm
.
completion
(
"Print me the first 100 powers of two, each on a newline."
).
response
)

Manual Setup

Set up the dependencies withuv(or your virtual environment of choice):

curl -LsSf https://astral.sh/uv/install.sh 
|
 sh
uv init 
&&
 uv venv --python 3.12 
#
 change version as needed

uv pip install -e 
.

This project includes aMakefileto simplify common tasks.

* make install: Install base dependencies.
* make check: Run linter, formatter, and tests.

To run a quick test, the following will run an RLM query with the OpenAI client using your environment variableOPENAI_API_KEY(feel free to change this). This will generate console output as well as a log which you can use with the visualizer to explore the trajectories.

make quickstart

## REPL Environments

We support two types of REPL environments -- isolated, and non-isolated. Non-isolated environments (default) run code execution on the same machine as the RLM (e.g. throughexec), which is pretty reasonable for some local low-risk tasks, like simple benchmarking, but can be problematic if the prompts or tool calls can interact with malicious users. Fully isolated environments use cloud-based sandboxes (e.g. Prime Sandboxes,Modal Sandboxes) to run code generated by the RLM, ensuring complete isolation from the host process. Environments can be added, but we natively support the following:local(default),ipython,docker,modal,prime,daytona,e2b.

rlm
 
=
 
RLM
(
 
environment
=
"..."
, 
# "local", "ipython", "docker", "modal", "prime", "daytona", "e2b"

 
environment_kwargs
=
{...},
)

### Local Environments

The defaultlocalenvironmentLocalREPLruns in the same process as the RLM itself, with specified global and local namespaces for minimal security. Using this REPL is generally safe, but should not be used for production settings. It also shares the same virtual environment (e.g. Conda or uv) as the host process.

#### IPython (requirespip install 'rlms[ipython]')

IPythonREPLruns cells inside a real IPython session — either in-process (default) or in a separateipykernelsubprocess. Subprocess mode adds hardcell_timeoutenforcement and full namespace isolation from the RLM host. See theIPythonREPL docsfor details.

#### Docker(requiresDocker installed)

We also support a Docker-based environment calledDockerREPLthat launches the REPL environment as a Docker image. By default, we use thepython:3.11-slimimage, but the user can specify custom images as well.

### Isolated Environments

We support several different REPL environments that run on separate, cloud-based machines. Whenever a recursive sub-call is made in these instances, it is requested from the host process.

#### Modal Sandboxes

To useModal Sandboxesas the REPL environment, you need to install and authenticate your Modal account.

uv add modal 
#
 add modal library

modal setup 
#
 authenticate account

#### Prime Intellect Sandboxes

Note

Prime Intellect Sandboxesare currently a beta feature. See thedocumentationfor more information. We noticed slow runtimes when using these sandboxes, which is currently an open issue.

To usePrime Sandboxes, install the SDK and set your API key:

uv pip install -e 
"
.[prime]
"

export
 PRIME_API_KEY=...

### Model Providers

We currently support most major clients (OpenAI, Anthropic), as well as the router platforms (OpenRouter, Portkey). For local models, we recommend using vLLM (which interfaces with theOpenAI client). To view or add support for more clients, start by looking atrlm/clients/.

## Training

We provide a simple RL training harness for training RLMs used in this repo (specifically thelocalREPL). The implementation uses no sandboxes for simplicity and slots easily your use case, but an ideal setup would use sandboxes for safety. Training logic is isolated to thetraining/folder, which exposesrlm.RLMas averifiersEnvironmentand plugs straight intoprime-rl. See thetraining READMEfor the launch command. The harness uses subprocess-isolated local REPL execution (no cloud sandboxes), matching thelocalenvironment above.

A worked example with an example.tomllives intraining/environments/oolong/(OOLONG long-context QA). New training environments can be added the same way — author averifiersenv that wraps your task (see theverifiers docs), then reference it from a config.

## Relevant Reading

* [Dec '25]Recursive Language Models arXiv
* [Oct '25]Recursive Language Models Blogpost

If you use this code or repository in your research, please cite:

@misc
{
zhang2026recursivelanguagemodels
,
 
title
=
{
Recursive Language Models
}
,
 
author
=
{
Alex L. Zhang and Tim Kraska and Omar Khattab
}
,
 
year
=
{
2026
}
,
 
eprint
=
{
2512.24601
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.AI
}
,
 
url
=
{
https://arxiv.org/abs/2512.24601
}
,
}

## RLMs in the Wild

There are many amazing demos and production-ready use cases of RLMs. We provide a list of notable examples that explicitly use RLMs as a central piece of their design.

* DSPy.RLM
* Ax
* context-labs/HALO:RLM-based Automatic Agent Optimization Loop
* viplismism/rlm-cli:CLI for Recursive Language Models
* alphaXiv Official Blog.Reinforcing Recursive Language Models
* Daytona.Building Deep Recursive Language Models
* Symbolica.SotA ARC-AGI-2 Results with REPL Agents
* Google Cloud Community Articles.RLMs in ADK
* Prime Intellect Blog.Recursive Language Models:theparadigm of 2026

## Optional: Trajectory metadata, logging, and debugging

RLMChatCompletionhas an optionalmetadatafield (defaultNone) that holds the full trajectory (run config + all iterations and sub-calls) so you can reconstruct the run. Pass anRLMLoggerto capture it:

* In-memory only(trajectory oncompletion.metadata):logger=RLMLogger()(nolog_dir).
* Also save to disk(JSONL for the visualizer):logger=RLMLogger(log_dir="./logs").

Visualizing logs.We also provide a simple visualizer to inspect code, sub-LM, and root-LM calls. UseRLMLogger(log_dir="./logs")so each completion writes a.jsonlfile:

from
 
rlm
.
logger
 
import
 
RLMLogger

from
 
rlm
 
import
 
RLM

logger
 
=
 
RLMLogger
(
log_dir
=
"./logs"
)

rlm
 
=
 
RLM
(..., 
logger
=
logger
)

To run the visualizer locally, we use Node.js and shadcn/ui:

cd visualizer/
npm run dev # default localhost:3001

## About

General plug-and-play inference library for Recursive Language Models (RLMs), supporting various sandboxes.

arxiv.org/abs/2512.24601

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.9k

 stars
 

### Watchers

49

 watching
 

### Forks

820

 forks
 

 Report repository

 

## Releases5

Change final answer function, add iPython support

 Latest

 

May 28, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.7%
* Makefile0.3%