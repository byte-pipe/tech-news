---
title: 'GitHub - asciimoo/hister: Your own search engine · GitHub'
url: https://github.com/asciimoo/hister
site_name: github
content_file: github-github-asciimoohister-your-own-search-engine-githu
fetched_at: '2026-08-25T11:24:44.681266'
original_url: https://github.com/asciimoo/hister
author: asciimoo
description: Your own search engine. Contribute to asciimoo/hister development by creating an account on GitHub.
---

asciimoo

 

/

hister

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork115
* Star2.5k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,966 Commits
1,966 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.forgejo/
workflows
.forgejo/
workflows
 
 
.github
.github
 
 
client
client
 
 
cmd
cmd
 
 
config
config
 
 
contrib/
systemd
contrib/
systemd
 
 
files
files
 
 
nix
nix
 
 
scripts
scripts
 
 
server
server
 
 
webui
webui
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.fallowrc.json
.fallowrc.json
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.toml
.golangci.toml
 
 
.goreleaser-rolling.yml
.goreleaser-rolling.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
.prettierignore
.prettierignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
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
 
 
compose.yml
compose.yml
 
 
docker-bake.hcl
docker-bake.hcl
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
generate.go
generate.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
hister.go
hister.go
 
 
manage.sh
manage.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
prettier.config.js
prettier.config.js
 
 
View all files

## Repository files navigation

# Hister

Your own search engine

Hister is a private search engine for the pages you visit and the files you keep. It indexes their full contents so you can find information again from the web interface, terminal, or an AI assistant connected through MCP.

Try the demo·Download Hister·Read the quickstart·Documentation

## Quickstart

1. Download the binary for your platform from thelatest release, then rename it tohister(hister.exeon Windows).
2. On Linux or macOS, make it executable:chmod +x hister
3. Start Hister on Linux or macOS:./hister listenOn Windows, run.\hister.exe listenin PowerShell.
4. Openhttp://127.0.0.1:4433and install the browser extension forFirefoxorChrome.

No configuration is required for a local personal setup. See thecomplete quickstartto import existing browser history and choose what Hister indexes.

## Features

* Privacy focused: No telemetry or mandatory cloud service. Run Hister locally or on infrastructure you control.
* Full text indexing: Search the actual contents of visited pages and local files, not only titles and URLs.
* Automatic browser indexing: Save newly visited pages with the Firefox or Chrome extension.
* Powerful queries: Use field filters, phrases, wildcards, negation, aliases, and result priorities.
* Optional semantic search: Find documents by meaning through an embeddings endpoint you configure.
* Crawler and browser import: Index websites or bring in existing browser history.
* Web, terminal, and MCP clients: Search from the browser, TUI, command line, or an AI assistant.
* Multi user support: Keep each user's documents and search results separate on a shared server.

## Privacy

By default, Hister has no telemetry and no cloud sync. The browser extension sends indexed page content only to the Hister server you configure, apart from downloading page favicons. The server stores documents and search indexes on that server.

Optional semantic search sends document text to the embeddings endpoint you choose. Review theprivacy overviewandsemantic search configurationbefore enabling remote integrations.

## Development

Requirements are Go 1.26, npm, and a C compiler for CGO dependencies.

git clone https://github.com/asciimoo/hister.git

cd
 hister
./manage.sh build

To work on the web app with hot reload and automatic Go rebuilds:

npm run serve:app

This starts a Vite development server and the Go backend with automatic rebuilds throughair.

## Community and contributing

Join us on IRCNet in#histeror onDiscord.

ReadCONTRIBUTING.mdbefore submitting a change. Bugs and suggestions belong in theissue tracker. For security reports, seeSECURITY.md.

## Sponsors

## License

AGPLv3or any later version