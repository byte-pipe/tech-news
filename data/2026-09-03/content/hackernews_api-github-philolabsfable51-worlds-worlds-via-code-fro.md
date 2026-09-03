---
title: 'GitHub - PhiloLabs/fable51-worlds: worlds via code, from fable 5.1 · GitHub'
url: https://github.com/PhiloLabs/fable51-worlds
site_name: hackernews_api
content_file: hackernews_api-github-philolabsfable51-worlds-worlds-via-code-fro
fetched_at: '2026-09-03T14:53:11.705505'
original_url: https://github.com/PhiloLabs/fable51-worlds
author: surreal_
date: '2026-09-02'
description: worlds via code, from fable 5.1. Contribute to PhiloLabs/fable51-worlds development by creating an account on GitHub.
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 PhiloLabs

 

/

fable51-worlds

Public

* NotificationsYou must be signed in to change notification settings
* Fork11
* Star322

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

8 Commits
8 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
kyoto-higashiyama
kyoto-higashiyama
 
 
union-square-sf
union-square-sf
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# fable51-worlds

Worlds via code.Explorable, browser-native reconstructions of real places — researched, modelled, and quality-checked end to end by autonomousClaude Fable 5.1agent swarms, then shipped as plainThree.jsapps you can run withnpm run dev.

No game engine. No proprietary 3D tiles. Every building, storefront, sign, tree and traffic light is generated from open data and public reference imagery by code that lives in this repo.

## Worlds

### 🌉Union Square, San Francisco

▶Watch the full 59-second walkthrough· 1920×1080 · aerial, plaza, Nintendo, lower level, Apple

The square and its surrounding blocks — Powell, Geary, Post and Stockton — on real terrain and a real street grid, with 129 identified storefronts, working traffic lights and cable cars, day/sunset/night, and two explorable interiors:Apple Union Square(300 Post St) andNintendo SAN FRANCISCO(331 Powell St).

Run it

cd union-square-sf && npm install && npm run dev

Buildings

453 OSM footprints · 75 hand-authored façades · 129 named storefronts

Life

220 pedestrians on a 1,398-node nav graph · 109 vehicles incl. Powell St cable cars

Interiors

Apple + Nintendo, 23 interactive objects

Validation

34 camera-matched viewpoints vs. real photographs · 147 comparison sheets · 9 independent reviewer reports

### ⛩️Higashiyama, Kyoto

▶Watch the full 54-second walkthrough· 1920×1080 · seven scenes — over the roofs, the Shirakawa, Yasaka Shrine, the weeping cherry, the Yasaka Pagoda, Sannenzaka, and Kiyomizu-dera at sunset

Kyoto's Southern Higashiyama walking route —Gion → Hanamikoji → Yasaka Shrine → Nene-no-michi → the Yasaka Pagoda → Ninenzaka → Sannenzaka → Kiyomizu-zaka → Kiyomizu-dera— 2.3 km of it, continuously walkable, climbing 76 m from the ochaya on Hanamikoji to the temple stage. Rendered3D-to-2D as a hand-painted anime background: cel materials with hue-shifted shadow bands, screen-space ink taken from a second difference of depth, and a split-tone grade.No binary assets at all— every sign, noren, lantern, roof tile and paving stone is drawn with Canvas2D at start-up.

Run it

cd kyoto-higashiyama && npm install && npm run dev

Or, with nothing installed

npm run viewer && open viewer/higashiyama.html
 — one self-contained HTML file

Buildings

266 buildings · 471 shopfronts · 19 hero landmarks across 15 districts

Detail

1,938 trees (11 species) · 3,076 props (60 kinds) · 142 interactions

Survey

Every elevation an independent GSI 1 m LiDAR query; street widths ray-cast to OSM footprints every 8 m

Validation

52 authored viewpoints · full-route player walkthrough · per-street passability sweep · zero page errors

Six widely-repeated figures were overturned by the survey and the world is built on the measured ones — the Yasaka Pagoda is38.79 m, not 46, with aconvextaper; the Kiyomizu stage deck is at115.5 m ASL, not 240; the stage is21.8 × 9.6 m on 168 pillars of 0.64 m diameter, not 18 × 10 m on 139 pillars of 2 m.

More worlds coming.

## How these are made

Each world follows the same pipeline, and every stage is in the repo so you can re-run it:

1. Reconnaissance— parallel research agents pull OpenStreetMap geometry, USGS elevation, transit and street specs, and a storefront census with per-fact sources and confidence levels.
2. Offline asset generation— Blender-as-a-library (bpy) scripts emit optimised GLB kits: façade modules, street furniture, vehicles, vegetation, retail fixtures, pedestrian body parts.
3. Runtime— a pure Three.js app assembles terrain, streets, façades, props, crowds and traffic from JSON specs.
4. Camera-match QA— Playwright drives the real app, screenshots fixed viewpoints, and diffs them against free-licensed photographs taken from the same spot; independent reviewer agents (architect, geographer, technical artist, interaction) file reports that drive the next fix cycle.

## License

Code and generated assets:MIT. Geometry is derived fromOpenStreetMap(ODbL) and USGS 3DEP (public domain). Reference photographs are not redistributed here — their provenance is recorded per sector in each world'srefs/*/SOURCES.md. Brand names and logos identify the real businesses at their real locations and belong to their owners.