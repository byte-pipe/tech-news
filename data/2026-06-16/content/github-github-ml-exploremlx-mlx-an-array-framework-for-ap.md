---
title: 'GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub'
url: https://github.com/ml-explore/mlx
site_name: github
content_file: github-github-ml-exploremlx-mlx-an-array-framework-for-ap
fetched_at: '2026-06-16T12:37:06.512638'
original_url: https://github.com/ml-explore/mlx
author: ml-explore
description: 'MLX: An array framework for Apple silicon. Contribute to ml-explore/mlx development by creating an account on GitHub.'
---

ml-explore

 

/

mlx

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.9k
* Star27k

 
 
 
 
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

1,898 Commits
1,898 Commits
.github
.github
 
 
benchmarks
benchmarks
 
 
cmake
cmake
 
 
docs
docs
 
 
examples
examples
 
 
mlx
mlx
 
 
python
python
 
 
tests
tests
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
ACKNOWLEDGMENTS.md
ACKNOWLEDGMENTS.md
 
 
CITATION.cff
CITATION.cff
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
mlx.pc.in
mlx.pc.in
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
View all files

## Repository files navigation

# MLX

Quickstart|Installation|Documentation|Examples

MLX is an array framework for machine learning on Apple silicon,
brought to you by Apple machine learning research.

Some key features of MLX include:

* Familiar APIs: MLX has a Python API that closely follows NumPy. MLX
also has fully featured C++,C, andSwiftAPIs, which closely mirror
the Python API. MLX has higher-level packages likemlx.nnandmlx.optimizerswith APIs that closely follow PyTorch to simplify building
more complex models.
* Composable function transformations: MLX supports composable function
transformations for automatic differentiation, automatic vectorization,
and computation graph optimization.
* Lazy computation: Computations in MLX are lazy. Arrays are only
materialized when needed.
* Dynamic graph construction: Computation graphs in MLX are constructed
dynamically. Changing the shapes of function arguments does not trigger
slow compilations, and debugging is simple and intuitive.
* Multi-device: Operations can run on any of the supported devices
(currently the CPU and the GPU).
* Unified memory: A notable difference from MLX and other frameworks
is theunified memory model. Arrays in MLX live in shared memory.
Operations on MLX arrays can be performed on any of the supported
device types without transferring data.

MLX is designed by machine learning researchers for machine learning
researchers. The framework is intended to be user-friendly, but still efficient
to train and deploy models. The design of the framework itself is also
conceptually simple. We intend to make it easy for researchers to extend and
improve MLX with the goal of quickly exploring new ideas.

The design of MLX is inspired by frameworks likeNumPy,PyTorch,Jax, andArrayFire.

## Examples

TheMLX examples repohas a
variety of examples, including:

* Transformer language modeltraining.
* Large-scale text generation withLLaMAand
finetuning withLoRA.
* Generating images withStable Diffusion.
* Speech recognition withOpenAI's Whisper.

## Quickstart

See thequick start
guidein the documentation.

## Installation

MLX is available onPyPI. To install MLX on
macOS, run:

pip install mlx

To install the CUDA backend on Linux, run:

pip install mlx[cuda]

To install a CPU-only Linux package, run:

pip install mlx[cpu]

Checkout thedocumentationfor more information on building the C++ and Python APIs from source.

## Contributing

Check out thecontribution guidelinesfor more information
on contributing to MLX. See thedocsfor more
information on building from source, and running tests.

We are grateful for all ofour
contributors. If you contribute
to MLX and wish to be acknowledged, please add your name to the list in your
pull request.

## Citing MLX

The MLX software suite was initially developed with equal contribution by Awni
Hannun, Jagrit Digani, Angelos Katharopoulos, and Ronan Collobert. If you find
MLX useful in your research and wish to cite it, please use the following
BibTex entry:

@software{mlx2023,
 author = {Awni Hannun and Jagrit Digani and Angelos Katharopoulos and Ronan Collobert},
 title = {{MLX}: Efficient and flexible machine learning on Apple silicon},
 url = {https://github.com/ml-explore},
 version = {0.0},
 year = {2023},
}

## About

MLX: An array framework for Apple silicon

ml-explore.github.io/mlx/

### Topics

 mlx

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

27k

 stars
 

### Watchers

200

 watching
 

### Forks

1.9k

 forks
 

 Report repository

 

## Releases73

v0.31.2

 Latest

 

Apr 22, 2026

 

+ 72 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++64.8%
* Python21.2%
* Cuda9.0%
* Metal3.4%
* CMake1.2%
* C0.3%
* Other0.1%