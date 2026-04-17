---
title: 'GitHub - Tracer-Cloud/opensre: Build your own AI SRE agents. The open source toolkit for the AI era ✨ · GitHub'
url: https://github.com/Tracer-Cloud/opensre
site_name: github
content_file: github-github-tracer-cloudopensre-build-your-own-ai-sre-a
fetched_at: '2026-04-17T11:51:16.544457'
original_url: https://github.com/Tracer-Cloud/opensre
author: Tracer-Cloud
description: 'Build your own AI SRE agents. The open source toolkit for the AI era ✨ - GitHub - Tracer-Cloud/opensre: Build your own AI SRE agents. The open source toolkit for the AI era ✨'
---

Tracer-Cloud

 

/

opensre

Public

* NotificationsYou must be signed in to change notification settings
* Fork150
* Star1.1k

 
 
 
 
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

1,103 Commits
1,103 Commits
.cursor
.cursor
 
 
.github
.github
 
 
app
app
 
 
docs
docs
 
 
packaging
packaging
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.tool-versions
.tool-versions
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DEPLOYEMENT.md
DEPLOYEMENT.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SETUP.md
SETUP.md
 
 
docker-compose.database.yml
docker-compose.database.yml
 
 
docker-compose.testing.yml
docker-compose.testing.yml
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
langgraph.json
langgraph.json
 
 
mypy.ini
mypy.ini
 
 
pyproject.toml
pyproject.toml
 
 
pytest.ini
pytest.ini
 
 
ruff.toml
ruff.toml
 
 
View all files

## Repository files navigation

### OpenSRE: Build Your Own AI SRE Agents

The open-source framework for AI SRE agents, and the training and evaluation environment they need to improve. Connect the 40+ tools you already run, define your own workflows, and investigate incidents on your own infrastructure.

Quickstart·Docs·FAQ·Security

## Why OpenSRE?

When something breaks in production, the evidence is scattered across logs, metrics, traces, runbooks, and Slack threads. OpenSRE is an open-source framework for AI SRE agents that resolve production incidents, built to run on your own infrastructure.

We do that because SWE-bench1gave coding agents scalable training data and clear feedback. Production incident response still lacks an equivalent.

Distributed failures are slower, noisier, and harder to simulate and evaluate than local code tasks, which is why AI SRE, and AI for production debugging more broadly, remains unsolved.

OpenSRE is buildingthatmissing layer:

an open reinforcement learning environment for agentic infrastructure incident response, with end-to-end tests and synthetic incident simulations for realistic production failures

We do that by:

* building easy-to-deploy, customizable AI SRE agents for production incident investigation and response
* running scored synthetic RCA suites that check root-cause accuracy, required evidence, and adversarial red herrings(tests/synthetic)
* running real-world end-to-end tests across cloud-backed scenarios including Kubernetes, EC2, CloudWatch, Lambda, ECS Fargate, and Flink(tests/e2e)
* keeping semantic test-catalog naming so e2e vs synthetic and local vs cloud boundaries stay obvious(tests/README.md)

Our mission is to build AI SRE agents on top of this, scale it to thousands of realistic infrastructure failure scenarios, and establish OpenSRE as the benchmark and training ground for AI SRE.

1https://arxiv.org/abs/2310.06770

## Install

curl -fsSL https://raw.githubusercontent.com/Tracer-Cloud/opensre/main/install.sh 
|
 bash

brew install Tracer-Cloud/opensre/opensre

irm https:
//
raw.githubusercontent.com
/
Tracer
-
Cloud
/
opensre
/
main
/
install.ps1 
|
 iex

## Quick Start

opensre onboard
opensre investigate -i tests/e2e/kubernetes/fixtures/datadog_k8s_alert.json
opensre update

## Development

New to OpenSRE?SeeSETUP.mdfor detailed platform-specific setup instructions, including Windows setup, environment configuration, and more.

git clone https://github.com/Tracer-Cloud/opensre

cd
 opensre
make install

#
 run opensre onboard to configure your local LLM provider

#
 and optionally validate/save Grafana, Datadog, Honeycomb, Coralogix, Slack, AWS, GitHub MCP, and Sentry integrations

opensre onboard
opensre investigate -i tests/e2e/kubernetes/fixtures/datadog_k8s_alert.json

## How OpenSRE Works

### Investigation Workflow

When an alert fires, OpenSRE automatically:

1. Fetchesthe alert context and correlated logs, metrics, and traces
2. Reasonsacross your connected systems to identify anomalies
3. Generatesa structured investigation report with probable root cause
4. Suggestsnext steps and, optionally, executes remediation actions
5. Postsa summary directly to Slack or PagerDuty - no context switching needed

## Benchmark

Generate the benchmark report:

make benchmark

## Capabilities

🔍 
Structured incident investigation

Correlated root-cause analysis across all your signals

📋 
Runbook-aware reasoning

OpenSRE reads your runbooks and applies them automatically

🔮 
Predictive failure detection

Catch emerging issues before they page you

🔗 
Evidence-backed root cause

Every conclusion is linked to the data behind it

🤖 
Full LLM flexibility

Bring your own model — Anthropic, OpenAI, Ollama, Gemini, OpenRouter, NVIDIA NIM

## Integrations

OpenSRE connects to 40+ tools and services across the modern cloud stack, from LLM providers and observability platforms to infrastructure, databases, and incident management.

Category

Integrations

Roadmap

AI / LLM Providers

Anthropic · OpenAI · Ollama · Google Gemini · OpenRouter · NVIDIA NIM · Bedrock

Observability

 Grafana (Loki · Mimir · Tempo) · 
 Datadog · Honeycomb · Coralogix · 
 CloudWatch · 
 Sentry · Elasticsearch

Splunk
 · 
New Relic
 · 
Victoria Logs

Infrastructure

 Kubernetes · 
 AWS (S3 · Lambda · EKS · EC2 · Bedrock) · 
 GCP · 
 Azure

Helm
 · 
ArgoCD

Database

MongoDB · ClickHouse

PostgreSQL · MySQL
 · 
MariaDB
 · 
MongoDB Atlas
 · 
Azure SQL
 · 
RDS
 · 
Snowflake

Data Platform

Apache Airflow · Apache Kafka · Apache Spark · Prefect

RabbitMQ

Dev Tools

 GitHub · GitHub MCP · Bitbucket

GitLab

Incident Management

 PagerDuty · Opsgenie · Jira

ServiceNow
 · 
incident.io
 · 
Alertmanager
 · 
Linear
 · 
Trello

Communication

 Slack · Google Docs

Discord
 · 
Teams
 · 
WhatsApp
 · 
Confluence
 · 
Notion

Agent Deployment

 Vercel · 
 LangSmith · 
 EC2 · 
 ECS

Railway

Protocols

 MCP · 
 ACP · 
 OpenClaw

## Contributing

OpenSRE is community-built. Every integration, improvement, and bug fix makes it better for thousands of engineers. We actively review PRs and welcome contributors of all experience levels.

Good first issues are labeledgood first issue. Ways to contribute:

* 🐛 Report bugs or missing edge cases
* 🔌 Add a new tool integration
* 📖 Improve documentation or runbook examples
* ⭐ Star the repo - it helps other engineers find OpenSRE

SeeCONTRIBUTING.mdfor the full guide.

Thanks goes to these amazing people:

davincios

VaibhavUpreti

aliya-tracer

arnetracer

kylie-tracer

paultracer

zeel2104

iamkalio

w3joe

yeoreums

anandgupta1202

rrajan94

vrk7

cerencamkiran

edgarmb14

lukegimza

ebrahim-sameh

shoaib050326

venturevd

shriyashsoni

Devesh36

KindaJayant

overcastbulb

Yashkapure06

Davda-James

Abhinnavverma

devankitjuneja

ramandagar

mvanhorn

abhishek-marathe04

yashksaini-coder

haliaeetusvocifer

Bahtya

mayankbharati-ops

harshareddy832

sundaram2021

micheal000010000-hub

ljivesh

gautamjain1503

mudittt

hamzzaaamalik

octo-patch

aniruddhaadak80

## Security

OpenSRE is designed with production environments in mind:

* No storing of raw log data beyond the investigation session
* All LLM calls use structured, auditable prompts
* Log transcripts are kept locally - never sent externally by default

SeeSECURITY.mdfor responsible disclosure.

## Telemetry

opensrecollects anonymous usage statistics with Posthog to help us understand adoption
and demonstrate traction to sponsors and investors who fund the project.
What we collect: command name, success/failure, rough runtime, CLI version,
Python version, OS family, machine architecture, and a small amount of
command-specific metadata such as which subcommand ran. Foropensre onboardandopensre investigate, we may also collect the selected model/provider and
whether the command used flags such as--interactiveor--input.

A randomly generated anonymous ID is created on first run and stored in~/.config/opensre/. We never collect alert contents, file contents,
hostnames, credentials, or any personally identifiable information.

Telemetry is automatically disabled in GitHub Actions and pytest runs.

To opt out locally, set the environment variable before running:

export
 OPENSRE_NO_TELEMETRY=1

The legacy aliasOPENSRE_ANALYTICS_DISABLED=1also still works.

To inspect the payload locally without sending anything, use:

export
 OPENSRE_TELEMETRY_DEBUG=1

## License

Apache 2.0 - seeLICENSEfor details.

## Citations

1https://arxiv.org/abs/2310.06770

## About

Build your own AI SRE agents. The open source toolkit for the AI era ✨

opensre.com

### Topics

 slack

 grafana

 site-reliability-engineering

 alerting

 datadog

 sre

 observability

 incident-management

 remediation

 root-cause-analysis

 ai-sre

### Resources

 Readme

 

### License

 Apache-2.0 license
 

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

1.1k

 stars
 

### Watchers

5

 watching
 

### Forks

150

 forks
 

 Report repository

 

## Releases11

Latest

 Latest

 

Apr 17, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python98.8%
* Other1.2%