---
title: 'GitHub - knadh/listmonk: High performance, self-hosted, newsletter and mailing list manager with a modern dashboard. Single binary app. · GitHub'
url: https://github.com/knadh/listmonk
site_name: github
content_file: github-github-knadhlistmonk-high-performance-self-hosted
fetched_at: '2026-05-17T19:29:26.507261'
original_url: https://github.com/knadh/listmonk
author: knadh
description: High performance, self-hosted, newsletter and mailing list manager with a modern dashboard. Single binary app. - knadh/listmonk
---

knadh

 

/

listmonk

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star20.5k

 
 
 
 
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

1,975 Commits
1,975 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
cmd
cmd
 
 
dev
dev
 
 
docs
docs
 
 
frontend
frontend
 
 
i18n
i18n
 
 
internal
internal
 
 
models
models
 
 
queries
queries
 
 
scripts
scripts
 
 
static
static
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.go-version
.go-version
 
 
.goreleaser-nightly.yml
.goreleaser-nightly.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
VERSION
VERSION
 
 
config.toml.sample
config.toml.sample
 
 
docker-compose.yml
docker-compose.yml
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
listmonk-simple.service
listmonk-simple.service
 
 
listmonk@.service
listmonk@.service
 
 
permissions.json
permissions.json
 
 
project.inlang.json
project.inlang.json
 
 
schema.sql
schema.sql
 
 
View all files

## Repository files navigation

listmonk is a standalone, self-hosted, newsletter and mailing list manager. It is fast, feature-rich, and packed into a single binary. It uses a PostgreSQL database as its data store.

Visitlistmonk.appfor more info. Check out thelive demo.

## Installation

### Docker

The latest image is available on DockerHub atlistmonk/listmonk:latest.
Download and use the sampledocker-compose.yml.

#
 Download the compose file to the current directory.

curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml

#
 Run the services in the background.

docker compose up -d

Visithttp://localhost:9000

Seeinstallation docs

### Binary

* Download thelatest releaseand extract the listmonk binary.
* ./listmonk --new-configto generate config.toml. Edit it.
* ./listmonk --installto setup the Postgres DB (or--upgradeto upgrade an existing DB. Upgrades are idempotent and running them multiple times have no side effects).
* Run./listmonkand visithttp://localhost:9000

Seeinstallation docs

## Developers

listmonk is free and open source software licensed under AGPLv3. If you are interested in contributing, refer to thedeveloper setup. The backend is written in Go and the frontend is Vue with Buefy for UI.

## License

listmonk is licensed under the AGPL v3 license.

## About

High performance, self-hosted, newsletter and mailing list manager with a modern dashboard. Single binary app.

listmonk.app

### Topics

 email-marketing

 self-hosted

 newsletter

 smtp

 transactional-emails

 campaign

 mailing-list

 sms-gateway

 email-subscription

 newsletter-management

 newsletter-software

 campaign-management

 listmonk

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

20.5k

 stars
 

### Watchers

133

 watching
 

### Forks

2.1k

 forks
 

 Report repository

 

## Releases40

v6.1.0

 Latest

 

Mar 29, 2026

 

+ 39 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go41.3%
* Vue24.9%
* JavaScript19.7%
* TypeScript8.8%
* HTML1.8%
* SCSS1.6%
* Other1.9%