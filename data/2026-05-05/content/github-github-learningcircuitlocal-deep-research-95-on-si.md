---
title: 'GitHub - LearningCircuit/local-deep-research: ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Everything Local & Encrypted. · GitHub'
url: https://github.com/LearningCircuit/local-deep-research
site_name: github
content_file: github-github-learningcircuitlocal-deep-research-95-on-si
fetched_at: '2026-05-05T11:59:32.711009'
original_url: https://github.com/LearningCircuit/local-deep-research
author: LearningCircuit
description: ~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Everything Local & Encrypted. - LearningCircuit/local-deep-research
---

LearningCircuit

 

/

local-deep-research

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork461
* Star4.9k

 
 
 
 
main
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

6,295 Commits
6,295 Commits
.github
.github
 
 
.pre-commit-hooks
.pre-commit-hooks
 
 
.semgrep/
rules
.semgrep/
rules
 
 
.zap
.zap
 
 
changelog.d
changelog.d
 
 
community_benchmark_results
community_benchmark_results
 
 
cookiecutter-docker
cookiecutter-docker
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
src/
local_deep_research
src/
local_deep_research
 
 
tests
tests
 
 
unraid-templates
unraid-templates
 
 
.file-whitelist.txt
.file-whitelist.txt
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.gitleaksignore
.gitleaksignore
 
 
.grype.yaml
.grype.yaml
 
 
.hadolint.yaml
.hadolint.yaml
 
 
.nvmrc
.nvmrc
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.safety-policy.yml
.safety-policy.yml
 
 
.trivyignore
.trivyignore
 
 
.yamllint.yaml
.yamllint.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bearer.yml
bearer.yml
 
 
docker-compose.gpu.override.yml
docker-compose.gpu.override.yml
 
 
docker-compose.unraid.yml
docker-compose.unraid.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.js
eslint.config.js
 
 
lighthouserc.json
lighthouserc.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pdm.lock
pdm.lock
 
 
playwright.config.js
playwright.config.js
 
 
pyproject.toml
pyproject.toml
 
 
vite.config.js
vite.config.js
 
 
vulture_whitelist.py
vulture_whitelist.py
 
 
View all files

## Repository files navigation

# Local Deep Research

AI-powered research assistant for deep, agentic research

Performs deep, agentic research using multiple LLMs and search engines with proper citations

▶️
 Watch Review by The Art Of The Terminal

## 🚀 What is Local Deep Research?

AI research assistant you control. Run locally for privacy, use any LLM and build your own searchable knowledge base. You own your data and see exactly how it works.

## ⚡ Quick Start

Option 1: Docker Run (Linux)

#
 Step 1: Pull and run Ollama

docker run -d -p 11434:11434 --name ollama ollama/ollama
docker 
exec
 ollama ollama pull gpt-oss:20b

#
 Step 2: Pull and run SearXNG for optimal search results

docker run -d -p 8080:8080 --name searxng searxng/searxng

#
 Step 3: Pull and run Local Deep Research

docker run -d -p 5000:5000 --network host \
 --name local-deep-research \
 --volume 
"
deep-research:/data
"
 \
 -e LDR_DATA_DIR=/data \
 localdeepresearch/local-deep-research

Option 2: Docker Compose

CPU-only (all platforms):

curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.yml 
&&
 docker compose up -d

With NVIDIA GPU (Linux):

curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.yml 
&&
 \
curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.gpu.override.yml 
&&
 \
docker compose -f docker-compose.yml -f docker-compose.gpu.override.yml up -d

Openhttp://localhost:5000after ~30 seconds. For GPU setup, environment variables, and more, see theDocker Compose Guide.

Option 3: pip install

pip install local-deep-research

Works on Windows, macOS, and Linux. SQLCipher encryption is included via pre-built wheels — no compilation needed.
PDF export on Windows requires Pango (setup guide).
If you encounter issues with encryption, setexport LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=trueto use standard SQLite instead.

More install options →

## 🏗️ How It Works

### Research

You ask a complex question. LDR:

* Does the research for you automatically
* Searches across web, academic papers, and your own documents
* Synthesizes everything into a report with proper citations

Choose from 20+ research strategies for quick facts, deep analysis, or academic research.

New: LangGraph Agent Strategy— An autonomous agentic research mode where the LLM decides what to search, which specialized engines to use (arXiv, PubMed, Semantic Scholar, etc.), and when to synthesize. Early results are promising — it adaptively switches between search engines based on what it finds and collects significantly more sources than pipeline-based strategies. Selectlanggraph-agentin Settings to try it.

### Build Your Knowledge Base

flowchart LR
 R[Research] --> D[Download Sources]
 D --> L[(Library)]
 L --> I[Index & Embed]
 I --> S[Search Your Docs]
 S -.-> R

 
Loading

Every research session finds valuable sources. Download them directly into your encrypted library—academic papers from ArXiv, PubMed articles, web pages. LDR extracts text, indexes everything, and makes it searchable. Next time you research, ask questions across your own documents and the live web together. Your knowledge compounds over time.

## 🛡️ Security

flowchart LR
 U1[User A] --> D1[(Encrypted DB)]
 U2[User B] --> D2[(Encrypted DB)]

 
Loading

Your data stays yours. Each user gets their own isolated SQLCipher database encrypted with AES-256 (Signal-level security). No password recovery means true zero-knowledge—even server admins can't read your data. Run fully local with Ollama + SearXNG and nothing ever leaves your machine.

In-memory credentials: Like all applications that use secrets at runtime — includingpassword managers, browsers, and API clients — credentials are held in plain text in process memory during active sessions. This is anindustry-wide accepted reality, not specific to LDR: if an attacker can read process memory, they can also read any in-process decryption key. We mitigate this with session-scoped credential lifetimes and core dump exclusion. Ideas for further improvements are always welcome viaGitHub Issues. See ourSecurity Policyfor details.

Supply Chain Security: Docker images are signed withCosign, include SLSA provenance attestations, and attach SBOMs. Verify with:

cosign verify localdeepresearch/local-deep-research:latest

Security Transparency: Scanner suppressions are documented with justifications inSecurity Alerts Assessment,Scorecard Compliance,Container CVE Suppressions, andSAST Rule Rationale. Some alerts (Dependabot, code scanning) can only be dismissed or are very difficult to suppress outside theGitHub Security tab, so the files above do not cover every dismissed finding.

Detailed Architecture →|Security Policy →|Security Review Process →

### 🔒 Privacy & Data

Local Deep Research containsno telemetry, no analytics, and no tracking. We do not collect, transmit, or store any data about you or your usage. No analytics SDKs, no phone-home calls, no crash reporting, no external scripts. Usage metrics stay in your local encrypted database.

The only network calls LDR makes are onesyouinitiate: search queries (to engines you configure), LLM API calls (to your chosen provider), and notifications (only if you set up Apprise).

Since we don't collect any usage data, we rely on you to tell us what works, what's broken, and what you'd like to see next —bug reports, feature ideas, and even which features you love or never use all help us improve LDR.

## 📊 Performance

~95% accuracy on SimpleQA benchmark(preliminary results)

* Tested with GPT-4.1-mini + SearXNG + focused-iteration strategy
* Comparable to state-of-the-art AI research systems
* Local models can achieve similar performance with proper configuration

### 🧭 Picking a model? Use the community benchmarks

Not sure which local model to run with LDR? The community-maintainedLDR Benchmarks dataset on Hugging Facetracks accuracy across models, search engines, and research strategies — it's the fastest way to see which Ollama / LM Studio / llama.cpp models actually work well for deep research before you download multi-GB weights.

* Browse leaderboards & download CSVs on Hugging Face →
* Submit your own results on GitHub →

## ✨ Key Features

### 🔍 Research Modes

* Quick Summary- Get answers in 30 seconds to 3 minutes with citations
* Detailed Research- Comprehensive analysis with structured findings
* Report Generation- Professional reports with sections and table of contents
* Document Analysis- Search your private documents with AI

### 🛠️ Advanced Capabilities

* LangChain Integration- Use any vector store as a search engine
* REST API- Authenticated HTTP access with per-user databases
* Benchmarking- Test and optimize your configuration
* Analytics Dashboard- Track costs, performance, and usage metrics
* Journal Quality System- Automatic journal reputation scoring with 212K+ indexed sources, predatory detection, and quality dashboard. Powered byOpenAlex(CC0),DOAJ(CC0), andStop Predatory Journals(MIT).
* Real-time Updates- WebSocket support for live research progress
* Export Options- Download results as PDF or Markdown
* Research History- Save, search, and revisit past research
* Adaptive Rate Limiting- Intelligent retry system that learns optimal wait times
* Keyboard Shortcuts- Navigate efficiently (ESC, Ctrl+Shift+1-5)
* Per-User Encrypted Databases- Secure, isolated data storage for each user

### 📰 News & Research Subscriptions

* Automated Research Digests- Subscribe to topics and receive AI-powered research summaries
* Customizable Frequency- Daily, weekly, or custom schedules for research updates
* Smart Filtering- AI filters and summarizes only the most relevant developments
* Multi-format Delivery- Get updates as markdown reports or structured summaries
* Topic & Query Support- Track specific searches or broad research areas

### 🌐 Search Sources

#### Free Search Engines

* Academic: arXiv, PubMed, Semantic Scholar
* General: Wikipedia, SearXNG
* Technical: GitHub, Elasticsearch
* Historical: Wayback Machine
* News: The Guardian, Wikinews

#### Premium Search Engines

* Tavily- AI-powered search
* Google- Via SerpAPI or Programmable Search Engine
* Brave Search- Privacy-focused web search

#### Custom Sources

* Local Documents- Search your files with AI
* LangChain Retrievers- Any vector store or database
* Meta Search- Combine multiple engines intelligently

LDR respectsrobots.txtand identifies itself honestly when fetching web pages — no stealth or anti-detection techniques. In rare cases this means a page that blocks automated access won't be fetched, which we consider the right trade-off.

Full Search Engines Guide →

## 📦 Installation Options

For most users, theQuick Startabove is all you need.

Method

Best for

Guide

Docker Compose

Most users (recommended)

Docker Compose Guide

Docker

Minimal setup

Installation Guide

pip

Developers, Python integration

pip Guide

Unraid

Unraid servers

Unraid Guide

All installation options →

## 💻 Usage Examples

### Python API

from
 
local_deep_research
.
api
 
import
 
LDRClient
, 
quick_query

# Option 1: Simplest - one line research

summary
 
=
 
quick_query
(
"username"
, 
"password"
, 
"What is quantum computing?"
)

print
(
summary
)

# Option 2: Client for multiple operations

client
 
=
 
LDRClient
()

client
.
login
(
"username"
, 
"password"
)

result
 
=
 
client
.
quick_research
(
"What are the latest advances in quantum computing?"
)

print
(
result
[
"summary"
])

### HTTP API

The code example below shows the basic API structure - for working examples, see the link below

import
 
requests

from
 
bs4
 
import
 
BeautifulSoup

# Create session and authenticate

session
 
=
 
requests
.
Session
()

login_page
 
=
 
session
.
get
(
"http://localhost:5000/auth/login"
)

soup
 
=
 
BeautifulSoup
(
login_page
.
text
, 
"html.parser"
)

login_csrf
 
=
 
soup
.
find
(
"input"
, {
"name"
: 
"csrf_token"
}).
get
(
"value"
)

# Login and get API CSRF token

session
.
post
(
"http://localhost:5000/auth/login"
,
 
data
=
{
"username"
: 
"user"
, 
"password"
: 
"pass"
, 
"csrf_token"
: 
login_csrf
})

csrf
 
=
 
session
.
get
(
"http://localhost:5000/auth/csrf-token"
).
json
()[
"csrf_token"
]

# Make API request

response
 
=
 
session
.
post
(
"http://localhost:5000/api/start_research"
,
 
json
=
{
"query"
: 
"Your research question"
},
 
headers
=
{
"X-CSRF-Token"
: 
csrf
})

🚀Ready-to-use HTTP API Examples → examples/api_usage/http/

* ✅Automatic user creation- works out of the box
* ✅Complete authenticationwith CSRF handling
* ✅Result retry logic- waits until research completes
* ✅Progress monitoringand error handling

### Command Line Tools

#
 Run benchmarks from CLI

python -m local_deep_research.benchmarks --dataset simpleqa --examples 50

#
 Manage rate limiting

python -m local_deep_research.web_search_engines.rate_limiting status
python -m local_deep_research.web_search_engines.rate_limiting reset

## 🔗 Enterprise Integration

Connect LDR to your existing knowledge base:

from
 
local_deep_research
.
api
 
import
 
quick_summary

# Use your existing LangChain retriever

result
 
=
 
quick_summary
(
 
query
=
"What are our deployment procedures?"
,
 
retrievers
=
{
"company_kb"
: 
your_retriever
},
 
search_tool
=
"company_kb"

)

Works with: FAISS, Chroma, Pinecone, Weaviate, Elasticsearch, and any LangChain-compatible retriever.

Integration Guide →

## 🔌 MCP Server (Claude Integration)

LDR provides an MCP (Model Context Protocol) server that allows AI assistants like Claude Desktop and Claude Code to perform deep research.

⚠️Security Note: This MCP server is designed forlocal use onlyvia STDIO transport (e.g., Claude Desktop). It has no built-in authentication or rate limiting. Do not expose over a network without implementing proper security controls. See theMCP Security Guidefor network deployment requirements.

### Installation

#
 Install with MCP extras

pip install 
"
local-deep-research[mcp]
"

### Claude Desktop Configuration

Add to yourclaude_desktop_config.json:

{
 
"mcpServers"
: {
 
"local-deep-research"
: {
 
"command"
: 
"
ldr-mcp
"
,
 
"env"
: {
 
"LDR_LLM_PROVIDER"
: 
"
openai
"
,
 
"LDR_LLM_OPENAI_API_KEY"
: 
"
sk-...
"

 }
 }
 }
}

### Claude Code Configuration

Add to your.mcp.json(project-level) or~/.claude/mcp.json(global):

{
 
"mcpServers"
: {
 
"local-deep-research"
: {
 
"command"
: 
"
ldr-mcp
"
,
 
"env"
: {
 
"LDR_LLM_PROVIDER"
: 
"
ollama
"
,
 
"LDR_LLM_OLLAMA_URL"
: 
"
http://localhost:11434
"

 }
 }
 }
}

### Available Tools

Tool

Description

Duration

LLM Cost

search

Raw results from a specific engine (arxiv, pubmed, wikipedia, ...)

5-30s

None

quick_research

Fast research summary

1-5 min

Yes

detailed_research

Comprehensive analysis

5-15 min

Yes

generate_report

Full markdown report

10-30 min

Yes

analyze_documents

Search local collections

30s-2 min

Yes

list_search_engines

List available search engines

instant

None

list_strategies

List research strategies

instant

None

get_configuration

Get current config

instant

None

### Individual Search Engines

Thesearchtool lets you query specific search engines directly and get raw results (title, link, snippet) — no LLM processing, no cost, fast. This is especially useful formonitoring and subscriptionswhere you want to check for new content regularly without burning LLM tokens.

# Search arXiv for recent papers
search(query="transformer architecture improvements", engine="arxiv")

# Search PubMed for medical literature
search(query="CRISPR clinical trials 2024", engine="pubmed")

# Search Wikipedia for quick facts
search(query="quantum error correction", engine="wikipedia")

# Search OpenClaw for legal case law
search(query="copyright fair use precedents", engine="openclaw")

# Use list_search_engines() to see all available engines

### Example Usage

"Use quick_research to find information about quantum computing applications"
"Search arxiv for recent papers on diffusion models"
"Generate a detailed research report on renewable energy trends"

## 📊 Performance & Analytics

### Benchmark Results

Early experiments on small SimpleQA dataset samples:

Configuration

Accuracy

Notes

gpt-4.1-mini + SearXNG + focused_iteration

90-95%

Limited sample size

gpt-4.1-mini + Tavily + focused_iteration

90-95%

Limited sample size

gemini-2.0-flash-001 + SearXNG

82%

Single test run

Note: These are preliminary results from initial testing. Performance varies significantly based on query types, model versions, and configurations.Run your own benchmarks →

Full community leaderboard:The community maintains a growing collection of benchmark results across models, strategies, and search engines in a dedicated repo with CI-validated submissions and auto-generated leaderboards:

* GitHub: LearningCircuit/ldr-benchmarks— submit your results here
* Hugging Face: local-deep-research/ldr-benchmarks— browse leaderboards and download CSVs

### Benchmark Contributors

Thanks to the community members who have contributed benchmark runs:

See all contributors →

### Built-in Analytics Dashboard

Track costs, performance, and usage with detailed metrics.Learn more →

## 🤖 Supported LLMs

### Local Models

* Ollama— connect to its native API (defaulthttp://localhost:11434)
* LM Studio— connect to its OpenAI-compatible server (defaulthttp://localhost:1234/v1)
* llama.cpp— connect tollama-server's OpenAI-compatible endpoint (defaulthttp://localhost:8080/v1); start withllama-server -m <model.gguf>
* Common models: Llama 3, Mistral, Gemma, DeepSeek, Qwen
* LLM processing stays local (search queries still go to web). No API costs.

💡Which local model should I pick?Check theLDR Benchmarks dataset on Hugging Face— community-submitted accuracy numbers across local and cloud models, so you can compare before downloading. Also onGitHubif you want to submit your own runs.

### Cloud Models

* OpenAI (GPT-4, GPT-3.5)
* Anthropic (Claude 3)
* Google (Gemini)
* 100+ models via OpenRouter

Model Setup →

### Upgrading from earlier versions

* llm.modelno longer has a default.Pre-1.7 installs auto-filledgemma3:12b(Ollama) when no model was configured, which silently downloaded a multi-GB binary. The field is now empty by default — pick a model in Settings → LLM, or research will fail loudly with a clear error.
* Thellamacppprovider now uses HTTP instead of in-process loading.If you previously setllm.llamacpp_model_pathto a local.gguffile, that setting is no longer read. Instead, runllama-server -m <your-model.gguf>(it ships with every modern llama.cpp build) and the defaultllm.llamacpp.urlofhttp://localhost:8080/v1will pick it up. Optional API key support is available viallm.llamacpp.api_keyif you putllama-serverbehind an auth proxy.

## 📚 Documentation

### Getting Started

* Installation Guide
* Frequently Asked Questions
* API Quickstart
* Configuration Guide
* Full Configuration Reference

### Core Features

* All Features Guide
* Search Engines Guide
* Analytics Dashboard

### Advanced Features

* LangChain Integration
* Benchmarking System
* Elasticsearch Setup
* SearXNG Setup

### Development

* Docker Compose Guide
* Development Guide
* Security Guide
* Release Guide

### Examples & Tutorials

* API Examples
* Benchmark Examples
* Optimization Examples

## 📰 Featured In

"Local Deep Researchdeserves special mentionfor those who prioritize privacy...tuned to use open-source LLMsthat can run on consumer GPUs or even CPUs. Journalists, researchers, or companies with sensitive topics can investigate informationwithout queries ever hitting an external server."

—Medium: Open-Source Deep Research AI Assistants

### News & Articles

* Korben.info- French tech blog ("Sherlock Holmes numérique")
* Roboto.fr- "L'alternative open-source gratuite à Deep Research d'OpenAI"
* KDJingPai AI Tools- AI productivity tools coverage
* AI Sharing Circle- AI resources coverage

### Community Discussions

* Hacker News- 190+ points, community discussion
* LangChain Twitter/X- Official LangChain promotion
* LangChain LinkedIn- 400+ likes

### International Coverage

#### 🇨🇳 Chinese

* Juejin (掘金)- Developer community
* Cnblogs (博客园)- Developer blogs
* GitHubDaily (Twitter/X)- Influential tech account
* Zhihu (知乎)- Tech community
* A姐分享- AI resources
* CSDN- Installation guide
* NetEase (网易)- Tech news portal

#### 🇯🇵 Japanese

* note.com: 調査革命：Local Deep Research徹底活用法- Comprehensive tutorial
* Qiita: Local Deep Researchを試す- Docker setup guide
* LangChainJP (Twitter/X)- Japanese LangChain community

#### 🇰🇷 Korean

* PyTorch Korea Forum- Korean ML community
* GeekNews (Hada.io)- Korean tech news

### Reviews & Analysis

* BSAIL Lab: How useful is Deep Research in Academia?- Academic review by contributor@djpetti
* The Art Of The Terminal: Use Local LLMs Already!- Comprehensive review of local AI tools, featuring LDR's research capabilities (embeddings now work!)

### Related Projects

* SearXNG LDR-Academic- Academic-focused SearXNG fork with 12 research engines (arXiv, Google Scholar, PubMed, etc.) designed for LDR
* DeepWiki Documentation- Third-party documentation and guides

Note:Third-party projects and articles are independently maintained. We link to them as useful resources but cannot guarantee their code quality or security.

## 🤝 Community & Support

* Discord- Get help and share research techniques
* Reddit- Updates and showcases
* GitHub Issues- Bug reports

## 🚀 Contributing

We welcome contributions of all sizes — from typo fixes to new features. The key rule:keep PRs small and atomic(one change per PR). For larger changes, please open an issue or start a discussion first — we want to protect your time and make sure your effort leads to a successful merge rather than a misaligned PR. See ourContributing Guideto get started.

## Acknowledgements

Local Deep Research is built on the work of many open-access initiatives, academic databases, and open-source projects. We are grateful to:

### Academic & Research Data

Source

What It Provides

License

OpenAlex

Academic metadata for ~280K sources and ~120K institutions, including DOAJ status

CC0

DOAJ

Directory of Open Access Journals — open-access verification (via OpenAlex)

CC0

arXiv

Preprints in physics, mathematics, CS, and more

Various (see arXiv license)

PubMed / NCBI

Biomedical and life sciences literature

Public domain (US Gov)

Semantic Scholar

Cross-discipline academic search with citation data

Terms

NASA ADS

Astrophysics, physics, and astronomy papers

Terms

Zenodo

Open research data, datasets, and software

Various per record

PubChem

Chemistry and biochemistry database

Public domain (US Gov)

Stop Predatory Journals

Predatory journal/publisher blacklist

MIT

JabRef

Journal abbreviation database

CC0

### Knowledge & Content Sources

Wikipedia•OpenLibrary•Project Gutenberg•GitHub•Stack Exchange•The Guardian•Wayback Machine

### Infrastructure & Frameworks

LangChain•Ollama•SearXNG•FAISS

### Support Open Access

These projects run on donations and grants, not paywalls. If Local Deep Research is useful to you, consider giving back to the open-access ecosystem that makes it possible:

* arXiv— free preprints for physics, math, CS, and more
* PubMed / NLM— open biomedical literature
* Wikipedia / Wikimedia— the free encyclopedia
* Internet Archive— the Wayback Machine and open digital library
* DOAJ— curating and verifying open-access journals worldwide
* OpenAlex— open scholarly metadata (sponsored byOurResearch)
* Project Gutenberg— free ebooks since 1971

## 📄 License

MIT License - seeLICENSEfile.

Dependencies:All third-party packages use permissive licenses (MIT, Apache-2.0, BSD, etc.) - seeallowlist

## About

~95% on SimpleQA (e.g. Qwen3.6-27B on a 3090). Supports all local and cloud LLMs (llama.cpp, Ollama, Google, ...). 10+ search engines - arXiv, PubMed, your private documents. Everything Local & Encrypted.

### Topics

 home-automation

 encryption

 research

 local

 homeserver

 self-hosted

 pubmed

 openai

 brave

 research-tool

 arxiv

 academia

 mistral

 searxng

 anthropic

 local-llm

 retrieval-augmented-generation

 ollama

 deep-research

 local-deep-research

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.9k

 stars
 

### Watchers

31

 watching
 

### Forks

461

 forks
 

 Report repository

 

## Releases153

Release 1.6.9

 Latest

 

May 2, 2026

 

+ 152 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* ko-fi.com/localdeepresearch

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python84.0%
* JavaScript11.9%
* HTML2.6%
* CSS1.4%
* Shell0.1%
* Dockerfile0.0%