---
title: Analyzing Claude Code usage with CloudWatch and OpenTelemetry | AWS Cloud Operations Blog
url: https://aws.amazon.com/blogs/mt/analyzing-claude-code-usage-with-cloudwatch-and-opentelemetry/
site_name: tldr
content_file: tldr-analyzing-claude-code-usage-with-cloudwatch-and-op
fetched_at: '2026-06-26T19:36:16.620554'
original_url: https://aws.amazon.com/blogs/mt/analyzing-claude-code-usage-with-cloudwatch-and-opentelemetry/
date: '2026-06-26'
published_date: '2026-06-17T07:45:49-07:00'
description: Analyzing Claude Code usage with CloudWatch and OpenTelemetry (6 minute read)
tags:
- tldr
---

## AWS Cloud Operations Blog

# Analyzing Claude Code usage with CloudWatch and OpenTelemetry

If your engineering organization uses AI coding agents like Claude Code, usage is likely growing faster than your ability to track it. Token consumption, cost per team, and developer productivity are questions that existing dashboards don’t answer, because the telemetry never made it to your observability backend.

With Amazon CloudWatch OpenTelemetry Protocol (OTLP) inGeneral Availability, metrics ingestion is now possible with bearer token authentication. This means, tools that emit OTLP can typically ship metrics directly to CloudWatch with a single authorization header. No collectors, no sidecars, no IAM credential wiring on developer machines. Connect the signals in minutes and get per-developer cost attribution, team-level usage analytics, and operational alerting, all queryable with Prometheus Query Language (PromQL).

This post walks through the end-to-end setup for Claude Code. Although the focus here is Claude Code, comprehensive guidance for OpenAI Codex and GitHub Copilot is available on theAWS Observability best practices. This post focuses on bearer token authentication for its simplicity on developer machines. For organizations that require SSO (Single Sign-On) or OIDC (OpenID Connect) for developer authentication, see theguidance repositoryfor federated identity patterns and token refresh helpers.

# Bearer token authentication

Bearer tokens (or CloudWatch metrics API key) allow tools running outside AWS (like Claude Code on developer laptops) to send metrics to CloudWatch without requiring the AWS SDK or IAM credential chains. Each token is tied to an AWS IAM user scoped exclusively to theCloudWatchAPIKeyAccessmanaged policy.

Important:Bearer tokens are long-term credentials. This post uses bearer tokens because AI coding agents run on developer laptops outside of AWS. SigV4 authentication would require either a central collector or running a collector process on every developer machine. Both approaches add operational complexity. Bearer tokens eliminate that infrastructure requirement entirely. For workloads running inside AWS where SigV4 with short-term credentials is feasible, prefer that approach for a stronger security posture. The CloudWatch OTLP endpoint requires HTTPS; requests over plain HTTP are rejected. For more information, seeCloudWatch OTLP Metrics Bearer Token Auth.

## Granularity strategy

Organizations control how granular their telemetry attribution is based on how they provision bearer tokens. At the finest level, each developer gets their own IAM user and bearer token, so attribution is inherent to the token itself. At a coarser level, a single token can be shared across a team or an entire organization, with identity attribution handled through client-side resource attributes instead. The following diagram illustrates these three approaches:

Figure 1: Token granularity strategy options

All three approaches produce identical dashboards and PromQL queries because attribution is driven by resource attributes, not the token itself. Start with a single shared token to validate the pipeline, then split to per-team or per-developer tokens as your security posture demands. Per-developer tokens are recommended when compliance requires credentials traceable to a named individual or when clean offboarding (revoking a single IAM user) is a hard requirement.

# Prerequisites

* An AWS account with permissions to create CloudWatch resources
* AWS CLI v2 installed and configured
* Latest Claude Code version
* A CloudWatch metrics API key (generated below)

## Create a bearer token via the console

In the CloudWatch console, navigate toSettingsunder theSetupsection.

1. Scroll toAPI Keys.
2. ChooseCreate.
3. Select anAPI key expiration.

CloudWatch creates the associated IAM user on your behalf with theCloudWatchAPIKeyAccesspolicy attached.

Figure 2: Creating a bearer token in the CloudWatch console Settings page.

## Create a bearer token via the CLI

Alternatively, create a token with the CLI using the following commands:

# Create an IAM user for CloudWatch metrics ingestion
aws iam create-user --user-name cloudwatch-metrics-api-key-user

# Attach the CloudWatchAPIKeyAccess managed policy
aws iam attach-user-policy \
 --user-name cloudwatch-metrics-api-key-user \
 --policy-arn arn:aws:iam::aws:policy/CloudWatchAPIKeyAccess

# Create a service-specific credential for CloudWatch metrics ingestion
aws iam create-service-specific-credential \
 --user-name cloudwatch-metrics-api-key-user \
 --service-name cloudwatch.amazonaws.com

The response includes theServiceCredentialSecretfield, which is the bearer token value. Store it securely inAWS Secrets Manageror your organization’s vault solution. A reminder that you should never commit the token to version control. For automated key rotation, useAWS Secrets Manager rotation with a Lambda function.

# Client-side configuration

With the bearer token set up, you can now configure Claude Code to export metrics. This approach uses client-side resource attributes set by each developer (or distributed via profile management).

# Retrieve token from Secrets Manager
BEARER_TOKEN=$(aws secretsmanager get-secret-value \
 --secret-id cloudwatch-otlp-bearer-token \
 --query SecretString \
 --output text)

export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json
export OTEL_EXPORTER_OTLP_ENDPOINT="https://monitoring.<AWS_REGION>.amazonaws.com"
export OTEL_RESOURCE_ATTRIBUTES="user.id=$(whoami),user.email=${USER_EMAIL},team.id=${TEAM:-engineering},cost_center=${COST_CENTER:-default},department=${DEPARTMENT:-engineering},environment=${ENV:-dev}"

# Security Note: Environment variables can be exposed through process listings and shell history.
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer ${BEARER_TOKEN}"

# control export frequency (2s, for testing)
export OTEL_METRIC_EXPORT_INTERVAL=2000

Replace<AWS_REGION>with your target Region (for example,us-east-1,eu-west-1).

TheOTEL_RESOURCE_ATTRIBUTESline attaches identity dimensions to every metric. Developers set these attributes directly. They become the PromQL labels for filtering and grouping in dashboards and alerts. Use whatever attributes your organization needs. The key requirement is consistency across your fleet so aggregations work.

Attribute

PromQL label

Purpose

Example

user.id

@resource.user.id

Per-developer attribution

jdoe

user.email

@resource.user.email

Per-developer attribution (email)

jdoe@acme.com

team.id

@resource.team.id

Team-level aggregation

platform-eng

cost_center

@resource.cost_center

Finance/chargeback grouping

CC-4200

department

@resource.department

Org-level rollup

engineering

environment

@resource.environment

Distinguish dev/staging/prod usage

production

You can find the full list of standard attributes and metrics available in theClaude Code documentation.

For fleet-wide enforcement of telemetry settings and privacy controls, Claude Code supportsadmin-managed settingsdeployable through your organization’s profile management solution.

# Verify metrics are flowing

After setting the environment variables, run a short Claude Code session:

# Start a brief session
claude -p "Let's conquer the world" --max-turns 1

To verify metrics are flowing, openCloudWatch Query Studioand enterclaude_. You will see a few metrics such asclaude_code.token.usagewhich tracks the number of tokens used.

Figure 3: Verifying metrics ingestion in CloudWatch Query Studio.

# Sample usage dashboard

Regardless of the granularity strategy described previously, aCloudWatch dashboardis available that uses PromQL to query Claude Code telemetry data. As long as your resource attributes follow the semantic conventions described in the client-side configuration section, all values appear in the dashboard automatically.

Deploy the pre-built dashboard:

# Download the dashboard definition
curl -o claude-code-dashboard.json \
 
https://raw.githubusercontent.com/aws-observability/aws-observability-accelerator/main/artifacts/cloudwatch-dashboards/claude-code/claude-code.json

aws cloudwatch put-dashboard \
 --dashboard-name claude-code-usage \
 --dashboard-body file://claude-code-dashboard.json \
 --output off \
 --region <AWS_REGION>

Verify the dashboard was created:

aws cloudwatch list-dashboards --dashboard-name-prefix claude-code --region <AWS_REGION>

The dashboard is organized into five sections. It starts with a high-level summary so stakeholders can assess overall health at a glance, then progressively drills into token economics, developer activity, organizational cost allocation, and infrastructure health.

## Overview

The top row provides a summary including total tokens consumed, active users, total sessions, and cache hit rate. Select the Region where you configured to send OTel metrics to Amazon CloudWatch.

Figure 4: Overview summary cards showing total tokens, active users, sessions, and cache hit rate.

## Token usage

This section answers the question engineering leaders ask first: “How much are we consuming, and where is it going?”. It breaks down token consumption over time, by type (input, output, cache read, cache creation), by model, by user, and by estimated cost. Use these panels to identify which models are driving spend and which users are the heaviest consumers.

Figure 5: Token usage section showing consumption over time, breakdown by type, usage by model, top users, estimated cost per user, and active users over time.

## Developer productivity

Beyond cost, this section tracks what developers are actually producing with the tool: lines of code added and removed, commits, active coding hours, pull requests created, and code edit patterns. The language breakdown pie chart reveals which parts of the codebase benefit most from AI assistance. The code edit decisions panel (accept vs reject) is a signal of how well the agent’s suggestions align with developer intent.

Figure 6: Developer productivity metrics showing lines of code, commits, active hours, pull requests, language distribution, and code edit accept/reject rates.

## Organizational breakdown

For organizations with multiple teams or departments, this section provides the cost allocation view. These panels map directly to thedepartmentandteam.idresource attributes configured in the client-side configuration section. Use them for chargeback, budget planning, and identifying which parts of the organization are adopting the tool most effectively.

Figure 7: Organizational breakdown showing token usage by department and by team.

## Amazon Bedrock API health

If you are usingAmazon Bedrock as the backend for Claude Code, the dashboard also includes infrastructure health panels. These show throttle events, client errors, and server errors broken down by model. Use them to correlate developer-reported issues (slow responses, failed requests) with upstream API behavior.

# Alerting

Every panel in the dashboard is backed by a PromQL query. To create an alarm from any panel:

1. Open the panel you are interested in (for example, token usage by user).
2. To open the underlying query, chooseView in Query Studio.
3. ChooseCreate alarmdirectly from Query Studio.
4. Adjust the query or thresholds as needed.

You can also write custom PromQL alarm queries for scenarios that go beyond what the dashboard shows. Here are a few examples:

## Individual spend spike

If someone spends more in 1 hour than 2x their entire previous day’s spend, that indicates an anomaly. This catches runaway loops, stuck agents, or compromised tokens.

sum by("@resource.user.email") (increase({"claude_code.cost.usage"}[1h]))
> 2 * avg_over_time(sum by("@resource.user.email") (increase({"claude_code.cost.usage"}[1h]))[24h:1h])

Figure 8 – PromQL alarm for user usage in 1h greater than his daily usage

## Team budget threshold

Alert when a team’s daily spend exceeds a defined budget:

sum by ("@resource.team.id") (increase({"claude_code.cost.usage"}[24h])) > 500

## Adoption regression

Detect when a team’s daily sessions drop below 50% of their 7-day average, a signal of potential tooling issues or access problems:

sum by ("@resource.team.id") (increase({"claude_code.session.count"}[1d]))
< 0.5 * avg_over_time(sum by ("@resource.team.id") (increase({"claude_code.session.count"}[1d]))[7d:1d])

# Using the dashboard in Amazon Managed Grafana

If you use Amazon Managed Grafana or self-managed Grafana, follow thequery from Grafana documentationto add CloudWatch as a PromQL data source, then import theGrafana dashboard JSON.

# Cost estimate

For a 200-developer organization where each developer runs ~20 sessions per day, each emitting ~7 metric data points with resource attributes, and developers are active ~22 days/month:

A typical OTLP data point with 10-15 attributes is 300-600 bytes. Using 450 bytes as a midpoint:

200 developers × 20 sessions/day × 7 metrics × 450 bytes = 12.6 MB/day
12.6 MB/day × 22 days = ~277 MB/month ≈ 0.27 GB/month

At$0.50/GBingestion, that is~$0.14/monthfor the base case. Even with high-cardinality metrics (100x volume), total ingestion stays under$14/month. PromQL queries in the CloudWatch console arefree.

The total cost for 200 developers, in this example, would beunder $15/month.

Visit theAmazon CloudWatch Pricing pagefor the latest updates.

# Cleanup

Important:CloudWatch retains metrics up to 15 months at no charge. Delete alarms and IAM resources to avoid ongoing costs and security exposure.

Follow these commands to remove all the resources you have created:

# Delete Dashboard
aws cloudwatch delete-dashboards --dashboard-names claude-code-usage --region <AWS_REGION>

# Delete CloudWatch Alarms
aws cloudwatch delete-alarms --alarm-names <alarm-name> --region <AWS_REGION>

# Delete service-specific credential
aws iam delete-service-specific-credential --user-name cloudwatch-metrics-api-key-user --service-specific-credential-id <credential-id>

# Detach policy from IAM user
aws iam detach-user-policy --user-name cloudwatch-metrics-api-key-user --policy-arn arn:aws:iam::aws:policy/CloudWatchAPIKeyAccess

# Delete IAM user
aws iam delete-user --user-name cloudwatch-metrics-api-key-user

# If using Secrets Manager, delete the secret
# WARNING: Deleting the secret is irreversible. The bearer token cannot be recovered.
# Ensure you no longer need the token before proceeding.
aws secretsmanager delete-secret --secret-id <secret-name> --region <AWS_REGION>

To stop telemetry export, unset the environment variables or remove them from your shell profile:

unset CLAUDE_CODE_ENABLE_TELEMETRY OTEL_METRICS_EXPORTER OTEL_EXPORTER_OTLP_ENDPOINT OTEL_EXPORTER_OTLP_HEADERS OTEL_RESOURCE_ATTRIBUTES

# Conclusion

In this post, you configured Claude Code to export OpenTelemetry metrics to Amazon CloudWatch using bearer token authentication, deployed a PromQL-powered dashboard for cost and usage visibility, and set up alerting for spend anomalies and adoption regression.

The same CloudWatch OTLP endpoint accepts telemetry from any OpenTelemetry-instrumented workload, not just IDE agents. For large organizations with multiple accounts and Regions, General Availability also introducedcross-account, cross-Region metrics centralization, which enables metrics collection into a single observability account for unified visibility.

Checkoutthe complete guideon how to setup IDE observability for GitHub Copilot, and OpenAI Codex.