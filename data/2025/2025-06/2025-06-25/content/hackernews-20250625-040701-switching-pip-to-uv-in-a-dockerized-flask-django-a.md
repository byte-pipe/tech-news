---
title: Switching pip to uv in a Dockerized Flask / Django App — Nick Janetakis
url: https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app
site_name: hackernews
fetched_at: '2025-06-25T04:07:01.484768'
original_url: https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app
date: '2025-06-25'
published_date: '2025-06-17T00:00:00+00:00'
description: I noticed about a 10x speed up across a number of projects, we'll avoid using a venv and run things as a non-root user too.
---

Updated on
June 17, 2025
in#docker,#flask

# Switching pip to uv in a Dockerized Flask / Django App

## I noticed about a 10x speed up across a number of projects, we'll avoid using
a venv and run things as a non-root user too.

Quick Jump:

Prefer video? Here is iton YouTube.

I was surprised at how painless it was to switch things over. You can see the
git diffs to make the change for both of my exampleFlaskandDjangoprojects. In this post we’ll go into more detail about these changes and how to
use a fewuvcommands.

### #pyproject.toml vs requirements.txt

Let’s start with defining our project’s dependencies.

You can create apyproject.tomlfile and delete yourrequirements.txtafter
you’ve entered your project’s dependencies and their versions intopyproject.toml.

You only need to add your top level dependencies, uv will make a lock file for
you automatically which is somewhat comparable to whatpip freezewould
produce except uv’s lock file has proper dependency trees and is way better.

Here’s a very small diff that shows an example of what to do, adjust it as
needed:

# pyproject.toml

+[project]

+dependencies = [

+ "redis==5.2.1",

+]

# requirements.txt

-redis==5.2.1

### #Dockerfile

It’s important that these steps happen in order. For example you’ll want the
environment variables defined before you install your dependencies.

#### Install uv

+COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/

* Ensure bothuvanduvxbinaries are installed on your system’s pathSince uv is a compiled Rust tool we only need statically compiled binariesYou can find the latest release here:https://github.com/astral-sh/uv/releases
* Since uv is a compiled Rust tool we only need statically compiled binaries
* You can find the latest release here:https://github.com/astral-sh/uv/releases

#### Dependency Files

-COPY --chown=python:python requirements*.txt ./

+COPY --chown=python:python pyproject.toml uv.lock* ./

* Reference uv’s dependency related files insteadThat trailing*is important because it makes the lock file optionalThe first time you build your project the lock file might not exist
* That trailing*is important because it makes the lock file optionalThe first time you build your project the lock file might not exist
* The first time you build your project the lock file might not exist

#### Environment Variables

+ENV \

+ UV_COMPILE_BYTECODE=1 \

+ UV_PROJECT_ENVIRONMENT="/home/python/.local" \

* UV_COMPILE_BYTECODEPython source files will be compiled to bytecodeThis is preferred since all bytecode gets compiled once at build timeYour app doesn’t need to do this at run-time when the container starts
* Python source files will be compiled to bytecodeThis is preferred since all bytecode gets compiled once at build timeYour app doesn’t need to do this at run-time when the container starts
* This is preferred since all bytecode gets compiled once at build timeYour app doesn’t need to do this at run-time when the container starts
* Your app doesn’t need to do this at run-time when the container starts
* UV_PROJECT_ENVIRONMENTinstructs uv to not make a virtual environment (venv)My example apps run things as a non-rootpythonuserUltimately all Python dependencies will be installed in this path
* My example apps run things as a non-rootpythonuser
* Ultimately all Python dependencies will be installed in this path

#### Dependency Install Commands

-RUN chmod 0755 bin/* && bin/pip3-install

+RUN chmod 0755 bin/* && bin/uv-install

In both cases I extracted their install commands to a separate script so it’s
easy to either run at build time in the Dockerfile (as seen above), or by
running it as a command at run-time to make sure your lock file gets updated
on your host machine through a volume.

In any case, both solutions are just shell scripts. Here’s the one for uv with
comments:

#!/usr/bin/env bash

set
 -o errexit

set
 -o pipefail

# Ensure we always have an up to date lock file.

if
 !
test
 -f uv.lock
||
 ! uv lock --check 2>/dev/null
;

then

 uv lock

fi

# Use the existing lock file exactly how it is defined.

uv sync --frozen --no-install-project

There’s a few ways to use uv, such as using its pip sub-command but I like
using sync since it’s the “uv way” of doing things. The pip sub-command is
there to help create a mental model of how uv works, or continue using pip’s
commands through uv if you prefer.

The--frozenflag ensures the lock file doesn’t get updated. That’s exactly
what we want because we expect the lock file to have a complete list of exact
versions we want to use for all dependencies that get installed.

The--no-install-projectflag skips installing your code as a Python package.
Since we have apyproject.tomlwith a project defined the default behavior
is to install it as a package.

For a typical web app, you usually have your project’s dependencies and that’s
it. Your project isn’t an installable project in itself. However, if you do
have that use case feel free to remove this flag! You can think of this as
using--editable .with pip.

### #Add, Update or Delete Your Dependencies

If you’re using my example starter app, it comes with a fewrun scriptshortcuts. They’re shortcut shell scripts to run certain commands in a
container:

* ./run deps:installBuild a new image and volume mount out a new lock fileIt’s mainly doingdocker compose buildand runningbin/uv-installinside of a container which has a volume mount so your host’s lock file gets updated
* Build a new image and volume mount out a new lock file
* It’s mainly doingdocker compose buildand runningbin/uv-installinside of a container which has a volume mount so your host’s lock file gets updated
* ./run deps:install --no-buildThe same as above except it skips building but still mounts out a new lock file
* The same as above except it skips building but still mounts out a new lock file
* ./run uv [...]It’s doingdocker compose exec web uv [...]Execute anyuvcommandsyou want, for example:uv add mypackage --no-syncUpdates yourpyproject.tomlfile and lock file but doesn’t install itThen you can run./run deps:installThis will either add a new dependency OR update an existing oneFor adding, if you omit==X.X.Xit will add the current latest version as>=X.X.Xinpyproject.tomlFor updating, include==X.X.Xsopyproject.tomlgets updateduv remove mypackage --no-syncThe same as above except it removes the package
* It’s doingdocker compose exec web uv [...]
* Execute anyuvcommandsyou want, for example:uv add mypackage --no-syncUpdates yourpyproject.tomlfile and lock file but doesn’t install itThen you can run./run deps:installThis will either add a new dependency OR update an existing oneFor adding, if you omit==X.X.Xit will add the current latest version as>=X.X.Xinpyproject.tomlFor updating, include==X.X.Xsopyproject.tomlgets updateduv remove mypackage --no-syncThe same as above except it removes the package
* uv add mypackage --no-syncUpdates yourpyproject.tomlfile and lock file but doesn’t install itThen you can run./run deps:installThis will either add a new dependency OR update an existing oneFor adding, if you omit==X.X.Xit will add the current latest version as>=X.X.Xinpyproject.tomlFor updating, include==X.X.Xsopyproject.tomlgets updated
* Updates yourpyproject.tomlfile and lock file but doesn’t install itThen you can run./run deps:install
* Then you can run./run deps:install
* This will either add a new dependency OR update an existing oneFor adding, if you omit==X.X.Xit will add the current latest version as>=X.X.Xinpyproject.tomlFor updating, include==X.X.Xsopyproject.tomlgets updated
* For adding, if you omit==X.X.Xit will add the current latest version as>=X.X.Xinpyproject.toml
* For updating, include==X.X.Xsopyproject.tomlgets updated
* uv remove mypackage --no-syncThe same as above except it removes the package
* The same as above except it removes the package
* ./run uv:outdatedIt’s doingdocker compose exec web uv tree --outdated --depth 1Show a list of outdated dependencies so you know what to update
* It’s doingdocker compose exec web uv tree --outdated --depth 1
* Show a list of outdated dependencies so you know what to update

The video below goes over the diffs together and runs some of the above commands.

### #Demo Video

#### Timestamps

* 0:17 – TL;DR on uv
* 1:36 – pyproject.toml to replace requirements.txt
* 3:05 – Dockerfile: install uv
* 3:56 – Dockerfile: dependency files
* 4:50 – Dockerfile: env vars
* 6:46 – Dockerfile: uv lock / sync
* 10:22 – Quick recap
* 10:44 – One way to update a package
* 11:41 – Checking for outdated packages
* 13:29 – Using uv add to add or update packages
* 15:27 – Adding a new package at its latest version
* 16:12 – Removing a package

Did you switch to uv, how did it go? Let me know below.
