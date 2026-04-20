---
title: 'GitHub - newton-physics/newton: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers. · GitHub'
url: https://github.com/newton-physics/newton
site_name: github
content_file: github-github-newton-physicsnewton-an-open-source-gpu-acc
fetched_at: '2026-03-18T11:20:43.211605'
original_url: https://github.com/newton-physics/newton
author: newton-physics
description: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers. - newton-physics/newton
---

newton-physics



/

newton

Public

* NotificationsYou must be signed in to change notification settings
* Fork303
* Star2.7k




 
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

1,563 Commits
1,563 Commits
.claude/
skills/
newton-api-design
.claude/
skills/
newton-api-design
 
 
.github
.github
 
 
asv/
benchmarks
asv/
benchmarks
 
 
docs
docs
 
 
newton
newton
 
 
scripts/
ci
scripts/
ci
 
 
.coderabbit.yml
.coderabbit.yml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.licenserc-docs.yaml
.licenserc-docs.yaml
 
 
.licenserc.yaml
.licenserc.yaml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
asv.conf.json
asv.conf.json
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Newton

Newton is a GPU-accelerated physics simulation engine built uponNVIDIA Warp, specifically targeting roboticists and simulation researchers.

Newton extends and generalizes Warp's (deprecated)warp.simmodule, and integratesMuJoCo Warpas its primary backend. Newton emphasizes GPU-based computation,OpenUSDsupport, differentiability, and user-defined extensibility, facilitating rapid iteration and scalable robotics simulation.

Newton is aLinux Foundationproject that is community-built and maintained. Code is licensed underApache-2.0. Documentation is licensed underCC-BY-4.0.

Newton was initiated byDisney Research,Google DeepMind, andNVIDIA.

## Requirements

* Python3.10+
* OS:Linux (x86-64, aarch64), Windows (x86-64), or macOS (CPU only)
* GPU:NVIDIA GPU (Maxwell or newer), driver 545 or newer (CUDA 12). No local CUDA Toolkit installation required. macOS runs on CPU.

For detailed system requirements and tested configurations, see theinstallation guide.

## Quickstart

pip install
"
newton[examples]
"

python -m newton.examples basic_pendulum

To install from source withuv, see theinstallation guide.

## Examples

Before running the examples below, install Newton with the examples extra:

pip install
"
newton[examples]
"

If you installed from source with uv, substituteuv runforpythonin the commands below.

### Basic Examples

python -m newton.examples basic_pendulum

python -m newton.examples basic_urdf

python -m newton.examples basic_viewer

python -m newton.examples basic_shapes

python -m newton.examples basic_joints

python -m newton.examples basic_conveyor

python -m newton.examples basic_heightfield

python -m newton.examples recording

python -m newton.examples replay_viewer

### Robot Examples

python -m newton.examples robot_cartpole

python -m newton.examples robot_humanoid

python -m newton.examples robot_g1

python -m newton.examples robot_h1

python -m newton.examples robot_anymal_d

python -m newton.examples robot_anymal_c_walk

python -m newton.examples robot_policy

python -m newton.examples robot_ur10

python -m newton.examples robot_panda_hydro

python -m newton.examples robot_allegro_hand

### Cable Examples

python -m newton.examples cable_twist

python -m newton.examples cable_y_junction

python -m newton.examples cable_bundle_hysteresis

python -m newton.examples cable_pile

### Cloth Examples

python -m newton.examples cloth_bending

python -m newton.examples cloth_hanging

python -m newton.examples cloth_style3d

python -m newton.examples cloth_h1

python -m newton.examples cloth_twist

python -m newton.examples cloth_franka

python -m newton.examples cloth_rollers

python -m newton.examples cloth_poker_cards

### Inverse Kinematics Examples

python -m newton.examples ik_franka

python -m newton.examples ik_h1

python -m newton.examples ik_custom

python -m newton.examples ik_cube_stacking

### MPM Examples

python -m newton.examples mpm_granular

python -m newton.examples mpm_anymal

python -m newton.examples mpm_twoway_coupling

python -m newton.examples mpm_grain_rendering

python -m newton.examples mpm_multi_material

### Sensor Examples

python -m newton.examples sensor_contact

python -m newton.examples sensor_tiled_camera

python -m newton.examples sensor_imu

### Selection Examples

python -m newton.examples selection_cartpole

python -m newton.examples selection_materials

python -m newton.examples selection_articulations

python -m newton.examples selection_multiple

### DiffSim Examples

python -m newton.examples diffsim_ball

python -m newton.examples diffsim_cloth

python -m newton.examples diffsim_drone

python -m newton.examples diffsim_spring_cage

python -m newton.examples diffsim_soft_body

python -m newton.examples diffsim_bear

### Multi-Physics Examples

python -m newton.examples softbody_gift

python -m newton.examples softbody_dropping_to_cloth

### Contacts Examples

python -m newton.examples nut_bolt_hydro

python -m newton.examples nut_bolt_sdf

python -m newton.examples brick_stacking

python -m newton.examples pyramid

### Softbody Examples

python -m newton.examples softbody_hanging

python -m newton.examples softbody_franka

### Example Options

The examples support the following command-line arguments:

Argument

Description

Default

--viewer

Viewer type:
gl
 (OpenGL window),
usd
 (USD file output),
rerun
 (ReRun), or
null
 (no viewer).

gl

--device

Compute device to use, e.g.,
cpu
,
cuda:0
, etc.

None
 (default Warp device)

--num-frames

Number of frames to simulate (for USD output).

100

--output-path

Output path for USD files (required if
--viewer usd
 is used).

None

Some examples may add additional arguments (see their respective source files for details).

### Example Usage

#
 List available examples

python -m newton.examples

#
 Run with the USD viewer and save to my_output.usd

python -m newton.examples basic_viewer --viewer usd --output-path my_output.usd

#
 Run on a selected device

python -m newton.examples basic_urdf --device cuda:0

#
 Combine options

python -m newton.examples basic_viewer --viewer gl --num-frames 500 --device cpu

## Contributing and Development

See thecontribution guidelinesand thedevelopment guidefor instructions on how to contribute to Newton.

## Support and Community Discussion

For questions, please consult theNewton documentationfirst before creatinga discussion in the main repository.

## Code of Conduct

By participating in this community, you agree to abide by the Linux FoundationCode of Conduct.

## Project Governance, Legal, and Members

Please see thenewton-governance repositoryfor more information about project governance.

## About

An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.

newton-physics.github.io/newton/

### Topics

 robotics

 physics-simulation

 nvidia-warp

 newton-physics

### Resources

 Readme



### License

 Apache-2.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

2.7k

 stars


### Watchers

35

 watching


### Forks

303

 forks


 Report repository



## Releases

14

tags

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python100.0%
