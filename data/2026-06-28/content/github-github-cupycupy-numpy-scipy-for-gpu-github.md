---
title: 'GitHub - cupy/cupy: NumPy & SciPy for GPU · GitHub'
url: https://github.com/cupy/cupy
site_name: github
content_file: github-github-cupycupy-numpy-scipy-for-gpu-github
fetched_at: '2026-06-28T11:36:51.371745'
original_url: https://github.com/cupy/cupy
author: cupy
description: NumPy & SciPy for GPU. Contribute to cupy/cupy development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 cupy

 

/

cupy

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star11.3k

 
 
 
 
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

31,536 Commits
31,536 Commits
.github
.github
 
 
.pfnci
.pfnci
 
 
cupy
cupy
 
 
cupy_backends
cupy_backends
 
 
cupyx
cupyx
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
install
install
 
 
tests
tests
 
 
third_party
third_party
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.mergify.yml
.mergify.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
CITATION.bib
CITATION.bib
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
codecov.yml
codecov.yml
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

# CuPy : NumPy & SciPy for GPU

Website|Install|Tutorial|Examples|Documentation|API Reference|Forum

CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated computing with Python.
CuPy acts as adrop-in replacementto run existing NumPy/SciPy code on NVIDIA CUDA or AMD ROCm platforms.

>
>>
 
import
 
cupy
 
as
 
cp

>
>>
 
x
 
=
 
cp
.
arange
(
6
).
reshape
(
2
, 
3
).
astype
(
'f'
)

>
>>
 
x

array
([[ 
0.
, 
1.
, 
2.
],
 [ 
3.
, 
4.
, 
5.
]], 
dtype
=
float32
)

>
>>
 
x
.
sum
(
axis
=
1
)

array
([ 
3.
, 
12.
], 
dtype
=
float32
)

CuPy also provides access to low-level CUDA features.
You can passndarrayto existing CUDA C/C++ programs viaRawKernels, useStreamsfor performance, or even callCUDA Runtime APIsdirectly.

## Installation

### Pip

Binary packages (wheels) are available for Linux and Windows onPyPI.
Choose the right package for your platform.

Platform

Architecture

Command

CUDA 12.x

x86_64 / aarch64

pip install cupy-cuda12x

CUDA 13.x

x86_64 / aarch64

pip install cupy-cuda13x

ROCm 7.0 (
experimental
)

x86_64

pip install cupy-rocm-7-0

Note

To install pre-releases, append--pre -U -f https://pip.cupy.dev/pre(e.g.,pip install cupy-cuda12x --pre -U -f https://pip.cupy.dev/pre).

### Conda

Binary packages are also available for Linux and Windows onConda-Forge.

Platform

Architecture

Command

CUDA

x86_64 / aarch64 / ppc64le

conda install -c conda-forge cupy

If you need a slim installation (without also getting CUDA dependencies installed), you can doconda install -c conda-forge cupy-core.

If you need to use a particular CUDA version (say 12.0), you can use thecuda-versionmetapackage to select the version, e.g.conda install -c conda-forge cupy cuda-version=12.0.

Note

If you encounter any problem with CuPy installed fromconda-forge, please feel free to report tocupy-feedstock, and we will help investigate if it is just a packaging issue inconda-forge's recipe or a real issue in CuPy.

### Docker

UseNVIDIA Container Toolkitto runCuPy container images.

$ docker run --gpus all -it cupy/cupy

## Resources

* Installation Guide- instructions on building from source
* Release Notes
* Projects using CuPy
* Contribution Guide
* GPU Acceleration in Python using CuPy and Numba (GTC November 2021 Technical Session)
* GPU-Acceleration of Signal Processing Workflows using CuPy and cuSignal1(ICASSP'21 Tutorial)

## License

MIT License (seeLICENSEfile).

CuPy is designed based on NumPy's API and SciPy's API (seedocs/source/license.rstfile).

CuPy is being developed and maintained byPreferred Networksandcommunity contributors.

## Reference

Ryosuke Okuta, Yuya Unno, Daisuke Nishino, Shohei Hido and Crissman Loomis.CuPy: A NumPy-Compatible Library for NVIDIA GPU Calculations.Proceedings of Workshop on Machine Learning Systems (LearningSys) in The Thirty-first Annual Conference on Neural Information Processing Systems (NIPS), (2017).
[PDF]

@inproceedings
{
cupy_learningsys2017
,
 
author
 = 
"
Okuta, Ryosuke and Unno, Yuya and Nishino, Daisuke and Hido, Shohei and Loomis, Crissman
"
,
 
title
 = 
"
CuPy: A NumPy-Compatible Library for NVIDIA GPU Calculations
"
,
 
booktitle
 = 
"
Proceedings of Workshop on Machine Learning Systems (LearningSys) in The Thirty-first Annual Conference on Neural Information Processing Systems (NIPS)
"
,
 
year
 = 
"
2017
"
,
 
url
 = 
"
http://learningsys.org/nips17/assets/papers/paper_16.pdf
"

}

## Footnotes

1. cuSignal is now part of CuPy starting v13.0.0.↩

## About

NumPy & SciPy for GPU

cupy.dev

### Topics

 python

 gpu

 numpy

 cuda

 cublas

 scipy

 tensor

 cudnn

 rocm

 cupy

 cusolver

 nccl

 curand

 cusparse

 nvrtc

 cutensor

 nvtx

 cusparselt

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

11.3k

 stars
 

### Watchers

130

 watching
 

### Forks

1.1k

 forks
 

 Report repository

 

## Releases153

v14.1.1

 Latest

 

Jun 1, 2026

 

+ 152 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Used by7.1k

 + 7,114
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python72.5%
* Cython18.5%
* C++4.9%
* C1.8%
* Cuda1.4%
* Dockerfile0.5%
* Other0.4%