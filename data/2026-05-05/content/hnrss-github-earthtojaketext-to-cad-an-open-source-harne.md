---
title: 'GitHub - earthtojake/text-to-cad: An open source harness for generating CAD models · GitHub'
url: https://github.com/earthtojake/text-to-cad
site_name: hnrss
content_file: hnrss-github-earthtojaketext-to-cad-an-open-source-harne
fetched_at: '2026-05-05T00:51:41.888700'
original_url: https://github.com/earthtojake/text-to-cad
date: '2026-05-01'
description: An open source harness for generating CAD models. Contribute to earthtojake/text-to-cad development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

earthtojake

 

/

text-to-cad

Public

* NotificationsYou must be signed in to change notification settings
* Fork225
* Star1.8k

 
 
 
 
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

18 Commits
18 Commits
.agents/
skills
.agents/
skills
 
 
.assets
.assets
 
 
.claude/
skills
.claude/
skills
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.lfsconfig
.lfsconfig
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# ⚙ Open Source Text to CAD Harness ⚙

An open source harness for generating 3D models with your favorite coding agent

Demo project

## ✨ Features

* Generate- Create source-controlled CAD models with coding agents like Codex and Claude Code.
* Export- Produce STEP, STL, 3MF, DXF, GLB, topology data, and URDF robot descriptions.
* Browse- Inspect generated geometry in CAD Explorer.
* Reference- Copy stable@cad[...]references so agents can make precise follow-up edits.
* Review- Render quick review images for fast checks during an iteration loop.
* Reproduce- Edit source files first, then regenerate explicit targets.
* Local- Run the harness and CAD Explorer locally with no backend to host.

## 🧰 Bundled Skills

This harness vendors file-targeted skills for CAD, robot-description, robot-motion, and manufacturing-preflight work. Use the bundled copies here for local CAD projects, or use the dedicated repositories when installing the skills outside this harness.

* CAD Skill- STEP, STL, 3MF, DXF, GLB/topology, render images, and@cad[...]geometry references.Bundled skill·Standalone repo
* URDF Skill- Generated URDF XML, robot links, joints, limits, validation, and mesh references.Bundled skill·Standalone repo
* Robot Motion Skill- ROS 2/MoveIt setup, CAD Explorer motion artifacts, inverse kinematics, path planning, and motion-server testing for existing URDFs.Bundled skill

Skills live canonically under.agents/skillsfor Codex. Claude Code compatibility is provided by per-skill symlinks in.claude/skills.

## 📸 Screenshots

CAD

URDF

Robot Motion

## 🔁 Workflow

1. Describe- Tell your agent about the part, assembly, fixture, robot, or mechanism you want.
2. Edit- Let your coding agent update repo-local CAD source files.
3. Regenerate- Create explicit STEP, STL, 3MF, DXF, GLB, or URDF targets.
4. Inspect- Open CAD Explorer to review the generated model.
5. Reference- Copy@cad[...]handles when you want geometry-aware edits.
6. Commit- Save the source and generated artifacts together once the model is ready.

## 🧪 Benchmarks

The repo stores.assets/**through Git LFS and excludes that tree from default LFS pulls so lightweight clones do not fetch GIF assets or benchmark detail pages. To hydrate only the benchmark assets locally, run:

git lfs pull --include=
"
.assets/benchmarks/**
"

#

Target

Prompt

Output

1

Rectangular calibration block with four holes

Create a centered 100 x 60 x 20 mm block with four 8 mm vertical through-holes. Add only a 2 mm chamfer on the top outer perimeter.

2

Circular flange with bolt-hole pattern

Create an 80 mm diameter, 10 mm thick circular flange with a 30 mm central through-bore. Add six 6 mm through-holes on a 60 mm bolt circle and fillet the outside circular edges.

3

L-bracket with gussets and two hole directions

Create an L-bracket from a base plate and rear vertical plate. Add vertical base holes, horizontal back-plate holes, two triangular gussets, and a filleted base/back transition.

4

Stepped shaft with keyway

Create a 120 mm shaft along X with 20/30/20 mm diameter stepped sections. Add end chamfers and a shallow rectangular keyway on top of the middle section.

5

Open-top electronics enclosure with bosses

Create a hollow open-top enclosure with 3 mm walls and floor. Add four internal standoffs with centered blind holes and 2 mm outside vertical corner fillets.

6

Aerospace-style clevis bracket with lightening cutouts

Create a symmetric clevis bracket with a base plate, two rounded lugs, base mounting holes, and a horizontal lug bore. Add triangular lightening cutouts, reinforcing ribs, and rounded transitions.

7

Radial-engine-style cylinder with cooling fins

Create a vertical engine-cylinder form with a central barrel, 12 cooling fins, a base flange, and a top cap. Add a 35 degree angled spark-plug boss with a coaxial through-hole.

8

Centrifugal impeller with backward-curved blades

Create a centrifugal impeller with a backplate, hub, and through-bore. Add 12 fused backward-curved blades sweeping about 45 degrees from root to tip.

9

Spiral staircase with helical handrail

Create a miniature spiral staircase with a central column, base disk, and 20 rising wedge treads. Add a one-revolution helical handrail and vertical balusters at the tread outer ends.

10

Simplified planetary gear stage

Create a flat planetary gear assembly with separate sun, planet, ring, carrier, and pin bodies. Use simplified trapezoidal teeth and place three planets around the sun on a 42 mm radius circle.

## 🚀 Quick Start

Clone the repo:

git clone https://github.com/earthtojake/text-to-cad.git

cd
 text-to-cad

Install Python CAD dependencies:

python3.11 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install -r .agents/skills/cad/requirements.txt

Install other bundled skill requirements only when you need those workflows:

./.venv/bin/pip install -r .agents/skills/urdf/requirements.txt

Install CAD Explorer dependencies:

npm --prefix .agents/skills/cad/explorer install

Run the local CAD Explorer from the project directory you want to scan:

npm --prefix .agents/skills/cad/explorer run dev

Then openhttp://localhost:4178.

For root-aware agent workflows across multiple projects, ask CAD Explorer to
reuse a matching server or start one on a free port:

npm --prefix .agents/skills/cad/explorer run dev:ensure -- --file STEP/sample_part.step

Then open the URL printed by the command.

## About

An open source harness for generating CAD models

### Topics

 ai

 robotics

 wasm

 stl

 cad

 mechanical-engineering

 dxf

 agents

 glb

 opencascade

 step

 3mf

 ai-agents

 build123d

 text-to-cad

 cad-skill

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.8k

 stars
 

### Watchers

13

 watching
 

### Forks

225

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript54.1%
* Python45.2%
* Other0.7%