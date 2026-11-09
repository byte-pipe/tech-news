---
title: 'GitHub - google-deepmind/mujoco: Multi-Joint dynamics with Contact. A general purpose physics simulator. · GitHub'
url: https://github.com/google-deepmind/mujoco
site_name: github
content_file: github-github-google-deepmindmujoco-multi-joint-dynamics
fetched_at: '2026-11-09T16:00:19.976129'
original_url: https://github.com/google-deepmind/mujoco
author: google-deepmind
description: Multi-Joint dynamics with Contact. A general purpose physics simulator. - google-deepmind/mujoco
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

6,601 Commits
6,601 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
cmake
cmake
 
 
dist
dist
 
 
doc
doc
 
 
include/
mujoco
include/
mujoco
 
 
mjx
mjx
 
 
model
model
 
 
plugin
plugin
 
 
python
python
 
 
sample
sample
 
 
simulate
simulate
 
 
src
src
 
 
studio
studio
 
 
test
test
 
 
unity
unity
 
 
wasm
wasm
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.readthedocs.yml
.readthedocs.yml
 
 
BUILD.bazel
BUILD.bazel
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
REPO.bazel
REPO.bazel
 
 
SECURITY.md
SECURITY.md
 
 
STYLEGUIDE.md
STYLEGUIDE.md
 
 
VERSIONING.md
VERSIONING.md
 
 
banner.png
banner.png
 
 
build_defs.bzl
build_defs.bzl
 
 
mujoco.lds
mujoco.lds
 
 
mujoco.unexported_symbols
mujoco.unexported_symbols
 
 
mujoco_plugin.exported_symbols
mujoco_plugin.exported_symbols
 
 
mujoco_plugin.lds
mujoco_plugin.lds
 
 
View all files

## Repository files navigation

MuJoCostands forMulti-Joint dynamics withContact. It is a
general purpose physics engine that aims to facilitate research and development
in robotics, biomechanics, graphics and animation, machine learning, and other
areas which demand fast and accurate simulation of articulated structures
interacting with their environment.

This repository is maintained byGoogle DeepMind.

MuJoCo has a C API and is intended for researchers and developers. The runtime
simulation module is tuned to maximize performance and operates on low-level
data structures that are preallocated by the built-in XML compiler. The library
includes interactive visualization in native desktop windows and web browsers.
MuJoCo further exposes a large number of utility functions for computing
physics-related quantities.

We also providePython bindingsand a plug-in for theUnitygame engine.

## Documentation

MuJoCo's documentation can be found atmujoco.readthedocs.io. Upcoming
features due for the next release can be found in thechangelogin the
"latest" branch.

## Getting Started

1. Try MuJoCo in your browser.Visitmujoco.orgto explore MuJoCo on desktop or mobile
with nothing to install, or openlive.mujoco.orgto
inspect and drag and drop your own models in the WebAssembly version of theMuJoCo Studioapp (slower than native C, since it runs in WebAssembly).
2. Run a viewer on your machine.Follow theGetting Startedguide in the documentation to download a prebuilt
release and run theMuJoCo Studioapp or the classicsimulateviewer (shown
inthis video) on your machine.
3. Explore our online IPython notebooks.If you are a Python user, you might want to start with our tutorial notebooks
running on Google Colab:

* Theintroductorytutorial teaches MuJoCo basics:
* TheModel Editingtutorial shows how to create and edit models procedurally:
* Therollouttutorial shows how to use the multithreadedrolloutmodule:
* TheLQRtutorial synthesizes a linear-quadratic controller, balancing a
humanoid on one leg:
* Theleast-squarestutorial explains how to use the Python-based nonlinear
least-squares solver:
* TheMJXtutorial provides usage examples ofMuJoCo XLA, a branch of MuJoCo written in JAX:
* Thedifferentiable physicstutorial trains locomotion policies with
analytical gradients automatically derived from MuJoCo's physics step:

## Installation

### Prebuilt binaries

Versioned releases are available as precompiled binaries from the GitHubreleases page, built for Linux (x86-64 and AArch64), Windows (x86-64 only),
and macOS (universal). This is the recommended way to use the software.

### Building from source

Users who wish to build MuJoCo from source should consult thebuild from
sourcesection of the documentation. However, note that the commit at
the tip of themainbranch may be unstable.

### Python (>= 3.11)

The native Python bindings, which come pre-packaged with a copy of MuJoCo, can
be installed fromPyPIvia:

pip install mujoco

Note that Pre-built Linux wheels targetmanylinux2014, seeherefor compatible distributions. For more
information such as building the bindings from source, see thePython bindingssection of the documentation.

## Versioning

We aim to release MuJoCo in the first week of each month. Our versioning
standards changed to modified Semantic Versioning in 3.5.0,
seeversioningfor details.

## Contributing

We welcome community engagement: questions, requests for help, bug reports and
feature requests. To read more about bug reports, feature requests and more
ambitious contributions, please see ourcontributors guideandstyle guide.

## Asking Questions

Questions and requests for help are welcome as a GitHub"Asking for Help" Discussionand should focus on a specific problem or question.

## Bug reports and feature requests

GitHubIssuesare reserved
for bug reports, feature requests and other development-related subjects.

## Related software

MuJoCo is the backbone for numerous environment packages. Below we list several
bindings and converters.

### Bindings

These packages give users of various languages access to MuJoCo functionality:

#### First-party bindings:

* Python bindingsdm_control, Google
DeepMind's related environment stack, includesPyMJCF,
a module for procedural manipulation of MuJoCo models.
* dm_control, Google
DeepMind's related environment stack, includesPyMJCF,
a module for procedural manipulation of MuJoCo models.
* JavaScript bindings and WebAssembly support(inspiredstillonearthandzalo's community projects;mjswanextends these with real-time policy control, interactive force
application, and more).
* C# bindings and Unity plug-in

#### Third-party bindings:

* MATLAB Simulink:Simulink Blockset for MuJoCo SimulatorbyManoj Velmurugan.
* Swift:swift-mujoco
* Java:mujoco-java
* Julia:MuJoCo.jl
* Rust:MuJoCo-rs

### Converters

* OpenSim:MyoConverterconverts
OpenSim models to MJCF.
* SDFormat:gz-mujocois a
two-way SDFormat <-> MJCF conversion tool.
* OBJ:obj2mjcfa script for converting composite OBJ files into a loadable MJCF model.
* onshape:Onshape to RobotConvertsonshapeCAD assemblies to MJCF.

## Citation

If you use MuJoCo for published research, please cite:

@inproceedings{todorov2012mujoco,
 title={MuJoCo: A physics engine for model-based control},
 author={Todorov, Emanuel and Erez, Tom and Tassa, Yuval},
 booktitle={2012 IEEE/RSJ International Conference on Intelligent Robots and Systems},
 pages={5026--5033},
 year={2012},
 organization={IEEE},
 doi={10.1109/IROS.2012.6386109}
}

## License and Disclaimer

Copyright 2021 DeepMind Technologies Limited.

Box collision code (engine_collision_box.c)
is Copyright 2016 Svetoslav Kolev.

ReStructuredText documents, images, and videos in thedocdirectory are made
available under the terms of the Creative Commons Attribution 4.0 (CC BY 4.0)
license. You may obtain a copy of the License athttps://creativecommons.org/licenses/by/4.0/legalcode.

Source code is licensed under the Apache License, Version 2.0. You may obtain a
copy of the License athttps://www.apache.org/licenses/LICENSE-2.0.

This is not an officially supported Google product.