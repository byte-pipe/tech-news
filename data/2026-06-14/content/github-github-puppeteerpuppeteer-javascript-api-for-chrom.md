---
title: 'GitHub - puppeteer/puppeteer: JavaScript API for Chrome and Firefox · GitHub'
url: https://github.com/puppeteer/puppeteer
site_name: github
content_file: github-github-puppeteerpuppeteer-javascript-api-for-chrom
fetched_at: '2026-06-14T11:44:10.388005'
original_url: https://github.com/puppeteer/puppeteer
author: puppeteer
description: JavaScript API for Chrome and Firefox. Contribute to puppeteer/puppeteer development by creating an account on GitHub.
---

puppeteer

 

/

puppeteer

Public

* NotificationsYou must be signed in to change notification settings
* Fork9.4k
* Star94.6k

 
 
 
 
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

6,344 Commits
6,344 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
test-d
test-d
 
 
test
test
 
 
tools
tools
 
 
website
website
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mocharc.cjs
.mocharc.cjs
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Herebyfile.mjs
Herebyfile.mjs
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
eslint.config.mjs
eslint.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
prettier.config.js
prettier.config.js
 
 
puppeteer.config.js
puppeteer.config.js
 
 
release-please-config.json
release-please-config.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsdoc.json
tsdoc.json
 
 
versions.json
versions.json
 
 
View all files

## Repository files navigation

# Puppeteer

Puppeteer is a JavaScript library which provides a high-level API to control
Chrome or Firefox over theDevTools ProtocolorWebDriver BiDi.
Puppeteer runs in the headless (no visible UI) by default

## Get started|API|FAQ|Contributing|Troubleshooting

## Installation

npm i puppeteer 
#
 Downloads compatible Chrome during installation.

npm i puppeteer-core 
#
 Alternatively, install as a library, without downloading Chrome.

:::note

Modern package managers (including npm (see theRFC), pnpm, Yarn, Bun, and Deno) block dependency install scripts by default. If the install script is blocked, Puppeteer will not download the browser during installation, leading to runtime errors.

You can manually download the required browsers after installation by running:

npx puppeteer browsers install

Alternatively, you can configure your package manager to allow the install script to run (for example, with npm, by adding"puppeteer"to"allowScripts"in yourpackage.json).

:::

## MCP

Installchrome-devtools-mcp,
a Puppeteer-based MCP server for browser automation and debugging.

Puppeteer also supports the experimentalWebMCPAPI.

## Example

import
 
puppeteer
 
from
 
'puppeteer'
;

// Or import puppeteer from 'puppeteer-core';

// Launch the browser and open a new blank page.

const
 
browser
 
=
 
await
 
puppeteer
.
launch
(
)
;

const
 
page
 
=
 
await
 
browser
.
newPage
(
)
;

// Navigate the page to a URL.

await
 
page
.
goto
(
'https://developer.chrome.com/'
)
;

// Set the screen size.

await
 
page
.
setViewport
(
{
width
: 
1080
,
 
height
: 
1024
}
)
;

// Open the search menu using the keyboard.

await
 
page
.
keyboard
.
press
(
'/'
)
;

// Type into search box using accessible input name.

await
 
page
.
locator
(
'::-p-aria(Search)'
)
.
fill
(
'automate beyond recorder'
)
;

// Wait and click on first result.

await
 
page
.
locator
(
'.devsite-result-item-link'
)
.
click
(
)
;

// Locate the full title with a unique string.

const
 
textSelector
 
=
 
await
 
page

 
.
locator
(
'::-p-text(Customize and automate)'
)

 
.
waitHandle
(
)
;

const
 
fullTitle
 
=
 
await
 
textSelector
?.
evaluate
(
el
 
=>
 
el
.
textContent
)
;

// Print the full title.

console
.
log
(
'The title of this blog post is "%s".'
,
 
fullTitle
)
;

await
 
browser
.
close
(
)
;

## About

JavaScript API for Chrome and Firefox

pptr.dev

### Topics

 testing

 firefox

 chrome

 automation

 web

 chromium

 developer-tools

 node-module

 headless-chrome

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

94.6k

 stars
 

### Watchers

1.2k

 watching
 

### Forks

9.4k

 forks
 

 Report repository

 

## Releases680

browsers: v3.0.4

 Latest

 

May 26, 2026

 

+ 679 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript93.8%
* JavaScript4.8%
* HTML1.1%
* CSS0.2%
* Dockerfile0.1%
* Shell0.0%