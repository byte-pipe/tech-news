---
title: Hands-on with Gemma 3 on Google Cloud - DEV Community
url: https://dev.to/googleai/hands-on-with-gemma-3-on-google-cloud-6e7
date: 2025-12-05
site: devto
model: llama3.2:1b
summarized_at: 2025-12-11T11:16:37.127492
screenshot: devto-hands-on-with-gemma-3-on-google-cloud-dev-communit.png
---

# Hands-on with Gemma 3 on Google Cloud - DEV Community

# Hands-on Summary: Gemma 3

## Introduction to Gemma 3

Gemma 3 is a family of lightweight, state-of-the-art open models that offer design flexibility and performance. This text provides an overview of the landscape of generative AI, including the shift towards open models, the growing demand for publicly available architectures, and the introduction of Google Cloud's new hands-on labs featuring Gemma 3.

## Key Features and Benefits

- **Open Models**: The architecture and weights are publicly available, providing transparency, data privacy, and the ability to fine-tune for specific use cases.
- **Control and Transparancy**: Developers have control over the model, offering a transparent development experience.
- **Data Privacy**: Publicly available models ensure robust data protection.

## Deployment Options

Gemma 3 is available in two deployment options:

### Cloud Run (Serverless)

This approach simplifies API upgradability without managing infrastructure or scaling workload manually. Gemma 3 can run on AWS or GCP and leverages GPU acceleration for rapid inference.

#### Serving Gemma 3 with vLLM on Cloud Run

* Containerize highly-throughput serving engine `vLLM` (`openfaaS`)
* Deploy to `Cloud Run`
* Utilize GPU acceleration for fast inference
* Leverage an OpenAI-compatible API endpoint

### Google Kubernetes Engine (GKE)

This path provides robust orchestration and control, ideal for complex AI platforms requiring high throughput and custom node management.

#### Deploying Open Models on GKE

* Prototype locally with `olLaMo`
* Containerize the setup
* Transition to `GKE Autopilot` for seamless deployment and resource management
* Deploy a scalable inference service using standard Kubernetes manifests
