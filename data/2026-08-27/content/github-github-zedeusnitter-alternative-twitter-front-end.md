---
title: 'GitHub - zedeus/nitter: Alternative Twitter front-end · GitHub'
url: https://github.com/zedeus/nitter
site_name: github
content_file: github-github-zedeusnitter-alternative-twitter-front-end
fetched_at: '2026-08-27T20:57:24.340849'
original_url: https://github.com/zedeus/nitter
author: zedeus
description: Alternative Twitter front-end. Contribute to zedeus/nitter development by creating an account on GitHub.
---

This repository was archived by the owner on Aug 26, 2026. It is now read-only.
 

 zedeus

 

/

nitter

Public archive

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star13.8k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,339 Commits
1,339 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
public
public
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.travis.yml
.travis.yml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
compose.yml
compose.yml
 
 
config.nims
config.nims
 
 
nitter.example.conf
nitter.example.conf
 
 
nitter.nimble
nitter.nimble
 
 
screenshot.png
screenshot.png
 
 
View all files

## Repository files navigation

# Nitter

Note

On 24 August 2026 cease and desist letters were sent by X Corp. demanding a permanent takedown of Nitter instances and the project's repository.

A free and open source alternative Twitter front-end focused on privacy and
performance.Inspired by theInvidiousproject.

## Donations

Liberapay:https://liberapay.com/zedeusPatreon:https://patreon.com/nitterKo-fi:https://ko-fi.com/zedeusBTC: bc1qpqpzjkcpgluhzf7x9yqe7jfe8gpfm5v08mdr55ETH: 0x24a0DB59A923B588c7A5EBd0dBDFDD1bCe9c4460XMR: 42hKayRoEAw4D6G6t8mQHPJHQcXqofjFuVfavqKeNMNUZfeJLJAcNU19i1bGdDvcdN6romiSscWGWJCczFLe9RFhM3d1zpLSOL: FF5bheiD5AqPEdc3eyjymJ8AoMRF1hS78Ht6FiSZZF1t$Nitter: 4fSxCKc91ELQYVdv3tmHW8R15KoALPwEngyoQe1XpumpZEC: u1vndfqtzyy6qkzhkapxelel7ams38wmfeccu3fdpy2wkuc4erxyjm8ncjhnyg747x6t0kf0faqhh2hxyplgaum08d2wnj4n7cyu9s6zhxkqw2aef4hgd4s6vh5hpqvfken98rg80kgtgn64ff70djy7s8f839z00hwhuzlcggvefhdlyszkvwy3c7yw623vw3rvar6q6evd3xcvveypt

## Features

* No JavaScript or ads
* All requests go through the backend, client never talks to Twitter
* Prevents Twitter from tracking your IP or JavaScript fingerprint
* Uses Twitter's unofficial API (no developer account required)
* Lightweight (for@nim_lang, 60KB vs 784KB from twitter.com)
* RSS feeds
* Themes
* Mobile support (responsive design)
* AGPLv3 licensed, no proprietary instances permitted

## Roadmap

* Embeds
* Account system with timeline support
* Archiving tweets/profiles
* Developer API

## Resources

The wiki containsa list of instancesandbrowser extensionsmaintained by the community.

## Why?

It's impossible to use Twitter without JavaScript enabled, and as of 2024 you
need to sign up. For privacy-minded folks, preventing JavaScript analytics and
IP-based tracking is important, but apart from using a VPN and uBlock/uMatrix,
it's impossible. Despite being behind a VPN and using heavy-duty adblockers,
you can get accurately tracked with yourbrowser's
fingerprint,no
JavaScript required. This all became
particularly important after Twitterremoved the
abilityfor users to control whether their data gets sent to advertisers.

Using an instance of Nitter (hosted on a VPS for example), you can browse
Twitter without JavaScript while retaining your privacy. In addition to
respecting your privacy, Nitter is on average around 15 times lighter than
Twitter, and in most cases serves pages faster (eg. timelines load 2-4x faster).

In the future a simple account system will be added that lets you follow Twitter
users, allowing you to have a clean chronological timeline without needing a
Twitter account.

## Screenshot

## Installation

### Dependencies

* libpcre
* libsass
* redis/valkey

To compile Nitter you need a Nim installation, seenim-lang.orgfor details. It is possible
to install it system-wide or in the user directory you create below.

To compile the scss files, you need to installlibsass. On Ubuntu and Debian,
you can uselibsass-dev.

Redis is required for caching and in the future for account info. As of 2024
Redis is no longer open source, so using the fork Valkey is recommended. It
should be available on most distros asredisorredis-server(Ubuntu/Debian), orvalkey/valkey-server. Running it with the default
config is fine, Nitter's default config is set to use the default port and
localhost.

Here's how to create anitteruser, clone the repo, and build the project
along with the scss and md files.

#
 useradd -m nitter

#
 su nitter

$ git clone https://github.com/zedeus/nitter
$ 
cd
 nitter
$ nimble -l build -d:danger --mm:refc
$ nimble -l scss
$ nimble -l md
$ cp nitter.example.conf nitter.conf

Set your hostname, port, HMAC key, https (must be correct for cookies), and
Redis info innitter.conf. To run Redis, either runredis-server --daemonize yes, orsystemctl enable --now redis(or
redis-server depending on the distro). Run Nitter by executing./nitteror
using the systemd service below. You should run Nitter behind a reverse proxy
such asNginxorApachefor security and
performance reasons.

### Docker

Page for the Docker image:https://hub.docker.com/r/zedeus/nitter

#### NOTE: The published image is multi-arch —zedeus/nitter:latestruns natively on bothamd64andarm64.

To run Nitter with Docker, you'll need to install and run Redis separately
before you can run the container. See below for how to also run Redis using
Docker.

First create your config file. The Docker commands mount it into the container,
so it has to exist on the host beforehand. If you've cloned the repo:

cp nitter.example.conf nitter.conf

If you're using the prebuilt image without a local clone, downloadnitter.example.confand save it asnitter.confinstead.

To build and run Nitter in Docker:

docker build -t nitter:latest 
.

docker run -v 
$(
pwd
)
/nitter.conf:/src/nitter.conf -d --network host nitter:latest

A prebuilt Docker image is provided as well:

docker run -v 
$(
pwd
)
/nitter.conf:/src/nitter.conf -d --network host zedeus/nitter:latest

Using docker-compose to run both Nitter and Redis as different containers:
ChangeredisHostfromlocalhosttonitter-redisinnitter.conf, then run:

docker-compose up -d

Note the Docker commands mountnitter.conf(andsessions.jsonlfor
docker-compose) from the directory you run them in. If a mounted file doesn't
exist, Docker silently creates a directory in its place and the container fails
withnot a directory: Are you trying to mount a directory onto a file. Remove
that directory and create the file as shown above.

### systemd

To run Nitter via systemd you can use this service file:

[Unit]

Description
=Nitter (An alternative Twitter front-end)

After
=syslog.target

After
=network.target

[Service]

Type
=simple

#
 set user and group

User
=nitter

Group
=nitter

#
 configure location

WorkingDirectory
=/home/nitter/nitter

ExecStart
=/home/nitter/nitter/nitter

Restart
=always

RestartSec
=15

[Install]

WantedBy
=multi-user.target

Then enable and run the service:systemctl enable --now nitter.service

### Logging

Nitter currently prints some errors to stdout, and there is no real logging
implemented. If you're running Nitter with systemd, you can check stdout like
this:journalctl -u nitter.service(add--followto see just the last 15
lines). If you're running the Docker image, you can do this:docker logs --follow *nitter container id*

## Contact

Feel free to join ourMatrix channel.
You can email me atzedeus@pm.meif you wish to contact me personally.

For legal inquiries, contactlegal@poast.org