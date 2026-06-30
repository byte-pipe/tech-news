---
title: Alert with SQL in Cloud Monitoring Observability Analytics | Google Cloud Blog
url: https://cloud.google.com/blog/products/management-tools/alert-with-sql-in-cloud-monitoring-observability-analytics/
site_name: tldr
content_file: tldr-alert-with-sql-in-cloud-monitoring-observability-a
fetched_at: '2026-06-30T11:56:16.257595'
original_url: https://cloud.google.com/blog/products/management-tools/alert-with-sql-in-cloud-monitoring-observability-analytics/
date: '2026-06-30'
description: Cloud Monitoring Observability Analytics lets you create alerts from (and get alerted about) analytical SQL queries of logs and traces.
tags:
- tldr
---

Management Tools

# From query to action: Introducing SQL alerting in Cloud Monitoring Observability Analytics

June 26, 2026

##### Joy Wang

Senior Product Manager

##### Mark Stahl

Staff software engineer

##### Try Gemini Enterprise Business Edition today

The front door to AI in the workplace

Try now 

Traditional alerting systems often force a compromise: you can either alert immediately on simple, noisy log events, or monitor rigid, pre-configured metrics that fail when faced with data with many unique answers like user sessions or IP addresses. But the most critical system issues — like a 20% spike in error rates for a specific customer or a latency anomaly correlated with database timeouts — are hidden in the aggregates and relationships between these signals.

Recently,we announcedthat you can now use SQL to query logs and traces inObservability Analytics(formerly Log Analytics). But the story gets better. You can also use SQL to create alertsin Observability Analytics. By bringing SQL directly to your alerting engine, you can write complex analytical queries over logs and traces and turn them into alerts. Whether you need to calculate error percentages, analyze high-cardinality dimensions, or JOIN logs and traces, SQL alerting helps you go from basic threshold monitoring to deep, contextual detection that goes beyond the capabilities of traditional alerting systems. SQL alerting is now in preview.

### How SQL-based alerting works

SQL alerting in Observability Analytics is available as part ofCloud Monitoring. An alerting policy runs your SQL query on a schedule you define (for example, every 10 minutes). It automatically applies a "lookback window" to your query, so it only analyzes the log entries or trace spans it received since the last time it ran.

If the results of your query meet the condition you set, Cloud Monitoring creates an incident and sends a notification to your chosen channels, like email, Slack, or PagerDuty.

Please note that because SQL-based alerting uses BigQuery to process telemetry data, query executions are billed through BigQuery under your standard on-demand pricing or BigQuery reservations.

### Two ways to trigger an alert

You can choose between two types of alert conditions.

1. Row count threshold:This is the simplest option. The alert fires if your query returns a number of rows that is greater than, equal to, or less than a threshold you set. This is perfect for "alert me if more than 10 users have failed logins" scenarios.
2. Boolean:This is the most powerful option. The alert fires if your query returnsanyrow where a specific column you define has a value of true. This lets you build complex logic, like calculating percentages, directly in your SQL query.

Example 1: Alerting on payment gateway failures (row count)

Scenario:Imagine that you’re an e-commerce operator, and you want to be alerted immediately if your payment gateway is experiencing systemic outages, while ignoring occasional, normal card declines (like an incorrect PIN).

To do this, you can write a query to filter for log entries indicating gateway timeouts, and use a row count threshold to trigger the alert only if the volume of these errors spikes.

Loading...
SELECT
 JSON_VALUE(json_payload.transaction_id) AS transaction_id,
 JSON_VALUE(json_payload.error_code) AS error_code
FROM
 `my-project-id.my-dataset.my-log-view`
WHERE
 JSON_VALUE(json_payload.status) = 'FAILED'
 -- Filter for systemic gateway issues, not user-input errors like WRONG_PIN
 AND JSON_VALUE(json_payload.failure_reason) = 'GATEWAY_TIMEOUT'

Alert configuration:

* Condition type: Row count threshold
* Trigger condition: Fired when row counts greater than (>) 10
* Evaluation window / lookback: 5 minutes (checks the last 5 minutes of data on your defined schedule)

Example 2: Alerting on agent latency (traces)

Scenario:You’re an AI platform engineer, and you want to ensure your multi-step AI agents are responding within acceptable time limits. You want to monitor the 99th percentile (p99) latency of the orchestrator service and get alerted if performance degrades.

To do this, you can write a SQL query against your trace data that calculates the p99 latency for all services and returnstrueif youragent-orchestratorexceeds 5 seconds (5000 milliseconds).

Loading...
WITH latency_data AS (
 SELECT
 APPROX_QUANTILES(duration_nano, 100)[OFFSET(99)] / 1000000 AS p99_ms
 FROM
 `my-project-id.us._Trace.Spans._AllSpans`
 WHERE
 -- Examine rows produced by the agent-orchestrator
 JSON_VALUE(resource.attributes, '$."service.name"') = 'agent-orchestrator'
 GROUP BY
 service_name
)
SELECT
 "agent-orchestrator" AS service_name,
 p99_ms,
 -- Boolean logic: Alert if p99 exceeds 5000ms
 (p99_ms > 5000) AS has_latency_spike
FROM
 latency_data

Alert configuration:

* Condition type: Boolean
* Target column:has_latency_spike
* Trigger condition: Fired when the query returns any row where this column evaluates to true.
* Evaluation window / lookback: 10 minutes (or your preferred scheduling interval)

### Before you begin

Before you can create a SQL-based alert, you need to set up a few things:

1. Analytics enabled:
2. Linked BigQuery dataset:Create a linked BigQuery dataset for the telemetry source (either thelog bucketor thetrace dataset). SQL-based alerts query the data through this BigQuery link.
3. IAM permissions:
4. Notification channels:Configure the notification channels(like email or Slack) where you want to receive alerts.

### How to create your alert

Creating asql-based alert policyis straightforward:

1. Navigate toObservability Analyticsin the Google Cloud console.
2. Compose and validate your SQL query.
3. Select theRun on BigQueryquery engine in the UI.
4. Click theCreate alertbutton from the results toolbar.
5. Define your condition (row count or boolean) and your evaluation schedule.
6. Add your notification channels, give your alert a clear name, and clickSave.

ForInfrastructure as Code (IaC) pipelines, you can also configure alerts via theAPIandTerraform.

### Get started

Ready to build more powerful, insightful alerts? Open theObservability Analyticspage in the console and try writing your first SQL query today. You can find more details and advanced examples in theofficial documentation.

Posted in
* Management Tools
* DevOps & SRE

##### Related articles

Management Tools

### Log Analytics is now Observability Analytics: Query logs and traces with SQL

By Joy Wang • 5-minute read

Databases

### Meet the latest Database Center, now with Gemini-powered fleet intelligence

By Kiran Shenoy • 5-minute read

Application Development

### Gemini Cloud Assist: Proactive cloud operations that work for you, even before you ask

By Michael Bachman • 5-minute read

Management Tools

### Unified Maintenance: A new, unified way to manage maintenance across Google Cloud

By Erol-Valeriu Chioasca • 2-minute read