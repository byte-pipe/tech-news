---
title: 'GitHub - lightpanda-io/browser: Lightpanda: the headless browser designed for AI and automation · GitHub'
url: https://github.com/lightpanda-io/browser
site_name: github
content_file: github-github-lightpanda-iobrowser-lightpanda-the-headles
fetched_at: '2026-03-13T11:14:29.993265'
original_url: https://github.com/lightpanda-io/browser
author: lightpanda-io
description: 'Lightpanda: the headless browser designed for AI and automation - lightpanda-io/browser'
---

lightpanda-io

 

/

browser

Public

* NotificationsYou must be signed in to change notification settings
* Fork486
* Star14.2k

 
 
 
 
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

4,853 Commits
4,853 Commits
.github
.github
 
 
src
src
 
 
.gitignore
.gitignore
 
 
CLA.md
CLA.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
LICENSING.md
LICENSING.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build.zig
build.zig
 
 
build.zig.zon
build.zig.zon
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
View all files

## Repository files navigation

# Lightpanda Browser

lightpanda.io

Lightpanda is the open-source browser made for headless usage:

* Javascript execution
* Support of Web APIs (partial, WIP)
* Compatible with Playwright1, Puppeteer, chromedp throughCDP

Fast web automation for AI agents, LLM training, scraping and testing:

* Ultra-low memory footprint (9x less than Chrome)
* Exceptionally fast execution (11x faster than Chrome)
* Instant startup

 

Puppeteer requesting 100 pages from a local website on a AWS EC2 m5.large instance.
Seebenchmark details.

## Quick start

### Install

Install from the nightly builds

You can download the last binary from thenightly
buildsfor
Linux x86_64 and MacOS aarch64.

For Linux

curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-x86_64-linux && \

chmod a+x ./lightpanda

For MacOS

curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/download/nightly/lightpanda-aarch64-macos && \

chmod a+x ./lightpanda

For Windows + WSL2

The Lightpanda browser is compatible to run on windows inside WSL. Follow the Linux instruction for installation from a WSL terminal.
It is recommended to install clients like Puppeteer on the Windows host.

Install from Docker

Lightpanda providesofficial Docker
imagesfor both Linux amd64 and
arm64 architectures.
The following command fetches the Docker image and starts a new container exposing Lightpanda's CDP server on port9222.

docker run -d --name lightpanda -p 9222:9222 lightpanda/browser:nightly

### Dump a URL

./lightpanda fetch --obey_robots --log_format pretty --log_level info https://demo-browser.lightpanda.io/campfire-commerce/

INFO telemetry : telemetry status . . . . . . . . . . . . . [+0ms]

 disabled = false

INFO page : navigate . . . . . . . . . . . . . . . . . . . . [+6ms]

 url = https://demo-browser.lightpanda.io/campfire-commerce/

 method = GET

 reason = address_bar

 body = false

 req_id = 1

INFO browser : executing script . . . . . . . . . . . . . . [+118ms]

 src = https://demo-browser.lightpanda.io/campfire-commerce/script.js

 kind = javascript

 cacheable = true

INFO http : request complete . . . . . . . . . . . . . . . . [+140ms]

 source = xhr

 url = https://demo-browser.lightpanda.io/campfire-commerce/json/product.json

 status = 200

 len = 4770

INFO http : request complete . . . . . . . . . . . . . . . . [+141ms]

 source = fetch

 url = https://demo-browser.lightpanda.io/campfire-commerce/json/reviews.json

 status = 200

 len = 1615

<!DOCTYPE html>

### Start a CDP server

./lightpanda serve --obey_robots --log_format pretty --log_level info --host 127.0.0.1 --port 9222

INFO telemetry : telemetry status . . . . . . . . . . . . . [+0ms]

 disabled = false

INFO app : server running . . . . . . . . . . . . . . . . . [+0ms]

 address = 127.0.0.1:9222

Once the CDP server started, you can run a Puppeteer script by configuring thebrowserWSEndpoint.

'use strict'

import
 
puppeteer
 
from
 
'puppeteer-core'
;

// use browserWSEndpoint to pass the Lightpanda's CDP server address.

const
 
browser
 
=
 
await
 
puppeteer
.
connect
(
{

 
browserWSEndpoint
: 
"ws://127.0.0.1:9222"
,

}
)
;

// The rest of your script remains the same.

const
 
context
 
=
 
await
 
browser
.
createBrowserContext
(
)
;

const
 
page
 
=
 
await
 
context
.
newPage
(
)
;

// Dump all the links from the page.

await
 
page
.
goto
(
'https://demo-browser.lightpanda.io/amiibo/'
,
 
{
waitUntil
: 
"networkidle0"
}
)
;

const
 
links
 
=
 
await
 
page
.
evaluate
(
(
)
 
=>
 
{

 
return
 
Array
.
from
(
document
.
querySelectorAll
(
'a'
)
)
.
map
(
row
 
=>
 
{

 
return
 
row
.
getAttribute
(
'href'
)
;

 
}
)
;

}
)
;

console
.
log
(
links
)
;

await
 
page
.
close
(
)
;

await
 
context
.
close
(
)
;

await
 
browser
.
disconnect
(
)
;

### Telemetry

By default, Lightpanda collects and sends usage telemetry. This can be disabled by setting an environment variableLIGHTPANDA_DISABLE_TELEMETRY=true. You can read Lightpanda's privacy policy at:https://lightpanda.io/privacy-policy.

## Status

Lightpanda is in Beta and currently a work in progress. Stability and coverage are improving and many websites now work.
You may still encounter errors or crashes. Please open an issue with specifics if so.

Here are the key features we have implemented:

* HTTP loader (Libcurl)
* HTML parser (html5ever)
* DOM tree
* Javascript support (v8)
* DOM APIs
* AjaxXHR APIFetch API
* XHR API
* Fetch API
* DOM dump
* CDP/websockets server
* Click
* Input form
* Cookies
* Custom HTTP headers
* Proxy support
* Network interception
* Respectrobots.txtwith option--obey_robots

NOTE: There are hundreds of Web APIs. Developing a browser (even just for headless mode) is a huge task. Coverage will increase over time.

You can also follow the progress of our Javascript support in our dedicatedzig-js-runtimeproject.

## Build from sources

### Prerequisites

Lightpanda is written withZig0.15.2. You have to
install it with the right version in order to build the project.

Lightpanda also depends onzig-js-runtime(with v8),Libcurlandhtml5ever.

To be able to build the v8 engine for zig-js-runtime, you have to install some libs:

ForDebian/Ubuntu based Linux:

sudo apt install xz-utils ca-certificates \
 pkg-config libglib2.0-dev \
 clang make curl git

You also need toinstall Rust.

For systems withNix, you can use the devShell:

nix develop

ForMacOS, you need cmake andRust.

brew install cmake

### Build and run

You an build the entire browser withmake buildormake build-devfor debug
env.

But you can directly use the zig command:zig build run.

#### Embed v8 snapshot

Lighpanda uses v8 snapshot. By default, it is created on startup but you can
embed it by using the following commands:

Generate the snapshot.

zig build snapshot_creator -- src/snapshot.bin

Build using the snapshot binary.

zig build -Dsnapshot_path=../../snapshot.bin

See#1279for more details.

## Test

### Unit Tests

You can test Lightpanda by runningmake test.

### End to end tests

To run end to end tests, you need to clone thedemo
repositoryinto../demodir.

You have to install thedemo's node
requirements

You also need to installGo> v1.24.

make end2end

### Web Platform Tests

Lightpanda is tested against the standardizedWeb Platform
Tests.

We usea forkincluding a customtestharnessreport.js.

For reference, you can easily execute a WPT test case with your browser viawpt.live.

#### Configure WPT HTTP server

To run the test, you must clone the repository, configure the custom hosts and generate theMANIFEST.jsonfile.

Clone the repository with theforkbranch.

git clone -b fork --depth=1 git@github.com:lightpanda-io/wpt.git

Enter into thewpt/dir.

Install custom domains in your/etc/hosts

./wpt make-hosts-file | sudo tee -a /etc/hosts

GenerateMANIFEST.json

./wpt manifest

Use theWPT's setup
guidefor
details.

#### Run WPT test suite

An externalGorunner is provided bygithub.com/lightpanda-io/demo/repository, located intowptrunner/dir.
You need to clone the project first.

First start the WPT's HTTP server from yourwpt/clone dir.

./wpt serve

Run a Lightpanda browser

zig build run -- --insecure_disable_tls_host_verification

Then you can start the wptrunner from the Demo's clone dir:

cd wptrunner && go run .

Or one specific test:

cd wptrunner && go run . Node-childNodes.html

wptrunnercommand accepts--summaryand--jsonoptions modifying output.
Also--concurrencydefine the concurrency limit.

⚠️Running the whole test suite will take a long time. In this case,
it's useful to build inreleaseFastmode to make tests faster.

zig build -Doptimize=ReleaseFast run

## Contributing

Lightpanda accepts pull requests through GitHub.

You have to sign ourCLAduring the pull request process otherwise
we're not able to accept your contributions.

## Why?

### Javascript execution is mandatory for the modern web

In the good old days, scraping a webpage was as easy as making an HTTP request, cURL-like. It’s not possible anymore, because Javascript is everywhere, like it or not:

* Ajax, Single Page App, infinite loading, “click to display”, instant search, etc.
* JS web frameworks: React, Vue, Angular & others

### Chrome is not the right tool

If we need Javascript, why not use a real web browser? Take a huge desktop application, hack it, and run it on the server. Hundreds or thousands of instances of Chrome if you use it at scale. Are you sure it’s such a good idea?

* Heavy on RAM and CPU, expensive to run
* Hard to package, deploy and maintain at scale
* Bloated, lots of features are not useful in headless usage

### Lightpanda is built for performance

If we want both Javascript and performance in a true headless browser, we need to start from scratch. Not another iteration of Chromium, really from a blank page. Crazy right? But that’s what we did:

* Not based on Chromium, Blink or WebKit
* Low-level system programming language (Zig) with optimisations in mind
* Opinionated: without graphical rendering

## Footnotes

1. Playwright support disclaimer:Due to the nature of Playwright, a script that works with the current version of the browser may not function correctly with a future version. Playwright uses an intermediate JavaScript layer that selects an execution strategy based on the browser's available features. If Lightpanda adds a newWeb API, Playwright may choose to execute different code for the same script. This new code path could attempt to use features that are not yet implemented. Lightpanda makes an effort to add compatibility tests, but we can't cover all scenarios. If you encounter an issue, please create aGitHub issueand include the last known working version of the script.↩

## About

Lightpanda: the headless browser designed for AI and automation

lightpanda.io

### Topics

 browser

 zig

 headless

 cdp

 browser-automation

 puppeteer

 playwright

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

14.2k

 stars
 

### Watchers

42

 watching
 

### Forks

486

 forks
 

 Report repository

 

## Releases8

nightly

 Latest

 

Jul 16, 2024

 

+ 7 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors26

+ 12 contributors

## Languages

* Zig73.9%
* HTML25.0%
* Rust0.6%
* JavaScript0.3%
* Makefile0.1%
* Dockerfile0.1%