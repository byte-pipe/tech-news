---
title: 'GitHub - The-Swarm-Corporation/AutoHedge: Build your autonomous hedge fund in minutes. AutoHedge harnesses the power of swarm intelligence and AI agents to automate market analysis, risk management, and trade execution. · GitHub'
url: https://github.com/The-Swarm-Corporation/AutoHedge
site_name: github
content_file: github-github-the-swarm-corporationautohedge-build-your-a
fetched_at: '2026-09-06T13:57:11.404862'
original_url: https://github.com/The-Swarm-Corporation/AutoHedge
author: The-Swarm-Corporation
description: Build your autonomous hedge fund in minutes. AutoHedge harnesses the power of swarm intelligence and AI agents to automate market analysis, risk management, and trade execution. - The-Swarm-Corporation/AutoHedge
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 The-Swarm-Corporation

 

/

AutoHedge

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork763
* Star4.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

37 Commits
37 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
autohedge
autohedge
 
 
experimental
experimental
 
 
logs
logs
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
example.py
example.py
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# AutoHedge

 
 
 

AutoHedge is an enterprise-grade autonomous agent hedge fund that trades on your behalf. It combines swarm intelligence and specialized AI agents to perform end-to-end market analysis, risk management, and execution with minimal human intervention.

Current support:Full autonomous trading on Solana.Coming soon:Coinbase and additional exchanges.

## Overview

AutoHedge is built to be the world's most powerful autonomous agent hedge fund. It runs continuous analysis, generates and validates trading theses, sizes risk, and executes orders across supported venues. The system is designed for institutional reliability: structured outputs, comprehensive logging, and a risk-first architecture that scales from single strategies to multi-venue, multi-asset deployment.

## Features

* Multi-Agent Architecture: Specialized agents for each stage of the trading pipelineDirector Agent: strategy and thesis generationQuant Agent: technical and statistical analysisRisk Management Agent: position sizing and risk assessmentExecution Agent: order generation and execution
* Director Agent: strategy and thesis generation
* Quant Agent: technical and statistical analysis
* Risk Management Agent: position sizing and risk assessment
* Execution Agent: order generation and execution
* Real-Time Market Analysis: Integration with live market data for analysis and execution
* Risk-First Design: Built-in risk management and position sizing before any execution
* Structured Output: JSON-formatted recommendations and analysis for downstream systems
* Enterprise Logging: Detailed, configurable logging for audit and debugging
* Extensible Framework: Modular design for custom strategies and new venues

## Supported Venues

Venue

Status

Notes

Solana

Supported

Full autonomous trading

Coinbase

Coming soon

In development

Other CEX

Roadmap

Planned expansion

## Quick Start

### Installation

pip install -U autohedge

### Environment Variables

#
 Jupiter API (token price & search tools)

#
 Get a key at https://portal.jup.ag

JUPITER_API_KEY=

#
 OpenAI (experimental agents)

OPENAI_API_KEY=
ANTHROPIC_API_KEY=
WORKSPACE_DIR=
"
agent_workspace
"

#
 Trading

WALLET_PRIVATE_KEY=
"
"

See.env.examplefor a full reference.

### Basic Usage

autohedge
 

## Architecture

AutoHedge uses a multi-agent pipeline where each agent has a defined responsibility:

graph TD
 A[Director Agent] --> B[Quant Agent]
 B --> C[Risk Manager]
 C --> D[Execution Agent]
 D --> E[Trade Output]

 
Loading

## Contributing

Contributions are welcome. SeeContributing Guidelinesfor details.

1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

MIT License. SeeLICENSEfor details.

## Acknowledgments

* Swarmsfor the AI agent framework

## Support

* Issue Tracker:GitHub Issues
* Community:Discord

AutoHedge byThe Swarm Corporation

Generated from
 
kyegomez/Python-Package-Template