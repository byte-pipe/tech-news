---
title: 'GitHub - huggingface/OpenEnv: An interface library for RL post training with environments. · GitHub'
url: https://github.com/huggingface/OpenEnv
site_name: github
content_file: github-github-huggingfaceopenenv-an-interface-library-for
fetched_at: '2026-06-13T11:39:51.888779'
original_url: https://github.com/huggingface/OpenEnv
author: huggingface
description: 'An interface library for RL post training with environments. - GitHub - huggingface/OpenEnv: An interface library for RL post training with environments.'
---

huggingface

 

/

OpenEnv

Public

* NotificationsYou must be signed in to change notification settings
* Fork391
* Star2.1k

 
 
 
 
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

1,532 Commits
1,532 Commits
.agents/
skills
.agents/
skills
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.github
.github
 
 
docs
docs
 
 
envs
envs
 
 
examples
examples
 
 
rfcs
rfcs
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tutorial
tutorial
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitkeep
.gitkeep
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# OpenEnv: Agentic Execution Environments

An e2e framework for creating, deploying and using isolated execution environments for agentic RL training, built using Gymnasium style simple APIs.

Featured Example:Train LLMs to play BlackJack usingtorchforge(PyTorch's agentic RL framework):examples/grpo_blackjack/

Zero to Hero Tutorial:End to end tutorial from ourGPU Modelecture and other hackathons.

## Quick Start

Install the OpenEnv package:

pip install openenv

Install an environment client (e.g., Echo):

pip install git+https://huggingface.co/spaces/openenv/echo_env

Then use the environment:

import
 
asyncio

from
 
echo_env
 
import
 
CallToolAction
, 
EchoEnv

async
 
def
 
main
():
 
# Connect to a running Space (async context manager)

 
async
 
with
 
EchoEnv
(
base_url
=
"https://openenv-echo-env.hf.space"
) 
as
 
client
:
 
# Reset the environment

 
result
 
=
 
await
 
client
.
reset
()
 
print
(
result
.
observation
.
echoed_message
) 
# "Echo environment ready!"

 
# Send messages

 
result
 
=
 
await
 
client
.
step
(
 
CallToolAction
(
 
tool_name
=
"echo_message"
,
 
arguments
=
{
"message"
: 
"Hello, World!"
},
 )
 )
 
print
(
result
.
observation
.
result
) 
# "Hello, World!"

 
print
(
result
.
reward
)

asyncio
.
run
(
main
())

Synchronous usageis also supported via the.sync()wrapper:

from
 
echo_env
 
import
 
CallToolAction
, 
EchoEnv

# Use .sync() for synchronous context manager

with
 
EchoEnv
(
base_url
=
"https://openenv-echo-env.hf.space"
).
sync
() 
as
 
client
:
 
result
 
=
 
client
.
reset
()
 
result
 
=
 
client
.
step
(
 
CallToolAction
(
 
tool_name
=
"echo_message"
,
 
arguments
=
{
"message"
: 
"Hello, World!"
},
 )
 )
 
print
(
result
.
observation
.
result
)

For a detailed quick start, check out thedocs page.

## Overview

OpenEnv provides a standard for interacting with agentic execution environments via simple Gymnasium style APIs -step(),reset(),state(). Users of agentic execution environments can interact with the environment during RL training loops using these simple APIs.

In addition to making it easier for researchers and RL framework writers, we also provide tools for environment creators making it easier for them to create richer environments and make them available over familiar protocols like HTTP and packaged using canonical technologies like docker. Environment creators can use the OpenEnv framework to create environments that are isolated, secure, and easy to deploy and use.

The OpenEnv CLI (openenv) provides commands to initialize new environments and deploy them to Hugging Face Spaces.

⚠️Early Development WarningOpenEnv is currently in an experimental
stage. You should expect bugs, incomplete features, and APIs that may change
in future versions. The project welcomes bugfixes, but significant changes
should be discussed before implementation so the technical committee and
community can coordinate scope, compatibility, and release timing. It's
recommended that you signal your intention to contribute in the issue tracker,
either by filing a new issue or by claiming an existing one.

### RFCs

Below is a list of active and historical RFCs for OpenEnv. RFCs are proposals for major changes or features. Please review and contribute!

* RFC 001: Baseline API and Interface Specifications
* RFC 002: Discoverability of environment tools by agents
* RFC 003: Add MCP (Model Context Protocol) support
* RFC 004: Add delayed rewards support for trajectory-based scoring
* RFC 005: Agentic Harness Integration

## Architecture

### Component Overview

┌─────────────────────────────────────────────────────────┐
│ Client Application │
│ ┌────────────────┐ ┌──────────────────┐ │
│ │ EchoEnv │ │ CodingEnv │ │
│ │ (EnvClient) │ │ (EnvClient) │ │
│ └────────┬───────┘ └────────┬─────────┘ │
└───────────┼───────────────────────────────┼─────────────┘
 │ WebSocket │ WebSocket
 │ (reset, step, state) │
┌───────────▼───────────────────────────────▼─────────────┐
│ Docker Containers (Isolated) │
│ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │ FastAPI Server │ │ FastAPI Server │ │
│ │ EchoEnvironment │ │ PythonCodeActEnv │ │
│ │ (Environment base) │ │ (Environment base) │ │
│ └──────────────────────┘ └──────────────────────┘ │
└─────────────────────────────────────────────────────────┘

### Core Components

#### 1. Web Interface

OpenEnv includes a built-in web interface for interactive environment exploration and debugging. The web interface provides:

* Two-Pane Layout: HumanAgent interaction on the left, state observation on the right
* Real-time Updates: WebSocket-based live updates without page refresh
* Dynamic Forms: Automatically generated action forms based on environment Action types
* Action History: Complete log of all actions taken and their results

The web interface isconditionally enabledbased on environment variables:

* Local Development: Disabled by default for lightweight development
* Manual Override: Enable withENABLE_WEB_INTERFACE=true

To use the web interface:

from
 
openenv
.
core
.
env_server
 
import
 
create_web_interface_app

from
 
your_env
.
models
 
import
 
YourAction
, 
YourObservation

from
 
your_env
.
server
.
your_environment
 
import
 
YourEnvironment

env
 
=
 
YourEnvironment
()

app
 
=
 
create_web_interface_app
(
env
, 
YourAction
, 
YourObservation
)

When enabled, openhttp://localhost:8000/webin your browser to interact with the environment.

#### 2. Environment (Server-Side)

Base class for implementing environment logic:

* reset(): Initialize a new episode, returns initialObservation
* step(action): Execute anAction, returns resultingObservation
* state(): Access episode metadata (Statewith episode_id, step_count, etc.)

#### 3. EnvClient (Client-Side)

Base class for environment communication:

* Async by default: Useasync withandawaitfor all operations
* Sync wrapper: Call.sync()to get aSyncEnvClientfor synchronous usage
* Handles WebSocket connections to environment server
* Contains a utility to spin up a docker container locally for the corresponding environment
* Type-safe action/observation parsing

#### 4. Container Providers

Manage container deployment:

* LocalDockerProvider: Run containers on local Docker daemon
* DockerSwarmProvider: Deploy to Docker Swarm clusters
* KubernetesProvider: Deploy to Kubernetes clusters
* UVProvider,DaytonaProvider: Additional runtime providers

#### 5. Models

Type-safe data structures:

* Action: Base class for environment actions
* Observation: Base class for environment observations
* State: Episode state tracking
* StepResult: Combines observation, reward, done flag

## Project Structure

### For Environment Creators

Use the CLI to quickly scaffold a new environment:

openenv init my_env

This creates the following structure:

my_env/
├── .dockerignore # Docker build exclusions
├── __init__.py # Export YourAction, YourObservation, YourEnv
├── models.py # Define Action, Observation, State dataclasses
├── client.py # Implement YourEnv(EnvClient)
├── README.md # Document your environment
├── openenv.yaml # Environment manifest
├── pyproject.toml # Dependencies and package configuration
├── outputs/ # Runtime outputs (logs, evals) - gitignored
│ ├── logs/
│ └── evals/
└── server/
 ├── your_environment.py # Implement YourEnvironment(Environment)
 ├── app.py # Create FastAPI app
 ├── requirements.txt # Dependencies for Docker (can be generated)
 └── Dockerfile # Define container image

#### Dependency Management

OpenEnv usespyproject.tomlas the primary dependency specification:

* Environment-levelpyproject.toml: Each environment defines its own dependencies
* Root-levelpyproject.toml: Contains shared core dependencies (fastapi, pydantic, uvicorn)
* Serverrequirements.txt: Can be auto-generated frompyproject.tomlfor Docker builds

Development Workflow:

#
 Install environment in editable mode

cd
 my_env
pip install -e 
.

#
 Or using uv (faster)

uv pip install -e 
.

#
 Run server locally without Docker

uv run server --host 0.0.0.0 --port 8000

Seeenvs/README.mdfor a complete guide on building environments.

### For Environment Users

To use an environment:

1. Install the client:pip install git+https://huggingface.co/spaces/openenv/echo_env
2. Import:from echo_env import CallToolAction, EchoEnv
3. Use async (recommended) or sync API:

Async (recommended):

async
 
with
 
EchoEnv
(
base_url
=
"..."
) 
as
 
client
:
 
result
 
=
 
await
 
client
.
reset
()
 
result
 
=
 
await
 
client
.
step
(
action
)

Sync (via.sync()wrapper):

with
 
EchoEnv
(
base_url
=
"..."
).
sync
() 
as
 
client
:
 
result
 
=
 
client
.
reset
()
 
result
 
=
 
client
.
step
(
action
)

See example scripts inexamples/directory.

## CLI Commands

The OpenEnv CLI provides commands to manage environments:

* openenv init <env_name>- Initialize a new environment from template
* openenv push [--repo-id <repo>] [--private]- Deploy environment to Hugging Face Spaces
* openenv serve- Serve an environment locally with optional auto-reload
* openenv build- Build the Docker image for an environment
* openenv fork <space-id>- Fork a Space from HF Hub to your account
* openenv validate- Validate an environment configuration

### Quick Start

#
 Create a new environment

openenv init my_game_env

#
 Deploy to Hugging Face (will prompt for login if needed)

cd
 my_game_env
openenv push

For detailed options run any command with--help.

## Development

### Installation

#
 Clone the repository

git clone https://github.com/huggingface/OpenEnv.git

cd
 OpenEnv

#
 Install core package in editable mode

pip install -e 
.

#
 Or using uv (faster)

uv pip install -e 
.

### Running Tests

OpenEnv uses a modular dependency structure: the core package is minimal, and each environment has its own dependencies. This means some tests require environment-specific packages.

#
 Install pytest (required for running tests)

uv pip install pytest

#
 Run all tests (skips tests requiring uninstalled dependencies)

PYTHONPATH=src:envs uv run pytest tests/ -v --tb=short

#
 Run a specific test file

PYTHONPATH=src:envs uv run pytest tests/envs/test_echo_environment.py -v

To run environment-specific tests, install that environment's dependencies:

#
 Example: Install coding_env with dev dependencies (includes smolagents + pytest)

uv pip install -e 
"
envs/coding_env[dev]
"

#
 Then run coding_env tests

PYTHONPATH=src:envs uv run pytest tests/envs/test_python_codeact_rewards.py -v

Tests will be automatically skipped if their required dependencies aren't installed.

## Integrations

OpenEnv works with a growing ecosystem of RL frameworks and platforms. If your project supports OpenEnv, open a PR to add it here.

### TRL

See theTRL exampleon how to integrate OpenEnv environments with GRPO training.

### torchforge

See GRPO BlackJack training example:examples/grpo_blackjack/

### Unsloth

See the 2048 game example based on gpt-oss:Colab notebook

### SkyRL

See theSkyRL exampleon how to train on OpenEnv environments with SkyRL.

### ART

See theART exampleon how OpenEnv environments can be used to train models with ART.

### Oumi

See theOumi exampleon how OpenEnv environments can be used to train models with Oumi.

### Lightning AI

Lightning AI templates

## Example Environments

Environment

Description

Echo Environment

Echoes back messages with metadata. Ideal for testing HTTP server infrastructure, learning framework basics, and verifying container deployment.

Coding Environment

Sandboxed Python code execution via smolagents. Captures stdout/stderr/exit codes, supports persistent episode context, and provides detailed error handling.

Chess Environment

Chess RL environment with configurable opponents and full rules support.

Atari Environment

Classic Arcade Learning Environment tasks for RL benchmarking.

FinRL Environment

Financial market simulations for algorithmic trading experiments.

Browse the full catalog of community environments athuggingface.co/docs/openenv/environments.

## Community Support & Acknowledgments

OpenEnv is governed by a technical committee that coordinates project direction, major technical decisions, RFCs, and release planning through the public issue tracker, pull requests, and RFC process. Current committee members: Meta-PyTorch, Reflection, Unsloth, Modal, Prime Intellect, Nvidia, Mercor, Fleet AI, and Hugging Face.

The project is also supported by a broader community of organizations. If you would like to add your project or organization here, please open a pull request for maintainer review.

Supporters include:Meta-PyTorch,Hugging Face,Scaler AI Labs,Patronus AI,Surge AI,LastMile AI,Unsloth,Reflection,vLLM,SkyRL(UC-Berkeley),Lightning AI,Axolotl AI,Stanford Scaling Intelligence Lab,Mithril,OpenMined,Fleet AI,Halluminate,Turing,Scale AI,Scorecard

And we'd also like to acknowledge the team at Farama Foundation as the OpenEnv API was heavily inspired by the work you all have done on Gymnasium. Cheers!

## License

BSD 3-Clause License (seeLICENSEfile)

## About

An interface library for RL post training with environments.

huggingface.co/docs/openenv/index

### Resources

 Readme

 

### License

 BSD-3-Clause license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.1k

 stars
 

### Watchers

16

 watching
 

### Forks

391

 forks
 

 Report repository

 

## Releases5

v0.3.1

 Latest

 

Jun 2, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python85.0%
* Jupyter Notebook10.7%
* Shell2.2%
* Dockerfile1.6%
* Other0.5%