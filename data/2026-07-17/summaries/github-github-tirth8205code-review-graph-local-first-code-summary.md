---
title: GitHub - tirth8205/code-review-graph: Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools...
url: https://github.com/tirth8205/code-review-graph
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-17T11:37:50.133170
---

# GitHub - tirth8205/code-review-graph: Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools...

**Code Review Graph for MCPIP**

A local-first code intelligence graph that automates code review by creating a persistent map of your codebase. This allows AI coding tools to read only what matters, reducing context overhead and improving performance.

**Key Features:**

* **Persistent Map**: Builds a structural map of your code with Tree-sitter, tracking changes incrementally.
* **MCP Integration**: Gives precise context via MCMCP, reading only what matters for effective review.
* **Auto-Detection**: Detects supported platforms via `pipx` and configures MCP accordingly.

**Usage:**

1. Install `code-review-graph`.
2. To target a specific platform:
	* `pip install code-review-graph --platform [platonic]`
3. Auto-detect supported platforms using `uv.lock`.
4. Run the command to initialize everything.
5. To configure your editor or tool for local-first coding, add custom instructions by providing a configuration file (e.g., `.rc`).

**System Requirements:**

* Python 3.10+
* Tree-sitter (included in MCP installation)
* `uvxorpip` install
* `pipx` install

By using this code review graph, developers can reduce context overhead and improve the efficiency of AI-powered code reviewers. This allows them to focus on writing high-quality code rather than manually managing complex coding dependencies.