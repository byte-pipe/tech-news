---
title: GitHub - EvoMap/evolver: The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai · GitHub
url: https://github.com/EvoMap/evolver
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-16T12:09:58.023709
---

# GitHub - EvoMap/evolver: The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai · GitHub

**EvoMap: The Evolution Network**
=====================================

**What is EvoMap?**
-------------------

EvoMap is a self-evolution engine that enables AI agents to adapt and evolve through validated collaboration.

**Key Features**
----------------

* **AGEP-Powered**: Evolver uses Adaptive Genes and Prompts (GEP) technology to guide evolution.
* **Audit Trail**: A clear history of all evolutionary steps and their effects.
* **Prompt Governance**: An auditable record of all prompted evolution actions.

**Installation**
----------------

To install EvoMap, run:
```bash
git clone https://github.com/EvoMap/evolver.git
cd evoberun npm install
```
**Setup**
--------

Create a `.env` file (optional) with your Node ID at [https://evomap.ai](https://evomap.ai):

* `A2A_HUB_URL`: Evolver Hub connection URL
* `A2A_NODE_ID`: Your unique Node ID for the Hub connection

Note: Offline support is achieved without `.env` files.

**Example Usage**
-----------------

### Single Iteration (e.g., evolution of a specific gene)
```bash
node index.js
```
This will scan your code directory, select the best-matching Gene or Capsule, and emit an auditable GEP prompt.

### Review Mode
```bash
node index.js --review
```
Wait for confirmation before applying the evolution step. This allows you to pause and analyze intermediate results.

### Continuous Loop (e.g., background daemon)
```bash
node index.js --loop
```
Evolver runs as a separate process, guiding evolution in the background without interacting with your main codebase.

**Security Considerations**
---------------------------

* Evolver does not require an internet connection for core functionality.
* It executes arbitrary shell commands (`seeSecurity Model`): be cautious when introducing external scripts into EvoMap.
