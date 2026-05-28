---
title: 'GitHub - microsoft/agent-governance-toolkit: AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10. · GitHub'
url: https://github.com/microsoft/agent-governance-toolkit
site_name: github
content_file: github-github-microsoftagent-governance-toolkit-ai-agent
fetched_at: '2026-05-28T12:11:32.636662'
original_url: https://github.com/microsoft/agent-governance-toolkit
author: microsoft
description: AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10. - microsoft/agent-governance-toolkit
---

microsoft

 

/

agent-governance-toolkit

Public

* NotificationsYou must be signed in to change notification settings
* Fork471
* Star3.1k

 
 
 
 
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

1,750 Commits
1,750 Commits
.clusterfuzzlite
.clusterfuzzlite
 
 
.github
.github
 
 
action
action
 
 
agent-governance-antigravity-cli
agent-governance-antigravity-cli
 
 
agent-governance-claude-code
agent-governance-claude-code
 
 
agent-governance-copilot-cli
agent-governance-copilot-cli
 
 
agent-governance-dotnet
agent-governance-dotnet
 
 
agent-governance-golang
agent-governance-golang
 
 
agent-governance-python
agent-governance-python
 
 
agent-governance-rust
agent-governance-rust
 
 
agent-governance-typescript
agent-governance-typescript
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
tests
tests
 
 
.cspell-repo-terms.txt
.cspell-repo-terms.txt
 
 
.cspell.json
.cspell.json
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaksignore
.gitleaksignore
 
 
.npmrc
.npmrc
 
 
.pre-commit-hooks.yaml
.pre-commit-hooks.yaml
 
 
.safety-policy.yml
.safety-policy.yml
 
 
.safety.yml
.safety.yml
 
 
.shellcheckrc
.shellcheckrc
 
 
AGENTS.md
AGENTS.md
 
 
ANTITRUST.md
ANTITRUST.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CHARTER.md
CHARTER.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
TRADEMARKS.md
TRADEMARKS.md
 
 
VERSION
VERSION
 
 
docker-compose.yml
docker-compose.yml
 
 
mkdocs.yml
mkdocs.yml
 
 
View all files

## Repository files navigation

🌍English|日本語|简体中文|한국어

# Agent Governance Toolkit

### Ship agents to production without losing sleep

🚀Quick Start·
 📋Specifications·
 📦PyPI·
 📝Changelog

Important

Public Preview-- production-quality, Microsoft-signed releases. May have breaking changes before GA.

Policy enforcement, identity, sandboxing, and SRE for autonomous AI agents. Onepip install, any framework.

## The Problem

Your AI agents call tools, browse the web, query databases, and delegate to other agents. Once deployed, they make decisions autonomously. You need answers to three questions:

1. Is this action allowed?An agent with access tosend_emailandquery_databaseshould not be able todrop_table. OAuth scopes and IAM roles control which services an agent can reach, not what it does once connected.

2. Which agent did this?In a multi-agent system, five agents might share a single API key. When something goes wrong, "an agent did it" is not an incident response.

3. Can you prove what happened?Auditors and regulators need tamper-evident records of every decision: what policy was active, what the agent requested, and why it was allowed or denied.

Prompt-level safety ("please follow the rules") is not a control surface. It is a polite request to a stochastic system.OWASP LLM01:2025states this explicitly:"it is unclear if there are fool-proof methods of prevention for prompt injection."The published numbers back this up. OnJailbreakBench (Chao et al., NeurIPS 2024), the standard open robustness benchmark for LLM jailbreaks, adaptive attacks reachnear-100% attack success ratesagainst frontier safety-aligned models.Andriushchenko et al., 2024report 100% ASR on GPT-4, GPT-3.5, Claude 3, and Llama-3 using simple prompt-only attacks, and even the strongest published prompt-layer defenses leak double-digit residual ASR. Microsoft's ownAI Red Teaming AgentformalizesAttack Success Rate (ASR), the rate of policy violations under adversarial input, as the canonical metric for this class of failure, andLessons from Red Teaming 100 Generative AI Productsconcludes that"AI red teaming is never complete"because model-layer defenses are probabilistic by construction.

AGT does not try to win that fight inside the prompt. Every tool call, message send, and delegation is intercepted in deterministic application codebeforethe model's intent reaches the wire. Actions the AGT kernel denies are not "unlikely." They arestructurally impossible. That is the difference between asking an agent to behave and making it incapable of misbehaving.

## Quick Start

Prerequisites:Python 3.10+

pip install agent-governance-toolkit[full]

Govern any tool function in two lines:

from
 
agentmesh
.
governance
 
import
 
govern

safe_tool
 
=
 
govern
(
my_tool
, 
policy
=
"policy.yaml"
) 
# every call checked, logged, enforced

That's it.safe_toolevaluates your YAML policy on every call, logs the decision, and raisesGovernanceDeniedif the action is blocked.

#
 policy.yaml

apiVersion
: 
governance.toolkit/v1

name
: 
production-policy

default_action
: 
allow

rules
:
 - 
name
: 
block-destructive

 
condition
: 
"
action.type in ['drop', 'delete', 'truncate']
"

 
action
: 
deny

 
description
: 
"
Destructive operations require human approval
"

 - 
name
: 
require-approval-for-send

 
condition
: 
"
action.type == 'send_email'
"

 
action
: 
require_approval

 
approvers
: 
["security-team"]

>
>>
 
safe_tool
(
action
=
"read"
, 
table
=
"users"
)
{
'table'
: 
'users'
, 
'rows'
: 
42
}

>
>>
 
safe_tool
(
action
=
"drop"
, 
table
=
"users"
)

GovernanceDenied
: 
Action
 
denied
 
by
 
policy
 
rule
 
'block-destructive'
:
 
Destructive
 
operations
 
require
 
human
 
approval

Or use the fullPolicyEvaluatorAPI for programmatic control:

PolicyEvaluator example

from
 
agent_os
.
policies
 
import
 (
 
PolicyEvaluator
, 
PolicyDocument
, 
PolicyRule
,
 
PolicyCondition
, 
PolicyAction
, 
PolicyOperator
, 
PolicyDefaults

)

evaluator
 
=
 
PolicyEvaluator
(
policies
=
[
PolicyDocument
(
 
name
=
"my-policy"
, 
version
=
"1.0"
,
 
defaults
=
PolicyDefaults
(
action
=
PolicyAction
.
ALLOW
),
 
rules
=
[
PolicyRule
(
 
name
=
"block-dangerous-tools"
,
 
condition
=
PolicyCondition
(
 
field
=
"tool_name"
,
 
operator
=
PolicyOperator
.
IN
,
 
value
=
[
"execute_code"
, 
"delete_file"
]
 ),
 
action
=
PolicyAction
.
DENY
, 
priority
=
100
,
 )],
)])

result
 
=
 
evaluator
.
evaluate
({
"tool_name"
: 
"web_search"
}) 
# Allowed

result
 
=
 
evaluator
.
evaluate
({
"tool_name"
: 
"delete_file"
}) 
# Blocked

TypeScript / .NET / Rust / Go examples

TypeScript

import
 
{
 
PolicyEngine
 
}
 
from
 
"@microsoft/agent-governance-sdk"
;

const
 
engine
 
=
 
new
 
PolicyEngine
(
[

 
{
 
action
: 
"web_search"
,
 
effect
: 
"allow"
 
}
,

 
{
 
action
: 
"shell_exec"
,
 
effect
: 
"deny"
 
}
,

]
)
;

engine
.
evaluate
(
"web_search"
)
;
 
// "allow"

engine
.
evaluate
(
"shell_exec"
)
;
 
// "deny"

.NET

using
 
AgentGovernance
;

using
 
AgentGovernance
.
Extensions
.
ModelContextProtocol
;

using
 
AgentGovernance
.
Policy
;

var
 
kernel
 
=
 
new
 
GovernanceKernel
(
new
 
GovernanceOptions

{

 
PolicyPaths
 
=
 
new
(
)
 
{
 
"policies/default.yaml"
 
}
,

}
)
;

var
 
result
 
=
 
kernel
.
EvaluateToolCall
(
"did:mesh:agent-1"
,
 
"web_search"
,

 
new
(
)
 
{
 
[
"query"
]
 
=
 
"latest AI news"
 
}
)
;

// MCP server integration

builder
.
Services
.
AddMcpServer
(
)

 
.
WithGovernance
(
options 
=>
 
options
.
PolicyPaths
.
Add
(
"policies/mcp.yaml"
)
)
;

Rust

use
 agent_governance
::
{
AgentMeshClient
,
 
ClientOptions
}
;

let
 client = 
AgentMeshClient
::
new
(
"my-agent"
)
.
unwrap
(
)
;

let
 result = client
.
execute_with_governance
(
"data.read"
,
 
None
)
;

assert
!
(
result
.
allowed
)
;

Go

import
 agentmesh 
"github.com/microsoft/agent-governance-toolkit/agent-governance-golang"

client
, 
_
 
:=
 
agentmesh
.
NewClient
(
"my-agent"
,
 
agentmesh
.
WithPolicyRules
([]agentmesh.
PolicyRule
{
 {
Action
: 
"data.read"
, 
Effect
: 
agentmesh
.
Allow
},
 {
Action
: 
"*"
, 
Effect
: 
agentmesh
.
Deny
},
 }),
)

result
 
:=
 
client
.
ExecuteWithGovernance
(
"data.read"
, 
nil
)

CLI tools:

agt doctor 
#
 check installation

agt verify 
#
 OWASP compliance check

agt verify --evidence ./agt-evidence.json --strict 
#
 fail CI on weak evidence

agt red-team scan ./prompts/ --min-grade B 
#
 prompt injection audit

agt lint-policy policies/ 
#
 validate policy files

Full walkthrough:quickstart.md-- zero to governed agents in 5 minutes.
🌍 Also in:日本語|简体中文|한국어

## How It Works

Agent ──► Policy Engine ──► Identity ──► Audit Log
 (YAML/OPA/Cedar) (SPIFFE/DID/mTLS) (Tamper-evident)
 │ │
 ├── Allowed ──► Tool executes │
 └── Denied ──► GovernanceDenied │
 ▼
 Decision Record

Every layer is optional. Start withgovern()and add layers as your risk profile grows. Most teams run policy enforcement + audit logging and never need the full stack.

## Packages

Package

Description

Agent OS

Policy engine, agent lifecycle, governance gate

Agent Mesh

Agent discovery, routing, and trust mesh

Agent Runtime

Execution sandboxing with four privilege rings

Agent SRE

Kill switch, SLO monitoring, chaos testing

Agent Compliance

OWASP verification, policy linting, integrity checks

Agent Marketplace

Plugin governance and trust scoring

Agent Lightning

RL training governance with violation penalties

Agent Hypervisor

Execution audit, delta engine, commitment anchoring

### Additional Capabilities

Capability

Description

MCP Security Gateway

Tool poisoning detection, drift monitoring, typosquatting, hidden instruction scanning (
Spec
)

Shadow AI Discovery

Find unregistered agents across processes, configs, and repos (
Discovery
)

Governance Dashboard

Real-time fleet visibility for health, trust, and compliance (
Dashboard
)

PromptDefense Evaluator

12-vector prompt injection audit (
Evaluator
)

Contributor Reputation

PR/issue author screening for social engineering. Reusable GitHub Action (
Action
)

## Install

Language

Package

Command

Python

agent-governance-toolkit

pip install agent-governance-toolkit[full]

TypeScript

@microsoft/agent-governance-sdk

npm install @microsoft/agent-governance-sdk

Copilot CLI

@microsoft/agent-governance-copilot-cli

npx @microsoft/agent-governance-copilot-cli install

Claude Code

@microsoft/agent-governance-claude-code

claude --plugin-dir ./agent-governance-claude-code

.NET

Microsoft.AgentGovernance

dotnet add package Microsoft.AgentGovernance

.NET MCP

Microsoft.AgentGovernance.Extensions.ModelContextProtocol

dotnet add package Microsoft.AgentGovernance.Extensions.ModelContextProtocol

Rust

agent-governance

cargo add agent-governance

Go

agent-governance-toolkit

go get github.com/microsoft/agent-governance-toolkit/agent-governance-golang

All five language SDKs implement core governance (policy, identity, trust, audit). Python has the full stack. Copilot CLI and Claude Code are first-party developer surfaces built on the TypeScript SDK.
SeeLanguage Package Matrixfor detailed per-language coverage.

Individual Python packages

Package

PyPI

Description

Agent OS

agent-os-kernel

Policy engine, capability model, audit logging, MCP gateway

AgentMesh

agentmesh-platform

Zero-trust identity, trust scoring, A2A/MCP/IATP bridges

Agent Runtime

agentmesh-runtime

Privilege rings, saga orchestration, termination control

Agent SRE

agent-sre

SLOs, error budgets, chaos engineering, circuit breakers

Agent Compliance

agent-governance-toolkit

OWASP verification, integrity checks, policy linting

Agent Discovery

agent-discovery

Shadow AI discovery, inventory, risk scoring

Agent Hypervisor

agent-hypervisor

Execution plan validation, reversibility verification

Agent Marketplace

agentmesh-marketplace

Plugin lifecycle management

Agent Lightning

agentmesh-lightning

RL training governance

### Prerequisites

* Python: 3.10+
* Node.js: 18+ / npm 9+ (TypeScript SDK)
* .NET: 8+
* Go: 1.25+
* Rust: 1.70+
* Optional:AZURE_CLIENT_ID,AZURE_TENANT_ID,AZURE_CLIENT_SECRETfor Azure-integrated features

## Framework Support

Framework

Integration

Microsoft Agent Framework

Native Middleware

Semantic Kernel

Native (.NET + Python)

AutoGen

Adapter

LangGraph
 / 
LangChain

Adapter

CrewAI

Adapter

OpenAI Agents SDK

Middleware

Claude Code

Governance plugin package

Google ADK

Adapter

LlamaIndex

Middleware

Haystack

Pipeline

Mastra

Adapter

Dify

Plugin

Azure AI Foundry

Deployment Guide

GitHub Copilot CLI

Governance installer

Full list:Framework Integrations·Quickstart Examples

## Examples

Example

Framework

What it demonstrates

openai-agents-governed

OpenAI Agents SDK

Policy-gated tool calls with trust tiers

crewai-governed

CrewAI

Multi-agent governance with role-based policies

smolagents-governed

HuggingFace smolagents

Lightweight agent governance

maf-integration

MAF

Microsoft Agent Framework integration

mcp-trust-verified-server

MCP

Trust-verified MCP server implementation

cedarling-governed

Cedar/Cedarling

Janssen Cedarling policy engine integration

governance-dashboard

Streamlit

Real-time fleet visibility dashboard

## Specifications

Every major component has a formal RFC 2119 specification with conformance tests. These specs define the behavioral contract: what implementations MUST, SHOULD, and MAY do.

Specification

Scope

Tests

Agent OS Policy Engine

Policy evaluation, rule merging, fail-closed semantics

68

AgentMesh Identity and Trust

Credentials, trust scoring, delegation chains

135

Agent Hypervisor Execution Control

Privilege rings, saga orchestration, kill switch

80

AgentMesh Trust and Coordination

Peer trust negotiation, mesh-wide policy

62

Agent SRE Governance

SLOs, error budgets, chaos, circuit breakers

111

MCP Security Gateway

Tool poisoning, drift detection, hidden instructions

127

Agent Lightning Fast-Path

RL training governance, violation penalties

100

Framework Adapter Contract

10 adapter integrations, interceptor chain

152

Audit and Compliance

Merkle audit, compliance mapping, Decision BOM

157

AgentMesh Wire Protocol

Message format, routing, serialization

--

992 conformance testsensure code stays aligned to specs.25 Architecture Decision Recordsdocument why.

## Standards Compliance

Standard

Coverage

OWASP Agentic AI Top 10

All ASI risk categories mapped with deterministic controls

NIST AI RMF 1.0

Full GOVERN, MAP, MEASURE, MANAGE alignment

EU AI Act

Compliance mapping with automated evidence

SOC 2

Control mapping with audit trail export

## Security

AGT enforces governance at the application middleware layer, not at the OS kernel level. The policy engine and agents share the same process boundary.

Production recommendation:Run each agent in a separate container for OS-level isolation. SeeArchitecture: Security Boundaries.

Tool

Coverage

CodeQL

Python + TypeScript SAST

Gitleaks

Secret scanning on PR/push/weekly

ClusterFuzzLite

7 fuzz targets (policy, injection, MCP, sandbox, trust)

Dependabot

13 ecosystems

OpenSSF Scorecard

Weekly scoring + SARIF upload

SeeKnown Limitationsfor honest design boundaries and recommended layered defense.

## Documentation

Category

Links

Getting Started

Quick Start
 · 
Tutorials
 (60+) · 
FAQ

Architecture

System Design
 · 
Threat Model
 · 
ADRs
 (25)

Specifications

All Specs
 (10 formal specs, 992 conformance tests)

API Reference

Agent OS
 · 
AgentMesh
 · 
Agent SRE

Compliance

OWASP
 · 
EU AI Act
 · 
NIST AI RMF
 · 
SOC 2

Deployment

Azure
 · 
AWS
 · 
GCP
 · 
Docker Compose

Extensions

VS Code
 · 
Framework Integrations

## Contributing

Contributing Guide·Community·Security Policy·Changelog

Using AGT?Add your organization toADOPTERS.md.

## Governance

Document

Purpose

GOVERNANCE.md

Decision-making, roles, contributor ladder

CHARTER.md

Technical charter (LF Projects format)

MAINTAINERS.md

Maintainers and organizations

SECURITY.md

Vulnerability reporting and response SLAs

CODE_OF_CONDUCT.md

Microsoft Open Source Code of Conduct

ANTITRUST.md

Competition law guidelines for participants

TRADEMARKS.md

Trademark usage policy

## Important Notes

If you use the Agent Governance Toolkit to build applications that operate with third-party agent frameworks or services, you do so at your own risk. We recommend reviewing all data being shared with third-party services and being cognizant of third-party practices for retention and location of data.

## Official Sources

The only official sources for the Agent Governance Toolkit are:

Resource

Location

Source code

github.com/microsoft/agent-governance-toolkit

Documentation

microsoft.github.io/agent-governance-toolkit

Python packages

pypi.org/user/agentgovtoolkit

npm packages

@microsoft/agentmesh-sdk
, 
@microsoft/agent-os-kernel
 on 
npmjs.com

NuGet packages

Microsoft.AgentGovernance.*
 on 
nuget.org

Rust crates

agent-os-kernel
, 
agentmesh
 on 
crates.io

The project team does not maintain or endorse any third-party websites,
packages, or documentation sites claiming to be official. If you encounter a
suspicious site or package using the Agent Governance Toolkit name, please
report it through the channels described inSECURITY.md.

## License

This project is licensed under theMIT License.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must followMicrosoft's Trademark & Brand Guidelines.
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## About

AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10.

### Topics

 microsoft

 python

 security

 owasp

 trust

 compliance

 governance

 ai-safety

 policy-engine

 ai-agents

 zero-trust

 agent-framework

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

3.1k

 stars
 

### Watchers

23

 watching
 

### Forks

471

 forks
 

 Report repository

 

## Releases17

v3.7.0

 Latest

 

May 18, 2026

 

+ 16 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python77.6%
* TypeScript10.0%
* C#3.6%
* Rust3.4%
* Go1.9%
* JavaScript1.6%
* Other1.9%