---
title: Bimo, an open-source bipedal robotics kit with sim-to-real transfer - Projects - Open Robotics Discourse
url: https://discourse.openrobotics.org/t/bimo-an-open-source-bipedal-robotics-kit-with-sim-to-real-transfer/57846
site_name: tldr
content_file: tldr-bimo-an-open-source-bipedal-robotics-kit-with-sim
fetched_at: '2026-09-06T13:57:21.635067'
original_url: https://discourse.openrobotics.org/t/bimo-an-open-source-bipedal-robotics-kit-with-sim-to-real-transfer/57846
date: '2026-09-06'
published_date: '2026-09-03T15:01:27+00:00'
description: Bimo is an open-source bipedal robot built to make bipedal robotics research accessible in a compact, affordable platform. It ships either as a fully assembled SLS Kit (ready to walk out of the box) or as a DIY Kit wh…
tags:
- tldr
---

# Bimo, an open-source bipedal robotics kit with sim-to-real transfer

Projects

ros2
, 
 
drl
, 
 
simulation
, 
 
isaac-sim

Mekion

 September 3, 2026, 3:01pm
 

1

Bimo SLS1920×1920 370 KB

Bimois an open-source bipedal robot built to make bipedal robotics research accessible in a compact, affordable platform. It ships either as a fully assembledSLS Kit(ready to walk out of the box) or as aDIY Kitwhere you print the parts yourself and assemble the robot.

## What you can use it for

* Learning and prototyping RL legged locomotionwith a real sim-to-real pipeline in Isaac Lab including distillation scripts for RL policy deployment on limited hardware (MCU).
* A teaching platform for robotics courses, as it covers RL deployment, computer vision, embedded C++/Python, and control loops in one small robot.
* A research basefor custom payloads (vision, SLAM, extra compute) thanks to the empty head cavity with M3 mounts and up to 1 kg payload support.
* Experimenting on legged locomotion algorithmssuch as getting Bimo walking immediately with a built-in CPG gait, customizing your own RL policies or designing other control methods.

## Main Specifications

Feature

Spec

Height

45 cm

Weight

~1.6 kg (no payload)

Payload

Up to 1 kg head-mounted

Actuators

8 × STS-3215 servos

Sensors

BNO08x 9-DOF IMU, 4× TOF sensors, 2× 180° FOV cameras

Controller

Custom RP2040-based board, compatible with SBCs

Control loop

20 Hz

Compute

Offboard PC, onboard SBC, or fully standalone on RP2040 (distilled RL or CPG)

## Fully Open-Source

CAD files (coming soon), RP2040 firmware, the Isaac Lab training environment, and a Python API are all released under Apache 2.0. There’s also a ROS 2 wrapper around the Python API for anyone who is more used to working with the ROS2 ecosystem.

## Current Project Status

v1.1.0has been published on GitHub: Bimo walks omnidirectionally with a stable CPG gait and sim-to-real works for forward walking with the RL policy. The project is in pre-order status before going into the CE/FCC certification and shipping.

* GitHub:the-bimo-project
* Website:mekion.com
* Discord:Mekion | The Bimo Project

Happy to answer any technical questions here. This is my first serious project and I’d love feedback from people building legged robots and working with ROS2 and RL.

3 Likes

ROS News of the Week for August 31st, 2026

### Related topics

Topic

Replies

Views

Activity

ROS News of the Week for August 31st, 2026

Community News

weekly-update

0

175

 September 4, 2026
 

🤖 Introducing MoboBot: An Open-source ROS2 Mobile Robot for Hands-on Learning and Development

Projects

ros2

 , 
 
development

 , 
 
humble

 , 
 
open-source

3

847

 March 12, 2026
 

Learn ROS 2 with a LIMO Robot - ROS Developers OpenClass #182

Training & Education

ros2

 , 
 
robotics

0

2771

 February 23, 2024
 

ROS Developers Open Class #136: Setup ROSbot to run ROS2

Training & Education

ros2

0

572

 February 7, 2022
 

Best Robotics Kit

ROS General

ros2

6

3222

 March 3, 2022