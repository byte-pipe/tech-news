---
title: The Ultimate Cloud Run Guide 2026 - DEV Community
url: https://dev.to/googleai/the-ultimate-cloud-run-guide-2026-54f8
date: 2026-06-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-02T06:01:25.508532
---

# The Ultimate Cloud Run Guide 2026 - DEV Community

# The Ultimate Cloud Run Guide 2026 – Recap

## 1. Getting started – deploy a container
- Cloud Run is Google Cloud’s serverless engine that runs any container on demand without managing VMs or clusters.  
- Demo 1 (Nginx) at 1:04.  
- Example commands: deploy the hello‑sample container and deploy an Nginx container.  
- If you don’t have a container image, you can deploy directly from source (see section 3).

## 2. Autoscaling / audience participation demo
- **Minimum instances** keep containers pre‑warmed, eliminating cold‑start latency.  
- **Maximum instances** set a hard scaling limit to control cost and protect downstream services.  
- Demo 2 at 6:10 (QR code gives each audience member their own container).  
- Discussion at 28:13; reference the Instance Autoscaling documentation.

## 3. How `gcloud` works under the hood
- `gcloud run deploy` from source triggers a five‑step pipeline:  
  1. **Upload** – local directory is stored in a secure GCS bucket.  
  2. **Build** – Cloud Build runs a Docker build (or uses Buildpacks when no Dockerfile is present).  
  3. **Store** – the resulting image is pushed to Artifact Registry.  
  4. **Create** – Cloud Run creates a new immutable revision.  
  5. **Migrate** – after passing the startup probe, 100 % of traffic is shifted to the new revision.  
- Demo 3 at 9:54; includes quickstart for a Go web app and other buildpack‑supported languages.

## 4. Overview of Cloud Run resources
- **Services** – ideal for web apps, APIs, and microservices; auto‑scales, provides HTTPS, traffic splitting, WebSockets, gRPC, HTTP/2.  
- **Jobs** – run‑to‑completion tasks (up to 7 days); suited for data processing, migrations, nightly scripts; can parallelize multiple tasks.  
- **Worker Pools** – always‑on instances that pull work (e.g., from a message queue); scaling is manual.  
- **Functions** – single‑purpose code (e.g., file‑upload triggers); supports Python, Node.js, Go, Java; no Dockerfile needed, Google builds the container automatically.  
- Code examples for each resource type are provided in the talk.

## 5. Reliable rollouts and preview links
- Cloud Run uses immutable revisions for zero‑downtime updates: the new revision scales up before traffic migration.  
- Rollbacks are instant by redirecting traffic to any healthy previous revision.  
- Preview links (traffic tags) let you test a new revision on a private URL (e.g., `https://latest---[service].run.app`) without exposing it publicly.  
- Demos at 10:10, 12:48, and 16:25; gradual rollout codelab included.

## 6. Structured logging
- No special logging libraries are required; write plain text to stdout or stderr.  
- For richer queries, output logs in JSON format so Cloud Logging can filter on custom fields (e.g., `jsonPayload.user_id`).  

## 7. Troubleshooting “container failed to start on port 8080”
- The error indicates Cloud Run could not start the container. Common causes:  
  - Application not listening on the port defined by the `PORT` environment variable.  
  - Startup crashes; check logs for stack traces.  
  - Long‑running initialization (e.g., loading large ML models) causing timeouts; defer heavy work until after the container is healthy.  
- Example: deploy the hello container but set the listening port to 8081 to reproduce the issue.

## 8. Google Cloud Developer Knowledge MCP server (public preview)
- Introduced as a public‑preview service for developer knowledge.  
- A codelab is available to explore the MCP server functionality.  

*The full talk is available via the provided link for viewers who prefer the video format.*