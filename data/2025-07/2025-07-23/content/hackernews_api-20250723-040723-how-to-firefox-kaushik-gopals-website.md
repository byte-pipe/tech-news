---
title: 🦊 How to Firefox - Kaushik Gopal's Website
url: https://kau.sh/blog/how-to-firefox/
site_name: hackernews_api
fetched_at: '2025-07-23T04:07:23.454553'
original_url: https://kau.sh/blog/how-to-firefox/
author: Kaushik Gopal
date: '2025-07-22'
description: Chrome finally pulled the trigger on the web’s best ad-blocker, uBlock Origin. Now that Chrome has hobbled uBO, Firefox—my beloved—1 is surging again. I want to do my part to convince you to switch to Firefox and show you how I use it.
tags:
- hackernews
- trending
---

Chrome finally pulled the trigger on the web’s best ad-blocker,uBlock Origin.

Now that Chrome has hobbled uBO, Firefox—my beloved—1is surging again. I want to do my part to convince you to switch to Firefox and show you how I use it.

# Why Firefox

Let’s get through the important talking points, in case you need a quick copy paste to convince a friend.

1. 100% open-source
2. Un-enshittify the web
3. Android users rejoice
4. Customize to your heart’s content

## 100% open-source

This section can be quick.

Here’s agithub linkto the source code of the Firefox browser. You can clone the repo, pop open your favoriteAIcode assistant and start asking questions about your browser - the most important app you use.

What libraries does their Android app use?libs.versions.tomlboom! Also 8.11.1 on android gradle plugin? not bad Firefox.

Their license allows you to fork and distributealternativeversions. Vibe code a whole new browser.

## Un-enshittify the web

Most of the web today isenshittifiedwith a cesspool of ads, popups, cookie notices, and tracking scripts. Our primary defense has been ad-blockers, with the most powerful being uBlock Origin.

uBO relies on community-curated filter lists that play a cat-and-mouse game to zap known ads, trackers, and other digital sludge. But with Chrome controlling the web, Google followed through on itspromiseto kneecapuBOwith Manifest V3, effectively blocking the full version from its extension store.

Sure, there’s uBlock Origin “Lite” now, which does the same thing, right?Nope:


 uBlock Origin Lite != uBlock Origin



* Filter lists update only when the extension updatesno fetching up to date lists from servers (this is a big one!)
* no fetching up to date lists from servers (this is a big one!)
* No custom filtersso noelement pickerwhich allows you to point and zap
* so noelement pickerwhich allows you to point and zap
* Many filters are dropped at conversion time due to MV3’s limited filter syntax
* No strict-blocked pages
* No per-site switches
* No dynamic filtering
* No importing external lists

Did you know,uBlock Origin works best on Firefox. Why not just use the real thing then? My browsing experience is beautiful because I have most of the shit-bits blocked away.

On my Pixel too.

## Android users rejoice

With Firefox for Android, you get seamless sync of tabs, bookmarks, passwords between browser and phone2. Let’s face it, Safari between Mac and iPhone is a sublime experience. We can get that with Firefox.

### Real browser extensions for mobile

Here’s something the iPhone isn’t getting anytime soon: honest-to-god browser extensions that you use on your desktop, also on your phone. Which means… you can run uBlock Origin on Android, completelyunnerfed.

Safari has extensions, but they still require an App Store review for distribution on Apple platforms. They alsojustgot a version of the uBO “Lite” extension.

## Customize to your heart’s content

But… Firefox doesn’t look as clean and minimal as Safari. You can claw the vertical tabs out of my cold dead Arc hands!

This is what my Firefox browser looks like:




 well akkva's of gwfox-css technically



It only takes about five minutes and a browser restart to get this look.

# My Firefox Setup

I’ll walk you through my setup now, from essential add-ons to privacy tweaks and a few “nice-to-have” extras.


 Nerd Alert



This ismysetup. I’m a nerd, so I find joy in tinkering. You don’t need to do all of this, but a few small tweaks can give you a massively better browser.

## The Essentials: uBlock Origin

Think of uBO as a powerful, wide-spectrum filter for the web. It uses community-maintained lists to block ads, trackers, cookie notices, and other digital sludge before it ever loads. Your browser stays faster and cleaner.

It can be confusing to know which filter lists to enable. I follow the advice of a uBOwizard on Reddit, and these settings alone make the web 90% better. Check the same boxes, and you’re good to go.




 You're completely set with this.











 Custom Filters are an exclusive uBO superpower



The “My filters” tab is where you can write your own rules to block nearly anything, from annoying widgets to entire domains.

#### Blockoutgoingnetwork traffic to Facebook

For the truly privacy-conscious, uBO can blockall outgoing trafficto specific domains, like Facebook.3In the past, Firefox’sFacebook Containeradd-on helped by isolating your Facebook activity. But if any other site embedded a Facebook widget or tracker, your data could still leak to Meta’s servers, fingerprinting you even if you never visit Facebook directly.

With a custom uBO rule, you can sever that connection entirely from non-Facebook sites. This is a level of control other browsers don’t offer.




 uBO custom filter: courtesy the reddit wizard fsau again



The other line you see there? That one-liner blocks all those “Sign in with Google?” pop-ups. This granular control isonlypossible with the full uBlock Origin, not the “Lite” version found on other browsers.

If you want to go deeper,this videois a great showcase of its advanced capabilities.

## Privacy power-up: Containers

Firefox now includesTotal Cookie Protectionby default. This automatically isolates cookies to the site that created them, giving each site its own “cookie jar”. This stops trackers from following you across the web.

This feature makes the oldMulti-Account Containers(MAC) add-on redundant for basic anti-tracking. However, the container technology itself is still incredibly useful for managing multiple online identities.

Instead of juggling separate browser profiles, you can use “Containers” to stay logged into two different Gmail accounts (e.g., “Work” and “Personal”) in the same browser window, with zero overlap.

The old MAC add-on made this possible, but it was clunky to setup. For a seamless setup, you just need oneabout:configtweak: setprivacy.userContext.newTabContainerOnLeftClick.enabledtotrue. Now, when you click the new tab button, you can choose which container to open. This works without the extra MAC add-on because the Container concept is baked natively into Firefox.

But what about links? A work link (like Datadog or Sentry) clicked from your email in a Work container, might open in the default container and use the wrong Google account. You could right click and say “Open in Container >” but that gets old fast. The optionalContaineriseadd-on solves this by letting you create simple rules that force specific sites to always open in their designated container.

This combination of a native config tweak and theContaineriseadd-on provides a simple, but more powerful multi-profile setup (than even MAC).

## Gravy add-ons

These are also not essential, but they add a nice layer of polish.

* Dark Reader: For a consistent, customizable dark mode on every site.
* Stylus: To apply custom CSS. I use it to force myfavorite monospace fonton code blocks.
* Return YouTube Dislike: Does what it says on the tin.
* Obsidian Web Clipper: To save notes and clippings directly to Obsidian, from desktop or mobile.
* Auto Tab Discard: Suspends background tabs to save RAM. A holdover from my RAM-strapped MacBook days, but it still does its job silently.

## Other Customizations

Firefox is famously customizable viaabout:config. Besides the container tweak, I only use one other:

### browser.tabs.insertAfterCurrent→true

* New tabs open next to your current tab, not at the end.
* You catch thatMr.Gruber?

## Hidden Gems

I’m collecting in this section, some of the cooler Firefox features that’ll make you wonder why every browser doesn’t have them:

* Type/and start typing for quick find (vs ⌘F). But dig this,'and Firefox will only match text for hyper links4
* If you have an obnoxious site disable right click, just hold Shift and Firefox will bypass and show it to you. No add-one required.
* URL bar search shortcuts:*for bookmarks,%for open tabs,^for history

The web can still be beautiful. You just need the right tools to see it. Godownload Firefoxand make your web beautiful again.

If you try this setup or have suggestion, let me know in the comments.

1. No, goddammit, AI didn’t write this post.↩︎
2. For the few who have reached this point of the article and furiously questioned why I don’t just use Zen browser or Libre.↩︎
3. You can of course send outgoing traffic from Meta owned websites so Threads etc. still work.↩︎
4. Seriously, try the apostrophe trick. It’s a game-changer for keyboard navigation.↩︎
