---
title: 'GitHub - henrygd/beszel: Lightweight server monitoring with historical data, docker stats, and alerts. · GitHub'
url: https://github.com/henrygd/beszel
site_name: tldr
content_file: tldr-github-henrygdbeszel-lightweight-server-monitoring
fetched_at: '2026-08-15T11:17:46.022955'
original_url: https://github.com/henrygd/beszel
date: '2026-08-15'
description: Lightweight server monitoring with historical data, docker stats, and alerts. - henrygd/beszel
tags:
- tldr
---

henrygd

 

/

beszel

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork956
* Star24.3k

 
 
 
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

1,497 Commits
1,497 Commits
.github
.github
 
 
agent
agent
 
 
internal
internal
 
 
supplemental
supplemental
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.goreleaser.yml
.goreleaser.yml
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
SECURITY.md
SECURITY.md
 
 
beszel.go
beszel.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
i18n.yml
i18n.yml
 
 
readme.md
readme.md
 
 
View all files

## Repository files navigation

# Beszel

Beszel is a lightweight server monitoring platform that includes Docker statistics, historical data, and alert functions.

It has a friendly web interface, simple configuration, and is ready to use out of the box. It supports automatic backup, multi-user, OAuth authentication, and API access.

## Features

* Lightweight: Smaller and less resource-intensive than leading solutions.
* Simple: Easy setup with little manual configuration required.
* Docker stats: Tracks CPU, memory, and network usage history for each container.
* Alerts: Configurable alerts for CPU, memory, disk, bandwidth, temperature, load average, and status.
* Multi-user: Users manage their own systems. Admins can share systems across users.
* OAuth / OIDC: Supports many OAuth2 providers. Password auth can be disabled.
* Automatic backups: Save to and restore from disk or S3-compatible storage.

## Architecture

Beszel consists of two main components: thehuband theagent.

* Hub: A web application built onPocketBasethat provides a dashboard for viewing and managing connected systems.
* Agent: Runs on each system you want to monitor and communicates system metrics to the hub.

## Getting started

Thequick start guideand other documentation is available on our website,beszel.dev. You'll be up and running in a few minutes.

## Screenshots

## Supported metrics

* CPU usage- Host system and Docker / Podman containers.
* Memory usage- Host system and containers. Includes swap and ZFS ARC.
* Disk usage- Host system. Supports multiple partitions and devices.
* Disk I/O- Host system. Supports multiple partitions and devices.
* Network usage- Host system and containers.
* Load average- Host system.
* Temperature- Host system sensors.
* GPU usage / power draw- Nvidia, AMD, and Intel.
* Battery- Host system battery charge.
* Containers- Status and metrics of all running Docker / Podman containers.
* S.M.A.R.T.- Host system disk health (includes eMMC wear/EOL and Linux mdraid array health via sysfs when available).

## Help and discussion

Please search existing issues and discussions before opening a new one. I try my best to respond, but may not always have time to do so.

#### Bug reports and feature requests

Bug reports and feature requests can be posted onGitHub issues.

#### Support and general discussion

Support requests and general discussion can be posted onGitHub discussionsor the community-runMatrix room:#beszel:matrix.org.

## License

Beszel is licensed under the MIT License. See theLICENSEfile for more details.