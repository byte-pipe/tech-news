---
title: 'GitHub - dani-garcia/vaultwarden: Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs · GitHub'
url: https://github.com/dani-garcia/vaultwarden
site_name: github
content_file: github-github-dani-garciavaultwarden-unofficial-bitwarden
fetched_at: '2026-04-24T11:56:23.411994'
original_url: https://github.com/dani-garcia/vaultwarden
author: dani-garcia
description: Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs - dani-garcia/vaultwarden
---

dani-garcia

 

/

vaultwarden

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star59k

 
 
 
 
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

3,013 Commits
3,013 Commits
.github
.github
 
 
docker
docker
 
 
macros
macros
 
 
migrations
migrations
 
 
playwright
playwright
 
 
resources
resources
 
 
src
src
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.template
.env.template
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.hadolint.yaml
.hadolint.yaml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.typos.toml
.typos.toml
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
build.rs
build.rs
 
 
diesel.toml
diesel.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

An alternative server implementation of the Bitwarden Client API, written in Rust and compatible withofficial Bitwarden clients[disclaimer], perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

 

 

 

Important

When using this server, please report any bugs or suggestions directly to us (seeGet in touch), regardless of whatever clients you are using (mobile, desktop, browser...). DO NOT use the official Bitwarden support channels.

## Features

A nearly complete implementation of the Bitwarden Client API is provided, including:

* Personal Vault
* Send
* Attachments
* Website icons
* Personal API Key
* OrganizationsCollections,Password Sharing,Member Roles,Groups,Event Logs,Admin Password Reset,Directory Connector,Policies
* Collections,Password Sharing,Member Roles,Groups,Event Logs,Admin Password Reset,Directory Connector,Policies
* Multi/Two Factor AuthenticationAuthenticator,Email,FIDO2 WebAuthn,YubiKey,Duo
* Authenticator,Email,FIDO2 WebAuthn,YubiKey,Duo
* Emergency Access
* Vaultwarden Admin Backend
* Modified Web Vault client(Bundled within our containers)

## Usage

Important

The web-vault requires the use a secure context for theWeb Crypto API.
That means it will only work viahttp://localhost:8000(using the port from the example below) or if youenable HTTPS.

The recommended way to install and use Vaultwarden is via our container images which are published toghcr.io,docker.ioandquay.io.
Seewhich container image to usefor an explanation of the provided tags.

There are alsocommunity driven packageswhich can be used, but those might be lagging behind the latest version or might deviate in the way Vaultwarden is configured, as described in ourWiki.

Alternatively, you can alsobuild Vaultwardenyourself.

While Vaultwarden is based upon theRocket web frameworkwhich has built-in support for TLS our recommendation would be that you setup a reverse proxy (seeproxy examples).

Tip

For more detailed examples on how to install, use and configure Vaultwarden you can check ourWiki.

### Docker/Podman CLI

Pull the container image and mount a volume from the host for persistent storage.You can replacedockerwithpodmanif you prefer to use podman.

docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
 --env DOMAIN=
"
https://vw.domain.tld
"
 \
 --volume /vw-data/:/data/ \
 --restart unless-stopped \
 --publish 127.0.0.1:8000:80 \
 vaultwarden/server:latest

This will preserve any persistent data under/vw-data/, you can adapt the path to whatever suits you.

### Docker Compose

To use Docker compose you need to create acompose.yamlwhich will hold the configuration to run the Vaultwarden container.

services
:
 
vaultwarden
:
 
image
: 
vaultwarden/server:latest

 
container_name
: 
vaultwarden

 
restart
: 
unless-stopped

 
environment
:
 
DOMAIN
: 
"
https://vw.domain.tld
"

 
volumes
:
 - 
./vw-data/:/data/

 
ports
:
 - 
127.0.0.1:8000:80

## Get in touch

Have a question, suggestion or need help? Join our community onMatrix,GitHub DiscussionsorDiscourse Forums.

Encountered a bug or crash? Please search our issue tracker and discussions to see if it's already been reported. If not, pleasestart a new discussionorcreate a new issue. Ensure you're using the latest version of Vaultwarden and there aren't any similar issues open or closed!

## Contributors

Thanks for your contribution to the project!

## Disclaimer

This project is not associated withBitwardenor Bitwarden, Inc.

However, one of the active maintainers for Vaultwarden is employed by Bitwarden and is allowed to contribute to the project on their own time. These contributions are independent of Bitwarden and are reviewed by other maintainers.

The maintainers work together to set the direction for the project, focusing on serving the self-hosting community, including individuals, families, and small organizations, while ensuring the project's sustainability.

Please note:We cannot be held liable for any data loss that may occur while using Vaultwarden. This includes passwords, attachments, and other information handled by the application. We highly recommend performing regular backups of your files and database. However, should you experience data loss, we encourage you to contact us immediately.

## Bitwarden_RS

This project was known as Bitwarden_RS and has been renamed to separate itself from the official Bitwarden server in the hopes of avoiding confusion and trademark/branding issues.Please see#1642 - v1.21.0 release and project rename to Vaultwardenfor more explanation.

## About

Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs

### Topics

 docker

 rust

 rocket

 bitwarden

 bitwarden-rs

 vaultwarden

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

59k

 stars
 

### Watchers

288

 watching
 

### Forks

2.7k

 forks
 

 Report repository

 

## Releases81

1.35.7

 Latest

 

Apr 13, 2026

 

+ 80 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* liberapay.com/dani-garcia
* https://paypal.me/DaniGG

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by494

 + 486
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust83.2%
* Handlebars10.2%
* TypeScript4.1%
* Shell0.8%
* Jinja0.7%
* HCL0.5%
* Other0.5%