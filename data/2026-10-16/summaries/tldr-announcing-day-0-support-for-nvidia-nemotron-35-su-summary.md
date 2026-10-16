---
title: Announcing Day 0 Support for NVIDIA Nemotron 3.5 Super VL on vLLM | vLLM Blog
url: https://vllm.ai/blog/2026-10-15-nemotron-3-5-super-vl-vllm
date: 2026-10-16
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-16T15:17:23.012300
---

# Announcing Day 0 Support for NVIDIA Nemotron 3.5 Super VL on vLLM | vLLM Blog

**NVIDIA Nemotron 3.5 Super VL Open-Source Multimodal Model**

**Overview**

NVIDIA Nemotron 3.5 Super VL is an open-source, customizable multimodal model designed for long-running agents. It combines reasoning, instruction following, and tool use with text, image, document, and video understanding, reducing the need for separate models and maintaining task-relevant context across workflow steps.

**Key Features**

- **Architecture**: A 120B model with 12B active parameters, using a mixture-of-experts design
- **Modalities**: Text, images, documents, and videos as input; text as output
- **Optimization**: A combination of vision encoder (C-Radio v4), hybrid Mamba-Transformer architecture, multi-token prediction, and NVFP4 quantization
- **Model Role**: High-accuracy agentic execution with native visual understanding for systems of models
- **Customization**: Post-training on NVIDIA NeMo using organization-specific data, tools, policies, and workflows
- **Deployment**: Optimized production serving across cloud and data center environments (1x GB10, B200, B300, RTX PRO 6000, H200, 2x H100)
- **Availability**: Model weights available for download on Hugging Face (BF16 and NVFP4)

**Incorporating Nemotron 3.5 Super VL**

To use Nemotron 3.5 Super VL with vLLM, follow these steps:

1. **Prepare Your TensorFlow Model**
   - Download and extract the vLLM serving layer from GitHub
   - Prepare your TensorFlow model according to the Getting Started with TensorFlow Cookbook

2. **Post-Training with NVIDIA NeMo**
   - Set up your environment with NVIDIA NeMo and vLLM
   - Post-train Nemotron 3.5 Super VL on top of your organization-specific data

3. **Integrate Nemotron 3.5 Super VL with vLLM**

   - Install Nemotron 3.5 Super VL and vLLM on your system
   - Use the vLLM serving layer to integrate Nemotron 3.5 Super VL with your existing application

**Run High-Throughput Inference**

- **Optimization**: Choose the right model weights (BF16 and NVFP4)
- **Model Deployment**: Use the optimized model for production serving across cloud and data center environments.