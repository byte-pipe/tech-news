---
title: GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub
url: https://github.com/z-lab/dflash
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-17T06:14:29.258451
---

# GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub

**z-lab/DFlash: Block Diffusion for Flash Speculative Decoding**

* **Overview**: A lightweight block diffusion model designed for speculative decoding, enabling efficient and high-quality parallel drafting.
* **Key Features**:
	+ Supports various prompt styles
	+ Handles different models and architectures
	+ Optimized for low-resource environments
* **Technical Details**:
	+ Utilizes a block diffusion architecture
	+ Allows for parallel drafting and decoding
	+ Experimental support for speed optimization techniques

**Supported Models**

* Kimi-K2.5 (Preview)
* z-lab/Kimi-K2.5-DFlash
* Qwen3.5-4B (non-thinking)
* Qwen3-4B-DFlash-b16
* ... and more to come

**Repository Files Navigation**

The repository contains a variety of files:

* `README.md` provides an overview of the project and its features
* `pyproject.toml` manages dependencies for PyTorch-based models (vLLM)
* `.gitignore` specifies files that should be ignored during the git lifecycle

**Installation**

Requires separate virtual environments to avoid conflicts, with various options for backend implementations:

* `Transformers`: a pre-installed backend
* `SGLang`: supports custom background jobs (SGLang)
* `vLLM`: utilizes Nightly builds of vLLM and requires Torch backend configuration

**Quick Start**

* Use `uv pip install -e ".[transformers]"` to install PyTorch-based models (vLLM)
* Choose an applicable backend: `Transformers`, `SGLang`, or `vLLM`
* Use command-line interface options to configure the model and attention-backend

**Additional Notes**

* Experimental support for speed optimization techniques is available.
* GitHub issues can be opened to request additional models.
