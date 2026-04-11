---
title: 'GitHub - callumlocke/json-formatter: Makes JSON easy to read. · GitHub'
url: https://github.com/callumlocke/json-formatter
site_name: hnrss
content_file: hnrss-github-callumlockejson-formatter-makes-json-easy-t
fetched_at: '2026-04-11T11:13:00.937367'
original_url: https://github.com/callumlocke/json-formatter
date: '2026-04-10'
description: Makes JSON easy to read. Contribute to callumlocke/json-formatter development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

callumlocke

 

/

json-formatter

Public

* NotificationsYou must be signed in to change notification settings
* Fork960
* Star4.1k

 
 
 
 
master
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

86 Commits
86 Commits
.vscode
.vscode
 
 
ext
ext
 
 
lib
lib
 
 
samples
samples
 
 
task
task
 
 
.gitignore
.gitignore
 
 
.prettierrc.yml
.prettierrc.yml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# ARCHIVED

I am no longer developing JSON Formatter as an open source project. I'm moving to a closed-source, commercial model in order to build a more comprehensive API-browsing tool with premium features.

I know some users (especially here on GitHub) will always prefer open source tools, so I’m leaving this repo online for others to use/fork, and I’ve published the final open source version asJSON Formatter Classic– you can switch to that if you just want a simple, open source, local-only JSON-formatting extension that won't receive updates.

# JSON Formatter

Chrome extension that helps you view and explore JSON API responses.

## Features

* Fast, even on very long JSON pages
* Dark mode
* Syntax highlighting
* Collapsible trees, with indent guides
* Clickable URLs
* Negligible performance impact on non-JSON pages (less than 1 millisecond)
* Works on any valid JSON page – URL doesn't matter
* Buttons for toggling between raw and parsed JSON
* Parsed JSON is exported as a global variable,json, so you can inspect it in the console (now working again!)

## Installation

Option 1– InstallJSON Formatter Classicfrom the Chrome Web Store.

Option 2– Install it from source (see below).

### Development

Clone repo and runbun install.

Commands:

* bun run build- single build
* bun run watch- same but watch-driven

You can installdistas a local, unpacked extension in Chrome with developer mode enabled.

## FAQ

### How does it detect JSON?

This turns out to be a complex thing to get right in a bulletproof way. In most cases it's based on theContent-Typeheader but in some cases it's necessary to inspect the 'page' strucure and see if it looks like a JSON endpoint. This is designed to work as fast as possible with no perceivable impact on browsing.

### Why are large numbers not displayed accurately?

This is alimitation of JavaScriptand therefore a limitation of JSON as interpreted by your web browser.

* Anything overNumber.MAX_SAFE_INTEGER(2^53 - 1or9007199254740991) is adjusted down to that number.
* Anything belowNumber.MIN_SAFE_INTEGER(-2^53 + 1or-9007199254740991) is adjusted up to that number.
* Extremely precise floating point numbers are rounded to 16 digits.

It's not JSON Formatter doing this, it's the nativeJSON.parsein V8. JSON Formatter shows you theparsedvalues, exactly the same as what you'll see if you fetch your JSON from any web application.

If your API endpoint really needs to represent numbers outside JavaScript's safe range, it shouldquote them as strings.

### Why are object keys sometimes in the wrong order?

What you see in JSON Formatter is a representation of theparsedobject/array. It's the same order you'll get withObject.keys( JSON.parse(json) )in JavaScript.

Historically, the JavaScript standard explicitly stated that object keys can be iterated in any order, and V8 took advantage of this by moving numeric string keys (like"1"or"99999") to the top to facilitate a small performance optimisation. This V8 implementation detail has since become standardised.

##### But I just want to see exactly what the server spits out

For now, your best option is to just use the "Raw" button to see the raw JSON. This is what the server sent. The "Parsed" buttons represents what you'll get fromJSON.parse.

In future JSON Formatter might switch from usingJSON.parseto a custom parser (if performance allows) in order to detect when a value has been 'changed' by parsing and show an appropriate warning.

## About

Makes JSON easy to read.

### Resources

 Readme

 

### License

 BSD-3-Clause license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.1k

 stars
 

### Watchers

92

 watching
 

### Forks

960

 forks
 

 Report repository

 

## Releases3

v0.8.0

 Latest

 

Sep 19, 2025

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript89.9%
* CSS7.7%
* HTML1.6%
* JavaScript0.8%