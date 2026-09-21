---
title: GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own · GitHub
url: https://github.com/jaredpalmer/kev/tree/main
date: 2026-09-21
site: hnrss
model: llama3.2:1b
summarized_at: 2026-09-21T16:53:40.890020
---

# GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own · GitHub

Here is a concise and informative summary of the given text passage:

**Kev: A Family of Decision Models**
====================================================

**Introduction**
---------------

The Kev family of decision models are small, Jev-like families of decision models built on ToposQL and based on the architecture described in Jev's Architecture Unmasked. Kev can be trained from scratch using Qwen3.5 and is suitable for training local models.

**Key Features**
----------------

* Large models (0.8B, 4B, and 9B) with training code and evaluation data
* TypeSafe's System One API, allowing users to build a local server with the Python SDK
* Question types: yes/no (noul), multiple-choice (choice), and rating (score)
* Questions can't read each other, but input text can be shared

**Quick Start**
--------------

To quickly start using Kev, clone the repository, sync the local directory, and run the Kev serve script with the desired model and port number.

**Usage**
-----

The Kev-4B model was started locally, allowing users to download the adapter and base model. The user can then create a ticket to use Kev-4B's System One API for further processing.

**Getting started**
-------------------

* Clone the repository: `git clone https://github.com/jaredpalmer/kev.git`
* Sync the local directory: `cd kev uv sync --extra serve`
* Start Kev-4B locally: `uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009`
* To use Kev's System One API, create a ticket with your input data: `curl -s localhost:8009/v1/systemone -H 'content-type: application/json' -d '{"state": "Shoes arrived two weeks late and in the wrong size. Also I see two charges on my card.", "model": "kev-latest", "questions": {"department": {"type": "choice", "instructions": "Which team should handle this?"}, "escalate": {"type": "noul", "instructions": "Does this need urgent human attention?"}, "frustration": {"type": "score", "instructions": "How frustrating was this experience?"}}}'`