---
title: How I Turned My Security Cameras Into an Automatic Bird Identification System with BirdNet-Go
url: https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/
site_name: hackernews_api
content_file: hackernews_api-how-i-turned-my-security-cameras-into-an-automatic
fetched_at: '2026-08-31T23:08:50.899789'
original_url: https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/
author: speckx
date: '2026-08-31'
published_date: '2026-06-04T18:30:38.000Z'
description: I turned three security cameras into an automatic bird identification system using BirdNet-Go. Now my wife and I can track every bird species that visits our yard in real-time.
tags:
- hackernews
- trending
---

My wife loves listening to the birds and identifying them using an app on her phone. I thought I'd take this a step further and see if there was something that can identify the birds based on their song. Looking around I found BirdNet andBirdNet-Go, then discovered you can run this on Docker and use the security cameras you already have outside to identify the birds. Awesome! So I took 3 of the cameras around my house and used their microphones to identify the birds. It was magic.

## Real-Time Bird and Bat Audio Detection

BirdNet-Go runs 24/7. It listens constantly. The moment a bird starts singing, it analyzes the audio and gives you an identification. No waiting, no manual recording. It works for bats too, which is pretty cool if you've got them flying around at dusk. The system just keeps running in the background, cataloging everything it hears. It also started detecting frogs which is interesting.

## Multi-Model Local AI Inference Engine

The whole thing runs locally on your hardware. No cloud services. No API calls. The AI models live right on your server or Raspberry Pi. This means it's fast, private, and doesn't cost you anything per month. You can even run multiple models if you want different detection strategies or regional bird databases. They recently added Google Perch v2 to the model gallery allowing for 14,795 species to be detected vs the 6,000 that BirdNET 2.4 provided.

## Alert Rules with Species List Matching

You can set up rules for specific birds. Want to know the instant a cardinal shows up? Done. Looking for a rare species in your area? Set an alert. The system matches against species lists and sends you notifications based on whatever criteria you set. It's like having a birding buddy who never sleeps. I even have it connected to a channel in my homes Discord server. Wait, your house doesn't have a dedicated Discord?

Setting up notifications and alerts for bird sightings into the house discord channel #birdnet

## Species Novelty Tracking for New Detections

This feature tracks which birds are new to your yard. First time a blue jay visits? BirdNet-Go flags it. It maintains a running list of every species it's detected, so you can see your yard's biodiversity grow over time. Honestly, this turned into a fun game for us.

## RTSP Stream Support for IP Cameras

If your cameras support RTSP, you're good to go. Most modern IP cameras do. You just point BirdNet-Go at the stream URL. I used three of my existing security cameras. Didn't need to buy any special hardware. The cameras I already had for security now pull double duty identifying birds.

## BirdWeather Integration for Data Sharing

BirdWeather is a community platform for sharing bird detection data. BirdNet-Go integrates with it directly. If you want to contribute your observations to a larger dataset, you can. It helps researchers and other birders see what's happening in your area. You don't have to use it, but it's nice that the option exists.

## Self-Hosted with No Cloud Dependencies

Everything lives on your network. The audio never leaves your house unless you explicitly share it. No subscription fees. No terms of service changes. No company shutting down the service in two years. You own the whole stack. It runs in Docker, so it's easy to manage alongside everything else in your homelab.

## Can connect to Home Assistant

Evernything needs to be able to connect to Home Assistant and BirdNET-Go can use MQTT to be discovered in Home Assistant.

## Visual Audio Channel Energy Level Analysis

The interface shows you real-time audio levels for each channel. You can see exactly what the microphones are picking up. This helps you position cameras better or troubleshoot why one isn't detecting anything. Sometimes you'll realize the camera is pointed at a noisy AC unit or getting wind noise, and you can adjust accordingly.

## IT DETECTED A FART!

A few nights ago I got a notification from Home Assistant that a fart was detected in the driveway. My neighbor was walking by my house on his nightly walk and ripped one as he passed by the driveway and the fart was detected.

## There's an app for that?

Someone made a free app for iOS called "BirdNET-Go Companion" that lets you connect you phone to your BirdNet-Go server and see the detections in a native iOS app. Awesome job Robert Oesterlin!

BIrdNET-Go Companion App - App Store
Download BIrdNET-Go Companion by Robert Oesterlin on the App Store. See screenshots, ratings and reviews, user tips, and more apps like BIrdNET-Go Companion.
App Store
Robert Oesterlin

## Final Thoughts

Look, this project surprised me. I expected it to be neat but figured I'd get bored after a week. Instead, my wife and I check it daily. We've learned which birds visit at what times. We've spotted species we didn't know lived nearby. My friends got interested too, I made this avaiable on the public house domain name (behind Cloudflare of course.) and allowed a few of my friends to connect to it and see how it works. It turned our security camera setup into something genuinely useful beyond security. If you've got cameras with microphones and even a passing interest in birds, give BirdNet-Go a shot. It's one of those homelab projects that actually improves daily life instead of just being technically interesting.

GitHub - tphakala/birdnet-go
Self-hosted realtime soundscape analyser for birds, bats and other wildlife. Multi-model local AI inference, runs 24/7 on a Raspberry Pi. — ⭐ 1,232 · 🍴 114 · nightly-20260601
GitHub
tphakala

## Let's answer some questions left onRedditandHacker News(Hi all!)

* A lot of folks mentioned using e-ink displays to view this data and what a smart idea. My wife and I access the web interface on our photos to see the list of recent detections. I also have Home Assistant integration tied in so it shows up on a screen I have configured there. I'm going to look into themobile companion appto see how that all works.
* Some folks talked about using special microphones to do the detection and I may do that for our back yard, we don't have cameras out there for personal privacy reasons but a mic would be great. One thing I didn't mention is the mics cut out if it hears speech, which is a nice feature.
* A few folks mentioned they their built or vibe coded their on versions of BirdNet-Go and I think thats great, I found what worked for me and it was a system my wife was already using on her phone with an app. Now it's like having her phone outside 24/7 capturing the bird calls.
* Someone asked if this can be turned into a doorbell, no it cant be but it can use your doorbell if it has an RTSP feed.
* Lots of folks mentioned Bats, yeah, if you have a specialized mic you can totally detect bats with better accuracy. We have a "bat box" down the street from us where someone set one up on a pole and some bats we believe live there.
* Yeah, the fart detector was funny!
* People asked about confidance in identifying birds and honesly we're not birders just people that have a crapton of birds around us so I used the RTSP streams to capture them and a local AI model to identify them.
* Lots of folks talking about hacking flock cameras to do this, go on with your bad selves! (share the project link in the comments below if you do!)
* Some folks mentioned that I had a small amount of detections, over the last 12 months we've had 418,726 with 271 unique species and 60.9% confidence rating average. Our most common bird for our area of Southern California is the House Finch with 118,667 detections.


 Share
 


 Facebook
 


 X
 


 Reddit
 


 Copy Link
 

Link copied!

Copy failed!

 Updated on
 

 Jun 4, 2026
 


 homelab
 


 selfhosting
 


 docker
 


 AI
 


 diy
 

### Read Next


 August 21, 2026
 


 Jason Tucker
 

#### Getting My iCloud Photos Onto My Own Storage with ImmiBridge

ImmiBridge pulled 51,000 photos and videos out of iCloud and into my self hosted Immich server over a single weekend. Here's how the setup and the sync actually went.


 homelab
 


 self-hosting
 


 Immich
 


 August 15, 2026
 


 Jason Tucker
 

#### What My Nest Hub Does Besides Show Family Photos

Teaching a Google Nest Hub to show more than family photos: a driveway camera feed on movement, and a now-playing card for whatever's on the living room Apple TV.


 home-assistant
 


 homelab
 


 smart-home
 

 

# Subscribe

It's free and lets you leave a comment on posts.

Subscribe

 

Success! Now Check Your Email

To complete Subscribe, click the confirmation link in your inbox. If
 it doesn’t arrive within 3 minutes, check your spam folder.