---
title: 'GitHub - git-bug/git-bug: Distributed, offline-first bug tracker integrated in git · GitHub'
url: https://github.com/git-bug/git-bug
site_name: hnrss
content_file: hnrss-github-git-buggit-bug-distributed-offline-first-bu
fetched_at: '2026-09-26T05:56:28.311383'
original_url: https://github.com/git-bug/git-bug
date: '2026-09-25'
description: Distributed, offline-first bug tracker integrated in git - git-bug/git-bug
tags:
- hackernews
- hnrss
---

git-bug

 

/

git-bug

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork325
* Star10.4k

 
 
 
trunk
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,694 Commits
2,694 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
api
api
 
 
bridge
bridge
 
 
cache
cache
 
 
commands
commands
 
 
doc
doc
 
 
entities
entities
 
 
entity
entity
 
 
misc
misc
 
 
query
query
 
 
repository
repository
 
 
termui
termui
 
 
tests
tests
 
 
util
util
 
 
webui
webui
 
 
.gitignore
.gitignore
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
.mailmap
.mailmap
 
 
.tool-versions
.tool-versions
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALLATION.md
INSTALLATION.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
version.go
version.go
 
 
View all files

## Repository files navigation

# git-bug

Issues-Documentation-Discussions

git-bugis a bug tracker that:

* is fully integrated in git: you only need your git repository to have a bug tracker
* is distributed: use your normal git remote to collaborate, push and pull your bugs!
* works offline: in a plane or under the sea? Keep reading and writing bugs!
* prevents vendor lock-in: your usual service is down or went bad? You already have a full backup.
* is fast: listing bugs or opening them is a matter of milliseconds
* doesn't pollute your project: no files are added in your project
* integrates with your tooling: use the UI you like (CLI, terminal, web) or integrate with your existing tools through the CLI or the GraphQL API
* bridges to other bug trackers: usebridgesto import and export to other trackers.

## Installation

SeeINSTALLATION.mdfor the complete guide, including how to build from source and verify your install.

## Workflows

There are multiple ways to usegit-bug. Seethe workflow documentationfor the details.

Native workflow

This is the puregit-bugexperience. In a similar fashion as with code, usegit bug pushandgit bug pullto push and pull your bugs between git remotes and collaborate with your teammate.

Bridge workflow

Asgit-bughas bridges with other bug-trackers, you can use it as your personal local remote interface. Sync withgit bug bridge pullandgit bug bridge push, work from your terminal, integrate into your editor, it's up to you. And it works offline!

Web UI workflow (WIP)

Often, projects need to have their bug-tracker public and accept editions from anyone facing a problem. To support this workflow,git-bugaims to have the web UI accept external OAuth authentication and act as a public portal. However the web UI is not up to speed for that yet. Contributions are very much welcome!

## CLI usage

Create a new identity:

git bug user create

Create a new bug:

git bug add

Your favorite editor will open to write a title and a message.

You can push your new entry to a remote:

git bug push [
<
remote
>
]

And pull for updates:

git bug pull [
<
remote
>
]

List existing bugs:

git bug ls

Filter and sort bugs using aquery:

git bug ls 
"
status:open sort:edit
"

Search for bugs by text content:

git bug ls 
"
foo bar
"
 baz

You can now use commands likeshow,comment,openorcloseto display and modify bugs. For more details about each command, you can rungit bug <command> --helpor read thecommand's documentation.

## Interactive terminal UI

An interactive terminal UI is available using the commandgit bug termuito browse and edit bugs.

## Web UI

You can launch a rich Web UI withgit bug webui. Browse, search and filter issues, open new ones, comment, and edit titles, labels and status. It also doubles as a code browser for your repository, with a file tree, syntax-highlighted files, commit history and diffs.

The web UI is packed inside the same go binary and served by a local http server. It talks to the backend through a GraphQL API, whose schema is availablehere.

## Bridges

git-bugcan import from and export to Github, Gitlab, Jira and Launchpad. See thefeature matrixfor what each bridge supports, and thebridge documentationfor the full guide.

Interactively configure a new bridge:

git bug bridge new

Or manually:

git bug bridge new \
 --name=
<
bridge
>
 \
 --target=github \
 --url=https://github.com/git-bug/git-bug \
 --login=
<
login
>
 \
 --token=
<
token
>

Import bugs:

git bug bridge pull [
<
name
>
]

Export modifications:

git bug bridge push [
<
name
>
]

Delete a bridge:

git bug bridge rm [
<
name
>
]

## Internals

Interested in how it works? Have a look at thedata modeland theinternal bird-view.

The on-disk format is formally specified in thegit-bug spec, covering the DAG entity format, identities and the bug entity. Read that if you want to write another implementation or a tool that reads git-bug data directly.

Or maybe you want tomake your own distributed data-structure in git?

See also all thedocs.

## Misc

* Bash, Zsh, fish, powershell completion
* ManPages

## Planned features

Thefeature matrixgives a good overview of what is planned, without being exhaustive.

Additional planned features:

* webUI that can be used as a public portal to accept user's input
* inflatable raptor

## Contribute

PRs accepted. Drop by theMatrix roomfor a chat, look at thefeature matrixor browse theissuesanddiscussionsto see what is worked on or discussed.

SeeCONTRIBUTING.mdto get a development environment going, build the project and run the tests. To work on the web UI, have a look atits dedicated README.

## Contributors ❤️

This project exists thanks to all the people who contribute.

## Backers & sponsors

Thank you to all our backers and sponsors! 🙏 [Become a backer or sponsor]

## License

Unless otherwise stated, this project is released under theGPLv3or later license © Michael Muré.

The git-bug logo byViktor Teplovis released under theCreative Commons Attribution 4.0 International (CC BY 4.0)license © Viktor Teplov.