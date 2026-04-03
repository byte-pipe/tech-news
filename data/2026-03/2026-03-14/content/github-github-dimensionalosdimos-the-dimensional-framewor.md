---
title: 'GitHub - dimensionalOS/dimos: The Dimensional Framework · GitHub'
url: https://github.com/dimensionalOS/dimos
site_name: github
content_file: github-github-dimensionalosdimos-the-dimensional-framewor
fetched_at: '2026-03-14T11:08:59.858737'
original_url: https://github.com/dimensionalOS/dimos
author: dimensionalOS
description: The Dimensional Framework. Contribute to dimensionalOS/dimos development by creating an account on GitHub.
---

dimensionalOS

 

/

dimos

Public

* NotificationsYou must be signed in to change notification settings
* Fork142
* Star697

 
 
 
 
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

566 Commits
566 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
assets
assets
 
 
bin
bin
 
 
data/
.lfs
data/
.lfs
 
 
dimos
dimos
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.envrc.nix
.envrc.nix
 
 
.envrc.venv
.envrc.venv
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
.style.yapf
.style.yapf
 
 
AGENTS.md
AGENTS.md
 
 
CLA.md
CLA.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
default.env
default.env
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

## The Agentive Operating System for Physical Space

Hardware•Installation•Agent CLI & MCP•Blueprints•Development

⚠️Pre-Release Beta⚠️

# Intro

Dimensional is the modern operating system for generalist robotics. We are setting the next-generation SDK standard, integrating with the majority of robot manufacturers.

With a simple install and no ROS required, build physical applications entirely in python that run on any humanoid, quadruped, or drone.

Dimensional is agent native -- "vibecode" your robots in natural language and build (local & hosted) multi-agent systems that work seamlessly with your hardware. Agents run as native modules — subscribing to any embedded stream, from perception (lidar, camera) and spatial memory down to control loops and motor drivers.

### Navigation and Mapping

 SLAM, dynamic obstacle avoidance, route planning, and autonomous exploration — via both DimOS native and ROS
Watch video

### Perception

 Detectors, 3d projections, VLMs, Audio processing
 

### Agentive Control, MCP

 "hey Robot, go find the kitchen"
Watch video

### Spatial Memory

 Spatio-temporal RAG, Dynamic memory, Object localization and permanence
Watch video

# Hardware

### Quadruped

### Humanoid

### Arm

### Drone

### Misc

 🟩 
Unitree Go2 pro/air

 🟥 
Unitree B1

 🟨 
Unitree G1

 🟨 
Xarm

 🟨 
AgileX Piper

 🟧 
MAVLink

 🟧 
DJI Mavic

 🟥 
Force Torque Sensor

🟩 stable 🟨 beta 🟧 alpha 🟥 experimental

Important

🤖 Direct your favorite Agent (OpenClaw, Claude Code, etc.) toAGENTS.mdand ourCLI and MCPinterfaces to start building powerful Dimensional applications.

# Installation

## Interactive Install

curl -fsSL https://raw.githubusercontent.com/dimensionalOS/dimos/main/scripts/install.sh 
|
 bash

Seescripts/install.sh --helpfor non-interactive and advanced options.

## Manual System Install

To set up your system dependencies, follow one of these guides:

* 🟩Ubuntu 22.04 / 24.04
* 🟩NixOS / General Linux
* 🟧macOS

Full system requirements, tested configs, and dependency tiers:docs/requirements.md

## Python Install

### Quickstart

uv venv --python 
"
3.12
"

source
 .venv/bin/activate
uv pip install 
'
dimos[base,unitree]
'

#
 Replay a recorded quadruped session (no hardware needed)

#
 NOTE: First run will show a black rerun window while ~75 MB downloads from LFS

dimos --replay run unitree-go2

#
 Install with simulation support

uv pip install 
'
dimos[base,unitree,sim]
'

#
 Run quadruped in MuJoCo simulation

dimos --simulation run unitree-go2

#
 Run humanoid in simulation

dimos --simulation run unitree-g1-sim

#
 Control a real robot (Unitree quadruped over WebRTC)

export
 ROBOT_IP=
<
YOUR_ROBOT_IP
>

dimos run unitree-go2

# Featured Runfiles

Run command

What it does

dimos --replay run unitree-go2

Quadruped navigation replay — SLAM, costmap, A* planning

dimos --replay --replay-dir unitree_go2_office_walk2 run unitree-go2-temporal-memory

Quadruped temporal memory replay

dimos --simulation run unitree-go2-agentic-mcp

Quadruped agentic + MCP server in simulation

dimos --simulation run unitree-g1

Humanoid in MuJoCo simulation

dimos --replay run drone-basic

Drone video + telemetry replay

dimos --replay run drone-agentic

Drone + LLM agent with flight skills (replay)

dimos run demo-camera

Webcam demo — no hardware needed

dimos run keyboard-teleop-xarm7

Keyboard teleop with mock xArm7 (requires 
dimos[manipulation]
 extra)

dimos --simulation run unitree-go2-agentic-ollama

Quadruped agentic with local LLM (requires 
Ollama
 + 
ollama serve
)

Full blueprint docs:docs/usage/blueprints.md

# Agent CLI and MCP

ThedimosCLI manages the full lifecycle — run blueprints, inspect state, interact with agents, and call skills via MCP.

dimos run unitree-go2-agentic-mcp --daemon 
#
 Start in background

dimos status 
#
 Check what's running

dimos log -f 
#
 Follow logs

dimos agent-send 
"
explore the room
"
 
#
 Send agent a command

dimos mcp list-tools 
#
 List available MCP skills

dimos mcp call relative_move --arg forward=0.5 
#
 Call a skill directly

dimos stop 
#
 Shut down

Full CLI reference:docs/usage/cli.md

# Usage

## Use DimOS as a Library

See below a simple robot connection module that sends streams of continuouscmd_velto the robot and receivescolor_imageto a simpleListenermodule. DimOS Modules are subsystems on a robot that communicate with other modules using standardized messages.

import
 
threading
, 
time
, 
numpy
 
as
 
np

from
 
dimos
.
core
.
blueprints
 
import
 
autoconnect

from
 
dimos
.
core
.
core
 
import
 
rpc

from
 
dimos
.
core
.
module
 
import
 
Module

from
 
dimos
.
core
.
stream
 
import
 
In
, 
Out

from
 
dimos
.
msgs
.
geometry_msgs
 
import
 
Twist

from
 
dimos
.
msgs
.
sensor_msgs
 
import
 
Image
, 
ImageFormat

class
 
RobotConnection
(
Module
):
 
cmd_vel
: 
In
[
Twist
]
 
color_image
: 
Out
[
Image
]

 
@
rpc

 
def
 
start
(
self
):
 
threading
.
Thread
(
target
=
self
.
_image_loop
, 
daemon
=
True
).
start
()

 
def
 
_image_loop
(
self
):
 
while
 
True
:
 
img
 
=
 
Image
.
from_numpy
(
 
np
.
zeros
((
120
, 
160
, 
3
), 
np
.
uint8
),
 
format
=
ImageFormat
.
RGB
,
 
frame_id
=
"camera_optical"
,
 )
 
self
.
color_image
.
publish
(
img
)
 
time
.
sleep
(
0.2
)

class
 
Listener
(
Module
):
 
color_image
: 
In
[
Image
]

 
@
rpc

 
def
 
start
(
self
):
 
self
.
color_image
.
subscribe
(
lambda
 
img
: 
print
(
f"image 
{
img
.
width
}
x
{
img
.
height
}
"
))

if
 
__name__
 
==
 
"__main__"
:
 
autoconnect
(
 
RobotConnection
.
blueprint
(),
 
Listener
.
blueprint
(),
 ).
build
().
loop
()

## Blueprints

Blueprints are instructions for how to construct and wire modules. We compose them withautoconnect(...), which connects streams by(name, type)and returns aBlueprint.

Blueprints can be composed, remapped, and have transports overridden ifautoconnect()fails due to conflicting variable names orIn[]andOut[]message types.

A blueprint example that connects the image stream from a robot to an LLM Agent for reasoning and action execution.

from
 
dimos
.
core
.
blueprints
 
import
 
autoconnect

from
 
dimos
.
core
.
transport
 
import
 
LCMTransport

from
 
dimos
.
msgs
.
sensor_msgs
 
import
 
Image

from
 
dimos
.
robot
.
unitree
.
go2
.
connection
 
import
 
go2_connection

from
 
dimos
.
agents
.
agent
 
import
 
agent

blueprint
 
=
 
autoconnect
(
 
go2_connection
(),
 
agent
(),
).
transports
({(
"color_image"
, 
Image
): 
LCMTransport
(
"/color_image"
, 
Image
)})

# Run the blueprint

if
 
__name__
 
==
 
"__main__"
:
 
blueprint
.
build
().
loop
()

## Library API

* Modules
* LCM
* Blueprints
* Transports— LCM, SHM, DDS, ROS 2
* Data Streams
* Configuration
* Visualization

## Demos

# Development

## Develop on DimOS

export
 GIT_LFS_SKIP_SMUDGE=1
git clone -b dev https://github.com/dimensionalOS/dimos.git

cd
 dimos

uv sync --all-extras --no-extra dds

#
 Run fast test suite

uv run pytest dimos

## Multi Language Support

Python is our glue and prototyping language, but we support many languages via LCM interop.

Check our language interop examples:

* C++
* Lua
* TypeScript

## About

The Dimensional Framework

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

697

 stars
 

### Watchers

11

 watching
 

### Forks

142

 forks
 

 Report repository

 

## Releases11

Release v0.0.11: Dimensional now fully Agent-native, Interactive Visualizer, Drones, Temporal Memory, Fleet control

 Latest

 

Mar 12, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python92.5%
* Shell1.9%
* TypeScript1.5%
* C++1.4%
* HTML1.2%
* Dockerfile0.6%
* Other0.9%