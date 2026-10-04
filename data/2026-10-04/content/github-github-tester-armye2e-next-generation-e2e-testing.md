---
title: 'GitHub - tester-army/e2e: Next generation e2e testing framework for web and mobile apps. · GitHub'
url: https://github.com/tester-army/e2e
site_name: github
content_file: github-github-tester-armye2e-next-generation-e2e-testing
fetched_at: '2026-10-04T15:40:33.072512'
original_url: https://github.com/tester-army/e2e
author: tester-army
description: Next generation e2e testing framework for web and mobile apps. - tester-army/e2e
---

tester-army

 

/

e2e

Public

* NotificationsYou must be signed in to change notification settings
* Fork102
* Star2.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

607 Commits
607 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.changeset
.changeset
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
apps
apps
 
 
docs
docs
 
 
packages
packages
 
 
scripts
scripts
 
 
skills/
e2e
skills/
e2e
 
 
.fallowrc.json
.fallowrc.json
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
skills-lock.json
skills-lock.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
View all files

## Repository files navigation

# e2e

e2eis an end-to-end testing framework for web and mobile apps. Describe a goal in natural language and an agent drives the app to reach it. Check the result with locators and assertions in the same test.

// tests/checkout.e2e.ts

import
 
{
 
test
,
 
expect
 
}
 
from
 
'e2e'
;

test
(
'a member upgrades to Pro'
,
 
async
 
(
{
 app
,
 agent
,
 screen 
}
)
 
=>
 
{

 
await
 
app
.
open
(
'/settings/billing'
)
;

 
await
 
agent
.
act
(
'upgrade the workspace to the Pro plan'
)
;

 
await
 
agent
.
assert
(
'the invoice preview shows a prorated amount'
)
;

 
await
 
expect
(
screen
.
getByRole
(
'status'
)
)
.
toContainText
(
'Pro'
)
;

}
)
;

An agent step that a later assertion verifies records its actions, and the
next run replays them with no model calls until the app changes. Tests
without agent steps need no model. Bring your own subscription, API key, or
local model.

## Quick start

npx e2e init

initasks for an engine, web or mobile, and a model provider, then writes a
config and an example test. Thequickstartcovers the rest.

## Packages

Package

What it does

e2e

The SDK, runner, and CLI.

@e2e-dev/web

Browser engine: Chromium, Firefox, and WebKit through Playwright.

@e2e-dev/mobile

iOS and Android engine: simulators and emulators through agent-device.

@e2e-dev/github

Reporter that posts results as a pull request comment.

@e2e-dev/kernel

Kernel hosted browsers for the web engine.

@e2e-dev/eas

EAS Simulators hosted iOS simulators and Android emulators for the mobile engine.

@e2e-dev/decision

Decision-model executors for bounded semantic actions and assertions.

## Documentation

e2e.tester.army/docs. Thee2epackage ships
every page, so coding agents can read them offline innode_modules/e2e/docs.

## Contributing

SeeCONTRIBUTING.md. Questions go toDiscord.

## Security

Please don't open public issues for security vulnerabilities. FollowSECURITY.mdand report them tosecurity@tester.army.

## Telemetry

The CLI sends anonymous usage data, such as which commands and engines run and
where runs fail, but no test content, app content, or credentials. Opt out withnpx e2e telemetry disableorE2E_TELEMETRY_DISABLED=1.Telemetrylists every field.

## Status

Note

e2e is in active development on the way to 1.0. APIs and config can still
change between minor releases.

## Made by TesterArmy

e2e is built byTesterArmy,
the agentic testing platform that runs natural language tests on web and mobile
apps, on every pull request or on a schedule.

Apache-2.0.