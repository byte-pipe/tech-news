---
title: 'GitHub - francescopace/espectre: 🛜 ESPectre 👻 - Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration. · GitHub'
url: https://github.com/francescopace/espectre
site_name: github
content_file: github-github-francescopaceespectre-espectre-motion-detec
fetched_at: '2026-06-09T12:03:07.756911'
original_url: https://github.com/francescopace/espectre
author: francescopace
description: 🛜 ESPectre 👻 - Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration. - francescopace/espectre
---

francescopace

 

/

espectre

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork624
* Star8k

 
 
 
 
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

253 Commits
253 Commits
.github
.github
 
 
components/
espectre
components/
espectre
 
 
docs
docs
 
 
examples
examples
 
 
images
images
 
 
micro-espectre
micro-espectre
 
 
test
test
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PERFORMANCE.md
PERFORMANCE.md
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
SETUP.md
SETUP.md
 
 
TUNING.md
TUNING.md
 
 
codecov.yml
codecov.yml
 
 
View all files

## Repository files navigation

# 🛜 ESPectre 👻

Motion detection system based on Wi-Fi spectre analysis (CSI), with native Home Assistant integration via ESPHome.

Tip

New ML Detector: Neural network-based motion detection. No calibration required, runs on-device. This is an experimental feature, and feedback is welcome in the dedicatedML detector discussion. Asnapshot buildwith the latest changes is also available (use-mlassets for the machine learning based detector), or followSetup guidefor custom configuration.

## Table of Contents

* In 3 Points
* What You Need
* Quick Start
* How It Works
* What You Can Do With It
* Sensor Placement Guide
* System Architecture
* FAQ
* Security and Privacy
* Technical Deep Dive
* Two-Platform Strategy
* Future Evolution
* Documentation
* Media
* Related Projects
* Acknowledgments
* License
* Author

## In 3 Points

1. What it does: Detects movement using Wi-Fi (no cameras, no microphones)
2. What you need: A ~€10 ESP32 device (S3 and C6 recommended, other variants supported)
3. Setup time: 10-15 minutes

## What You Need

### Hardware

* 2.4GHz Wi-Fi Router- the one you already have at home works fine
* ESP32 with CSI support- ESP32-C6, ESP32-S3, ESP32-C3, ESP32 (original) or other variants. SeeSETUP.mdfor the complete platform comparison table.

ESP32-S3 DevKit with external antennas

### Software (All Free)

* Home Assistant(on Raspberry Pi, PC, NAS, or cloud)
* ESPHome(integrated in Home Assistant or standalone)

### Required Skills

* Basic YAML knowledgefor configuration
* Home Assistant familiarity(optional but recommended)
* NOprogramming required
* NOrouter configuration needed

## Quick Start

Setup time: ~10-15 minutesDifficulty: Easy (YAML configuration only)

1. Setup & Installation: Follow the complete guide inSETUP.md
2. Tuning: Optimize for your environment withTUNING.md

Home Assistant dashboard with real-time motion detection, threshold control, and debug sensors

## How It Works

When someone moves in a room, they "disturb" the Wi-Fi waves traveling between the router and the sensor. It's like when you move your hand in front of a flashlight and see the shadow change.

The ESP32 device "listens" to these changes and understands if there's movement.

### Advantages

* No cameras(total privacy)
* No wearables needed(no bracelets or sensors to wear)
* Works through walls(Wi-Fi passes through walls)
* Very cheap(~€10 total)

Want to understand the technical details? SeeALGORITHMS.mdfor CSI explanation and signal processing documentation.

## What You Can Do With It

### Practical Examples

* Home security: Get an alert if someone enters while you're away
* Elderly care: Monitor activity to detect falls or prolonged inactivity
* Smart automation: Turn on lights/heating only when someone is present
* Energy saving: Automatically turn off devices in empty rooms
* Child monitoring: Alert if they leave the room during the night
* Climate control: Heat/cool only occupied zones

## Where to Place the Sensor

Optimal sensor placement is crucial for reliable movement detection.

### Recommended Distance from Router

Optimal range: 3-8 meters

Distance

Signal

Multipath

Sensitivity

Noise

Recommendation

< 2m

Too strong

Minimal

Low

Low

❌ Too close

3-8m

Strong

Good

High

Low

✅ 
Optimal

> 10-15m

Weak

Variable

Low

High

❌ Too far

### Placement Tips

Do:

* Position sensor in the area to monitor (not necessarily in direct line with router)
* Height: 1-1.5 meters from ground (desk/table height)
* External antenna: Use IPEX connector for better reception

Don't:

* Avoid metal obstacles between router and sensor (refrigerators, metal cabinets)
* Avoid corners or enclosed spaces (reduces multipath diversity)

## System Architecture

### Processing Pipeline

ESPectre uses a focused processing pipeline for motion detection:

┌─────────────┐
│ CSI Data │ Raw Wi-Fi Channel State Information
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Gain Lock │ AGC/FFT stabilization (~3 seconds)
│ │ Locks hardware gain for stable measurements
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Auto │ Automatic subcarrier selection (once at boot)
│ Calibration │ Selects optimal 12 subcarriers (NBVI)
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Adaptive │ auto: P95 × 1.1 | min: P100
│ Threshold │ or fixed manual value
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Hampel │ Turbulence outlier removal
│ Filter │ (enabled by default)
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Low-pass │ Noise reduction (smoothing)
│ Filter │ (optional, disabled by default)
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Detection │ MVS or ML score
│ Evaluation │ every evaluation_interval packets
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Hit Filter │ motion_on_hits / motion_off_hits
│ │ edge-driven IDLE ↔ MOTION
└──────┬──────┘
 │
 ▼
┌─────────────┐
│ Home │ Edge-driven motion binary +
│ Assistant │ periodic Movement Score / Threshold
└─────────────┘

### Single or Multiple Sensors

┌─────────┐ ┌─────────┐ ┌─────────┐
│ ESP32 │ │ ESP32 │ │ ESP32 │
│ Room 1 │ │ Room 2 │ │ Room 3 │
└────┬────┘ └────┬────┘ └────┬────┘
 │ │ │
 └────────────┴────────────┘
 │
 │ ESPHome Native API
 ▼
 ┌────────────────────┐
 │ Home Assistant │
 │ (Auto-discovery) │
 └────────────────────┘

Each sensor is automatically discovered by Home Assistant with:

* Binary sensor for motion detection, published immediately on state edges
* Movement score sensor, published on the periodic cadence
* Adjustable threshold (number entity)

### Automatic Subcarrier Selection

ESPectre implementsNBVI(Normalized Band Variance Index) for automatic subcarrier selection, achieving near-optimal performance (F1>96%) withzero manual configuration. The algorithm selects 12 non-consecutive subcarriers based on stability metrics and spectral diversity.

⚠️IMPORTANT(MVS mode): Keep the roomquiet and stillfor 10 seconds after device boot. The auto-calibration runs during this time and movement will affect detection accuracy. ML mode skips calibration.

For algorithm details, seeALGORITHMS.md.

## FAQ for Beginners

Click to expand FAQ

Q: Do I need programming knowledge to use it?A: No! ESPectre uses YAML configuration files. Just download the example, flash it, and configure WiFi via the ESPHome app or web interface.

Q: Does it work with my router?A: Yes, if your router has 2.4GHz Wi-Fi (virtually all modern routers have it).

Q: How much does it cost in total?A: Hardware: ~€10 for an ESP32 device (S3/C6 recommended, other variants also work). Software: All free and open source. You'll also need Home Assistant running somewhere (Raspberry Pi ~€35-50, or any existing PC/NAS).

Q: Do I need to modify anything on the router?A: No! The router works normally. The sensor "listens" to Wi-Fi signals without modifying anything.

Q: Does it work through walls?A: Yes, the 2.4GHz Wi-Fi signal penetrates drywall. Reinforced concrete walls reduce sensitivity but detection remains possible at reduced distances.

Q: How many sensors are needed for a house?A: It depends on size. One sensor can monitor ~50 m². For larger homes, use multiple sensors (1 sensor every 50-70 m² for optimal coverage).

Q: Can it distinguish between people and pets?A: The system uses a 2-state segmentation model (IDLE/MOTION) that identifies generic movement without distinguishing between people, pets, or other moving objects. For more sophisticated classification (people vs pets, activity recognition, gesture detection), trained AI/ML models would be required (seeFuture Evolutionsection).

Q: Does it work with mesh Wi-Fi networks?A: Yes, it works normally. Make sure the ESP32 connects to the 2.4 GHz band.

Q: How accurate is the detection?A: Detection accuracy is highly environment-dependent and requires proper tuning. Factors affecting performance include: room layout, wall materials, furniture placement, distance from router (optimal: 3-8m), and interference levels. In optimal conditions with proper tuning, the system provides reliable movement detection. Adjust thesegmentation_thresholdparameter to tune sensitivity for your specific environment.

Q: What's the power consumption?A: ~500mW typical during continuous operation. The firmware includes support for power optimization, and deep sleep modes can be implemented for battery-powered deployments, though this would require custom modifications to the code.

Q: If it doesn't work, can I get help?A: Yes, open anIssue on GitHubor contact me via email.

## Security and Privacy

Privacy, Security & Ethical Considerations (click to expand)

### Nature of Collected Data

The system collectsanonymous datarelated to the physical characteristics of the Wi-Fi radio channel:

* Amplitudes and phases of OFDM subcarriers
* Statistical signal variances
* NOT collected: personal identities, communication contents, images, audio

CSI data represents only the properties of the transmission medium and does not contain direct identifying information.

### Privacy Advantages

* No cameras: Respect for visual privacy
* No microphones: No audio recording
* No wearables: Doesn't require wearable devices
* Aggregated data: Only statistical metrics, not raw identifying data

### ⚠️Disclaimer and Ethical Considerations

WARNING: Despite the intrinsic anonymity of CSI data, this system can be used for:

* Non-consensual monitoring: Detecting presence/movement of people without their explicit consent
* Behavioral profiling: With advanced AI models, inferring daily life patterns
* Domestic privacy violation: Tracking activities inside private homes

### Usage Responsibility

The user is solely responsible for using this system and must:

1. Obtain explicit consentfrom all monitored persons
2. Respect local regulations(GDPR in EU, local privacy laws)
3. Clearly informabout the presence of the sensing system
4. Limit useto legitimate purposes (home security, personal home automation)
5. Protect datawith encryption and controlled access
6. DO NOT usefor illegal surveillance, stalking, or violation of others' privacy

## Technical Deep Dive

For algorithm details (MVS, NBVI calibration, Hampel filter), seeALGORITHMS.md.

For performance metrics (confusion matrix, F1-score, benchmarks), seePERFORMANCE.md.

## Two-Platform Strategy

This project follows adual-platform approachto balance innovation speed with production stability:

### ESPectre (This Repository) - Production Platform

Target: End users, smart home enthusiasts, Home Assistant users

* ESPHome componentwith native Home Assistant integration
* YAML configuration- no programming required
* Auto-discovery- devices appear automatically in Home Assistant
* Production-ready- stable, tested, easy to deploy
* Demonstrative- showcases research results in a user-friendly package

### Micro-ESPectre- R&D Platform

Target: Researchers, developers, academic/industrial applications

* Python/MicroPythonimplementation for rapid prototyping
* MQTT-based- flexible integration (not limited to Home Assistant)
* Fast iteration- test new algorithms in seconds, not minutes
* Analysis tools- comprehensive suite for CSI data analysis
* Use cases: Academic research, industrial sensing, algorithm development

Micro-ESPectre gives you the fundamentals for:

* People counting
* Activity recognition(walking, falling, sitting, sleeping)
* Localization and tracking
* Gesture recognition

### Development Flow

┌─────────────────────┐ Validated ┌──────────────────────┐
│ Micro-ESPectre │ ─────────────────► │ ESPectre │
│ (R&D Platform) │ algorithms │ (Production Platform)│
│ │ │ │
│ • Fast prototyping │ │ • ESPHome component │
│ • Algorithm testing │ │ • Home Assistant │
│ • Data analysis │ │ • End-user ready │
│ • MQTT flexibility │ │ • Native API │
└─────────────────────┘ └──────────────────────┘

Innovation cycle: New features and algorithms are first developed and validated in Micro-ESPectre (Python), then ported to ESPectre (C++) once proven effective.

## Future Evolution

While ESPectre v2.x focuses onmotion detection(MVS + automatic subcarrier selection), the project is exploring machine learning capabilities for advanced applications:

Capability

Status

Description

ML Detector

Experimental

Neural network (MLP 9→32→16→1)

Gesture Recognition

Planned

Detect hand gestures (swipe, push, circle) for smart home control

Human Activity Recognition

Planned

Identify activities (sitting, walking, falling)

People Counting

Planned

Estimate number of people in a room

3D Localization

Research

Indoor positioning (30-50cm accuracy) via phase-coherent antenna array

The ML Detector is already available withdetection_algorithm: mlin your YAML configuration. For algorithm details, seeALGORITHMS.mdandPERFORMANCE.mdfor current metricsThe ML data collection and training infrastructure is documented inML_DATA_COLLECTION.md.

SeeROADMAP.mdfor detailed plans, timelines, and how to contribute.

## Documentation

### ESPectre (Production)

Document

Description

Intro

(This file) Project overview, quick start, FAQ

Setup Guide

Installation and configuration with ESPHome

Tuning Guide

Parameter tuning for optimal detection

Performance

Benchmarks, confusion matrix, F1-score

The Game

Browser game, USB streaming API, interactive threshold tuning

Test Suite

PlatformIO Unity test documentation

### Micro-ESPectre (R&D)

Document

Description

Intro

R&D platform overview, CLI, MQTT, Web Monitor

Algorithms

Scientific documentation of MVS, NBVI calibration, Hampel filter

Analysis Tools

CSI analysis and optimization scripts

ML Data Collection

Building labeled datasets for machine learning

References

Academic papers and research resources

### Project

Document

Description

Roadmap

Project vision and ML plans

Contributing

How to contribute (code, data, docs)

Changelog

Version history and release notes

Security

Security policy and vulnerability reporting

Code of Conduct

Community guidelines

## Media

Articles

Title

Medium

How I Turned My Wi-Fi Into a Motion Sensor - Part 1

Medium

How I Turned My Wi-Fi Into a Motion Sensor - Part 2

IoT For All

How I Turned My Wi-Fi Into a Motion Sensor

Hackaday

Make Your Own ESP32-Based Person Sensor, No Special Hardware Needed

Adafruit Learn

ESPectre Human Detector for Feather

Seeed Studio Wiki

Deploying Espectre on Seeed Studio XIAO ESP32 Series with ESPHome

Blog

Discussion

Home Assistant

ESPectre - Wi-Fi Motion Detection for Home Assistant

Videos

Video

@GithubAwesome

ESPectre

Podcasts

Episode

Hackaday

Podcast Episode 355: Person Detectors, Walkie Talkies, Open Smartphones...

## Related Projects

* radio-presence-scanner: complementary presence-sensing project focused on BLE radio observations from host devices (Python), with optional HTTP dashboard.
* micropython-esp32-csi: custom MicroPython fork exposing ESP32 CSI APIs, used as the firmware foundation for rapid CSI prototyping in the Micro-ESPectre workflow.

## Acknowledgments

ESPectre leverages the native Wi-Fi CSI capabilities of ESP32 chips. Thanks toEspressiffor making CSI accessible in the ESP-IDF framework and for recognizing ESPectre as acommunity projectin theiresp-csirepository.

## License

This project is released under theGNU General Public License v3.0 (GPLv3).

GPLv3 ensures that:

* The software remains free and open source
* Anyone can use, study, modify, and distribute it
* Modifications must be shared under the same license
* Protects end-user rights and software freedom

SeeLICENSEfor the full license text.

Contributions are submitted under GPLv3 and must include a DCOSigned-off-bytrailer on each commit (git commit -s).

## Author

Francesco PaceEmail:francesco.pace@espectre.devLinkedIn:linkedin.com/in/francescopace

If you find ESPectre useful and want to support its development, you can buy me a coffee. It's completely optional.
I work on this project because I'm passionate about it. Contributions help me buy new hardware to expand the list of tested and supported devices, and dedicate more time to new features.

## About

🛜 ESPectre 👻 - Motion detection system based on Wi-Fi spectre analysis (CSI), with Home Assistant integration.

espectre.dev

### Topics

 motion-detection

 wifi

 diy

 home-assistant

 csi

 esp-32

 wifi-sensing

 espectre

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

8k

 stars
 

### Watchers

78

 watching
 

### Forks

624

 forks
 

 Report repository

 

## Releases15

v2.8.0 - Detection hardening, ML cross-chip reliability, and runtime motion policy

 Latest

 

May 21, 2026

 

+ 14 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/francescopace

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python58.8%
* C++26.5%
* HTML7.4%
* Jupyter Notebook5.4%
* C1.4%
* Shell0.5%