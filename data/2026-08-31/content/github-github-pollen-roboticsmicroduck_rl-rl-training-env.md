---
title: 'GitHub - pollen-robotics/microduck_rl: RL training environments for Microduck (mjlab) · GitHub'
url: https://github.com/pollen-robotics/microduck_rl
site_name: github
content_file: github-github-pollen-roboticsmicroduck_rl-rl-training-env
fetched_at: '2026-08-31T02:21:42.254494'
original_url: https://github.com/pollen-robotics/microduck_rl
author: pollen-robotics
description: RL training environments for Microduck (mjlab). Contribute to pollen-robotics/microduck_rl development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 pollen-robotics

 

/

microduck_rl

Public

* NotificationsYou must be signed in to change notification settings
* Fork127
* Star720

 
 
 
develop
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,180 Commits
1,180 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
docs
docs
 
 
scripts
scripts
 
 
src/
mjlab_microduck
src/
mjlab_microduck
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Microduck RL

RL training environments forMicroduck—
a ~800 g, ~25 cm tall bipedal robot — built onmjlab(MuJoCo Warp) with PPO.
Policies are trained here at 50 Hz, exported to ONNX, and deployed on the real
robot by the runtime inpollen-robotics/microduck.

interaction.mov

The repo encodes the full sim2real recipe:BAMactuator physics, domain randomization, backlash simulation, and the
reward-design lessons that made it work
(seeAGENTS.mdfor the distilled playbook).

## Quickstart

Requires a CUDA GPU (training runs through MuJoCo Warp) anduv.

On ARM boxes (DGX Spark / GB10, Jetson):uv syncpulls ~2 GB of CUDA
wheels on first run and uv's default 30 s HTTP timeout can abort mid-download.
ExportUV_HTTP_TIMEOUT=600for the first sync.

git clone https://github.com/pollen-robotics/microduck_rl

cd
 microduck_rl

#
 train the walking policy (uses your GPU; ~1-2 h for a usable gait at 4096 envs)

uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096

#
 watch a trained policy in the viewer

uv run play Mjlab-Velocity-Flat-MicroDuck --wandb-run-path 
<
entity/project/run_id
>

#
 export to ONNX for deployment

uv run scripts/export.py Mjlab-Velocity-Flat-MicroDuck --wandb-run-path 
<
...
>

#
 drive the exported policy in CPU MuJoCo with the keyboard

uv run scripts/infer_policy.py --walking output.onnx

Resume from a checkpoint:

uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096 \
 --agent.run-name resume --agent.load-checkpoint model_29999.pt --agent.resume True

No GPU? Add--hf-jobsto any train command to run it on Hugging Face Jobs
instead of locally (seescripts/hf/README.md).

## Tasks

uv run list-envsprints the live registry. Flat/Rough variants exist where noted.

Task id

Terrain

Description

Mjlab-Velocity-{Flat,Rough}-MicroDuck

flat/rough

The main task
: walking with velocity commands + head-pose commands

Mjlab-VelStand-{Flat,Rough}-MicroDuck

flat/rough

Walking + fall recovery in one policy

Mjlab-StandUp-{Flat,Rough}-MicroDuck

flat/rough

Stand up from face-down/face-up/sitting, then hold the stand + body-pose control

Mjlab-SitStand-{Flat,Rough}-MicroDuck

flat/rough

Commanded sit ↔ stand in one policy, gently, head commandable

Mjlab-GroundPick-{Flat,Rough}-MicroDuck

flat/rough

Crouch and touch the ground with the mouth tip, return to stand

Mjlab-BallKick-Flat-MicroDuck

flat

Kick a 70 mm / 15 g ball forward (actor is ball-blind)

Mjlab-Roulade-Flat-MicroDuck

flat

Forward roll over the head, land back on the feet

Mjlab-Velocity-Flat-MicroDuck-Rollers

flat

Roller-skate velocity tracking (passive wheels under the feet)

Mjlab-Velocity-Swizzle-MicroDuck

flat

Classic symmetric swizzle skating

Mjlab-RollerCrouch-Flat-MicroDuck

flat

Crouch while gliding on rollers

Mjlab-RollerSlope-Flat-MicroDuck

slope

Glide down slopes on rollers

Mjlab-RollerStandUp-Flat-MicroDuck

flat

Stand up from the ground onto the wheels

Mjlab-Spin-Flat-MicroDuck

flat

Fast spin in place on rollers

At deployment the runtime hot-swaps these policies (walk / recover / trick)
behind a shared 61-dimensional observation contract, so any of them can take
over the robot at any moment.scripts/infer_policy.pyrehearses exactly that:

uv run scripts/infer_policy.py --walking walk.onnx --standing stand.onnx \
 --sitstand sitstand.onnx --roulade roulade.onnx --new-cmd-obs

Keyboard-driven (velocity commands,Gground pick,Ysit/stand,Rroulade,K/Lkicks);--debug,--save-csv,--recordsupport sim2real comparisons.

### Backlash variants

Every main task has aBacklashtwin that trains on a model with ±1° of gear
play (2° total) in series with each of the 14 servo joints: insert-BacklashbeforeMicroDuckin the task id, e.g.Mjlab-Velocity-Flat-Backlash-MicroDuck.

The backlash is modeled properly for sim2real: each servo gets an unactuatedpassive_<joint>_backlashhinge, and because the real encoder sits on the
output side of the play, both the firmware PD emulation
(BacklashEncoderBamActuator) and thejoint_pos/joint_velobservations
readthroughthe backlash (qpos[servo] + qpos[backlash]). Observation and
action dims are unchanged, so ONNX export and the runtime need no changes.
Seesrc/mjlab_microduck/tasks/backlash.py.

## Actuator model

All tasks use theBAMM6 actuator model for
the Dynamixel XL330 (voltage control law, back-EMF, Coulomb/Stribeck/load-dependent
friction), with per-env domain randomization on battery voltage, voltage sag
under load, command delay, and friction magnitude
(FrictionDRBamActuatorinsrc/mjlab_microduck/actuator/).

At this scale — tiny servos driving a ~800 g biped — actuator fidelity is most
of the sim2real gap, which is why the actuator is modeled down to its voltage
control law instead of an ideal PD.

## Robot models

MJCF models live insrc/mjlab_microduck/robot/microduck/and are exported
from Onshape withonshape-to-robot,
oneconfig_mjcf_*.jsonper model:

XML

Used by

robot_walk.xml

Velocity (stripped trunk/head contacts — falling is cheap)

robot_allcollisions.xml

VelStand, StandUp, SitStand, GroundPick, BallKick, Roulade (body can physically lie on the ground)

robot_allcollisions_rollers.xml

Roller tasks (passive wheels)

robot_*_backlash.xml

Backlash task variants (generated by 
add_backlash.py
)

scene*.xmlfiles wrap the robots with a floor + keyframes (STAND/SIT/FOLD)
for quick viewing and forinfer_policy.py.

## Project structure

src/mjlab_microduck/
├── robot/
│ ├── microduck/ # MJCF exports, export configs, scenes, add_backlash.py
│ └── microduck_constants.py # robot cfgs, HOME frame, BAM actuator cfg
├── actuator/friction_dr_bam.py # BAM + friction DR + backlash encoder feedback
├── tasks/
│ ├── __init__.py # task registration (base + backlash variants)
│ ├── mdp.py # rewards, events, observations, custom classes
│ ├── backlash.py # make_backlash_variant() env-cfg wrapper
│ └── microduck_*_env_cfg.py # one cfg module per task family
├── train_cli.py # `train` entry point (+ --hf-jobs)
└── hf_jobs.py # Hugging Face Jobs submission

Conventions worth knowing:

* The observation layout is shared across every policy (61-dim actor obs:
48 proprioception + commands[twist(3), head_pose(4), body_pose(6)]), which
is what makes runtime policy hot-swapping possible. Envs that don't use a
command slot zero-pad it rather than dropping it.
* Unactuated joints are all namedpassive_*(roller wheels, backlash
hinges); actuators, joint observations and pose rewards select servo joints
with^(?!passive_).*.
* Domain-randomization toggles areENABLE_*booleans at the top of each
env cfg file.
* Joint layout (14 servos): 0–4 left leg (hip_yaw, hip_roll, hip_pitch, knee,
ankle), 5–8 neck/head (neck_pitch, head_pitch, head_yaw, head_roll),
9–13 right leg.
* The exporter bakes the observation normalizer into the ONNX graph — always
deploy ONNX produced byscripts/export.py, never a hand-converted
checkpoint, or the policy sees unnormalized observations at runtime.

AGENTS.mddocuments the env-building workflow and the reward-design
rules learned across the project (also aimed at AI coding agents working in
this repo).

## Tests

uv run --with pytest pytest tests/

CPU-only config-invariant and reward-function regression tests — they lock in
joint-index mappings, reward sign conventions, and NaN guards.

## Related projects

* microduck— the Microduck project home, including the onboard runtime that runs the exported policies
* mjlab— the training framework (MuJoCo Warp + rsl_rl)
* BAM— better actuator models, by Rhoban

## License

This project is licensed under the Apache 2.0 License. See theLICENSEfile for details.
3D model files are licensed under Creative Commons BY-SA-NC.