---
title: Chat with Your App Service Logs Using GitHub Copilot | Microsoft Community Hub
url: https://techcommunity.microsoft.com/blog/appsonazureblog/chat-with-your-app-service-logs-using-github-copilot/4491573
site_name: tldr
content_file: tldr-chat-with-your-app-service-logs-using-github-copil
fetched_at: '2026-02-21T19:11:02.334044'
original_url: https://techcommunity.microsoft.com/blog/appsonazureblog/chat-with-your-app-service-logs-using-github-copilot/4491573
date: '2026-02-21'
description: The Problem We know that logs and observability on App Service can be tricky—it's feedback we hear from customers all the time. There are many sources of...
tags:
- tldr
---

## Blog Post

Apps on Azure Blog
7 MIN READ

# Chat with Your App Service Logs Using GitHub Copilot

jordanselig
Microsoft
Feb 06, 2026

## TL;DR: We built an open-source MCP server that lets GitHub Copilot (and other AI assistants) directly query your App Service logs, analyze errors, and help you debug issues—all through natural language conversation.

## The Problem

We know that logs and observability on App Service can be tricky—it's feedback we hear from customers all the time. There are many sources of information: Kudu container logs, Log Analytics tables (AppServiceHTTPLogs, ConsoleLogs, PlatformLogs, AppLogs), deployment logs, metrics, and more. It's not always obvious where to look, especially when you're troubleshooting under pressure.

Today, debugging production issues often involves:

1. Opening the Azure Portal
2. Figuring out which blade or log source has the information you need
3. Navigating to Log Analytics and remembering (or searching for) the right KQL syntax
4. Interpreting results and manually correlating across multiple log tables
5. Repeating this process until you find the root cause

This proof-of-concept is one of our attempts to simplify this experience,using AI to bridge the gap between your question and the answer—no matter where that answer lives.

What if you could just ask:"Why did my app stop?"and get an answer without ever having to leave your IDE or terminal?

## The Solution: App Service Observability MCP Server

We've built a proof-of-conceptMCP (Model Context Protocol)server that exposes App Service observability tools directly to AI assistants like GitHub Copilot in VS Code. It can be accessed from your preferred IDE like VS Code, or directly in your CLI such as GitHub Copilot CLI or Claude Code. You now don't even have to leave your coding environment to get answers to your App Service issues.

Key capabilities:

* Query logsfrom Log Analytics (HTTP logs, Console logs, Platform logs)
* Fetch container logsdirectly from Kudu (no setup required!)
* Analyze HTTP errorsgrouped by status code and endpoint
* Find slow requestsexceeding latency thresholds
* Diagnose deployment issues— automatically correlate deploys with startup failures and errors
* Check logging setup— runtime-specific recommendations (Python, Node.js, .NET, Java)
* View deployment historyand correlate with issues
* Investigate container restartsand identify root causes

## Demo

To see how the tool works, here are a series of screenshots going over a real-world scenario where a deployment issue breaks an app. The first screenshot is from when the app was functioning with no issues. You can see the tool calls one of MCP tools to get the app info.

I then asked if there were any issues. It found a couple issues early on, but they were all transient and after reviewing logs and errors, it determined the app was functional.

I then introduced a bug into my app and redeployed. I changed the name of a reference to a config file to one that didn't exist, thereby causing the app to crash because it was trying to load a file that didn't exist. GitHub Copilot was easily able to pick up the issue based on the deployment logs tooling. Also, because GitHub Copliot has direct access to my codebase for the app it was analyzing, it was able to see that the file that I was referencing didn't exist and knew what to change it to to get the app working again. This is one of the benefits of running this tool locally alongside your codebase - in addition to the tooling, it can also keep an eye on your codebase. Now if you've ever used GitHub Copilot to help deploy one of your apps, you may know that it can natively make calls using the Azure CLI for example to pull logs. But in my experience, these actions don't always work, take multiple attempts, and take a significant amount of time to complete. With the tooling and skills here, this operation becomes seamless because the agent knows exactly what to do and how to do it. It takes away the guesswork and multiple attempts that an agent without this tool would have to go through.

In the following screenshot, I asked why the deployment was taking so long. Usually a deployment with azd for an app like the demo app here takes under a minute, so I wanted it to help me understand what the delay was caused by. Within a couple seconds, it was able to pickup the bug I introduced.

Lastly, I then asked it to correlate the error with a deployment. One of the major problem areas our customers have is determining which deployment led to a specific error. We've built a tool into this feature that can correlate deployements and errors. Here's what the tool found. You can see I did a couple deployments with config file names that didn't exist. The tool was able to pinpoint the exact deployments that caused the issue and also tell me what to change to remediate the issue. This is a major benefit that was only possible with the help of AI and it's reasoning capabilities.

## How It Works

The MCP server sits between your AI assistant and Azure, translating natural language requests into API calls:

Important:Some tools require Log Analytics diagnostic settings to be enabled, but `get_recent_logs` and `get_deployments` work out of the box by calling Kudu and ARM directly.

## Security: Your Credentials, Your Access

A common question when connecting AI tools to cloud resources:"What access does this have?"

The MCP server here uses `DefaultAzureCredential` from the Azure SDK, which means it leverages your existing Azure identity—typically from `az login`.It can only access resources you already have permission to access.There are no stored secrets, no service principals with elevated privileges, and no additional credentials required.

In other words: if you could run the investigation yourself in the portal or via Azure CLI, the MCP server can do it. If you don't have access to a resource, neither does the server.

This design ensures:

* No privilege escalation— The AI operates with your exact permissions
* Existing RBAC applies— Your organization's access controls are respected
* Audit trail intact— All API calls use your identity and appear in Azure activity logs

Looking ahead:For production scenarios with fully autonomous agents (running unattended or on a schedule), you'd want to apply least-privilege principles—create a dedicated service principal or managed identity with only the specific permissions needed (e.g., Reader on the App Service, Log Analytics Reader on the workspace). This limits blast radius and follows security best practices for any automated system accessing cloud resources.

## The Agent Skill: Domain Expertise for Debugging

Beyond just exposing tools, we've included anAgent Skillfile (SKILL.md) that gives the AI domain expertise for App Service debugging.

### What's an Agent Skill?

Agent Skillsare markdown files that provide structured knowledge to AI assistants. When GitHub Copilot has access to our SKILL.md, it gains:

* Debugging workflows— Step-by-step approaches for investigating issues
* Common error patterns— OOM crashes, Always On issues, HTTP 500/503 errors
* KQL query templates— Ready-to-use queries for each scenario
* SKU reference— Which features are available on each pricing tier
* Best practices— How to present findings with actionable recommendations

### Tools + Knowledge = Better Debugging

The MCP tools and Agent Skill work together:

Component
Role
MCP Tools
Fetch real data from your Azure resources
Agent Skill
Interpret results and guide investigations

For example, when investigating a container restart, the Agent Skill teaches Copilot to:

1. Check for OOM patterns in platform logs
2. Look for crash loops vs. graceful terminations
3. Consider Always On settings based on the SKU
4. Provide the right `az` command to fix the issue

## Example: Investigating a Container Stop

Here's a real conversation showing AI-assisted debugging:

User:"Show me the recent logs"

Copilot:calls get_recent_logs

2026-01-30T19:52:42Z Container start method called.

2026-01-30T19:52:43Z Container is running.

2026-01-30T19:52:57Z Site started.

2026-01-30T19:53:17Z Container is terminating. Grace period: 5 seconds.

2026-01-30T19:53:22Z Site stopped.

Copilot:The site started but stopped after 20 seconds. Want me to investigate?

User:"Please investigate"

Copilot:calls check_diagnostics, get_http_errors, query_logs, get_app_info

Root Cause:Your container is stopping because"Always On" is disabled. With low traffic (only 14 requests in 24 hours), App Service terminates idle containers to save resources.

Evidence:

* ✅ No errors in platform or application logs
* ✅ No HTTP 5xx errors
* Container terminated gracefully (not a crash)

Fix:

az webapp config set --name your-app --resource-group your-rg --always-on true

Note: Requires Basic tier or higher.

No portal. No manual KQL. Just ask and get answers.

## Getting Started

### Prerequisites

* Node.js 20+
* Azure CLI (`az login` for authentication)
* VS Code with GitHub Copilot

### Installation

git clone https://github.com/seligj95/app-service-observability-agent.git
cd app-service-observability-agent
npm install && npm run build

### Configure VS Code

Create `.vscode/mcp.json` in your workspace:

{
 "servers": {
 "appservice-logs": {
 "command": "node",
 "args": ["/path/to/app-service-observability-agent/dist/index.js"],
 "type": "stdio",
 "env": {
 "AZURE_SUBSCRIPTION_ID": "your-subscription-id",
 "AZURE_RESOURCE_GROUP": "your-resource-group",
 "AZURE_APP_NAME": "your-app-name"
 }
 }
 }
}

Reload VS Code, click "Start" next to the server, and start chatting with Copilot about your App Service!

## What's Next?

This is aproof-of-conceptdemonstrating what an App Service AI observability tool could look like. We're exploring how this pattern could become a first-class feature of the platform.

Imagine a future where every App Service has a built-in MCP endpoint for observability:https://my-app.scm.azurewebsites.net/mcp.

Stay tuned for part 2 of this blog where we will show how to host this tool on App Service so that not just you, but you're whole team can leverage this tool for your workloads.

## Try It Out

* GitHub Repo:github.com/seligj95/app-service-observability-agent
* Agent Skill:Check outSKILL.mdfor the debugging knowledge base

We'd love your feedback! Use the comments below or open an issue or PR if you have ideas for additional tools or debugging patterns.

Updated
Feb 06, 2026
Version 1.0
azure app service
web apps
Comment
Comment
jordanselig
Microsoft
Joined
October 14, 2021
Send Message
View Profile
Apps on Azure Blog
Follow this blog board to get notified when there's new activity
