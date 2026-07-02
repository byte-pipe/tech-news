---
title: 'GitHub - pytorch/pytorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration · GitHub'
url: https://github.com/pytorch/pytorch
site_name: github
content_file: github-github-pytorchpytorch-tensors-and-dynamic-neural-n
fetched_at: '2026-07-02T11:50:28.744330'
original_url: https://github.com/pytorch/pytorch
author: pytorch
description: Tensors and Dynamic neural networks in Python with strong GPU acceleration - pytorch/pytorch
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 pytorch

 

/

pytorch

Public

* NotificationsYou must be signed in to change notification settings
* Fork28.2k
* Star101k

 
 
 
 
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

106,806 Commits
106,806 Commits
.ci
.ci
 
 
.claude/
skills
.claude/
skills
 
 
.ctags.d
.ctags.d
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.spin
.spin
 
 
.vscode
.vscode
 
 
android
android
 
 
aten
aten
 
 
benchmarks
benchmarks
 
 
binaries
binaries
 
 
c10
c10
 
 
caffe2
caffe2
 
 
cmake
cmake
 
 
docs
docs
 
 
functorch
functorch
 
 
mypy_plugins
mypy_plugins
 
 
scripts
scripts
 
 
test
test
 
 
third_party
third_party
 
 
tools
tools
 
 
torch
torch
 
 
torchgen
torchgen
 
 
.bc-linter.yml
.bc-linter.yml
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.cmakelintrc
.cmakelintrc
 
 
.coveragerc
.coveragerc
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.flake8
.flake8
 
 
.gdbinit
.gdbinit
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.lintrunner.toml
.lintrunner.toml
 
 
.lldbinit
.lldbinit
 
 
AGENTS.md
AGENTS.md
 
 
BUCK.oss
BUCK.oss
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GLOSSARY.md
GLOSSARY.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
buckbuild.bzl
buckbuild.bzl
 
 
build.bzl
build.bzl
 
 
build_variables.bzl
build_variables.bzl
 
 
codex_setup.sh
codex_setup.sh
 
 
defs.bzl
defs.bzl
 
 
docker.Makefile
docker.Makefile
 
 
mypy-strict.ini
mypy-strict.ini
 
 
mypy.ini
mypy.ini
 
 
pt_ops.bzl
pt_ops.bzl
 
 
pt_template_srcs.bzl
pt_template_srcs.bzl
 
 
pyproject.toml
pyproject.toml
 
 
pyrefly.toml
pyrefly.toml
 
 
pytest.ini
pytest.ini
 
 
requirements-build.txt
requirements-build.txt
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
ubsan.supp
ubsan.supp
 
 
ufunc_defs.bzl
ufunc_defs.bzl
 
 
version.txt
version.txt
 
 
View all files

## Repository files navigation

PyTorch is a Python package that provides two high-level features:

* Tensor computation (like NumPy) with strong GPU acceleration
* Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy, and Cython to extend PyTorch when needed.

Our trunk health (Continuous Integration signals) can be found athud.pytorch.org.

* More About PyTorchA GPU-Ready Tensor LibraryDynamic Neural Networks: Tape-Based AutogradPython FirstImperative ExperiencesFast and LeanExtensions Without Pain
* A GPU-Ready Tensor Library
* Dynamic Neural Networks: Tape-Based Autograd
* Python First
* Imperative Experiences
* Fast and Lean
* Extensions Without Pain
* InstallationBinariesNVIDIA Jetson PlatformsFrom SourcePrerequisitesNVIDIA CUDA SupportAMD ROCm SupportIntel GPU SupportGet the PyTorch SourceInstall DependenciesInstall PyTorchAdjust Build Options (Optional)Docker ImageUsing pre-built imagesBuilding the image yourselfBuilding the DocumentationTroubleshooting CI ErrorsBuilding a PDFPrevious Versions
* BinariesNVIDIA Jetson Platforms
* NVIDIA Jetson Platforms
* From SourcePrerequisitesNVIDIA CUDA SupportAMD ROCm SupportIntel GPU SupportGet the PyTorch SourceInstall DependenciesInstall PyTorchAdjust Build Options (Optional)
* PrerequisitesNVIDIA CUDA SupportAMD ROCm SupportIntel GPU Support
* NVIDIA CUDA Support
* AMD ROCm Support
* Intel GPU Support
* Get the PyTorch Source
* Install Dependencies
* Install PyTorchAdjust Build Options (Optional)
* Adjust Build Options (Optional)
* Docker ImageUsing pre-built imagesBuilding the image yourself
* Using pre-built images
* Building the image yourself
* Building the DocumentationTroubleshooting CI ErrorsBuilding a PDF
* Troubleshooting CI Errors
* Building a PDF
* Previous Versions
* Getting Started
* Resources
* Communication
* Releases and Contributing
* The Team
* License

## More About PyTorch

Learn the basics of PyTorch

At a granular level, PyTorch is a library that consists of the following components:

Component

Description

torch

A Tensor library like NumPy, with strong GPU support

torch.autograd

A tape-based automatic differentiation library that supports all differentiable Tensor operations in torch

torch.jit

A compilation stack (TorchScript) to create serializable and optimizable models from PyTorch code

torch.nn

A neural networks library deeply integrated with autograd designed for maximum flexibility

torch.multiprocessing

Python multiprocessing, but with magical memory sharing of torch Tensors across processes. Useful for data loading and Hogwild training

torch.utils

DataLoader and other utility functions for convenience

Usually, PyTorch is used either as:

* A replacement for NumPy to use the power of GPUs.
* A deep learning research platform that provides maximum flexibility and speed.

Elaborating Further:

### A GPU-Ready Tensor Library

If you use NumPy, then you have used Tensors (a.k.a. ndarray).

PyTorch provides Tensors that can live either on the CPU or the GPU and accelerates the
computation by a huge amount.

We provide a wide variety of tensor routines to accelerate and fit your scientific computation needs
such as slicing, indexing, mathematical operations, linear algebra, reductions.
And they are fast!

### Dynamic Neural Networks: Tape-Based Autograd

PyTorch has a unique way of building neural networks: using and replaying a tape recorder.

Most frameworks such as TensorFlow, Theano, Caffe, and CNTK have a static view of the world.
One has to build a neural network and reuse the same structure again and again.
Changing the way the network behaves means that one has to start from scratch.

With PyTorch, we use a technique called reverse-mode auto-differentiation, which allows you to
change the way your network behaves arbitrarily with zero lag or overhead. Our inspiration comes
from several research papers on this topic, as well as current and past work such astorch-autograd,autograd,Chainer, etc.

While this technique is not unique to PyTorch, it's one of the fastest implementations of it to date.
You get the best of speed and flexibility for your crazy research.

### Python First

PyTorch is not a Python binding into a monolithic C++ framework.
It is built to be deeply integrated into Python.
You can use it naturally like you would useNumPy/SciPy/scikit-learnetc.
You can write your new neural network layers in Python itself, using your favorite libraries
and use packages such asCythonandNumba.
Our goal is to not reinvent the wheel where appropriate.

### Imperative Experiences

PyTorch is designed to be intuitive, linear in thought, and easy to use.
When you execute a line of code, it gets executed. There isn't an asynchronous view of the world.
When you drop into a debugger or receive error messages and stack traces, understanding them is straightforward.
The stack trace points to exactly where your code was defined.
We hope you never spend hours debugging your code because of bad stack traces or asynchronous and opaque execution engines.

### Fast and Lean

PyTorch has minimal framework overhead. We integrate acceleration libraries
such asIntel MKLand NVIDIA (cuDNN,NCCL) to maximize speed.
At the core, its CPU and GPU Tensor and neural network backends
are mature and have been tested for years.

Hence, PyTorch is quite fast — whether you run small or large neural networks.

The memory usage in PyTorch is extremely efficient compared to Torch or some of the alternatives.
We've written custom memory allocators for the GPU to make sure that
your deep learning models are maximally memory efficient.
This enables you to train bigger deep learning models than before.

### Extensions Without Pain

Writing new neural network modules, or interfacing with PyTorch's Tensor API, was designed to be straightforward
and with minimal abstractions.

You can write new neural network layers in Python using the torch APIor your favorite NumPy-based libraries such as SciPy.

If you want to write your layers in C/C++, we provide a convenient extension API that is efficient and with minimal boilerplate.
No wrapper code needs to be written. You can seea tutorial hereandan example here.

## Installation

### Binaries

Commands to install binaries via Conda or pip wheels are on our website:https://pytorch.org/get-started/locally/

#### NVIDIA Jetson Platforms

Python wheels for NVIDIA's Jetson Nano, Jetson TX1/TX2, Jetson Xavier NX/AGX, and Jetson AGX Orin are providedhereand the L4T container is publishedhere

They require JetPack 4.2 and above, and@dusty-nvand@ptrblckare maintaining them.

### From Source

#### Prerequisites

If you are installing from source, you will need:

* Python 3.10 or later
* A compiler that fully supports C++20, such as clang or gcc (gcc 11.3.0 or newer is required, on Linux)
* Visual Studio or Visual Studio Build Tool (Windows only)
* At least 10 GB of free disk space
* 30-60 minutes for the initial build (subsequent rebuilds are much faster)

* PyTorch CI uses Visual C++ BuildTools, which come with Visual Studio Enterprise,
Professional, or Community Editions. You can also install the build tools fromhttps://visualstudio.microsoft.com/visual-cpp-build-tools/. The build toolsdo notcome with Visual Studio Code by default.

An example of environment setup is shown below:

* Linux:

$ 
source
 
<
CONDA_INSTALL_DIR
>
/bin/activate
$ conda create -y -n 
<
CONDA_NAME
>

$ conda activate 
<
CONDA_NAME
>

* Windows:

$ 
source
 
<
CONDA_INSTALL_DIR
>
\S
cripts
\a
ctivate.bat
$ conda create -y -n 
<
CONDA_NAME
>

$ conda activate 
<
CONDA_NAME
>

$ call 
"
C:\Program Files\Microsoft Visual Studio\<VERSION>\Community\VC\Auxiliary\Build\vcvarsall.bat
"
 x64

A conda environment is not required. You can also do a PyTorch build in a
standard virtual environment, e.g., created with tools likeuv, provided
your system has installed all the necessary dependencies unavailable as pip
packages (e.g., CUDA, MKL.)

##### NVIDIA CUDA Support

If you want to compile with CUDA support,select a supported version of CUDA from our support matrix, then install the following:

* NVIDIA CUDA
* NVIDIA cuDNNv9.0 or above
* Compilercompatible with CUDA

Note: You could refer to thecuDNN Support Matrixfor cuDNN versions with the various supported CUDA, CUDA driver, and NVIDIA hardware.

If you want to disable CUDA support, export the environment variableUSE_CUDA=0.
Other potentially useful environment variables may be found insetup.py. If
CUDA is installed in a non-standard location, set PATH so that the nvcc you
want to use can be found (e.g.,export PATH=/usr/local/cuda-12.8/bin:$PATH).

If you are building for NVIDIA's Jetson platforms (Jetson Nano, TX1, TX2, AGX Xavier), Instructions to install PyTorch for Jetson Nano areavailable here

##### AMD ROCm Support

If you want to compile with ROCm support, install

* AMD ROCm4.0 and above installation
* ROCm is currently supported only for Linux systems.

By default the build system expects ROCm to be installed in/opt/rocm. If ROCm is installed in a different directory, theROCM_PATHenvironment variable must be set to the ROCm installation directory. The build system automatically detects the AMD GPU architecture. Optionally, the AMD GPU architecture can be explicitly set with thePYTORCH_ROCM_ARCHenvironment variableAMD GPU architecture

If you want to disable ROCm support, export the environment variableUSE_ROCM=0.
Other potentially useful environment variables may be found insetup.py.

##### Intel GPU Support

If you want to compile with Intel GPU support, follow these

* PyTorch Prerequisites for Intel GPUsinstructions.
* Intel GPU is supported for Linux and Windows.

If you want to disable Intel GPU support, export the environment variableUSE_XPU=0.
Other potentially useful environment variables may be found insetup.py.

#### Get the PyTorch Source

git clone https://github.com/pytorch/pytorch

cd
 pytorch

#
 if you are updating an existing checkout

git submodule sync
git submodule update --init --recursive

#### Install Dependencies

Common

#
 Run this command from the PyTorch directory after cloning the source code using the “Get the PyTorch Source“ section above

pip install --group dev

On Linux

pip install mkl-static mkl-include

#
 CUDA only: Add LAPACK support for the GPU if needed

#
 magma installation: run with active conda environment. specify CUDA version to install

.ci/docker/common/install_magma_conda.sh 12.4

#
 (optional) If using torch.compile with inductor/triton, install the matching version of triton

#
 Run from the pytorch directory after cloning

#
 For Intel GPU support, please explicitly `export USE_XPU=1` before running command.

make triton

On Windows

pip install mkl-static mkl-include

#
 Add these packages if torch.distributed is needed.

#
 Distributed package support on Windows is a prototype feature and is subject to changes.

conda install -c conda-forge libuv=1.51

#### Install PyTorch

On Linux

If you're compiling for AMD ROCm then first run this command:

#
 Only run this if you're compiling for ROCm

python tools/amd_build/build_amd.py

Install PyTorch

#
 the CMake prefix for conda environment

export
 CMAKE_PREFIX_PATH=
"
${CONDA_PREFIX
:-
'
$(dirname $(which conda))/../
'
}
:
${CMAKE_PREFIX_PATH}
"

python -m pip install --no-build-isolation -v -e 
.

#
 the CMake prefix for non-conda environment, e.g. Python venv

#
 call following after activating the venv

export
 CMAKE_PREFIX_PATH=
"
${VIRTUAL_ENV}
:
${CMAKE_PREFIX_PATH}
"

On macOS

python -m pip install --no-build-isolation -v -e 
.

On Windows

If you want to build legacy python code, please refer toBuilding on legacy code and CUDA

CPU-only builds

In this mode PyTorch computations will run on your CPU, not your GPU.

python -m pip install --no-build-isolation -v -e .

Note on OpenMP: The desired OpenMP implementation is Intel OpenMP (iomp). In order to link against iomp, you'll need to manually download the library and set up the building environment by tweakingCMAKE_INCLUDE_PATHandLIB. The instructionhereis an example for setting up both MKL and Intel OpenMP. Without these configurations for CMake, Microsoft Visual C OpenMP runtime (vcomp) will be used.

CUDA based build

In this mode PyTorch computations will leverage your GPU via CUDA for faster number crunching

NVTXis needed to build PyTorch with CUDA.
NVTX is a part of CUDA distributive, where it is called "Nsight Compute". To install it onto an already installed CUDA run CUDA installation once again and check the corresponding checkbox.
Make sure that CUDA with Nsight Compute is installed after Visual Studio.

Currently, VS 2017 / 2019, and Ninja are supported as the generator of CMake. Ifninja.exeis detected inPATH, then Ninja will be used as the default generator, otherwise, it will use VS 2017 / 2019.If Ninja is selected as the generator, the latest MSVC will get selected as the underlying toolchain.

Additional libraries such asMagma,oneDNN, a.k.a. MKLDNN or DNNL, andSccacheare often needed. Please refer to theinstallation-helperto install them.

You can refer to thebuild_pytorch.batscript for some other environment variables configurations

cmd

::
 Set the environment variables after you have downloaded and unzipped the mkl package,

::
 else CMake would throw an error as `Could NOT find OpenMP`.

set
 
CMAKE_INCLUDE_PATH
=
{Your directory}\mkl\include

set
 
LIB
=
{Your directory}\mkl\lib;
%LIB%

::
 Read the content in the previous section carefully before you proceed.

::
 [Optional] If you want to override the underlying toolset used by Ninja and Visual Studio with CUDA, please run the following script block.

::
 "Visual Studio 2019 Developer Command Prompt" will be run automatically.

::
 Make sure you have CMake >= 3.12 before you do this when you use the Visual Studio generator.

set
 
CMAKE_GENERATOR_TOOLSET_VERSION
=
14.27

set
 
DISTUTILS_USE_SDK
=
1

for
 /f 
"
usebackq tokens=*
"
 
%i in (`"%
ProgramFiles(x86)
%\Microsoft Visual Studio\Installer\vswhere.exe" -version [15^,17^) -products * -latest -property installationPath`) do call "%
i\VC\Auxiliary\Build\vcvarsall.bat
"
 x64 -vcvars_ver=
%CMAKE_GENERATOR_TOOLSET_VERSION%

::
 [Optional] If you want to override the CUDA host compiler

set
 
CUDAHOSTCXX
=
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.27.29110\bin\HostX64\x64\cl.exe

python -m pip install --no-build-isolation -v -e .

Intel GPU builds

In this mode PyTorch with Intel GPU support will be built.

Please make surethe common prerequisitesas well asthe prerequisites for Intel GPUare properly installed and the environment variables are configured prior to starting the build. For build tool support,Visual Studio 2022is required.

Then PyTorch can be built with the command:

::
 CMD Commands:

::
 Set the CMAKE_PREFIX_PATH to help find corresponding packages

::
 %CONDA_PREFIX% only works after `conda activate custom_env`

if
 
defined
 CMAKE_PREFIX_PATH (
 
set
 
"
CMAKE_PREFIX_PATH
=
%CONDA_PREFIX%
\Library;
%CMAKE_PREFIX_PATH%
"

) 
else
 (
 
set
 
"
CMAKE_PREFIX_PATH
=
%CONDA_PREFIX%
\Library
"

)

python -m pip install --no-build-isolation -v -e .

##### Adjust Build Options (Optional)

You can adjust the configuration of cmake variables optionally (without building first), by doing
the following. For example, adjusting the pre-detected directories for CuDNN or BLAS can be done
with such a step.

On Linux

export
 CMAKE_PREFIX_PATH=
"
${CONDA_PREFIX
:-
'
$(dirname $(which conda))/../
'
}
:
${CMAKE_PREFIX_PATH}
"

CMAKE_ONLY=1 python setup.py build
ccmake build 
#
 or cmake-gui build

On macOS

export
 CMAKE_PREFIX_PATH=
"
${CONDA_PREFIX
:-
'
$(dirname $(which conda))/../
'
}
:
${CMAKE_PREFIX_PATH}
"

MACOSX_DEPLOYMENT_TARGET=11.0 CMAKE_ONLY=1 python setup.py build
ccmake build 
#
 or cmake-gui build

### Docker Image

#### Using pre-built images

You can also pull a pre-built docker image from Docker Hub and run with docker v23.0+

docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest

Please note that PyTorch uses shared memory to share data between processes, so if torch multiprocessing is used (e.g.
for multithreaded data loaders) the default shared memory segment size that container runs with is not enough, and you
should increase shared memory size either with--ipc=hostor--shm-sizecommand line options tonvidia-docker run.

#### Building the image yourself

NOTE:Must be built with a Docker version >= 23.0

The Dockerfile is supplied to build images with CUDA 12.1 support and cuDNN v9.
You can passPYTHON_VERSION=x.ymake variable to specify which Python version is to be used by Miniconda, or leave it
unset to use the default, as the Dockerfile uses system Python.

make -f docker.Makefile

#
 images are tagged as docker.io/${your_docker_username}/pytorch

You can also pass theCMAKE_VARS="..."environment variable to specify additional CMake variables to be passed to CMake during the build.
Seesetup.pyfor the list of available variables.

make -f docker.Makefile

### Building the Documentation

To build documentation in various formats, you will needSphinxand thepytorch_sphinx_theme2.

Before you build the documentation locally, ensuretorchis
installed in your environment. For small fixes, you can install the
nightly version as described inGetting Started.

For more complex fixes, such as adding a new module and docstrings for
the new module, you might need to install torchfrom source.
SeeDocstring Guidelinesfor docstring conventions.

cd
 docs/
pip install -r requirements.txt
make html
make serve

Runmaketo get a list of all available output formats.

If you get a katex error runnpm install katex. If it persists, trynpm install -g katex

Note

If you see a numpy incompatibility error, run:

pip install 'numpy<2'

#### Troubleshooting CI Errors

Your build may show errors you didn't have locally - here's how to find the errors relevant to the docs.

If the build has any errors, you will see something like this on the PR:

Any doc-related errors will occur in jobs that include "doc" somewhere in the title. It doesn't look like any of these jobs are relevant to our docs.

Let's take a look anyway. Click on the job to see the logs:

And we can be sure that this job does not involve docs.

Looking at this build, we can see these jobs are relevant to our docs - and they didn't have any errors:

You might also see a comment on the PR like this:

We can see that some of these issues are relevant to our docs.

Open the logs by clicking on theghlink:

And here we can see there is a doc-related error:

You can always find the relevant doc builds by going to theCheckstab on your PR, and scrolling down topull.

You can either click through or toggle the accordion to see all of the jobs here, where you can see the docs jobs highlighted:

If you click through, you'll see the doc jobs at the bottom, like this:

#### Building a PDF

To compile a PDF of all PyTorch documentation, ensure you havetexliveand LaTeX installed. On macOS, you can install them using:

brew install --cask mactex

To create the PDF:

1. Run:make latexpdfThis will generate the necessary files in thebuild/latexdirectory.
2. Navigate to this directory and execute:make LATEXOPTS="-interaction=nonstopmode"This will produce apytorch.pdfwith the desired content. Run this
command one more time so that it generates the correct table
of contents and index.

Note

To view the Table of Contents, switch to theTable of Contentsview in your PDF viewer.

### Previous Versions

Installation instructions and binaries for previous PyTorch versions may be found
onour website.

## Getting Started

Pointers to get you started:

* Tutorials: get you started with understanding and using PyTorch
* Examples: easy to understand PyTorch code across all domains
* The API Reference
* Glossary

## Resources

* PyTorch.org
* PyTorch Tutorials
* PyTorch Examples
* PyTorch Models
* Intro to Deep Learning with PyTorch from Udacity
* Intro to Machine Learning with PyTorch from Udacity
* Deep Neural Networks with PyTorch from Coursera
* PyTorch Twitter
* PyTorch Blog
* PyTorch YouTube

## Communication

* Forums: Discuss implementations, research, etc.https://discuss.pytorch.org
* GitHub Issues: Bug reports, feature requests, install issues, RFCs, thoughts, etc.
* Slack: ThePyTorch Slackhosts a primary audience of moderate to experienced PyTorch users and developers for general chat, online discussions, collaboration, etc. If you are a beginner looking for help, the primary medium isPyTorch Forums. If you need a slack invite, please fill this form:https://goo.gl/forms/PP1AGvNHpSaJP8to1
* Newsletter: No-noise, a one-way email newsletter with important announcements about PyTorch. You can sign-up here:https://eepurl.com/cbG0rv
* Facebook Page: Important announcements about PyTorch.https://www.facebook.com/pytorch
* For brand guidelines, please visit our website atpytorch.org

## Releases and Contributing

Typically, PyTorch has three minor releases a year. Please let us know if you encounter a bug byfiling an issue.

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further discussion.

If you plan to contribute new features, utility functions, or extensions to the core, please first open an issue and discuss the feature with us.
Sending a PR without discussion might end up resulting in a rejected PR because we might be taking the core in a different direction than you might be aware of.

To learn more about making a contribution to PyTorch, please see ourContribution page. For more information about PyTorch releases, seeRelease page.

## The Team

PyTorch is a community-driven project with several skillful engineers and researchers contributing to it.

PyTorch is currently maintained bySoumith Chintala,Gregory Chanan,Dmytro Dzhulgakov,Edward Yang,Alban Desmaison,Piotr BialeckiandNikita Shulgawith major contributions coming from hundreds of talented individuals in various forms and means.
A non-exhaustive but growing list needs to mention:Trevor Killeen,Sasank Chilamkurthy,Sergey Zagoruyko,Adam Lerer,Francisco Massa,Alykhan Tejani,Luca Antiga,Alban Desmaison,Andreas Koepf,James Bradbury,Zeming Lin,Yuandong Tian,Guillaume Lample,Marat Dukhan,Natalia Gimelshein,Christian Sarofeen,Martin Raison,Edward Yang,Zachary Devito.

Note: This project is unrelated tohughperkins/pytorchwith the same name. Hugh is a valuable contributor to the Torch community and has helped with many things Torch and PyTorch.

## License

PyTorch has a BSD-style license, as found in theLICENSEfile.

## About

Tensors and Dynamic neural networks in Python with strong GPU acceleration

pytorch.org

### Topics

 python

 machine-learning

 deep-learning

 neural-network

 gpu

 numpy

 autograd

 tensor

### Resources

 Readme

 

### License

 View license
 

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

101k

 stars
 

### Watchers

1.8k

 watching
 

### Forks

28.2k

 forks
 

 Report repository

 

## Releases67

PyTorch 2.12.1 Release, bug fix release

 Latest

 

Jun 18, 2026

 

+ 66 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by835k

 + 834,897
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python64.1%
* C++28.5%
* Cuda2.6%
* C1.3%
* Objective-C++1.0%
* CMake0.6%
* Other1.9%