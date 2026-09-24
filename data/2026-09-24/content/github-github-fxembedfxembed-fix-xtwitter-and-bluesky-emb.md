---
title: 'GitHub - FxEmbed/FxEmbed: Fix X/Twitter and Bluesky embeds! Use multiple images, videos, polls, translations and more on Discord, Telegram and others · GitHub'
url: https://github.com/FxEmbed/FxEmbed
site_name: github
content_file: github-github-fxembedfxembed-fix-xtwitter-and-bluesky-emb
fetched_at: '2026-09-24T15:44:11.633407'
original_url: https://github.com/FxEmbed/FxEmbed
author: FxEmbed
description: Fix X/Twitter and Bluesky embeds! Use multiple images, videos, polls, translations and more on Discord, Telegram and others - FxEmbed/FxEmbed
---

FxEmbed

 

/

FxEmbed

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork247
* Star5.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,207 Commits
4,207 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
assets/
logos
assets/
logos
 
 
docs
docs
 
 
i18n
i18n
 
 
packages/
atmosphere
packages/
atmosphere
 
 
src
src
 
 
test
test
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
branding.example.json
branding.example.json
 
 
credentials.example.json
credentials.example.json
 
 
docker-compose.yml
docker-compose.yml
 
 
esbuild.config.mjs
esbuild.config.mjs
 
 
eslint.config.mjs
eslint.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
renovate.json
renovate.json
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.mts
vitest.config.mts
 
 
worker.js
worker.js
 
 
wrangler.example.toml
wrangler.example.toml
 
 
View all files

## Repository files navigation

# FxEmbed

## Home of FxTwitter, FixupX, and FxBluesky

### Embed videos, polls, quotes, translations, & more on Discord, Telegram, and others!

### twitter.com: Addfxbefore yourtwitter.comlink

### x.com: Addfixupbefore yourx.comlink

### bsky.app: Addfxbefore yourbsky.applink

## Documentation

## API Reference

## Self-Hosting Guide

## Docker

FxEmbed is a Cloudflare Worker, so the Docker image runs the local Workers runtime through Wrangler rather than starting a plain Node.js server. The image usesnode:24-bookworm-slimbecause Wrangler'sworkerdbinary is glibc-linked and does not run reliably on Alpine/musl.

Before building, copy and edit the local configuration files if you need custom domains, branding, or credentials:

cp .env.example .env
cp wrangler.example.toml wrangler.toml
cp branding.example.json branding.json

Build and run with Docker Compose:

docker compose up -d --build

The worker listens onhttp://localhost:8787. Because FxEmbed routes by theHostheader, test a specific realm like this:

curl -H 
"
Host: fxtwitter.com
"
 -H 
"
User-Agent: Discordbot/2.0
"
 
"
http://localhost:8787/user/status/123
"

You can also openhttp://localhost:8787/without aHostheader to see the local realm prefixes.

Environment variables from.envare bundled during the Docker build, so rebuild the image after changing domain lists or other build-time configuration:

docker compose up -d --build

Runtime secrets such asCREDENTIAL_KEYandEXCEPTION_DISCORD_WEBHOOKcan be supplied through your shell or Compose.envfile. Stop the service with:

docker compose down

Licensed under the permissive MIT license. Feel free to send a pull request!

## Star History

## Bugs or issues?

Feel free toopen an issue

## Additional Credits

MosaicMulti-image combiner byAntonio32Aand improved bySyfaro,Deer Spangle, anddangered wolf

Everyone else who has contributed to the main project!

## Disclaimer

Twitter, Tweet, and X are trademarks of X Corp. This project is not affiliated in any way with X Corp or Twitter.