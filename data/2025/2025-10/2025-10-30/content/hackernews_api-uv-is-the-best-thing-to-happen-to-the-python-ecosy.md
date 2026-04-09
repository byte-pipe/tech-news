---
title: uv is the best thing to happen to the Python ecosystem in a decade - Blog - Dr. Emily L. Hunt
url: https://emily.space/posts/251023-uv
site_name: hackernews_api
fetched_at: '2025-10-30T11:08:52.949248'
original_url: https://emily.space/posts/251023-uv
author: Dr. Emily L. Hunt
date: '2025-10-29'
description: Released in 2024, uv is hands-down the best tool for managing Python installations and dependencies. Here's why.
tags:
- hackernews
- trending
---

# uv is the best thing to happen to the Python ecosystem in a decade



Programming



23 October 2025 | Reading time: 6 minutes



It’s 2025. Does installing Python, managing virtual environments, and synchronizing dependencies between your colleagues really have to be so difficult? Well… no! Abrilliantnew tool calleduvcame out recently thatrevolutionizeshow easy installing and using Python can be.



uv is a free, open-source tool built by Astral, a small startup that has been churning out Python tools (like the excellent linterRuff) for the past few years. uv can:


* Install any Python version for you
* Install packages
* Manage virtual environments
* Solve dependency conflictsextremelyquickly (veryimportant for big projects.)


What’s best is that it can do all of the abovebetter than any other tool, in my opinion. It’sshockingly fast, written in Rust, and works on almost any operating system or platform.



## Installing uv



uv isstraightforward to install. There are a few ways, but the easiest (in my opinion) is this one-liner command — for Linux and Mac, it’s:


curl

-LsSf
 https://astral.sh/uv/install.sh
|

sh


or on Windows in powershell:


powershell
-ExecutionPolicy
 ByPass
-c

"irm https://astral.sh/uv/install.ps1 | iex"


You can then access uv with the commanduv.Installing uv will not mess up any of your existing Python installations— it’s a separate tool, so it’s safe to install it just to try it out.



## Managing Python for a project



It’s always a good idea to work withvirtual environmentsfor any Python project. It keeps different bits of code and dependencies ringfenced from one another, and in my experience, it can savea lotof hassle to get into the habit of using virtual environments as soon as you can. uv naturally uses virtual environments, so it’s very easy to start using them if you get into using uv.



uv will build a Python environment for you based on what’s specified in apyproject.tomlfile in the directory (or parent directories) you’re working in.pyproject.tomlfiles are astandard, modern formatfor specifying dependencies for a Python project. A barebones one might look a bit like this:


[
project
]

name

=

"my_project"

version

=

"1.0.0"

requires-python

=

">=3.9,<3.13"

dependencies

=

[


"astropy>=5.0.0"
,


"pandas>=1.0.0,<2.0"
,

]


In essence, it just has to specifywhich Python version to useandsome dependencies.Adding a name and version number also aren’t a bad idea.



(Sidenote: for projects that you publish as packages, such as to the Python Package Index that pip and uv use,pyproject.tomlfiles are a modern way to specifyeverything you needto publish your package.)



## Making a new project with uv



To start a new Python project with uv, you can run


uv init


Which will create a new project for you, with apyproject.toml, aREADME.md, and other important bits of boilerplate.



There are a lot of different ways to run this command, likeuv init --bare(which only creates a pyproject.toml),uv init --package(which sets up a new Python package), and more. I recommend runninguv init --helpto read about them.



## Once you have/if you already have apyproject.tomlfile



Once you initialize a project — or if you already have apyproject.tomlfile in your project — it’s very easy to start using uv. You just need to do


uv
sync


in the directory that yourpyproject.tomlfile is in. This command (and in fact, most uv commands if you haven’t ran it already) will:


1. Automatically install a valid version of Python
2. Install all dependencies to a new virtual environment in the directory.venv
3. Create auv.lockfile in your directory, which saves theexact, platform-agnosticversion ofeverypackage installed — meaning that other colleagues can replicate your Python environment exactly.


In principle, you can ‘activate’ this new virtual environment like any typical virtual environment that you may have seen in other tools, but the most ‘uv-onic’ way to use uv is simply to prepend any command withuv run. This command automatically picks up the correct virtual environment for you and runs your command with it. For instance, to run a script — instead of


source
 .venv/bin/activate
python myscript.py


you can just do


uv run myscript.py


which will have the same effect. Likewise, to use a ‘tool’ like Jupyter Lab, you can just do


uv run jupyter lab


in your project’s directory, as opposed to first ‘activating’ the environment and then runningjupyter labseparately.



## Adding dependencies



You can always just edit yourpyproject.tomlfile manually: uv will detect the changes and rebuild your project’s virtual environment. But uv also has easier ways to add dependencies — you can just do


uv
add
 numpy
>=
2.0


to add a package, including specifying version constraints (like the above.) This command automatically edits yourpyproject.tomlfor you.uv addis also extremely powerful for adding remote dependencies from git or elsewhere on your computer (but I won’t get into that here.)



## Pinning a Python version



Finally, I think that one of the most useful things uv can do is to pin a specific Python version for your project. Doing


uv python pin
3.12
.9


would pin the current project toexactlyPython 3.12.9 for you, and anyone else using uv — meaning that you really can replicate theexactsame Python install across multiple machines.



## uvx: ignore all of the above and just run a tool, now!



But sometimes, you might just want to run a tool quickly — like using Ruff to lint code somewhere, or starting a Jupyter notebook server without an environment, or even just quickly starting an IPython session with pandas installed so you can open up a file. Theuv toolcommand, which has a short aliasuvx, makes this insanely easy. Running a command like


uvx ruff


will automatically download the tool you want to use and run it in a one-off virtual environment. Once the tool has been downloaded before, this is lightning-fast because of how uv uses caches.



There are a lot of occasions when I might want to do this — a common one might be to quickly start an IPython session with pandas installed (using--withto add dependencies) so that I can quickly open & look at a parquet file. For instance:


uvx
--with
 pandas,pyarrow ipython


Or, maybe just starting a Jupyter Lab server so that I can quickly open a Jupyter notebook that a student sent me:


uvx jupyter lab


Or honestly just so many other weird, one-off use cases whereuvxis really nice to have around.I don’t feel like I’m missing out by always using virtual environments, becauseuvxalways gives you a ‘get out of jail free’ card whenever you need it.



## If that hasn’t sold you: a personal note



I first discovered uv last year, while working together with our other lovely developers on buildingThe Astrosky Ecosystem— a wonderful project to build open-source social media integrations for astronomers online. But with multiple developers all working asynchronously on multiple operating systems, managing Python installations quickly became a huge task.



uv is anincredibly powerful simplificationfor us that we use across our entire tech stack. As developers, we can all work with identical Python installations, which is especially important given a number of semi-experimental dependencies that we use that have breaking changes with every version. On GitHub Actions, we’re planning to use uv to quickly build a Python environment and run our unit tests. In production, uv already manages Python for all of our servers.



It’s justso niceto always know that Python and package installation willalwaysbe handledconsistently and correctlyacross all of our machines.That’s why uv is the best thing to happen to the Python ecosystem in a decade.



## Find out more



There’s a lot more onthe uv docs, including agetting started page, morein-depth guides,explanations of important concepts, anda full command reference.
