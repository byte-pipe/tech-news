---
title: 'GitHub - blakeblackshear/frigate: NVR with realtime local object detection for IP cameras · GitHub'
url: https://github.com/blakeblackshear/frigate
site_name: github
content_file: github-github-blakeblackshearfrigate-nvr-with-realtime-lo
fetched_at: '2026-05-24T11:30:57.378933'
original_url: https://github.com/blakeblackshear/frigate
author: blakeblackshear
description: NVR with realtime local object detection for IP cameras - blakeblackshear/frigate
---

blakeblackshear

 

/

frigate

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.2k
* Star32.6k

 
 
 
 
dev
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

5,794 Commits
5,794 Commits
.cspell
.cspell
 
 
.cursor/
rules
.cursor/
rules
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
config
config
 
 
docker
docker
 
 
docs
docs
 
 
frigate
frigate
 
 
migrations
migrations
 
 
notebooks
notebooks
 
 
testing-scripts
testing-scripts
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.pylintrc
.pylintrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
TRADEMARK.md
TRADEMARK.md
 
 
audio-labelmap.txt
audio-labelmap.txt
 
 
cspell.json
cspell.json
 
 
docker-compose.yml
docker-compose.yml
 
 
generate_config_translations.py
generate_config_translations.py
 
 
labelmap.txt
labelmap.txt
 
 
netlify.toml
netlify.toml
 
 
package-lock.json
package-lock.json
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Frigate NVR™ - Realtime Object Detection for IP Cameras

[English] |简体中文

A complete and local NVR designed forHome Assistantwith AI object detection. Uses OpenCV and Tensorflow to perform realtime object detection locally for IP cameras.

Use of a GPU or AI accelerator is highly recommended. AI accelerators will outperform even the best CPUs with very little overhead. See Frigate's supportedobject detectors.

* Tight integration with Home Assistant via acustom component
* Designed to minimize resource use and maximize performance by only looking for objects when and where it is necessary
* Leverages multiprocessing heavily with an emphasis on realtime over processing every frame
* Uses a very low overhead motion detection to determine where to run object detection
* Object detection with TensorFlow runs in separate processes for maximum FPS
* Communicates over MQTT for easy integration into other systems
* Records video with retention settings based on detected objects
* 24/7 recording
* Re-streaming via RTSP to reduce the number of connections to your camera
* WebRTC & MSE support for low-latency live view

## Documentation

View the documentation athttps://docs.frigate.video

## Donations

If you would like to make a donation to support development, please useGithub Sponsors.

## License

This project is licensed under theMIT License.

* Code:The source code, configuration files, and documentation in this repository are available under theMIT License. You are free to use, modify, and distribute the code as long as you include the original copyright notice.
* Trademarks:The "Frigate" name, the "Frigate NVR" brand, and the Frigate logo aretrademarks of Frigate, Inc.and arenotcovered by the MIT License.

Please see ourTrademark Policyfor details on acceptable use of our brand assets.

## Screenshots

### Live dashboard

### Streamlined review workflow

### Multi-camera scrubbing

### Built-in mask and zone editor

## Translations

We useWeblateto support language translations. Contributions are always welcome.

Copyright © 2026 Frigate, Inc.

## About

NVR with realtime local object detection for IP cameras

frigate.video

### Topics

 home-automation

 mqtt

 ai

 camera

 rtsp

 tensorflow

 nvr

 realtime

 home-assistant

 homeautomation

 object-detection

 google-coral

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

32.6k

 stars
 

### Watchers

246

 watching
 

### Forks

3.2k

 forks
 

 Report repository

 

## Releases77

0.17.1 Release

 Latest

 

Mar 22, 2026

 

+ 76 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript54.0%
* Python44.5%
* CSS0.4%
* Shell0.4%
* Dockerfile0.3%
* JavaScript0.2%
* Other0.2%