---
title: Self-Hosting on the Dark Web | David Álvarez Rosa
url: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/
site_name: hackernews_api
content_file: hackernews_api-self-hosting-on-the-dark-web-david-álvarez-rosa
fetched_at: '2026-09-28T18:26:04.915061'
original_url: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/
author: mooreds
date: '2026-09-27'
published_date: '2026-06-01T10:55:00+01:00'
description: This site is now reachable over Tor as a hidden service, at a .onion address that resolves only inside the Tor network. Tor relays and encrypts your traffic as …
tags:
- hackernews
- trending
---

This site is now reachable over Tor as a hidden service, at a.onionaddress that resolves only inside the Tor network.11Open it in theTor Browser. There is no certificate authority, no DNS, and no exposed
IP—the address is derived directly from a public key, and the
connection is end-to-end encrypted by Tor itself.Torrelays and
encrypts your traffic as it passes through thousands of volunteer-run
servers, so that no single party can link who you are to what you are
doing; a hidden service extends that anonymity to the server itself.

It’s built by the nonprofitTor Project, which advances human rights and
freedoms through free software and open networks, so that anyone can use
the internet free from tracking, surveillance, and censorship. The
network only works because people use it, so considersupporting themor
running a relay—your contribution helps millions stay safe and private
online every day.

## The hidden service§

Install Tor and point a hidden service at a local port. Edit/etc/tor/torrc

HiddenServiceDir /var/lib/tor/blog/

HiddenServicePort 80 127.0.0.1:8080

The directory must be a dedicated, Tor-owned path—not your web
root.22Tor stores the service’s private key andhostnamefile here
and insists on owning it (chmod 700, userdebian-tor). Point it at
your site files and Tor refuses to start.Restart Tor and read the
address it generates

$ sudo systemctl restart tor@default

$ sudo cat /var/lib/tor/blog/hostname

dhevt6e4rtgbtr3jh53xrpwmgtilkah6nyjujocsspssrsexc7omxhid.onion

## Serving the site§

Tor forwards the onion’s port 80 to127.0.0.1:8080, so the web server
just needs to listen there. Add an nginx server block for it—no TLS,
no HTTP/2, no QUIC, since Tor speaks plain TCP and provides its own
encryption.

server
 
{

 
listen
 
127.0.0.1
:
8080
;

 
server_name
 
dhevt6e4rtgbtr3jh53xrpwmgtilkah6nyjujocsspssrsexc7omxhid.onion
;

 
root
 
/srv/tor.david.alvarezrosa.com
;

 
index
 
index.html
;

 
error_page
 
404
 
/404/index.html
;

 
location
 
/
 
{

 
try_files
 
$uri
 
$uri/
 
=
404
;

 
}

}

Reload nginx and the site is live on Tor.

## Building for the onion§

A static site bakes its base URL into absolute links, so a clearnet
build would point visitors back to the clearnet domain even when served
over Tor. The fix is to build a second copy with the onion as its base
URL

$ hugo --minify --baseURL
=
"http://dhevt6e4rtgbtr3jh53xrpwmgtilkah6nyjujocsspssrsexc7omxhid.onion/"

The deploy pipeline does this automatically: every push builds the site
once per target—clearnet and Tor—and rsyncs each to its own web
root, so the two stay in sync without any manual work.33SeeFirst
Steps on a New Serverfor the underlying machine; the full configuration
lives in myhomelabrepository, and thesite’s own repositoryholds the
GitHub Actions workflow that builds and deploys the Tor copy.

That’s it. Read this site over Tor atdhevt6e4rtgbtr3jh53xrpwmgtilkah6nyjujocsspssrsexc7omxhid.onion.

## Read Next§

September 21, 2026self-hostingSelf-Hosting Behind CGNATLibre software, libre hardware, and my mother's basement.

May 17, 2026self-hostingFirst Steps on a New ServerA personal checklist for settling into a fresh machine.

August 27, 2026c++·performanceOptimizing a Spin-LockSqueezing every pico out of the simplest lock.

## Subscribe§

My mailing list is free, occasional, and covers a variety of topics.
I will never sell or share your email address.

Subscribe

Have feedback? Email me atdavid@alvarezrosa.com.