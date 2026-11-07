---
title: GitHub - prometheus/prometheus: The Prometheus monitoring system and time series database. · GitHub
url: https://github.com/prometheus/prometheus
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:00.866747
---

# GitHub - prometheus/prometheus: The Prometheus monitoring system and time series database. · GitHub

# Prometheus Repository Overview

## Project Description
- Prometheus is a Cloud Native Computing Foundation project for systems and service monitoring.  
- It collects metrics from configured targets, evaluates rule expressions, displays results, and can trigger alerts.

## Key Features
- Multi‑dimensional data model (metric name + key/value dimensions)  
- PromQL, a powerful query language leveraging dimensionality  
- Autonomous single‑server nodes; no dependency on distributed storage  
- HTTP pull model for time‑series collection, with optional push gateway for batch jobs  
- Service discovery (static or dynamic)  
- Various graphing and dashboarding options  
- Hierarchical and horizontal federation support  

## Installation Options
- **Precompiled binaries**: Download the latest release from the download section on prometheus.io and follow the Installing guide.  
- **Docker images**: Available on Quay.io and Docker Hub. Example to run:
  ```bash
  docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
  ```
  Access at `http://localhost:9090/`.  
- **Building from source**:  
  - Prerequisites: Go (version in `go.mod` or newer), NodeJS (version in `.nvmrc` or newer), npm ≥ 10.  
  - Clone the repo, then either:
    - Use `go install github.com/prometheus/prometheus/cmd/...` (run from repo root to access web assets)  
    - Or run `make build` to embed web assets, allowing execution from any location.  
  - Common Makefile targets: `build`, `test`, `test-short`, `format`, `vet`, `assets`.  

## Service Discovery Customization
- Build tags control which discovery plugins are included.  
- Example to exclude all optional SDs and re‑enable only Kubernetes:
  ```yaml
  build:
    tags:
      all:
        - netgo
        - builtinassets
        - remove_all_sd
        - enable_kubernetes_sd
  ```
- Available tags: `remove_all_sd`, `enable_<name>_sd`.  
- Out‑of‑tree plugins may require adjustments to `go.mod` and `go.sum`.  

## Docker Image Build
- Local image build steps:
  ```bash
  make promu
  promu crossbuild -p linux/$(go env GOHOSTARCH)
  make common-docker-current-arch
  ```
- Replace `$(go env GOHOSTARCH)` with a specific architecture (e.g., `amd64`) to build for other platforms.  
- The `make docker` target is intended for CI use only.  

## Using Prometheus as a Go Library
- The main repository builds a standalone binary and is not optimized as a library, but parts can be used.  
- **Remote Write** protobuf is published separately and can be imported:
  ```bash
  go get buf.build/gen/go/prometheus/prometheus/protocolbuffers/go@latest
  ```
- **Versioning for library use**:  
  - v3.y.z releases are tagged as `v0.3y.z` (y padded to two digits).  
  - v2.y.z releases are tagged as `v0.y.z`.  
  - Example: `go get github.com/prometheus/prometheus@v0.300.0` for Prometheus v3.0.0.  

## React UI Development
- Build, run, and develop the React‑based UI following the instructions in the UI’s `README.md`.  

## Additional Resources
- Full documentation, examples, and guides at `prometheus.io`.  
- GoDoc documentation via `pkg.go.dev`.  
- Repository files include `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, licensing, and CI configuration.