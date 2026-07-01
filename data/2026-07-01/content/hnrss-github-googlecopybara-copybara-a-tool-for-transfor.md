---
title: 'GitHub - google/copybara: Copybara: A tool for transforming and moving code between repositories. · GitHub'
url: https://github.com/google/copybara
site_name: hnrss
content_file: hnrss-github-googlecopybara-copybara-a-tool-for-transfor
fetched_at: '2026-07-01T19:59:05.321610'
original_url: https://github.com/google/copybara
date: '2026-06-30'
description: 'Copybara: A tool for transforming and moving code between repositories. - google/copybara'
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 google

 

/

copybara

Public

* NotificationsYou must be signed in to change notification settings
* Fork316
* Star3.2k

 
 
 
 
master
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

3,651 Commits
3,651 Commits
.docker
.docker
 
 
.github/
workflows
.github/
workflows
 
 
ci/
ubuntu
ci/
ubuntu
 
 
copybara/
integration
copybara/
integration
 
 
docs
docs
 
 
external/
third_party
external/
third_party
 
 
java/
com/
google/
copybara
java/
com/
google/
copybara
 
 
javatests/
com/
google/
copybara
javatests/
com/
google/
copybara
 
 
scripts
scripts
 
 
third_party
third_party
 
 
.bazelproject
.bazelproject
 
 
.bazelrc
.bazelrc
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
AUTHORS
AUTHORS
 
 
BUILD
BUILD
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
ci.Dockerfile
ci.Dockerfile
 
 
cloudbuild.sh
cloudbuild.sh
 
 
cloudbuild.yaml
cloudbuild.yaml
 
 
cloudbuild_setup.sh
cloudbuild_setup.sh
 
 
repositories.bzl
repositories.bzl
 
 
View all files

## Repository files navigation

# Copybara

A tool for transforming and moving code between repositories.

Copybara is a tool used internally at Google. It transforms and moves code between repositories.

Often, source code needs to exist in multiple repositories, and Copybara allows you to transform
and move source code between these repositories. A common case is a project that involves
maintaining a confidential repository and a public repository in sync.

Copybara requires you to choose one of the repositories to be the authoritative repository, so that
there is always one source of truth. However, the tool allows contributions to any repository, and
any repository can be used to cut a release.

The most common use case involves repetitive movement of code from one repository to another.
Copybara can also be used for moving code once to a new repository.

Examples uses of Copybara include:

* Importing sections of code from a confidential repository to a public repository.
* Importing code from a public repository to a confidential repository.
* Importing a change from a non-authoritative repository into the authoritative repository. When
a change is made in the non-authoritative repository (for example, a contributor in the public
repository), Copybara transforms and moves that change into the appropriate place in the
authoritative repository. Any merge conflicts are dealt with in the same way as an out-of-date
change within the authoritative repository.

One of the main features of Copybara is that it is stateless, or more specifically, that it stores
the state in the destination repository (As a label in the commit message). This allows several
users (or a service) to use Copybara for the same config/repositories and get the same result.

Currently, the only supported type of repository is Git. Copybara is also able
to read from Mercurial repositories, but the feature is still experimental.
The extensible architecture allows adding bespoke origins and destinations
for almost any use case.
Official support for other repositories types will be added in the future.

## Example

core
.
workflow
(
 
name
 
=
 
"default"
,
 
origin
 
=
 
git
.
github_origin
(
 
url
 
=
 
"https://github.com/google/copybara.git"
,
 
ref
 
=
 
"master"
,
 ),
 
destination
 
=
 
git
.
destination
(
 
url
 
=
 
"file:///tmp/foo"
,
 ),

 
# Copy everything but don't remove a README_INTERNAL.txt file if it exists.

 
destination_files
 
=
 
glob
([
"third_party/copybara/**"
], 
exclude
 
=
 [
"README_INTERNAL.txt"
]),

 
authoring
 
=
 
authoring
.
pass_thru
(
"Default email <default@default.com>"
),
 
transformations
 
=
 [
 
core
.
replace
(
 
before
 
=
 
"//third_party/bazel/bashunit"
,
 
after
 
=
 
"//another/path:bashunit"
,
 
paths
 
=
 
glob
([
"**/BUILD"
])),
 
core
.
move
(
""
, 
"third_party/copybara"
)
 ],
)

Run:

$ (mkdir /tmp/foo 
;
 
cd
 /tmp/foo 
;
 git init --bare)
$ copybara copy.bara.sky

## Getting Started using Copybara

The easiest way to start is with weekly "snapshot" releases, that include pre-built a binary.
Note that these are released automatically without any manual testing, version compatibility or correctness guarantees.

Choose a release fromhttps://github.com/google/copybara/releases.

### Building from Source

To use an unreleased version of copybara, so you need to compile from HEAD.
In order to do that, you need to do the following:

* Install JDK 11.
* Install Bazel.
* Clone the copybara source locally:git clone https://github.com/google/copybara.git
* git clone https://github.com/google/copybara.git
* Build:bazel build //java/com/google/copybarabazel build //java/com/google/copybara:copybara_deploy.jarto create an executable uberjar.
* bazel build //java/com/google/copybara
* bazel build //java/com/google/copybara:copybara_deploy.jarto create an executable uberjar.
* Tests:bazel test //...if you want to ensure you are not using a broken version. Note that
certain tests require the underlying tool to be installed(e.g. Mercurial, Quilt, etc.). It is
fine to skip those tests if your Pull Request is unrelated to those modules (And our CI will
run all the tests anyway).

### System packages

These packages can be installed using the appropriate package manager for your
system.

#### Arch Linux

* aur/copybara-git

### Using Intellij with Bazel plugin

If you use Intellij and the Bazel plugin, use this project configuration:

directories:
 copybara/integration
 java/com/google/copybara
 javatests/com/google/copybara
 third_party

targets:
 //copybara/integration/...
 //java/com/google/copybara/...
 //javatests/com/google/copybara/...
 //third_party/...

Note: configuration files can be stored in any place, even in a local folder.
We recommend using a VCS (like git) to store them; treat them as source code.

### Using pre-built Copybara in Bazel

If using a weekly snapshot release, install Copybara as follows:

1. Copybara ships with class files with version 65.0, so it must be run with Java Runtime 21 or greater. Add to your.bazelrcfile:run --java_runtime_version=remotejdk_21
2. Usehttp_jarto download the release artifact.* In WORKSPACE:load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")
* In MODULE.bazel:http_jar = use_repo_rule("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")
3. In WORKSPACE or MODULE.bazel, fill in the[version]placeholder:http_jar(name="com_github_google_copybara",# Fill in from https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar.sha256# sha256 = "",urls=["https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar"],
)
4. In any BUILD file (perhaps/tools/BUILD.bazel) declare thejava_binary:load("@rules_java//java:java_binary.bzl","java_binary")java_binary(name="copybara",main_class="com.google.copybara.Main",runtime_deps=["@com_github_google_copybara//jar"],
)
5. Use that target withbazel run, for examplebazel run //tools:copybara -- migrate copy.bara.sky

### Building Copybara from Source as an external Bazel repository

There are convenience macros defined for all of Copybara's dependencies. Add the
following code to yourWORKSPACEfile, replacing{{ sha256sum }}and{{ commit }}as necessary.

http_archive
(
 
name
 
=
 
"com_github_google_copybara"
,
 
sha256
 
=
 
"{{ sha256sum }}"
,
 
strip_prefix
 
=
 
"copybara-{{ commit }}"
,
 
url
 
=
 
"https://github.com/google/copybara/archive/{{ commit }}.zip"
,
)

load
(
"@com_github_google_copybara//:repositories.bzl"
, 
"copybara_repositories"
)

copybara_repositories
()

load
(
"@com_github_google_copybara//:repositories.maven.bzl"
, 
"copybara_maven_repositories"
)

copybara_maven_repositories
()

load
(
"@com_github_google_copybara//:repositories.go.bzl"
, 
"copybara_go_repositories"
)

copybara_go_repositories
()

You can then build and run the Copybara tool from within your workspace:

bazel run @com_github_google_copybara//java/com/google/copybara -- 
<
args...
>

### Using Docker to build and run Copybara

NOTE: Docker use is currently experimental, and we encourage feedback or contributions.

You can build copybara using Docker like so

docker build --rm -t copybara 
.

Once this has finished building, you can run the image like so from the root of
the code you are trying to use Copybara on:

docker run -it -v 
"
$(
pwd
)
"
:/usr/src/app copybara 
help

#### Environment variables

In addition to passing cmd args to the container, you can also set the following
environment variables as an alternative:

* COPYBARA_SUBCOMMAND=migrateallows you to change the command run, defaults tomigrate
* allows you to change the command run, defaults tomigrate
* COPYBARA_CONFIG=copy.bara.skyallows you to specify a path to a config file, defaults to rootcopy.bara.sky
* allows you to specify a path to a config file, defaults to rootcopy.bara.sky
* COPYBARA_WORKFLOW=defaultallows you to specify the workflow to run, defaults todefault
* allows you to specify the workflow to run, defaults todefault
* COPYBARA_SOURCEREF=''allows you to specify the sourceref, defaults to none
* allows you to specify the sourceref, defaults to none
* COPYBARA_OPTIONS=''allows you to specify options for copybara, defaults to none
* allows you to specify options for copybara, defaults to none

docker run \
 -e COPYBARA_SUBCOMMAND=
'
validate
'
 \
 -e COPYBARA_CONFIG=
'
other.config.sky
'
 \
 -v 
"
$(
pwd
)
"
:/usr/src/app \
 -it copybara

#### Git Config and Credentials

There are a number of ways by which to share your git config and ssh credentials
with the Docker container, an example is below:

docker run \
 -v 
~
/.gitconfig:/root/.gitconfig:ro \
 -v 
~
/.ssh:/root/.ssh \
 -v 
${SSH_AUTH_SOCK}
:
${SSH_AUTH_SOCK}
 -e SSH_AUTH_SOCK
 -v 
"
$(
pwd
)
"
:/usr/src/app \
 -it copybara

## Documentation

We are still working on the documentation. Here are some resources:

* Reference documentation
* Examples
* Tutorial on how to get started

## Contact us

If you have any questions about how Copybara works, please contact us at ourmailing list.

## Optional tips

* If you want to see the test errors in Bazel, instead of having tocatthe
logs, add this line to your~/.bazelrc:test --test_output=streamed

## About

Copybara: A tool for transforming and moving code between repositories.

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

3.2k

 stars
 

### Watchers

48

 watching
 

### Forks

316

 forks
 

 Report repository

 

## Releases64

Release v20260629

 Latest

 

Jun 29, 2026

 

+ 63 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Java96.4%
* Starlark2.8%
* Other0.8%