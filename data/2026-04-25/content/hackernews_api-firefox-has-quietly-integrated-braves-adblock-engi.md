---
title: Firefox Has Quietly Integrated Brave's Adblock Engine
url: https://itsfoss.com/news/firefox-ships-brave-adblock-engine/
site_name: hackernews_api
content_file: hackernews_api-firefox-has-quietly-integrated-braves-adblock-engi
fetched_at: '2026-04-25T11:37:25.108139'
original_url: https://itsfoss.com/news/firefox-ships-brave-adblock-engine/
author: nreece
date: '2026-04-25'
published_date: '2026-04-24T11:12:27.000Z'
description: Mozilla shipped it in Firefox 149 without a mention in the release notes.
tags:
- hackernews
- trending
---

# Firefox Has Quietly Integrated Brave's Adblock Engine

Mozilla shipped it in Firefox 149 without a mention in the release notes.

 

 

 

 

 

Sourav Rudra

24 Apr 2026

3 min read

On this page

 

Back in March,Firefox 149was released with many changes, like a free built-in VPN, aSplit Viewthat allows the loading of two pages side by side, and the XDG portal file picker as the new default on Linux.

However, an interesting addition had gone mostly unnoticed until now.

## Firefox has Some Brave in it now

Shivan Kaul Sahib, the VP of Privacy and Security atBrave, has put outa blog postabout something that didn't make it into the Firefox 149 release notes at all. The browser now shipsadblock-rust,Brave's open source Rust-based ad and tracker blocking engine.

The change landed via BugzillaBug 2013888, which was filed and handled by Mozilla engineerBenjamin VanderSloot. The bug is titled "Add a prototype rich content blocking engine," and keeps the engine disabled by default with no user interface or filter lists included.

For informational purposes,adblock-rustis the engine behind Brave's native content blocker (aka ad blocker). It is written inRustand licensed underMPL-2.0, handling network request blocking, cosmetic filtering, and features auBlock Origin-compatible filter list syntax.

Shivan also mentions thatWaterfox, the popular Firefox fork,has adopted adblock-rust, building directly upon Firefox's own implementation.

## Want to test it?

Before starting, head toEnhanced Tracking Protection's shield icon in the address bar and turn it off for the website you will be testing this with. This way, adblock-rust is doing the work, not Firefox's existing feature.

🚧
I suggest testing this experimental feature on a throwaway installation of Firefox.

Now open a new tab and go toabout:config. Accept the warning when it shows up. Search forprivacy.trackingprotection.content.protection.enabledand set it to "true" by clicking on the toggle. 👇

Next, search forprivacy.trackingprotection.content.protection.test_list_urls, click on the "Edit" button, and paste the following value to add theEasyListandEasyPrivacyfilter lists to Firefox:

https://easylist.to/easylist/easylist.txt|https://easylist.to/easylist/easyprivacy.txt

Remember to click on the blue-colored "Save" button before moving on.

Left: advertisement shown; Right: advertisement blocked

Now visit a site with known ads, likeYahoo(as I did above). If it's working, ad slots will still render in the page layout, but the actual ad content will be blocked. In my test, the banner on Yahoo came up showing only the text "Advertisement" with the advert bit stripped out.

Support independent Linux journalism! If you think we are doing a good job at helping people use Linux on their personal computers, support us by opting for Plus membership.Here's what you get with It's FOSS Plus membership:

✅ 5 Free eBooks on Linux, Docker and Bash✅ Ad-free reading experience✅ Badges in the comment section and forum✅ Support creation of educational Linux materials

 Join It's FOSS Plus
 

News

About the author

 

## Sourav Rudra

A nerd with a passion for open source software, custom PC builds, motorsports, and exploring the endless possibilities of this world.