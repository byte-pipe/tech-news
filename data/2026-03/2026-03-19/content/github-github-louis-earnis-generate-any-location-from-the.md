---
title: 'GitHub - louis-e/arnis: Generate any location from the real world in Minecraft with a high level of detail. · GitHub'
url: https://github.com/louis-e/arnis
site_name: github
content_file: github-github-louis-earnis-generate-any-location-from-the
fetched_at: '2026-03-19T11:17:36.259600'
original_url: https://github.com/louis-e/arnis
author: louis-e
description: Generate any location from the real world in Minecraft with a high level of detail. - louis-e/arnis
---

louis-e

 

/

arnis

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork931
* Star10.1k

 
 
 
 
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

1,489 Commits
1,489 Commits
.github
.github
 
 
assets
assets
 
 
capabilities
capabilities
 
 
src
src
 
 
tests/
map_transformation
tests/
map_transformation
 
 
.envrc
.envrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.rs
build.rs
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
taginfo.json
taginfo.json
 
 
tauri.conf.json
tauri.conf.json
 
 
View all files

## Repository files navigation

# Arnis

Arnis creates complex and accurate Minecraft Java Edition (1.17+) and Bedrock Edition worlds that reflect real-world geography, topography, and architecture.

This free and open source project is designed to handle large-scale geographic data from the real world and generate detailed Minecraft worlds. The algorithm processes geospatial data from OpenStreetMap as well as elevation data to create an accurate Minecraft representation of terrain and architecture.
Generate your hometown, big cities, and natural landscapes with ease!

Want to generate on mobile or want larger maps?MapSmithgenerates worlds in your browser, no install required.

This Github page andarnismc.comare the only official project websites. Do not download Arnis from any other website.

## ⌨️ Usage

Download thelatest releaseorcompilethe project on your own.

Choose your area on the map using the rectangle tool and select your Minecraft world - then simply click onStart Generation!
Additionally, you can customize various generation settings, such as world scale, spawn point, or building interior generation.

## 📚 Documentation

Full documentation is available in theGitHub Wiki, covering topics such as technical explanations, FAQs, contribution guidelines and roadmaps.

backgroundvid.webm

## 🏆 Open Source

#### Key objectives of this project

* Modularity: Ensure that all components (e.g., data fetching, processing, and world generation) are cleanly separated into distinct modules for better maintainability and scalability.
* Performance Optimization: We aim to keep a good performance and speed of the world generation process.
* Comprehensive Documentation: Detailed in-code documentation for a clear structure and logic.
* User-Friendly Experience: Focus on making the project easy to use for end users.
* Cross-Platform Support: We want this project to run smoothly on Windows, macOS, and Linux.

#### How to contribute

This project is open source and welcomes contributions from everyone! Whether you're interested in fixing bugs, improving performance, adding new features, or enhancing documentation, your input is valuable. Simply fork the repository, make your changes, and submit a pull request. Please respect the above mentioned key objectives. Contributions of all levels are appreciated, and your efforts help improve this tool for everyone.

Command line Build:cargo run --no-default-features -- --terrain --path="C:/YOUR_PATH/.minecraft/saves/worldname" --bbox="min_lat,min_lng,max_lat,max_lng"GUI Build:cargo run

After your pull request was merged, I will take care of regularly creating update releases which will include your changes.

If you are using Nix, you can run the program directly withnix run github:louis-e/arnis -- --terrain --path=YOUR_PATH/.minecraft/saves/worldname --bbox="min_lat,min_lng,max_lat,max_lng"

## ⭐ Star History

## 📰 Academic & Press Recognition

Arnis has been recognized in various academic and press publications after gaining more attention in December 2024.

Building realistic Minecraft worlds with Open Data on AWS: How Arnis uses elevation datasets at scale

Floodcraft: Game-based Interactive Learning Environment using Minecraft for Flood Mitigation and Preparedness for K-12 Education

Hackaday: Bringing OpenStreetMap Data into Minecraft

TomsHardware: Minecraft Tool Lets You Create Scale Replicas of Real-World Locations

XDA Developers: Hometown Minecraft Map: Arnis

Free to use press assets, including screenshots and logos, can be foundhere.

## ©️ License Information

Copyright (c) 2022-2025 Louis Erbkamm (louis-e)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.1

Download Arnis only from the official sourcehttps://arnismc.comorhttps://github.com/louis-e/arnis/. Every other website providing a download and claiming to be affiliated with the project is unofficial and may be malicious.

The logo was made by @nxfx21.

## Footnotes

1. https://github.com/louis-e/arnis/blob/main/LICENSE↩

## About

Generate any location from the real world in Minecraft with a high level of detail.

arnismc.com/

### Topics

 rust

 minecraft

 maps

 openstreetmap

 osm

 overpass-api

 tauri

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

10.1k

 stars
 

### Watchers

43

 watching
 

### Forks

931

 forks
 

 Report repository

 

## Releases15

Metropolis Update (v2.5.0)

 Latest

 

Feb 14, 2026

 

+ 14 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/louisdev

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.8%
* Other0.2%