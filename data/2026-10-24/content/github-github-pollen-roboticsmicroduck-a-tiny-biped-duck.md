---
title: 'GitHub - pollen-robotics/microduck: A Tiny biped duck robot 🦆 · GitHub'
url: https://github.com/pollen-robotics/microduck
site_name: github
content_file: github-github-pollen-roboticsmicroduck-a-tiny-biped-duck
fetched_at: '2026-10-24T14:29:31.974785'
original_url: https://github.com/pollen-robotics/microduck
author: pollen-robotics
description: A Tiny biped duck robot 🦆. Contribute to pollen-robotics/microduck development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,392 Commits
1,392 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.github/
workflows
.github/
workflows
 
 
btd
btd
 
 
configd
configd
 
 
deploy
deploy
 
 
docs
docs
 
 
duck-ble
duck-ble
 
 
duck-control
duck-control
 
 
duck-detect
duck-detect
 
 
duck-ether
duck-ether
 
 
duck-ipc-proto
duck-ipc-proto
 
 
duckctl
duckctl
 
 
hooks
hooks
 
 
kinematics
kinematics
 
 
mediad
mediad
 
 
netpadd
netpadd
 
 
nfc
nfc
 
 
odometry
odometry
 
 
pad-imu
pad-imu
 
 
pad-map
pad-map
 
 
padd
padd
 
 
pet-detect
pet-detect
 
 
robotctl
robotctl
 
 
robotd-params
robotd-params
 
 
robotd
robotd
 
 
scripts
scripts
 
 
sounds
sounds
 
 
spaces
spaces
 
 
test-support
test-support
 
 
tof
tof
 
 
updater
updater
 
 
uyvy
uyvy
 
 
xtask
xtask
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Microduck

A tiny biped robot that moves using reinforcement learning policies.

Get yours here·Cheat sheet·Training the policies·How it works·Contributing

This repo is the duck's brain.About 25 cm and 800 g of robot, run by a handful of daemons on a
Rockchip RK3566: a 50 Hz control loop driving fifteen servos from neural policies, the radios and
the camera, and the update machinery that gets new software onto a robot without bricking it.

Everything you need to run a Microduck is here.If you want one,get yours here.

The policies it runs are trained next door, inmicroduck_rl— MuJoCo and PPO, the sim2real
recipe, and the export to ONNX that this repo loads.

## It does things

walk.MP4

roller_cut.mp4

It walks.
 Pick up a gamepad and drive.

It rolls.
 Put wheels on, ask for roller mode, and it loads the other brain.

grasp.MP4

standup.MP4

It picks things up.
 Beak to the floor, one button.

It gets back up.
 Knock it over and it stands itself up.

It also sits, kicks a ball, rolls forward on command, and quacks in a voice that is its own.

## Where to find things

### You have a duck

Cheat sheet

Every 
robotctl
 command: drive, configure, voice, chorale, theremin, wifi, updates, logs. Start here.

Gamepad

The full button mapping, and pairing a pad — 
once per pad
, plus what to do when it will not bond.

duckctl

The robot from a laptop over Bluetooth, with no network and no ssh.

Updates

Install, roll back, pin. Every update is verified, health-gated and reversible.

### You are building on it

microduck_rl

Where the policies come from: MuJoCo, PPO, domain randomisation, and the ONNX export this repo loads.

How it works

The whole system on one page — the daemons, the bus, how an update reaches a robot — then a page per part.

Set up a dev board

From a blank board to a robot that takes branch builds.

Dev cheat sheet

Branch builds, release candidates, driving from a laptop, and the restart traps after an update.

Push your branch

Build on your machine, install over ssh, about a minute.

The simulated duck

No robot on the desk? 
scripts/duck-sim
 runs the real daemons against a body in MuJoCo — one duck in a window, or four as machines you log into.

CONTRIBUTING.md

Building, testing, layout, conventions, releasing.

Docs index

Everything, including the design pages and the open problems.

## Under the hood

Rust, no framework, one workspace.robotdowns the control loop and the motor bus;updaterdinstalls signed releases and rolls them back when a robot comes up unhealthy;configdowns wifi
and identity;btdis the Bluetooth path a phone uses;paddreads the gamepad;mediadstreams
the camera over WebRTC;tofdserves the depth sensor. They talk over one JSON-RPC contract on
Unix sockets, and every client — the app, the console, the gamepad, your script — sends exactly the
same calls.

The interesting decisions are written down:docs/design/is why things are the
way they are, anddocs/project/is what has gone wrong and what would close it.

## A note on ducks

No duck was harmed in the making of this robot. Several were consulted.