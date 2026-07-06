---
title: 'GitHub - karakeep-app/karakeep: A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search · GitHub'
url: https://github.com/karakeep-app/karakeep
site_name: github
content_file: github-github-karakeep-appkarakeep-a-self-hostable-bookma
fetched_at: '2026-07-06T12:20:17.293311'
original_url: https://github.com/karakeep-app/karakeep
author: karakeep-app
description: A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search - karakeep-app/karakeep
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 karakeep-app

 

/

karakeep

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star26.7k

 
 
 
 
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

2,077 Commits
2,077 Commits
.claude
.claude
 
 
.github
.github
 
 
.husky
.husky
 
 
apps
apps
 
 
charts
charts
 
 
docker
docker
 
 
docs
docs
 
 
kubernetes
kubernetes
 
 
packages
packages
 
 
patches
patches
 
 
screenshots
screenshots
 
 
skills
skills
 
 
snapshots
snapshots
 
 
tooling
tooling
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.env.sample
.env.sample
 
 
.gitignore
.gitignore
 
 
.ignore
.ignore
 
 
.nvmrc
.nvmrc
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
karakeep-linux.sh
karakeep-linux.sh
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
start-dev.sh
start-dev.sh
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

Karakeep (previously Hoarder) is a self-hostable bookmark-everything app with a touch of AI for the data hoarders out there.

## Features

* 🔗 Bookmark links, take simple notes and store images and pdfs.
* ⬇️ Automatic fetching for link titles, descriptions and images.
* 📋 Sort your bookmarks into lists.
* 👥 Collaborate with others on the same list.
* 🔎 Full text search of all the content stored.
* ✨ LLM-based automatic tagging and summarization. With supports for local models using ollama!
* 🤖 LLM Agents (e.g. OpenClaw, Hermes) friendly with powerfulCLI, andofficial skills.
* ⚙️ Rule-based engine for customized management.
* 🎆 OCR for extracting text from images.
* 🔖Chrome plugin,Firefox addon, andSafari extensionfor quick bookmarking.
* 📱 AniOS app, and anAndroid app.
* 📰 Auto hoarding from RSS feeds.
* 🔌 REST API and multiple clients.
* 🌐 Multi-language support.
* 🖍️ Mark and store highlights from your hoarded content.
* 🗄️ Full page archival (usingmonolith) to protect against link rot.
* ▶️Auto video archiving usingyt-dlp.
* ☑️ Bulk actions support.
* 🔐 SSO support.
* 🌙 Dark mode support.
* 💾 Self-hosting first.
* ⬇️ Bookmark importers from Chrome, Pocket, Linkwarden, Omnivore, Tab Session Manager.
* 🔄 Automatic sync with browser bookmarks viafloccus.
* [Planned] Offline reading on mobile, semantic search across bookmarks, ...

⚠️This app is under heavy development.

## Documentation

* Installation
* Configuration
* Screenshots
* Security Considerations
* Development

## Demo

You can access the demo athttps://try.karakeep.app. Login with the following creds:

email: demo@karakeep.app
password: demodemo

The demo is seeded with some content, but it's in read-only mode to prevent abuse.

## About the name

The name Karakeep is inspired by the Arabic word "كراكيب" (karakeeb), a colloquial term commonly used to refer to miscellaneous clutter, odds and ends, or items that may seem disorganized but often hold personal value or hidden usefulness. It evokes the image of a messy drawer or forgotten box, full of stuff you can't quite throw away—because somehow, it matters (or more likely, because you're a hoarder!).

## Stack

* NextJSfor the web app. Using app router.
* Drizzlefor the database and its migrations.
* NextAuthfor authentication.
* tRPCfor client->server communication.
* Puppeteerfor crawling the bookmarks.
* OpenAIbecause AI is so hot right now.
* Meilisearchfor the full content search.

## Why did I build it?

I browse reddit, twitter and hackernews a lot from my phone. I frequently find interesting stuff (articles, tools, etc) that I'd like to bookmark and read later when I'm in front of a laptop. Typical read-it-later apps usecase. Initially, I was usingPocketfor that. Then I got into self-hosting and I wanted to self-host this usecase. I usedmemosfor those quick notes and I loved it but it was lacking some features that I found important for that usecase such as link previews and automatic tagging (more on that in the next section).

I'm a systems engineer in my day job (and have been for the past 7 years). I didn't want to get too detached from the web development world. I decided to build this app as a way to keep my hand dirty with web development, and at the same time, build something that I care about and use every day.

## Alternatives

* memos: I love memos. I have it running on my home server and it's one of my most used self-hosted apps. It doesn't, however, archive or preview the links shared in it. It's just that I dump a lot of links there and I'd have loved if I'd be able to figure which link is that by just looking at my timeline. Also, given the variety of things I dump there, I'd have loved if it does some sort of automatic tagging for what I save there. This is exactly the usecase that I'm trying to tackle with Karakeep.
* mymind: Mymind is the closest alternative to this project and from where I drew a lot of inspirations. It's a commercial product though.
* raindrop: A polished open source bookmark manager that supports links, images and files. It's not self-hostable though.
* Bookmark managers (mostly focused on bookmarking links):Pocket(Dead): Pocket is what hooked me into the whole idea of read-it-later apps. I used ita lot. However, I recently got into home-labbing and became obsessed with the idea of running my services in my home server. Karakeep is meant to be a self-hosting first app. Mozilla recently announced that it's shutting down pocket.Linkwarden: An open-source self-hostable bookmark manager that I ran for a bit in my homelab. It's focused mostly on links and supports collaborative collections.Wallabag: Wallabag is a well-established open source read-it-later app written in php.Shiori: Shiori is meant to be an open source pocket clone written in Go.
* Pocket(Dead): Pocket is what hooked me into the whole idea of read-it-later apps. I used ita lot. However, I recently got into home-labbing and became obsessed with the idea of running my services in my home server. Karakeep is meant to be a self-hosting first app. Mozilla recently announced that it's shutting down pocket.
* Linkwarden: An open-source self-hostable bookmark manager that I ran for a bit in my homelab. It's focused mostly on links and supports collaborative collections.
* Wallabag: Wallabag is a well-established open source read-it-later app written in php.
* Shiori: Shiori is meant to be an open source pocket clone written in Go.

## Translations

Karakeep uses Weblate for managing translations. If you want to help translate Karakeep, you can do sohere.

## Karakeep Cloud ☁️

If you're not comfortable with self-hosting, you can use our managed Karakeep cloud atcloud.karakeep.app. Cloud subscriptions support the development of Karakeep.

## Support

If you're enjoying using Karakeep, drop a ⭐️ on the repo!

## Community Channels

* Join us onDiscord.
* Follow us on Twitter:@karakeep_app.

## License

Karakeep is licensed underAGPL-3.0and owned byLocalhost Labs Ltd.

## Star History

## About

A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search

karakeep.app

### Topics

 react-native

 nextjs

 bookmarks

 self-hosted

 read-it-later

 bookmarks-manager

 bookmark-manager

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
 

Custom properties
 

### Stars

26.7k

 stars
 

### Watchers

75

 watching
 

### Forks

1.3k

 forks
 

 Report repository

 

## Releases49

0.32.0

 Latest

 

May 8, 2026

 

+ 48 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/mbassem

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript98.6%
* Shell0.5%
* JavaScript0.3%
* Astro0.2%
* Dockerfile0.2%
* CSS0.1%
* Other0.1%