---
title: 'GitHub - floci-io/floci: Light, fluffy, and always free - The AWS Local Emulator alternative · GitHub'
url: https://github.com/floci-io/floci
site_name: github
content_file: github-github-floci-iofloci-light-fluffy-and-always-free
fetched_at: '2026-11-05T15:23:35.566136'
original_url: https://github.com/floci-io/floci
author: floci-io
description: Light, fluffy, and always free - The AWS Local Emulator alternative - floci-io/floci
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,880 Commits
4,880 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.mvn/
wrapper
.mvn/
wrapper
 
 
bin
bin
 
 
compatibility-tests
compatibility-tests
 
 
docker
docker
 
 
docs
docs
 
 
licenses
licenses
 
 
overrides
overrides
 
 
src
src
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.releaserc.json
.releaserc.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
mkdocs.yml
mkdocs.yml
 
 
mvnw
mvnw
 
 
mvnw.cmd
mvnw.cmd
 
 
pom.xml
pom.xml
 
 
View all files

## Repository files navigation

Any Cloud. Locally.Light, fluffy, and always freeNo account. No auth token. No feature gates. Justdocker compose up.

Quick Start·Features·Services·SDKs·Testcontainers·Migration·Docs

## What is Floci?

Floci is a free, open-source local AWS emulator for development, testing, and CI.

It gives you AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid feature gates. Point your AWS SDK, CLI, Terraform, CDK, OpenTofu, or test suite athttp://localhost:4566and keep your existing workflows.

Already using LocalStack? Floci is a drop-in replacement: swap the image and keep going. SeeMigrating from LocalStack.

Floci is the AWS member of theFlociemulator family, named afterfloccus, the cloud formation that looks like popcorn.

Emulator

Cloud

Port

floci

AWS

4566

floci-az

Azure

4577

floci-gcp

GCP

4588

floci-oci

OCI

4599

## Quick Start

The fastest way to run Floci is with the officialCLI

floci start

No Docker? Eachreleasealso ships a standalonefloci-awsbinary for Linux, macOS and Windows; seeNative binary.

Export the AWS environment variables:

eval
 
$(
floci env
)

Use your existing AWS tools normally:

aws s3 mb s3://my-bucket

aws dynamodb create-table \
 --table-name demo-table \
 --attribute-definitions AttributeName=pk,AttributeType=S \
 --key-schema AttributeName=pk,KeyType=HASH \
 --billing-mode PAY_PER_REQUEST

aws dynamodb list-tables

### Watch it run

This short demo shows the CLI flow: start Floci, export the local AWS environment, run standard AWS CLI commands, and stop the emulator.

floci-cli-demo.mp4

All AWS services are available athttp://localhost:4566. Anypublished AWS regionworks, in every partition. Credentials can be any non-empty values unless you explicitly enable stricter service-specific auth checks.

Prefer Docker Compose?

Create acompose.yamlfile:

services
:
 
floci
:
 
image
: 
floci/floci:latest

 
ports
:
 - 
"
4566:4566
"

Start Floci:

docker compose up

Then configure your AWS environment manually:

export
 AWS_ENDPOINT_URL=http://localhost:4566

export
 AWS_DEFAULT_REGION=us-east-1

export
 AWS_ACCESS_KEY_ID=test

export
 AWS_SECRET_ACCESS_KEY=test

Using the old 
hectorvent/floci
 image?

Update your image name:

#
 Before

image
: 
hectorvent/floci:latest

#
 After

image
: 
floci/floci:latest

The oldhectorvent/flocirepository no longer receives updates.

## Web Console

Floci ships a browser console for inspecting the resources in your local emulator.

Open it at:http://localhost:4566/_floci/ui

Nothing runs at boot. The first request pulls the console image, starts it as a sidecar container on Floci's Docker network, hands it Floci's own reachable address plus the standard AWS environment, polls its health endpoint, and redirects the browser once it reports it can reach Floci. The sidecar's port is bound by Docker, so it needs noports:entry of your own, and its logs are streamed into CloudWatch Logs under/floci/ui.

Starting a container needs the Docker socket:

services
:
 
floci
:
 
image
: 
floci/floci:latest

 
ports
:
 - 
"
4566:4566
"

 
volumes
:
 - 
/var/run/docker.sock:/var/run/docker.sock

Variable

Default

Description

FLOCI_SERVICES_UI_ENABLED

true

Enable the console sidecar

FLOCI_SERVICES_UI_IMAGE

floci/floci-ui:0.7.0

Console image to run

FLOCI_SERVICES_UI_CONTAINER_NAME

floci-ui

Name of the sidecar container

FLOCI_SERVICES_UI_PORT

4500

Host port the console is published on

FLOCI_SERVICES_UI_BIND_ADDRESS

(none)

Host interface that port is published on. Unset publishes on every interface; set 
127.0.0.1
 when Floci's own port is loopback-only

FLOCI_SERVICES_UI_KEEP_RUNNING_ON_SHUTDOWN

false

Leave the sidecar running when Floci stops

### Running a different console

The console is not fixed to the one Floci ships. Any console implementing theFloci console contractruns with nothing but an image name: listen on the port inPORT, serveGET /api/health, talk to Floci atAWS_ENDPOINT_URL.

environment
:
 
FLOCI_SERVICES_UI_IMAGE
: 
acme/my-console:1.0

A console that differs from the contract's defaults says so in its ownio.floci.console.*image labels, so its operators do not have to.StackPort, for example, listens on 8080 rather than 4500; on an image that predates the labels, say it by hand:

environment
:
 
FLOCI_SERVICES_UI_IMAGE
: 
davireis/stackport:latest

 
FLOCI_SERVICES_UI_CONTAINER_NAME
: 
floci-stackport

 
FLOCI_SERVICES_UI_PORT
: 
"
8080
"

 
FLOCI_SERVICES_UI_INTERNAL_PORT
: 
"
8080
"

Floci Dashis another. It honoursPORT, so only the two things it does differ on need naming:

environment
:
 
FLOCI_SERVICES_UI_IMAGE
: 
ghcr.io/ofsazib/floci-dash:latest

 
FLOCI_SERVICES_UI_CONTAINER_NAME
: 
floci-dash

 
FLOCI_SERVICES_UI_ENDPOINT_ENV
: 
FLOCI_URL

 
FLOCI_SERVICES_UI_STATUS_PATH
: 
/api/healthz

The endpoint itself is never configured by hand: Floci resolves its own reachable address at start time and injects it asAWS_ENDPOINT_URL.

Full reference:Web ConsoleandConsole Contract v1.

## Features

Local AWS without the cloud account

Run AWS-compatible services locally without an AWS account, auth token, or paid feature gates.

Real Docker where fidelity matters

Lambda, RDS, Neptune, ElastiCache, MSK, ECS, EC2, EKS, OpenSearch, CodeBuild, and Managed Service for Apache Flink use real Docker-backed execution instead of shallow mocks.

Drop-in AWS compatibility

Point standard AWS clients athttp://localhost:4566. Existing credentials, regions, SDKs, CLI commands, and IaC workflows stay familiar.

Terraform can provision AWS-shaped resources locally through Floci using the standard HashiCorp AWS provider. See theTerraform with Floci guidefor provider configuration, resource examples, and optional emulated S3 state.

Fast enough for CI

The native image starts in milliseconds and keeps idle memory low, making it practical for local development and test pipelines.

Configurable persistence

Choose from in-memory, persistent, hybrid, and write-ahead log storage depending on the durability profile you need.

## Why Floci?

LocalStack's community editionsunset in March 2026, requiring auth tokens and freezing security updates. Floci is the no-strings-attached alternative.

Capability

Floci

LocalStack Community

Auth token required

No

Yes

Security updates

Yes

Frozen

Startup time

~24 ms

~3.3 s

Idle memory

~13 MiB

~143 MiB

Docker image size

~90 MB

~1.0 GB

License

MIT

Restricted

API Gateway v2 / HTTP API

Yes

No

Cognito

Yes

No

RDS, ElastiCache, MSK

Real Docker

No

Neptune (graph DB + Gremlin WebSocket)

Real Docker

No

DocumentDB (MongoDB-compatible)

Real Docker

No

ECS, EC2, EKS

Real Docker

No

CodeBuild

Real Docker execution

No

Native binary

~40 MB

No

Broad AWS coverage. Free forever.See theServices Overviewfor the full list of emulated services.

## Architecture Overview

flowchart LR
 Client["AWS SDK / CLI"]

 subgraph Floci ["Floci, port 4566"]
 Router["HTTP Router\nJAX-RS / Vert.x"]

 subgraph Stateless ["Stateless Services"]
 A["SSM · SQS · SNS\nIAM · STS · KMS\nSecrets Manager · SES\nCognito · Kinesis\nEventBridge · Scheduler · AppConfig\nCloudWatch · Step Functions\nCloudFormation · ACM · Config · CloudTrail\nAPI Gateway · AppSync · ELB v2 · Auto Scaling\nElastic Beanstalk · CodeDeploy · CodePipeline · Backup · FIS · Bedrock Runtime · Bedrock AgentCore · Route53 · Transfer"]
 end

 subgraph Stateful ["Stateful Services"]
 B["S3 · DynamoDB\nDynamoDB Streams"]
 end

 subgraph Containers ["Container Services"]
 C["Lambda\nElastiCache\nRDS\nNeptune\nECS\nEC2\nMSK\nEKS\nOpenSearch\nCodeBuild\nManaged Flink"]
 D["Athena -> floci-duck\nDuckDB sidecar"]
 end

 Router --> Stateless
 Router --> Stateful
 Router --> Containers
 Stateless & Stateful --> Store[("StorageBackend\nmemory · hybrid · persistent · wal")]
 end

 Docker["Docker Engine"]
 Client -->|"HTTP :4566\nAWS wire protocol"| Router
 Containers -->|"Docker API\nIAM / SigV4 auth"| Docker

 
Loading

## Supported Services

Floci supports local emulation for application services, data services, eventing, identity, infrastructure, billing, and container-backed workloads.

Category

Services

Core app services

S3, SQS, SNS, DynamoDB, Lambda, Lambda MicroVMs, Lambda Web Functions, IAM, STS, KMS, Payment Cryptography, Secrets Manager, SSM

Events and workflows

EventBridge, EventBridge V2, EventBridge Pipes, EventBridge Scheduler, Step Functions, SWF, CloudWatch Logs, CloudWatch Metrics, CloudWatch OAM, CloudWatch RUM, Managed Prometheus (AMP)

API and identity

API Gateway REST, API Gateway v2, AppSync, Cognito, Cognito Identity, ACM, Route53, Route 53 Resolver, Cloud Map, Global Accelerator

Containers and compute

ECS, EC2, Lightsail, EKS, MWAA, ECR, EFS, CodeBuild, CodeDeploy, CodePipeline, CodeGuru Reviewer, CodeArtifact, AWS Batch, Auto Scaling, Application Auto Scaling, Elastic Beanstalk, ELB v2, ELB Classic

Data, analytics, and AI

Athena, Glue, Lake Formation, EMR, EMR Serverless, Redshift, Redshift Data API, Redshift Serverless, Firehose, Managed Service for Apache Flink, OpenSearch, S3 Tables, S3 Vectors, Textract, Transcribe, Comprehend, Rekognition, Translate, Bedrock, Bedrock Runtime, Bedrock AgentCore, Bedrock AgentCore Control, SageMaker

Databases and caching

Aurora DSQL, RDS, RDS Data API, Neptune, DocumentDB, DMS, MemoryDB, ElastiCache, Timestream for InfluxDB

Messaging and transfer

SES, Kinesis, MSK, Amazon MQ, Transfer Family, DataSync, IoT Core, Amazon Connect, Amazon AppIntegrations

Security and governance

AWS Network Firewall, AWS RAM, Service Quotas, WAF v2, GuardDuty, Amazon Inspector, CloudTrail, CloudFront, Resource Groups Tagging API, Resource Explorer 2, CloudHSM v2, Organizations, AWS Account Management, IAM Access Analyzer, IAM Identity Center (SSO Admin, OIDC, Access Portal, SCIM), Identity Store, Amazon Macie, Amazon Detective, Security Hub, Amazon Verified Permissions, Control Catalog, Control Tower, Service Catalog, AWS Marketplace

Cost and billing

AWS Budgets, Pricing, Cost Explorer, Cost and Usage Reports, BCM Pricing Calculator, BCM Data Exports

Resilience, backup, and config

AWS FIS, AWS Backup, Amazon Data Lifecycle Manager, AWS Config, AppConfig, AppConfigData, CloudFormation, Cloud Control API

For operation-level compatibility, see theServices Overview.

Detailed service notes

Service

How it works

Notable features

SSM

In-process + EC2 containers

Parameter Store (version history, labels, SecureString, tagging); Run Command (SendCommand, GetCommandInvocation, direct EC2 container execution, agent polling)

SQS

In-process

Standard and FIFO queues, DLQ, visibility timeout, batch operations, tagging

SNS

In-process

Topics, subscriptions, SQS, Lambda and HTTP delivery, tagging

S3

In-process

Versioning, multipart upload, pre-signed URLs, Object Lock, object annotations, event notifications

S3 Vectors

In-process

Vector buckets, indexes, put / get / list / delete vectors, cosine similarity queries

DynamoDB

In-process

GSI, LSI, Query, Scan, TTL, transactions, batch operations; Streams with shard iterators and Lambda event source mapping

Lambda

Real Docker

Runtime environment, execution model, warm container pool, aliases, Function URLs

API Gateway REST

In-process

Resources, methods, stages, Lambda proxy, MOCK integrations, AWS integrations

API Gateway v2

In-process

HTTP APIs, routes, integrations, JWT authorizers, stages

AppSync

In-process

GraphQL API management API, schema registry, AWS scalars, domain names, channel namespaces

IAM

In-process

Users, roles, groups, policies, instance profiles, access keys; STS AssumeRole, WebIdentity, SAML, GetFederationToken, GetSessionToken

Cognito

In-process

User pools, app clients, auth flows, JWKS and OpenID well-known endpoints

KMS

In-process

Encrypt, decrypt, sign, verify, data keys, aliases

Payment Cryptography

In-process

Keys with real AES-256 material and check values, aliases, tagging

Kinesis

In-process

Streams, shards, enhanced fan-out, split and merge

Secrets Manager

In-process

Versioning, resource policies, tagging

Step Functions

In-process

ASL execution, task tokens, execution history

SWF

In-process

Decision and activity tasks, timers, child workflows, timeouts, real Lambda invocation

CloudFormation

In-process

Stacks, change sets, resource provisioning, StackSets (cross-account instances)

EventBridge

In-process

Custom buses, rules, SQS, SNS and Lambda targets

EventBridge V2

In-process

Event buses and filtered subscribers delivering to SQS

EventBridge Pipes

In-process

Poller-based integration connecting SQS, Kinesis, DynamoDB, and MSK sources to targets with optional filtering

EventBridge Scheduler

In-process

Schedule groups, schedules, flexible time windows, retry policies, DLQs

CloudWatch Logs

In-process

Log groups, streams, ingestion, filtering

CloudWatch Metrics

In-process

Custom metrics, statistics, alarms

CloudWatch OAM

In-process

Full 15-operation sink, policy, cross-account link, and tagging API

ElastiCache

Real Docker

Redis / Valkey protocol, IAM auth, SigV4 validation

MemoryDB

Real Docker

Redis / Valkey protocol via real containers; JSON 1.1 control plane; reuses ElastiCache RESP proxy

Aurora DSQL

Real Docker, mock mode available

PostgreSQL 16 per cluster behind a TLS endpoint with IAM token auth, 
AWS IAM GRANT
 role mappings; not yet DSQL's limits and async indexes

RDS

Real Docker

PostgreSQL, MySQL, MariaDB, IAM auth, JDBC-compatible engines

Timestream for InfluxDB

Real Docker, mock mode available

InfluxDB 2.x DB instances and read replica clusters via 
influxdb:2.7
; initial auth secret in Secrets Manager; backups and restore through the influx CLI

RDS Data API

REST JSON over real RDS containers

Raw SQL execution and transactions for local MySQL / MariaDB RDS resources

Neptune

Real Docker

Graph DB via TinkerPop Gremlin Server (default) or Neo4j for openCypher/Bolt (
NEPTUNE_DB_TYPE
); RDS-shaped control plane; SigV4 proxy on port 8182

DocumentDB

Real Docker, mock mode available

MongoDB-compatible cluster via real MongoDB containers; RDS-shaped control plane; MongoDB wire protocol on port 27017

MSK

Real Docker

Kafka-compatible broker via Redpanda

Amazon MQ

Real Docker

RabbitMQ broker via rabbitmq:3-management; AMQP + management console

Athena

In-process with DuckDB sidecar

Real SQL execution over S3 and Glue-backed views

Glue

In-process

Data Catalog, Schema Registry, tables consumed by Athena

EMR

In-process

Cluster (job flow) lifecycle, instance groups and fleets (including resizing), bootstrap actions, steps, security configurations, scaling and termination policies, block public access, tagging

Data Firehose

In-process

Streaming delivery, buffered flush to S3 with GZIP/ZIP/Snappy compression

Managed Service for Apache Flink

Real Docker

Kinesis Analytics V2 control plane; StartApplication runs a real Flink cluster (JobManager + TaskManager, image per RuntimeEnvironment), pulls the application JAR from local S3, and submits the job

ECS

Real Docker

Clusters, task definitions, tasks, services, capacity providers, task sets

EC2

Real Docker

RunInstances launches containers, SSH key injection, UserData, IMDS, VPC resources

Lightsail

In-process

Instances, disks, static IPs, key pairs, ports, tags, regions, blueprints, bundles, operations

ACM

In-process

Certificate issuance and validation lifecycle

ECR

In-process with real registry

Repositories, docker push / pull, image-backed Lambda functions

Resource Groups Tagging API

In-process

GetResources, tag and untag resources, tag key and value discovery across services

SES

In-process

v1 and v2 APIs: send email, raw email, identity verification, DKIM, templates, configuration sets, account sending

OpenSearch

Real Docker

Domain CRUD, tags, versions, instance types, upgrade stubs

AppConfig

In-process

Applications, environments, profiles, hosted versions, deployments

AppConfigData

In-process

Configuration sessions and dynamic configuration retrieval

Bedrock

In-process

Guardrail lifecycle, versions, and tags on the control plane

Bedrock Runtime

In-process stub

Dummy Converse and InvokeModel responses for local development

Bedrock AgentCore

In-process stub

Stateful control plane (agent runtimes, gateways, memory, workload identity); canned InvokeAgentRuntime responses

EKS

Real Docker, mock mode available

k3s clusters with live Kubernetes API server

MWAA

Real Docker, mock mode available

Real Apache Airflow (LocalExecutor) + Postgres metadata DB per environment; web/CLI proxy; S3-backed DAG sync

ELB v2

In-process

ALB, NLB, target groups, listeners, routing rules, Lambda targets, tags

CodeBuild

In-process with real Docker

Real buildspec execution, CloudWatch logs, S3 artifacts

CodeDeploy

In-process with Lambda traffic shifting

Deployment groups, configs, lifecycle hooks, auto-rollback

CodePipeline

In-process orchestration

Pipelines, executions, S3 artifacts, approvals, local providers, custom workers

AWS Network Firewall

In-process

DescribeFirewall with stable emulated endpoint attachments for infrastructure tooling

Service Quotas

In-process

Generated quota catalog with generous static values; real quota codes for CodeBuild and Lambda concurrency

AWS RAM

In-process

EnableSharingWithAwsOrganization opt-in

AWS Batch

In-process

Compute environments, job queues, job definitions, job submission and lifecycle

Auto Scaling

In-process with reconciler

Launch configs, ASGs, desired capacity reconciliation, lifecycle hooks

Application Auto Scaling

In-process

Scalable targets, target-tracking and step scaling policies, CloudWatch alarm creation, tagging (policies are stored but inert)

Elastic Beanstalk

In-process

Applications, application versions, environments, configuration templates, platform and solution stack metadata

AWS Backup

In-process

Vaults, backup plans, selections, simulated job lifecycle, recovery points

Amazon Data Lifecycle Manager

In-process

Lifecycle policy and tag management; schedules are stored but do not create snapshots or AMIs

AWS FIS

In-process

All 26 management APIs for templates, experiments, target accounts, action and target discovery, safety lever, tagging, and pagination; experiment execution is a safe control-plane simulation and does not inject faults into other services

AWS Config

In-process

Config rules, evaluation-driven compliance (PutEvaluations, compliance details and summaries), configuration recorders, delivery channels, retention configuration, conformance packs, tagging

Organizations

In-process

Organizations, roots, nested OUs, member accounts, all policy types with 
FullAWSAccess
 and effective-policy inheritance, trusted service access, delegated administrators, resource policy, and the full invitation/handshake flow; created accounts are usable Floci accounts and member accounts can read the organization they belong to

CloudTrail

In-process

Trails, event selectors (S3 data events with bucket/prefix matching), 
StartLogging
/
StopLogging
, scheduled gzipped log file emission to the destination bucket at AWS-shaped key paths, IAM-deny path emits 
AccessDenied
 records

CloudFront

In-process

Distributions, origins, cache behaviors, invalidations, tagging

WAF v2

In-process

Web ACLs, IP sets, regex pattern sets, rule groups, logging configs, resource associations, tagging (REGIONAL and CLOUDFRONT scopes)

AWS Resource Groups

In-process

Five capacity-pool operations: stored groups, verified EC2 reservation membership, scoped pagination and group deletion; no dynamic queries or capacity allocation

Resource Explorer 2

In-process

All 32 management APIs: index and view lifecycle, multi-Region setup tasks, the full search query grammar, and tagging; 30 services expose their resources for search, gathered live rather than from an index

Route53

In-process

Hosted zones, SOA and NS records, resource record sets, change tracking, tagging

Cloud Map

In-process

HTTP and DNS namespaces, services, instance registration, discovery queries, operations, tagging

Transfer Family

In-process

Server lifecycle, user management, SSH key import, tagging

Textract

In-process stub

API-compatible stubs, dummy block data, async job simulation

Transcribe

In-process stub

Transcription jobs and custom vocabularies; jobs complete immediately, no real audio processing

Pricing

In-process with static snapshot

Product discovery, attributes, price list files, pagination

Cost Explorer

In-process

Cost synthesized from Floci resource state and pricing snapshots

Cost and Usage Reports

In-process with floci-duck sidecar

CUR 2.0 and FOCUS 1.2 columns, account-scoped storage, Parquet emission

BCM Pricing Calculator

In-process

Workload estimate create, usage pricing, read, and delete lifecycle

BCM Data Exports

In-process

Export lifecycle, executions, update and delete operations

## Real Docker Integration

Floci uses real Docker containers when in-process emulation would reduce fidelity. This applies to stateful databases, connection-heavy protocols, runtimes, and build systems.

Service

Default image

What is real

Lambda

public.ecr.aws/lambda/<runtime>

AWS runtime environment, execution model, warm container pool

ElastiCache

valkey/valkey:8

Redis / Valkey protocol, ACL-based IAM auth, SigV4 validation

RDS PostgreSQL

postgres:16-alpine

PostgreSQL engine, IAM auth, JDBC-compatible access

RDS MySQL / Aurora

mysql:8.0

MySQL engine, IAM auth, JDBC-compatible access

RDS MariaDB

mariadb:11

MariaDB engine, IAM auth, JDBC-compatible access

Neptune

tinkerpop/gremlin-server:3.7.3

TinkerPop Gremlin Server; Gremlin WebSocket on port 8182; SigV4 auth proxy

Neptune (openCypher)

neo4j:5-community

Neo4j backend when 
FLOCI_SERVICES_NEPTUNE_DB_TYPE=neo4j
; openCypher over Bolt

DocumentDB

mongo:7.0

MongoDB engine; MongoDB wire protocol on port 27017

MSK

redpandadata/redpanda:latest

Kafka-compatible broker via Redpanda

Amazon MQ

rabbitmq:3-management

RabbitMQ broker; AMQP on port 5672, management console on 15672

Managed Service for Apache Flink

apache/flink:<version>

Apache Flink JobManager; image chosen per RuntimeEnvironment (FLINK-1_15 … FLINK-1_20, FLINK-2_0 … FLINK-2_3)

EC2

AMI-mapped Linux images

Linux containers, SSH key injection, UserData, IMDS, IAM credentials

ECS

User-specified task image

Container lifecycle, start, stop, health checks

EKS

rancher/k3s:latest

Kubernetes API server via k3s

MWAA

apache/airflow:<version>-python3.12
 + 
postgres:16-alpine

Real Apache Airflow (LocalExecutor: scheduler + webserver) with its own Postgres metadata DB; webserver/CLI reachable via Floci's proxy

CodeBuild

User-specified environment image

Buildspec execution, log streaming, S3 artifact upload

OpenSearch

opensearchproject/opensearch:2

Full OpenSearch engine with REST API

ECR

registry:2

OCI-compatible registry for docker push and docker pull

Verified Permissions

floci/floci-sidecar-cedar:1.1.0

Cedar 4 policy parsing, schema validation and authorization decisions, via a 
Floci sidecar

AppSync

floci/floci-sidecar-graphql:0.2.0

graphql-java schema validation, query planning and execution, via a 
Floci sidecar

Docker-backed services require the Docker socket:

docker run -d --name floci \
 -p 4566:4566 \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -u root \
 floci/floci:latest

### Overriding default images

Variable

Default

FLOCI_SERVICES_ELASTICACHE_DEFAULT_IMAGE

valkey/valkey:8

FLOCI_SERVICES_RDS_DEFAULT_POSTGRES_IMAGE

postgres:16-alpine

FLOCI_SERVICES_RDS_DEFAULT_MYSQL_IMAGE

mysql:8.0

FLOCI_SERVICES_RDS_DEFAULT_MARIADB_IMAGE

mariadb:11

FLOCI_SERVICES_MSK_DEFAULT_IMAGE

redpandadata/redpanda:latest

FLOCI_SERVICES_OPENSEARCH_DEFAULT_IMAGE

(unset — images resolve per requested 
EngineVersion
)

FLOCI_SERVICES_KINESIS_ANALYTICS_DEFAULT_IMAGE

(unset; chosen per RuntimeEnvironment)

FLOCI_SERVICES_NEPTUNE_DEFAULT_IMAGE

tinkerpop/gremlin-server:3.7.3

FLOCI_SERVICES_NEPTUNE_DEFAULT_NEO4J_IMAGE

neo4j:5-community

FLOCI_SERVICES_DOCDB_DEFAULT_IMAGE

mongo:7.0

FLOCI_SERVICES_EKS_DEFAULT_IMAGE

rancher/k3s:latest

FLOCI_SERVICES_MWAA_DEFAULT_POSTGRES_IMAGE

postgres:16-alpine

FLOCI_SERVICES_ECR_REGISTRY_IMAGE

registry:2

FLOCI_SERVICES_LAMBDA_ECR_BASE_URI

public.ecr.aws

## Persistence and Storage Modes

Floci can trade speed for durability depending on the workflow. Configure the default mode withFLOCI_STORAGE_MODE, or override storage per service.

Mode

Behavior

Best for

Durability

memory

Entirely in RAM. Data is lost when the container stops.

CI and ephemeral tests

None

persistent

Loaded at startup and flushed to disk immediately on every write operation.

Simple local state preservation with immediate persistence

Medium

hybrid

In-memory performance with periodic async flushing every 5 seconds.

Local development

Good

wal

Write-ahead log. Every mutation is logged before responding.

Maximum durability

Highest

Usememoryfor fast test runs. Usehybridwhen you want state preserved across container restarts without much overhead.

For more detail, see theStorage Configuration documentation.

## Multi-Account Isolation

Floci supports per-account resource isolation with no extra setup. IfAWS_ACCESS_KEY_IDis exactly 12 digits, Floci uses it as the account ID. Resources created by one account are invisible to another.

AWS_ACCESS_KEY_ID=111111111111 aws sqs create-queue --queue-name orders
AWS_ACCESS_KEY_ID=222222222222 aws sqs create-queue --queue-name orders

Any other key format, such astestorAKIA..., causes Floci to fall back toFLOCI_DEFAULT_ACCOUNT_ID, which defaults to000000000000.

STS temporary credentials are routed too: credentials fromAssumeRoleresolve to the assumed role's account, so the cross-account assume-role-then-provision pattern works locally. Resolution precedence is 12-digit AKID → temporary-session lookup →FLOCI_DEFAULT_ACCOUNT_ID.

See theMulti-Account Isolation docs.

## SDK Integration

Point your existing AWS SDK athttp://localhost:4566.

Java, AWS SDK v2

var
 
client
 = 
DynamoDbClient
.
builder
()
 .
endpointOverride
(
URI
.
create
(
"http://localhost:4566"
))
 .
region
(
Region
.
US_EAST_1
)
 .
credentialsProvider
(
StaticCredentialsProvider
.
create
(
 
AwsBasicCredentials
.
create
(
"test"
, 
"test"
)))
 .
build
();

client
.
createTable
(
b
 -> 
b

 .
tableName
(
"demo-table"
)
 .
billingMode
(
BillingMode
.
PAY_PER_REQUEST
)
 .
attributeDefinitions
(
 
AttributeDefinition
.
builder
().
attributeName
(
"pk"
).
attributeType
(
ScalarAttributeType
.
S
).
build
())
 .
keySchema
(
 
KeySchemaElement
.
builder
().
attributeName
(
"pk"
).
keyType
(
KeyType
.
HASH
).
build
()));

System
.
out
.
println
(
client
.
listTables
().
tableNames
());

Python, boto3

import
 
boto3

client
 
=
 
boto3
.
client
(
 
"ssm"
,
 
endpoint_url
=
"http://localhost:4566"
,
 
region_name
=
"us-east-1"
,
 
aws_access_key_id
=
"test"
,
 
aws_secret_access_key
=
"test"
,
)

client
.
put_parameter
(
 
Name
=
"/demo/app/message"
,
 
Value
=
"hello from floci"
,
 
Type
=
"String"
,
 
Overwrite
=
True
,
)

response
 
=
 
client
.
get_parameter
(
Name
=
"/demo/app/message"
)

print
(
response
[
"Parameter"
][
"Value"
])

Node.js, AWS SDK v3

import
 
{
 
SQSClient
,
 
SendMessageCommand
 
}
 
from
 
"@aws-sdk/client-sqs"
;

const
 
client
 
=
 
new
 
SQSClient
(
{

 
endpoint
: 
"http://localhost:4566"
,

 
region
: 
"us-east-1"
,

 
credentials
: 
{
 
accessKeyId
: 
"test"
,
 
secretAccessKey
: 
"test"
 
}
,

}
)
;

await
 
client
.
send
(

 
new
 
SendMessageCommand
(
{

 
QueueUrl
: 
"http://localhost:4566/000000000000/demo-queue"
,

 
MessageBody
: 
"hello from floci"
,

 
}
)
,

)
;

Go, AWS SDK v2

package
 main

import
 (
 
"context"

 
"fmt"

 
"log"

 
"github.com/aws/aws-sdk-go-v2/config"

 
"github.com/aws/aws-sdk-go-v2/credentials"

 
"github.com/aws/aws-sdk-go-v2/service/s3"

)

func
 
main
() {
 
cfg
, 
err
 
:=
 
config
.
LoadDefaultConfig
(
context
.
TODO
(),
 
config
.
WithRegion
(
"us-east-1"
),
 
config
.
WithCredentialsProvider
(
 
credentials
.
NewStaticCredentialsProvider
(
"test"
, 
"test"
, 
""
),
 ),
 
config
.
WithBaseEndpoint
(
"http://localhost:4566"
),
 )
 
if
 
err
 
!=
 
nil
 {
 
log
.
Fatal
(
err
)
 }

 
client
 
:=
 
s3
.
NewFromConfig
(
cfg
, 
func
(
o
 
*
s3.
Options
) {
 
o
.
UsePathStyle
 
=
 
true

 })

 
out
, 
err
 
:=
 
client
.
ListBuckets
(
context
.
TODO
(), 
nil
)
 
if
 
err
 
!=
 
nil
 {
 
log
.
Fatal
(
err
)
 }

 
fmt
.
Println
(
out
.
Buckets
)
}

Rust, AWS SDK

use
 aws_sdk_secretsmanager
::
config
::
{
Credentials
,
 
Region
}
;

use
 aws_sdk_secretsmanager
::
Client
;

#
[
tokio
::
main
]

async
 
fn
 
main
(
)
 -> 
Result
<
(
)
,
 
Box
<
dyn
 std
::
error
::
Error
>
>
 
{

 
let
 config = aws_config
::
defaults
(
aws_config
::
BehaviorVersion
::
latest
(
)
)

 
.
region
(
Region
::
new
(
"us-east-1"
)
)

 
.
credentials_provider
(
Credentials
::
new
(
"test"
,
 
"test"
,
 
None
,
 
None
,
 
"floci"
)
)

 
.
endpoint_url
(
"http://localhost:4566"
)

 
.
load
(
)

 
.
await
;

 
let
 client = 
Client
::
new
(
&
config
)
;

 client
 
.
create_secret
(
)

 
.
name
(
"demo/secret"
)

 
.
secret_string
(
"hello from floci"
)

 
.
send
(
)

 
.
await
?
;

 
Ok
(
(
)
)

}

Bash, AWS CLI

export
 AWS_ACCESS_KEY_ID=test

export
 AWS_SECRET_ACCESS_KEY=test

export
 AWS_DEFAULT_REGION=us-east-1

aws --endpoint-url http://localhost:4566 s3 mb s3://my-bucket
aws --endpoint-url http://localhost:4566 s3 ls

## Testcontainers

Floci has Testcontainers modules for starting isolated Floci instances directly from tests. This avoids shared state, manual daemon setup, and port conflicts.

For Testcontainers 1.x, use the versions as indicated in the table below.

Language

Package

Latest

Registry

Source

Java

io.floci:testcontainers-floci

1.14.0

Maven Central

GitHub

Node.js

@floci/testcontainers

0.1.0

npm

GitHub

Python

testcontainers-floci

0.1.1

PyPI

GitHub

.NET

Testcontainers.Floci

see releases

GitHub Packages

GitHub

Go

In progress

In progress

N/A

GitHub

Java

<
dependency
>
 <
groupId
>io.floci</
groupId
>
 <
artifactId
>testcontainers-floci</
artifactId
>
 <
version
>1.14.0</
version
>
 <
scope
>test</
scope
>
</
dependency
>

@
Testcontainers

class
 
S3IntegrationTest
 {

 
@
Container

 
static
 
FlociContainer
 
floci
 = 
new
 
FlociContainer
();

 
@
Test

 
void
 
shouldCreateBucket
() {
 
S3Client
 
s3
 = 
S3Client
.
builder
()
 .
endpointOverride
(
URI
.
create
(
floci
.
getEndpoint
()))
 .
region
(
Region
.
of
(
floci
.
getRegion
()))
 .
credentialsProvider
(
StaticCredentialsProvider
.
create
(
 
AwsBasicCredentials
.
create
(
floci
.
getAccessKey
(), 
floci
.
getSecretKey
())))
 .
forcePathStyle
(
true
)
 .
build
();

 
s3
.
createBucket
(
b
 -> 
b
.
bucket
(
"my-bucket"
));
 }
}

For Testcontainers 2.x / Spring Boot 4.x, use version2.15.0.

Node.js / TypeScript

npm install --save-dev @floci/testcontainers

import
 
{
 
FlociContainer
 
}
 
from
 
"@floci/testcontainers"
;

import
 
{
 
S3Client
,
 
CreateBucketCommand
 
}
 
from
 
"@aws-sdk/client-s3"
;

describe
(
"S3"
,
 
(
)
 
=>
 
{

 
let
 
floci
: 
FlociContainer
;

 
beforeAll
(
async
 
(
)
 
=>
 
{

 
floci
 
=
 
await
 
new
 
FlociContainer
(
)
.
start
(
)
;

 
}
)
;

 
afterAll
(
async
 
(
)
 
=>
 
{

 
await
 
floci
.
stop
(
)
;

 
}
)
;

 
it
(
"creates a bucket"
,
 
async
 
(
)
 
=>
 
{

 
const
 
s3
 
=
 
new
 
S3Client
(
{

 
endpoint
: 
floci
.
getEndpoint
(
)
,

 
region
: 
floci
.
getRegion
(
)
,

 
credentials
: 
{

 
accessKeyId
: 
floci
.
getAccessKey
(
)
,

 
secretAccessKey
: 
floci
.
getSecretKey
(
)
,

 
}
,

 
forcePathStyle
: 
true
,

 
}
)
;

 
await
 
s3
.
send
(
new
 
CreateBucketCommand
(
{
 
Bucket
: 
"my-bucket"
 
}
)
)
;

 
}
)
;

}
)
;

Python

pip install testcontainers-floci

import
 
boto3

from
 
floci
 
import
 
FlociContainer

def
 
test_s3_create_bucket
():
 
with
 
FlociContainer
() 
as
 
floci
:
 
s3
 
=
 
boto3
.
client
(
 
"s3"
,
 
endpoint_url
=
floci
.
get_endpoint
(),
 
region_name
=
floci
.
get_region
(),
 
aws_access_key_id
=
floci
.
get_access_key
(),
 
aws_secret_access_key
=
floci
.
get_secret_key
(),
 )
 
s3
.
create_bucket
(
Bucket
=
"my-bucket"
)

## Compatibility Testing

Thecompatibility-testsdirectory validates Floci across SDKs and tooling workflows.

Module

Language / Tool

SDK / Client

Tests

sdk-test-java

Java 17

AWS SDK for Java v2

1,326

sdk-test-node

Node.js

AWS SDK for JavaScript v3

449

sdk-test-python

Python 3

boto3

311

sdk-test-go

Go

AWS SDK for Go v2 + RDS Data API SDK v1

157

sdk-test-awscli

Bash

AWS CLI v2

205

compat-terraform

Terraform

v1.10+

67

compat-opentofu

OpenTofu

v1.9+

41

compat-cdk

AWS CDK

v2+

20

2,576 automated compatibility tests across 5 SDKs and 3 IaC tools.

## Migrating from LocalStack

Floci is a drop-in replacement for LocalStack Community. The port, credentials, SDK configuration, and CLI endpoint pattern work the same way. Swap the image and keep going.

#
 Before

image
: 
localstack/localstack

#
 After, standard image

image
: 
floci/floci:latest

#
 After, if init scripts need AWS CLI or boto3

image
: 
floci/floci:latest-compat

LocalStack environment variables are translated automatically:

LocalStack

Floci equivalent

LOCALSTACK_HOST

FLOCI_HOSTNAME

PERSISTENCE=1

FLOCI_STORAGE_MODE=persistent

LAMBDA_DOCKER_NETWORK

FLOCI_SERVICES_LAMBDA_DOCKER_NETWORK

LAMBDA_REMOVE_CONTAINERS=1

FLOCI_SERVICES_LAMBDA_EPHEMERAL=true

DEBUG=1

QUARKUS_LOG_LEVEL=DEBUG

Init scripts mounted under/etc/localstack/init/run unchanged. The/_localstack/initand/_localstack/healthendpoints are still served. Once the emulator is up, the log also ends with a LocalStack-styleReady.line, so tooling that watches the log for it, such as the default wait strategy of Testcontainers'LocalStackContainer, works unchanged. SetLOCALSTACK_PARITY=falseto opt out of automatic translation.

See thefull migration guide.

## Image Tags

Every tag combines a variant and a channel.

Channel

Standard

Baseline (ARM64 only)

Compat with AWS CLI and boto3

Release, floating

latest

latest-baseline

latest-compat

Release, pinned

x.y.z

x.y.z-baseline

x.y.z-compat

Nightly, floating

nightly

—

nightly-compat

Nightly, dated

nightly-mmddyyyy

—

nightly-mmddyyyy-compat

Uselatestfor stable releases, a pinned version for reproducible builds, andnightlyto trackmain.

#
 Recommended

image
: 
floci/floci:latest

#
 Includes AWS CLI and boto3

image
: 
floci/floci:latest-compat

#
 ARM64 baseline for Raspberry Pi 4 / pre-LSE cores

image
: 
floci/floci:latest-baseline

#
 Pinned release

image
: 
floci/floci:x.y.z

#
 Track main

image
: 
floci/floci:nightly

### Release train

Stable releases ship on the15th and the last day of each month, cut automatically at 00:30 US Central time. Between trains,floci/floci:nightlytracksmain. Every merged fix is available the next day, and datednightly-mmddyyyytags let you pin a specific night's build.

Versions are derived from Conventional Commits bysemantic-release;CHANGELOG.mdis generated, never hand-edited. Releases are cut frommainonly: there are no maintenance branches.

## Configuration

All settings are overridable through environment variables with theFLOCI_prefix.

Variable

Default

Description

FLOCI_PORT

4566

Port exposed by the Floci API

FLOCI_DEFAULT_REGION

us-east-1

Default AWS region

FLOCI_DEFAULT_ACCOUNT_ID

000000000000

Default AWS account ID

FLOCI_BASE_URL

http://localhost:4566

Base URL used when Floci returns service URLs

FLOCI_HOSTNAME

Unset

Hostname used in returned URLs when Floci runs inside Docker Compose

FLOCI_STORAGE_MODE

memory

Storage mode: 
memory
, 
persistent
, 
hybrid
, or 
wal

FLOCI_STORAGE_PERSISTENT_PATH

./data

Directory used for persisted state

FLOCI_SERVICES_LAMBDA_ECR_BASE_URI

public.ecr.aws

ECR base URI used when pulling Lambda runtime images (legacy name 
FLOCI_ECR_BASE_URI
 still works)

FLOCI_SERVICES_S3_ENFORCE_AUTH

false

Enforce S3 public/private read access and reject unknown signed S3 access keys

Full reference:configuration docs

### Multi-container Docker Compose

When your application runs in a different container, setFLOCI_HOSTNAMEto the Floci service name so returned URLs, such as SQSQueueUrlvalues, resolve correctly.

services
:
 
floci
:
 
image
: 
floci/floci:latest

 
ports
:
 - 
"
4566:4566
"

 
environment
:
 - 
FLOCI_HOSTNAME=floci

 
my-app
:
 
environment
:
 - 
AWS_ENDPOINT_URL=http://floci:4566

 
depends_on
:
 - 
floci

Without this, services may return URLs usinglocalhost, which points to the wrong container from the application container.

## Community

Join the Floci community onSlackorGitHub Discussions. Feature ideas, compatibility questions, design tradeoffs, and rough proposals are welcome.

## Sponsors

Floci is independent open source, funded by the people and companies who use it.
Sponsorship buys gratitude and nothing else: every emulated service is free for
everyone, forever, and no sponsor gets features, priority, or roadmap influence
that the rest of the Flock does not.

### 🥇 Gold

Large logo with top placement in the emulator READMEs and on floci.io, plus a
mention in release notes.

IceGuard·Softmax

### 🥈 Silver

Logo in the emulator READMEs and on floci.io, plus a mention in release notes.

Your logo here.Become a sponsor.

### 🥉 Community

Name in the emulator READMEs, a sponsor badge on GitHub, and our sincere thanks.

AutoScout24·Nexxion AI

Every sponsor, including the Friends of the Flock who support Floci outside these
tiers, is listed inTHANKS.md.

Sponsor Floci

## Star History

## Contributors

## License

MIT. Use it however you want.