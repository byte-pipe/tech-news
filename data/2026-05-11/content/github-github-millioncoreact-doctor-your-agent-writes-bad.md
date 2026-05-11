---
title: 'GitHub - millionco/react-doctor: Your agent writes bad React. This catches it · GitHub'
url: https://github.com/millionco/react-doctor
site_name: github
content_file: github-github-millioncoreact-doctor-your-agent-writes-bad
fetched_at: '2026-05-11T13:46:43.672555'
original_url: https://github.com/millionco/react-doctor
author: millionco
description: Your agent writes bad React. This catches it. Contribute to millionco/react-doctor development by creating an account on GitHub.
---

millionco

 

/

react-doctor

Public

* NotificationsYou must be signed in to change notification settings
* Fork242
* Star7.7k

 
 
 
Use this GitHub action with your project
Add this Action to an existing workflow or create a new one
View on Marketplace
 
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

276 Commits
276 Commits
.agents/
skills
.agents/
skills
 
 
.changeset
.changeset
 
 
.github
.github
 
 
assets
assets
 
 
packages
packages
 
 
scripts
scripts
 
 
skills/
react-doctor
skills/
react-doctor
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
action.yml
action.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

Your agent writes bad React, this catches it.

One command scans your codebase and outputs a0 to 100 health scorewith actionable diagnostics.

Works with Next.js, Vite, and React Native.

### See it in action →

## Install

Run this at your project root:

npx -y react-doctor@latest 
.

You'll get a score (75+ Great, 50 to 74 Needs work, under 50 Critical) and a list of issues across state & effects, performance, architecture, security, accessibility, and dead code. Rules toggle automatically based on your framework and React version.

Main.mp4

## Install for your coding agent

Teach your coding agent React best practices so it stops writing the bad code in the first place.

npx -y react-doctor@latest install

You'll be prompted to pick which detected agents to install for. Pass--yesto skip prompts.

Works with Claude Code, Cursor, Codex, OpenCode, and 50+ other agents.

## GitHub Actions

A composite action ships with this repository. Drop it into.github/workflows/react-doctor.yml:

name
: 
React Doctor

on
:
 
pull_request
:
 
push
:
 
branches
: 
[main]

permissions
:
 
contents
: 
read

 
pull-requests
: 
write 
#
 required to post PR comments

jobs
:
 
react-doctor
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
uses
: 
actions/checkout@v5

 
with
:
 
fetch-depth
: 
0
 
#
 required for `diff`

 - 
uses
: 
millionco/react-doctor@main

 
with
:
 
diff
: 
main

 
github-token
: 
${{ secrets.GITHUB_TOKEN }}

Whengithub-tokenis set onpull_requestevents, findings are posted (and updated) as a PR comment. The action also exposes ascoreoutput (0–100) you can use in subsequent steps.

Inputs:directory,verbose,project,diff,github-token,fail-on(error/warning/none),offline,node-version. Seeaction.ymlfor full descriptions.

Prefer not to add a marketplace action? The barenpxform works too:

- 
run
: 
npx -y react-doctor@latest --fail-on warning

## Configuration

Create areact-doctor.config.jsonin your project root:

{
 
"ignore"
: {
 
"rules"
: [
"
react/no-danger
"
, 
"
jsx-a11y/no-autofocus
"
],
 
"files"
: [
"
src/generated/**
"
],
 
"overrides"
: [
 {
 
"files"
: [
"
components/modules/diff/**
"
],
 
"rules"
: [
"
react-doctor/no-array-index-as-key
"
, 
"
react-doctor/no-render-in-render
"
]
 },
 {
 
"files"
: [
"
components/search/HighlightedSnippet.tsx
"
],
 
"rules"
: [
"
react/no-danger
"
]
 }
 ]
 }
}

Three nested keys, three layers of granularity — pick the narrowest one that fits:

* ignore.rulessilences a rule across the whole codebase.
* ignore.filessilenceseveryrule on the matched files (use sparingly — it loses coverage for unrelated rules).
* ignore.overridessilences only the listed rules on the matched files, leaving every other rule active. This is what you want when a single file (or glob) legitimately needs an exemption from one or two rules but should still be scanned for everything else.

You can also use the"reactDoctor"key inpackage.json. CLI flags always override config values.

React Doctor respects.gitignore,.eslintignore,.oxlintignore,.prettierignore, andlinguist-vendored/linguist-generatedannotations in.gitattributes. Inline// eslint-disable*and// oxlint-disable*comments are honored too.

If you have a JSON oxlint or eslint config (.oxlintrc.jsonor.eslintrc.json), its rules get merged into the scan automatically and count toward the score. SetadoptExistingLintConfig: falseto opt out.

#### Optional companion plugins

When the following ESLint plugins are installed in the scanned project (or hoisted in your monorepo), React Doctor folds their rules into the same scan. Both are listed asoptional peer dependencies— install only what you want.

Plugin

Adds

Namespace

eslint-plugin-react-hooks
 (v6 or v7)

The React Compiler frontend's correctness rules — fired when a React Compiler is detected in the project.

react-hooks-js/*

eslint-plugin-react-you-might-not-need-an-effect
 (v0.10+)

Complementary effects-as-anti-pattern rules (
no-derived-state
, 
no-chain-state-updates
, 
no-event-handler
, 
no-pass-data-to-parent
, …) that run alongside React Doctor's native State & Effects rules.

effect/*

### Inline suppressions

// react-doctor-disable-next-line react-doctor/no-cascading-set-state

useEffect
(
(
)
 
=>
 
{

 
setA
(
value
)
;

 
setB
(
value
)
;

}
,
 
[
value
]
)
;

When two rules fire on the same line, you have two equivalent options. Comma-separate the rule ids on a single comment:

// react-doctor-disable-next-line react-doctor/rerender-state-only-in-handlers, react-doctor/no-derived-useState

const
 
[
localSearch
,
 
setLocalSearch
]
 
=
 
useState
(
searchQuery
)
;

Or stack one comment per rule directly above the diagnostic. Stacked comments are honored as long as nothing but otherreact-doctor-disable-next-linecomments sits between them and the target line:

// react-doctor-disable-next-line react-doctor/rerender-state-only-in-handlers

// react-doctor-disable-next-line react-doctor/no-derived-useState

const
 
[
localSearch
,
 
setLocalSearch
]
 
=
 
useState
(
searchQuery
)
;

A code line between stacked comments breaks the chain: only the comment immediately above the diagnostic (and any contiguousreact-doctor-disable-next-linecomments stacked on top of it) is honored. If a comment looks adjacent but the rule still fires, runreact-doctor --explain <file:line>— it reports whether a nearby suppression was found, what rules it covers, and why it didn't apply.

Block comments work inside JSX:

{
/* react-doctor-disable-next-line react/no-danger */
}

<
div
 
dangerouslySetInnerHTML
=
{
{
 __html 
}
}
 
/>

For multi-line JSX, putting the comment immediately above the opening tag covers the entire attribute list (matching ESLint convention).

## Lint plugin (standalone)

The same rule set ships as both an oxlint plugin and an ESLint plugin, so you can wire it into whichever lint engine your project already runs.

oxlintin.oxlintrc.json:

ESLintflat config:

import
 
reactDoctor
 
from
 
"react-doctor/eslint-plugin"
;

export
 
default
 
[

 
reactDoctor
.
configs
.
recommended
,

 
reactDoctor
.
configs
.
next
,

 
reactDoctor
.
configs
[
"react-native"
]
,

 
reactDoctor
.
configs
[
"tanstack-start"
]
,

 
reactDoctor
.
configs
[
"tanstack-query"
]
,

]
;

The full rule list lives inoxlint-config.ts.

## CLI reference

Usage: react-doctor [directory] [options]

Options:
 -v, --version display the version number
 --no-lint skip linting
 --no-dead-code skip dead code detection
 --verbose show every rule and per-file details (default shows top 3 rules)
 --score output only the score
 --json output a single structured JSON report
 -y, --yes skip prompts, scan all workspace projects
 --full skip prompts, always run a full scan
 --project <name> select workspace project (comma-separated for multiple)
 --diff [base] scan only files changed vs base branch
 --staged scan only staged files (for pre-commit hooks)
 --offline skip telemetry
 --fail-on <level> exit with error on diagnostics: error, warning, none
 --annotations output diagnostics as GitHub Actions annotations
 --explain <file:line> diagnose why a rule fired or why a suppression didn't apply
 --why <file:line> alias for --explain
 -h, --help display help

When a suppression isn't working,--explain <file:line>(or its alias--why <file:line>) reports what the scanner sees at that location, including why a nearbyreact-doctor-disable-next-linedidn't apply. The diagnosis distinguishes the common failure modes — adjacent comment for a different rule (use the comma form), a code line between the comment and the diagnostic (the chain is broken), or no nearby suppression at all. The same hint surfaces inline with--verbosefor every flagged site, and in--jsonoutput asdiagnostic.suppressionHint, so a single scan doubles as a suppression audit without a separate flag.

--jsonproduces a parsable object on stdout with all human-readable output suppressed. Errors still produce a JSON object withok: false, so stdout is always a valid document.

### Config keys

Key

Type

Default

ignore.rules

string[]

[]

ignore.files

string[]

[]

ignore.overrides

{ files, rules? }[]

[]

lint

boolean

true

deadCode

boolean

true

verbose

boolean

false

diff

boolean | string

failOn

"error" | "warning" | "none"

"none"

customRulesOnly

boolean

false

share

boolean

true

textComponents

string[]

[]

rawTextWrapperComponents

string[]

[]

respectInlineDisables

boolean

true

adoptExistingLintConfig

boolean

true

textComponentsis the broad escape hatch forrn-no-raw-text— list components that themselves behave like React Native's<Text>(customTypography,NativeTabs.Trigger.Label, etc.) and the rule will treat them as text containers regardless of what their children look like.

rawTextWrapperComponentsis the narrower option for components that are not text elements but safely route string-only children through an internal<Text>(e.g.heroui-native'sButton, which stringifies its children and renders them through aButtonLabel). Listed wrappers suppressrn-no-raw-textonly when their children are entirely stringifiable. A wrapper with mixed children — e.g.<Button>Save<Icon /></Button>— still reports because the wrapper can't safely route raw text alongside a sibling JSX element.

## Node.js API

import
 
{
 
diagnose
,
 
toJsonReport
,
 
summarizeDiagnostics
 
}
 
from
 
"react-doctor/api"
;

const
 
result
 
=
 
await
 
diagnose
(
"./path/to/your/react-project"
)
;

console
.
log
(
result
.
score
)
;
 
// { score: 82, label: "Great" } or null

console
.
log
(
result
.
diagnostics
)
;
 
// Diagnostic[]

console
.
log
(
result
.
project
)
;
 
// detected framework, React version, etc.

diagnoseaccepts a second argument:{ lint?: boolean, deadCode?: boolean }.

const
 
report
 
=
 
toJsonReport
(
result
,
 
{
 
version
: 
"1.0.0"
 
}
)
;

const
 
counts
 
=
 
summarizeDiagnostics
(
result
.
diagnostics
)
;

react-doctor/apire-exportsJsonReport,JsonReportSummary,JsonReportProjectEntry,JsonReportMode, plus the lower-levelbuildJsonReportandbuildJsonReportErrorbuilders. Seepackages/react-doctor/src/api.tsfor the full types.

## Leaderboard

Top React codebases scanned by React Doctor, ranked by score. Updated automatically frommillionco/react-doctor-benchmarks.

#

Repo

Score

1

executor

94

2

nodejs.org

86

3

tldraw

70

4

t3code

68

5

better-auth

64

6

excalidraw

63

7

mastra

63

8

payload

60

9

typebot

57

10

plane

56

See thefull leaderboard.

## Resources & Contributing Back

Want to try it out? Check outthe demo.

Looking to contribute back? Clone the repo, install, build, and submit a PR.

git clone https://github.com/millionco/react-doctor

cd
 react-doctor
pnpm install
pnpm build
node packages/react-doctor/bin/react-doctor.js /path/to/your/react-project

Find a bug? Head to theissue tracker.

### License

React Doctor is MIT-licensed open-source software.

## About

Your agent writes bad React. This catches it

react.doctor

### Topics

 react

 doctor

 skill

 code-review

 agents

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

7.7k

 stars
 

### Watchers

12

 watching
 

### Forks

242

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript100.0%