---
title: 'GitHub - galilai-group/stable-worldmodel: A platform for reproducible world model research and evaluation · GitHub'
url: https://github.com/galilai-group/stable-worldmodel
site_name: github
content_file: github-github-galilai-groupstable-worldmodel-a-platform-f
fetched_at: '2026-05-29T12:06:54.361543'
original_url: https://github.com/galilai-group/stable-worldmodel
author: galilai-group
description: A platform for reproducible world model research and evaluation - galilai-group/stable-worldmodel
---

galilai-group

 

/

stable-worldmodel

Public

* NotificationsYou must be signed in to change notification settings
* Fork143
* Star1k

 
 
 
 
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

622 Commits
622 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
scripts
scripts
 
 
stable_worldmodel
stable_worldmodel
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
README.md
README.md
 
 
mkdocs.yaml
mkdocs.yaml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# stable-worldmodel

A platform for reproducible world model research and evaluation.

Installation·Quick Start·Environments·Solvers & Baselines·Documentation·Paper·Citation

stable-worldmodelprovides a single, unified interface for the three stages of world model research —collecting data,training, andevaluating with model-predictive control— across a large suite of standardized environments. It ships with reference implementations of common baselines and planning solvers so research code can stay focused on the contribution that matters: the model and the objective.

## Installation

From PyPI:

pip install stable-worldmodel 
#
 base only

pip install 
'
stable-worldmodel[all]
'
 
#
 + training, environments, and data formats

LeRobot dataset support is a separate opt-in extra (requires Python 3.12+):pip install 'stable-worldmodel[lerobot]'.

From source (development):

git clone https://github.com/galilai-group/stable-worldmodel

cd
 stable-worldmodel
uv venv --python=3.10 
&&
 
source
 .venv/bin/activate
uv sync --extra all --group dev

Datasets and checkpoints are stored under$STABLEWM_HOME(defaults to~/.stable_worldmodel/). Override the variable to point at your preferred storage location.

The library is in active development. APIs may change between minor versions.

## Quick Start

import
 
stable_worldmodel
 
as
 
swm

from
 
stable_worldmodel
.
policy
 
import
 
WorldModelPolicy
, 
PlanConfig

from
 
stable_worldmodel
.
solver
 
import
 
CEMSolver

# 1. Collect a dataset

world
 
=
 
swm
.
World
(
"swm/PushT-v1"
, 
num_envs
=
8
)

world
.
set_policy
(
your_expert_policy
)

world
.
collect
(
"data/pusht_demo.lance"
, 
episodes
=
100
, 
seed
=
0
)

# 2. Load it and train your world model (format is autodetected)

dataset
 
=
 
swm
.
data
.
load_dataset
(
"data/pusht_demo.lance"
, 
num_steps
=
16
)

world_model
 
=
 ... 
# your model

# 3. Evaluate with model-predictive control

solver
 
=
 
CEMSolver
(
model
=
world_model
, 
num_samples
=
300
)

policy
 
=
 
WorldModelPolicy
(
solver
=
solver
, 
config
=
PlanConfig
(
horizon
=
10
))

world
.
set_policy
(
policy
)

results
 
=
 
world
.
evaluate
(
episodes
=
50
)

print
(
f"Success Rate: 
{
results
[
'success_rate'
]:.1f
}
%"
)

Reference implementations are provided inscripts/train/:lewm.pyimplementsLeWM, andprejepa.pyreproducesDINO-WM.

GPU utilization for LeWM trained with Push-T LanceDB dataset on a H200 GPU.

## Data Formats

Recording, loading, and conversion all go through a smallformat registry. Pick the backend that matches your trade-off, orregister your own.

Format

On-disk layout

Best for

lance

LanceDB table (episode-contiguous flat rows)

default — append-friendly, fast indexed reads

hdf5

single 
.h5
 file (one dataset per column)

portable single-file artifact

folder

.npz
 columns + one JPEG per step

inspection, partial-key streaming

video

.npz
 columns + one MP4 per episode (
decord
)

long episodes, compact image storage

lerobot

lerobot://<repo_id>
 (read-only adapter)

training/eval directly on LeRobot Hub datasets

world
.
collect
(
"data/pusht.lance"
, 
episodes
=
100
) 
# default: lance

world
.
collect
(
"data/pusht_video"
, 
episodes
=
100
, 
format
=
"video"
) 
# mp4 episodes

ds
 
=
 
swm
.
data
.
load_dataset
(
"data/pusht.lance"
, 
num_steps
=
16
) 
# autodetect

swm
.
data
.
convert
(
"data/pusht.lance"
, 
"data/pusht_video"
,
 
dest_format
=
"video"
, 
fps
=
30
) 
# one-shot migration

Every writer accepts amodekwarg ('append'(default),'overwrite','error'); re-runningworld.collectextends the existing dataset rather than failing.

Throughput & storage benchmarks

Numbers below were produced byscripts/benchmark/compare_h5_lance.pyand can be reproduced with it. Benchmarks use thePushT datasetfrom theLeWorldModelpaper.

## Throughput

Format

Source

Cache

samples/s

ms/step

HDF5

local

no-cache

1416.1

45.2

HDF5

local

cached

1474.0

43.4

LanceDB

local

no-cache

4814.8

13.3

LanceDB

local

cached

4431.3

14.4

Video

local

-

1330.6

48.1

LanceDB

s3

no-cache

3183.7

20.1

LanceDB

s3

cached

3253.2

19.7

HDF5

s3

no-cache

9.1

7032.5

HDF5

s3

cached

756.5

84.6

## Storage size per format (local)

Format

Local size

HDF5

43.12 GB

LanceDB

13.31 GB

Video

496.29 MB

## Environments

Top row: default appearance  ·  Bottom row: visual factor of variation

Environments are pulled from theDeepMind Control Suite,Gymnasium classic control,OGBench,Craftax, theArcade Learning Environment(100+ Atari games), and classical world model benchmarks (Two-Room,PushT). Most environments ship with a set offactors of variation— independently controllable visual and physical parameters (lighting, textures, dynamics, morphology) — that make it straightforward to evaluate zero-shot generalization to distribution shifts without any additional setup. Adding a new environment only requires conforming to theGymnasiuminterface.

Full environment list

Environment ID

# FoV

swm/PushT-v1

16

swm/TwoRoom-v1

17

swm/OGBCube-v0

11

swm/OGBScene-v0

12

swm/HumanoidDMControl-v0

7

swm/CheetahDMControl-v0

7

swm/HopperDMControl-v0

7

swm/ReacherDMControl-v0

8

swm/WalkerDMControl-v0

8

swm/AcrobotDMControl-v0

8

swm/PendulumDMControl-v0

6

swm/CartpoleDMControl-v0

6

swm/BallInCupDMControl-v0

9

swm/FingerDMControl-v0

10

swm/ManipulatorDMControl-v0

8

swm/QuadrupedDMControl-v0

7

swm/CartPoleControl-v1

10

swm/MountainCarControl-v0

5

swm/MountainCarContinuousControl-v0

4

swm/AcrobotControl-v1

11

swm/PendulumControl-v1

9

swm/FetchReach-v3

8

swm/FetchPush-v3

11

swm/FetchSlide-v3

11

swm/FetchPickAndPlace-v3

11

swm/CraftaxClassicPixels-v1

—

swm/CraftaxClassicSymbolic-v1

—

swm/CraftaxPixels-v1

—

swm/CraftaxSymbolic-v1

—

ALE/* (100+ Atari games)

—

## Solvers and Baselines

Solver

Type

Cross-Entropy Method (CEM)

Sampling

Improved CEM (iCEM)

Sampling

Model Predictive Path Integral (MPPI)

Sampling

Predictive Sampling

Sampling

Gradient Descent (SGD, Adam)

Gradient

Projected Gradient Descent (PGD)

Gradient

Augmented Lagrangian

Constrained Opt

Baseline

Type

DINO-WM

JEPA

PLDM

JEPA

LeWM

JEPA

GCBC

Behaviour Cloning

GCIVL

RL

GCIQL

RL

## Command-Line Interface

After installation, theswmcommand is available for inspecting/converting datasets, environments, and checkpoints without writing code:

swm datasets 
#
 list cached datasets

swm inspect pusht_expert_train 
#
 inspect a specific dataset

swm envs 
#
 list all registered environments

swm fovs PushT-v1 
#
 show factors of variation for an environment

swm checkpoints 
#
 list available model checkpoints

swm convert pusht_expert_train --dest-format video 
#
 convert a dataset to another format

## Documentation

The full documentation lives atgalilai-group.github.io/stable-worldmodel, with API references, tutorials, and guides.

## Built onstable-worldmodel

* C-JEPA
* LeWM

## Citation

@misc
{
maes_lld2026swm
,
 
title
 = 
{
stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation
}
,
 
author
 = 
{
Lucas Maes and Quentin Le Lidec and Luiz Facury and Nassim Massaudi and

 Ayush Chaurasia and Francesco Capuano and Richard Gao and Taj Gillin and

 Dan Haramati and Damien Scieur and Yann LeCun and Randall Balestriero
}
,
 
year
 = 
{
2026
}
,
 
eprint
 = 
{
2605.21800
}
,
 
archivePrefix
 = 
{
arXiv
}
,
 
primaryClass
 = 
{
cs.LG
}
,
 
url
 = 
{
https://arxiv.org/abs/2605.21800
}
,
}

## Questions

Open anissue— happy to help.

## About

A platform for reproducible world model research and evaluation

galilai-group.github.io/stable-worldmodel/

### Topics

 deep-learning

 pytorch

 model-predictive-control

 jepa

 world-model

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1k

 stars
 

### Watchers

13

 watching
 

### Forks

143

 forks
 

 Report repository

 

## Releases6

0.1.0

 Latest

 

May 26, 2026

 

+ 5 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.7%
* Shell0.3%