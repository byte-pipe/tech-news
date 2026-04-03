---
title: 'GitHub - fluxerapp/fluxer: A free and open source instant messaging and VoIP platform built for friends, groups, and communities. Self-hosting and more activity in this repository is coming very soon! See the README. · GitHub'
url: https://github.com/fluxerapp/fluxer
site_name: github
content_file: github-github-fluxerappfluxer-a-free-and-open-source-inst
fetched_at: '2026-03-16T11:23:17.783157'
original_url: https://github.com/fluxerapp/fluxer
author: fluxerapp
description: A free and open source instant messaging and VoIP platform built for friends, groups, and communities. Self-hosting and more activity in this repository is coming very soon! See the README. - fluxerapp/fluxer
---

fluxerapp

 

/

fluxer

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork350
* Star6.5k

 
 
 
 
refactor
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

173 Commits
173 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
config
config
 
 
dev
dev
 
 
fluxer_admin
fluxer_admin
 
 
fluxer_api
fluxer_api
 
 
fluxer_app
fluxer_app
 
 
fluxer_app_proxy
fluxer_app_proxy
 
 
fluxer_desktop
fluxer_desktop
 
 
fluxer_devops
fluxer_devops
 
 
fluxer_docs
fluxer_docs
 
 
fluxer_gateway
fluxer_gateway
 
 
fluxer_integration
fluxer_integration
 
 
fluxer_marketing
fluxer_marketing
 
 
fluxer_media_proxy
fluxer_media_proxy
 
 
fluxer_relay
fluxer_relay
 
 
fluxer_relay_directory
fluxer_relay_directory
 
 
fluxer_server
fluxer_server
 
 
fluxer_static @ 6c688eb
fluxer_static @ 6c688eb
 
 
media
media
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
tsconfigs
tsconfigs
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.envrc
.envrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.ignore
.ignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.tool-versions
.tool-versions
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
LICENSING.md
LICENSING.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
biome.json
biome.json
 
 
compose.yaml
compose.yaml
 
 
devenv.lock
devenv.lock
 
 
devenv.nix
devenv.nix
 
 
devenv.yaml
devenv.yaml
 
 
flake.lock
flake.lock
 
 
knip.json
knip.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

Caution

I'm repeating it again: Holy smokes, what a ride. Fluxer is taking off much earlier than I'd expected.

I know it's hard to resist, but please wait a little longer before you dive deep into the current codebase or try to set up self-hosting. I'm aware the current stack isn't very lightweight. I'm working on making self-hosting as straightforward as possible and the development environment likewise.

Self-hosted deployments won't include any traces of Plutonium, and nothing is paywalled. You can still configure your own tiers and limits in the admin panel.

Thanks for bearing with me. Development on Fluxer is about to get much easier, and the project will be made sustainable through community contributions and bounties for development work. Stay tuned – there's not much left now.

I thought I could take it a bit easier while shipping this stabilising update, but Discord's announcement in Februrary has changed things.

There's just been a lot of work involved in keeping the production deployment up and running, handling trust & safety concerns, answering support emails, handling billing issues, and working on the refactor at the same time. I'm really excited to open up development and make it easier for others to contribute, and I can't wait to see what the community builds on Fluxer!

As soon as the refactor is ready (not much longer now!), I'll enable PRs and interact more actively and push updates to this repository more frequently. The remaining parts of the refactor are currently being worked on and being tested live in production that has over 125,000 users (and we're only two full-time employees for now). After that, all work will happen openly in public.

The team is also growing, though we remain small and can't offer very competitive salaries just yet – but if you want to work part-time or contract on projects, or you think you're a great fit for the roles we're hiring for (though not as actively across all roles at this time, but we'll keep you on file for when we are), check out thecareers page:D

❤️

Note

Learn about the developer behind Fluxer, the goals of the project, the tech stack, and what's coming next.

Read the launch blog post·View full roadmap

# Fluxer

Fluxer is afree and open source instant messaging and VoIP platformfor friends, groups, and communities. Self-host it and every feature is unlocked.

## Quick links

* Self-hosting guide
* Documentation
* Donate to support development
* Security

## Features

Real-time messaging– typing indicators, reactions, and threaded replies.

Voice & video– calls in communities and DMs with screen sharing, powered by LiveKit.

Rich media– link previews, image and video attachments, and GIF search via KLIPY.

Communities and channels– text and voice channels organised into categories with granular permissions.

Custom expressions– upload custom emojis and stickers for your community.

Self-hostable– run your own instance with full control of your data and no vendor lock-in.

Note

Native mobile apps and federation are top priorities. If you'd like to support this work,donationsare greatly appreciated. You can also share feedback by emailingdevelopers@fluxer.app.

## Self-hosting

Note

New to Fluxer? Follow theself-hosting guidefor step-by-step setup instructions.

TBD

### Deployment helpers

* livekitctl– bootstrap a LiveKit SFU for voice and video

## Development

### Tech stack

* TypeScriptandNode.jsfor backend services
* Honoas the web framework for all HTTP services
* Erlang/OTPfor the real-time WebSocket gateway (message routing and presence)
* ReactandElectronfor the desktop and web client
* Rustcompiled to WebAssembly for performance-critical client code
* SQLitefor storage by default, with optionalCassandrafor distributed deployments
* Meilisearchfor full-text search and indexing
* Valkey(Redis-compatible) for caching, rate limiting, and ephemeral coordination
* LiveKitfor voice and video infrastructure

### Devenv development environment

Fluxer supports development throughdevenvonly. It provides a reproducible Nix environment and a single, declarative process manager for the dev stack.

1. Install Nix and devenv using thedevenv getting started guide.
2. Enter the environment:

devenv shell

If you use direnv, the repo includes a.envrcthat loads devenv automatically – rundirenv allowonce.

### Getting started

Start all services and the development server with:

devenv up

Open the instance in a browser at your dev server URL (e.g.http://localhost:48763/).

Emails sent during development (verification codes, notifications, etc.) are captured by a local Mailpit instance. Access the inbox at your dev server URL +/mailpit/(e.g.http://localhost:48763/mailpit/).

### Voice on a remote VM

If you develop on a remote VM behind Cloudflare Tunnels (or a similar HTTP-only tunnel), voice and video won't work out of the box. Cloudflare Tunnels only proxy HTTP/WebSocket traffic, so WebRTC media transport needs a direct path to the server. Open these ports on the VM's firewall:

Port

Protocol

Purpose

3478

UDP

TURN/STUN

7881

TCP

ICE-TCP fallback

50000-50100

UDP

RTP/RTCP media

The bootstrap script configures LiveKit automatically based ondomain.base_domainin yourconfig.json. When set to a non-localhost domain, it enables external IP discovery so clients can connect directly for media while signaling continues through the tunnel.

### Devcontainer (experimental)

There is experimental support for developing in aVS Code Dev Container/ GitHub Codespace without Nix. The.devcontainer/directory provides a Docker Compose setup with all required tooling and backing services.

#
 Inside the dev container, start all processes:

process-compose -f .devcontainer/process-compose.yml up

Open the app athttp://localhost:48763and the dev email inbox athttp://localhost:48763/mailpit/. Predefined VS Code debugging targets are available in.vscode/launch.json.

Warning

Bluesky OAuth is disabled in the devcontainer because it requires HTTPS. All other features work normally.

### Documentation

To develop the documentation site with live preview:

pnpm dev:docs

## Contributing

Fluxer isfree and open source softwarelicensed underAGPLv3. Contributions are welcome.

SeeCONTRIBUTING.mdfor development processes and how to propose changes, andCODE_OF_CONDUCT.mdfor community guidelines.

## Security

Report vulnerabilities atfluxer.app/security. Do not use public issues for security reports.

License

Copyright (c) 2026 Fluxer Contributors

Licensed under theGNU Affero General Public License v3:

Copyright (c) 2026 Fluxer Contributors

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see https://www.gnu.org/licenses/

SeeLICENSING.mdfor details on commercial licensing and the CLA.

## About

A free and open source instant messaging and VoIP platform built for friends, groups, and communities. Self-hosting and more activity in this repository is coming very soon! See the README.

fluxer.app

### Topics

 fluxer

 fluxerapp

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6.5k

 stars
 

### Watchers

86

 watching
 

### Forks

350

 forks
 

 Report repository

 

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://fluxer.app/donate

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript83.0%
* Erlang7.5%
* CSS5.4%
* MDX2.1%
* JavaScript0.7%
* Python0.4%
* Other0.9%