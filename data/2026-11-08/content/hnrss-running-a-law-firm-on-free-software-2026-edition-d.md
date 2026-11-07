---
title: Running a law firm on Free software (2026 edition) | decoded.legal's blog
url: https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/
site_name: hnrss
content_file: hnrss-running-a-law-firm-on-free-software-2026-edition-d
fetched_at: '2026-11-08T09:03:23.094711'
original_url: https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/
date: '2026-11-07'
tags:
- hackernews
- hnrss
---

# Running a law firm on Free software (2026 edition)

Published on:2026-11-06 12:18:47byNeil Brown

I started running decoded.legal - a small English law firm, focussing
on Internet, telecoms, and tech law - on Free software, both client and
server side, around five years ago. I have used Free software in my
personal life for a lot longer than that.

Back in 2022,I
wrote about my experiences after the first year or so.

I wrotean
update in 2024.

Someone asked me recently what I am doing now, and, while it is
mostly the same, some bits have changed. So here is the 2026 update.

## Client-side stuff

I am still using Debian, with GNOME, and it works well for me.

I’m using iton
a ThinkPad X1 Yoga Gen 6, as my primary machine, and, being a “Yoga”
version, I rather like being able to fold the screen back and write on
it to mark up documents. (Here
are my thoughts on the different “Active Pens” available for
it.)

However, the machine itself seems to have a hardware problem with the
Thunderbolt / USB-C ports (fine for power, very flaky for data), and so
I might need to replace it. And I havenoidea what laptop I
might get.

* Email (MUA):Thunderbirdandmutt, depending on what I am doingQuick Folder Move and Move Message And Yourself are particularly
useful add-ons for Thunderbird, for rapid filing of email with keyboard
shortcutsThunderbird seems to be having a problem with some recurring
calendar invitations, whileikhalis handling them fine.
I’ve not dug into it, but it is a nuisance.
* Quick Folder Move and Move Message And Yourself are particularly
useful add-ons for Thunderbird, for rapid filing of email with keyboard
shortcuts
* Thunderbird seems to be having a problem with some recurring
calendar invitations, whileikhalis handling them fine.
I’ve not dug into it, but it is a nuisance.
* Document production:LibreOffice’s Writerif I
want a “Word” document (e.g. I am exchanging documents with other
lawyers), and I amusingpandocandtypstto convert
Markdown files that I tend to write invimfor some
other bits. I’d like to exploretexat some point, as I
have a client who likes diffs to their .tex files, and that looks rather
neat.
* Presentations:reveal.jsI absolutely love this.I have a bash script which sets up a template for a new
presentation, and then I just write the presentation using Markdown. I
get a nicely-formatted presentation (using a css template) with very
little effort, and no distracting GUIBlogpost
about reveal.jsHere are some
presentations I’ve given, using reveal.js
* I absolutely love this.
* I have a bash script which sets up a template for a new
presentation, and then I just write the presentation using Markdown. I
get a nicely-formatted presentation (using a css template) with very
little effort, and no distracting GUI
* Blogpost
about reveal.js
* Here are some
presentations I’ve given, using reveal.js
* File manager:NautilusMainly because it is GNOME’s default, although, especially whencombined
with some useful bash scripts, it works well for my needs
* Mainly because it is GNOME’s default, although, especially whencombined
with some useful bash scripts, it works well for my needs
* PDFs:evincefor most reading;Xournal++for marking up PDFs;PDFarrangerandpdftkfor interfering
with PDFs
* Text expansion:espansoThis is a fantastic shortcut for me, saving me from typing the same
thing multiple times. I have loads of shortcuts set up, and I’d be lost
without them.
* This is a fantastic shortcut for me, saving me from typing the same
thing multiple times. I have loads of shortcuts set up, and I’d be lost
without them.
* Browser:FirefoxorlinksI am still using Firefox. It is … fine? I should probably look at
LibreWolf or another fork, as I’m not enamoured by Mozilla’s direction
of travel but, for now, Firefox it is.I use Firefox for joining people’s Teams and Zoom etc. meetings, if
someone else sets up the meeting, and that works fine
* I am still using Firefox. It is … fine? I should probably look at
LibreWolf or another fork, as I’m not enamoured by Mozilla’s direction
of travel but, for now, Firefox it is.
* I use Firefox for joining people’s Teams and Zoom etc. meetings, if
someone else sets up the meeting, and that works fine
* Local wiki / knowledge management:vimwikibecause I use vim so much,vimwikiwas quite an obvious
choice.I use this for keeping track of my professional development, and for
various notes
* because I use vim so much,vimwikiwas quite an obvious
choice.
* I use this for keeping track of my professional development, and for
various notes
* Disk encryption:LUKS
* Client-side encryption of files before syncing them withSyncthing:Cryptomator
* Fediverse: I tend to use theMastodonadvanced
web UI or, when I want fewer images, the TUItoot.I schedule toots - for example, about blogposts, usinga
simple bash script and a cron job; it has moved on a bit since I
wrote that post, but it is the same principle
* I schedule toots - for example, about blogposts, usinga
simple bash script and a cron job; it has moved on a bit since I
wrote that post, but it is the same principle
* Password manager:Bitwarden, using thevaultwardenserver, with YubiKeys for managing more
sensitive credentials
* Markdown editor (for blogposts; I do presentations in vim or
gedit):Apostrophe
* Scanning:paperless-ngx
* Label printing: there’s agreat
FOSS web UI for Brother (and perhaps other) label printers. I don’t
print many labels, as we aim to be paperless, but it’s convenient when I
need to do so

Why so many terminal-based tools? The simple answer is that I am very
comfortable in a terminal, and I like them. They have fewer distractions
and, when compared with most GUI software, are just - IMHO - easier to
use, especially when I don’t need to move my hands away from the
keyboard. So, while I don’t use them exclusively, I usemutt,vim,ikhal,ncmpcpp,newsboat,toot,links, and various other TUIs, frequently.

## Server-side stuff

Everything here - other than Signal - is self-hosted, and I’m mostly
using Intel NUCs now. I still have some Raspberry Pi devices, but fewer
than I did.

(Again, this doesn’t list everything; just the main
applications.)

* Email (MTA):postfix / dovecotI need to move our mail infrastructure at some point, and I want to
look at Stalwart.
* I need to move our mail infrastructure at some point, and I want to
look at Stalwart.
* File synchronisation:SyncthingOne of the bigger changes since last time was moving away from
Nextcloud. I just was not getting on with it, and it was causing me more
problems than it solved. So I switched to Syncthing for file sync, and
radicale for CalDAV / CardDAV. I’ve been more than happy with this
combination.
* One of the bigger changes since last time was moving away from
Nextcloud. I just was not getting on with it, and it was causing me more
problems than it solved. So I switched to Syncthing for file sync, and
radicale for CalDAV / CardDAV. I’ve been more than happy with this
combination.
* Video conferencing:SignalI ran jitsi for years, but stopped using it a few months back. Jitsi
is great, and I remain a fan, but most of the time I am joining other
people’s Teams or Zoom meetings, so I was running the Jitsi server for
very little usage. I turned it off, and instead offer Signal. I have had
no grumbles.
* I ran jitsi for years, but stopped using it a few months back. Jitsi
is great, and I remain a fan, but most of the time I am joining other
people’s Teams or Zoom meetings, so I was running the Jitsi server for
very little usage. I turned it off, and instead offer Signal. I have had
no grumbles.
* Invoicing and tracking payments:InvoicePlane,
just for generating PDF invoices. Clients don’t interact with
it
* Time tracking:Kimaiv2 of Kimai is excellent, and I had a very pleasant exchange with
the developer, which is always nice.
* v2 of Kimai is excellent, and I had a very pleasant exchange with
the developer, which is always nice.
* “Case management” / “Matter management”:EspoCRM
* VPN:WireGuard, using trailofbit’salgoansible scripts on one machine, andPiVPNon another (albeit not on a Pi)
* Vulnerability scanning:greenbone/OpenVAS
* Monitoring:Uptime KumaI implemented this not long after the last update. It … just
works?
* I implemented this not long after the last update. It … just
works?
* Forge / hosted git repository:ForgejoI use this for version tracking the website, and for a couple of
template projectsI do not host anything particularly important on it - for that, I
have a git process running on another machine, which is not accessible
over the Internet, and I just push to that
* I use this for version tracking the website, and for a couple of
template projects
* I do not host anything particularly important on it - for that, I
have a git process running on another machine, which is not accessible
over the Internet, and I just push to that
* SIEM:Wazuh
* Password manager:vaultwarden
* Website: it is a static site built viamkdocs,
hosted onapache2It got even simpler and even faster to load. Yes, it’s basic, but I
like it!We still havean
.onion version. If you visitdecoded.legalin Tor Browser, it should
re-direct your automatically
* It got even simpler and even faster to load. Yes, it’s basic, but I
like it!
* We still havean
.onion version. If you visitdecoded.legalin Tor Browser, it should
re-direct your automatically
* Blog:BSSGAfter a couple of annoyances with hugo, I moved to BSSG - a bash
static site generator. The developer, Stefano, is amazing, and it is
working incredibly well. I’ve gone for a very basic, easy to read, theme
- which should be very similar to what was there before - and there’s
still an RSS feed for it, of courseI blog quite frequently, and, rather than keep private / internal
“knowhow” files, I tend to just blog things and share the learningsI tend touse my personal blogfor posts about the more technical bits and piecesI have automated the most common actions - templates, and publishing
- using bash scripts, so that I can focus on writing (in Markdown);
getting it online is the easiest bit
* After a couple of annoyances with hugo, I moved to BSSG - a bash
static site generator. The developer, Stefano, is amazing, and it is
working incredibly well. I’ve gone for a very basic, easy to read, theme
- which should be very similar to what was there before - and there’s
still an RSS feed for it, of course
* I blog quite frequently, and, rather than keep private / internal
“knowhow” files, I tend to just blog things and share the learnings
* I tend touse my personal blogfor posts about the more technical bits and pieces
* I have automated the most common actions - templates, and publishing
- using bash scripts, so that I can focus on writing (in Markdown);
getting it online is the easiest bit
* Fediverse: I am using the *glitch-soc Mastodon** forkSwitching fromnormal
Mastodon to glitch-soc Mastodonwas easyI stopped using Markdown in toots, even though I like the rendered
output (i.e. as html not as markdown), but this is not supported
consistently well across clients, so I stopped using it.I turned off decoded.legal’s own fedi instance. I had been on the
fence as to whether this is worthwhile or not for a while, and decided
that, really, it was not.
* Switching fromnormal
Mastodon to glitch-soc Mastodonwas easy
* I stopped using Markdown in toots, even though I like the rendered
output (i.e. as html not as markdown), but this is not supported
consistently well across clients, so I stopped using it.
* I turned off decoded.legal’s own fedi instance. I had been on the
fence as to whether this is worthwhile or not for a while, and decided
that, really, it was not.
* Knowledge management, and managing our law firm’s (numerous)
policies and procedures:dokuwikiwith the Markdown
plugin
* DNS:unbound, withPi-Holein
front of itI used to run a doh server, but I’ve stopped doing that.
* I used to run a doh server, but I’ve stopped doing that.
* Backups:resticandrsyncNotes
on restic
* Notes
on restic
* Forms:LiberaFormsI have been really happy with LiberaForms, for easy-to-create and
easy-to-use forms, especially since they implemented encryption, so that
the form responses are stored encrypted on the server. I still delete
them as soon as I can, but knowing that they are encrypted in the
database is welcome.I use LiberaForms for our “Know Your Client” pre-engagement
questionnaire, and for various other bits
* I have been really happy with LiberaForms, for easy-to-create and
easy-to-use forms, especially since they implemented encryption, so that
the form responses are stored encrypted on the server. I still delete
them as soon as I can, but knowing that they are encrypted in the
database is welcome.
* I use LiberaForms for our “Know Your Client” pre-engagement
questionnaire, and for various other bits
* Collaborative document editing: I don’t.I used to run CryptPad, but it just didn’t get much use, so I turned
it off.
* I used to run CryptPad, but it just didn’t get much use, so I turned
it off.

## AI tools

None, for various reasons.

## Mobile device

I’m using a Pixel running GrapheneOS for my mobile device.

I use F-Droid as the main app store.

Using Android doesn’t thrill me, especially given Google’s direction
of travel, but at the moment - despite trying quite a lot of different
OSs and devices, including postmarketOS and Ubuntu Touch, as well as
SailfishOS previously - I have not found something that does what I need
better than GrapheneOS.

## Working with others
(who don’t use FOSS tools)

No change here: zero problems.

Many of my clients use Microsoft’s software, or Apple’s software.

 
Linux
 
tech
 
Debian
 
law firm
 
FOSS
 
Free software