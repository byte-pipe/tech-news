---
title: 'GitHub - openai/codex-security: SDKs and CLI for Codex Security · GitHub'
url: https://github.com/openai/codex-security
site_name: hackernews_api
content_file: hackernews_api-github-openaicodex-security-sdks-and-cli-for-codex
fetched_at: '2026-07-29T12:28:25.134586'
original_url: https://github.com/openai/codex-security
author: bakigul
date: '2026-07-29'
description: SDKs and CLI for Codex Security. Contribute to openai/codex-security development by creating an account on GitHub.
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 openai

 

/

codex-security

Public

* NotificationsYou must be signed in to change notification settings
* Fork95
* Star1.7k

 
 
 
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

111 Commits
111 Commits
.github/
workflows
.github/
workflows
 
 
docker
docker
 
 
sdk/
typescript
sdk/
typescript
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
compose.yaml
compose.yaml
 
 
View all files

## Repository files navigation

# Codex Security

@openai/codex-securityis a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. Scan repositories, review changes, track findings over time, and run security checks in CI.

Documentation

## Quick start

Requires Node.js 22 or later, Python 3.10 or later, and access to Codex Security.

npm install @openai/codex-security
npx codex-security login
npx codex-security scan 
.

For CI, setOPENAI_API_KEYinstead of signing in.

If both a ChatGPT sign-in and an API key are available, interactive scans ask
which credential to use. CI and other noninteractive scans keep the existing
API-key precedence. Select a credential explicitly when needed:

npx codex-security scan 
.
 --auth chatgpt
npx codex-security scan 
.
 --auth api-key

To make your ChatGPT sign-in the automatic default, unset any configured API
keys:

unset
 OPENAI_API_KEY CODEX_API_KEY

Scan history is stored in the Codex Security workbench state directory. If that
directory cannot be written, setCODEX_SECURITY_STATE_DIRto a writable
directory outside the repository.

## TypeScript SDK

import
 
{
 
CodexSecurity
 
}
 
from
 
"@openai/codex-security"
;

const
 
security
 
=
 
new
 
CodexSecurity
(
)
;

const
 
result
 
=
 
await
 
security
.
run
(
"."
)
;

console
.
log
(
result
.
reportPath
)
;

await
 
security
.
close
(
)
;

For installation, authentication, scan options, and CI setup, see theofficial documentation.