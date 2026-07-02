---
title: Building an Open-Source Robot Vacuum — Meet OOMWOO - Makers Pet
url: https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/
site_name: hackernews_api
content_file: hackernews_api-building-an-open-source-robot-vacuum-meet-oomwoo-m
fetched_at: '2026-07-02T19:33:51.285578'
original_url: https://makerspet.com/blog/building-an-open-source-robot-vacuum-meet-oomwoo/
author: devicelimit
date: '2026-07-02'
published_date: '2026-06-14T21:38:37-07:00'
description: 'I’m starting a new build-in-public project: oomwoo, an open-source robot vacuum you build yourself. Raspberry Pi, ROS 2, 2D LiDAR, Home Assistant, 3D printed, local-first — and open from the first commit.'
tags:
- hackernews
- trending
---

Today I’m kicking off my most ambitious Maker’s Pet project yet:oomwoo, an open-source home robot vacuum thatyoucan build yourself. Open hardware, open firmware, open software — and built in public, from the first commit.

No cloud required. No vendor lock-in. It maps your home with an affordable 2D LiDAR and navigates on its own, runs locally, and integrates natively with Home Assistant. If you’re into Raspberry Pi, ROS 2, 3D printing, or just the idea of owning a vacuum you fully understand and control — this one’s for you.

About the name: “oomwoo” is a rotational ambigram — it reads the same flipped 180°, just like the robot itself roaming your floor in every direction.

Reference design — roughly how the finished oomwoo will look.

## What oomwoo is

oomwoo is a build-it-yourself robot vacuum designed for the maker community:

* Affordable and fully open— hardware, software, and firmware
* 2D LiDAR mapping and autonomous navigationwith ROS 2 / Nav2
* Native Home Assistant integrationfor local control
* 3D-printable, documented, hackable chassis
* Local-first— no cloud needed for everyday cleaning, ever
* Home-appliance quality— not a throwaway build
* Step-by-step, zero-to-hero build instructions, with a complete bill of materials so you can source every part yourself

Optional extras — cloud features, and eventually an app store of ROS 2 apps to customize how your vacuum behaves — will layer on top. But the core promise never changes:the vacuum always works cloud-free and local, out of the box.

The underside of the reference design.

## Where the project is today

This is genuinely early — and that’s the point of building in public. The first milestone (v0) is a bare-bones, working build:

* 3D-printed chassis
* ROS 2 Gazebo simulation
* LiDAR with manual SLAM
* ROS 2 on a Raspberry Pi 5 and/or ESP32 running micro-ROS (final architecture still being decided)

The open-source deliverables I’m working toward: bill of materials, 3D-printable files, ROS 2 packages, firmware, a motor-driver and sensor PCB, full build / bringup / troubleshooting docs, and demo videos.

Top cover removed — a peek at the internal layout.

## Build it with me — massively in parallel

oomwoo is organized so the community can build itin parallel. The robot and its software are split into self-contained modules. You pick whatever module interests you, work on it whenever you want, and submit your work as a pull request. Multiple people can tackle the same module — the best solution surfaces over time.

Modules ready to start right now include:

* ROS 2 URDF + Gazebo simulation— robot model, TF, bumper, sim
* First clean— coverage cleaning while SLAM-mapping and exploring
* Dust bin— design, 3D print, and test
* Vacuum fan / blower assembly— blower motor, impeller, volute housing

If you’d like to jump in, theGitHub repohas the module list, the architecture doc, and contribution guidelines.

## Follow along

I’ll be sharing progress, dead ends, and wins as they happen:

* GitHub:github.com/makerspet/oomwoo— code, docs, and discussions
* Discord:join the build chat
* YouTube:build-in-public channel
* Reddit:r/ArduinoAndRobotics
* X:@0OMWO0

### Follow OOMWOO build

Open-source robot vacuum community build updates

Subscribe

## Parts Kit

Everything about oomwoo stays open — you can source every part yourself. If you’d rather skip the parts hunt, a convenience kit (motors, PCB, brushes, gaskets, LiDAR) will be available here at Maker’s Pet, from the same maker behind this project. The kit is a convenience,never a requirement.

## More oomwoo: repos & tutorials

* Main project(RFCs, BOM, design docs):github.com/makerspet/oomwoo
* oomwoo-one— first model, ROS 2 + Gazebo simulation:github.com/makerspet/oomwoo-one
* oomwoo-install— ROS 2 / Docker dev environment:github.com/makerspet/oomwoo-install
* Tutorial:How to source the BOM for oomwoo
Tags
#
 3D Printing
#
 ESP32
#
 Featured
#
 Gazebo
#
 Home Assistant
#
 LiDAR
#
 micro-ROS
#
 OOMWOO
#
 Raspberry Pi
#
 Robot Vacuum
#
 ROS 2