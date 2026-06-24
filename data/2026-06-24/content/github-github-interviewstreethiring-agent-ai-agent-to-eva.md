---
title: 'GitHub - interviewstreet/hiring-agent: AI agent to evaluate and score resumes. · GitHub'
url: https://github.com/interviewstreet/hiring-agent
site_name: github
content_file: github-github-interviewstreethiring-agent-ai-agent-to-eva
fetched_at: '2026-06-24T11:56:51.998133'
original_url: https://github.com/interviewstreet/hiring-agent
author: interviewstreet
description: AI agent to evaluate and score resumes. Contribute to interviewstreet/hiring-agent development by creating an account on GitHub.
---

interviewstreet

 

/

hiring-agent

Public

* NotificationsYou must be signed in to change notification settings
* Fork565
* Star1.8k

 
 
 
 
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

74 Commits
74 Commits
prompts
prompts
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
config.py
config.py
 
 
evaluator.py
evaluator.py
 
 
github.py
github.py
 
 
llm_utils.py
llm_utils.py
 
 
models.py
models.py
 
 
pdf.py
pdf.py
 
 
prompt.py
prompt.py
 
 
pymupdf_rag.py
pymupdf_rag.py
 
 
requirements.txt
requirements.txt
 
 
score.py
score.py
 
 
transform.py
transform.py
 
 
View all files

## Repository files navigation

# Hiring Agent

Resume-to-Score pipelinethat extracts structured data from PDFs, enriches with GitHub signals, and outputs a fair, explainable evaluation.

## Contents

* Overview
* Architecture
* Installation and SetupPrerequisitesQuick setup with pipOllama models
* Prerequisites
* Quick setup with pip
* Ollama models
* Configuration
* How it works
* CLI usage
* Directory layout
* Provider details
* Contributing
* License

## Overview

Hiring Agent parses a resume PDF to Markdown, extracts sectioned JSON using a local or hosted LLM, augments the data with GitHub profile and repository signals, then produces an objective evaluation with category scores, evidence, bonus points, and deductions. You can run fully local with Ollama or use Google Gemini.

## Architecture

Flow

1. pymupdf_rag.pyconverts PDF pages to Markdown-like text.
2. pdf.pycalls the LLM per section using Jinja templates underprompts/templates.
3. github.pyfetches profile and repos, classifies projects, and asks the LLM to select the top 7.
4. evaluator.pyruns a strict-scored evaluation with fairness constraints.
5. score.pyorchestrates everything end to end and writes CSV when development mode is on.

Key modules

* models.pyPydantic schemas and LLM provider interfaces.
* llm_utils.pyProvider initialization and response cleanup.
* transform.pyNormalization from loose LLM JSON to JSON Resume style.
* prompts/All Jinja templates for extraction and scoring.

## Installation and Setup

### Prerequisites

* Python 3.11+The repository pins.python-versionto 3.11.13.
* One LLM backend(either of them)Ollamafor local models
Install from theofficial site, then runollama serve.Google Geminiif you have an API key, get it fromhere.
* Ollamafor local models
Install from theofficial site, then runollama serve.
* Google Geminiif you have an API key, get it fromhere.

### Quick setup with pip

$ git clone https://github.com/interviewstreet/hiring-agent
$ 
cd
 hiring-agent

$ python -m venv .venv

#
 Linux or macOS

$ 
source
 .venv/bin/activate

#
 Windows

#
 .venv\Scripts\activate

$ pip install -r requirements.txt

### Ollama Models

Pull the model you want to use. For example:

$ ollama pull gemma3:4b

If you want different results, you can pull other models such as:

#
 For higher system configuration

$ ollama pull gemma3:12b

#
 For lower system configuration

$ ollama pull gemma3:1b

## Configuration

Copy the template and set your environment variables.

$ cp .env.example .env

Environment variables

Variable

Values

Description

LLM_PROVIDER

ollama
 or 
gemini

Chooses provider. Defaults to Ollama.

DEFAULT_MODEL

for example 
gemma3:4b
 or 
gemini-2.5-pro

Model name passed to the provider.

GEMINI_API_KEY

string

Required when 
LLM_PROVIDER=gemini
.

GITHUB_TOKEN

optional

Inherits from your shell environment, improves GitHub API rate limits.

Provider mapping lives inprompt.pyandmodels.py. Theconfig.pyfile has a single flag:

# config.py

DEVELOPMENT_MODE
 
=
 
True
 
# enables caching and CSV export

You can leave it on during iteration. See the next section for details.

## How it works

1) PDF extraction

* pymupdf_rag.pyandpdf.pyread the PDF using PyMuPDF and convert pages to Markdown-like text.
* Theto_markdownroutine handles headings, links, tables, and basic formatting.

2) Section parsing with templates

* prompts/templates/*.jinjadefine strict instructions for each section
Basics, Work, Education, Skills, Projects, Awards.
* pdf.PDFHandlercalls the LLM per section and assembles aJSONResumeobject (seemodels.py).

3) GitHub enrichment

* github.pyextracts a username from the resume profiles, fetches profile and repos, and classifies each project.
* It asks the LLM to select exactly 7 unique projects with a minimum author commit threshold, favoring meaningful contributions.

4) Evaluation

* evaluator.pyuses templates that encode fairness and scoring rules.
* Scores includeopen_source,self_projects,production, andtechnical_skills, plus bonus and deductions, then an explanation for evidence.

5) Output and CSV export

* score.pyprints a readable summary to stdout.
* WhenDEVELOPMENT_MODE=Trueit creates or appends aresume_evaluations.csvwith key fields, and caches intermediate JSON undercache/.

## CLI usage

### End to end scoring

Provide a path to a resume PDF.

$ python score.py /path/to/resume.pdf

What happens:

1. If development mode is on, the PDF extraction result is cached tocache/resumecache_<basename>.json.
2. If a GitHub profile is found in the resume, repositories are fetched and cached tocache/githubcache_<basename>.json.
3. The evaluator prints a report and, in development mode, appends a CSV row toresume_evaluations.csv.

## Directory layout

.
├── .env.example
├── .python-version
├── config.py
├── evaluator.py
├── github.py
├── llm_utils.py
├── models.py
├── pdf.py
├── prompt.py
├── prompts/
│ ├── template_manager.py
│ └── templates/
│ ├── awards.jinja
│ ├── basics.jinja
│ ├── education.jinja
│ ├── github_project_selection.jinja
│ ├── projects.jinja
│ ├── resume_evaluation_criteria.jinja
│ ├── resume_evaluation_system_message.jinja
│ ├── skills.jinja
│ ├── system_message.jinja
│ └── work.jinja
├── pymupdf_rag.py
├── requirements.txt
├── score.py
└── transform.py

## Provider details

### Ollama

* SetLLM_PROVIDER=ollama
* SetDEFAULT_MODELto any pulled model, for examplegemma3:4b
* The provider wrapper inmodels.OllamaProvidercallsollama.chat

### Gemini

* SetLLM_PROVIDER=gemini
* SetDEFAULT_MODELto a supported Gemini model, for examplegemini-2.0-flash
* ProvideGEMINI_API_KEY
* The wrapper inmodels.GeminiProvideradapts responses to a unified format

## Contributing

Please read theCONTRIBUTING.mdfor detailed guidelines on filing issues, proposing changes, and submitting pull requests. Key principles include:

* Keep prompts declarative and provider-agnostic.
* Validate changes with a couple of real resumes under different providers.
* Add or adjust unit-free smoke tests that call each stage with minimal inputs.

## License

MIT© HackerRank

## About

AI agent to evaluate and score resumes.

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.8k

 stars
 

### Watchers

4

 watching
 

### Forks

565

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

* Python84.4%
* Jinja15.6%