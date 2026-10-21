---
title: GitHub - google-pytorch/torch_tpu · GitHub
url: https://github.com/google-pytorch/torch_tpu
site_name: hackernews_api
content_file: hackernews_api-github-google-pytorchtorch_tpu-github
fetched_at: '2026-10-21T11:11:09.059605'
original_url: https://github.com/google-pytorch/torch_tpu
author: ilreb
date: '2026-10-21'
description: Contribute to google-pytorch/torch_tpu development by creating an account on GitHub.
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

4,465 Commits
4,465 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills/
docs-review
.agents/
skills/
docs-review
 
 
.github
.github
 
 
.vscode
.vscode
 
 
bazel
bazel
 
 
build_files
build_files
 
 
ci
ci
 
 
csrc
csrc
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
perflab
perflab
 
 
requirements
requirements
 
 
shims
shims
 
 
src/
torch_tpu
src/
torch_tpu
 
 
tests
tests
 
 
tools
tools
 
 
.bazelignore
.bazelignore
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.clang-format
.clang-format
 
 
.clangd
.clangd
 
 
.gitignore
.gitignore
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
AGENTS.md
AGENTS.md
 
 
BUILD.bazel
BUILD.bazel
 
 
CLAUDE.md
CLAUDE.md
 
 
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
 
 
WORKSPACE
WORKSPACE
 
 
WORKSPACE.bzlmod
WORKSPACE.bzlmod
 
 
bazel_downloader.cfg
bazel_downloader.cfg
 
 
mkdocs.yml
mkdocs.yml
 
 
mkdocs_hooks.py
mkdocs_hooks.py
 
 
noxfile.py
noxfile.py
 
 
pyproject.toml
pyproject.toml
 
 
visibility.bzl
visibility.bzl
 
 
View all files

## Repository files navigation

## Description

This project provides a PyTorch backend for Google's Tensor Processing Units
(TPUs), enabling users to run PyTorch models and operations on TPU devices. It
includes custom ATen kernels for various PyTorch operations, a compilation cache
for optimizing execution, and examples for distributed training and model
inference.

## Features

* PyTorch ATen kernel implementation for TPU.
* Compilation cache for optimized execution of XLA computations.
* Support for distributed training (Data Parallelism, Tensor Parallelism).
* Examples for various models (Llama, Qwen, ResNet, DLRM, minGPT, UNet).
* Integration withtorch.compile()for graph mode execution.
* Utilities for debugging and benchmarking.

## User Guide and Interactive Notebooks

A user guide is available athttps://torchtpu.readthedocs.io/. This is a
static version of the interactive notebooks. They are available in the docs
folder.

The notebooks are Marimo (similar to Jupyter). They can be run withmarimo edit file.pyand then you can access them in your browser. You will need to be
running this from a TPU VM, a v6e GCE instance is easiest.

## Installation

The same instructions are available in the user guide linked above.

TorchTPU's Python version support policy matchesPyTorch's Release Compatibility Matrix.
Currently,Python 3.11+is supported. See thePython Version Support Policyfor
more details.

First create a Python virtual environment:

python -m venv .venv

source
 .venv/bin/activate

or, withuv

uv venv .venv

source
 .venv/bin/activate

### Install via pip

Install the latest public release
(0.2.0 on PyPI) (foruvprependuvto allpipcommands):

pip install torch_tpu==0.2.0 --extra-index-url https://download.pytorch.org/whl/cpu

### Build from source

Wheels can be built via:

bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel

All OSS Bazel builds default to optimized mode (-c opt) automatically via.bazelrc. Unoptimized builds (-c fastbuild,-c dbg) can degrade
performance and are not used for wheel builds. If you are developing or
debugging C++ code and explicitly want an unoptimized wheel, pass--//:allow_unoptimized_wheel=True:

bazel build -c dbg --config=wheel_common //ci/wheel:torch_tpu_wheel \
 --//:allow_unoptimized_wheel=True

--config=wheel_commonis required, and the build fails at build time without
it. The config sets--//:wheel_build=True, which routes the shared XLA/MLIR
backend through thetorch_version-reset transition so that pywrap factors it
into a singlelibxla_base.so; built without the flag, every per-version common
ships its own copy of the backend and the resulting wheel aborts onimport torchwith duplicate static registrations.

wheel_commonalso turns on the Remote Build Execution (RBE) remote cache and
remote executor. If you do not have RBE credentials, append--config=no_rbeto
strip those flags back out:

bazel build --config=wheel_common //ci/wheel:torch_tpu_wheel --config=no_rbe

The order matters here:--config=no_rbehas to come after--config=wheel_common, because the later config is the one that wins for the
remote-cache and remote-executor flags they both set.

Install wheel via:

cd
 
<
path_to_repo
>

python -m venv .venv
;
 
source
 .venv/bin/activate

#
 The extra-index-url provides the CPU version of torch rather than the default CUDA build.

pip install ../bazel-bin/ci/wheel/
*
.whl --extra-index-url https://download.pytorch.org/whl/cpu

Note that installing without--extra-index-url https://download.pytorch.org/whl/cpuwill install the CUDA version oftorch;
pass--extra-index-urlas shown above or install the CPU build separately.

## Getting Started

Some pointers to get you started:

* PyTorch: Official PyTorch documentation
* Tutorials and examples: easy to understand PyTorch code using TorchTPU
* Public APIs: the TorchTPU APIs that you can use

## Dependencies

The project uses Bazel for dependency management. Key Python dependencies are:

TBD

## Bazel setup

This project uses Bazel for building and dependency management.

To install Bazel, we actually install Bazelisk, which is a transparent wrapper
that handles downloading and installing Bazel itself.

There are several ways to install Bazelisk. Here are some common ways:

* If you have Go installed:go install github.com/bazelbuild/bazelisk@latest
* Download the binary directly:wget -O ~/bin/bazel https://github.com/bazelbuild/bazelisk/releases/download/v1.27.0/bazelisk-linux-amd64

See theBazelisk READMEfor more install instructions

However you install it, add it's location toPATH.

To verify the install, runbazel infoin the repo's root directory:

bazel info

It should print information about the repo without errors.

## VSCodeclangdSetup

For C++ code navigation, it is recommended to use VSCode withclangdextension.
Relying on acompilation databasegenerated from Bazel action graph,clangdis able to
enrich the editor with various smart features, including code completions, go-to
definitions,etc.

1. Install VSCode extensions via UI or the following command:code --install-extension llvm-vs-code-extensions.vscode-clangd#Uninstall Microsoft C++ extensions to avoid interference.code --uninstall-extension ms-vscode.cpptools
2. Generate the initialcompile_commands.json:tools/setup_clangd.py

It may take a while (> 30 minutes) for the first run to make a full build, but
reruns will be incremental and cheap. If you have runbazel buildrecently,
generated files already exist so you can pass--no-buildto skip waiting for
heavy builds (note that on a fresh workspace, skipping the build may preventclangdfrom resolving generated files). See more options in thescriptfile-level comments.

Alternatively, you can invoke the script vianox(arguments after--are
forwarded):

nox -s refresh_compile_commands -- --no-build
nox -s refresh_compile_commands -- //src/torch_tpu/ops/...

## Contributing

We welcome contributions to the PyTorch on TPU project! Please see ourCONTRIBUTING.mdfor guidelines on how to contribute,
including signing our Contributor License Agreement (CLA) and code review
processes.

## Star History

## License

This project is licensed under the Apache 2.0 License. See theLICENSEfile for details.