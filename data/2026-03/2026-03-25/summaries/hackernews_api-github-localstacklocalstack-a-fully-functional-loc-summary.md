---
title: GitHub - localstack/localstack: 💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline · GitHub
url: https://github.com/localstack/localstack
date: 2026-03-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-25T01:03:34.897222
---

# GitHub - localstack/localstack: 💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline · GitHub

# LocalStack Repository (archived)

## Overview
- Cloud service emulator that lets you develop and test AWS applications locally without connecting to the real cloud.
- Runs in a single Docker container; works on laptops and CI environments.
- Supports many AWS services such as Lambda, S3, DynamoDB, Kinesis, SQS, SNS, etc.; the Pro version adds extra APIs and advanced features.
- Full list of supported APIs is available on the Feature Coverage page.

## Archive Notice
- The repository was archived by the owner on Mar 23 2026 and is now read‑only.
- Development has been consolidated into a single, unified LocalStack image to reduce fragmentation and focus resources.
- Users are encouraged to use **LocalStack for AWS** (free Hobby plan for non‑commercial use) and continue submitting bug reports, feature requests, and joining the Slack community.

## Installation
- The recommended entry point is the LocalStack CLI, which requires a functional Docker environment.
- **Homebrew (macOS/Linux)**: `brew install localstack/tap/localstack-cli`
- **Binary download**: download the latest release from the GitHub releases page, extract the archive, and place the binary in a directory on your `PATH`.
- **PyPI**: `python3 -m pip install localstack`
- Run everything as a non‑root user; avoid using `sudo` or running as the root user.

## Quickstart
1. Start LocalStack in Docker mode: `localstack start -d`
2. Check which services are available: `localstack status services`
3. Example – create an SQS queue:
   `awslocal sqs create-queue --queue-name sample-queue`

## Running Options
- LocalStack CLI
- Docker
- Docker Compose
- Helm

## Usage Resources
- Documentation includes configuration guides, CI integration, tool integrations, FAQs, and more.
- Graphical interfaces are available via the LocalStack Web Application, Desktop client, and Docker Extension.

## Releases
- All release notes and change logs are published in the GitHub releases section and the project changelog file.

## Contributing
- Read the contributing guide and development environment setup instructions.
- Explore the codebase, open issues, and submit pull requests.
- Contributions and feedback are appreciated.

## Community & Support
- Join the LocalStack Slack Community.
- Use the GitHub issue tracker for bug reports, feature requests, and support questions.

## Acknowledgements
- Thanks to all contributors and backers who have helped build and maintain the project.
