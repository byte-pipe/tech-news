---
title: GitHub - huggingface/transformers: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio,...
url: https://github.com/huggingface/transformers
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-08-11T11:55:09.574349
---

# GitHub - huggingface/transformers: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio,...

**Transformers Framework Overview**

The Hugging Face Transformers framework is a model-definition framework for state-of-the-art machine learning models in text, computer vision, audio, and multimodal models. **Overview**: This framework acts as the pivot across frameworks, allowing developers to share model definitions that are compatible with multiple training and inference engines.

**Key Features**

* Conserves model definition: Defines the most important ideas and essential details of a model.
* Simple, customizable, and efficient: Allows for easy sharing and adaptation of model definitions.
* Compatible with various training and inference engines: Works with models supported by e.g. Axolotl, Unsloth, DeepSpeed, FSDP, PyTorch-Lightning, ..., in addition to vLLM, SGLang, TGI.

**State-of-the-Art Models on the Hub**

Over 1 million+ pre-trained Transformers model checkpoints are available on the Hugging Face Hub. Developers can explore and use these models for their projects.

### Installation

* Works with Python 3.10+.
* Works with PyTorch 2.5+

### Virtual Environment Setup

Create a virtual environment using `venv`, a fast Rust-based Python package and project manager.

```bash
# venv setup
python:
  -m venv my_env
  . my_env \*
```

Install Transformers in your virtual environment:

```bash
pip install transformers[torch]
```

Transformers will be installed to `my_env/lib/python3.10/site-packages/transformers`.

### Quick Start

To use the framework, follow these steps:

1. Clone or download the "awesome-transformers.md" repository.
2. Create a new virtual environment with venv, install Transformers using pip, and activate it.
3. Initialize a new Git repository in your directory using `git init`.
4. Add files to the repository using `git add .`
5. Commit changes by running `git commit -m "initial commit"`
6. Create a new project folder structure using the following command in your terminal:
   ```bash
python setup.py venv init python3 -p my_env
```
7. Make necessary configurations or run various scripts to prepare for development.

Once you have completed these steps, you can start exploring and using the Transformers framework for your machine learning projects.