---
title: GitHub - MadsLorentzen/ai-job-search: AI-powered job application framework built on Claude Code. Fork it, fill in your profile, and let Claude evaluat...
url: https://github.com/MadsLorentzen/ai-job-search
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-07T12:08:28.722718
---

# GitHub - MadsLorentzen/ai-job-search: AI-powered job application framework built on Claude Code. Fork it, fill in your profile, and let Claude evaluat...

# AI Job Search Framework Overview

**Overview**

The AI Job Search framework is a structured workflow built on Claude Code, an open-source job application engine. The framework provides a comprehensive solution for career guidance, including:

* Self-profiling and fit evaluation
* Tailored CV generation and cover letter preparation
* Salary benchmarking and recommendation
* Keyword search functionality

**Key Features**

* **Language-agnostic**: The framework is designed to work with multiple languages and countries.
* ** Danish job market support**: Pre-built support for popular Danish job boards, such as Jobindex and Jobnet.
* **Claude Code integration**: Seamless connection to Claude's job application engine.
* **Automated keyword processing**: Optional use of LaTeX distribution and font specification tools to ensure compatibility with modern fonts.

**Prerequisites**

* **Claude Code (CLI)**: Must be installed and configured for Python 3.10+.
* **Bun (Danish job search CLI tool)**: For Danish market support.
* **LaTeX distribution**: Includes LaTeX compilation utilities, such as xelatex and pdflatex.

**Quick Start**

1. Fork and clone the repository `github repo fork MadsLorentzen/ai-job-search --clone`.
2. Install the required job search tools:
	+ Clone the Danish market support tool: `./agents/skills/jobdanmark-search/cli`
3. Clone the Jobindex Search Tool: `./jobs/index-search/cli`
4. Clone the Jobnet Search Tool: `./jobs/index-engine/cli`

## Setting Up Your Profile

1. **Fork the framework**: Clone the repository and rename it to your preferred name.
2. **Install dependencies**: Use Bun to install required packages: `bun init /path/to/your/profile`.
3. **Fill in your profile**: Complete your profile with relevant attributes, such as education and work experience.

## Launching Your Job Search

1. **Launch the framework**: Run: `./fraud/runner`
2. **Select your job index**: Choose an available job index (Jobindex or Jobnet) to search for jobs.
3. **Provide a keyword search term**: Add relevant keywords to help Claude Code engine narrow down results.

**Example Use Cases**

* Generating a CV tailored to specific industries or job roles: `./fraud/runner -b agents/skills/cv-gen-cli`
* Preparing cover letters with optimized salary benchmarks: `./fraud/runner -c agents/skills/salary-gen-cli`

Note: This summary aims to provide an overview of the AI Job Search framework and its key features. For a comprehensive understanding, I recommend exploring the original repository and documentation for further details.