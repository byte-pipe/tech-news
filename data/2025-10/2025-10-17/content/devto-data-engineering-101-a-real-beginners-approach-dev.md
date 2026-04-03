---
title: Data Engineering 101 - A real beginner's approach - DEV Community
url: https://dev.to/danielhe4rt/data-engineering-101-a-real-beginners-approach-25a8
site_name: devto
fetched_at: '2025-10-17T11:08:15.917033'
original_url: https://dev.to/danielhe4rt/data-engineering-101-a-real-beginners-approach-25a8
author: Daniel Reis
date: '2025-10-14'
description: This is the article about Data Engineering that you find if you search the subject on Google and get... Tagged with datascience, database, bruin, programming.
tags: '#datascience, #database, #bruin, #programming'
---

This is the article about Data Engineering that you find if you search the subject on Google and get redirected after clickFeeling Lucky.

Also, this article is a POV of an experienced webdev engineer that started a new topic in his career, that means: that's my study, my research, if you have anything to add, feel free to teach me in the comments below! I would love to learn more!

## Table of Contents

* 1. Prologue
* 2. First Impressions: Exploring Bruin’s Structure2.1. Core File:.bruin.yml2.2. Pipeline: A Way Easier Apache Airflow2.3. Assets: The Building Blocks of Data Products2.4. Policies: Enforcing Quality and Governance2.5. Glossary: Speaking the Same Language
* 2.1. Core File:.bruin.yml
* 2.2. Pipeline: A Way Easier Apache Airflow
* 2.3. Assets: The Building Blocks of Data Products
* 2.4. Policies: Enforcing Quality and Governance
* 2.5. Glossary: Speaking the Same Language
* 3. Building Our First Pipeline3.1. Step 1: Ingest from Your Source to a Data Lake3.2. Step 2: Formatting and Validating the Data (Staging Layer)3.3. Step 3: Designing the Analytics (Mart) Layer
* 3.1. Step 1: Ingest from Your Source to a Data Lake
* 3.2. Step 2: Formatting and Validating the Data (Staging Layer)
* 3.3. Step 3: Designing the Analytics (Mart) Layer
* 4. Full Preview Data Flow
* 5. Overpowered VS Code Extension
* 6. Conclusion

## 1. Prologue

I have to admit: whenever someone mentionedData Engineering, I used to tune out. It always sounded like something impossibly complex — almostmagical.

This week, I finally decided to dive in. I thought it would be fairly straightforward, but it didn’t take long to realize how deep the rabbit hole goes.

This field isn’t just a few scripts or SQL queries; it’s an entireecosystemof interconnected tools, concepts, and responsibilities that form the backbone of modern data systems.

Concepts like:

* Data Catalogs and Governance:understanding who owns the data, how to ensure quality, and how to track lineage.
* Orchestration:coordinating dependencies and workflows with tools likeApache AirfloworDagster.
* Transformation (ETL/ELT):cleaning and standardizing data using tools such asdbtorFivetran.
* Ingestion and Streaming:connecting sources and moving data in real time withKafka,Airbyte, orConfluent Cloud.
* Observability and Quality:monitoring data health with solutions likeMonte CarloandDatafold.

For each article clicked, just opened up a new world of tools, words, frameworks, architectures, and best practices.And somehow, all of ithas to work together— governance, orchestration, transformation, ingestion, observability, infrastructure.

As a developer, I’m used to learning alanguageand aframeworkand then getting to work.But in data engineering, it’s different.

It’s about understanding an entireecosystemand how each piece connects to the next.

After hours of reading docs, chasing GitHub repos, and jumping between tools, articles, and endless definitions, I finally foundthe toolthat made everything click —Bruin.

### Imagine a single framework that:

* Pipelines as Code— Everything lives in version-controlled text (YAML, SQL, Python). No hidden UIs or databases. Reproducible, reviewable, and automatable.
* Multi-Language by Nature— Native support for SQL and Python, plus the ability to plug in binaries or containers for more complex use cases.
* Composable Pipelines— Combine technologies, sources, and destinations in one seamless flow — no glue code, no hacks.
* No Lock-In— 100% open-source (Apache-licensed) CLI that runs anywhere: locally, in CI, or in production. You keep full control of your pipelines and data.
* Built for Developers and Data Quality— Fast local runs, integrated checks, and quick feedback loops. Data products that are tested, trusted, and easy to ship.

…and itfits all the core Data Engineering conceptsI just mentioned earlier.

I’ll admit it — I’m the kind of person who embracesproductive laziness. If there’s a way to do more with fewer tools and less friction, I’m in.

So before we get started, here’s the plan:

In most setups, data flows from OLTP databases → ingestion → data lake/warehouse → transformation → marts → analytics dashboards.

Tools likeAirbytehandle ingestion,dbthandles transformation,Airfloworchestrates dependencies — and Bruin combines those layersinto one unified framework.

This article will walk through thefundamental principles of Data Engineering, while exploring howBruinbrings them all together through a simple, real-world pipeline.

## 2. First Impressions: Exploring Bruin’s Structure

I’ll be honest — I used to have a bit of a bias against Data Science/Engineering projects. Every time I looked at one, it felt messy and unstructured, with files and notebooks scattered everywhere. Coming from a software development background, that kind of chaos always bothered me.

But once I started looking atBruin’s project structure, that perception completely changed. Everything suddenly feltorganized and intentional.The framework naturally enforces structure through its layers — and once you follow them, everything starts to make sense.

### Example: Project Structure

├── duckdb.db
├── ecommerce-mart
│ ├── assets
│ │ ├── ingestion
│ │ │ ├── raw.customers.asset.yml
│ │ │ ├── raw.order_items.asset.yml
│ │ │ ├── raw.orders.asset.yml
│ │ │ ├── raw.products.asset.yml
│ │ │ └── raw.product_variants.asset.yml
│ │ ├── mart
│ │ │ ├── mart.customers-by-age.asset.py
│ │ │ ├── mart.customers-by-country.asset.yml
│ │ │ ├── mart.product_performance.sql
│ │ │ ├── mart.sales_daily.sql
│ │ │ └── mart.variant_profitability.sql
│ │ └── staging
│ │ ├── stg.customers.asset.yml
│ │ ├── stg.order_items.sql
│ │ ├── stg.orders.sql
│ │ ├── stg.products.sql
│ │ └── stg.product_variants.sql
│ └── pipeline.yml
├── glossary.yml
├── policy.yml
└── .bruin.yml

Enter fullscreen mode

Exit fullscreen mode

### What Each Part Does

* .bruin.ymlThe main configuration file for your Bruin environment.Definesglobal settingslike defaultconnections, variables, andbehaviorfor all pipelines.
* The main configuration file for your Bruin environment.
* Definesglobal settingslike defaultconnections, variables, andbehaviorfor all pipelines.
* policy.ymlYour data governance and validation policy file.Defines data quality rules, access controls, and compliance checks that Bruin can automatically enforce before shipping data products.
* Your data governance and validation policy file.
* Defines data quality rules, access controls, and compliance checks that Bruin can automatically enforce before shipping data products.
* glossary.ymlWorks as a lightweight data catalog for your project.Documents terms, metrics, and datasets so everyone on the team speaks the same language.Also helps with lineage, documentation, and discoverability.
* Works as a lightweight data catalog for your project.
* Documents terms, metrics, and datasets so everyone on the team speaks the same language.
* Also helps with lineage, documentation, and discoverability.
* some-feature/pipeline.ymlDefines a specific pipeline for a domain or project (in this example,ecommerce).Describes the end-to-end data flow — which assets to run, their dependencies, and schedules.Pipelines are modular, so you can maintain separate ones for different business domains.
* Defines a specific pipeline for a domain or project (in this example,ecommerce).
* Describes the end-to-end data flow — which assets to run, their dependencies, and schedules.
* Pipelines are modular, so you can maintain separate ones for different business domains.
* some-feature/assets/*Contains all the assets — the building blocks of your data pipelines.Each asset handles a distinct task: ingesting raw data, transforming it, or generating analytical tables.Since every asset is a file, it’sversion-controlled, testable, and reusable— just like code.
* Contains all the assets — the building blocks of your data pipelines.
* Each asset handles a distinct task: ingesting raw data, transforming it, or generating analytical tables.
* Since every asset is a file, it’sversion-controlled, testable, and reusable— just like code.

With just that, we're able to run a full pipeline. However, I still think we need to go through each step and file individually — I promise it’ll be quick!

### 2.1. Core File:.bruin.yml

Think of.bruin.ymlas theroot configurationof your project — the file that tells Bruinhowandwhereto run everything.

Instead of scattering settings across scripts or environment variables, Bruin centralizes them here: connections, credentials, and environment-specific configurations all live in one place.It also serves as Bruin’sdefault secrets backend, so your pipelines can access databases or warehouses securely and consistently.

bruin run ecommerce/pipeline.yml
--config-file
 /path/to/.bruin.yml

Enter fullscreen mode

Exit fullscreen mode

A simple example:

default_environment
:

default

environments
:


default
:


connections
:


postgres
:


-

name
:

pg-default


username
:

postgres

# (hardcoded as well)


password
:

${PG_PASSWORD}


host
:

${PG_HOST}


port
:

${PG_PORT}


database
:

${PG_DATABASE}


duckdb
:


-

name
:

duckdb-default


path
:

duckdb.db

Enter fullscreen mode

Exit fullscreen mode

### What’s Happening Here

* default_environment— sets the environment Bruin will use unless specified otherwise.
* environments— defines multiple setups (e.g.,dev,staging,prod), each with its own configuration.
* connections— lists every system Bruin can connect to, like Postgres or DuckDB.
Each connection gets a name (e.g.,pg-default) that you’ll reference across pipelines and assets.
* Environment variable support— any value wrapped in${...}will be automatically read from your system environment.

This means you can keep credentials out of source control while still running locally or in CI/CD environments.

This design keeps everythingcentralized, secure, and version-controlled, while giving you the flexibility to inject secrets dynamically through environment variables — perfect for switching between local, staging, and production without touching the code.

### 2.2. Pipeline: A WAY EASIER Apache Airflow

For each feature you have, it will have to come with apipeline.ymlfile.This is the file that will group all your assets and understand that it's not a single asset running, but a chained list of assets.

- ecommerce-mart/
 ├─ pipeline.yml -> you're here
 └─ assets/
 ├─ some-asset.sql
 ├─ definitely-an-asset.yml
 └─ another-asset.py

Enter fullscreen mode

Exit fullscreen mode

There you also configure each connection you want to use on the specific pipeline:

name
:

product_ecommerce_marts

schedule
:

daily

# relevant for Bruin Cloud deployments

default_connections
:


duckdb
:

"
duckdb-default"


postgres
:

"
pg-default"

Enter fullscreen mode

Exit fullscreen mode

### 2.3. Assets: The Building Blocks of Data Products

Every data pipeline inBruinis composed ofassets— modular, self-contained units that define a specific operation: ingesting, transforming, or producing a dataset.

Each asset exists as a file under theassets/directory, and its filename doubles as its identity inside the pipeline graph.

If you remember the file structure shown in the beginning, you must remember that I have multiple types of assets in the pipeline. That's the most cool part, since you can write down in multiple languages and still being something simple. Here's some possibilities:

Type

Description

Filename (in the file tree)

YAML

Declarative configuration for ingestion or metadata-heavy assets

raw.customers.asset.yml

SQL

Pure transformation logic — think dbt-style models

stg.orders.sql

Python

Custom logic or integrations (e.g., APIs, validations, or machine learning steps)

mart.sales_daily.asset.py

You’re free to organize assets however you like — there’s no rigid hierarchy to follow.The key insight is thatthe orchestration happens implicitly through dependencies, not through an external DAG engine like Airflow.

Each asset declares what it depends on, andBruin automatically builds and executes the dependency graphfor you.

Example:

1. raw.orders.asset.yml

# raw.orders.asset.yml

name
:

raw.orders

type
:

ingestr

description
:

Ingest OLTP orders from Postgres into the DuckDB raw layer.

parameters
:


source_connection
:

pg-default


source_table
:

"
public.orders"


destination
:

duckdb

Enter fullscreen mode

Exit fullscreen mode

1. raw.order_items.asset.yml

# raw.order_items.asset.yml

name
:

raw.order_items

type
:

ingestr

description
:

Ingest OLTP order_items from Postgres into the DuckDB raw layer.

depends
:


-

raw.orders

# declares a dependency on the 'raw.orders' asset

parameters
:


source_connection
:

pg-default


source_table
:

"
public.order_items"


destination
:

duckdb

Enter fullscreen mode

Exit fullscreen mode

... turns into:

graph TD
 raw.orders --> raw.order_items;

Enter fullscreen mode

Exit fullscreen mode

By chaining assets like this, you describelogical relationshipsbetween data operations rather than manually orchestrating steps.The result is adeclarative, composable, and maintainable pipeline— easy to read, version, and extend just like application code.

One of the most powerful aspects of Bruin is how it connectsdata qualityandgovernancedirectly into your assets.By defining checks under each column, you’re not only validating your data but also documenting ownership, expectations, and constraints — all version-controlled and enforceable at runtime.

This means Bruin doesn’t justrunpipelines — itaudits,documents, andgovernsthem as part of the same workflow.

### 2.4. Policies: Enforcing Quality and Governance

Policies inBruinact as the rulebook that keeps your data pipelines consistent, compliant, and high quality.They ensure every asset and pipeline follows best practices — from naming conventions and ownership to validation and metadata completeness.

At their core, policies are defined in a singlepolicy.ymlfile located at the root of your project.This file lets youlint,validate, andenforce standardsautomatically before a pipeline runs.

#### Quick Overview

rulesets
:


-

name
:

standard


selector
:


-

path
:

.*/ecommerce/.*


rules
:


-

asset-has-owner


-

asset-name-is-lowercase


-

asset-has-description

Enter fullscreen mode

Exit fullscreen mode

Eachrulesetdefines:

* wherethe rule applies (selector→ match by path, tag, or name),
* whatto enforce (rules→ built-in or custom validation rules).

Once defined, you can validate your entire project:

bruin validate ecommerce

# Validating pipelines in 'ecommerce' for 'default' environment...

# Pipeline: ecommerce_pg_to_duckdb (.)

# raw.order_items (assets/ingestion/raw.order_items.asset.yml)

# └── Asset must have an owner (policy:standard:asset-has-owner)

Enter fullscreen mode

Exit fullscreen mode

Bruin automatically lints assets before execution — ensuring thatnon-compliant pipelines never run.

#### Built-in and Custom Rules

Rule

Target

Description

asset-has-owner

asset

Each asset must define an owner.

asset-has-description

asset

Assets must include a description.

asset-name-is-lowercase

asset

Asset names must be lowercase.

pipeline-has-retries

pipeline

Pipelines must define retry settings.

You can also define your own rules:

custom_rules
:


-

name
:

asset-has-owner


description
:

every asset should have an owner


criteria
:

asset.Owner != ""

Enter fullscreen mode

Exit fullscreen mode

Rules can target eitherassetsorpipelines, and they use logical expressions to determine compliance.

Policies transform Bruin into aself-governing data platform— one where best practices aren’t optional, they’re enforced.By committing your rules to version control, you make data governance part of the development workflow, not an afterthought.

### 2.5. Glossary: Speaking the Same Language

In data projects, one of the hardest problems isn’t technical — it’scommunication.Different teams often use the same word to mean different things.That’s whereBruin’s Glossarycomes in.

A glossary is defined inglossary.ymlat the root of your project.It acts as ashared dictionaryof business concepts (likeCustomerorOrder) and their attributes, keeping teams aligned across pipelines.

entities
:


Customer
:


description
:

A registered user or business in our platform.


attributes
:


ID
:


type
:

integer


description
:

Unique customer identifier.

Enter fullscreen mode

Exit fullscreen mode

You can reference these definitions inside assets usingextends, avoiding duplication and ensuring consistency:

# raw.customers.asset.yml

name
:

raw.customers

type
:

ingestr

columns
:


-

name
:

customer_id


extends
:

Customer.ID

Enter fullscreen mode

Exit fullscreen mode

This automatically inherits thetypeanddescriptionfrom the glossary.It’s a simple idea, but a powerful one — yourdata definitions become version-controlled and shared, just like code.

## 3. Building Our First Pipeline

Now that we’ve explored the structure and philosophy behindBruin, it’s time to build an end-to-end pipeline.We’ll go fromraw ingestionto aclean staging layer, and finally, toanalytics-ready marts— all defined as code.

We’ll assume you already have:

* APostgresdatabase as your data source.
* ADuckDBdatabase as your analytical storage.
* A working.bruin.ymlfile configured with both connections
### 3.1 Step 1 : Ingest from Your Source to a Data Lake

The first step is to move data from Postgres into DuckDB.This creates yourRaw Layer— data replicated from the source with minimal transformation.

Create an ingestion asset file:

touch
assets/ingestion/raw.customers.asset.yml

Enter fullscreen mode

Exit fullscreen mode

Then define the asset:

# assets/ingestion/raw.customers.asset.yml

name
:

raw.customers

type
:

ingestr

description
:

Ingest OLTP customers from Postgres into the DuckDB raw layer.

parameters
:


source_connection
:

pg-default


source_table
:

"
public.customers"


destination
:

duckdb

columns
:


-

name
:

id


type
:

integer


primary_key
:

true


checks
:


-

name
:

not_null


-

name
:

unique


-

name
:

email


type
:

string


checks
:


-

name
:

not_null


-

name
:

unique


-

name
:

country


type
:

string


checks
:


-

name
:

not_null

Enter fullscreen mode

Exit fullscreen mode

This tells Bruin to extract data from your Postgres tablepublic.customers, validate column quality, and store it in the DuckDB raw layer.

#### Running the Asset

bruin run ecommerce/assets/ingestion/raw.customers.asset.yml

Enter fullscreen mode

Exit fullscreen mode

Expected output:

Analyzed the pipeline 'ecommerce_pg_to_duckdb' with 13 assets.
Running only the asset 'raw.customers'

 Pipeline: ecommerce_pg_to_duckdb (../../..)
 No issues found
✓ Successfully validated 13 assets across 1 pipeline, all good.
 Interval: 2025-10-12T00:00:00Z - 2025-10-12T23:59:59Z

Starting the pipeline execution...
 PASS raw.customers ........

 bruin run completed successfully in 2.095s

✓ Assets executed 1 succeeded

Enter fullscreen mode

Exit fullscreen mode

You can now query the ingested data:

bruin query
--connection
 duckdb-default
--query

"SELECT * FROM raw.customers LIMIT 5"

Enter fullscreen mode

Exit fullscreen mode

Result:

┌────┬───────────────────┬───────────────────────────┬───────────┬──────────────────┬──────────────────────────────────────┬──────────────────────────────────────┐
│ ID │ FULL_NAME │ EMAIL │ COUNTRY │ CITY │ CREATED_AT │ UPDATED_AT │
├────┼───────────────────┼───────────────────────────┼───────────┼──────────────────┼──────────────────────────────────────┼──────────────────────────────────────┤
│ 1 │ Allison Hill │ donaldgarcia@example.net │ Uganda │ New Roberttown │ 2025-10-10 18:19:13.083281 +0000 UTC │ 2025-10-10 00:42:59.71112 +0000 UTC │
│ 2 │ David Guzman │ jennifermiles@example.com │ Cyprus │ Lawrencetown │ 2025-10-10 07:52:47.643619 +0000 UTC │ 2025-10-10 06:23:42.864287 +0000 UTC │
│ 3 │ Caitlin Henderson │ eric51@example.org │ Hong Kong │ West Melanieview │ 2025-10-10 21:06:02.639412 +0000 UTC │ 2025-10-10 19:23:17.540169 +0000 UTC │
│ 4 │ Monica Herrera │ smiller@example.net │ Niger │ Barbaraland │ 2025-10-11 01:33:43.032929 +0000 UTC │ 2025-10-10 02:29:27.22515 +0000 UTC │
│ 5 │ Darren Roberts │ wyattmichelle@example.com │ Fiji │ Reidstad │ 2025-10-10 12:05:18.734246 +0000 UTC │ 2025-10-10 00:51:13.406526 +0000 UTC │
└────┴───────────────────┴───────────────────────────┴───────────┴──────────────────┴──────────────────────────────────────┴──────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

Yourraw layeris now established and validated.

### 3.2 Step 2: Formatting and Validating the Data (Staging Layer)

Next, we’ll clean and standardize the ingested data before using it in analytics.This layer is calledStaging (stg)— it’s where you enforce schema, column consistency, and apply business rules.

Create the file:

touch
ecommerce/assets/staging/stg.customers.asset.sql

Enter fullscreen mode

Exit fullscreen mode

And define it as follows:

/* @bruin
name: stg.customers
type: duckdb.sql
materialization:
 type: table

depends:
 - raw.customers

checks:
 columns:
 id:
 - not_null
 email:
 - not_null
 - unique
 country:
 - not_null
@bruin */

SELECT

id
::
INT

AS

customer_id
,


COALESCE
(
TRIM
(
email
),

''
)

AS

email
,


COALESCE
(
TRIM
(
country
),

'Unknown'
)

AS

country
,


created_at
,


updated_at

FROM

raw
.
customers

WHERE

email

IS

NOT

NULL
;

Enter fullscreen mode

Exit fullscreen mode

Here’s what’s happening:

* TheBruin annotation block (@bruin)defines metadata for the asset.
* Thedependskey ensures this staging steponly runs afterraw.customerscompletes — Bruin automatically manages the dependency chain.
* Thecolumn checksensure data quality before and after the transformation.
* The SQL query itself performs light cleaning and enforces type consistency.

This design mimics orchestration tools likeAirflow, but without external schedulers — dependencies and checks are declared right inside your code.

#### Validation and Execution

Before running, validate the asset:

bruin validate ecommerce/assets/staging/stg.customers.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Expected output:

Pipeline: ecommerce_pg_to_duckdb
(
.
)

 No issues found

✓ Successfully validated 13 assets across 1 pipeline, all good.

Enter fullscreen mode

Exit fullscreen mode

Now execute it:

bruin run ecommerce/assets/staging/stg.customers.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Result:

bruin run ecommerce/assets/staging/stg.customers.asset.sql
Analyzed the pipeline 'ecommerce_pg_to_duckdb' with 15 assets.
Running only the asset 'stg.customers'

Pipeline: ecommerce_pg_to_duckdb (../../..)
 No issues found

✓ Successfully validated 15 assets across 1 pipeline, all good.

Interval: 2025-10-12T00:00:00Z - 2025-10-12T23:59:59Z

Starting the pipeline execution...

[21:28:16] Running: stg.customers
[21:28:16] Finished: stg.customers (41ms)

==================================================

PASS stg.customers

bruin run completed successfully in 41ms

 ✓ Assets executed 1 succeeded

Enter fullscreen mode

Exit fullscreen mode

Confirm that the transformation worked:

bruin query
"SELECT country, COUNT(*) AS customers FROM stg.customers GROUP BY country ORDER BY customers DESC;"

Enter fullscreen mode

Exit fullscreen mode

Sample output:

country | customers
--------------+-----------
BRAZIL | 420
GERMANY | 255
UNITED STATES | 198
ARGENTINA | 190
SOUTH KOREA | 182

Enter fullscreen mode

Exit fullscreen mode

At this point, you have aclean, validated datasetready for analytics.

### 3.3 Step 3: Designing the Analytics (Mart) Layer

The final step is to build yourMart Layer, where business-ready data lives.This is the layer analysts and dashboards query directly.Each Mart asset aggregates or reshapes the staging data into meaningful datasets for reporting and analysis.

#### 3.3.1 Asset:mart.customers_by_country.asset.sql

Create the following file:

touch
ecommerce/assets/mart/mart.customers_by_country.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Then define the asset:

/* @bruin
name: mart.customers_by_country
type: duckdb.sql

materialization:
 type: table

depends:
 - stg.customers
@bruin */

SELECT


country
,


COUNT
(
*
)

AS

total_customers

FROM

stg
.
customers

GROUP

BY

country

ORDER

BY

total_customers

DESC
;

Enter fullscreen mode

Exit fullscreen mode

This SQL asset aggregates customers by country and depends onstg.customers, ensuring the staging layer runs first.It materializes as a table inside DuckDB.

Run it:

bruin run ecommerce/assets/mart/mart.customers_by_country.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Expected output:

Pipeline: ecommerce_pg_to_duckdb (.)
Running mart.customers_by_country
✓ Table materialized successfully in DuckDB

Enter fullscreen mode

Exit fullscreen mode

Verify the results:

bruin query
--connection
 duckdb-default
--query

"SELECT * FROM mart.customers_by_country LIMIT 5;"

Enter fullscreen mode

Exit fullscreen mode

Result:

┌───────────────┬───────────────────┐
│ COUNTRY │ TOTAL_CUSTOMERS │
├───────────────┼───────────────────┤
│ BRAZIL │ 420 │
│ GERMANY │ 255 │
│ UNITED STATES │ 198 │
│ ARGENTINA │ 190 │
│ SOUTH KOREA │ 182 │
└───────────────┴───────────────────┘

Enter fullscreen mode

Exit fullscreen mode

#### 3.3.2 Asset:mart.customers_by_age.asset.sql

Now, let’s create a second mart that segments customers into age groups.

Create the file:

touch
ecommerce/assets/mart/mart.customers_by_age.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Define it as follows:

/* @bruin
name: mart.customers_by_age
type: duckdb.sql

materialization:
 type: table
depends:
 - stg.customers

@bruin */


WITH

src

AS

(


SELECT


CASE


WHEN

age

<

25

THEN

'18-24'


WHEN

age

BETWEEN

25

AND

34

THEN

'25-34'


WHEN

age

BETWEEN

35

AND

49

THEN

'35-49'


ELSE

'50+'


END

AS

age_group


FROM

stg
.
customers

)

SELECT


age_group
,


COUNT
(
*
)

AS

total_customers


FROM

src


GROUP

BY

age_group


ORDER

BY

total_customers

DESC
;

Enter fullscreen mode

Exit fullscreen mode

This asset computes customer distribution by age brackets using a simpleCASEexpression and aggregates the results.

Run it:

bruin run ecommerce/assets/mart/mart.customers_by_age.asset.sql

Enter fullscreen mode

Exit fullscreen mode

Expected output:

bruin run ecommerce/assets/mart/mart.customers_by_age.asset.sql
Analyzed the pipeline 'ecommerce_pg_to_duckdb' with 15 assets.
Running only the asset 'mart.customers_by_age'

Pipeline: ecommerce_pg_to_duckdb (../../..)
 No issues found

✓ Successfully validated 15 assets across 1 pipeline, all good.

Interval: 2025-10-12T00:00:00Z - 2025-10-12T23:59:59Z

Starting the pipeline execution...

[21:10:24] Running: mart.customers_by_age
[21:10:24] Finished: mart.customers_by_age (39ms)

==================================================

PASS mart.customers_by_age

bruin run completed successfully in 39ms

 ✓ Assets executed 1 succeeded

Enter fullscreen mode

Exit fullscreen mode

Confirm that the mart is populated correctly:

bruin query
--connection
 duckdb-default
--query

"SELECT * FROM mart.customers_by_age;"

Enter fullscreen mode

Exit fullscreen mode

Result:

┌─────────────┬───────────────────┐
│ AGE_GROUP │ TOTAL_CUSTOMERS │
├─────────────┼───────────────────┤
│ 25-34 │ 460 │
│ 35-49 │ 310 │
│ 18-24 │ 250 │
│ 50+ │ 225 │
└─────────────┴───────────────────┘

Enter fullscreen mode

Exit fullscreen mode

### 4. Full Preview Data Flow

Hopefully, if I got it right, the concepts explained in the beginning didn't got that messy and we actually made the pipeline become a real thing only using Bruin and a couple of queries!

Our example pipeline look like this:

graph TD
 raw.customers --> stg.customers
 stg.customers --> mart.customers_by_country
 stg.customers --> mart.customers_by_age

Enter fullscreen mode

Exit fullscreen mode

At this stage, you’ve built afully declarative, end-to-end data pipelinewith Bruin — ingestion, staging, and analytics — all governed, validated, and reproducible, without any external orchestration layer.

## 5. Overpowered VS Code Extension

When I first installed theBruin VS Code Extension, I had no idea what I was doing.At that time, I didn’t really understand howBruin— or evenData Engineering— worked.I clicked around, saw a bunch of YAMLs and metadata markers, and quickly gave up.

Week later, after finally understanding the ecosystem — ingestion, staging, marts, and governance — I decided to open the extension again, ad that’s when itall clicked.

It wasn’t just a helper. It wasthe missing piece.

The extension brings the same declarative power of Bruin’s CLI into avisual, developer-friendly environment.It automatically scans your assets, validates configurations, runs queries directly against your databases, and even manages your YAMLs in real time.

Everything happens inside VS Code — validation, lineage exploration, metadata checks, and query previews.

What impressed me most was howfluid and openit is. There’sno vendor lock-inhere — it’s completely open source.You can fork it, extend it, or contribute back to the community just like the CLI itself.

In short, the Bruin VS Code Extension isn’t just a companion — it’s the natural evolution of the workflow. Once you understand Bruin, this tool feels like magic finally explained.

## 6. Conclusion

This study was my first real attempt to understandBruinand whatData Engineeringactually means in practice. What once felt abstract and complicated started to make a bit more sense after breaking things apart, experimenting, and connecting the dots one step at a time.

I wouldn’t say I fully understand everything yet—far from it—but I can finally see how the pieces fit together: ingestion, staging, marts, validation, and governance. Bruin helped me get hands-on with those concepts in a way that felt approachable instead of overwhelming.

The process of exploring, failing, reading, and rebuilding turned out to be the most valuable part. There’s still a lot to learn, but this was a solid first step toward really understanding how data moves, transforms, and tells a story (just like this article).

GitHub Demo: E-commerce Pipeline with BruinBruin Website

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
