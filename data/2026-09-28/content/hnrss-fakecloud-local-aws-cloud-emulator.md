---
title: fakecloud - Local AWS Cloud Emulator
url: https://fakecloud.dev/
site_name: hnrss
content_file: hnrss-fakecloud-local-aws-cloud-emulator
fetched_at: '2026-09-28T13:22:40.667574'
original_url: https://fakecloud.dev/
date: '2026-09-26'
description: fakecloud is a free, open-source local AWS cloud emulator. Single binary, no auth required, no paid tier, plus first-party SDKs for test assertions.
tags:
- hackernews
- hnrss
---

# fakecloud

Local AWS cloud emulator for integration tests. Run your app with normal AWS clients, stay fully local, and use fakecloud SDKs when your tests need deeper visibility.105 services. 7,508 operations. 248,557/248,557 Smithy variants pass — true 100% conformance.Get StartedWhy fakecloud

## Why fakecloud?

fakecloud gives you a local AWS environment that behaves like infrastructure, not a mock. Your app uses the regular AWS SDK, CLI, and IaC tools. Unlike today's LocalStack Community setup, you do not need an account, auth token, or paid plan just to keep core development flows local.The SDKs make that workflow nicer, not narrower.Start fakecloud, run the code you actually ship, inspect emails/messages/invocations after the fact, and force async AWS-style behavior to happen on demand.

## Built for realistic local testing

Real APIs for your app, purpose-built tooling for your tests.Workflow### Test what your app really doesUse normal AWS clients against localhost, then verify the effects with fakecloud instead of stitching together polling, fixtures, or private test hooks.SDKs### First-party test clientsTypeScript, Python, Go, PHP, Java, and Rust SDKs wrap the/_fakecloud/*endpoints for resets, assertions, and manual control of async processors after your app has already used the normal AWS APIs.Coverage### 105 AWS servicesS3, SQS, SNS, EventBridge, EventBridge Pipes, EventBridge Scheduler, Lambda, EC2, DynamoDB, IAM, STS, Organizations, SSM, Secrets Manager, CloudWatch Logs, CloudWatch (Metrics & Alarms), KMS, CloudFormation, Cloud Control API, SES, Cognito User Pools, Cognito Identity, Kinesis, Firehose, RDS, RDS Data API, Aurora DSQL, Resource Groups, Resource Groups Tagging API, ElastiCache, MemoryDB, EKS, Cloud Map, Step Functions, API Gateway v1 (REST), API Gateway v2 (HTTP), Bedrock, Bedrock Agent, Bedrock Agent Runtime, Bedrock Runtime, ECR, ECS, Elastic Load Balancing v2, CloudFront, Route 53, WAF v2, Application Auto Scaling, Athena, ACM, and Glue.Tested### Conformance testedTrue 100% conformance across all 3,932 implemented API operations: 248,557/248,557 Smithy-model-generated test variants pass on every commit, backed by end-to-end tests against the official AWS SDKs.Real behavior### Cross-service flows are wired up30+ service-to-service integrations: S3 notifications, SNS fanout, EventBridge targets, DynamoDB Streams, CloudWatch Logs subscriptions, Cognito triggers, Step Functions task integrations, API Gateway → Lambda, and more — all exercise real service interactions.Simple### No auth, no lock-in, no paid tierRun a single binary or Docker image, use any dummy credentials, and keep the whole workflow local without signing in to someone else's platform.

## SDKs for test assertions

Keep using the AWS SDK in your app. Use fakecloud SDKs when your tests need visibility and control on top of the emulator itself.TypeScript### npm install fakecloudInspect SES emails, SNS messages, SQS queues, Lambda invocations, Cognito confirmation codes, and more.View on npmPython### pip install fakecloudAsync and sync clients for pytest or app-level integration tests, with the same introspection and simulation coverage.View on PyPIGo### go get github.com/faiscadev/fakecloud/sdks/goContext-friendly helpers for resets, event history, SES inbound simulation, and the rest of the fakecloud test surface.View on pkg.go.devRust### cargo add fakecloud-sdkNative Rust client for tests that need resets, state inspection, and direct access to the fakecloud introspection surface.View on crates.io

## Quick Start

Start fakecloud, point your AWS client at localhost, then assert what happened.# Install (no Cargo or Docker needed)$curl -fsSL https://fakecloud.dev/install.sh | bash# or: brew install fakecloud$fakecloud# Your app uses the normal AWS SDK against localhost$aws --endpoint-url http://localhost:4566 sqs create-queue \--queue-name my-queue# Your tests can inspect state through the fakecloud SDK$npm install fakecloud

## How it compares

If you want a fully local workflow with real AWS APIs and no account requirement, fakecloud is built for that path. The SDKs are an extra testing advantage, not a replacement for that positioning.fakecloudLocalStack CommunityLicenseAGPL-3.0ProprietaryAuth requiredNoYes (account + token)Commercial useFreePaid plans onlyDocker requiredNo (standalone binary)YesStartup time~300ms~3sIdle memory~10 MiB~150 MiBInstall size~19 MB binary~1 GB Docker imageAWS services46 at true 100% conformance30+ (paid-only past Community)Test assertion SDKsTypeScript, Python, Go, PHP, Java, RustPython, JavaCognito User Pools122 operationsPaid onlySES v2110 operationsPaid onlySES inbound emailReal receipt rule actionsStored but never executedRDS163 operations, PostgreSQL/MySQL/MariaDB via Docker, PostgreSQLaws_lambdaextensionPaid onlyElastiCache75 operations, Redis and Valkey via DockerPaid onlyMemoryDB45 operations, full control planePaid onlyEKSCluster control plane (batch 1)Paid onlyAPI Gateway v2103 operations, HTTP APIs + developer portals + JWT/Lambda authorizersPaid onlyBedrock214 operations across 4 APIs (Bedrock + Bedrock Runtime + Bedrock Agent + Bedrock Agent Runtime)Not available

## Supported services

Every implemented API is covered by conformance and behavioral testing, with the service mix tuned for local development and integration tests.S3REST protocol · XMLSQSQuery protocol · XMLSNSQuery protocol · XMLEventBridgeJSON protocolEventBridge SchedulerJSON protocolSSMJSON protocolDynamoDBJSON protocolIAMQuery protocolSTSQuery protocolLambdaREST protocol · JSONSecrets ManagerJSON protocolCloudWatch LogsJSON protocolKMSJSON protocolCloudFormationQuery protocolSESREST + Query protocolCognito User PoolsJSON protocolKinesisJSON protocolRDSQuery protocolElastiCacheQuery protocolMemoryDBJSON 1.1 protocolEKSREST-JSON protocolStep FunctionsJSON protocolAPI Gateway v1 (REST)REST protocol · JSONAPI Gateway v2REST protocol · JSONBedrockREST protocol · JSONBedrock RuntimeREST protocol · JSONBedrock AgentREST protocol · JSONBedrock Agent RuntimeREST protocol · JSONECRREST protocol · JSONECSJSON protocolElastic Load Balancing v2Query protocolCloudFrontREST protocol · XMLRoute 53REST protocol · XMLACMJSON protocolACM PCAJSON protocolApplication Auto ScalingJSON protocolWAF v2JSON protocolAthenaJSON protocolGlueJSON protocolCognito IdentityJSON protocolCloudWatch (Metrics & Alarms)Query protocolFirehoseJSON protocolEC2Query protocol · XMLOrganizationsJSON protocolCloud Control APIJSON protocolEventBridge PipesREST protocol · JSONRDS Data APIREST protocol · JSONAurora DSQLREST protocol · JSONResource GroupsREST protocol · JSONResource Groups Tagging APIJSON protocol

## Who's using fakecloud

Early days, and the list is just getting started. Using fakecloud in CI, local dev, or tests? Add your team on GitHub. The numbers below are package downloads and stars, not a user count.See adopters·Add your team