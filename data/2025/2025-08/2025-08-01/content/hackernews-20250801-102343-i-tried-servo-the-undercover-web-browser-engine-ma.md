---
title: I tried Servo, the undercover web browser engine made with Rust
url: https://www.spacebar.news/servo-undercover-web-browser-engine/
site_name: hackernews
fetched_at: '2025-08-01T10:23:43.063451'
original_url: https://www.spacebar.news/servo-undercover-web-browser-engine/
author: robtherobber
date: '2025-08-01'
published_date: '2025-07-30T14:40:53.000Z'
description: Servo was supposed to be Firefox's future. Now it's an independent effort to make a fast and secure web browser engine.
---

"Everything is chrome in the future" was a linesaid by SpongeBob SquarePantsinan episode from 1999, and it turned out to be a prophecy about web browsers. Google Chrome is the world's most popular browser, and most of its competitors are based on the same Chromium code: Microsoft Edge, Vivaldi, Opera, Brave, and Arc, just to name a few. The main exceptions are Safari and Firefox.

It wasn't always this way. At the start of the millennium, Internet Explorer used its ownTridentengine on Windows andTasmanon Mac, Opera usedPresto, some embedded devices usedNetFront, Netscape hadGecko, and KDE madeKHTMLfor its Konqueror browser. Those browsers eventually faded away or adopted a competing engine to simplify development. KHTML was the basis for Safari's WebKit, which in turn became Chromium's Blink engine, and Netscape's Gecko engine became the foundation for Firefox. Operaditched its custom Presto enginein 2013 and switched to Chromium, and Microsoft Edgemade the same movein 2020.

This is a danger to the open web in more ways than one. If there is only one functioning implementation of a standard, the implementationbecomes the standard. The web becomes to Google what Java is to Oracle. It also means the limitations and security flaws in Chromium affect most other browsers, which became a topic of conversation withGoogle's recent Manifest V3 transition.

Thankfully, there is an alternative browser engine that could one day give Chrome, Safari, and Firefox a run for their money, and you'veprobablynever heard about it. It's calledServo.

## Hello, Servo

Servo's goal is to create a web rendering engine entirely in the Rust programming language, which is built aroundmulti-threaded operationsandmemory safety. The first one is important because modern CPUs are designed to split work across multiple cores or threads. The more rendering code you can move to parallel operations, the faster performance you get. The second part is important because it shrinks the potential for security vulnerabilities—Chromium developerssaidat one point that "around 70% of our serious security bugs are memory safety problems."

Servo is unique for a few other reasons, too. It's managed by theLinux Foundation Europewith decisions made by a technical steering committee, not a big tech company. One of the main goals is to be an "embeddable web rendering engine," meaning it's not just for browsers—it could be a replacement forElectronor theAndroid WebView. Servo is also the first completely new browser engine in decades, so it's taking lessons learned from mainstream browsers while building a new foundation.

There are no full-featured web browsers using Servo right now, but you can try it out with thenightly snapshotsfor Windows, macOS, Android, and Linux. Those builds are just the engine with a basic web browser interface around it. No data synchronization, bookmarks, extensions, or anything else.

Most sites have at least a few rendering bugs, and a few are completely broken. Google search results have many overlapping elements, and theMacRumorshome page crashed after some scrolling. Sites like Wikipedia,CNN Lite,my personal site, andtext-only NPRworked perfectly.

There are alsosome demo pageson the Servo website to show off the engine's graphical capabilities. The Dogemania test ran at a smooth 60 FPS on my M4 Pro MacBook Pro until reaching around 400 images, and the Particle Physics test averaged around 55 FPS. Safari 18.5 on the same computer could handle over 1,500 images on Dogemania and roughly 60 FPS on Particle Physics. Servo was running under x86 emulation since there are no ARM builds for macOS yet, so it wasn't acompletelyfair fight in performance.

I also tried the classicAcid3 test, which was created in 2008 to test various web browser standards—Internet Explorer famously had a failing grade until the IE 9 beta builds in late 2010pushed the score to 95/100. Most modern browsers get around 95 points, since some elements of the test are now broken, but Servo is a bit behind at 83/100.

Servo still has a long way to go for general browsing, but I'm impressed with it. Thecurrent roadmaplists Shadow DOM and CSS Grid as priorities, which should fix many rendering issues on popular websites, among other improvements.

Here's the plot twist: Servo was originally a Mozilla project. Development kicked off in 2012, andSamsung joined the effortin 2013. There wereplans to develop an Android browseror other application based around Servo, and once the technology was proven and stable, it could have potentially replaced Firefox's long-running Gecko engine.

Mozilla later decided to replace parts of Gecko in Firefox with Servo code, instead of waiting for the entire engine to be a drop-in replacement. Ablog post from 2017described it as "replacing a jet engine while the jet is still in flight." The first major component in Firefox to be replaced was the CSS engine, which finally rolled out with the release of Firefox 57. Mozilla nicknamed that updateFirefox Quantum, andbenchmarks showedthe browser was significantly faster and used less RAM.

The plan to slowly replace bits of Firefox's Gecko code seemed to be going well, untilMozilla laid off 250 employees in 2020, including many of the developers responsible for Servo development. It's still baffling to me that Mozilla threw out Firefox's technical future, to say nothing of the workers impacted by the layoffs. Five years later, Mozilla's side projects still aren'tworkingout, and the company has donemore rounds of layoffs.

The Servo projectreorganizedunder the Linux Foundation in November of that year, and later in 2023, it gained new backing fromIgaliaand other organizations while moving to Linux Foundation Europe. Servo got a second chance at life, and development isfairly active.

## A guessing game

The United States Department of Justice is currently wrapping up its legal action against Google, which alleged the company of holding a monopoly over search engines that was perpetuated by Chrome and Android's popularity. Google lost in court, andthe DOJ wants Googleto sell off the Chrome browser and stop making search engine deals with other browsers.

Mozilla isasking the case's judgetonotkill those deals, because Google's default search engine placement in Firefox is the vast majority of Mozilla's income. The company said it could have to "scale back operations and cut support for critical projects like Gecko, the only remaining browser engine competing with Google’s Chromium and Apple’s WebKit."

It's game theory time. Let's say Mozilla loses those Google paychecks, and Firefox switches to WebKit or Chromium/Blink to save on development costs. I'm pretty suresomeonewould try to fork the Gecko-based Firefox and keep it going outside of Mozilla—maybe the Linux Foundation, maybe someone else. If the Gecko engine comes under community ownership just like Servo, perhaps the original plan to slowly morph Gecko into Servo could be revived.

Alternatively, Gecko could just fade away. WebKit isalreadyestablishedin the Linux ecosystem, and the general population will probably continue using Chrome and Safari. It's fun to think about the possibilities, though.

No matter what happens to Firefox or Gecko, I'm excited to see where Servo goes next.
