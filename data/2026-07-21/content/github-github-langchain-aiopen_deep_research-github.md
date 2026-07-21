---
title: GitHub - langchain-ai/open_deep_research · GitHub
url: https://github.com/langchain-ai/open_deep_research
site_name: github
content_file: github-github-langchain-aiopen_deep_research-github
fetched_at: '2026-07-21T19:33:14.897105'
original_url: https://github.com/langchain-ai/open_deep_research
author: langchain-ai
description: Contribute to langchain-ai/open_deep_research development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 langchain-ai

 

/

open_deep_research

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star12.2k

 
 
 
 
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

220 Commits
220 Commits
.github
.github
 
 
examples
examples
 
 
src
src
 
 
tests
tests
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
langgraph.json
langgraph.json
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# 🔬 Open Deep Research

Deep research has broken out as one of the most popular agent applications. This is a simple, configurable, fully open source deep research agent that works across many model providers, search tools, and MCP servers. It's performance is on par with many popular deep research agents (see Deep Research Bench leaderboard).

### 🔥 Recent Updates

August 14, 2025: See our free coursehere(and course repohere) on building open deep research.

August 7, 2025: Added GPT-5 and updated the Deep Research Bench evaluation w/ GPT-5 results.

August 2, 2025: Achieved #6 ranking on theDeep Research Bench Leaderboardwith an overall score of 0.4344.

July 30, 2025: Read about the evolution from our original implementations to the current version in ourblog post.

July 16, 2025: Read more in ourblogand watch ourvideofor a quick overview.

### 🚀 Quickstart

1. Clone the repository and activate a virtual environment:

git clone https://github.com/langchain-ai/open_deep_research.git

cd
 open_deep_research
uv venv

source
 .venv/bin/activate 
#
 On Windows: .venv\Scripts\activate

1. Install dependencies:

uv sync

#
 or

uv pip install -r pyproject.toml

1. Set up your.envfile to customize the environment variables (for model selection, search tools, and other configuration settings):

cp .env.example .env

1. Launch agent with the LangGraph server locally:

#
 Install dependencies and start the LangGraph server

uvx --refresh --from 
"
langgraph-cli[inmem]
"
 --with-editable 
.
 --python 3.11 langgraph dev --allow-blocking

This will open the LangGraph Studio UI in your browser.

- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

Ask a question in themessagesinput field and clickSubmit. Select different configuration in the "Manage Assistants" tab.

### ⚙️ Configurations

#### LLM 🧠

Open Deep Research supports a wide range of LLM providers via theinit_chat_model() API. It uses LLMs for a few different tasks. See the below model fields in theconfiguration.pyfile for more details. This can be accessed via the LangGraph Studio UI.

* Summarization(default:openai:gpt-4.1-mini): Summarizes search API results
* Research(default:openai:gpt-4.1): Power the search agent
* Compression(default:openai:gpt-4.1): Compresses research findings
* Final Report Model(default:openai:gpt-4.1): Write the final report

Note: the selected model will need to supportstructured outputsandtool calling.

Note: For OpenRouter: Followthis guideand for local models via Ollama seesetup instructions.

#### Search API 🔍

Open Deep Research supports a wide range of search tools. By default it uses theTavilysearch API. Has full MCP compatibility and work native web search for Anthropic and OpenAI. See thesearch_apiandmcp_configfields in theconfiguration.pyfile for more details. This can be accessed via the LangGraph Studio UI.

#### Other

See the fields in theconfiguration.pyfor various other settings to customize the behavior of Open Deep Research.

### 📊 Evaluation

Open Deep Research is configured for evaluation withDeep Research Bench. This benchmark has 100 PhD-level research tasks (50 English, 50 Chinese), crafted by domain experts across 22 fields (e.g., Science & Tech, Business & Finance) to mirror real-world deep-research needs. It has 2 evaluation metrics, but the leaderboard is based on the RACE score. This uses LLM-as-a-judge (Gemini) to evaluate research reports against a golden set of reports compiled by experts across a set of metrics.

#### Usage

Warning: Running across the 100 examples can cost ~$20-$100 depending on the model selection.

The dataset is available onLangSmith via this link. To kick off evaluation, run the following command:

#
 Run comprehensive evaluation on LangSmith datasets

python tests/run_evaluate.py

This will provide a link to a LangSmith experiment, which will have a nameYOUR_EXPERIMENT_NAME. Once this is done, extract the results to a JSONL file that can be submitted to the Deep Research Bench.

python tests/extract_langsmith_data.py --project-name 
"
YOUR_EXPERIMENT_NAME
"
 --model-name 
"
you-model-name
"
 --dataset-name 
"
deep_research_bench
"

This createstests/expt_results/deep_research_bench_model-name.jsonlwith the required format. Move the generated JSONL file to a local clone of the Deep Research Bench repository and follow theirQuick Start guidefor evaluation submission.

#### Results

Name

Commit

Summarization

Research

Compression

Total Cost

Total Tokens

RACE Score

Experiment

GPT-5

ca3951d

openai:gpt-4.1-mini

openai:gpt-5

openai:gpt-4.1

204,640,896

0.4943

Link

Defaults

6532a41

openai:gpt-4.1-mini

openai:gpt-4.1

openai:gpt-4.1

$45.98

58,015,332

0.4309

Link

Claude Sonnet 4

f877ea9

openai:gpt-4.1-mini

anthropic:claude-sonnet-4-20250514

openai:gpt-4.1

$187.09

138,917,050

0.4401

Link

Deep Research Bench Submission

c0a160b

openai:gpt-4.1-nano

openai:gpt-4.1

openai:gpt-4.1

$87.83

207,005,549

0.4344

Link

### 🚀 Deployments and Usage

#### LangGraph Studio

Follow thequickstartto start LangGraph server locally and test the agent out on LangGraph Studio.

#### Hosted deployment

You can easily deploy toLangGraph Platform.

#### Open Agent Platform

Open Agent Platform (OAP) is a UI from which non-technical users can build and configure their own agents. OAP is great for allowing users to configure the Deep Researcher with different MCP tools and search APIs that are best suited to their needs and the problems that they want to solve.

We've deployed Open Deep Research to our public demo instance of OAP. All you need to do is add your API Keys, and you can test out the Deep Researcher for yourself! Try it outhere

You can also deploy your own instance of OAP, and make your own custom agents (like Deep Researcher) available on it to your users.

1. Deploy Open Agent Platform
2. Add Deep Researcher to OAP

### Legacy Implementations 🏛️

Thesrc/legacy/folder contains two earlier implementations that provide alternative approaches to automated research. They are less performant than the current implementation, but provide alternative ideas understanding the different approaches to deep research.

#### 1. Workflow Implementation (legacy/graph.py)

* Plan-and-Execute: Structured workflow with human-in-the-loop planning
* Sequential Processing: Creates sections one by one with reflection
* Interactive Control: Allows feedback and approval of report plans
* Quality Focused: Emphasizes accuracy through iterative refinement

#### 2. Multi-Agent Implementation (legacy/multi_agent.py)

* Supervisor-Researcher Architecture: Coordinated multi-agent system
* Parallel Processing: Multiple researchers work simultaneously
* Speed Optimized: Faster report generation through concurrency
* MCP Support: Extensive Model Context Protocol integration

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

12.2k

 stars
 

### Watchers

74

 watching
 

### Forks

1.7k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python69.6%
* Jupyter Notebook30.4%