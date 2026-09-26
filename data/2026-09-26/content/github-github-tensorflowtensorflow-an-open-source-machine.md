---
title: 'GitHub - tensorflow/tensorflow: An Open Source Machine Learning Framework for Everyone · GitHub'
url: https://github.com/tensorflow/tensorflow
site_name: github
content_file: github-github-tensorflowtensorflow-an-open-source-machine
fetched_at: '2026-09-26T14:54:03.086064'
original_url: https://github.com/tensorflow/tensorflow
author: tensorflow
description: An Open Source Machine Learning Framework for Everyone - tensorflow/tensorflow
---

tensorflow

 

/

tensorflow

Public

* NotificationsYou must be signed in to change notification settings
* Fork77.6k
* Star200k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

199,467 Commits
199,467 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.gemini
.gemini
 
 
.github
.github
 
 
ci
ci
 
 
tensorflow
tensorflow
 
 
third_party
third_party
 
 
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
 
 
.gitignore
.gitignore
 
 
.pylintrc
.pylintrc
 
 
.zenodo.json
.zenodo.json
 
 
AUTHORS
AUTHORS
 
 
BUILD
BUILD
 
 
CITATION.cff
CITATION.cff
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
ISSUES.md
ISSUES.md
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
WORKSPACE
WORKSPACE
 
 
arm_compiler.BUILD
arm_compiler.BUILD
 
 
bazel_downloader.cfg
bazel_downloader.cfg
 
 
configure
configure
 
 
configure.cmd
configure.cmd
 
 
configure.py
configure.py
 
 
models.BUILD
models.BUILD
 
 
requirements_lock_3_10.txt
requirements_lock_3_10.txt
 
 
requirements_lock_3_11.txt
requirements_lock_3_11.txt
 
 
requirements_lock_3_12.txt
requirements_lock_3_12.txt
 
 
requirements_lock_3_13.txt
requirements_lock_3_13.txt
 
 
requirements_lock_3_14.txt
requirements_lock_3_14.txt
 
 
requirements_lock_3_14_freethreaded.txt
requirements_lock_3_14_freethreaded.txt
 
 
View all files

## Repository files navigation

Documentation

TensorFlowis an end-to-end open source platform
for machine learning. It has a comprehensive, flexible ecosystem oftools,libraries, andcommunityresources that lets
researchers push the state-of-the-art in ML and developers easily build and
deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working within
the Machine Intelligence team at Google Brain to conduct research in machine
learning and neural networks. However, the framework is versatile enough to be
used in other areas as well.

TensorFlow provides stablePythonandC++APIs, as well as a
non-guaranteed backward compatible API forother languages.

Keep up-to-date with release announcements and security updates by subscribing
toannounce@tensorflow.org.
See all themailing lists.

## Install

See theTensorFlow install guidefor thepip package, toenable GPU support, use aDocker container, andbuild from source.

To install the current release, which includes support forCUDA-enabled GPU cards(Ubuntu and
Windows):

 pip install tensorflow

Other devices (DirectX and MacOS-metal) are supported usingDevice Plugins.

A smaller CPU-only TensorFlow package is also available:

 pip install tensorflow-cpu

To update TensorFlow to the latest version, add the--upgradeflag to the
commands above.

Nightly binaries are available for testing using thetf-nightlyandtf-nightly-cpupackages on PyPI.

#### Try your first TensorFlow program

$ python

>
>>
 
import
 
tensorflow
 
as
 
tf

>
>>
 
tf
.
add
(
1
, 
2
).
numpy
()

3

>
>>
 
hello
 
=
 
tf
.
constant
(
'Hello, TensorFlow!'
)

>
>>
 
hello
.
numpy
()

b'Hello, TensorFlow!'

For more examples, see theTensorFlow Tutorials.

## Contribution guidelines

If you want to contribute to TensorFlow, be sure to review theContribution Guidelines. This project adheres to TensorFlow'sCode of Conduct. By participating, you are expected to
uphold this code.

We useGitHub Issuesfor
tracking requests and bugs, please seeTensorFlow Forumfor general questions and
discussion, and please direct specific questions toStack Overflow.

The TensorFlow project strives to abide by generally accepted best practices in
open-source software development.

## Patching guidelines

Follow these steps to patch a specific version of TensorFlow, for example, to
apply fixes to bugs or security vulnerabilities:

* Clone the TensorFlow repository and switch to the appropriate branch for
your desired version—for example,r2.8for version 2.8.
* Apply the desired changes (i.e., cherry-pick them) and resolve any code
conflicts.
* Run TensorFlow tests and ensure they pass.
* Buildthe TensorFlow pip
package from source.

## Continuous build status

You can find more community-supported platforms and configurations in theTensorFlow SIG Build Community Builds Table.

### Official Builds

Build Type

Status

Artifacts

Linux CPU

PyPI

Linux GPU

PyPI

Linux XLA

TBA

macOS

PyPI

Windows CPU

PyPI

Windows GPU

PyPI

Android

Download

Raspberry Pi 0 and 1

Py3

Raspberry Pi 2 and 3

Py3

## Resources

* TensorFlow.org
* TensorFlow Tutorials
* TensorFlow Official Models
* TensorFlow Examples
* TensorFlow Codelabs
* TensorFlow Blog
* Learn ML with TensorFlow
* TensorFlow Twitter
* TensorFlow YouTube
* TensorFlow model optimization roadmap
* TensorFlow White Papers
* TensorBoard Visualization Toolkit
* TensorFlow Code Search

Learn more about theTensorFlow Communityand how toContribute.

## Courses

* Coursera
* Udacity
* Edx

## License

Apache License 2.0