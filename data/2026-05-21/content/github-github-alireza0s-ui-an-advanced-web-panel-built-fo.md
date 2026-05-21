---
title: 'GitHub - alireza0/s-ui: An advanced Web Panel • Built for SagerNet/Sing-Box · GitHub'
url: https://github.com/alireza0/s-ui
site_name: github
content_file: github-github-alireza0s-ui-an-advanced-web-panel-built-fo
fetched_at: '2026-05-21T12:05:44.524342'
original_url: https://github.com/alireza0/s-ui
author: alireza0
description: An advanced Web Panel • Built for SagerNet/Sing-Box - alireza0/s-ui
---

alireza0

 

/

s-ui

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star8.9k

 
 
 
 
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

530 Commits
530 Commits
.github
.github
 
 
api
api
 
 
app
app
 
 
cmd
cmd
 
 
config
config
 
 
core
core
 
 
cronjob
cronjob
 
 
database
database
 
 
frontend @ a4b8816
frontend @ a4b8816
 
 
logger
logger
 
 
middleware
middleware
 
 
network
network
 
 
service
service
 
 
sub
sub
 
 
util
util
 
 
web
web
 
 
windows
windows
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.frontend-artifact
Dockerfile.frontend-artifact
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
docker-build-test.sh
docker-build-test.sh
 
 
docker-compose.yml
docker-compose.yml
 
 
entrypoint.sh
entrypoint.sh
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
main.go
main.go
 
 
runSUI.sh
runSUI.sh
 
 
s-ui.service
s-ui.service
 
 
s-ui.sh
s-ui.sh
 
 
View all files

## Repository files navigation

# S-UI

An Advanced Web Panel • Built on SagerNet/Sing-Box

Disclaimer:This project is only for personal learning and communication, please do not use it for illegal purposes, please do not use it in a production environment

If you think this project is helpful to you, you may wish to give a🌟

Want to contribute?SeeCONTRIBUTING.mdfor development setup, coding conventions, testing, and the pull request process.

## Quick Overview

Features

Enable?

Multi-Protocol

✔️

Multi-Language

✔️

Multi-Client/Inbound

✔️

Advanced Traffic Routing Interface

✔️

Client & Traffic & System Status

✔️

Subscription Link (link/json/clash + info)

✔️

Dark/Light Theme

✔️

API Interface

✔️

## Supported Platforms

Platform

Architecture

Status

Linux

amd64, arm64, armv7, armv6, armv5, 386, s390x

✅ Supported

Windows

amd64, 386, arm64

✅ Supported

macOS

amd64, arm64

🚧 Experimental

## Screenshots

Other UI Screenshots

## API Documentation

API-Documentation Wiki

## Default Installation Information

* Panel Port: 2095
* Panel Path: /app/
* Subscription Port: 2096
* Subscription Path: /sub/
* User/Password: admin

## Install & Upgrade to Latest Version

### Linux/macOS

bash 
<(
curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/master/install.sh
)

### Windows

1. Download the latest Windows release fromGitHub Releases
2. Extract the ZIP file
3. Runinstall-windows.batas Administrator
4. Follow the installation wizard

## Install legacy Version

Step 1:To install your desired legacy version, add the version to the end of the installation command. e.g., ver1.0.0:

VERSION=1.0.0 
&&
 bash 
<(
curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/
$VERSION
/install.sh
)
 
$VERSION

## Manual installation

### Linux/macOS

1. Get the latest version of S-UI based on your OS/Architecture from GitHub:https://github.com/alireza0/s-ui/releases/latest
2. OPTIONALGet the latest version ofs-ui.shhttps://raw.githubusercontent.com/alireza0/s-ui/master/s-ui.sh
3. OPTIONALCopys-ui.shto /usr/bin/ and runchmod +x /usr/bin/s-ui.
4. Extract s-ui tar.gz file to a directory of your choice and navigate to the directory where you extracted the tar.gz file.
5. Copy *.service files to /etc/systemd/system/ and runsystemctl daemon-reload.
6. Enable autostart and start S-UI service usingsystemctl enable s-ui --now
7. Start sing-box service usingsystemctl enable sing-box --now

### Windows

1. Get the latest Windows version from GitHub:https://github.com/alireza0/s-ui/releases/latest
2. Download the appropriate Windows package (e.g.,s-ui-windows-amd64.zip)
3. Extract the ZIP file to a directory of your choice
4. Runinstall-windows.batas Administrator
5. Follow the installation wizard
6. Access the panel athttp://localhost:2095/app

## Uninstall S-UI

sudo -i

systemctl disable s-ui --now

rm -f /etc/systemd/system/sing-box.service
systemctl daemon-reload

rm -fr /usr/local/s-ui
rm /usr/bin/s-ui

## Install using Docker

Click for details

### Usage

Step 1:Install Docker

curl -fsSL https://get.docker.com 
|
 sh

Step 2:Install S-UI

Docker compose method

mkdir s-ui 
&&
 
cd
 s-ui
wget -q https://raw.githubusercontent.com/alireza0/s-ui/master/docker-compose.yml
docker compose up -d

Use docker

mkdir s-ui 
&&
 
cd
 s-ui
docker run -itd \
 -p 2095:2095 -p 2096:2096 -p 443:443 -p 80:80 \
 -v 
$PWD
/db/:/app/db/ \
 -v 
$PWD
/cert/:/root/cert/ \
 --name s-ui --restart=unless-stopped \
 alireza7/s-ui:latest

Build your own image

git clone https://github.com/alireza0/s-ui
git submodule update --init --recursive
docker build -t s-ui 
.

## Manual run ( contribution )

Click for details

### Build and run whole project

./runSUI.sh

### Clone the repository

#
 clone repository

git clone https://github.com/alireza0/s-ui

#
 clone submodules

git submodule update --init --recursive

### - Frontend

Visits-ui-frontendfor frontend code

### - Backend

Please build frontend once before!

To build backend:

#
 remove old frontend compiled files

rm -fr web/html/
*

#
 apply new frontend compiled files

cp -R frontend/dist/ web/html/

#
 build

go build -o sui main.go

To run backend (from root folder of repository):

./sui

## Languages

* English
* Farsi
* Vietnamese
* Chinese (Simplified)
* Chinese (Traditional)
* Russian

## Features

* Supported protocols:General: Mixed, SOCKS, HTTP, HTTPS, Direct, Redirect, TProxyV2Ray based: VLESS, VMess, Trojan, ShadowsocksOther protocols: ShadowTLS, Hysteria, Hysteria2, Naive, TUIC
* General: Mixed, SOCKS, HTTP, HTTPS, Direct, Redirect, TProxy
* V2Ray based: VLESS, VMess, Trojan, Shadowsocks
* Other protocols: ShadowTLS, Hysteria, Hysteria2, Naive, TUIC
* Supports XTLS protocols
* An advanced interface for routing traffic, incorporating PROXY Protocol, External, and Transparent Proxy, SSL Certificate, and Port
* An advanced interface for inbound and outbound configuration
* Clients’ traffic cap and expiration date
* Displays online clients, inbounds and outbounds with traffic statistics, and system status monitoring
* Subscription service with ability to add external links and subscription
* HTTPS for secure access to the web panel and subscription service (self-provided domain + SSL certificate)
* Dark/Light theme

## Environment Variables

Click for details

### Usage

Variable

Type

Default

SUI_LOG_LEVEL

"debug"
 | 
"info"
 | 
"warn"
 | 
"error"

"info"

SUI_DEBUG

boolean

false

SUI_BIN_FOLDER

string

"bin"

SUI_DB_FOLDER

string

"db"

SINGBOX_API

string

-

## SSL Certificate

Click for details

### Certbot

snap install core
;
 snap refresh core
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot

certbot certonly --standalone --register-unsafely-without-email --non-interactive --agree-tos -d 
<
Your Domain Name
>

## Stargazers over Time

## About

An advanced Web Panel • Built for SagerNet/Sing-Box

t.me/XrayUI

### Topics

 shadowsocks

 trojan

 vmess

 vless

 hysteria

 tuic

 sing-box

 shadowtls

 hysteria2

 naive-proxy

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

8.9k

 stars
 

### Watchers

46

 watching
 

### Forks

1.5k

 forks
 

 Report repository

 

## Releases41

v1.4.2

 Latest

 

May 19, 2026

 

+ 40 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

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

* Go82.5%
* Shell10.7%
* Batchfile5.1%
* PowerShell1.3%
* Dockerfile0.4%