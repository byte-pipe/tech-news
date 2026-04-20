---
title: MiniStack — Free Open-Source Local AWS Emulator
url: https://ministack.org/
site_name: hnrss
content_file: hnrss-ministack-free-open-source-local-aws-emulator
fetched_at: '2026-04-01T11:24:30.086089'
original_url: https://ministack.org/
author: Nahuel
date: '2026-03-31'
description: Free, open-source LocalStack alternative. 33 AWS services on a single port. Real Postgres, Redis, Docker containers. MIT licensed, no account required.
tags:
- hackernews
- hnrss
---

# ThefreeLocalStackreplacement

LocalStack is no longer free.MiniStack is.33 AWS services on a single
 port — withreal Postgres, Redis, and Docker containers. No account, no license key, no
 telemetry.

 View on GitHub

🐳 Docker Hub

$
docker run -p 4566:4566
 nahuelnucera/ministack
copy

33

AWS Services

~2s

Startup

~30MB

RAM at idle

150MB

Docker Image

763

Tests passing

⚠️

LocalStack moved core services behind a paid plan.
 If you relied on
 LocalStack Community for local dev and CI/CD, MiniStack is your free, MIT-licensed drop-in replacement. No
 sign-up, no API key, no telemetry.

ministack — bash

# Start MiniStack

$
 docker run
-p

4566:4566

 nahuelnucera/ministack


# Works with any AWS tool — no config changes

$
 aws
--endpoint-url=
http://localhost:4566
 s3 mb s3://my-bucket

make_bucket: my-bucket

# Real database — RDS spins up actual Postgres

$
 aws
--endpoint-url=
http://localhost:4566
 rds create-db-instance \

--db-instance-identifier
 mydb
--engine
 postgres \

--master-username
 admin
--master-user-password
 secret

✓ Real Postgres container running on localhost:15432

# Real Redis via ElastiCache

$
 aws
--endpoint-url=
http://localhost:4566
 elasticache \
 create-cache-cluster
--cache-cluster-id
 my-redis
--engine
 redis

✓ Real Redis container running on localhost:16379

33 Services

## Everything you need, locally

Core AWS services plus real infrastructure — RDS runs actual databases, ElastiCache runs real
 Redis, ECS starts real Docker containers, Athena executes real SQL via DuckDB (when installed).

🪣

S3

Buckets, objects, versioning, encryption, lifecycle, CORS, Object Lock, replication
REST/XML

📨

SQS

Queues, FIFO, DLQ, batch, visibility
JSON+Query

📢

SNS

Topics, subscriptions, fanout to SQS, batch publish
Query/XML

🗃️

DynamoDB

Tables, CRUD, query, scan, transactions, TTL, GSI
JSON

⚡

Lambda

Real Python execution, warm workers, SQS event source mapping, Layers
REST/JSON

🔐

IAM

Users, roles, policies, groups, instance profiles, OIDC
Query/XML

🎫

STS

CallerIdentity, AssumeRole, GetSessionToken
Query/XML

🔑

Secrets Manager

CRUD, versioning, rotation, resource policies
JSON

📊

CW Logs

Groups, streams, retention, subscription filters, metric filters, Insights
JSON

📐

SSM Params

String, SecureString, paths, labels, tags
JSON

🚌

EventBridge

Buses, rules, targets, Lambda dispatch, archives, permissions
JSON

🌊

Kinesis

Streams, split/merge shards, consumers, encryption, monitoring
JSON

📈

CW Metrics

Metrics, alarms, composite alarms, dashboards, alarm history
Query/CBOR

✉️

SES

Send email/raw/templated, identities, configuration sets
Query/XML

🔄

Step Functions

Full ASL engine, sync execution, task tokens, all state types
JSON

🌐

API Gateway v2

HTTP APIs, Lambda proxy, path params, execute-api data plane
REST/JSON

🔌

API Gateway v1

REST APIs, resources, methods, integrations, stages, MOCK, Lambda proxy format 1.0
REST/JSON

🐘

RDS

Real Postgres/MySQL containers
Real Docker

🔴

ElastiCache

Real Redis/Memcached containers, users, user groups
Real
 Docker

🐳

ECS

RunTask starts real containers, capacity providers
Real Docker

🧪

Glue

Catalog, crawlers, jobs, triggers, workflows
Real Exec

🔍

Athena

Real SQL via DuckDB (optional), data catalogs, prepared statements
DuckDB

🚒

Firehose

Delivery streams, PutRecord/PutRecordBatch, S3 delivery, encryption, tags
REST/JSON

🌐

Route53

Hosted zones, record sets (CREATE/UPSERT/DELETE), health checks, tags, alias records
REST/XML

🔒

Cognito

User pools, auth flows, TOTP MFA, identity pools, federated credentials
JSON

🖥️

EC2

Instances, VPCs, subnets, security groups, route tables, ENIs, elastic IPs, NAT gateways, NACLs,
 flow logs, VPC peering, DHCP options, egress-only IGWs
Query/XML

⚡

EMR

Clusters, steps, instance groups/fleets, bootstrap actions, tags — Pro-only on LocalStack

JSON

💾

EBS

Volumes, snapshots, attach/detach, modify, copy — Pro-only on LocalStack
Query/XML

📁

EFS

File systems, mount targets, access points, lifecycle, backup policy — Pro-only on LocalStack

REST/JSON

⚖️

ALB / ELBv2

Load balancers, target groups, listeners, rules, Lambda targets + live data-plane routing —
 Pro-only on LocalStack
Query/XML

🔐

ACM

Request, import, describe certificates; DNS validation records; SANs; tags
JSON

✉️

SES v2

SendEmail, identities, configuration sets, account suppression — REST API
REST/JSON

🛡️

WAF v2

WebACLs, IP sets, rule groups, resource associations, LockToken enforcement — Pro-only on
 LocalStack
JSON

Comparison

## LocalStack vs MiniStack

Same developer experience. Fraction of the cost and footprint.

Feature

LocalStack Free

LocalStack Pro

MiniStack ⚡

Core services (S3, SQS, DDB…)

Now paid

✅

✅ Free

Lambda, IAM, SSM, EventBridge

Paid

✅

✅ Free

RDS (real DB containers)

❌

✅

✅ Real Postgres/MySQL

ElastiCache (real Redis)

❌

✅

✅ Real Redis

ECS (real Docker)

❌

✅

✅ Real Docker

Athena (real SQL)

❌

✅

✅ DuckDB (optional)

Glue Catalog + Jobs

❌

✅

✅

API Gateway v2 (HTTP APIs)

✅

✅

✅ + data plane

API Gateway v1 (REST APIs)

✅

✅

✅ + data plane

Firehose

✅

✅

✅ S3 delivery

Route53

✅

✅

✅

Cognito (user pools + identity)

Paid

✅

✅ Free

EC2 (instances, VPC, subnets, SGs)

Paid

✅

✅ Free

EMR (clusters, steps, instance groups)

Paid

✅

✅ Free

EBS (volumes, snapshots, attach/detach)

Paid

✅

✅ Free

EFS (file systems, mount targets, access points)

Paid

✅

✅ Free

ALB / ELBv2 (LBs, listeners, rules + Lambda data plane)

Paid

✅

✅ Free

SNS→SQS fanout + SQS→Lambda ESM

❌

✅

✅

Startup time

~15-30s

~15-30s

~2s

Memory at idle

~500MB

~500MB

~30MB

Docker image

~1 GB

~1 GB

150 MB

License

BSL (restricted)

Proprietary

MIT

Price

Now paid

$35+/mo

$0 forever

Built different

## Real infrastructure, not mocks

Where it matters most — RDS, ElastiCache, and ECS run real Docker containers. No fake endpoints, no
 stubbed responses.

🐘

Real databases via RDS

CreateDBInstance spins up an actual Postgres or MySQL Docker container. Connect with psycopg2 —
 it's a real database.

🔴

Real Redis via ElastiCache

CreateCacheCluster starts an actual Redis container. Use redis-py, run SUBSCRIBE, use it as your
 session store.

🐳

Real containers via ECS

RunTask pulls and starts real Docker containers via the Docker socket. Test your ECS task
 definitions locally.

🔍

Real SQL via Athena

Queries execute via DuckDB when installed. Query S3 data with actual SQL, get actual result sets
 back. Falls back to mock results without it.

🔌

Full SDK compatibility

Works with boto3, AWS CLI, Terraform, CDK, Pulumi — any tool that speaks the AWS API.

🔓

MIT licensed forever

No BSL, no feature gates, no "community" vs "pro". Every service is free. Fork it, embed it. MIT
 is MIT.

## Stop paying for local development

One command. 33 services. Real infrastructure. Free.

 GitHub

🐳 Docker Hub

$
docker run -p 4566:4566
 nahuelnucera/ministack
copy
