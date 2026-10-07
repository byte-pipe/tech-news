---
title: Your GitHub README Isn't a Profile. It's a Storefront. (Here Are the 5 Rules I Used - DEV Community
url: https://dev.to/akhourianmolkumar/your-github-readme-isnt-a-profile-its-a-storefront-here-are-the-5-rules-i-used-57jm
site_name: devto
content_file: devto-your-github-readme-isnt-a-profile-its-a-storefront
fetched_at: '2026-10-07T23:28:44.837297'
original_url: https://dev.to/akhourianmolkumar/your-github-readme-isnt-a-profile-its-a-storefront-here-are-the-5-rules-i-used-57jm
author: Akhouri Anmol Kumar
date: '2026-10-06'
description: 'Description: "I stopped decorating my GitHub profile and started shipping it like a product page.... Tagged with github, design, webdev, showdev.'
tags: '#showdev, #github, #design, #webdev'
---

Features four ready-to-download desktop apps

Description: "I stopped decorating my GitHub profile and started shipping it like a product page. Four apps, four download buttons, zero widgets."

I [stopped / spent a weekend] treating my GitHub profile like a résumé and started treating it like aproduct page.

Now a stranger lands on it and can download one of my four appsbefore they finish reading my name.

👉Live:github.com/Akhouri-Anmol-Kumar

Credit: the spark to push my profile past badges came fromGiorgi Kobaidze's cyberpunk-console post. Go read it.

## The problem with every "awesome" profile

Open ten popular profile READMEs. You'll see the same things:

* a wall of badges
* a stats card that shows commit counts
* a "Hi 👋 I'm ___" line
* a snake eating your contribution graph

They're decorations. None of them answer the question every visitor has in the first three seconds:

### "What can I get from this person, right now?"

I build desktop apps:ATLOCK, APIC, ANOTE and ACALCU. So I asked myself a different question:

What if my README worked like an app store listing?

## The 5 Rules of a Storefront README

### Rule 1: The 3-Second Download Test

If someone can't download your best work within 3 seconds of landing, the page has failed.

So each of my apps gets its own card, anddirectly under every card is a download buttonthat points to the actual.ziprelease. There's no "see releases" and no hunting.

<td
 
align=
"center"
>

 
<a
 
href=
"https://github.com/USER/APP"
>

 
<img
 
src=
"assets/app_card.svg"
 
width=
"408"
 
alt=
"APP"
>

 
</a><br>

 
<a
 
href=
"https://github.com/USER/APP/releases/download/TAG/APP.zip"
>

 
<img
 
src=
"https://img.shields.io/badge/⬇%20DOWNLOAD%20APP-B8935F?style=for-the-badge&labelColor=8a6c3f&logo=windows&logoColor=white"
 
height=
"38"
>

 
</a>

</td>

Enter fullscreen mode

Exit fullscreen mode

Card on top, action underneath. It's the same pattern as a store listing.

### Rule 2: Pick one metal and never leave it

Mine isgold:#B8935Ffor the light tone and#8a6c3ffor the shadow.

The ring-light logo, the section headers, the buttons and the card edges all use it. Because every element shares one palette, the page looks designed rather than assembled.

Badges look cheap because they're every color at once.

### Rule 3: One width, everywhere

Every full-width image on my profile is830px. That's the entire layout system.

Nothing is slightly wider or narrower than its neighbour, so the page reads as one column instead of a pile of widgets. The app cards are 408px, which is two cards plus a gutter inside that same 830.

If you only copy one rule from this post, copy this one.

### Rule 4: Name your sections like paths

My headers aren't "About Me" and "Projects". They are:

~/links
~/apps
~/status
~/stack

Enter fullscreen mode

Exit fullscreen mode

It costs nothing, and it tells a developer in half a second that the person behind the page lives in a terminal. It also makes the page scannable, because every header looks the same and sits in the same place.

### Rule 5: Make your manifesto a design element, not a paragraph

Right in the middle of the page I put one banner:

Zero telemetry. Zero cloud. Zero subscriptions. Zero ads.

It isn't a bio line. It's the whole product philosophy, rendered as a full-width image. And the page closes with one sentence:

Your machine. Your data. Your control.

Visitors don't remember bullet lists. They remember a line they could repeat.

## The "no widgets" decision

I made one hard choice:every visual on my page lives in my own repo.

No stat cards from someone else's server. No streak counters that go blank when a free service sleeps. No images that vanish when a third party changes a URL.

My cards, headers, hero and footer are all SVGs in/assets, and the only outside piece is the download badge. (If I ever need to remove even that, I can swap in my own SVG.)

Two details that matter:

* I use absoluteraw.githubusercontent.comURLs for images, so the README still renders if it's copied, mirrored or previewed somewhere else.
* Everything has alt text, including the manifesto banner, so the page works for screen readers and for people whose images fail to load.

## The structure at a glance

[ ring-light logo ]
[ hero: whoami ]
[ ~/links → Website · Blog · LinkedIn · Peerlist · Instagram ]
[ ~/apps → 2×2 grid of cards, each with a DOWNLOAD button ]
[ ~/status → ZERO telemetry banner ]
[ ~/stack → tech stack ]
[ footer → "Your machine. Your data. Your control." ]

Enter fullscreen mode

Exit fullscreen mode

Only six sections and one action per app. Nothing on the page is there just to fill space.

Here's the challenge.Your profile has one job. Find it, then make that job a button.

* Selling apps? Put a download button under each one.
* A writer? Put your three best posts as cards.
* A library author? Putnpm i your-libas the hero.

Thendrop your link in the commentsand tell me the one action your page is built around. I'll read every one.

Stop decorating your profile and start shipping it. 🚀

I'm Anmol, and I build privacy-first desktop software at Akhouri Systems.🌐Website· 💼LinkedIn· 🔒ATLOCK

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (45 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse