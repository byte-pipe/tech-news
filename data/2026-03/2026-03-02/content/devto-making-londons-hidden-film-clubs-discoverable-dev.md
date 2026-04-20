---
title: Making London's hidden film clubs discoverable - DEV Community
url: https://dev.to/alistairjcbrown/i-built-a-film-club-discovery-tool-for-londons-cinema-community-2md
site_name: devto
content_file: devto-making-londons-hidden-film-clubs-discoverable-dev
fetched_at: '2026-03-02T08:25:14.247929'
original_url: https://dev.to/alistairjcbrown/i-built-a-film-club-discovery-tool-for-londons-cinema-community-2md
author: Alistair
date: '2026-03-01'
description: 'This is a submission for the DEV Weekend Challenge: Community The Community I''ve spent... Tagged with devchallenge, weekendchallenge, showdev.'
tags: '#showdev, #devchallenge, #weekendchallenge'
---

DEV Weekend Challenge: Community

This is a submission for theDEV Weekend Challenge: Community

## The Community

I've spent the last year buildingClusterflick— a site that pulls together cinema listings from across London so you can see everything showing, everywhere, without jumping between a dozen different websites. It started as a personal itch: I just wanted to know what was on (for the backstory,see my intro post)

But the more I used it, the more I realised I was only solving half the problem. I could tell youwhatwas showing atwhich venue— but I couldn't tell you if the screening was part of afilm club, whether the club screenings were accessible, or even that the club existed at all. London has a genuinely brilliant film club scene: community cinemas, genre nights, archive screenings, disability-led clubs. Most of them are invisible unless you already know to look for them.

That felt wrong. These communities deserve better than a buried events page most people never find.

## What I Built

Two new features, both aimed at making London's film club community more discoverable.

### Film Club Pages

clusterflick.com/film-clubsgives each film club its own dedicated page. Each page shows their logo, a short description of who they are and what they programme, links back to their own site, and — crucially — pulls together their full upcoming lineup acrossallthe venues they screen at. A lot of clubs move around; they're not tied to a single cinema. Clusterflick now reflects that.

To give a sense of the range:

* Bar Trashprogrammes cult and curiosity films for people who've exhausted the mainstream;
* Pitchblack Playbackruns immersive listening sessions in the dark, using cinema sound systems the way most people never get to hear them;
* andLost Reelsspecialises in bringing forgotten, lost, or otherwise unavailable films back to UK screens.

Three very different clubs, all doing something you won't find on a standard listings site, and all working across multiple venues.

I also included accessibility information on each club page, surfaced directly from the screening data. If a club regularly programmes relaxed screenings or subtitled showings, that's highlighted. It shouldn't take three clicks to find out whether a club is somewhere you can actually go.

### Near Me

clusterflick.com/near-meuses the browser's location API to show you what's geographically closest to wherever you are right now — venues, films showing there, and the film clubs attached to those screenings. It's not trying to be Google Maps. The goal is simpler: give someone a starting point. "What's on near me tonight?" is one of the most natural questions in the world, and it's surprisingly hard to answer if you don't already know which cinemas are in your area. And alongside "what's on near me?", it now also answers "what film clubs are near me?" — surfacing the clubs connected to those local venues.

Together, these two features turn Clusterflick from a listings aggregator into something closer to a community directory.

## Demo

Both features are live now:

* 🎬 Film clubs:clusterflick.com/film-clubs
* 📍 Near me:clusterflick.com/near-me

## Code

## clusterflick/clusterflick.com

### Code for the clusterflick website

# Clusterflick

clusterflick.com·Storybook (Chromatic)

Every film, every cinema, one place.

Clusterflick is an open-source web app that aggregates film screenings from
across London cinemas into a single, searchable interface. Compare screenings
find showtimes, and discover what's on — whether you're chasing new releases or
cult classics.

## Features

* Unified Cinema Listings— Browse film screenings from 240+ London cinemas
in one place
* Rich Movie Data— View ratings and reviews from IMDb, Letterboxd
Metacritic, and Rotten Tomatoes
* Multiple Event Types— Find movies, TV screenings, comedy, music events,
talks, workshops, and more
* Venues & Boroughs— Browse all cinemas by venue or explore all 33 London
boroughs
* Festival Pages— Dedicated pages for London film festivals with full
programme listings
* Accessibility Filters— Filter by audio description, subtitles, hard of
hearing support, relaxed screenings, and baby-friendly showings
* Geolocation— Sort venues by distance from your current location
* Shareable Filters—…

View on GitHub

And the data pipeline that feeds the cinema data the site relies on is here:github.com/clusterflick/data-combined

## How I Built It

The site is built withNext.jsand TypeScript, hosted on GitHub Pages. The film club pages are server-side rendered — all the data is known ahead of time, so they can be fully built at deploy. Near Me is the opposite: since it depends on the user's location, there's nothing to pre-render. The venue and screening data loads client-side, and the results appear once both that data and the user's location are available.

TheNear Melogic is straightforward in principle: grab the user's coordinates from the browser Location API, load the cinema location data from the data pipeline, calculate distances, sort, render. The trickier part was deciding what "near" means when you're in London. After some trial and error, 2 miles turned out to be the sweet spot — enough to surface a decent set of options without stretching the definition of "nearby" too far.

For thefilm club pages, the main work was research and curation. I used Claude to help with the initial research pass — pulling together descriptions, verifying club details, and drafting copy — then reviewed and edited everything manually. The club-to-screening relationships come from the data pipeline, which already tags screenings with their organiser where that data is available. In the end I've added 22 clubs to the system, and over time I'll continue to add more.

CI/CD runs via GitHub Actions. The data pipeline runs twice a day, and the site rebuilds automatically each time it finishes — so listings stay fresh without any manual intervention. I can also kick off a deployment manually when there are site updates to ship.

This has beensitting in my GitHub issuesfor the last few months — five separate issues, all variations on the same ask; "what's nearby?" and "how do I find film clubs?". I kept kicking them down the road. This weekend challenge was the forcing function I needed to actually ship them. 🎉

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
