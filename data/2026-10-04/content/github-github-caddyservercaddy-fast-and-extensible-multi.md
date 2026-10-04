---
title: 'GitHub - caddyserver/caddy: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS · GitHub'
url: https://github.com/caddyserver/caddy
site_name: github
content_file: github-github-caddyservercaddy-fast-and-extensible-multi
fetched_at: '2026-10-04T15:40:32.505970'
original_url: https://github.com/caddyserver/caddy
author: caddyserver
description: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS - caddyserver/caddy
---

caddyserver

 

/

caddy

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork5k
* Star76.4k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,725 Commits
2,725 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
caddyconfig
caddyconfig
 
 
caddytest
caddytest
 
 
cmd
cmd
 
 
internal
internal
 
 
modules
modules
 
 
notify
notify
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
AUTHORS
AUTHORS
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
admin.go
admin.go
 
 
admin_checkhost_case_test.go
admin_checkhost_case_test.go
 
 
admin_origin_case_test.go
admin_origin_case_test.go
 
 
admin_test.go
admin_test.go
 
 
caddy.go
caddy.go
 
 
caddy_test.go
caddy_test.go
 
 
context.go
context.go
 
 
context_test.go
context_test.go
 
 
duration_fuzz.go
duration_fuzz.go
 
 
filepath.go
filepath.go
 
 
filepath_windows.go
filepath_windows.go
 
 
filesystem.go
filesystem.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
listen.go
listen.go
 
 
listen_reuseUnixSocket.go
listen_reuseUnixSocket.go
 
 
listen_reuseUnixSocket_windows.go
listen_reuseUnixSocket_windows.go
 
 
listen_test.go
listen_test.go
 
 
listen_unix.go
listen_unix.go
 
 
listen_unix_setopt.go
listen_unix_setopt.go
 
 
listen_unix_setopt_freebsd.go
listen_unix_setopt_freebsd.go
 
 
listen_unix_test.go
listen_unix_test.go
 
 
listeners.go
listeners.go
 
 
listeners_fuzz.go
listeners_fuzz.go
 
 
listeners_port_span_test.go
listeners_port_span_test.go
 
 
listeners_test.go
listeners_test.go
 
 
logging.go
logging.go
 
 
logging_test.go
logging_test.go
 
 
metrics.go
metrics.go
 
 
modules.go
modules.go
 
 
modules_test.go
modules_test.go
 
 
replacer.go
replacer.go
 
 
replacer_fuzz.go
replacer_fuzz.go
 
 
replacer_test.go
replacer_test.go
 
 
service_windows.go
service_windows.go
 
 
sigtrap.go
sigtrap.go
 
 
sigtrap_nonposix.go
sigtrap_nonposix.go
 
 
sigtrap_posix.go
sigtrap_posix.go
 
 
storage.go
storage.go
 
 
usagepool.go
usagepool.go
 
 
usagepool_test.go
usagepool_test.go
 
 
View all files

## Repository files navigation

### aproject

### Every site on HTTPS

Caddy is an extensible server platform that uses TLS by default.

Releases·Documentation·Get Help

	 
	

	 
	

	 
	

	 
	

	 
	

Powered by

Special thanks to:

### Warp, built for coding with multiple AI agents

Available for MacOS, Linux, & Windows

### Menu

* Features
* Install
* Build from sourceFor developmentWith version information and/or plugins
* For development
* With version information and/or plugins
* Quick start
* Overview
* Full documentation
* Getting help
* About

## Features

* Easy configurationwith theCaddyfile
* Powerful configurationwith itsnative JSON config
* Dynamic configurationwith theJSON API
* Config adaptersif you don't like JSON
* Automatic HTTPSby defaultZeroSSLandLet's Encryptfor public namesFully-managed local CA for internal names & IPsCan coordinate with other Caddy instances in a clusterMulti-issuer fallbackEncrypted ClientHello (ECH) support
* ZeroSSLandLet's Encryptfor public names
* Fully-managed local CA for internal names & IPs
* Can coordinate with other Caddy instances in a cluster
* Multi-issuer fallback
* Encrypted ClientHello (ECH) support
* Stays up when other servers go downdue to TLS/OCSP/certificate-related issues
* Production-readyafter serving trillions of requests and managing millions of TLS certificates
* Scales to hundreds of thousands of sitesas proven in production
* HTTP/1.1, HTTP/2, and HTTP/3all supported by default
* Highly extensiblemodular architecturelets Caddy do anything without bloat
* Runs anywherewithno external dependencies(not even libc)
* Written in Go, a language with highermemory safety guaranteesthan other servers
* Actuallyfun to use
* So much more todiscover

## Install

The simplest, cross-platform way to get started is to download Caddy fromGitHub Releasesand place the executable file in your PATH.

Seeour online documentationfor other install instructions.

## Build from source

Requirements:

* Go 1.26.0 or newer

### For development

Note:These stepswill not embed proper version information. For that, please follow the instructions in the next section.

$ git clone 
"
https://github.com/caddyserver/caddy.git
"

$ 
cd
 caddy/cmd/caddy/
$ go build

When you run Caddy, it may try to bind to low ports unless otherwise specified in your config. If your OS requires elevated privileges for this, you will need to give your new binary permission to do so. On Linux, this can be done easily with:sudo setcap cap_net_bind_service=+ep ./caddy

If you prefer to usego runwhich only creates temporary binaries, you can still do this with the includedsetcap.shlike so:

$ go run -exec ./setcap.sh main.go

If you don't want to type your password forsetcap, usesudo visudoto edit your sudoers file and allow your user account to run that command without a password, for example:

username ALL=(ALL:ALL) NOPASSWD: /usr/sbin/setcap

replacingusernamewith your actual username. Please be careful and only do this if you know what you are doing! We are only qualified to document how to use Caddy, not Go tooling or your computer, and we are providing these instructions for convenience only; please learn how to use your own computer at your own risk and make any needful adjustments.

Then you can run the tests in all modules or a specific one:

$ go 
test
 ./...
$ go 
test
 ./modules/caddyhttp/tracing/

### With version information and/or plugins

Usingour builder tool,xcaddy...

$ xcaddy build

...the following steps are automated:

1. Create a new folder:mkdir caddy
2. Change into it:cd caddy
3. CopyCaddy's main.gointo the empty folder. Add imports for any custom plugins you want to add.
4. Initialize a Go module:go mod init caddy
5. (Optional) Pin Caddy version:go get github.com/caddyserver/caddy/v2@versionreplacingversionwith a git tag, commit, or branch name.
6. (Optional) Add plugins by adding their import:_ "import/path/here"
7. Compile:go build -tags=nobadger,nomysql,nopgx

## Quick start

TheCaddy websitehas documentation that includes tutorials, quick-start guides, reference, and more.

We recommend that all users -- regardless of experience level -- do ourGetting Startedguide to become familiar with using Caddy.

If you've only got a minute,the website has several quick-start tutorialsto choose from! However, after finishing a quick-start tutorial, please read more documentation to understand how the software works. 🙂

## Overview

Caddy is most often used as an HTTPS server, but it is suitable for any long-running Go program. First and foremost, it is a platform to run Go applications. Caddy "apps" are just Go programs that are implemented as Caddy modules. Two apps --tlsandhttp-- ship standard with Caddy.

Caddy apps instantly benefit fromautomated documentation, graceful on-lineconfig changes via API, and unification with other Caddy apps.

AlthoughJSONis Caddy's native config language, Caddy can accept input fromconfig adapterswhich can essentially convert any config format of your choice into JSON: Caddyfile, JSON 5, YAML, TOML, NGINX config, and more.

The primary way to configure Caddy is throughits API, but if you prefer config files, thecommand-line interfacesupports those too.

Caddy exposes an unprecedented level of control compared to any web server in existence. In Caddy, you are usually setting the actual values of the initialized types in memory that power everything from your HTTP handlers and TLS handshakes to your storage medium. Caddy is also ridiculously extensible, with a powerful plugin system that makes vast improvements over other web servers.

To wield the power of this design, you need to know how the config document is structured. Please seeour documentation sitefor details aboutCaddy's config structure.

Nearly all of Caddy's configuration is contained in a single config document, rather than being scattered across CLI flags and env variables and a configuration file as with other web servers. This makes managing your server config more straightforward and reduces hidden variables/factors.

## Full documentation

Our website has complete documentation:

https://caddyserver.com/docs/

The docs are also open source. You can contribute to them here:https://github.com/caddyserver/website

## Getting help

* We advise companies using Caddy to secure a support contract throughArdan Labsbefore help is needed.
* Asponsorshipgoes a long way! We can offer private help to sponsors. If Caddy is benefitting your company, please consider a sponsorship. This not only helps fund full-time work to ensure the longevity of the project, it provides your company the resources, support, and discounts you need; along with being a great look for your company to your customers and potential customers!
* Individuals can exchange help for free on our community forum athttps://caddy.community. Remember that people give help out of their spare time and good will. The best way to get help is to give it first!

Please use ourissue trackeronly for bug reports and feature requests, i.e. actionable development items (support questions will usually be referred to the forums).

## About

Matthew Holt began developing Caddy in 2014 while studying computer science at Brigham Young University. (The name "Caddy" was chosen because this software helps with the tedious, mundane tasks of serving the Web, and is also a single place for multiple things to be organized together.) It soon became the first web server to use HTTPS automatically and by default, and now has hundreds of contributors and has served trillions of HTTPS requests.

The name "Caddy" is trademarked.The name of the software is "Caddy", not "Caddy Server" or "CaddyServer". Please call it "Caddy" or, if you wish to clarify, "the Caddy web server". Caddy is a registered trademark of Stack Holdings GmbH.

* Project on X:@caddyserver
* Author on X:@mholt6

Caddy is a project ofZeroSSL, an HID Global company.

Debian package repository hosting is graciously provided byCloudsmith. Cloudsmith is the only fully hosted, cloud-native, universal package management solution, that enables your organization to create, store and share packages in any format, to any place, with total confidence.