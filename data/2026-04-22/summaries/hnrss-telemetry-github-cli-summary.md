---
title: Telemetry | GitHub CLI
url: https://cli.github.com/telemetry
date: 2026-04-22
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-22T20:08:16.310314
---

# Telemetry | GitHub CLI

# Telemetry Overview
GitHub CLI collects pseudonymous telemetry data to help improve the product and user experience. This data is used to understand adoption, feature usage, and other aspects of user behavior.

## Why Collect Telemetry
As GitHub CLI adoption grows, our team needs visibility into how features are being used in practice. We use this data to prioritize work and evaluate whether features meet real user needs.

## How Telemetry Works
GitHub CLI sends telemetry events as part of its operations. This data is captured using JavaScript code running on the GitHub backend server.

### Reviewing Telemetry
To view telemetry data, users can opt out or log mode being enabled in their `~/.ghrc` file. Logging mode displays a JSON payload that shows what telemetry events would be sent under the open source license.

### Logging Mode
In logging mode:

*   The original console output is preserved.
*   A new `stdout:disabled` configuration option allows inspection of every field before deciding to keep analytics enabled.

## Key Points

| Point        | Meaning                                       |
|--------------|------------------------------------------------|
| Telemetry purpose | Improving user experience and adoption           |
| Telemetry data type | JSON payload reflecting feature usage          |
| Logging mode   | Viewing telemetry in the open source environment  |
| Data storage    | Internal analytics infrastructure               |

## What's Possible
-   Opt out of telemetry (logging mode)
-   Disable telemetry by setting a configuration option
-   Add features and extensions with their own telemetry data