---
title: 'GitHub - bigskysoftware/htmx: </> htmx - high power tools for HTML · GitHub'
url: https://github.com/bigskysoftware/htmx
site_name: github
content_file: github-github-bigskysoftwarehtmx-htmx-high-power-tools-fo
fetched_at: '2026-08-30T06:00:12.494518'
original_url: https://github.com/bigskysoftware/htmx
author: bigskysoftware
description: </> htmx - high power tools for HTML. Contribute to bigskysoftware/htmx development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 bigskysoftware

 

/

htmx

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star49.1k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,551 Commits
3,551 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
dist
dist
 
 
editors/
jetbrains
editors/
jetbrains
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
www
www
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
netlify.toml
netlify.toml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
web-test-runner.config.mjs
web-test-runner.config.mjs
 
 
View all files

## Repository files navigation

high power tools for HTML

## introduction

htmx allows you to accessAJAX,CSS Transitions,WebSocketsandServer Sent Eventsdirectly in HTML, usingattributes, so you can buildmodern user interfaceswith thesimplicityandpowerof hypertext

htmx is small (~14k min.gz'd),dependency-free&extendable

## motivation

* Why should only<a>and<form>be able to make HTTP requests?
* Why should onlyclick&submitevents trigger them?
* Why should only GET & POST be available?
* Why should you only be able to replace theentirescreen?

By removing these arbitrary constraints htmx completes HTML as ahypertext

## quick start

 
<
script
 
src
="
https://cdn.jsdelivr.net/npm/htmx.org@2.0.10/dist/htmx.min.js
" 
 
integrity
="
sha384-H5SrcfygHmAuTDZphMHqBJLc3FhssKjG7w/CeCpFReSfwBWDTKpkzPP8c+cLsK+V
" 
 
crossorigin
="
anonymous
"
>
</
script
>

 
<!-- have a button POST a click via AJAX -->

 
<
button
 
hx-post
="
/clicked
" 
hx-swap
="
outerHTML
"
>

 Click Me
 
</
button
>

Thehx-postandhx-swapattributes tell htmx:

"When a user clicks on this button, issue an AJAX request to /clicked, and replace the entire button with the response"

htmx is the successor tointercooler.js

### installing as a node package

To install using npm:

npm install htmx.org --save

Note there is an old broken package calledhtmx. This ishtmx.org.

## website & docs

* https://htmx.org
* https://htmx.org/docs

## contributing

Want to contribute? Check out ourcontribution guidelines

No time? Thenbecome a sponsor

### hacking guide

To develop htmx locally, you will need to install the development dependencies.

Run:

npm install

Then, run a web server in the root.

This is easiest with:

npx serve

You can then run the test suite by navigating to:

http://0.0.0.0:3000/test/

At this point you can modify/src/htmx.jsto add features, and then add tests in the appropriate area under/test.

* /test/index.html- the root test page from which all other tests are included
* /test/attributes- attribute specific tests
* /test/core- core functionality tests
* /test/core/regressions.js- regression tests
* /test/ext- extension tests
* /test/manual- manual tests that cannot be automated

htmx uses themochatesting framework, thechaiassertion framework
andsinonto mock out AJAX requests. They are all OK.

## haiku

javascript fatigue:longing for a hypertextalready in hand