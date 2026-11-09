---
title: GitHub - google-deepmind/mujoco: Multi-Joint dynamics with Contact. A general purpose physics simulator. · GitHub
url: https://github.com/google-deepmind/mujoco
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:16.810781
---

# GitHub - google-deepmind/mujoco: Multi-Joint dynamics with Contact. A general purpose physics simulator. · GitHub

# MuJoCo Repository Overview

## Repository Structure
- Contains source code, documentation, examples, and build configurations.
- Key directories: `src`, `include/mujoco`, `python`, `studio`, `test`, `sample`, `plugin`, `unity`, `wasm`, `doc`.
- Build files: `CMakeLists.txt`, `BUILD.bazel`, `.bazelrc`, `.clang-format`.
- Supporting files: `README.md`, `LICENSE`, `CONTRIBUTING.md`, `STYLEGUIDE.md`, `VERSIONING.md`.

## Project Description
- MuJoCo (Multi‑Joint dynamics with Contact) is a general‑purpose physics engine.
- Targets research and development in robotics, biomechanics, graphics, animation, machine learning, etc.
- Provides a high‑performance C API, interactive visualizers (desktop and web), and extensive utility functions.
- Officially maintained by Google DeepMind.

## Documentation & Getting Started
- Full docs at **mujoco.readthedocs.io**; upcoming features listed in the “latest” branch changelog.
- Quick start options:
  1. Run MuJoCo in a browser via **mujoco.org** or **live.mujoco.org** (WebAssembly version).
  2. Download a prebuilt release and use the MuJoCo Studio app or the classic `simulate` viewer.
  3. Explore Python tutorial notebooks on Google Colab (intro, model editing, rollout, LQR, least‑squares, MJX, differentiable physics).

## Installation
- **Prebuilt binaries**: Available for Linux (x86‑64, AArch64), Windows (x86‑64), macOS (universal) via GitHub releases (recommended).
- **Build from source**: Instructions in the docs; note that the tip of the main branch may be unstable.
- **Python bindings (≥ 3.11)**: Install with `pip install mujoco`; wheels target manylinux2014. Source‑build details also provided.

## Versioning
- Monthly releases, first week of each month.
- Uses modified Semantic Versioning since version 3.5.0 (see `VERSIONING.md`).

## Contribution & Support
- Community contributions welcomed (issues, feature requests, pull requests).
- Guidelines in `CONTRIBUTING.md` and `STYLEGUIDE.md`.
- Help requests should be posted in the GitHub “Asking for Help” discussion; bug reports and feature requests belong in GitHub Issues.

## Related Software
- **First‑party bindings**: Python (`dm_control`, `PyMJCF`), JavaScript/WebAssembly, C# (Unity).
- **Third‑party bindings**: MATLAB Simulink, Swift, Java, Julia, Rust.
- **Converters**: OpenSim → MJCF, SDFormat ↔ MJCF, OBJ → MJCF, Onshape → MJCF.

## Citation
- Recommended citation for research:
  ```
  @inproceedings{todorov2012mujoco,
    title={MuJoCo: A physics engine for model-based control},
    author={Todorov, Emanuel and Erez, Tom and Tassa, Yuval},
    booktitle={2012 IEEE/RSJ International Conference on Intelligent Robots and Systems},
    pages={5026--5033},
    year={2012},
    organization={IEEE},
    doi={10.1109/IROS.2012.6386109}
  }
  ```

## License
- Source code: Apache License 2.0.
- Documentation (reST, images, videos): Creative Commons Attribution 4.0 (CC BY 4.0).
- Note: Not an officially supported Google product.