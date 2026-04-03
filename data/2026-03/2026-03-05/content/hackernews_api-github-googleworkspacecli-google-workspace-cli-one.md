---
title: 'GitHub - googleworkspace/cli: Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills. · GitHub'
url: https://github.com/googleworkspace/cli
site_name: hackernews_api
content_file: hackernews_api-github-googleworkspacecli-google-workspace-cli-one
fetched_at: '2026-03-05T11:16:03.854248'
original_url: https://github.com/googleworkspace/cli
author: gonzalovargas
date: '2026-03-05'
description: Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills. - googleworkspace/cli
tags:
- hackernews
- trending
---

googleworkspace

 

/

cli

Public

* NotificationsYou must be signed in to change notification settings
* Fork193
* Star7.1k

 
 
 
 
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

99 Commits
99 Commits
.agent
.agent
 
 
.changeset
.changeset
 
 
.github
.github
 
 
art
art
 
 
docs
docs
 
 
registry
registry
 
 
scripts
scripts
 
 
skills
skills
 
 
src
src
 
 
templates/
modelarmor
templates/
modelarmor
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTEXT.md
CONTEXT.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
demo.gif
demo.gif
 
 
dist-workspace.toml
dist-workspace.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
gemini-extension.json
gemini-extension.json
 
 
lefthook.yml
lefthook.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
View all files

## Repository files navigation

# gws

One CLI for all of Google Workspace — built for humans and AI agents.Drive, Gmail, Calendar, and every Workspace API. Zero boilerplate. Structured JSON output. 40+ agent skills included.

Note

This isnotan officially supported Google product.

npm install -g @googleworkspace/cli

gwsdoesn't ship a static list of commands. It reads Google's ownDiscovery Serviceat runtime and builds its entire command surface dynamically. When Google Workspace adds an API endpoint or method,gwspicks it up automatically.

Important

This project is under active development. Expect breaking changes as we march toward v1.0.

## Contents

* Prerequisites
* Installation
* Quick Start
* Why gws?
* Authentication
* AI Agent Skills
* MCP Server
* Advanced Usage
* Architecture
* Troubleshooting
* Development

## Prerequisites

* Node.js 18+— fornpm install(or download a pre-built binary fromGitHub Releases)
* A Google Cloud project— required for OAuth credentials. You can create one via theGoogle Cloud Consoleor with thegcloudCLIor with thegws auth setupcommand.
* A Google accountwith access to Google Workspace

## Installation

npm install -g @googleworkspace/cli

The npm package bundles pre-built native binaries for your OS and architecture.
No Rust toolchain required.

Pre-built binaries are also available on theGitHub Releasespage.

Or build from source:

cargo install --path 
.

A Nix flake is also available atgithub:googleworkspace/cli

nix run github:googleworkspace/cli

## Quick Start

gws auth setup 
#
 walks you through Google Cloud project config

gws auth login 
#
 subsequent OAuth login

gws drive files list --params 
'
{"pageSize": 5}
'

## Why gws?

For humans— stop writingcurlcalls against REST docs.gwsgives you--helpon every resource,--dry-runto preview requests, and auto‑pagination.

For AI agents— every response is structured JSON. Pair it with the included agent skills and your LLM can manage Workspace without custom tooling.

#
 List the 10 most recent files

gws drive files list --params 
'
{"pageSize": 10}
'

#
 Create a spreadsheet

gws sheets spreadsheets create --json 
'
{"properties": {"title": "Q1 Budget"}}
'

#
 Send a Chat message

gws chat spaces messages create \
 --params 
'
{"parent": "spaces/xyz"}
'
 \
 --json 
'
{"text": "Deploy complete."}
'
 \
 --dry-run

#
 Introspect any method's request/response schema

gws schema drive.files.list

#
 Stream paginated results as NDJSON

gws drive files list --params 
'
{"pageSize": 100}
'
 --page-all 
|
 jq -r 
'
.files[].name
'

## Authentication

The CLI supports multiple auth workflows so it works on your laptop, in CI, and on a server.

### Which setup should I use?

I have…

Use

gcloud
 installed and authenticated

gws auth setup
 (fastest)

A GCP project but no 
gcloud

Manual OAuth setup

An existing OAuth access token

GOOGLE_WORKSPACE_CLI_TOKEN

Existing Credentials

GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE

### Interactive (local desktop)

Credentials are encrypted at rest (AES-256-GCM) with the key stored in your OS keyring.

gws auth setup 
#
 one-time: creates a Cloud project, enables APIs, logs you in

gws auth login 
#
 subsequent scope selection and login

gws auth setuprequires thegcloudCLI. If you don't havegcloud, use themanual setupbelow instead.

Warning

Scope limits in testing mode:If your OAuth app is unverified (testing mode),
Google limits consent to ~25 scopes. Therecommendedscope preset includes 85+
scopes andwill failfor unverified apps. Choose individual service scopes instead:

gws auth login --scopes drive,gmail,calendar

### Multiple accounts

You can authenticate with more than one Google account and switch between them:

gws auth login --account work@corp.com 
#
 login and register an account

gws auth login --account personal@gmail.com

gws auth list 
#
 list registered accounts

gws auth default work@corp.com. 
#
 set the default

gws --account personal@gmail.com drive files list 
#
 one-off override

export
 GOOGLE_WORKSPACE_CLI_ACCOUNT=personal@gmail.com 
#
 env var override

Credentials are stored per-account ascredentials.<b64-email>.encin~/.config/gws/, with anaccounts.jsonregistry tracking defaults.

### Manual OAuth setup (Google Cloud Console)

Use this whengws auth setupcannot automate project/client creation, or when you want explicit control.

1. Open Google Cloud Console in the target project:* OAuth consent screen:https://console.cloud.google.com/apis/credentials/consent?project=<PROJECT_ID>
* Credentials:https://console.cloud.google.com/apis/credentials?project=<PROJECT_ID>
2. Configure OAuth branding/audience if prompted:* App type:External(testing mode is fine)
3. Add your account underTest users
4. Create an OAuth client:* Type:Desktop app
5. Download the client JSON and save it to:* ~/.config/gws/client_secret.json

Important

You must add yourself as a test user.In the OAuth consent screen, clickTest users → Add usersand enter your Google account email. Without this,
login will fail with a generic "Access blocked" error.

Then run:

gws auth login

### Browser-assisted auth (human or agent)

You can complete OAuth either manually or with browser automation.

* Human flow: rungws auth login, open the printed URL, approve scopes.
* Agent-assisted flow: the agent opens the URL, selects account, handles consent prompts, and returns control once the localhost callback succeeds.

If consent shows"Google hasn't verified this app"(testing mode), clickContinue.
If scope checkboxes appear, select required scopes (orSelect all) before continuing.

### Headless / CI (export flow)

1. Complete interactive auth on a machine with a browser.
2. Export credentials:gws authexport--unmasked>credentials.json
3. On the headless machine:exportGOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/credentials.json
gws drive files list#just works

### Service Account (server-to-server)

Point to your key file; no login needed.

export
 GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/service-account.json
gws drive files list

For Domain-Wide Delegation, add:

export
 GOOGLE_WORKSPACE_CLI_IMPERSONATED_USER=admin@example.com

### Pre-obtained Access Token

Useful when another tool (e.g.gcloud) already mints tokens for your environment.

export
 GOOGLE_WORKSPACE_CLI_TOKEN=
$(
gcloud auth print-access-token
)

### Precedence

Priority

Source

Set via

1

Access token

GOOGLE_WORKSPACE_CLI_TOKEN

2

Credentials file

GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE

3

Per-account encrypted credentials

gws auth login --account EMAIL

4

Plaintext credentials

~/.config/gws/credentials.json

Account resolution:--accountflag >GOOGLE_WORKSPACE_CLI_ACCOUNTenv var > default inaccounts.json.

Environment variables can also live in a.envfile.

## AI Agent Skills

The repo ships 100+ Agent Skills (SKILL.mdfiles) — one for every supported API, plus higher-level helpers for common workflows and 50 curated recipes for Gmail, Drive, Docs, Calendar, and Sheets. See the fullSkills Indexfor the complete list.

#
 Install all skills at once

npx skills add https://github.com/googleworkspace/cli

#
 Or pick only what you need

npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-drive
npx skills add https://github.com/googleworkspace/cli/tree/main/skills/gws-gmail

OpenClaw setup

#
 Symlink all skills (stays in sync with repo)

ln -s 
$(
pwd
)
/skills/gws-
*
 
~
/.openclaw/skills/

#
 Or copy specific skills

cp -r skills/gws-drive skills/gws-gmail 
~
/.openclaw/skills/

Thegws-sharedskill includes aninstallblock so OpenClaw auto-installs the CLI vianpmifgwsisn't on PATH.

## Gemini CLI Extension

1. Authenticate the CLI first:gws auth setup
2. Install the extension into the Gemini CLI:gemini extensions install https://github.com/googleworkspace/cli

Installing this extension gives your Gemini CLI agent direct access to allgwscommands and Google Workspace agent skills. Becausegwshandles its own authentication securely, you simply need to authenticate your terminal once prior to using the agent, and the extension will automatically inherit your credentials.

## MCP Server

gws mcpstarts aModel Context Protocolserver over stdio, exposing Google Workspace APIs as structured tools that any MCP-compatible client (Claude Desktop, Gemini CLI, VS Code, etc.) can call.

gws mcp -s drive 
#
 expose Drive tools

gws mcp -s drive,gmail,calendar 
#
 expose multiple services

gws mcp -s all 
#
 expose all services (many tools!)

Configure in your MCP client:

{
 
"mcpServers"
: {
 
"gws"
: {
 
"command"
: 
"
gws
"
,
 
"args"
: [
"
mcp
"
, 
"
-s
"
, 
"
drive,gmail,calendar
"
]
 }
 }
}

Tip

Each service adds roughly 10–80 tools. Keep the list to what you actually need
to stay under your client's tool limit (typically 50–100 tools).

Flag

Description

-s, --services <list>

Comma-separated services to expose, or 
all

-w, --workflows

Also expose workflow tools

-e, --helpers

Also expose helper tools

## Advanced Usage

### Multipart Uploads

gws drive files create --json 
'
{"name": "report.pdf"}
'
 --upload ./report.pdf

### Pagination

Flag

Description

Default

--page-all

Auto-paginate, one JSON line per page (NDJSON)

off

--page-limit <N>

Max pages to fetch

10

--page-delay <MS>

Delay between pages

100 ms

### Google Sheets — Shell Escaping

Sheets ranges use!which bash interprets as history expansion. Always wrap values insingle quotes:

#
 Read cells A1:C10 from "Sheet1"

gws sheets spreadsheets values get \
 --params 
'
{"spreadsheetId": "SPREADSHEET_ID", "range": "Sheet1!A1:C10"}
'

#
 Append rows

gws sheets spreadsheets values append \
 --params 
'
{"spreadsheetId": "ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}
'
 \
 --json 
'
{"values": [["Name", "Score"], ["Alice", 95]]}
'

### Model Armor (Response Sanitization)

IntegrateGoogle Cloud Model Armorto scan API responses for prompt injection before they reach your agent.

gws gmail users messages get --params 
'
...
'
 \
 --sanitize 
"
projects/P/locations/L/templates/T
"

Variable

Description

GOOGLE_WORKSPACE_CLI_SANITIZE_TEMPLATE

Default Model Armor template

GOOGLE_WORKSPACE_CLI_SANITIZE_MODE

warn
 (default) or 
block

## Architecture

gwsuses atwo-phase parsingstrategy:

1. Readargv[1]to identify the service (e.g.drive)
2. Fetch the service's Discovery Document (cached 24 h)
3. Build aclap::Commandtree from the document's resources and methods
4. Re-parse the remaining arguments
5. Authenticate, build the HTTP request, execute

All output — success, errors, download metadata — is structured JSON.

## Troubleshooting

### "Access blocked" or 403 during login

Your OAuth app is intesting modeand your account is not listed as a test user.

Fix:Open theOAuth consent screenin your GCP project →Test users→Add users→ enter your Google account email. Then retrygws auth login.

### "Google hasn't verified this app"

Expected when your app is in testing mode. ClickAdvanced→Go to <app name> (unsafe)to proceed. This is safe for personal use; verification is only required to publish the app to other users.

### Too many scopes / consent screen error

Unverified (testing mode) apps are limited to ~25 OAuth scopes. Therecommendedscope preset includes many scopes and will exceed this limit.

Fix:Select only the scopes you need:

gws auth login --scopes drive,gmail,calendar

### gcloudCLI not found

gws auth setuprequires thegcloudCLI to automate project creation. You have three options:

1. Install gcloudand usegclouddirectly.
2. Re-rungws auth setupwhich wrapsgcloudcalls.
3. Skipgcloudentirely — set up OAuth credentials manually in theCloud Console

### redirect_uri_mismatch

The OAuth client was not created as aDesktop apptype. In theCredentialspage, delete the existing client, create a new one with typeDesktop app, and download the new JSON.

### API not enabled —accessNotConfigured

If a required Google API is not enabled for your GCP project, you will see a
403 error with reasonaccessNotConfigured:

{
 
"error"
: {
 
"code"
: 
403
,
 
"message"
: 
"
Gmail API has not been used in project 549352339482 ...
"
,
 
"reason"
: 
"
accessNotConfigured
"
,
 
"enable_url"
: 
"
https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=549352339482
"

 }
}

gwsalso prints an actionable hint tostderr:

💡 API not enabled for your GCP project.
 Enable it at: https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=549352339482
 After enabling, wait a few seconds and retry your command.

Steps to fix:

1. Click theenable_urllink (or copy it from theenable_urlJSON field).
2. In the GCP Console, clickEnable.
3. Wait ~10 seconds, then retry yourgwscommand.

Tip

You can also rungws auth setupwhich walks you through enabling all required
APIs for your project automatically.

## Development

cargo build 
#
 dev build

cargo clippy -- -D warnings 
#
 lint

cargo 
test
 
#
 unit tests

./scripts/coverage.sh 
#
 HTML coverage report → target/llvm-cov/html/

## License

Apache-2.0

## Disclaimer

Caution

This isnotan officially supported Google product.

## About

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

developers.google.com/workspace

### Topics

 rust

 cli

 automation

 oauth2

 google-drive

 google-sheets

 google-calendar

 google-docs

 google-api

 google-chat

 google-workspace

 google-admin

 ai-agent

 discovery-api

 agent-skills

 gemini-cli-extension

### Resources

 Readme

 

### License

 Apache-2.0 license
 

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

7.1k

 stars
 

### Watchers

14

 watching
 

### Forks

193

 forks
 

 Report repository

 

## Releases15

0.4.4

 Latest

 

Mar 5, 2026

 

+ 14 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.3%
* Other0.7%