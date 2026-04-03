---
title: 'GitHub - usestrix/strix: Open-source AI hackers to find and fix your app’s vulnerabilities. · GitHub'
url: https://github.com/usestrix/strix
site_name: github
content_file: github-github-usestrixstrix-open-source-ai-hackers-to-fin
fetched_at: '2026-03-25T11:19:46.160186'
original_url: https://github.com/usestrix/strix
author: usestrix
description: Open-source AI hackers to find and fix your app’s vulnerabilities. - usestrix/strix
---

usestrix

 

/

strix

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.3k
* Star21.4k

 
 
 
 
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

346 Commits
346 Commits
.github
.github
 
 
benchmarks
benchmarks
 
 
containers
containers
 
 
docs
docs
 
 
scripts
scripts
 
 
strix
strix
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
poetry.lock
poetry.lock
 
 
pyproject.toml
pyproject.toml
 
 
strix.spec
strix.spec
 
 
View all files

## Repository files navigation

# Strix

### Open-source AI hackers to find and fix your app’s vulnerabilities.

Tip

New!Strix integrates seamlessly with GitHub Actions and CI/CD pipelines. Automatically scan for vulnerabilities on every pull request and block insecure code before it reaches production!

## Strix Overview

Strix are autonomous AI agents that act just like real hackers - they run your code dynamically, find vulnerabilities, and validate them through actual proof-of-concepts. Built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting or the false positives of static analysis tools.

Key Capabilities:

* Full hacker toolkitout of the box
* Teams of agentsthat collaborate and scale
* Real validationwith PoCs, not false positives
* Developer‑firstCLI with actionable reports
* Auto‑fix & reportingto accelerate remediation

## Use Cases

* Application Security Testing- Detect and validate critical vulnerabilities in your applications
* Rapid Penetration Testing- Get penetration tests done in hours, not weeks, with compliance reports
* Bug Bounty Automation- Automate bug bounty research and generate PoCs for faster reporting
* CI/CD Integration- Run tests in CI/CD to block vulnerabilities before reaching production

## 🚀 Quick Start

Prerequisites:

* Docker (running)
* An LLM API key from anysupported provider(OpenAI, Anthropic, Google, etc.)

### Installation & First Scan

#
 Install Strix

curl -sSL https://strix.ai/install 
|
 bash

#
 Configure your AI provider

export
 STRIX_LLM=
"
openai/gpt-5.4
"

export
 LLM_API_KEY=
"
your-api-key
"

#
 Run your first security assessment

strix --target ./app-directory

Note

First run automatically pulls the sandbox Docker image. Results are saved tostrix_runs/<run-name>

## ☁️ Strix Platform

Try the Strix full-stack security platform atapp.strix.ai— sign up for free, connect your repos and domains, and launch a pentest in minutes.

* Validated findings with PoCsand reproduction steps
* One-click autofixas ready-to-merge pull requests
* Continuous monitoringacross code, cloud, and infrastructure
* Integrationswith GitHub, Slack, Jira, Linear, and CI/CD pipelines
* Continuous learningthat builds on past findings and remediations

Start your first pentest →

## ✨ Features

### Agentic Security Tools

Strix agents come equipped with a comprehensive security testing toolkit:

* Full HTTP Proxy- Full request/response manipulation and analysis
* Browser Automation- Multi-tab browser for testing of XSS, CSRF, auth flows
* Terminal Environments- Interactive shells for command execution and testing
* Python Runtime- Custom exploit development and validation
* Reconnaissance- Automated OSINT and attack surface mapping
* Code Analysis- Static and dynamic analysis capabilities
* Knowledge Management- Structured findings and attack documentation

### Comprehensive Vulnerability Detection

Strix can identify and validate a wide range of security vulnerabilities:

* Access Control- IDOR, privilege escalation, auth bypass
* Injection Attacks- SQL, NoSQL, command injection
* Server-Side- SSRF, XXE, deserialization flaws
* Client-Side- XSS, prototype pollution, DOM vulnerabilities
* Business Logic- Race conditions, workflow manipulation
* Authentication- JWT vulnerabilities, session management
* Infrastructure- Misconfigurations, exposed services

### Graph of Agents

Advanced multi-agent orchestration for comprehensive security testing:

* Distributed Workflows- Specialized agents for different attacks and assets
* Scalable Testing- Parallel execution for fast comprehensive coverage
* Dynamic Coordination- Agents collaborate and share discoveries

## Usage Examples

### Basic Usage

#
 Scan a local codebase

strix --target ./app-directory

#
 Security review of a GitHub repository

strix --target https://github.com/org/repo

#
 Black-box web application assessment

strix --target https://your-app.com

### Advanced Testing Scenarios

#
 Grey-box authenticated testing

strix --target https://your-app.com --instruction 
"
Perform authenticated testing using credentials: user:pass
"

#
 Multi-target testing (source code + deployed app)

strix -t https://github.com/org/app -t https://your-app.com

#
 Focused testing with custom instructions

strix --target api.your-app.com --instruction 
"
Focus on business logic flaws and IDOR vulnerabilities
"

#
 Provide detailed instructions through file (e.g., rules of engagement, scope, exclusions)

strix --target api.your-app.com --instruction-file ./instruction.md

### Headless Mode

Run Strix programmatically without interactive UI using the-n/--non-interactiveflag—perfect for servers and automated jobs. The CLI prints real-time vulnerability findings, and the final report before exiting. Exits with non-zero code when vulnerabilities are found.

strix -n --target https://your-app.com

### CI/CD (GitHub Actions)

Strix can be added to your pipeline to run a security test on pull requests with a lightweight GitHub Actions workflow:

name
: 
strix-penetration-test

on
:
 
pull_request
:

jobs
:
 
security-scan
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v6

 - 
name
: 
Install Strix

 
run
: 
curl -sSL https://strix.ai/install | bash

 - 
name
: 
Run Strix

 
env
:
 
STRIX_LLM
: 
${{ secrets.STRIX_LLM }}

 
LLM_API_KEY
: 
${{ secrets.LLM_API_KEY }}

 
run
: 
strix -n -t ./ --scan-mode quick

### Configuration

export
 STRIX_LLM=
"
openai/gpt-5.4
"

export
 LLM_API_KEY=
"
your-api-key
"

#
 Optional

export
 LLM_API_BASE=
"
your-api-base-url
"
 
#
 if using a local model, e.g. Ollama, LMStudio

export
 PERPLEXITY_API_KEY=
"
your-api-key
"
 
#
 for search capabilities

export
 STRIX_REASONING_EFFORT=
"
high
"
 
#
 control thinking effort (default: high, quick scan: medium)

Note

Strix automatically saves your configuration to~/.strix/cli-config.json, so you don't have to re-enter it on every run.

Recommended models for best results:

* OpenAI GPT-5.4—openai/gpt-5.4
* Anthropic Claude Sonnet 4.6—anthropic/claude-sonnet-4-6
* Google Gemini 3 Pro Preview—vertex_ai/gemini-3-pro-preview

See theLLM Providers documentationfor all supported providers including Vertex AI, Bedrock, Azure, and local models.

## Enterprise

Get the same Strix experience withenterprise-gradecontrols: SSO (SAML/OIDC), custom compliance reports, dedicated support & SLA, custom deployment options (VPC/self-hosted), BYOK model support, and tailored agents optimized for your environment.Learn more.

## Documentation

Full documentation is available atdocs.strix.ai— including detailed guides for usage, CI/CD integrations, skills, and advanced configuration.

## Contributing

We welcome contributions of code, docs, and new skills - check out ourContributing Guideto get started or open apull request/issue.

## Join Our Community

Have questions? Found a bug? Want to contribute?Join our Discord!

## Support the Project

Love Strix?Give us a ⭐ on GitHub!

## Acknowledgements

Strix builds on the incredible work of open-source projects likeLiteLLM,Caido,Nuclei,Playwright, andTextual. Huge thanks to their maintainers!

Warning

Only test apps you own or have permission to test. You are responsible for using Strix ethically and legally.

## About

Open-source AI hackers to find and fix your app’s vulnerabilities.

strix.ai

### Topics

 artificial-intelligence

 cybersecurity

 penetration-testing

 agents

 llm

 generative-ai

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

21.4k

 stars
 

### Watchers

115

 watching
 

### Forks

2.3k

 forks
 

 Report repository

 

## Releases11

v0.8.3

 Latest

 

Mar 23, 2026

 

+ 10 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python91.3%
* Jinja4.4%
* Shell2.9%
* Other1.4%