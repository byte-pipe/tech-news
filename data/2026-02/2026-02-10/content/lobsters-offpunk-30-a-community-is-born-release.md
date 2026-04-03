---
title: Offpunk 3.0 "A Community is Born" Release
url: https://ploum.net/2026-02-09-offpunk3.html
site_name: lobsters
content_file: lobsters-offpunk-30-a-community-is-born-release
fetched_at: '2026-02-10T11:02:00.454080'
original_url: https://ploum.net/2026-02-09-offpunk3.html
date: '2026-02-10'
description: Offpunk 3.0
tags: show, browsers
---

# Offpunk 3.0 "A Community is Born" Release

byPloumon 2026-02-09

For the last four years, I’ve been developing Offpunk, a command-line Web, Gemini, and Gopher browser that allows you to work offline. And I’ve just released version 3.0. It is probably not for everyone, but I use it every single day. I like it, and it seems I’m not alone!

* Offpunk, the offline-first command-line browser

Something wonderful happened on the road leading to 3.0: Offpunk became a true cooperative effort. Offpunk 3.0 is probably the first release that contains code I didn’t review line-by-line. Umerdify (by Vincent Jousse), all the translation infrastructure (by the always-present JMCS), and the community packaging effort are areas for which I barely touched the code.

So, before anything else, I want to thank all the people involved for sharing their energy and motivation. I’m very grateful for every contribution the project received. I’m also really happy to see "old names" replying from time to time on the mailing list. It makes me feel like there’s an emerging Offpunk community where everybody can contribute at their own pace.

There were a lot of changes between 2.8 and 3.0, which probably means some new bugs and some regressions. We count on you, yes, you!, to report them and make 3.1 a lot more stable. It’s as easy at typing "bugreport" in offpunk!

From the deepest of my terminal, thank you!

But enough with the cheering, let’s jump to…

## The 11 most important changes in Offpunk 3.0

* Instructions to install Offpunk
* Dowload Offpunk 3.0

### 0. Use Offpunk in your language.

Offpunk is now translatable and has been translated into Spanish, Galician, and Dutch. Step-in to translate Offpunk into your language! (awesome work by JMCS with the help of Bert Livens)

* How to help translating Offpunk (offpunk.net)

### 1. Openk as a standalone tool

"opnk" standalone tool has been renamed to "openk" to make it more obvious. Openk is a command-line tool that tries to open any file in the terminal and, if not possible, opens it in your preferred software, falling back to xdg-open as a last resort.

People using opnk directly should change it everywhere. Users not using "opnk" in their terminal are not affected.

### 2. See XKCD comics in your terminal

"xkcdpunk" is a new standalone tool that allows displaying XKCD comics directly in your terminal.

XKCDpunk in action

### 3. Get only the good part and remove cruft for thousands of websites

Offpunk now integrates "unmerdify," a library written by Vincent Jousse that extracts the content of HTML articles using the "ftr-site-config" set of rules maintained by the FiveFilters community.

* Unmerdify on Codeberg

You can contribute by creating or improving rules for your frequently visited websites.

* Site Patterns | FiveFilters.org Docs (help.fivefilters.org)
* fivefilters/ftr-site-config: Site-specific article extraction rules to aid content extractors, feed readers, and 'read later' applications. (github.com)

If no ftr rule is found, Offpunk falls back to "readability," as has been the case since 0.1. "info" will tell you if unmerdify or readability was used to display the content of a page.

To use umerdify, users should manually clone the ftr-site-config repository:git clone https://github.com/fivefilters/ftr-site-config.gitThen, in their offpunkrc:

set ftr_site_config /path/to/ftr-site-config

Automating this step is an objective for 3.1

### 4. Offpunk goes social with "share" and "reply"

New social functions: "share" to send the URL of a page by email and "reply" to reply to the author if an email is found. "Reply" will remember the email used for each site/capsule/hole.

### 5. Browse websites while logged in

Offpunk doesn’t support login into websites. But the new "cookies" command allows you to import a cookie txt file to be used with a given http domain.

From your traditional browser (Firefox, Librewolf, Chromium, … ), log into the website. Then export the cookie with the "cookie-txt" extension. Once you have this "mycookie.txt" text file, launch Offpunk and run:

cookies import mycookie.txt https://domain-of-the-cookie.net/

This allows you, for example, to read LWN.NET if you have a subscription. (contributed by Urja)

### 6. Bigger, better images, even in Gemini

Images are now displayed by default in gemini and their display size has been increased.

Gemini capsule of Thierry Crouzet displayed in Offpunk

This can be reverted with the following lines in offpunkrc:

set images_size 40
set gemini_images false

Remember that images are displayed as "blocks" when reading a page but if you access the image URL directly (by following the yellow link beneath), the image will be displayed perfectly if you are using a sixels-compatible terminal.

### 7. Display hidden RSS/Atom links

If available, links to hidden RSS/Atom feeds are now displayed at the bottom of HTML pages.

This makes the "feed" command a lot less useful and allows you to quickly discover interesting new feeds.

### 8. Display blocked links

Links to blocked domains are now displayed in red by default.

A blocked link to X on standblog.org

This can be reverted with the following lines in offpunkrc:

theme blocked_link none

### 9. Preset themes

Support for multiple themes with "theme preset." Existing themes are "offpunk1" (default), "cyan," "yellow" and "bw." Don’t hesitate to contribute yours!

### 10. Better redirects and true blocks

"redirects" now operate on the netcache level. This means that no requests to blocked URLs should ever be made (which was still happening before)

## And many changes, improvements and bugfixes

- "root" is now smarter and goes to the root of a website, not the domain.Old behaviour can still be achieved with "root /"- "ls" command is deprecated and has been replaced by "links"- new "websearch" command configured to use wiby.me by default- "set default_cmd" allows you to configure what Offpunk will do when pressing enter on an empty command line. By default, it is "links 10."- "view switch" allows you to switch between normal and full view (contributed by Andrew Fowlie)- "help help" will allow you to send an email to the offpunk-users mailing list- "bugreport" will send a bug report to the offpunk-devel mailing list- And, of course, multiple bugfixes…

* Come and join the Offpunk community!

### About the author

I’mPloum, a writer and an engineer. I like to explore how technology impacts society. You can subscribeby emailorby rss. I value privacy and never share your adress.

I writescience-fiction novels in French. ForBikepunk, my new post-apocalyptic-cyclist book, my publisher is looking for contacts in other countries to distribute it in languages other than French. If you can help,contact me!
