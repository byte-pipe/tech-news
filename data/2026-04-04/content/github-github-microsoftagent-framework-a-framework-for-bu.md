---
title: 'GitHub - microsoft/agent-framework: A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. · GitHub'
url: https://github.com/microsoft/agent-framework
site_name: github
content_file: github-github-microsoftagent-framework-a-framework-for-bu
fetched_at: '2026-04-04T11:11:35.355262'
original_url: https://github.com/microsoft/agent-framework
author: microsoft
description: A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET. - microsoft/agent-framework
---

microsoft

 

/

agent-framework

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star8.5k

 
 
 
 
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

1,834 Commits
1,834 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
declarative-agents
declarative-agents
 
 
docs
docs
 
 
dotnet
dotnet
 
 
python
python
 
 
schemas
schemas
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
COMMUNITY.md
COMMUNITY.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
TRANSPARENCY_FAQ.md
TRANSPARENCY_FAQ.md
 
 
wf-source-gen-plan.md
wf-source-gen-plan.md
 
 
View all files

## Repository files navigation

# Welcome to Microsoft Agent Framework!

Welcome to Microsoft's comprehensive multi-language framework for building, orchestrating, and deploying AI agents with support for both .NET and Python implementations. This framework provides everything from simple chat agents to complex multi-agent workflows with graph-based orchestration.

Watch the full Agent Framework introduction (30 min)

## 📋 Getting Started

### 📦 Installation

Python

pip install agent-framework

#
 This will install all sub-packages, see `python/packages` for individual packages.

#
 It may take a minute on first install on Windows.

.NET

dotnet add package Microsoft.Agents.AI

### 📚 Documentation

* Overview- High level overview of the framework
* Quick Start- Get started with a simple agent
* Tutorials- Step by step tutorials
* User Guide- In-depth user guide for building agents and workflows
* Migration from Semantic Kernel- Guide to migrate from Semantic Kernel
* Migration from AutoGen- Guide to migrate from AutoGen

Still have questions? Join ourweekly office hoursor ask questions in ourDiscord channelto get help from the team and other users.

### ✨Highlights

* Graph-based Workflows: Connect agents and deterministic functions using data flows with streaming, checkpointing, human-in-the-loop, and time-travel capabilitiesPython workflows|.NET workflows
* Python workflows|.NET workflows
* AF Labs: Experimental packages for cutting-edge features including benchmarking, reinforcement learning, and research initiativesLabs directory
* Labs directory
* DevUI: Interactive developer UI for agent development, testing, and debugging workflowsDevUI package
* DevUI package

See the DevUI in action (1 min)

* Python and C#/.NET Support: Full framework support for both Python and C#/.NET implementations with consistent APIsPython packages|.NET source
* Python packages|.NET source
* Observability: Built-in OpenTelemetry integration for distributed tracing, monitoring, and debuggingPython observability|.NET telemetry
* Python observability|.NET telemetry
* Multiple Agent Provider Support: Support for various LLM providers with more being added continuouslyPython examples|.NET examples
* Python examples|.NET examples
* Middleware: Flexible middleware system for request/response processing, exception handling, and custom pipelinesPython middleware|.NET middleware
* Python middleware|.NET middleware

### 💬We want your feedback!

* For bugs, please file aGitHub issue.

## Quickstart

### Basic Agent - Python

Create a simple Azure Responses Agent that writes a haiku about the Microsoft Agent Framework

# pip install agent-framework

# Use `az login` to authenticate with Azure CLI

import
 
os

import
 
asyncio

from
 
agent_framework
 
import
 
Agent

from
 
agent_framework
.
foundry
 
import
 
FoundryChatClient

from
 
azure
.
identity
 
import
 
AzureCliCredential

async
 
def
 
main
():
 
# Initialize a chat agent with Microsoft Foundry

 
# the endpoint, deployment name, and api version can be set via environment variables

 
# or they can be passed in directly to the FoundryChatClient constructor

 
agent
 
=
 
Agent
(
 
client
=
FoundryChatClient
(
 
credential
=
AzureCliCredential
(),
 
# project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],

 
# model=os.environ["FOUNDRY_MODEL_DEPLOYMENT_NAME"],

 ),
 
name
=
"HaikuBot"
,
 
instructions
=
"You are an upbeat assistant that writes beautifully."
,
 )

 
print
(
await
 
agent
.
run
(
"Write a haiku about Microsoft Agent Framework."
))

if
 
__name__
 
==
 
"__main__"
:
 
asyncio
.
run
(
main
())

### Basic Agent - .NET

Create a simple Agent, using OpenAI Responses, that writes a haiku about the Microsoft Agent Framework

// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease

using
 
Microsoft
.
Agents
.
AI
;

using
 
OpenAI
;

using
 
OpenAI
.
Responses
;

// Replace the <apikey> with your OpenAI API key.

var
 
agent
 
=
 
new
 
OpenAIClient
(
"<apikey>"
)

 
.
GetResponsesClient
(
"gpt-4o-mini"
)

 
.
AsAIAgent
(
name
:
 
"HaikuBot"
,
 
instructions
:
 
"You are an upbeat assistant that writes beautifully."
)
;

Console
.
WriteLine
(
await
 
agent
.
RunAsync
(
"Write a haiku about Microsoft Agent Framework."
)
)
;

Create a simple Agent, using Microsoft Foundry with token-based auth, that writes a haiku about the Microsoft Agent Framework

// dotnet add package Microsoft.Agents.AI.AzureAI --prerelease

// dotnet add package Azure.Identity

// Use `az login` to authenticate with Azure CLI

using
 
Azure
.
AI
.
Projects
;

using
 
Azure
.
Identity
;

using
 
Microsoft
.
Agents
.
AI
;

var
 
endpoint
 
=
 
Environment
.
GetEnvironmentVariable
(
"AZURE_AI_PROJECT_ENDPOINT"
)
 
??
 
throw
 
new
 
InvalidOperationException
(
"AZURE_AI_PROJECT_ENDPOINT is not set."
)
;

var
 
deploymentName
 
=
 
Environment
.
GetEnvironmentVariable
(
"AZURE_AI_MODEL_DEPLOYMENT_NAME"
)
 
??
 
"gpt-4o-mini"
;

var
 
agent
 
=
 
new
 
AIProjectClient
(
new
 
Uri
(
endpoint
)
,
 
new
 
DefaultAzureCredential
(
)
)

 
.
AsAIAgent
(
model
:
 
deploymentName
,
 
name
:
 
"HaikuBot"
,
 
instructions
:
 
"You are an upbeat assistant that writes beautifully."
)
;

Console
.
WriteLine
(
await
 
agent
.
RunAsync
(
"Write a haiku about Microsoft Agent Framework."
)
)
;

## More Examples & Samples

### Python

* Getting Started: progressive tutorial from hello-world to hosting
* Agent Concepts: deep-dive samples by topic (tools, middleware, providers, etc.)
* Workflows: workflow creation and integration with agents
* Hosting: A2A, Azure Functions, Durable Task hosting
* End-to-End: full applications, evaluation, and demos

### .NET

* Getting Started: progressive tutorial from hello agent to hosting
* Agent Concepts: basic agent creation and tool usage
* Agent Providers: samples showing different agent providers
* Workflows: advanced multi-agent patterns and workflow orchestration
* Hosting: A2A, Durable Agents, Durable Workflows
* End-to-End: full applications and demos

## Troubleshooting

### Authentication

Problem

Cause

Fix

Authentication errors when using Azure credentials

Not signed in to Azure CLI

Run 
az login
 before starting your app

API key errors

Wrong or missing API key

Verify the key and ensure it's for the correct resource/provider

Tip:DefaultAzureCredentialis convenient for development but in production, consider using a specific credential (e.g.,ManagedIdentityCredential) to avoid latency issues, unintended credential probing, and potential security risks from fallback mechanisms.

### Environment Variables

The samples typically read configuration from environment variables. Common required variables:

Variable

Used by

Purpose

AZURE_OPENAI_ENDPOINT

Azure OpenAI samples

Your Azure OpenAI resource URL

AZURE_OPENAI_DEPLOYMENT_NAME

Azure OpenAI samples

Model deployment name (e.g. 
gpt-4o-mini
)

AZURE_AI_PROJECT_ENDPOINT

Microsoft Foundry samples

Your Microsoft Foundry project endpoint

AZURE_AI_MODEL_DEPLOYMENT_NAME

Microsoft Foundry samples

Model deployment name

OPENAI_API_KEY

OpenAI (non-Azure) samples

Your OpenAI platform API key

## Contributor Resources

* Contributing Guide
* Python Development Guide
* Design Documents
* Architectural Decision Records

## Important Notes

If you use the Microsoft Agent Framework to build applications that operate with third-party servers or agents, you do so at your own risk. We recommend reviewing all data being shared with third-party servers or agents and being cognizant of third-party practices for retention and location of data. It is your responsibility to manage whether your data will flow outside of your organization's Azure compliance and geographic boundaries and any related implications.

## About

A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.

aka.ms/agent-framework

### Topics

 python

 sdk

 ai

 dotnet

 orchestration

 multi-agent

 workflows

 agents

 agent-framework

 agentic-ai

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

8.5k

 stars
 

### Watchers

92

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases69

dotnet-1.0.0

 Latest

 

Apr 2, 2026

 

+ 68 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python50.6%
* C#45.2%
* TypeScript3.7%
* HTML0.3%
* CSS0.1%
* PowerShell0.1%