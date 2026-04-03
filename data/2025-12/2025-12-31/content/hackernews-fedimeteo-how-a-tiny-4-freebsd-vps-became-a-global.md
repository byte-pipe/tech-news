---
title: 'FediMeteo: How a Tiny €4 FreeBSD VPS Became a Global Weather Service for Thousands - IT Notes'
url: https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/
site_name: hackernews
fetched_at: '2025-12-31T11:07:12.423868'
original_url: https://it-notes.dragas.net/2025/02/26/fedimeteo-how-a-tiny-freebsd-vps-became-a-global-weather-service-for-thousands/
author: Stefano Marinelli
date: '2025-12-31'
description: How a simple idea turned into an international weather service on the Fediverse.
---

## Personal Introduction

Weather has always significantly influenced my life. When I was a young athlete, knowing the forecast in advance would have allowed me to better plan my training sessions. As I grew older, I could choose whether to go to school on my motorcycle or, for safety reasons, have my grandfather drive me. And it was him, my grandfather, who was my go-to meteorologist. He followed all weather patterns and forecasts, a remnant of his childhood in the countryside and his life on the move. It's to him that I dedicateFediMeteo.

The idea forFediMeteostarted almost by chance while I was checking the holiday weather forecast to plan an outing. Suddenly, I thought how nice it would be to receive regular weather updates for my city directly in my timeline. After reflecting for a few minutes, I registered a domain and started planning.

## Design Principles

The choice of operating system was almost automatic. The idea was to separate instances by country, and FreeBSD jails are one of the most useful tools for this purpose.

I initially thought the project would generate little interest. I was wrong. After all, weather affects many of our lives, directly or indirectly. So I decided to structure everything in this way:

* I would use a test VPS to see how things would go. The VPSwas a small VM on a German provider with 4 shared cores, 4GB of RAM, 120GB of SSD disk space, and a 1Gbit/sec internet connectionand now is a 4 euro per month VPS in Milano, Italy - 4 shared cores, 8 GB RAM and 75GB disk space.
* I would separate various countries into different instances, for both management and security reasons, as well as to have the possibility of relocating just some of them if needed.
* Weather data would come from a reliable and open-source friendly source. I narrowed it down to two options:wttr.inandOpen-Meteo, two solutions I know and that have always given me reliable results.
* I would pay close attention to accessibility: forecasts would be in local languages, consultable via text browsers, with emojis to give an idea even to those who don't speak local languages, and everything would be accessible without JavaScript or other requirements. One's mother tongue is always more "familiar" than a second language, even if you're fluent.
* I would manage everything according to Unix philosophy: small pieces working together. The more years pass, the more I understand how valuable this approach is.
* The software chosen to manage the instances issnac. Snac embodies my philosophy of minimal and effective software, perfect for this purpose. It provides clear web pages for those who want to consult via the web, "speaks" the ActivityPub protocol perfectly, produces RSS feeds for each user (i.e., city), has extremely low RAM and CPU consumption, compiles in seconds, and is stable. The developer is an extremely helpful and positive person, and in my opinion, this carries equal weight as everything else.
* I would do it for myself. If there was no interest, I would have kept it running anyway, without expanding it. So no anxiety or fear of failure.

## Technical Implementation

I started setting up the first "pieces" during the days around Christmas 2024. The scheme was clear: each jail would handle everything internally. A Python script would download data, city by city, and produce markdown. The city coordinates would be calculated via thegeopylibrary and passed towttr.inandOpen-Meteo. No data would be stored locally. This approach gives the ability to process all cities together. Just pass the city and country to the script, and the markdown would be served. At that point, snac comes into play: without the need to use external utilities, the "snac note" command allows posting from stdin by specifying the instance directory and the user to post from. No need to make API calls with external utilities, having to manage API keys, permissions, etc.

### Setting Up for Italy

To simplify things, I first structured the jail for Italy. I made a list of the main cities, normalizing them. For example, La Spezia became la_spezia. Forlì, with an accent, became forli - this for maximum compatibility since each city would be a snac user. I then created a script that takes this list and creates snac users via "snac adduser." At that point, after creating all the users, the script would modify the JSON of each user to convert the city name to uppercase, insert the bio (a standard text), activate the "bot" flag, and set the avatar, which was the same for all users at the time. This script is also able to add a new city: just run the script with the (normalized) name of the city, and it will add it - also adding it to the "cities.txt" file, so it will be updated in the next weather update cycle.

### Core Application Development

I then created the heart of the service. A Python application (initially only in Italian, then multilingual, separating the operational part from the text) able to receive (via command line) the name of a city and a country code (corresponding to the file with texts in the local language). The script determines the coordinates and then, using API calls, requests the current weather conditions, those for the next 12 hours, and the next 7 days. I conducted experiments with both wttr.in and Open-Meteo, and both gave good results. However, I settled on Open-Meteo because, for my uses, it has always provided very reliable results. This application directly provides an output in Markdown since snac supports it, at least partially.

The cities.txt file is also crucial for updates. I created a script - post.sh, in pure sh, that scrolls through all cities, and for each one, launches the FediMeteo application and publishes its output using snac directly via command line. Once the job is finished, it makes a call to my instance ofUptime-Kuma, which keeps an eye on the situation. In case of failure, the monitoring will alert me that there have been no recent updates, and I can check.

At this point, the system cron takes care of launching post.sh every 6 hours. The requests are serialized, so the cities will update one at a time, and the posts will be sent to followers.

## Growth and Unexpected Success

After listing all Italian provincial capitals, I started testing everything. It worked perfectly. Of course, I had to make some adjustments at all levels. For example, one of the problems encountered was that snac did not set the language of the posts, and some users could have missed them. The developer was very quick and, as soon as I exposed the problem, immediately modified the program so that the post could keep the system language, set as an environment variable in the sh script.

After two days, I decided to start adding other countries and announce the project. And the announcement was unexpectedly well received: there were many boosts, and people started asking me to add their cities or countries. I tried to do what I could, within the limits of my physical condition, as in those days, I had the flu that kept me at home with a fever and illness for several days. I started adding many countries in the heart of Europe, translating the main indications into local languages but maintaining emojis so that everything would be understandable even to those who don't speak the local language. There were some small problems reported by some users. One of them: not all weather conditions had been translated, so sometimes they appeared in Italian - as well as errors. In bilingual countries, I tried to include all local languages. Sometimes, unfortunately, making mistakes as I encountered dynamics unknown to me or difficult to interpret. For example, in Ireland, forecasts were published in Irish, but it was pointed out to me that not everyone speaks it, so I modified and published in English.

### A Turning Point

The turning point was when FediFollows (@FediFollows@social.growyourown.services- who also manages the siteFedi Directory) started publishing the list of countries and cities, highlighting the project. Many people became aware of FediMeteo and started following the various accounts, the various cities. And from here came requests to add new countries and some new information, such as wind speed. Moreover, I was asked (rightly, to avoid flooding timelines) to publish posts as unlisted - this way, followers would see the posts, but they wouldn't fill local timelines. Snac didn't support this, but again, the snac dev came to my rescue in a few hours.

## Scaling Challenges

But with new countries came new challenges. For example, in my original implementation, all units of measurement were in metric/decimal/Celsius - and this doesn't adapt well to realities like the USA. Moreover, focusing on Europe, almost all countries were located in a single timezone, while for larger countries (such as Australia, USA, Canada, etc.), this is totally different. So I started developing a more complete and global version and, in the meantime, added almost all of Europe. The new version would have to be backward compatible, would have to take into account timezone differences for each city, different measurements (e.g., degrees C and F), as well as, initially more difficult part, being able to separate cities with the same name based on states or provinces. I had already seen a similar problem with the implementation of support for Germany, so it had to be addressed properly.

The original goal was to have a VPS for each continent, but I soon realized that thanks to the quality of snac's code and FreeBSD's efficient management, even keeping countries in separate jails, the load didn't increase much. So I decided to challenge myself and the limits of the economical 4 euros per month VPS. That is, to insert as much as possible until seeing what the limits were. Limits that, to date, I have not yet reached. I would also soon exhaust the available API calls for Open-Meteo's free accounts, so I tried to contact the team and explain everything. I was positively surprised to read that they appreciated the project and provided me with a dedicated API key.

Compatible with my free time, I managed to complete the richer and more complete version of my Python program. I'm not a professional dev, I'm more oriented towards systems, so the code is probably quite poor in the eyes of an expert dev. But, in the end, it just needs to take an input and give me an output. It's not a daemon, it's not a service that responds on the network. For that, snac takes care of it.

## Expansion to North America

So I decided to start with a very important launch: the USA and Canada. A non-trivial part was identifying the main cities in order to cover, state by state, all the territory. In the end, I identified more than 1200 cities. A number that, by itself, exceeded the sum of all other countries (at that time). And the program, now, is able to take an input with a separator (two underscores: __) between city and state. In this way, it's possible to perfectly understand the differences between city and state: new_york__new_york is an example I like to make, but there are many.

The launch of the USA was interesting: despite having had many previous requests, the reception was initially quite lukewarm, to my extreme surprise. The number of followers in Canada, in a few hours, far exceeded that of the USA. On the contrary, the country with the most followers (in a few days, more than 1000) was Germany. Followed by the UK - which I expected would have been the first.

## System Performance

The VPS held up well. Except for the moments when FediFollows launched (after fixing some FreeBSD tuning, the service slowed slightly but didn't crash), the load remained extremely low. So I continued to expand: Japan, Australia, New Zealand, etc.

## Current Status

At the time of the last update of this article (30 December 2025), the supported countries are 38: Argentina, Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, India, Ireland, Italy, Japan, Latvia, Lithuania, Malta, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, Taiwan, the United Kingdom, and the United States of America (with more regions coming soon!).

Direct followers in the Fediverse are around 7,707 and growing daily, excluding those who follow hashtags or cities via RSS, whose number I can't estimate. However, a quick look at the logs suggests there are many more.

The cities currently covered are 2937 - growing based on new countries and requests.

## Challenges Encountered

There have been some problems. The most serious, by my fault, was the API key leak: I had left a debug code active and, the first time Open-Meteo had problems, the error message also included the API call - including the API key. Some users reported it to me (others just mocked) and I fixed the code and immediately reported everything to the Open-Meteo team, who kindly gave me a new API Key and deactivated the old one.

A further problem was related to geopy. It makes a call to Nominatim to determine coordinates. One of the times Nominatim didn't respond, my program wasn't able to determine the position and went into error. I solved this by introducing coordinate caching: now the program, the first time it encounters a city, requests and saves the coordinates. If present, they will be used in the future without making a new request via geopy. This is both lighter on their servers and faster and safer for us.

## Infrastructure Details

And the VPS? It has no problems and is surprisingly fast and effective. FreeBSD 14.3-RELEASE, BastilleBSD to manage the jails. Currently, there are 39 jails - one for haproxy, theFediMeteo website, so nginx, and the snac instance forFediMeteo announcements and support- the other 38 for the individual instances. Each of them, therefore, has its autonomous ZFS dataset. Every 15 minutes, there is a local snapshot of all datasets. Every hour, the homepage is regenerated: a small script calculates the number of followers (counting, instance by instance, the followers of individual cities, since I don't publish except in aggregate to avoid possible triangulations and privacy leaks of users). Every hour, moreover, an external backup is made viazfs-autobackup(on encrypted at rest dataset), and once a day, a further backup is made in my datacenter, on disks encrypted with geli. The occupied RAM is 501 MB (yes, exactly: 501 MB), which rises slightly when updates are in progress. Updates normally occur every 6 hours. I have tried, as much as possible, to space them out to avoid overloads in timelines (or on the server itself). Only for the USA, I added a sleep of 5 seconds between one city and another, to give snac the opportunity to better organize the sending of messages. It probably wouldn't be necessary, with the current numbers, but better safe than sorry. In this way, the USA is processed in about 2 and a half hours, but the other jails (thus countries) can work autonomously and send their updates.

The average load of the VPS (taking as reference both the last 24 hours and the last two weeks) is about 25%, as it rises to 70/75% when updates occur for larger instances (such as the USA), or when it is announced by FediFollows. Otherwise, it is on average less than 10%. So, the VPS still has huge margin, and new instances, with new nations, will still be inside it.

## Conclusion

This article, although in some parts very conversational, aims to demonstrate how it's possible to build solid, valid, and efficient solutions without the need to use expensive and complex services. Moreover, this is the demonstration of how it's possible to have your online presence without the need to put your data in the hands of third parties or without necessarily having to resort to complex stacks. Sometimes, less is more.

The success of this project demonstrates, once again, that my grandfather was right: weather forecasts interest everyone. He worried about my health and, thanks to his concerns, we spent time together. In the same way, I see many followers and friends talking to me or among themselves about the weather, their experiences, what happens. Again, in my life, weather forecasts have helped sociality and socialization.

Thank you, Grandpa.
