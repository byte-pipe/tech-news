---
title: GitHub - floci-io/floci: Light, fluffy, and always free - The AWS Local Emulator alternative · GitHub
url: https://github.com/floci-io/floci
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:24:15.765457
---

# GitHub - floci-io/floci: Light, fluffy, and always free - The AWS Local Emulator alternative · GitHub

# Floci – Light, fluffy, and always free

## What is Floci?
- Open‑source local AWS emulator for development, testing, and CI.
- Provides AWS‑shaped services on localhost without a cloud account, auth token, or paid feature gates.
- Compatible with AWS SDK, CLI, Terraform, CDK, OpenTofu, and test suites via `http://localhost:4566`.
- Drop‑in replacement for LocalStack; swap the Docker image and keep existing workflows.
- Part of the Floci emulator family (AWS, Azure, GCP, OCI) each listening on a distinct port.

## Quick Start
### CLI method
1. Install the official CLI and run `floci start`.
2. Export environment variables with `eval $(floci env)`.
3. Use standard AWS commands, e.g. `aws s3 mb s3://my-bucket` or DynamoDB table creation.
4. Stop the emulator when finished.

### Docker Compose method
```yaml
services:
  floci:
    image: floci/floci:latest
    ports:
      - "4566:4566"
```
- Start with `docker compose up`.
- Manually set AWS env vars:
  - `AWS_ENDPOINT_URL=http://localhost:4566`
  - `AWS_DEFAULT_REGION=us-east-1`
  - `AWS_ACCESS_KEY_ID=test`
  - `AWS_SECRET_ACCESS_KEY=test`

### Updating from the old image
- Replace `hectorvent/floci:latest` with `floci/floci:latest`; the old repository is no longer updated.

## Web Console
- Accessible at `http://localhost:4566/_floci/ui`.
- Launched on first request as a sidecar container; no extra host ports needed.
- Requires Docker socket mount:
  ```yaml
  volumes:
    - /var/run/docker.sock:/var/run/docker.sock
  ```
- Configurable via environment variables (e.g., `FLOCI_SERVICES_UI_ENABLED`, `FLOCI_SERVICES_UI_IMAGE`, `FLOCI_SERVICES_UI_PORT`).
- Custom consoles can be used by providing an image that follows the Floci console contract (health endpoint, AWS endpoint env var).

## Key Features
- **No AWS account needed** – runs entirely locally.
- **Real Docker execution** for services where fidelity matters (Lambda, RDS, Neptune, ElastiCache, MSK, ECS, EC2, EKS, OpenSearch, CodeBuild, Flink, etc.).
- **Full AWS compatibility** – point clients to `localhost:4566`; existing credentials, regions, SDKs, CLI commands, and IaC workflows work unchanged.
- **Terraform support** via the standard HashiCorp AWS provider.
- **Fast startup** – native binary starts in milliseconds, low idle memory.
- **Configurable persistence** – in‑memory, persistent, hybrid, or write‑ahead log storage.

## Why Choose Floci over LocalStack?
| Feature | Floci | LocalStack Community (as of Mar 2026) |
|---------|-------|---------------------------------------|
| Auth token required | No | Yes |
| Security updates | Yes | Frozen |
| Startup time | ~24 ms | ~3.3 s |
| Idle memory | ~13 MiB | ~143 MiB |
| Docker image size | ~90 MB | ~1 GB |
| License | MIT | Restricted |
| Real Docker for RDS, ElastiCache, MSK, Neptune, DocumentDB, ECS, EC2, EKS, CodeBuild | Yes | No |
| API Gateway v2 / HTTP API | Yes | No |
| Cognito | Yes | No |

- Provides broad AWS coverage for free forever.

## Architecture Overview
- Client (AWS SDK/CLI) → **Floci** (port 4566) → HTTP router (JAX‑RS / Vert.x) → Stateless services (SSM, SQS, …) and stateful Docker‑backed services.
- Sidecar console runs alongside Floci, receives the reachable address via `AWS_ENDPOINT_URL`, and reports health via `/api/health`.  

---  

*Floci delivers a lightweight, fully compatible AWS emulator that runs locally without any cloud dependencies, making it ideal for rapid development, testing, and CI pipelines.*