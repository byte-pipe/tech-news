---
title: 'Data-to-Production: Bridging the Gap Between Iceberg and Live Microservices'
url: https://www.wix.engineering/post/data-to-production-bridging-the-gap-between-iceberg-and-live-microservices
site_name: tldr
content_file: tldr-data-to-production-bridging-the-gap-between-iceber
fetched_at: '2026-02-22T19:11:31.097570'
original_url: https://www.wix.engineering/post/data-to-production-bridging-the-gap-between-iceberg-and-live-microservices
date: '2026-02-22'
published_date: '2026-02-17T11:04:08.008Z'
description: 'Data-to-Production: Bridging the Gap Between Iceberg and Live Microservices (7 minute read)'
tags:
- tldr
---

Search

At Wix, our Data Warehouse (DWH) is a massive repository of insights. Built on Amazon S3 using Apache Iceberg table formats, and populated by Trino and Spark jobs, it houses petabytes of data—from user segmentation and logs to AI chat analytics.

However, storage is only half the battle.

The real challenge—and the "holy grail" for many data engineering teams—isActivation: taking that petabyte-scale data and exposing it to backend microservices with millisecond latency, high availability, and strict type safety.

We call this initiativeData-to-Production.

In the last few months, we’ve built a platform that has already ingested billions of rows from varying Iceberg schemas into ClickHouse, serving critical features like AI Chat Analytics and User Segmentation. This blog details how we architected the system, the custom tooling we built to make it robust, and the lessons learned along the way.

### The Architecture: A Bird’s-Eye View

The system is designed to decouple the complexity of big data ingestion from the simplicity required by product engineers. It consists of three main pillars:

1. The MetaData Layer:A registration and governance layer where users define what data they need.
2. The Ingestion Engine (Airflow + Python):A dynamic, self-healing pipeline that moves data from S3/Iceberg to ClickHouse.
3. The Serving Layer (Scala):A type-safe JSON API that allows microservices to query ClickHouse securely.

### 1. The Metadata Layer: Registration & Governance

We didn't want to become a bottleneck where data engineers had to write customized ETL scripts for every new request. Instead, we built aSelf-Service Platform.

#### The Internal Self-Service Console

Product teams onboard their data using a custom user interface. Instead of writing DAGs, they provide a declarative configuration for their table including:

* Source:The Iceberg table location (S3 path/catalog info).
* Urgency:Is this a critical 24/7 production feature or a business-hours-only dashboard?
* Performance Tuning:Users must specify Sort Keys (crucial for ClickHouse performance), Partition Columns, and Primary Keys (for deduplication).
* Lifecycle:An optional TTL column to automatically expire old data.

#### Human-in-the-Loop Governance

While ingestion is automated, performance remains highly sensitive. A poorly defined sort key or indexing strategy can severely impact a ClickHouse cluster. To mitigate this, table registration is intentionally gated.

When a user registers a table, our team receives a Slack alert containing the proposed schema, partitioning, and indexing configuration. We review these choices before explicitly approving the table, ensuring that only performant, production-safe datasets are exposed to downstream services.

This human-in-the-loop model allows us to balance self-service velocity with cluster stability during the platform’s early and scaling phases. Looking ahead, we are actively working to automate these validations using rule-based checks and learned heuristics.

### 2. The Engine Room: Deep Dive into the Ingestion Pipeline

While the Serving Layer provides the polish, the Ingestion Engine is the heavy lifter. Moving petabytes of data reliably from a data lake (Iceberg on S3) to a real-time OLAP database (ClickHouse) is fraught with challenges: network timeouts, schema drift, data consistency, and idempotency.

#### Architecture: The "Configuration-as-Code" Approach

We moved away from writing custom DAGs for every table. Instead, we built aDynamic DAG Generator.

The process starts with theconfiguration service API. This service holds the metadata for every table we want to sync. Our Airflow environment polls this configuration and spins up Task Factories. These factories automatically construct the dependency chain for a table based on its requested Loading Method. This means a simple config change (e.g., switching from "Overwrite" to "Upsert") instantly changes the underlying pipeline logic without a single line of Airflow code being touched.

#### The Three Loading Strategies

We support three distinct loading patterns, each utilizing different ClickHouse engines and SQL operations to optimize for consistency and performance.

A. OVERWRITE (The Atomic Swap)

* Used for:Dimension tables, Lookup tables, and Full Refreshes.
* Staging:We create a temporary MergeTree table (table_staging).
* Load:We ingest the entire dataset from Iceberg/S3 into this staging table.
* Swap:We executeEXCHANGE TABLES target AND table_staging. This operation is atomic—queries running against the target continue to work on the old data until the millisecond the swap completes.
* Cleanup:The old data (now intable_staging) is dropped.

B. UPSERT (Incremental Deduplication)

* Used for:Mutable Fact tables (e.g., User Events where properties might update) or dimension tables.
* We utilize theReplacingMergeTreeengine, which deduplicates data in the background based on the Sorting Key.
* Watermark Detection:The pipeline queries the target table forMAX(watermark_column).
* Delta Load:We construct a query to the Trino/Iceberg source:SELECT * FROM source WHERE updated_at > {max_watermark}.
* Insert:Only these new/modified rows are inserted into ClickHouse.
* Schema Evolution:If the pipeline detects a schema change (e.g., a new column), it automatically escalates this run to a Full Reload viaEXCHANGE TABLESto ensure the new schema is applied historically.

C. PARTITION_REPLACE

Used for:Fact tables, Immutable Logs, Event Streams, and Time-Series data. This is our most complex but efficient strategy.

* Surgical Replacement:Instead of a generic insert, we useALTER TABLE target REPLACE PARTITION {id} FROM staging. This atomically swaps out specific blocks of time (e.g., specific hours or days), ensuring perfectly consistent historical data.
* The Catch-Up Logic:If a DAG fails or is paused for several hours, the target table falls behind. The system automatically handles this by comparing the max partition date in ClickHouse against the current time. If it falls behind, it enters a CATCHUP mode; otherwise, it runs a NORMAL load.

#### Reliability: The Custom Verified Operator & Idempotency

Standard Airflow operators use synchronous HTTP calls, which often time out on long data loads. To fix this, we built acustom, verified Airflow operator.

Async Polling & Deterministic Query IDs:Instead of holding a connection open, our operator submits the query and immediately detaches. It then pollssystem.query_logto verify completion.

Crucially, we generate aDeterministic Query IDbased on the DAG, Task, and Run context. If an Airflow worker crashes and restarts:

1. The new worker generates the same ID.
2. It checkssystem.query_log.
3. If it sees the query already succeeded, it skips execution entirely. This makes our pipeline idempotent and crash-resilient.

#### Safety Valves

We implemented specific protections to prevent data corruption:

* Empty Staging Protection:Before anEXCHANGE TABLESoperation, we check if the staging table has rows. If it's empty (due to an upstream filter error), we abort the swap to prevent wiping production data.
* Row Count Validation:After a load, we comparecount(*)between Trino and ClickHouse. If a mismatch is detected, the pipeline fails.

### 3. The Serving Layer: Safe, Semantic, and Low-Latency Access

While the Ingestion Engine handles the "heavy lifting," the Serving Layer is the brain of the operation. It acts as the gateway through which all microservices access analytical data.

When designing this layer, we rejected two common approaches:

* Direct SQL Access:Too dangerous. It creates tight coupling, invites SQL injection, and allows inefficient queries to degrade cluster performance.
* Rigid REST Endpoints:Too slow to iterate. Creating a new endpoint for every business question creates a bottleneck.

Instead, we built aType-Safe, Semantic Query DSLrunning on our Scala backend framework.

### 3.1. The Semantic DSL: Querying as Code

Instead of sending raw SQL strings, developers construct a structured JSON object defined by a strict Protobuf contract. This treats a query as a logical tree of operations rather than a text blob.

Example Request:

“Give me the daily message count and unique users for the 'PROJECT_ALPHA' namespace over the last 30 days, filling in gaps where no messages occurred.”

{
	"table_id": "prod_ai_insights_daily",
	"query": {
		"measures": [
			{
			"aggregation": { "function_name": "SUM", "column": "total_message_count" },

			"alias": "total_messages"
		},
		{
				"aggregation": { "function_name": "COUNT", "column": "user_id", "distinct": true },

			"alias": "unique_users"
		}
		],
	"filters": {
		"condition": {
			"column": "namespace",
			"operator": "EQUALS",
			"values": ["PROJECT_ALPHA"]
		}
	},
	"time_dimensions": [
			{
				"column": "message_ts",
				"granularity": "day",
				"date_range": { "relative": "last_30_days" },
				"fill_gaps": true
			}
		]
	}
}

### 3.2. The Compilation Pipeline

The Serving Layer is effectively a compiler. It transforms the semantic intent of the JSON into dialect-specific, highly optimized ClickHouse SQL.

* Validation & Type Checking:The engine verifies the request against the Table Registry. It ensures columns exist and that operators are valid for the data type.
* Expression Tree Resolution:We support complex, nested arithmetic and logic that doesn't exist in the raw table (e.g., calculating "Profit Margin" on the fly).
* Time-Series Intelligence (fill_gaps):If you query for "daily visits" and a specific day has zero visits, standard SQL simply returns no row. Our engine detectsfill_gaps: trueand injects ClickHouse's specificWITH FILLsyntax, ensuring the API returns a continuous time series with zero-filled gaps.

### 3.3. Performance Optimizations & Consistency

The Serving Layer is "engine-aware." It knows how the data was ingested and optimizes queries accordingly.

* Handling Upserts (FINAL):For tables utilizing the UPSERT strategy (ReplacingMergeTree), duplicate rows may exist temporarily. To guarantee consistency, the Serving Layer automatically detects this table type and appends theFINALmodifier to the query.
* Partition Optimization:Simply addingFINALcan act as a performance brake because it forces merging. To mitigate this, our compiler injects settings to instruct ClickHouse to merge data only within partitions—massive performance gain for time-series data—while still guaranteeing correctness.

### 3.4. Security:

Exposing analytical data requires strict guardrails.

* SQL Injection Immunity:The DSL makes injection mathematically impossible. User input is never concatenated into the query string. Even if a user sends malicious strings, the engine binds them as strict String parameters.
* Resource Governance:To prevent "Bad Neighbors" (queries that hog cluster resources), we enforce:Max Limit:Strict caps on row counts.Timeouts:Short default timeouts with hard execution limits.Complexity Limits:Validation fails requests with excessive nested aggregations or filter depth.
* Max Limit:Strict caps on row counts.
* Timeouts:Short default timeouts with hard execution limits.
* Complexity Limits:Validation fails requests with excessive nested aggregations or filter depth.

### 3.5. Developer Experience

We recognized that while a JSON DSL is powerful for machines, humans think in SQL. To ease adoption, we built aSQL translation endpoint.

A developer can paste standard SQL into this endpoint, and the service returns the perfectly formatted JSON object required to run it. This tool has been critical for adoption, allowing engineers to migrate legacy queries in minutes.

### Conclusion

Data-to-Production has transformed how we build user-facing data products by turning data ingestion and serving into a first-class, managed platform. Instead of treating data pipelines as offline, analytical workflows, we enable Data Engineers to expose DWH data directly to backend production services—safely, consistently, and with production-grade guarantees.

At the core of the platform is an end-to-end flow:

1. Ingestionfrom Iceberg tables into ClickHouse, with built-in schema evolution, validation, automatic catch-up, and operational safeguards.
2. Servingthrough managed services, allowing production services to consume fresh, query-optimized data as part of user-facing request paths.

This closes the traditional gap between analytics and production. What once required weeks of custom glue code, manual reviews, and risky handoffs is now a self-service path. Crucially, this is not just faster—it’s safer. By treating data exposure as a platform capability, we’ve dramatically reduced the Activation Gap and unlocked a new class of data-powered features.

 

This post was written byAlmog Gelber

 

More of Wix Engineering's updates and insights:

* Follow us on:Twitter|Facebook|LinkedIn|TikTok
* Join ourTelegram channel
* Visit us onGitHub
* Subscribe to our monthly newsletter
* Subscribe to ourYouTube channel
* Follow our Medium publication
* Listen to our podcast onApple,SpotifyorGoogle
