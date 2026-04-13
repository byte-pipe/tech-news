---
title: Someone Bought 30 WordPress Plugins and Planted a Backdoor in All of Them.
url: https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/
date: 2026-04-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-14T06:02:54.610747
---

# Someone Bought 30 WordPress Plugins and Planted a Backdoor in All of Them.

# Someone Bought 30 WordPress Plugins and Planted a Backdoor in All of Them.

## Overview
- A supply‑chain attack affected more than 30 free WordPress plugins from the “Essential Plugin” portfolio.  
- The attacker bought the entire plugin business on Flippa, inserted a hidden backdoor, and later activated it to serve SEO spam only to Googlebot.  
- WordPress.org detected the malicious code, forced an update, and permanently closed all affected plugins on a single day.

## Timeline of Events
- **Jan 2019 – Aug 2025**: The plugin *Countdown Timer Ultimate* (and others) were installed on many sites; the `wpos-analytics` module functioned as a legitimate analytics opt‑in.  
- **Aug 8 2025 (v2.6.7)**: A commit added 191 lines of code, including a PHP deserialization backdoor and an unauthenticated REST endpoint.  
- **Apr 5‑6 2026**: The dormant backdoor was weaponized; the module downloaded `wp-comments-posts.php` and injected malicious PHP into `wp-config.php`.  
- **Apr 7 2026**: WordPress.org Plugins Team permanently closed 31 plugins from the Essential Plugin author.  
- **Apr 8 2026**: An auto‑update to v2.6.9.1 neutralized the phone‑home mechanism but did not remove the injected code in `wp-config.php`.

## Technical Details of the Malware
- The backdoor fetched a payload from `analytics.essentialplugin.com`, placed it in `wp-comments-posts.php`, and injected a large PHP block into `wp-config.php`.  
- Injected code:
  - Retrieved spam links, redirects, and fake pages from a command‑and‑control (C2) server.  
  - Served the spam only to Googlebot, keeping it invisible to site owners.  
  - Resolved the C2 domain via an Ethereum smart contract, allowing the attacker to change the target domain without traditional DNS takedowns.  
- The malicious code remained after the forced update because the update only altered the plugin files, not `wp-config.php`.

## Forensic Investigation
- Daily Restic backups (captured by CaptainCore) were compared across eight snapshots to pinpoint the injection window.  
- File size of `wp-config.php` jumped from ~3.3 KB to 9.5 KB between 04:22 UTC and 11:06 UTC on Apr 6 2026, giving a 6‑hour 44‑minute injection window.  
- Analysis of 939 quicksave snapshots showed the backdoor code was present in the plugin source since Aug 8 2025 but stayed dormant for eight months.

## Business Context – Flippa Sale
- Original developers (Minesh Shah, Anoop Ranawat, Pratik Jain) built the portfolio under “WP Online Support” (2015) and later rebranded to “Essential Plugin.”  
- Revenue declined 35‑45 % in late 2024; the business was listed on Flippa.  
- Buyer “Kris” (background in SEO, crypto, and online gambling) purchased the entire portfolio for six figures in early 2025.  
- The first SVN commit by the new owner introduced the backdoor code.

## WordPress.org Response
- On Apr 7 2026, the Plugins Team closed all 31 plugins authored by Essential Plugin in a single action.  
- The following day, an auto‑update (v2.6.9.1) was forced across all installations, commenting out the backdoor line but leaving the injected `wp-config.php` code untouched.

## List of Permanently Closed Plugins
- Accordion and Accordion Slider  
- Album and Image Gallery Plus Lightbox  
- Audio Player with Playlist Ultimate  
- Blog Designer for Post and Widget  
- Countdown Timer Ultimate  
- Featured Post Creative  
- Footer Mega Grid Columns  
- Hero Banner Ultimate  
- HTML5 VideoGallery Plus Player  
- Meta Slider and Carousel with Lightbox  
- Popup Anything on Click  
- Portfolio and Projects  
- Post Category Image with Grid and Slider  
- Post Grid and Filter Ultimate  
- Preloader for Website  
- Product Categories Designs for WooCommerce  
- Responsive WP FAQ with Category  
- SlidersPack – All in One Image Sliders  
- SP News And Widget  
- Styles for WP PageNavi – Addon  
- Ticker Ultimate  
- Timeline and History Slider  
- Woo Product Slider and Carousel with Category  
- WP Blog and Widgets  
- WP Featured Content and Slider  
- WP Logo Showcase Responsive Slider and Carousel  
- WP Responsive Recent Post Slider  
- WP Slick Slider and Image Carousel  
- WP Team Showcase and Slider  
- WP Testimonial with Widget  
- WP Trending Post Slider and Widget  

All plugins were removed from the WordPress.org repository, and the author profile now returns no results.