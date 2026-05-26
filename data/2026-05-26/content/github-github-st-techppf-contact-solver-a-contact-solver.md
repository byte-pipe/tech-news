---
title: 'GitHub - st-tech/ppf-contact-solver: A contact solver for physics-based simulations involving 👚 shells, 🪵 solids and 🪢 rods. · GitHub'
url: https://github.com/st-tech/ppf-contact-solver
site_name: github
content_file: github-github-st-techppf-contact-solver-a-contact-solver
fetched_at: '2026-05-26T19:41:29.094100'
original_url: https://github.com/st-tech/ppf-contact-solver
author: st-tech
description: A contact solver for physics-based simulations involving 👚 shells, 🪵 solids and 🪢 rods. - st-tech/ppf-contact-solver
---

st-tech

 

/

ppf-contact-solver

Public

* NotificationsYou must be signed in to change notification settings
* Fork245
* Star3.4k

 
 
 
 
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

359 Commits
359 Commits
.github
.github
 
 
articles
articles
 
 
asset/
image
asset/
image
 
 
blender_addon
blender_addon
 
 
build-win-native
build-win-native
 
 
crates
crates
 
 
docs
docs
 
 
eigsys
eigsys
 
 
examples
examples
 
 
frontend
frontend
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.markdownlint.json
.markdownlint.json
 
 
CITATION.cff
CITATION.cff
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build-all.sh
build-all.sh
 
 
docker-build.sh
docker-build.sh
 
 
install-blender-addon.ps1
install-blender-addon.ps1
 
 
install-blender-addon.sh
install-blender-addon.sh
 
 
install-blender.sh
install-blender.sh
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.json
pyrightconfig.json
 
 
warmup.py
warmup.py
 
 
View all files

## Repository files navigation

# ZOZO's Contact Solver 🫶

A contact solver for physics-based simulations
involving 👚 shells, 🪵 solids and 🪢 rods. All made byZOZO, Inc., the largest fashion e-commerce company in Japan.

🤖 Wehighlyrespect that readers expect to hear the author's original voice and tone, which we work to retain throughout. Our use of LLMs is clarified in(Markdown).

## 👀 Quick Look

🎨 Simulate remotely from ourBlender add-on(screenshots taken on macOS; you can also run locally if you have a modern NVIDIA GPU on Windows or Linux)

blender-addon-trailer-2026.mp4

🚀 Or double clickstart.bat(Windows) or run a Docker command (Linux/Windows) to get it running

🌐 Click the URL and explore our examples

## ✨ Highlights

* 💪 Robust: Contact resolutions are penetration-free. No snagging intersections.
* ⏲ Scalable: An extreme case includes beyond 180M contacts. Not just one million.
* 🚲 Cache Efficient: All on the GPU runs in single precision. No double precision.
* 🥼 Not Rubbery: Triangles never extend beyond strict upper bounds (e.g., 1%).
* 📐 Finite Element Method: We use FEM for deformables and symbolic force jacobians.
* ⚔️ Highly Stressed: We run GitHub Actions to run stress tests10 times in a row.
* 🚀 Massively Parallel: Both contact and elasticity solvers are run on the GPU.
* 🪟 Windows Executable: No installation wizard shown. Just unzip and run(Video).
* 🐳 Docker Sealed: All can be deployed fast. The image is ~1GB.
* 🌐 JupyterLab Included: Open your browser and run examples right away(Video).
* 🐍 Documented Python APIs: Our Python code is fullydocstringedand lintable(Video).
* ☁️ Cloud-Ready: Our solver can be seamlessly deployed on major cloud platforms.
* 🎨 Blender Add-on: Simulate remotely and fetch results locally, even on macOS.
* 🤖 MCP Support: Let a LLM run simulations for you using natural language.
* ✨ Stay Clean: You can remove all traces after use.
* 📜 Permissive License: Apache 2.0 allows commercial and proprietary use.

⚠️Built for offline uses; not real time. Some examples may run at an interactive rate.

## 🔖 Table of Contents

* 📝 Change History
* 🎓 Technical Materials
* ⚡️ Requirements
* 💨 Getting Started🪟 Windows Native Executable🐳 Docker (Linux and Windows)
* 🪟 Windows Native Executable
* 🐳 Docker (Linux and Windows)
* 🐍 How To Use🎨 Blender Add-on🌐 JupyterLab📚 Python APIs and Parameters
* 🎨 Blender Add-on
* 🌐 JupyterLab📚 Python APIs and Parameters
* 📚 Python APIs and Parameters
* 🔍 Obtaining Logs
* 🖼️ Catalogue🎨 Blender Add-on Examples🌐 JupyterLab Examples💰 Budget Table on AWS🏗️ Large Scale Examples
* 🎨 Blender Add-on Examples
* 🌐 JupyterLab Examples
* 💰 Budget Table on AWS
* 🏗️ Large Scale Examples
* 🚀 GitHub Actions⚔️ Ten Consecutive Runs📦 Action Artifacts
* ⚔️ Ten Consecutive Runs
* 📦 Action Artifacts
* 📡 Deploying on Cloud Services📦 Deploying on vast.ai📦 Deploying on Scaleway📦 Deploying on Amazon Web Services📦 Deploying on Google Compute Engine
* 📦 Deploying on vast.ai
* 📦 Deploying on Scaleway
* 📦 Deploying on Amazon Web Services
* 📦 Deploying on Google Compute Engine
* 🤝 Community Works🧩 Blender Add-ons📺 Videos📰 Articles📣 Sharing Your Work
* 🧩 Blender Add-ons
* 📺 Videos
* 📰 Articles
* 📣 Sharing Your Work
* 💼 Commercial Use and Beyond
* 📬 Contributing
* 💬 Participating Discussions
* 📨 Reaching the Author
* 🙏 Acknowledgements

### 📚 Advanced Contents

* 🧑 Setting Up Your Development Environment(Markdown)
* 🐞 Bug Fixes and Updates(Markdown)

## 📝 Change History

* (2026.04.30) Added a Blender Add-on support. See thedocumentation.
* (2025.12.18) Added native Windows standalone executable build support(Video).
* (2025.11.26) Addedlarge-woven.ipynb(Video)tolarge scale examples.
* (2025.11.12) Addedfive-twist.ipynb(Video)andlarge-five-twist.ipynb(Video)showcasing over 180M count. Seelarge scale examples.
* (2025.10.03) Massive refactor of the codebase(Markdown). Note that this change includes breaking changes to our Python APIs.
* (2025.08.09) Added a hindsight note ineigensystem analysisto acknowledge prior work byPoya et al. (2023).
* (2025.05.01) Simulation states now can be saved and loaded(Video).

More history records

- (2025.04.02) Added 9 examples. See the [catalogue](#️-catalogue).
- (2025.03.03) Added a [budget table on AWS](#-budget-table-on-aws).
- (2025.02.28) Added a [reference branch and a Docker image of our TOG paper](#-technical-materials).
- (2025.02.26) Added Floating Point-Rounding Errors in ACCD in [hindsight](./articles/hindsight.md).
- (2025.02.07) Updated the [trapped example](./examples/trapped.ipynb) [(Video)](
https://zozo.box.com/s/lnnyeqrvm86rxnwyjxhojfj0jgm5nphn
) with squishy balls.
- (2025.03.03) Added a [budget table on AWS](#-budget-table-on-aws).
- (2025.02.28) Added a [reference branch and a Docker image of our TOG paper](#-technical-materials).
- (2025.02.26) Added Floating Point-Rounding Errors in ACCD in [hindsight](./articles/hindsight.md).
- (2025.02.07) Updated the [trapped example](./examples/trapped.ipynb) [(Video)](
https://zozo.box.com/s/lnnyeqrvm86rxnwyjxhojfj0jgm5nphn
) with squishy balls.
- (2025.1.8) Added a [domino example](./examples/domino.ipynb) [(Video)](
https://zozo.box.com/s/p5ksfqja1ew3c6vntco5zq6g0kgf7xoo
).
- (2025.1.5) Added a [single twist example](./examples/twist.ipynb) [(Video)](
https://zozo.box.com/s/4phoyyeertd2mcfv436kp2ojmo1x0eio
).
- (2024.12.31) Added full documentation for Python APIs, parameters, and log files [(GitHub Pages)](
https://st-tech.github.io/ppf-contact-solver
).
- (2024.12.27) Line search for strain limiting is improved [(Markdown)](./articles/bug.md#new-strain-limiting-line-search)
- (2024.12.23) Added [(Bug Fixes and Updates)](./articles/bug.md)
- (2024.12.21) Added a [house of cards example](./examples/cards.ipynb) [(Video)](
https://zozo.box.com/s/7c114pua0107xkz4nc3bwfdzpkhgn1o9
)
- (2024.12.18) Added a [frictional contact example](./examples/friction.ipynb): armadillo sliding on the slope [(Video)](
https://zozo.box.com/s/15r5o7rrowwtbrsrjjpj35v8xt92ufhr
)
- (2024.12.18) Added a [hindsight](./articles/hindsight.md) noting that the tilt angle was not 
$30^\circ$
, but rather 
$26.57^\circ$

- (2024.12.16) Removed thrust dependencies to fix runtime errors for the driver version `560.94` [(Issue Link)](
#1
)

## 🎓 Technical Materials

#### 📘A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness

siga2024-main-mini.mp4

* 📚 Published inACM Transactions on Graphics (TOG) Vol.43, No.6
* 🎥 Main video(Video)
* 🎥 Additional video examples(Directory)
* 🎥 Presentation videos(Short)(Long)
* 📃 Main paper(PDF)(Hindsight)
* 📊 Supplementary PDF(PDF)
* 🤖 Supplementary scripts(Directory)
* 🔍 Singular-value eigenanalysis(Markdown)

##### 📌 Reference Implementation

The main branch is undergoing frequent updates and will deviate from the paper.
To retain consistency with the paper, we have created a new branchsigasia-2024.

* 🛠️ Only maintenance updates are planned for this branch.
* 🚫 General usersshould notuse this branch as it is not optimized for best performance.
* 🚫 All algorithmic changes listed in this(Markdown)are excluded from this branch.
* 📦 We also provide a pre-compiled Docker image:ghcr.io/st-tech/ppf-contact-solver-compiled-sigasia-2024:latestof this branch.
* 🌐Template Link for vast.ai

## ⚡️ Requirements

* 🔥 An NVIDIA GPU with CUDA 12.8 or newer support. The RTX 4090 or 5090 is ideal for large-scale simulations, while the RTX 3090, 4070, or 5070 remains suitable for small to medium-scale workloads.
* 💻 x86 architecture (arm64 is not supported)
* 🐳 A Docker environment (seebelow) or 🪟 Windows 10/11 for native executable (seebelow)
* 🎨 Blender 5+ (only if you intend to use the Blender add-on)

## 💨 Getting Started

Whether you plan to use the Blender add-on or the JupyterLab interface, the solver engine itself must first be deployed. The steps below apply to both.

⚠️Do not runwarmup.pylocally. If you do, you are very likely to hit failures and find it difficult to cleanup.

#### 🪟 Windows Native Executable

For Windows 10/11 users, a self-contained executable (~320MB) is available.
No Python, Docker, or CUDA Toolkit installation is needed.
All should simply work out of the box(Video).

🤔 If you are cautious, you can review thebuild workflowto verify safety yourself.
We try to maximize transparency;we never build locally and upload.

1. Install the latest NVIDIA driver(Link)
2. Download the latest release fromGitHub Releasesand unzip
3. Double clickstart.bat

JupyterLab frontend will auto-start. You should be able to access it athttp://localhost:8080.

#### 🐳 Docker (Linux and Windows)

Install a NVIDIA driver(Link)on your host system and follow the instructions below specific to the operating system to get a Docker running:

🐧 Linux

🪟 Windows

Install the Docker engine from here 
(Link)
. Also, install the NVIDIA Container Toolkit 
(Link)
. Just to make sure that the Container Toolkit is loaded, run 
sudo service docker restart
.

Install the Docker Desktop 
(Link)
. You may need to log out or reboot after the installation. After logging back in, launch Docker Desktop to ensure that Docker is running.

Next, run the following command to start the container. If no edits are needed, just copy and paste:

##### 🪟 Windows (PowerShell)

$MY_WEB_PORT
 = 8080 
#
 JupyterLab port on your side

$MY_BLENDER_PORT
 = 9090 
#
 Solver port for the Blender add-on

$IMAGE_NAME
 = 
"
ghcr.io/st-tech/ppf-contact-solver-compiled:latest
"

docker run --rm -it 
`

 --name ppf-contact-solver 
`

 --gpus all 
`

 -p 
${MY_WEB_PORT}
:
${MY_WEB_PORT}
 
`

 -p 
${MY_BLENDER_PORT}
:
${MY_BLENDER_PORT}
 
`

 -e WEB_PORT=
${MY_WEB_PORT}
 
`

 
$IMAGE_NAME
 
#
 Image size ~1GB

##### 🐧 Linux (Bash/Zsh)

MY_WEB_PORT=8080 
#
 JupyterLab port on your side

MY_BLENDER_PORT=9090 
#
 Solver port for the Blender add-on

IMAGE_NAME=ghcr.io/st-tech/ppf-contact-solver-compiled:latest
docker run --rm -it \
 --name ppf-contact-solver \
 --gpus all \
 -p 
${MY_WEB_PORT}
:
${MY_WEB_PORT}
 \
 -p 
${MY_BLENDER_PORT}
:
${MY_BLENDER_PORT}
 \
 -e WEB_PORT=
${MY_WEB_PORT}
 \
 
$IMAGE_NAME
 
#
 Image size ~1GB

The image download shall be started.
Our image is hosted onGitHub Container Registry(~1GB).
JupyterLab will then auto-start.
Eventually you should be seeing:

==== JupyterLab Launched! 🚀 ====
 http://localhost:8080
 Press Ctrl+C to shutdown
================================

Next, open your browser and navigate tohttp://localhost:8080. The port8080can change if you change theMY_WEB_PORTvariable.
Keep your terminal window open.
Now you are ready to go! 🎉

#### 🛑 Shutting Down

To shut down the container, just pressCtrl+Cin the terminal.
The container will be removed and all traces will be cleaned up. 🧹

If you wish to keep the container running in the background, replace--rmwith-d. To shutdown the container and remove it, rundocker stop ppf-contact-solver && docker rm ppf-contact-solver.

#### 🔧 Advanced Installation

If you wish to build the docker image from scratch, please refer to the cleaner installation guide(Markdown).

## 🐍 How To Use

We provide two frontends: a Blender add-on and a JupyterLab interface. The Blender add-on lets you build scenes and run simulations entirely within Blender's UI, while JupyterLab lets you script everything in Python from your browser. Both communicate with the same solver engine, so pick whichever you like.

In both cases, you can interact with the simulator on your laptop while the actual simulation runs on a remote headless server over the internet.
This means thatyou don't have to own NVIDIA hardware, but can rent it atvast.aifor less than $0.5 per hour.
That said, if you do have a modern NVIDIA GPU on a local Windows or Linux machine, you can also run the solver directly on it.
Actually, this(Video)was recorded on avast.aiinstance.
The experience is good! 👍

### 🎨 Blender Add-on

Our Blender add-on aims to offer a familiar UI that best feels like everything works locally, but under the hood, it communicates with a remote server whereallsimulations run, and then the results are fetched back.

This provides a unique experience where users can leverage powerfulremoteGPUs while working seamlessly in their local Blender environment. Remarkably, our Blender add-on works even onmacOSsystems 😊, unlike other CUDA-based physics simulator add-ons that require local NVIDIA GPUs.
More importantly,you can work on a laptop without worrying about draining the battery fast. 🔋

Follow this pageHow to Installto learn how to install the add-on. For a thorough walk through workflow, we refer to our documentation below:

Here are some highlights:

#### 📖 Docs Look

We maintain afull docs sitewith workflow guides and recorded walkthroughs for the add-on:

Workflow documentation page. 
(Link)

Video tutorials page. 
(Link)

#### 🖼️ UI Look

Here are a couple of screenshots of the add-on running inside Blender:

Kite scene set up in Blender. 
(full-size)

Zebra scene set up in Blender. 
(full-size)

#### 🤖 From Natural Language to Simulation (via MCP)

We expose all of the add-on's tools through an MCP server, so any LLM (Claude, Codex, etc.) can drive the whole pipeline from a natural language prompt. Scene building, parameter tweaks, and running the simulation all happen without UI clicks. Here are two examples:

Codex (left) driving Blender (right) through the add-on's MCP server.

A prompt: drape a sheet over a sphere and make an animation video mp4 render 300 frames.

#### 🐍 From a Python Script to Simulation

You can also drive the entire pipeline from a Python script inside Blender's scripting editor. This is handy for procedural scene setup and batch variant generation. Below is a full example that drapes a sheet over a sphere:

import
 
addon_utils

import
 
importlib

import
 
bpy

# Look up the add-on module under whichever extension repository Blender

# installed it into and grab the public solver API.

addon
 
=
 
next
(
m
 
for
 
m
 
in
 
addon_utils
.
modules
() 
if
 
m
.
__name__
.
endswith
(
".ppf_contact_solver"
))

solver
 
=
 
importlib
.
import_module
(
f"
{
addon
.
__name__
}
.ops.api"
).
solver

# Reset any prior state.

solver
.
clear
()

# Create a sphere (the static collider) at the origin.

bpy
.
ops
.
mesh
.
primitive_ico_sphere_add
(
subdivisions
=
4
, 
radius
=
0.5
, 
location
=
(
0
, 
0
, 
0
))

bpy
.
context
.
object
.
name
 
=
 
"Sphere"

# Create a 2x2 sheet just above the sphere as a 64x64 grid.

bpy
.
ops
.
mesh
.
primitive_grid_add
(
x_subdivisions
=
64
, 
y_subdivisions
=
64
, 
size
=
2
, 
location
=
(
0
, 
0
, 
0.6
))

sheet
 
=
 
bpy
.
context
.
object

sheet
.
name
 
=
 
"Sheet"

# Pin the two corners on the -x edge via a vertex group.

vg
 
=
 
sheet
.
vertex_groups
.
new
(
name
=
"Corners"
)

corner_indices
 
=
 [
 
i
 
for
 
i
, 
v
 
in
 
enumerate
(
sheet
.
data
.
vertices
)
 
if
 
v
.
co
.
x
 
<
 
-
0.99
 
and
 
abs
(
abs
(
v
.
co
.
y
) 
-
 
1.0
) 
<
 
0.01

]

vg
.
add
(
corner_indices
, 
1.0
, 
"REPLACE"
)

# Build solver groups.

cloth
 
=
 
solver
.
create_group
(
"Cloth"
, 
type
=
"SHELL"
)

cloth
.
add
(
"Sheet"
)

cloth
.
param
.
enable_strain_limit
 
=
 
True

cloth
.
param
.
strain_limit
 
=
 
0.05

cloth
.
param
.
bend
 
=
 
1

ball
 
=
 
solver
.
create_group
(
"Ball"
, 
type
=
"STATIC"
)

ball
.
add
(
"Sphere"
)

# Pin the two sheet corners.

cloth
.
create_pin
(
"Sheet"
, 
"Corners"
)

# Scene parameters.

solver
.
param
.
frame_count
 
=
 
100

solver
.
param
.
step_size
 
=
 
0.01

Here's how the script runs inside Blender(full-size):

For the fullsolver.*surface, see theBlender Python API guide.

### 🌐 JupyterLab

Our frontend is accessible through a browser using our built-in JupyterLab interface.
All is set up when you open it for the first time.
Results can be interactively viewed through the browser and exported as needed.
Our Python interface is designed with the following principles in mind:

* 🛠️ In-Pipeline Tri/Tet Creation: Depending on external 3D/CAD softwares for triangulation or tetrahedralization makes dynamic resolution changes cumbersome. We provide handy.triangulate()and.tetrahedralize()calls to keep everything in-pipeline, allowing users to skip explicit mesh exports to 3D/CAD software.
* 🚫 No Mesh Data Included: Preparing mesh data using external tools can be cumbersome. Our frontend minimizes this effort by allowing meshes to be created on the fly or downloaded when needed.
* 🔗 Method Chaining: We adopt the method chaining style from JavaScript, making the API intuitive to understand and read smoothly.
* 📦 Single Import for Everything: All frontend features are accessible by simply importing withfrom frontend import App.

Here's an example of draping five sheets over a sphere with two corners pinned.
We have more examples in theexamplesdirectory. Please take a look! 👀

# import our frontend

from
 
frontend
 
import
 
App

# make an app

app
 
=
 
App
.
create
(
"drape"
)

# create a square mesh resolution 128 spanning the xz plane

V
, 
F
 
=
 
app
.
mesh
.
square
(
res
=
128
, 
ex
=
[
1
, 
0
, 
0
], 
ey
=
[
0
, 
0
, 
1
])

# add to the asset and name it "sheet"

app
.
asset
.
add
.
tri
(
"sheet"
, 
V
, 
F
)

# create an icosphere mesh radius 0.5

V
, 
F
 
=
 
app
.
mesh
.
icosphere
(
r
=
0.5
, 
subdiv_count
=
4
)

# add to the asset and name it "sphere"

app
.
asset
.
add
.
tri
(
"sphere"
, 
V
, 
F
)

# create a scene

scene
 
=
 
app
.
scene
.
create
()

# define gap between sheets

gap
 
=
 
0.01

for
 
i
 
in
 
range
(
5
):

 
# add the sheet asset to the scene with an vertical offset

 
obj
 
=
 
scene
.
add
(
"sheet"
).
at
(
0
, 
gap
 
*
 
i
, 
0
)

 
# pick two corners

 
corner
 
=
 
obj
.
grab
([
1
, 
0
, 
-
1
]) 
+
 
obj
.
grab
([
-
1
, 
0
, 
-
1
])

 
# pin the corners

 
obj
.
pin
(
corner
)

 
# set the strict limit on maximum strain to 5% per triangle

 
obj
.
param
.
set
(
"strain-limit"
, 
0.05
)

# add a sphere mesh at a lower position with jitter and set it static collider

scene
.
add
(
"sphere"
).
at
(
0
, 
-
0.5
 
-
 
gap
, 
0
).
jitter
().
pin
()

# compile the scene and report stats

scene
 
=
 
scene
.
build
().
report
()

# preview the initial scene, shows image left

scene
.
preview
()

# create a new session with the compiled scene

session
 
=
 
app
.
session
.
create
(
scene
)

# set session params

session
.
param
.
set
(
"frames"
, 
100
).
set
(
"dt"
, 
0.01
)

# build this session

session
 
=
 
session
.
build
()

# start the simulation and live-preview the results, shows image right

session
.
start
().
preview
()

# also show streaming logs

session
.
stream
()

# or interactively view the animation sequences

session
.
animate
()

# export all simulated frames in (sequences of ply meshes + a video)

session
.
export
.
animation
()

#### 📚 Python APIs and Parameters

* Full API documentation is available on ourGitHub Pages. The major APIs are documented using docstrings and compiled withSphinxWe have also includedjupyter-lspto provide interactive linting assistance and display docstrings as you type. See this video(Video)for an example.
The behaviors can be changed through the settings.
* A list of parameters used inparam.set(key,value)is documented here:(Simulation Parameters)(Material Parameters).

⚠️Please note that our Python APIs are subject to breaking changes as this repository undergoes frequent iterations. If you need APIs to be fixed, please fork.

## 🔍 Obtaining Logs

Logs for the simulation can also be queried through our Python APIs. Here's an example of how to get a list of recorded logs, fetch them, and compute the average.

# get a list of log names

logs
 
=
 
session
.
get
.
log
.
names
()

print
(
logs
)

assert
 
"time-per-frame"
 
in
 
logs

assert
 
"newton-steps"
 
in
 
logs

# get a list of time per video frame

msec_per_video
 
=
 
session
.
get
.
log
.
numbers
(
"time-per-frame"
)

# compute the average time per video frame

print
(
"avg per frame:"
, 
sum
([
n
 
for
 
_
, 
n
 
in
 
msec_per_video
]) 
/
 
len
(
msec_per_video
))

# get a list of newton steps

newton_steps
 
=
 
session
.
get
.
log
.
numbers
(
"newton-steps"
)

# compute the average of consumed newton steps

print
(
"avg newton steps:"
, 
sum
([
n
 
for
 
_
, 
n
 
in
 
newton_steps
]) 
/
 
len
(
newton_steps
))

# Last 8 lines. Omit for everything.

print
(
"==== log stream ===="
)

for
 
line
 
in
 
session
.
get
.
log
.
stdout
(
n_lines
=
8
):
 
print
(
line
)

Below are some representatives.vid_timerefers to the video time in seconds and is recorded asfloat.msrefers to the consumed simulation time in milliseconds recorded asint.vid_frameis the video frame count recorded asint.

Name

Description

Format

time-per-frame

Time per video frame

list[(vid_frame,ms)]

matrix-assembly

Matrix assembly time

list[(vid_time,ms)]

pcg-linsolve

Linear system solve time

list[(vid_time,ms)]

line-search

Line search time

list[(vid_time,ms)]

time-per-step

Time per step

list[(vid_time,ms)]

newton-steps

Newton iterations per step

list[(vid_time,count)]

num-contact

Contact count

list[(vid_time,count)]

max-sigma

Max stretch

list(vid_time,float)

The full list of log names and their descriptions is documented here:(GitHub Pages).

Note that some entries have multiple records at the same video time. This occurs because the same operation is executed multiple times within a single step during the inner Newton's iterations. For example, the linear system solve is performed at each Newton's step, so if multiple Newton's steps are executed, multiple linear system solve times appear in the record at the same video time.

If you would like to retrieve the raw log stream, you can do so by

# Last 8 lines. Omit for everything.

for
 
line
 
in
 
session
.
get
.
log
.
stdout
(
n_lines
=
8
):
 
print
(
line
)

This will output something like:

* dt: 1.000e-03
* max_sigma: 1.045e+00
* avg_sigma: 1.030e+00
------ newton step 1 ------
 ====== contact_matrix_assembly ======
 > dry_pass...0 msec
 > rebuild...7 msec
 > fillin_pass...0 msec

If you would like to readstderr, you can do so usingsession.get.stderr()(if it exists).
This returnslist[str].
All the log files are updated in real-time and can be fetched right after the simulation starts; you don't have to wait until it finishes.

## 🖼️ Catalogue

### 🎨 Blender Add-on Examples

These scenes are all built with ouradd-on. The simulation itself runs on a remote solver, or directly on your local machine if you have a modern NVIDIA GPU on Windows or Linux.

You set the geometry, constraints, and parameters from Blender's UI, and the saved.blendcarries everything the add-on needs.

kite.blend
 
(Video)

crumple.blend
 
(Video)

puff.blend
 
(Video)

press.blend
 
(Video)

zebra.blend
 
(Video)

curtain.blend
 
(Video)

The simulated portion (objects, groups, pins, and solver parameters) is generated by a script you drop into Blender's Scripting editor. Cameras, lighting, and any non-simulated props are still set up in Blender's UI. Each script is linked above its thumbnail.

cards.py
 
(Video)

five-twist.py
 
(Video)

noodle.py
 
(Video)

woven.py
 
(Video)

### 🌐 JupyterLab Examples

All these examples run on our Python frontend through JupyterLab. Click any notebook to see how the scene is built, or click the video link to watch the result.

woven.ipynb
 
(Video)

stack.ipynb
 
(Video)

trampoline.ipynb
 
(Video)

needle.ipynb
 
(Video)

cards.ipynb
 
(Video)

codim.ipynb
 
(Video)

hang.ipynb
 
(Video)

trapped.ipynb
 
(Video)

domino.ipynb
 
(Video)

noodle.ipynb
 
(Video)

drape.ipynb
 
(Video)

five-twist.ipynb
 
(Video)

ribbon.ipynb
 
(Video)

curtain.ipynb
 
(Video)

fishingknot.ipynb
 
(Video)

friction.ipynb
 
(Video)

belt.ipynb
 
(Video)

fitting.ipynb
 
(Video)

roller.ipynb
 
(Video)

yarn.ipynb
 
(Video)

### 💰 Budget Table on AWS

Below is a table summarizing the estimated costs for running our examples on a NVIDIA L4 instanceg6.2xlargeat Amazon Web Services US regions (us-east-1andus-east-2).

* 💰 Uptime cost is approximately $1 per hour.
* ⏳ Deployment time is approximately 8 minutes ($0.13). Instance loading takes 3 minutes, and Docker pull & load takes 5 minutes.
* 🎮 The NVIDIA L4 delivers30.3 TFLOPS for FP32, offering approximately 36% of theperformance of an RTX 4090.
* 🎥 Video frame rate is 60fps.

Example

Cost

Time

#Frame

#Vert

#Face

#Tet

#Rod

Max Strain

trapped

$0.37

22.6m

300

263K

299K

885K

N/A

N/A

twist

$0.91

55m

500

203K

406K

N/A

N/A

N/A

stack

$0.60

36.2m

120

166.7K

327.7K

8.8K

N/A

5%

trampoline

$0.74

44.5m

120

56.8K

62.2K

158.0K

N/A

1%

needle

$0.31

18.4m

120

86K

168.9K

8.8K

N/A

5%

cards

$0.29

17.5m

300

8.7K

13.8K

1.9K

N/A

5%

domino

$0.12

4.3m

250

0.5K

0.8K

N/A

N/A

N/A

drape

$0.10

3.5m

100

81.9K

161.3K

N/A

N/A

5%

curtain

$0.33

19.6m

300

64K

124K

N/A

N/A

5%

friction

$0.17

10m

700

1.1K

N/A

1K

N/A

N/A

hang

$0.12

7.5m

200

16.3K

32.2K

N/A

N/A

1%

belt

$0.19

11.4m

200

12.3K

23.3K

N/A

N/A

5%

codim

$0.36

21.6m

240

122.7K

90K

474.1K

1.3K

N/A

fishingknot

$0.38

22.5m

830

19.6K

36.9K

N/A

N/A

5%

fitting

$0.03

1.54m

240

28.4K

54.9K

N/A

N/A

10%

noodle

$0.14

8.45m

240

116.2K

N/A

N/A

116.2K

N/A

ribbon

$0.23

13.9m

480

34.9K

52.9K

8.8K

N/A

5%

woven

$0.58

34.6m

450

115.6K

N/A

N/A

115.4K

N/A

yarn

$0.01

0.24m

120

28.5K

N/A

N/A

28.5K

N/A

roller

$0.03

2.08m

240

21.4K

22.2K

61.0K

N/A

N/A

#### 🏗️ Large Scale Examples

Large scale examples are run on avast.aiinstance with an RTX 4090.
These examples are not included in GitHub Action tests since they can take days to finish.

large-twist.ipynb
 
(Video)

large-five-twist.ipynb
 
(Video)

large-woven.ipynb
 
(Video)

Example

Commit

#Vert

#Face

#Rod

#Contact

#Frame

Time/Frame

large-twist

cbafbd2

3.2M

6.4M

N/A

56.7M

2,000

46.4s

large-five-twist

6ab6984

8.2M

16.4M

N/A

184.1M

2,413

144.5s

large-woven

4c07b83

2.7M

N/A

2.7M

8.9M

946

436.8s

📝 Large scale examples take a very long time, and it's easy to lose connection or close the browser.
Our frontend lets you close and reopen it at your convenience. Just recover your session after you reconnect.
Here's an example cell how to recover:

# In case you shutdown the server (or kernel) and still want

# to restart, do this.

# Do not run other cells used to create this scene.

# You can also recover this way if you closed the browser.

# Just directly run this in a new cell or in a new notebook.

from
 
frontend
 
import
 
App

# recover the session

session
 
=
 
App
.
recover
(
"app-name"
)

# resume if not currently running

if
 
not
 
App
.
busy
():
 
session
.
resume
()

# preview the current state

session
.
preview
()

# stream the logs

session
.
stream
()

## 🚀 GitHub Actions

We implemented GitHub Actions that test all of our examples except for large scale ones, which take from days to weeks to finish.
We perform explicit intersection checks at the end of each step, which raises an error if an intersection is detected.This ensures that all steps are confirmed to be penetration-free if tests pass.The runner types are described as follows:

The tested runner of this action is the Ubuntu NVIDIA GPU-Optimized Image for AI and HPC with an NVIDIA Tesla T4 (16 GB VRAM) with Driver version570.133.20.
This is not a self-hosted runner, meaning that each time the runner launches, all environments are fresh. 🌱

 

We use the GitHub-hosted runner, but the actual simulation runs on ag6e.2xlargeAWS instance.
Since we start with a fresh instance, the environment is clean every time.
We take advantage of the ability to deploy on the cloud; this action is performed in parallel, which reduces the total action time.

This action exercises ourBlender add-onon free GitHub-hosted Linux and macOS runners in parallel. Blender 5.1.1 is installed from the official Blender Foundation mirror, the Rust solver is built in CPU-emulated mode (no CUDA required), and the add-on is installed as a Blender 5 extension. A headless test rig then runs the full scenario registry covering add-on UI flows.

### 📦 Action Artifacts

We generate zipped action artifacts for each run. These artifacts include:

* 📝 Logs: Detailed logs of the simulation runs.
* 📊 Metrics: Performance metrics and statistics.
* 📹 Videos: Simulated animations.

Please note that these artifacts will be deleted after a month.

### ⚔️ Ten Consecutive Runs

We know that you can't judge the reliability of contact resolution by simply watching a single success video example.
To ensure greater transparency, we implemented GitHub Actions to run many of our examples via automated GitHub Actions, not just once, but10 times in a rowfor both Docker and Windows.
This means thata single failure out of 10 tests is considered a failure of the entire test suite!Also, we apply small jitters to the position of objects in the scene, soat each run, the scene is slightly different.

##### 🪟 Windows Native

##### 🐧 Linux

## 📡 Deploying on Cloud Services

Running our solver on the cloud has a few practical advantages:

* 💰 Pay only when you use it: Spin up an instance, run your experiment, and delete it when you're done. You pay for hours, not for a GPU sitting on your desk.
* 📈 Scale on demand: If you have a deadline, just launch multiple instances and run experiments in parallel. No waiting in a queue.
* 🤝 Share with collaborators: Send the JupyterLab link to a remote teammate and they can watch the simulation right alongside you.
* 🔒 Cloud-grade security: You inherit whatever security the provider gives you, which is usually a lot more than you'd set up yourself.
* 🐛 Reproducible environments: Users and developers share the same kernel and driver, making bug reproduction more reliable than across heterogeneous local setups.
* 🛠️ No hardware maintenance: No driver updates, no thermal management, and no replacement costs when hardware fails.

Below, we describe how to deploy our solver on major cloud services. These instructions are up to date as of late 2024 and are subject to change.

⚠️For all the services below, don't forget to delete the instance after use, or you'll be charged for nothing. 💸

### 📦 Deploying onvast.ai

* Select our template(Link).
* Create an instance and connect via SSH with port forwarding, e.g.ssh -L 8080:localhost:8080 root@<host> -p <port>, then openhttp://localhost:8080in your browser.

### 📦 Deploying onScaleway

* Set zone tofr-par-2
* Select typeL4-1-24GorGPU-3070-S
* ChooseUbuntu Jammy GPU OS 12
* Do not skipthe Docker container creation in the installation process; it is required.
* This setup costs approximately €0.76 per hour.
* CLI instructions are described in(Markdown).

### 📦 Deploying onAmazon Web Services

* Amazon Machine Image (AMI):Deep Learning Base AMI with Single CUDA (Ubuntu 22.04)
* Instance Type:g6.2xlarge(Recommended)
* This setup costs around $1 per hour.
* Do not skipthe Docker container creation in the installation process; it is required.

### 📦 Deploying onGoogle Compute Engine

* SelectGPUs. We recommend the GPU typeNVIDIA L4because it's affordable and accessible, as it does not require a high quota. You may selectT4instead for testing purposes.
* DonotcheckEnable Virtual Workstation (NVIDIA GRID).
* We recommend the machine typeg2-standard-8.
* Choose the OS typeDeep Learning VM with CUDA 12.4 M129and set the disk size to50GB.
* As of late 2024, this configuration costs approximately $0.86 per hour inus-central1 (Iowa)and $1.00 per hour inasia-east1 (Taiwan).
* Port number8080is reserved by the OS image. Set$MY_WEB_PORTto8888. When connecting viagcloud, use the following format:gcloud compute ssh --zone "xxxx" "instance-name" -- -L 8080:localhost:8888.
* Do not skipthe Docker container creation in the installation process; it is required.
* CLI instructions are described in(Markdown).

## 🤝 Community Works

### 🧩 Blender Add-ons

Alongside ourofficial Blender add-on, the following community add-ons are also available:

* AndoSim
* ArzteZ-PPF-solver

### 📺 Videos

* The Worst Bug In Games Is Now Gone ForeverbyTwo Minute Papers.
* Visual Components - ZOZO's Contact Solver Handshankingbyidkfa.
* Blender 3D - ZOZO's Contact Solver Capability Test - Squished Cloths under Rubber Ballby[BH]Lithium.

### 📰 Articles

* A New Open-Source Physics Engine for Blender - ZOZO's Contact Solveronr/blender.
* New Simulation Method To Achieve Accuracy In Collision Physicsby Amber Rutherford on80 Level.
* New Research Might Have Finally Solved the Clipping Bugby LLL Inc.
* New Open-Source Physics Engine For Blender Releasedon80 Level.
* The Official Blender Add-on for ZOZO's Contact Solver - An Open-Source Physics SolveronPixelSham.
* ZOZO's Contact Solver Blender Add-on 2026(Japanese article) on3D人-3dnchu-.
* ZOZO Releases Open-Source High-Precision Physics Simulation "ppf-contact-solver", Enabling Large-Scale Cloth Simulation from Blender(Japanese article) onMODELING HAPPY.
* ZOZO's Contact Solver: open-source physics simulation lands in Blender 5onKabum.

### 📣 Sharing Your Work

Our work still needs many improvements, and our documentation and tutorial videos are not very sophisticated.
The author would greatly appreciate it if you made your own tutorial videos, write-ups, or blog posts about the solver, and posted them online on YouTube, your blog, social media, or anywhere else.

If you post about it onX.com, please consider using the#ZOZOContactSolvertag so the author and community users can find your work.

## 💼 Commercial Use and Beyond

This project is released under theApache License 2.0. In plain terms, you may use, modify, and redistribute the code in commercial products, including proprietary software, without paying royalties or open-sourcing your own code. You only need to preserve the license notice and the attribution required by the license.

If you build something on top of this solver, we would love to hear about it, but you are not obligated to disclose anything.

## 📬 Contributing

We appreciate your interest in opening pull requests, but we are not ready to accept external pull requests because doing so involves resolving copyright and licensing matters withZOZO, Inc.For the time being, please open issues for bug reports under the terms described below. If you wish to extend the codebase, please fork the repository and work on it.

By submitting an Issue or suggestion to this repository, you agree that your contribution is provided under the terms of theApache License, Version 2.0. Any bug reports or feature proposals you provide will be deemed to be licensed to us and the community on a royalty-free, unrestricted basis for the purpose of improving this software.

SeeCONTRIBUTING.mdfor details.
Thank you!

## 💬 Participating Discussions

We have openedGitHub Discussionsas a place for questions, ideas, and conversations about the solver. Feel free to drop by to ask questions, share your work, or chat with the community.

## 📨 Reaching the Author

This project is owned byZOZO, Inc.and maintained by Ryoichi Ando.

For bug reports or feature requests, please open an issue on GitHub. For usage questions,GitHub Discussionsis the best place to ask. Either route is the fastest way to reach the author and keeps the conversation searchable for other users.

If you would prefer to reach out privately, you can also email the author atryoichi.ando@zozo.com.

Please refrain from attaching code patches or other materials that would be considered contributions to this project. Anything you do send is treated under the terms ofCONTRIBUTING.md: by sending it you agree it is licensed to us and the community under theApache License, Version 2.0on a royalty-free, unrestricted basis.

If you used this project in a public piece of work, whether a paper, a production credit, or a personal project, the author would love to feature it here. A link to your article, project page, or website is all we need (rather than images or clips themselves, since hosting them here may run into licensing issues), and we will be happy to add it.

## 🙏 Acknowledgements

The author thanksZOZO, Inc.for permitting the release of the code and the team members for assisting with the internal paperwork for this project.
This repository is owned byZOZO, Inc.

## About

A contact solver for physics-based simulations involving 👚 shells, 🪵 solids and 🪢 rods.

### Topics

 simulation

 physics

 collision

 contact

 cloth

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

3.4k

 stars
 

### Watchers

29

 watching
 

### Forks

245

 forks
 

 Report repository

 

## Releases6

Blender Add-on 1.0.6 (addon-2026-05-25-0558)

 Latest

 

May 24, 2026

 

+ 5 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python55.5%
* Rust32.3%
* Cuda6.1%
* C++3.0%
* Batchfile1.6%
* Shell1.2%
* Other0.3%