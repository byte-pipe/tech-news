---
title: Hands-on with Gemma 3 on Google Cloud - DEV Community
url: https://dev.to/googleai/hands-on-with-gemma-3-on-google-cloud-6e7
site_name: devto
fetched_at: '2025-12-11T11:07:26.770698'
original_url: https://dev.to/googleai/hands-on-with-gemma-3-on-google-cloud-6e7
author: Olivier Bourgeois
date: '2025-12-05'
description: The landscape of generative AI is shifting. While proprietary APIs are powerful, there is a growing... Tagged with gemma, ai, cloud, opensource.
tags: '#gemma, #ai, #cloud, #opensource'
---

The landscape of generative AI is shifting. While proprietary APIs are powerful, there is a growing demand foropen models—models where the architecture and weights are publicly available. This shift puts control back in the hands of developers, offering transparency, data privacy, and the ability to fine-tune for specific use cases.

To help you navigate this landscape, we are releasingtwo new hands-on labsfeaturingGemma 3, Google’s latest family of lightweight, state-of-the-art open models.

## Why Gemma?

Built from the same research and technology as Gemini, Gemma models are designed for responsible AI development. Gemma 3 is particularly exciting because it offers multimodal capabilities (text and image) and fits efficiently on smaller hardware footprints while delivering massive performance.

But running a model on your laptop is very different from running it in production. You need scale, reliability, and hardware acceleration (GPUs). The question is:Where should you deploy?

We have prepared two different paths for you, depending on your infrastructure needs:Cloud RunorGoogle Kubernetes Engine (GKE).

## Path 1: The Serverless Approach (Cloud Run)

Best for:Developers who want an API up and running instantly without managing infrastructure, scaling to zero when not in use.

If your priority is simplicity and cost-efficiency for stateless workloads, Cloud Run is your answer. It abstracts away the server management entirely. With the recent addition of GPU support on Cloud Run, you can now serve modern LLMs without provisioning a cluster.

### Start the lab!

Lab:Serving Gemma 3 with vLLM on Cloud Run

Objectives:

* ContainerizevLLM(a high-throughput serving engine).
* Deploy Gemma 3 toCloud Run.
* Leverage GPU acceleration for fast inference.
* Expose an OpenAI-compatible API endpoint.

## Path 2: The Platform Approach (GKE)

Best for:Engineering teams building complex AI platforms, requiring high throughput, custom orchestration, or integration with a broader microservices ecosystem.

When your application graduates from a prototype to a high-traffic production system, you need the control of Kubernetes. GKE Autopilot gives you that power while still handling the heavy lifting of node management. This path creates a seamless journey from local testing to cloud production.

### Start the lab!

Lab:Deploying Open Models on GKE

In this lab, you will learn how to:

* Prototype locally usingOllama.
* Containerize your setup and transition toGKE Autopilot.
* Deploy a scalable inference service using standard Kubernetes manifests.
* Manage resources effectively for production workloads.

## Which Path Will You Choose?

Whether you are looking for the serverless simplicity of Cloud Run or the robust orchestration of GKE, Google Cloud provides the tools to take Gemma 3 from a concept to a deployed application.

Dive into the labs today and start building:

* Serving Gemma 3 with vLLM on Cloud Run
* Deploying Open Models on GKE

Share your progress and connect with others on the journey using the hashtag#ProductionReadyAI. Happy learning!

These labs are part of theOpen Modelsmodule in our officialProduction-Ready AI with Google Cloudprogram. Explore the full curriculum for more content that will help you bridge the gap from a promising prototype to a production-grade AI application.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
