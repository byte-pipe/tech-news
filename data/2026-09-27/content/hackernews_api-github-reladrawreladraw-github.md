---
title: GitHub - reladraw/reladraw · GitHub
url: https://github.com/reladraw/reladraw
site_name: hackernews_api
content_file: hackernews_api-github-reladrawreladraw-github
fetched_at: '2026-09-27T15:32:24.269467'
original_url: https://github.com/reladraw/reladraw
author: jpwalsh234
date: '2026-09-26'
description: Contribute to reladraw/reladraw development by creating an account on GitHub.
tags:
- hackernews
- trending
---

reladraw

 

/

reladraw

Public

* NotificationsYou must be signed in to change notification settings
* Fork12
* Star669

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

70 Commits
70 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude/
skills/
reladraw
.claude/
skills/
reladraw
 
 
docs
docs
 
 
examples
examples
 
 
src
src
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SYNTAX.md
SYNTAX.md
 
 
dev.sh
dev.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# reladraw

reladraw is a text language for diagrams where you say where things go.

Try it in your browser →

I wanted to be able to create custom, expressive diagrams where I decided how to arrange the diagram, but without the inefficiency of manually drawing in draw.io. For example, this is a diagram drawn in draw.io:

This is the same diagram, but written in reladraw (examples/arch.reladraw).

## Why not Mermaid or draw.io?

Mermaid, Graphviz and D2 let you declare boxes and connections, then determine positions for you. If you have a particular picture in mind, these aren't the right tool.

On the other hand, tools like draw.io or Excalidraw allow absolute placement, but that means much more effort, whether for humans clicking and dragging nodes around or agents recalculating coordinates and editing verbose XML source code files.

reladraw sits between those two extremes, aiming to have the benefits of a diagram language, like Mermaid, but also having the expressiveness and custom placement that you can get with draw.io. Positions are relative, so you don't have to manually pick coordinates. For example:

node app "Web app"
node app.ui "Interface"
node app.api "API" below app.ui

node store "Database" right of app level with app

edge app.api -> store "queries" from: right to: left

See alsoSYNTAX.mdandexamples/.

## Install

npm install -g reladraw
reladraw diagram.reladraw -o diagram.svg

Or from a clone, which also gets you the examples:

npm install && npm run build
node dist/cli.js examples/arch.reladraw -o out.svg

## Using it with an agent

To install a skill to let your agent know how to use reladraw:

npx skills add reladraw/reladraw -g

That installs it for every agent you use (Claude Code, Codex, Cursor, Copilot and others), each in its own skills directory. Leave off-gto install it into the current project only. To install it for just one agent, name it with-a:

npx skills add reladraw/reladraw -g -a claude-code

That gets you a copy of the skill at the time you run it, so you'll need to re-run that command to get the latest skill when there is a new release.

## Status

Version 0.8.0. Early stage, but works. The parser, layout engine, and SVG renderer are written in TypeScript, with zero runtime dependencies. There is a command-line tool that turns a .reladraw text file into an SVG.

The language isn't stable yet, so expect the syntax to change.

## License

Apache-2.0. SeeLICENSE. The license covers the code, not the name. It grants no rights to "reladraw", the project logo or the project's other marks. SeeNOTICE.

## Contributing

Issues are welcome. Particularly helpful is a diagram you could not represent in reladraw. While the language is still changing quickly, an issue helps more than a pull request. SeeCONTRIBUTING.md.