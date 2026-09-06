---
title: Bimo, an open-source bipedal robotics kit with sim-to-real transfer - Projects - Open Robotics Discourse
url: https://discourse.openrobotics.org/t/bimo-an-open-source-bipedal-robotics-kit-with-sim-to-real-transfer/57846
date: 2026-09-06
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-06T13:58:20.653021
---

# Bimo, an open-source bipedal robotics kit with sim-to-real transfer - Projects - Open Robotics Discourse

# Bimo, an open-source bipedal robotics kit with sim-to-real transfer

## Overview
Bimo is an open-source bipedal robot designed for easy access to bipedal robotics research and development. It ships as a fully assembled kit or DIY kit where users can print the parts themselves and assemble the robot. Bimo is ideal for learning and prototyping legged locomotion with a real sim-to-real pipeline in Isaac Lab, a popular robotics simulation environment.

## Key Features

* Compatible with various operating systems, including ROS 2, and is designed to be fully open-source
* Includes a custom RP2040-based board, compatible with SiFive-based hardware
* Features multiple actuators, sensors, and control components, allowing for customized control and payload support
* Supports up to 1 kg payload, with a head-mounted payload of up to 1 kg

## Technical Specifications

* Features
  * 45 cm height
  * 1.6 kg weight
  * Customized payload capacity of up to 1 kg
  * Actuators: 8 x STS-3215 servos
  * Sensors: BNO08x 9-DOF IMU, 4 x TOF sensors, 2 x 180° FOV cameras
  * Control loop: 20 Hz
* Components and tools:
  * Custom RP2040-based board
  * CAD files (coming soon)
  * RP2040 firmware
  * Isaac Lab training environment
  * Python API
  * ROS 2 wrapper

## Features and Capabilities

* Sim-to-real transfer to enable real-world testing and validation
* Omnidirectional movement capability with a stable CPG gait
* Forward walking capability with the RL policy, and simulation support for advanced features
* Customizable control methods and payload support
* A variety of sensors and actuator configurations available

## Projects and Resources

* GitHub: [bimo-project](https://github.com/bimo-project)
* Website: [mekion.com](http://mekion.com)
* Discord: [Mekion | The Bimo Project](https://discord.com/invite/mekion-the-bimo-Project)

* Related topics: ROS News of the Week, MoboBot, ROS Developers OpenClass #182, ROS Developers Open Class #136, and ROS Ge
* Community news: weekly-update and ROS Developers Open Class #2771
* Training and education resources: Learn ROS 2 with a LIMO Robot, ROS Developers Open Class #136, and Best Robotics Kit