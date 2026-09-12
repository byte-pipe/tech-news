---
title: Make Your First Edit to OpenStreetMap in the Next 15 Minutes | Website Wizard JOSM Plugin
url: https://high5apps.github.io/josm-plugin-website-wizard/
site_name: hackernews_api
content_file: hackernews_api-make-your-first-edit-to-openstreetmap-in-the-next
fetched_at: '2026-09-12T21:12:34.650266'
original_url: https://high5apps.github.io/josm-plugin-website-wizard/
author: juliantigler
date: '2026-09-12'
description: Website Wizard JOSM Plugin
tags:
- hackernews
- trending
---

## Intro

This quick tutorial will help you make a meaningful contribution toOpenStreetMap(OSM) in less than 15 minutes. By the end, you will have added an officialwebsitetagto a nearby shop or amenity. Soon after, your contribution will be ingested into dozens of freeOSM-based services, helping people worldwide.

Why awebsitetag? Once a place in OSM has awebsitetag, it becomes way easier to determine other helpful info about that place. Nearly every place’s official website has info about itsphone,opening_hours,email, andother tags. So adding awebsitetag is a great place to get started.

Got your stopwatch out? Ready, set, go!

## 1. Create an OSM account

Sign upfor a free OSM account and then confirm your email.

## 2. Download and Run JOSM

Download JOSM(~365 MB) for your specific operating system and then run it.

JOSM, the Java OSM editor app, is a powerful tool for querying and editing OSM data. While simpler in-browser editors exist, JOSM offerspluginsthat make your edit as quick and easy as possible.

## 3. Download OSM Data

1. PressCtrl+Shift+↓(or⌘+Shift+↓on Mac) to open theDownloaddialog
2. Determine your area of interest (AOI). It should be somewhere you’re familiar with, no larger than a few city blocks.
3. Locate your AOI on the map. You can pan the map withctrl+clickdragging and zoom in by scrolling.
4. Click and drag to create a box around your AOI
5. Click⬇️ Download. If this fails, your AOI was probably too large. Choose a smaller AOI and try again.

## 4. Filter Irrelevant OSM Data

Now we’ll filter the OSM data to only show shops and amenities that don’t have a website.

1. Find theFilterpanel on the right side of the screen
2. Click the+icon to open the Filter dialog
3. Copy/paste the following query into theSearch stringtext fieldname=* ((amenity=* "addr:housenumber"=*) | shop=*) -website=* -"contact:website"=*
4. ClickSubmit filter
5. CheckE, uncheckH, and checkIin the Filter panel. You should now only see the relevant places in your AOI.

## 5. Set Up the Website Wizard Plugin

1. PressF12(or⌘+,on Mac) to open JOSM’sPreferencesdialog
2. Click the🧩 puzzle pieceicon on the left side to open thePluginsconfig
3. Click⬇️ Download list
4. Scroll down the list of plugins until you see🌐 WebsiteWizard
5. Check its checkbox
6. ClickOKto install it

## 6. Search for an Official Website

1. Click the 🌐 icon on the left side of the screen to show the🌐 Website Wizardpanel on the right side of the screen
2. Type your AOI’s city and/or neighborhood into Website Wizard’sSearch Prefixtext field
3. Click a shop or amenity in your AOI
4. ClickSearchto openDuckDuckGoin your default browser with the query autofilled as the Search Prefix + the place’s name
5. Determine if any of the search results represent theofficialwebsite for your place. Do NOT use search results for social media profiles, review sites, or other business aggregators. When in doubt, don’t use it. If you don’t find one, just repeat steps 3 to 5 with another place in your AOI.
6. Copy/paste theofficialwebsite URL into theWebsite URLtext field
7. ClickSave. If you make a mistake, you can always pressctrl+z(⌘+zon Mac) to undo it.

## 7. Upload Your Changeset

1. PressCtrl+Shift+↑(or⌘+Shift+↑on Mac) to open theUploaddialog
2. TypeAdd website to <city and/or neighborhood> shops and amenitiesin the text field labeledProvide a brief comment…
3. Selectsurveyin the dropdown labeledSpecify the data source…
4. ClickUpload Changes, which will open OSM in your browser
5. Enter your OSM credentials
6. ClickLog In
7. ClickAuthorizeto allow JOSM to create the changeset for you

## Conclusion

🎉🎊🥳 Congratulations- you just made OSM a little bit better for everyone! Plus you got a preview of some of the cool things you can do with JOSM and OSM data.

So what next?

You could keep going and add awebsitetag to every place in your AOI. For example, I quickly added 66 newwebsitetags in Seattle’s Wallingford neighborhood inthis changeset.

Or you could modify the filter to show places in your AOI with awebsitetag but nophonetag. Then you could add thephonetag based on info from the website.

Or you could spread the word about OSM and Website Wizard! The United States alone has more than 1 million shops. So if we want to put them all on the map, we’ll need to get many more people to help.

No matter what’s next, feel proud for pushing OSM a little closer toward becoming the world’s greatest map!