---
title: 'GitHub - dirac-run/dirac: Coding Agent singularly focused efficiency and context curation. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and many many other optimizations. https://dirac.run/ · GitHub'
url: https://github.com/dirac-run/dirac
site_name: hnrss
content_file: hnrss-github-dirac-rundirac-coding-agent-singularly-focu
fetched_at: '2026-04-28T06:00:41.548357'
original_url: https://github.com/dirac-run/dirac
date: '2026-04-27'
description: Coding Agent singularly focused efficiency and context curation. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and many many other optimizations. https://dirac.run/ - dirac-run/dirac
tags:
- hackernews
- hnrss
---

dirac-run

 

/

dirac

Public

* NotificationsYou must be signed in to change notification settings
* Fork21
* Star513

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

178 Commits
178 Commits
.github/
workflows
.github/
workflows
 
 
.vscode
.vscode
 
 
agent-registry
agent-registry
 
 
assets
assets
 
 
cli
cli
 
 
evals
evals
 
 
locales
locales
 
 
proto
proto
 
 
scripts
scripts
 
 
src
src
 
 
standalone/
runtime-files
standalone/
runtime-files
 
 
walkthrough
walkthrough
 
 
webview-ui
webview-ui
 
 
.gitignore
.gitignore
 
 
.mocharc.json
.mocharc.json
 
 
.nvmrc
.nvmrc
 
 
.nycrc.unit.json
.nycrc.unit.json
 
 
.vscode-test.mjs
.vscode-test.mjs
 
 
.vscodeignore
.vscodeignore
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.jsonc
biome.jsonc
 
 
buf.yaml
buf.yaml
 
 
esbuild.mjs
esbuild.mjs
 
 
knip.json
knip.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.test.json
tsconfig.test.json
 
 
tsconfig.unit-test.json
tsconfig.unit-test.json
 
 
update_models.js
update_models.js
 
 
View all files

## Repository files navigation

# Dirac - Accurate & Highly Token Efficient Open Source AI Agent

Dirac topped theTerminal-Bench-2 leaderboardforgemini-3-flash-previewwith a 65.2% score!

It is a well studied phenomenon that any given model's reasoning ability degrades with the context length. If we can keep context tightly curated, we improve both accuracy and cost while making larger changes tractable in a single task.

Dirac is an open-source coding agent built with this in mind. It reduces API costs by64.8%on average while producing better and faster work. Using hash-anchored parallel edits, AST manipulation, and a suite of advanced optimizations. Oh, and no MCP.

Our goal: Optimize for bang-for-the-buck on tooling with bare minimum prompting instead of going blindly minimalistic.

## 📊 Evals

Dirac is benchmarked against other leading open-source agents on complex, real-world refactoring tasks. Dirac consistently achieves 100% accuracy at a fraction of the cost. These evals are run on public github repos and should be reproducible by anyone.

🏆TerminalBench 2.0 Leaderboard: Dirac recently topped theTerminal-Bench-2 leaderboardwith a65.2%score usinggemini-3-flash-preview. This outperforms both Google's official baseline (47.6%) and the top closed-source agent Junie CLI (64.3%). This was achieved without any benchmark-specific info or anyAGENTS.mdfiles being inserted.

Note on the cost table below: A bug was discovered in Cline, the parent repo, after running these evals (issue #10314). We have submitted aPR #10315to fix this. This bug caused the evals for Dirac and Cline to slightly underreport the numbers ($0.03 vs $0.05 per million token cache read). Although there won't be a large difference, we will update the evals soon.

All tasks for all models usedgemini-3-flash-previewwith thinking set tohigh

Task (Repo)

Files*

Cline

Kilo

Ohmypi

Opencode

Pimono

Roo

Dirac

Task1 (
transformers
)

8

🟢 
(diff)
 [$0.37]

🔴 
(diff)
 [N/A]

🟡 
(diff)
 [$0.24]

🟢 
(diff)
 [$0.20]

🟢 
(diff)
 [$0.34]

🟢 
(diff)
 [$0.49]

🟢 
(diff)
 [$0.13]

Task2 (
vscode
)

21

🟢 
(diff)
 [$0.67]

🟡 
(diff)
 [$0.78]

🟢 
(diff)
 [$0.63]

🟢 
(diff)
 [$0.40]

🟢 
(diff)
 [$0.48]

🟡 
(diff)
 [$0.58]

🟢 
(diff)
 [$0.23]

Task3 (
vscode
)

12

🟡 
(diff)
 [$0.42]

🟢 
(diff)
 [$0.70]

🟢 
(diff)
 [$0.64]

🟢 
(diff)
 [$0.32]

🟢 
(diff)
 [$0.25]

🟡 
(diff)
 [$0.45]

🟢 
(diff)
 [$0.16]

Task4 (
django
)

14

🟢 
(diff)
 [$0.36]

🟢 
(diff)
 [$0.42]

🟡 
(diff)
 [$0.32]

🟢 
(diff)
 [$0.24]

🟡 
(diff)
 [$0.24]

🟢 
(diff)
 [$0.17]

🟢 
(diff)
 [$0.08]

Task5 (
vscode
)

3

🔴 
(diff)
 [N/A]

🟢 
(diff)
 [$0.71]

🟢 
(diff)
 [$0.43]

🟢 
(diff)
 [$0.53]

🟢 
(diff)
 [$0.50]

🟢 
(diff)
 [$0.36]

🟢 
(diff)
 [$0.17]

Task6 (
transformers
)

25

🟢 
(diff)
 [$0.87]

🟡 
(diff)
 [$1.51]

🟢 
(diff)
 [$0.94]

🟢 
(diff)
 [$0.90]

🟢 
(diff)
 [$0.52]

🟢 
(diff)
 [$1.44]

🟢 
(diff)
 [$0.34]

Task7 (
vscode
)

13

🟡 
(diff)
 [$0.51]

🟢 
(diff)
 [$0.77]

🟢 
(diff)
 [$0.74]

🟢 
(diff)
 [$0.67]

🟡 
(diff)
 [$0.45]

🟢 
(diff)
 [$1.05]

🟢 
(diff)
 [$0.25]

Task8 (
transformers
)

3

🟢 
(diff)
 [$0.25]

🟢 
(diff)
 [$0.19]

🟢 
(diff)
 [$0.17]

🟢 
(diff)
 [$0.26]

🟢 
(diff)
 [$0.23]

🟢 
(diff)
 [$0.29]

🟢 
(diff)
 [$0.12]

Total Correct

5/8

5/8

6/8

8/8

6/8

6/8

8/8

Avg Cost

$0.49

$0.73

$0.51

$0.44

$0.38

$0.60

$0.18

🟢 Success | 🟡 Incomplete | 🔴 Failure

Cost Comparison: Dirac is64.8% cheaperthan the competition (a2.8xcost reduction).

* Expected number of files to be modified/created to complete the task.

Seeevals/README.mdfor detailed task descriptions and methodology.

## 🚀 Key Features

* Hash-Anchored Edits: Dirac uses stable line hashes to target edits with extreme precision, avoiding the "lost in translation" issues of traditional line-number based editing.
* AST-Native Precision: Built-in understanding of language syntax (TypeScript, Python, C++, etc.) allows Dirac to perform structural manipulations like function extraction or class refactoring with 100% accuracy.
* Multi-File Batching: Dirac can process and edit multiple files in a single LLM roundtrip, significantly reducing latency and API costs.
* High-Bandwidth Context: Optimized context curation keeps the agent lean and fast, ensuring the LLM always has the most relevant information without wasting tokens.
* Autonomous Tool Use: Dirac can read/write files, execute terminal commands, use a headless browser, and more - all while keeping you in control with an approval-based workflow.
* Skills & AGENTS.md: Customize Dirac's behavior with project-specific instructions usingAGENTS.mdfiles. It also seamlessly picks up Claude's skills by automatically reading from.ai,.claude, and.agentsdirectories.
* Native Tool Calling Only: To ensure maximum reliability and performance, Dirac exclusively supports models with native tool calling enabled. (Note: MCP is not supported).

## 📦 Installation

### VS Code Extension

Install Dirac from theVS Code Marketplace.

### CLI (Terminal)

Install the Dirac CLI globally using npm:

npm install -g dirac-cli

## 🚀 CLI Quick Start

1. Authenticate:dirac auth
2. Run your first task:dirac"Analyze the architecture of this project"

### Configuration (Environment Variables)

You can provide API keys via environment variables to skip thedirac authstep. This is ideal for CI/CD or non-persistent environments:

* ANTHROPIC_API_KEY
* OPENAI_API_KEY
* OPENROUTER_API_KEY
* GEMINI_API_KEY
* GROQ_API_KEY
* MISTRAL_API_KEY
* XAI_API_KEY(x.ai)
* HF_TOKEN(HuggingFace)
* ... and others (seesrc/shared/storage/env-config.tsfor the full list).

### Common Commands

* dirac "prompt": Start an interactive task.
* dirac -p "prompt": Run inPlan Modeto see the strategy before executing.
* dirac -y "prompt":Yolo Mode(auto-approve all actions, great for simple fixes).
* git diff | dirac "Review these changes": Pipe context directly into Dirac.
* dirac history: View and resume previous tasks.

## 🛠️ Getting Started

1. Open the Dirac sidebar in VS Code.
2. Configure your preferred AI provider (Anthropic, OpenAI, OpenRouter, etc.).
3. Start a new task by describing what you want to build or fix.
4. Watch Dirac go!

## 📈 Star History

## 📄 License

Dirac isopen sourceand licensed under theApache License 2.0.

## 🤝 Acknowledgments

Dirac is a fork of the excellentClineproject. We are grateful to the Cline team and contributors for their foundational work.

Built with ❤️ byMax TrivediatDirac Delta Labs

## About

Coding Agent singularly focused efficiency and context curation. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and many many other optimizations.https://dirac.run/

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

513

 stars
 

### Watchers

3

 watching
 

### Forks

21

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript95.9%
* JavaScript2.8%
* Shell0.7%
* CSS0.4%
* Roff0.2%
* Python0.0%