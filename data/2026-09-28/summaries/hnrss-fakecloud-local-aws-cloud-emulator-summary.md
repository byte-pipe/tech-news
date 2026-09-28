---
title: fakecloud - Local AWS Cloud Emulator
url: https://fakecloud.dev/
date: 2026-09-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:22:51.290898
---

# fakecloud - Local AWS Cloud Emulator

# fakecloud – Local AWS Cloud Emulator

## Why fakecloud?
- Provides a fully local AWS environment that behaves like real infrastructure, not a simple mock.  
- Works with standard AWS SDKs, CLI, and IaC tools without needing an AWS account, auth token, or paid plan.  
- Enables inspection of emails, messages, and invocations after execution and allows on‑demand triggering of async AWS‑style behavior.

## Built for realistic local testing
- **Workflow:** Run your application against localhost using normal AWS clients, then verify effects with fakecloud instead of custom polling or fixtures.  
- **First‑party test clients:** SDKs for TypeScript, Python, Go, PHP, Java, and Rust wrap the `_fakecloud/*` endpoints for resets, assertions, and manual control of async processors after normal AWS API calls.  
- **Coverage:** Emulates 105 AWS services (e.g., S3, SQS, SNS, Lambda, DynamoDB, IAM, CloudFormation, Bedrock, EKS, etc.) with 7,508 operations.  
- **Conformance:** 100 % true conformance—248,557 Smithy‑model test variants pass on every commit.  
- **Real behavior:** Over 30 service‑to‑service integrations (S3 notifications, SNS fan‑out, EventBridge targets, DynamoDB Streams, etc.) are wired together to exercise authentic interactions.  
- **Simplicity:** No authentication, no vendor lock‑in, no paid tier; run a single binary or Docker image with dummy credentials.

## SDKs for test assertions
- **TypeScript:** `npm install fakecloud` – inspect SES emails, SNS messages, SQS queues, Lambda invocations, Cognito codes, etc.  
- **Python:** `pip install fakecloud` – async and sync clients for pytest or integration tests with full introspection.  
- **Go:** `go get github.com/faiscadev/fakecloud/sdks/go` – context‑friendly helpers for resets, event history, SES inbound simulation, etc.  
- **Rust:** `cargo add fakecloud-sdk` – native client for resets, state inspection, and direct access to the introspection surface.

## Quick Start
1. Install the binary (no Docker required):  
   ```bash
   curl -fsSL https://fakecloud.dev/install.sh | bash
   # or: brew install fakecloud
   ```  
2. Start fakecloud: `fakecloud`  
3. Point your AWS client to localhost, e.g.:  
   ```bash
   aws --endpoint-url http://localhost:4566 sqs create-queue --queue-name my-queue
   ```  
4. Use the fakecloud SDK in tests to inspect state, e.g., `npm install fakecloud`.

## Comparison with LocalStack Community
| Feature | fakecloud | LocalStack Community |
|---|---|---|
| License | AGPL‑3.0 | Proprietary |
| Auth required | No | Yes (account + token) |
| Commercial use | Free | Paid plans only |
| Docker needed | No (standalone binary) | Yes |
| Startup time | ~300 ms | ~3 s |
| Idle memory | ~10 MiB | ~150 MiB |
| Install size | ~19 MB binary | ~1 GB Docker image |
| AWS services covered | 105 services, 100 % conformance | 46 services, 100 % conformance (paid tiers add more) |
| Test‑assertion SDKs | TypeScript, Python, Go, PHP, Java, Rust | Python, Java |
| Advanced services (e.g., Bedrock, EKS, RDS Docker) | Available | Paid only or not available |

## Supported services
- Core services: S3, SQS, SNS, EventBridge, DynamoDB, IAM, STS, Lambda, Secrets Manager, CloudWatch (Logs, Metrics, Alarms), KMS, CloudFormation, SES, Cognito (User Pools & Identity), Kinesis, RDS, ElastiCache, MemoryDB, EKS, Step Functions, API Gateway v1 & v2, Bedrock family, ECR, ECS, ELB v2, CloudFront, Route 53, ACM, Application Auto Scaling, WAF v2, Athena, Glue, etc.  
- All implemented APIs are covered by conformance and behavioral testing, with protocols (REST, JSON, XML, Query) matching the official AWS specifications.

## Who's using fakecloud
- Early adopters are using fakecloud in CI pipelines, local development, and integration tests.  
- Teams can add themselves on GitHub to be listed as adopters; download and star metrics are shown for each language package.