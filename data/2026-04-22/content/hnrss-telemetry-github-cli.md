---
title: Telemetry | GitHub CLI
url: https://cli.github.com/telemetry
site_name: hnrss
content_file: hnrss-telemetry-github-cli
fetched_at: '2026-04-22T20:04:40.692154'
original_url: https://cli.github.com/telemetry
date: '2026-04-22'
description: Take GitHub to the command line
tags:
- hackernews
- hnrss
---

# Telemetry

GitHub CLI sends pseudonymous telemetry to help us improve the product. We want you to understand what is being sent and why.

## Why we collect telemetry

As agentic adoption of GitHub CLI grows, our team needs visibility into how features are being used in practice. We use this data to prioritize our work and evaluate whether features are meeting real user needs.

For example, when we ship a new subcommand, we want to understand whether anyone is using it and how. If adoption is low, we know we need to revisit the feature's discoverability or design. If a subcommand sees high usage with certain flags, that tells us where to invest in a better experience.

## Reviewing telemetry

GitHub CLI is open source, you can review the telemetry implementation in thecli/clirepository. However, if you want to see exactly what would be sent without actually sending it, you can enable logging mode using either an environment variable, or configuration option.

Environment variable:

export GH_TELEMETRY=log

CLI config:

gh config set telemetry log

In logging mode, the JSON payload that would normally be sent is printed to stderr instead. This lets you inspect every field before deciding whether to keep telemetry enabled, for example:

GH_TELEMETRY=log gh repo list --archived

prints something like:

Telemetry payload:
{
 "events": [
 {
 "type": "command_invocation",
 "dimensions": {
 "agent": "",
 "architecture": "arm64",
 "command": "gh repo list",
 "device_id": "1e9a73a6-c8bd-4e1e-be02-78f4b11de4e1",
 "flags": "archived",
 "invocation_id": "eda780f5-27f9-433c-a7ae-7a033361e572",
 "is_tty": "true",
 "os": "darwin",
 "timestamp": "2026-04-16T14:55:13.418Z",
 "version": "2.91.0"
 }
 }
 ]
}

Note that this command can only log telemetry for the exact command and context in which it ran. For example, changing environment variables, or authenticated accounts may change the events, and event dimensions that are included in the payload.

## How to opt out

You can opt-out of the telemetry you see in the aforementionedlogmode using either an environment variable, or configuration option.

Environment variables:

export GH_TELEMETRY=false

Any falsy value works:0,false,disabled, or an empty string. You can also use theDO_NOT_TRACKconvention:

export DO_NOT_TRACK=true

CLI config:

gh config set telemetry disabled

Note:The environment variables take precedence over the config value.

## Where data is sent

Telemetry events are sent to GitHub's internal analytics infrastructure. For more information about how GitHub handles your data, see theGitHub General Privacy Statement.

## Additional information

GitHub CLI allows you to add features to the product by installing GitHub and third-party extensions, including agents. These extensions may be collecting their own usage data and are not controlled by opting out. Consult the specific extension's documentation to learn about its telemetry reporting and whether it can be disabled.

This page describes client-side data collection for the GitHub CLI (gh). It does not apply to GitHub Copilot or the Copilot CLI, which handle data collection separately. For information on the Copilot CLI, seeUsing GitHub Copilot CLIandResponsible Use of the GitHub Copilot CLI.