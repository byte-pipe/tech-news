---
title: 'GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. · GitHub'
url: https://github.com/uber/ADR
site_name: github
content_file: github-github-uberadr-adr-secures-enterprise-ai-agents-th
fetched_at: '2026-08-04T11:45:58.875098'
original_url: https://github.com/uber/ADR
author: uber
description: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. - uber/ADR
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 uber

 

/

ADR

Public

* NotificationsYou must be signed in to change notification settings
* Fork60
* Star509

 
 
 
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

33 Commits
33 Commits
.github
.github
 
 
Detection
Detection
 
 
Sensor
Sensor
 
 
docs
docs
 
 
.gitignore
.gitignore
 
 
CITATION.cff
CITATION.cff
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# ADR: Agentic AI Detection and Response

ADR (Agentic AI Detection and Response) is an enterprise security system for AI agents. It helps organizations secure employee-facing agents such as Cursor, Claude Code, and Codex, as well as customer-facing agents such as AI support agents.

ADR isdeployed in production at Uber, and the accompanying paper was accepted toMLSys 2026:Paper PDF·Slides PDF

## How ADR secures enterprise AI agents

ADR secures enterprise AI agents through four complementary capabilities: observing agent activity, evaluating defenses, detecting threats, and preventing unsafe actions.

1. ADR Observability: Understand what AI agents are doing and why.In production, ADR captures agent intent, tool use, and execution traces across 7+ AI coding tools on macOS, Linux, and Windows, as well as internal automation and customer-facing support agents.
2. ADR Benchmark: Test agent security under realistic enterprise conditions.ADR-Bench includes 300+ tasks, 133 MCP servers, and coverage of all 17 agent attack techniques.
3. ADR Detection: Detect risky agent behavior efficiently.Its two-tier architecture combines high-recall triage with deeper agentic reasoning for suspicious sessions.
4. ADR Prevention: Stop unsafe actions before they cause harm.This component is not included in the current open-source release.Stay tuned.

## Repository layout

This repository contains the open-sourceADR Sensor,ADR-Bench, andADR Detectordescribed in the paper. The offlineADR Explorerengine, which hardens ADR Detection through pre-deployment red teaming, is not included here.

Path

ADR component

Description

Sensor/

ADR Observability

Collect and normalize agent telemetry from Claude Code, Cursor, Codex, and others

Detection/

ADR Benchmark + Detection

Dual-agent detector, 133 MCP servers, 303 benchmark tasks, baselines, figure scripts

docs/REPRODUCIBILITY.md

Evaluation

Step-by-step workflow to reproduce benchmark detection and paper figures

## Quick start: ADR Detection

git clone https://github.com/uber/ADR

cd
 ADR/Detection
uv sync

export
 ANTHROPIC_API_KEY=
"
...
"
 OPENAI_API_KEY=
"
...
"

Default detector isadr(ADR dual-agent). For keyless smoke tests, use--detector llamafirewall(seeDetection/README.md).

Seedocs/REPRODUCIBILITY.mdfor the full evaluation workflow (inflate packed benchmark → run detectors → plot figures).

Component documentation:

* Sensor/README.md: telemetry collection and unified schema
* Detection/README.md: ADR-Bench, detector baselines, MCP infrastructure

## Citation

@inproceedings
{
li2026adr
,
 
title
=
{
ADR: An Agentic Detection System for Enterprise Agentic AI Security
}
,
 
author
=
{
Li, Chenning and Hu, Pan and Xu, Justin and Ozbas, Baris and Liu, Olivia and Van, Caroline and Li, Manxue and Zhou, Wei and Alizadeh, Mohammad and Zhang, Pengyu and Sriramadhesikan, KK and Zhang, Ming
}
,
 
booktitle
=
{
Proceedings of the Ninth Conference on Machine Learning and Systems
}
,
 
year
=
{
2026
}

}

Or useCITATION.cff.

## License

Apache License 2.0. SeeLICENSE.Detection/benchmark/agentdojo/is vendored third-party code under its ownLICENSE(MIT).

## Data notice

Detection/includessyntheticbenchmark fixtures (fake credentials, emulated environments, prompt-injection scenarios) for defensive security research only. Details:docs/OPEN_SOURCE_REVIEW.md.