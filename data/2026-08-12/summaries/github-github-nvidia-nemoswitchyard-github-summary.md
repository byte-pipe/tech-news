---
title: GitHub - NVIDIA-NeMo/Switchyard · GitHub
url: https://github.com/NVIDIA-NeMo/Switchyard
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-08-12T11:47:15.559428
---

# GitHub - NVIDIA-NeMo/Switchyard · GitHub

### Switchyard: A Rust Proxy and Library for LLM Traffic

**Overview**

Switchyard is a Rust library that provides a flexible proxy and routing system for Large Language Models (LLMs). It seamlessly routes requests across multiple providers, translates between OpenAI models and Anthropic APIs, records operational metrics, and offers composable routing algorithms.

### Features

* **Protocol Translation**: Compatible with OpenAI Chat, Anthropic Messages, and OpenAI Responses formats
* **Multi-Backend Routing**: Random routing, LLM-as-classifier routing, signal-driven stage-router, or custom algorithm implementation
* **Operational Metrics**: Tracks requests, errors, latency, tokens, and routing overhead

### Maturity

Switchyard is a pre-alpha software in development. Expect significant changes before reaching version 1.0.

**Why Use Switchyard?**

Point a coding agent (e.g., Claude) to interact with OpenAI Chat or Anthropic Messages models, using Switchyard as the proxy for seamless communication and efficient routing of traffic across multiple models. This allows for robust testing and optimization without exposing your underlying infrastructure.

Switchyard is suitable for A/B benchmarking, signal-driven stage-routing, or creating custom algorithms that require precise control over LLM behavior.

### Prerequisites and Download

* **Cargo.toml**: Install the Switchyard crates manually by running `cargo install switchyard`.

Some additional resources:

* **docs**: Visit the [Switchyard documentation](https://switchyard-rs.org/docs/) for more information on usage, features, and troubleshooting.
* **mkdocs.yml**: Check out the mkdocs.yml file for configuration settings and customization options.