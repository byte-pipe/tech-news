---
title: Introducing OpenWorkers – Self-hosted Cloudflare Workers in Rust
url: https://openworkers.com/introducing-openworkers
date: 2026-01-01
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-02T11:14:13.552366
screenshot: hackernews_api-introducing-openworkers-self-hosted-cloudflare-wor.png
---

# Introducing OpenWorkers – Self-hosted Cloudflare Workers in Rust

## Introducing OpenWorkers

### Overview
OpenWorkers is a self-hosted Cloudflare Workers runtime in Rust, allowing users to execute JavaScript code in V8 isolates. This enables a powerful programming model similar to Cloudflare's Workers functionality.

### Key Features and Components

* **Bindings and Storage**: Supports various storage options like KV, PostgreSQL, S3 compatible storage, and service bindings.
* **Web APIs**: Provides a set of Web API functions for standard programming.
* **Architecture**: Demonstrates a full-stack architecture with several components, including:
	+ `nginx` proxy
	+ `dashboard`
	+ `api`
	+ `logs`
	+ `runner` (three instances)
	+ `postgate`
	+ `nats`
	+ PostgreSQL database

### Self-Hosting Guide

* **Setup**: Clone the GitHub repository, extract the code into a directory, create an `.env.example` file, and modify it to match your desired environment.
* **Deployment**: Use a single PostgreSQL database for deployment and run Docker Compose, which will manage and orchestrate the environment.

### Features and Benefits

* Simplified deployment
* Support for multiple storage options
* Easy integration with Web API functions and services
* Suitable for use cases that demand low-latency performance

### Why I Built This

The creation of OpenWorkers was motivated by my interest in self-hosted Cloudflare Workers. After several iterations on different technologies, such as JVM-based sandboxing (vm2) and Deno-core implementation (deno-core), the goal was achieved: running JavaScript with native thread isolation using Rust.
