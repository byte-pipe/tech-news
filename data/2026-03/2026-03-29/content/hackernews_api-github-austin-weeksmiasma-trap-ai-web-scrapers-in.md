---
title: 'GitHub - austin-weeks/miasma: Trap AI web scrapers in an endless poison pit. · GitHub'
url: https://github.com/austin-weeks/miasma
site_name: hackernews_api
content_file: hackernews_api-github-austin-weeksmiasma-trap-ai-web-scrapers-in
fetched_at: '2026-03-29T19:15:57.515337'
original_url: https://github.com/austin-weeks/miasma
author: LucidLynx
date: '2026-03-29'
description: Trap AI web scrapers in an endless poison pit. Contribute to austin-weeks/miasma development by creating an account on GitHub.
tags:
- hackernews
- trending
---

austin-weeks

 

/

miasma

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3
* Star323

 
 
 
 
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

49 Commits
49 Commits
.github
.github
 
 
src
src
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# 🌀 Miasma

AI companies continually scrape the internet at an enormous scale, swallowing up all of its contents to use as training data for their next models. If you have a public website,they are already stealing your work.

Miasmais here to help you fight back! Spin up the server and point any malicious traffic towards it.Miasmawill send poisoned training data from thepoison fountainalongside multiple self-referential links. It's an endless buffet of slop for the slop machines.

Miasmais very fast and has a minimal memory footprint - you should not have to waste compute resources fending off the internet's leeches.

## Installation

Install withcargo(recommended):

cargo install miasma

Or, download a pre-built binary fromreleases.

## Quick Start

StartMiasmawith default configuration:

miasma

View all availableconfiguration options:

miasma --help

## How to Trap Scrapers

Let's walk through an example of setting up a server to trap scrapers withMiasma. We'll pick/botsas our server's path to direct scraper traffic. We'll be usingNginxas our server's reverse proxy, but the same result can be achieved with many different setups.

When we're done, scrapers will be trapped like so:

### Embedding Hidden Links

Within our site, we'll include a few hidden links leading to/bots.

<
a
 
href
="
/bots
" 
style
="
display: none;
" 
aria-hidden
="
true
" 
tabindex
="
1
"
>

 Amazing high quality data here!

</
a
>

Thestyle="display: none;",aria-hidden="true", andtabindex="1"attributes ensure links are totally invisible to human visitors and will be ignored by screen readers and keyboard navigation. They willonlybe visible to scrapers.

### Configuring our Nginx Proxy

Since our hidden links point to/bots, we'll configure this path to proxyMiasma. Let's assume we're runningMiasmaon port9855.

location
 
~
 ^/bots
(
$|/.*
)
$ 
{

 
proxy_pass
 
http
://localhost:
9855
;

}

This will match all variations of the/botspath ->/bots,/bots/,/bots/12345, etc.

### RunMiasma

Lastly, we'll startMiasmaand specify/botsas the link prefix. This instructsMiasmato start links with/bots/, which ensures scrapers are properly routed through ourNginxproxy back toMiasma.

We'll also limit the number of max in-flight connections to 50. At 50 connections, we can expect 50-60 MB peak memory usage. Note that any requests exceeding this limit will immediately receive a429response rather than being added to a queue.

miasma --link-prefix 
'
/bots
'
 -p 9855 -c 50

### Enjoy!

Let's deploy and watch as multi-billion dollar companies greedily eat from our endless slop machine!

### robots.txt

Be sure to protect friendly bots and search engines fromMiasmain yourrobots.txt!

User-agent: Googlebot
User-agent: Bingbot
User-agent: DuckDuckBot
User-agent: Slurp
User-agent: SomeOtherNiceBot
Disallow: /bots
Allow: /

## Configuration

Miasmacan be configured via its CLI options:

Option

Default

Description

port

9999

The port the server should bind to.

host

localhost

The host address the server should bind to.

max-in-flight

500

Maximum number of allowable in-flight requests. Requests received when in flight is exceeded will receive a 
429
 response. 
Miasma's
 memory usage scales directly with the number of in-flight requests - set this to a lower value if memory usage is a concern.

link-prefix

/

Prefix for self-directing links. This should be the path where you host 
Miasma
, e.g. 
/bots
.

link-count

5

Number of self-directing links to include in each response page.

force-gzip

false

Always gzip responses regardless of the client's 
Accept-Encoding
 header. 
Forcing compression can help reduce egress costs.

poison-source

https://rnsaffn.com/poison2/

Proxy source for poisoned training data.

## Development

Contributions are welcome! Please open anissuefor bugs reports or feature requests. Primarily AI-generated contributions will be automatically rejected.

## About

Trap AI web scrapers in an endless poison pit.

### Topics

 ai

 free-software

 web-scraping

 anti-spam

 anti-ai

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

323

 stars
 

### Watchers

1

 watching
 

### Forks

3

 forks
 

 Report repository

 

## Releases3

v0.1.18

 Latest

 

Mar 29, 2026

 

+ 2 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* ko-fi.com/austinweeks

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* austin-weeksAustin Weeks

## Languages

* Rust96.7%
* HTML3.3%