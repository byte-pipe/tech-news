---
title: 'GitHub - truelockmc/streambert: A cross-platform Electron Desktop App to stream and download any Movie, TV Series or Anime in the World. Zero Ads and Tracking · GitHub'
url: https://github.com/truelockmc/streambert
site_name: github
content_file: github-github-truelockmcstreambert-a-cross-platform-elect
fetched_at: '2026-05-20T12:02:51.088142'
original_url: https://github.com/truelockmc/streambert
author: truelockmc
description: A cross-platform Electron Desktop App to stream and download any Movie, TV Series or Anime in the World. Zero Ads and Tracking - truelockmc/streambert
---

truelockmc

 

/

streambert

Public

* NotificationsYou must be signed in to change notification settings
* Fork212
* Star2.4k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

290 Commits
290 Commits
.github
.github
 
 
public
public
 
 
screenshots
screenshots
 
 
src
src
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
index.html
index.html
 
 
index.js
index.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
popout-preload.js
popout-preload.js
 
 
preload.js
preload.js
 
 
tmdb-tutorial.md
tmdb-tutorial.md
 
 
vite.config.js
vite.config.js
 
 
View all files

## Repository files navigation

# Streambert

A cross-platform Electron Desktop App to stream and download any Movie, TV Series or Anime in the World. Zero Ads and TrackingInstallation

## Why Streambert?

* 🎦Streaming:Stream any Movie, Anime or TV Series from around the World.
* 📥Downloading:Download anything you want to watch.
* 📃Subtitles:Download and manage Subtitles.
* ⚙️Customizability:Customize the Interface and Features to your unique needs.
* 📚Library:Track what you watched, save stuff you want to watch and manage your Downloads.
* ✨Trending:Discover new things to Watch every Day.
* 🛡️Privacy:Completely Ads and Tracker free, forever.
* ⚡Speed:Stream faster than any Browser can, download with multithreading.

## Streaming

The Application mainly gets Video Streams from VidSrc (you can also Stream from videasy.net and 2Embed).It fetches Information for Images, Info Texts, Search and Homepage fromtmdb.

## Downloading

You can download those Video Streams because the Program sources Links to their .m3u8 Playlist Files (similar to this Browser Extension).Once you click 'Download' these Links are used to download the Full Movie/TV Episode usingthis Program. You can then watch them In-App or take the Files on any Storage Medium you want.

## Anime

You can also watch Anime, the App checks if a Movie or Series is an Anime and then sources its Metadata fromAniListinstead oftmdb.Media Files for Animes are scraped from AllManga.to (i stole this mechanic fromani-cli). The App directly gets .mp4 Files and doesnt evem show you the AllManga website, you can also download these Files, just like any other Content.

## Requirements

* Node.js(>=22.12.0) installed (only if you aren't usingprebuilt Binaries)
* A free TMDB API Read Access Token (Guide on how to get one)
* For downloading,this Programsomewhere on your PC andffmpeginstalled

## Installation

On first launch you'll be prompted to enter your TMDB API key. (Guide on how to get one)
It's saved locally, you only need to do this once.

### Linux, Manual (.deb / .AppImage / .pacman)

Download the latest.deb.pacmanor.AppImagefrom theReleasespage.

#
 .deb

sudo dpkg -i streambert_
*
.deb

#
 Arch Linux (.pacman)

sudo pacman -U streambert-
*
.pacman

#
 .AppImage (you can also do it with Gearlever)

chmod +x Streambert-x64.AppImage 
&&
 ./Streambert-x64.AppImage

### Windows

Download the latestStreambert Setup *.exefrom theReleasespage and run it.

## Building from Source

1. Install dependencies:

npm install

1. Build

npm run dist:win

or

npm run dist:linux

or (for Arch Linux)

npm run dist:arch

or (for an AppImage only)

npm run dist:appimage

Important

If you are building/installing on Arch Linux and encounter errors, you may need these libraries:

* libcrypt.so.1 error:sudo pacman -S libxcrypt-compat
* http-parser dependency error:yay -S http-parser(from AUR)

## Legal Disclaimer

IMPORTANT: This application is for educational and personal use only.

* Streambert does not host, store, or distribute any copyrighted content
* All content is sourced from third-party providers and websites
* Users are solely responsible for ensuring they have legal rights to access any content
* The developer does not endorse or encourage copyright infringement
* Users must comply with all applicable laws in their jurisdiction
* Any legal issues should be directed to the actual content providers
* This app functions as a search engine aggregator only
* No copyrighted material is stored on my side

## Legal Notice

This application is provided "as is" for educational purposes. The developer:

* Does not claim ownership of any content
* Does not profit from copyrighted material in any way
* Does not control third-party content providers
* Encourages users to support content creators through legal means

Project Structure

Project Root
├── index.html
├── main.js
├── package.json
├── preload.js
├── vite.config.js
├── LICENSE
├── README.md
├── public
│ ├── icon.png
│ ├── installer-sidebar.bmp
│ └── logo.svg
├── screenshots
│ ├── adblock.png
│ ├── anime.png
│ ├── api-settings_tmdb.png
│ ├── application_tmdb.png
│ ├── download.png
│ ├── icon.png
│ ├── movie.png
│ ├── personal-use_tmdb.png
│ ├── series.png
│ ├── setup.png
│ ├── signup_tmdb.png
│ ├── subs.png
│ ├── token_tmdb.png
│ └── trending.png
└── src
 ├── App.jsx
 ├── main.jsx
 ├── components
 │ ├── BlockedStatsModal.jsx
 │ ├── CloseConfirmModal.jsx
 │ ├── DownloadModal.jsx
 │ ├── ErrorBoundary.jsx
 │ ├── Icons.jsx
 │ ├── KeyboardShortcutsModal.jsx
 │ ├── MediaCard.jsx
 │ ├── SearchModal.jsx
 │ ├── SetupScreen.jsx
 │ ├── Sidebar.jsx
 │ ├── SubtitleDownloaderModal.jsx
 │ ├── TrailerModal.jsx
 │ ├── TrendingCarousel.jsx
 │ ├── UpdateModal.jsx
 │ └── WindowTitlebar.jsx
 ├── ipc
 │ ├── allmanga.js
 │ ├── blockStats.js
 │ ├── downloads.js
 │ ├── player.js
 │ ├── storage.js
 │ └── subtitles.js
 ├── pages
 │ ├── DownloadsPage.jsx
 │ ├── HomePage.jsx
 │ ├── LibraryPage.jsx
 │ ├── MoviePage.jsx
 │ ├── SettingsPage.jsx
 │ └── TVPage.jsx
 ├── styles
 │ ├── global.css
 │ └── fonts
 │ ├── bebas-neue-regular.woff2
 │ ├── dm-sans-300.woff2
 │ ├── dm-sans-500.woff2
 │ ├── dm-sans-600.woff2
 │ └── dm-sans-regular.woff2
 └── utils
 ├── ageRating.js
 ├── aniSkip.js
 ├── api.js
 ├── appearance.js
 ├── backup.js
 ├── episodeMappings.js
 ├── homeLayout.js
 ├── storage.js
 ├── subtitles.js
 ├── updates.js
 ├── useBlockedStats.js
 └── useRatings.js

## About

A cross-platform Electron Desktop App to stream and download any Movie, TV Series or Anime in the World. Zero Ads and Tracking

### Topics

 electron

 downloader

 streaming

 movies

 anime

 tv

 series

 tmdb-api

 streaming-video

 anime-downloader

 anime-scraper

 piracy

 modern-ui

 movies-streaming

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.4k

 stars
 

### Watchers

14

 watching
 

### Forks

212

 forks
 

 Report repository

 

## Releases17

v.2.4

 Latest

 

Apr 30, 2026

 

+ 16 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript90.6%
* CSS9.4%