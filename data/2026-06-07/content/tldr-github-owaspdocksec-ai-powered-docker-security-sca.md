---
title: 'GitHub - OWASP/DockSec: AI-powered Docker security scanner that explains vulnerabilities in plain English. An OWASP Incubator Project. · GitHub'
url: https://github.com/OWASP/DockSec
site_name: tldr
content_file: tldr-github-owaspdocksec-ai-powered-docker-security-sca
fetched_at: '2026-06-07T19:33:26.497240'
original_url: https://github.com/OWASP/DockSec
date: '2026-06-07'
description: AI-powered Docker security scanner that explains vulnerabilities in plain English. An OWASP Incubator Project. - OWASP/DockSec
tags:
- tldr
---

OWASP

 

/

DockSec

Public

* NotificationsYou must be signed in to change notification settings
* Fork69
* Star356

 
 
 
 
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

217 Commits
217 Commits
.github
.github
 
 
docksec
docksec
 
 
docs
docs
 
 
images
images
 
 
tests
tests
 
 
.DS_Store
.DS_Store
 
 
.cursorrules
.cursorrules
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
MENTORS.md
MENTORS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SPONSORSHIP.md
SPONSORSHIP.md
 
 
_config.yml
_config.yml
 
 
action.yml
action.yml
 
 
entrypoint.sh
entrypoint.sh
 
 
index.md
index.md
 
 
info.md
info.md
 
 
leaders.md
leaders.md
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
tab_announcements.md
tab_announcements.md
 
 
tab_gettingstarted.md
tab_gettingstarted.md
 
 
tab_leadership.md
tab_leadership.md
 
 
View all files

## Repository files navigation

 
 
 

 
 

 
 

 

# DockSec

AI-powered Docker security scanner that explains vulnerabilities in plain English

## What is DockSec?

DockSec is anOWASP Incubator Projectthat bridges the gap between complex security scan results and actionable developer fixes. It integrates industry-standard scanners (Trivy, Hadolint, Docker Scout) with advanced AI to providecontext-aware security analysis.

Instead of overwhelming you with a list of 200+ CVEs, DockSec:

* Prioritizeswhat actually affects your specific container setup.
* Explainsvulnerabilities in plain English, not just security jargon.
* Suggestsspecific, line-by-line fixes for your Dockerfile.
* Generatesprofessional, interactive security reports for your team.

Think of it as having a security expert sitting right next to you, reviewing your Dockerfiles in real-time.

## How It Works

DockSec workflow: From scanning to actionable insights

DockSec follows a robust four-stage pipeline:

1. Scan: Runs Trivy, Hadolint, and Docker Scout locally on your environment.
2. Analyze: AI correlates findings across all scanners to remove noise and assess real-world impact.
3. Recommend: Generates human-readable explanations and specific remediation steps.
4. Report: Exports actionable results in JSON, PDF, HTML, or Markdown formats.

## Leaders

DockSec is led by a dedicated team committed to making container security accessible.

* Advait Patel- Project Lead

For questions or discussions, please join the#project-docksecchannel on OWASP Slack.

## Quick Start

### GitHub Action

Integrate DockSec into your GitHub Actions workflow:

- 
name
: 
Run DockSec AI Scanner

 
uses
: 
OWASP/DockSec@main

 
with
:
 
dockerfile
: 
'
Dockerfile
'

 
openai_api_key
: 
${{ secrets.OPENAI_API_KEY }}

### CLI Usage

#
 Install DockSec

pip install docksec

#
 Scan a Dockerfile (AI-powered)

#
 Reports will be saved to ~/.docksec/results/

docksec Dockerfile

#
 Scan Dockerfile + Docker image

docksec Dockerfile -i myapp:latest

#
 Scan only a Docker image

docksec --image-only -i myapp:latest

#
 Fast scan only (no AI)

docksec Dockerfile --scan-only

## Features

* Smart Analysis: AI explains what vulnerabilities mean foryourspecific setup.
* Multi-LLM Support: Use OpenAI, Anthropic Claude (4.x), Google Gemini (1.5+), or local models via Ollama.
* Deep Integration: Combines Trivy (vulnerabilities), Hadolint (linting), and Docker Scout.
* Security Scoring: Get a 0-100 score to track your security posture over time.
* Centralized Reporting: All reports are neatly organized in~/.docksec/results/by default.
* Rich Formats: Professional exports in HTML (interactive), PDF, JSON, and CSV.
* CI/CD Ready: Designed for easy integration into GitHub Actions and build pipelines.
* GitHub Action: Available on the GitHub Marketplace for automated security scans.

## Contributing

DockSec thrives on community contributions. Whether you are a developer, designer, or security enthusiast, there are many ways to get involved:

* Code Contributions: Fix bugs or add new features.
* Documentation: Improve guides or create tutorials.
* Issue Reporting: Identify and report bugs.
* Feedback: Share your experience and suggestions.

To get started, check out ourContributing Guidelines,Code of Conduct, andSponsorship Guide.

## Community and Social Media

* OWASP Project Page:owasp.org/DockSec/
* OWASP Slack:#project-docksec
* PyPI:pypi.org/project/docksec/
* Issues:Report a bug

If DockSec helps you, give it a ⭐ to help others discover it!

 Built with ❤️ by 
Advait Patel
 and the OWASP community.

## About

AI-powered Docker security scanner that explains vulnerabilities in plain English. An OWASP Incubator Project.

owasp.org/DockSec/

### Topics

 python

 owasp

 devsecops

 hadolint

 vulnerability-scanner

 docker-security

 ai-security

 trivy

 docksec

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

356

 stars
 

### Watchers

5

 watching
 

### Forks

69

 forks
 

 Report repository

 

## Releases11

Version 2026.5.22.3

 Latest

 

May 22, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python93.4%
* HTML5.3%
* Other1.3%