---
title: AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support | AWS News Blog
url: https://aws.amazon.com/blogs/aws/aws-glue-6-0-now-available-with-30-lower-price-and-full-apache-iceberg-v3-support/
date: 2026-08-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:05:54.514131
---

# AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support | AWS News Blog

# AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support

## Overview
- General availability announced; pricing 30 % lower than previous Glue versions.  
- Built on modern runtime: Apache Spark 4.1, Python 3.13, Scala 2.13.  
- Offers faster performance, simplified ETL authoring, improved PySpark speed, and real‑time streaming with single‑digit millisecond latency.

## New Iceberg v3 support
- Complete Apache Iceberg v3 implementation (Iceberg 1.11.0).  
- Introduces VARIANT data type with shredding, enabling faster reads of semi‑structured JSON, logs, and events without schema flattening.  
- Additional Iceberg capabilities:
  - Geometry and Geography types for native spatial analytics.  
  - Nanosecond‑precision timestamps for IoT, scientific, and high‑frequency financial data.  
  - Unknown type handling to tolerate evolving schemas without pipeline failures.

## Spark 4.1 runtime enhancements
- **Spark declarative pipelines**: engineers declare desired data shape; engine optimizes execution order automatically.  
- **Arrow‑native Python UDFs/UDTFs**: removes Python‑JVM serialization overhead, boosting PySpark transformation performance.  
- **Real‑time streaming mode**: stateless streaming with single‑digit millisecond latency, suited for low‑latency event processing and routing.

## Getting started
- No API changes; select version with `--glue-version` in create‑job or update‑job APIs (CLI, SDK, Glue Studio, SageMaker Unified Studio, IDEs).  
- In Glue Studio console: choose “Glue 6.0 – Supports Spark 4.1, Scala 2, Python 3” on the Job Details tab.  
- For notebooks/Jupyter: set `%glue_version 6.0`.  
- Upgrade existing jobs via Spark upgrade agent in Glue Studio or use auto‑upgrade feature.

## Availability & pricing
- Generally available in all AWS regions where Glue operates.  
- Hourly billing by the second for crawlers and ETL jobs; monthly fee for Data Catalog metadata (first 1 M objects and accesses are free).  
- Links to region availability, pricing page, and migration documentation provided.

## Feedback
- Users encouraged to try Glue 6.0 in the Glue Studio console and submit feedback via AWS re:Post or standard AWS support channels.