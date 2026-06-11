---
title: 'GitHub - aws/agent-toolkit-for-aws: Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS · GitHub'
url: https://github.com/aws/agent-toolkit-for-aws
site_name: tldr
content_file: tldr-github-awsagent-toolkit-for-aws-official-aws-suppo
fetched_at: '2026-06-11T12:23:43.132541'
original_url: https://github.com/aws/agent-toolkit-for-aws
date: '2026-06-11'
description: Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS - aws/agent-toolkit-for-aws
tags:
- tldr
---

aws

 

/

agent-toolkit-for-aws

Public

* NotificationsYou must be signed in to change notification settings
* Fork77
* Star847

 
 
 
 
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

62 Commits
62 Commits
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.github
.github
 
 
plugins
plugins
 
 
rules
rules
 
 
skills
skills
 
 
tools
tools
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.markdownlint-cli2.yaml
.markdownlint-cli2.yaml
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SUPPORT.md
SUPPORT.md
 
 
mise.toml
mise.toml
 
 
View all files

## Repository files navigation

# Agent Toolkit for AWS

Help AI coding agents build, deploy, and manage applications on AWS.

The Agent Toolkit for AWS gives AI coding agents the tools, knowledge, and guardrails they need to work with AWS services. It works with the coding agents developers already use — including Claude Code, Codex, Cursor, and Kiro.

## Quick start

### Claude Code

The plugins are available on the official Anthropic marketplace (claude-plugins-official) which is added to your Claude Code installation by default.
Use the following commands to install supported plugins from the toolkit:

Foraws-corethat covers service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, and deployment:

/plugin install aws-core@claude-plugins-official

Tip:If you getPlugin not found, update your local marketplace index first:

/plugin marketplace update claude-plugins-official

Foraws-agentsthat covers building AI agents on AWS with Amazon Bedrock and AgentCore:

/plugin install aws-agents@claude-plugins-official

Foraws-data-analyticsthat covers data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena:

/plugin install aws-data-analytics@claude-plugins-official

### Codex

In your terminal:

codex plugin marketplace add aws/agent-toolkit-for-aws

Then launch Codex and run/pluginsto browse and install theaws-coreplugin.

### Cursor

Add this repository as a team marketplace fromSettings → Plugins → Team Marketplaces → Add Marketplace → Import from Repo, pointing it ataws/agent-toolkit-for-aws. Cursor indexes the plugins listed in.cursor-plugin/marketplace.jsonon import.

Then open thePluginspanel and install theaws-coreplugin (start here), oraws-agentsandaws-data-analyticsas needed. Each plugin bundles the AWS MCP Server configuration and agent skills.

### Kiro

Add the AWS MCP Server to your Kiro MCP configuration (.kiro/settings/mcp.json):

{
 
"mcpServers"
: {
 
"aws"
: {
 
"command"
: 
"
uvx
"
,
 
"args"
: [
 
"
mcp-proxy-for-aws@1.6.0
"
,
 
"
https://aws-mcp.us-east-1.api.aws/mcp
"
,
 
"
--metadata
"
, 
"
AWS_REGION=us-west-2
"

 ]
 }
 }
}

Note:It is recommended to pin to a specific version (e.g.,@1.6.0) to ensure reproducible behavior and protect against supply chain risks. We recommend regularly checkingPyPIfor new stable versions and updating accordingly.

Then install skills from this repository:

npx skills add aws/agent-toolkit-for-aws/skills

Prerequisites:You needuvinstalled. An AWS account with credentials configured locally is required for API calls and script execution, but not for documentation search or skill discovery. See theuser guidefor detailed setup instructions.

### Other agents

See theAWS MCP Server getting started guidefor instructions on configuring the AWS MCP Server with your agent.

Then install skills from this repository:

npx skills add aws/agent-toolkit-for-aws/skills

Prerequisites:You needuvinstalled. An AWS account with credentials configured locally is required for API calls and script execution, but not for documentation search or skill discovery. See theuser guidefor detailed setup instructions.

## What's included

### Plugins

Plugins bundle the AWS MCP Server configuration and agent skills into a single install for your coding agent.

Plugin

Description

aws-core

Core AWS skills and MCP Server configuration. Covers service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, and deployment. 
Start here.

aws-agents

Skills for building AI agents on AWS with Amazon Bedrock and AgentCore.

aws-data-analytics

Skills for data lake, analytics, and ETL workflows with S3 Tables, AWS Glue, and Athena.

Plugins are currently available for Claude Code, Codex, and Cursor. For other agents, configure the AWS MCP Server directly and install skills from this repository.

### Skills

Agent skills are curated packages of instructions and reference materials that help agents complete specific AWS tasks. Skills are loaded on demand — agents discover and retrieve only what's relevant to the current task.

npx skills add aws/agent-toolkit-for-aws/skills

Browse theskills/directory to see all available skills.

### Rules files

Recommended project-level configuration files that tell agents how to use AWS most effectively — for example, by using the AWS MCP Server, discovering available skills, or searching documentation before acting.

Seerules/for details.

### AWS MCP Server

TheAWS MCP Serveris a managed server that gives agents access to AWS through the Model Context Protocol. It provides:

* Full AWS API coverage— Interact with any of the 300+ AWS services through a single authenticated endpoint.
* Sandboxed script execution— Agents can run Python scripts in an isolated environment for complex multi-step operations.
* Real-time documentation access— Search and retrieve current AWS documentation, API references, and service capabilities without authentication.
* Enterprise controls— Amazon CloudWatch metrics, IAM context keys for agent-specific policies, and AWS CloudTrail audit logging.

For details on operation, available tools, authentication, and supported Regions, see theAWS MCP Server documentation.

## Documentation

* User guide— Setup, configuration, and reference documentation.
* AWS MCP Server tools— Reference for all available MCP tools.

## How the Agent Toolkit relates to the MCP servers, skills, and plugins in AWS Labs

In 2025, AWS began releasing MCP servers, skills, and plugins as part ofAWS Labs. The Agent Toolkit for AWS is the successor to those tools. We recommend using the Agent Toolkit for AWS, because it offers key features including:

* IAM condition keys that distinguish between agent actions and human actions, so you can write policies that apply only to agents. For example, you can write policies that only allow read-only actions through the MCP server, even if the user’s underlying IAM role can take write actions).
* CloudWatch metrics and CloudTrail audit logging for every request, so you can monitor and audit coding agent activity.
* Agent skills that have undergone thorough end-to-end evaluations, so you can be confident that workflows will complete successfully.

AWS LabsMCP servers, skills, and plugins will continue to work and accept contributions, and over time the best of AWS Labs will be transitioned to the Agent Toolkit for AWS to ensure that customers can access the broadest array of tooling and guidance for their agents.

## License

This project is licensed under the Apache-2.0 License. SeeLICENSEfor details.

## About

Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS

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

847

 stars
 

### Watchers

8

 watching
 

### Forks

77

 forks
 

 Report repository

 

## Releases

No releases published

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python93.9%
* TypeScript3.7%
* Shell2.4%

 Generated from 
amazon-archives/__template_Apache-2.0