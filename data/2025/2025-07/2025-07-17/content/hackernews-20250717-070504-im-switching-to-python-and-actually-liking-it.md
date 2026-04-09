---
title: I'm Switching to Python and Actually Liking It
url: https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html
site_name: hackernews
fetched_at: '2025-07-17T07:05:04.923633'
original_url: https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html
author: César Soto Valero
date: '2025-07-17'
published_date: '2025-07-15T00:00:00-07:00'
description: I’ve started writing more Python code lately (because of… AI, you know). In this post, I share the tools, libraries, configs, and other integrations I use for building production-grade Python applications following a frontend-backend architecture.
---

I started to code more inPythonaround 6 months ago.
Why?
Because of AI, obviously.
It’s clear (to me) that bigmoneyopportunities are all over AI these days.
And guess what’s thede factoprogramming language for AI?
Yep, that sneaky one.

I had used Python before, but only for small scripts.
For example,this scriptscrapes metadata from all videos onmy YouTube channel.
The metadata is dumped asa JSON filethat I use to nicely display statistics of the videoson this static page.
As you cansee here, this little script runs in solo mode every Monday via GitHub Actions.
Doing this kind of thing in Python is just way more convenient than, say, using Batch.
Not only because the syntax is more human-friendly, but also because the Python interpreter is natively integrated in all Unix distros.
Isn’t that cool?

So yeah, Python is powerful, and it couples very well with the now ubiquitousVSCodeeditor.
But I didn’t treat it seriously until recently,1it was just after I wanted to build AI applications (RAG, Agents, GenAI tools, etc.) for the “real world” that I realized that whether you like it or not, Python is the language of choice for that matters.

So I decided to give it a serious try, and to my great surprise, I’ve found that Python, and everything around it, has really improved a lot over the last decades.

Here’re just three examples:

1. Python has created a very complete ecosystem of libraries and tools for processing and analyzing data.2
2. Python has gotten faster with optimized static compilers likeCython.
3. Python has done a good job of hiding its legacy ugliness (such as__init__,__new__, and similar aberrations), swettening its syntax to accomodate developerswith good taste.

Thanks to this and many other things, I’m now feeling a particular joy for the language.

However, during this time, I’ve found that there’s still a big gap between using Python for “production-ready”3apps vs. the usual Jupyter notebook or script-based workflow.

So in this post, I share the tools, libraries, configs, and other integrations that bring me joy, and that I now use for building my Python applications.

⚠️ This post is highly biased toward the tools I personally use today, and if you think I’m missing some gem, please let me/us know (preferably in the comment section below).

# Project Structure

I prefer to use amonorepostructure (backend and frontend) for my Python projects.4

Why?

1. Because of my bad memory: I don’t like code parts scattered across multiple repositories (it’s definitely not search-friendly).
2. Because having multiple repost is mostly unnecessary: I’m just one guy, and I believe that if a project grows to the point that it needs to be split into multiple repositories, then it’s a sign of over-engineering.
3. Because I’m lazy: I like to keep things as simple as possible, compile, test, containerize, and deploy from a single location.5

I would like to have a tool that generates the project structure for me, but I haven’t found one that fits me yet.
In the past, I usedCCDS, a project initialization tool mostly for Data Science projects.
It’s very good, but it’s not targeting full-stack developers as its core users.

Here’s the typical structure of a project with a frontend-backend architecture (I’ll go through each subpart later in this post):

project/
│
├── .github/
# GitHub Actions workflows for CI/CD pipelines

│ ├── workflows/
# Directory containing YAML files for automated workflows

│ └── dependabot.yml
# Configuration for Dependabot to manage dependencies

│
├── .vscode/
# VSCode configuration for the project

│ ├── launch.json
# Debugging configurations for VSCode

│ └── settings.json
# Project-specific settings for VSCode

│
├── docs/
# Website and docs (a static SPA with MkDocs)

│
├── project-api/
# Backend API for handling business logic and heavy processing

│ ├── data/
# Directory for storing datasets or other static files

│ ├── notebooks/
# Jupyter notebooks for quick (and dirty) experimentation and prototyping

│ ├── tools/
# Utility scripts and tools for development or deployment

│ ├── src/
# Source code for the backend application

│ │ ├── app/
# Main application code

│ │ └── tests/
# Unit tests for the backend

│ │
│ ├── .dockerignore
# Specifies files to exclude from Docker builds

│ ├── .python-version
# Python version specification for pyenv

│ ├── Dockerfile
# Docker configuration for containerizing the backend

│ ├── Makefile
# Automation tasks for building, testing, and deploying

│ ├── pyproject.toml
# Python project configuration file

│ ├── README.md
# Documentation for the backend API

│ └── uv.lock
# Lock file for dependencies managed by UV

│
├── project-ui/
# Frontend UI for the project (Next.js, React, etc.)

│
├── .gitignore
# Global Git ignore file for the repository

├── .pre-commit-config.yaml
# Configuration for pre-commit hooks

├── CONTRIBUTING.md
# Guidelines for contributing to the project

├── docker-compose.yml
# Docker Compose configuration for multi-container setups

├── LICENSE
# License information for the project (I always choose MIT)

├── Makefile
# Automation tasks for building, testing, and deploying

└── README.md
# Main documentation for the project (main features, installation, and usage)

Myprojectis the root directory and the name of my GitHub repo.
I like short names for projects, ideally less than 10 characters long. Nosnake_case; separation with hyphens is OK to me.
Note that the project should be self-contained, meaning it includes documentation, build/deployment infrastructure, and any other necessary files to run it standalone.

It’s important not to do any heavy data processing steps in theproject-ui, as I opted to separate frontend logic from backend responsibilities.
Instead, I choose to make HTTP requests to theproject-apiserver that contains the Python code.
This way, we keep the browser application light while delegating the heavy lifting and business logic to the server.

There’s an__init__.pyfile inproject-api/src/appto indicate thatappis a Python module (it can be imported from other modules).

# Python Toolbox

## uv

I useuvas my Python package manager and build tool. It’s all I need to install and manage dependencies.

Here are the core commands to set it up:

1
2
3
4
5
6
7
8
9
10
11
12
13
14

# Install uv globally if not already installed

curl
-sSfL
 <https://astral.sh/install.sh> | sh

# Initialize a new project (adds .gitignore, .python-version, pyproject.toml, etc.)

uv init project-api

# Add some dependencies into the project and update pyproject.toml

uv add
--dev
 pytest ruff pre-commit mkdocs gitleaks fastapi pydantic

# Update the lock file with the latest versions of the dependencies (creates a .venv if not already created)

uv
sync

# Activate the .venv

uv venv activate

Note that the most important file foruvispyproject.toml.6This filecontainsmetadata and the list of dependencies required to build and run the project.

## ruff

I really likeruff.
It’s a super-fast Python linter and code formatter, designed to help lazy developers like me keep our codebases clean and maintainable.
Ruff combinesisort,flake8,autoflake, and similar tools into a single command-line interface:

1
2
3
4

# Lint all files in `/path/to/code` (and any subdirectories).

ruff check path/to/code/

# Format all files in `/path/to/code` (and any subdirectories).

ruff format path/to/code/

Ruff supports thePEP 8style guide out of the box.

## ty

tyis a type checker for Python.
It is a great combo fortyping, the popular Python module for adding static typing.
I think typing really helps me catch type errors early in the development process. I actually don’t care about having to write more code, in fact, I prefer it if it improves code quality and reduces the likelihood of runtime errors.

NOTE:At the time of writing,tyis still in early development by Astral (the same company behinduvandruff), but I’ve been using it and haven’t found any noticeable flaws so far.

## pytest

pytestisTHEtesting library for Python.
Writing simple and scalable test cases with it is just super easy.
It supports fixtures, parameterized tests, and has a rich ecosystem of plugins.
Just create a file namedtest_<unit_or_module>.pyinproject-api/src/app/tests/, and run:

uv run pytest

That’s it!

## Pydantic

Pydanticis a data validation and settings management library for Python.
It helps manage all kinds of configuration settings, such as API keys, database connection details, or model parameters (hardcoding these values is a very bad practice, btw).

In particular,Pydantic Settingsallows you to define application configurations using Pydantic models.
It can automatically load settings from environment variables or special.envfiles, validate their types, and make them easily accessible in your code.

Here’s an illustrative example:

1
2
3
4
5
6
7
8
9
10

from

pydantic

import

BaseSettings

class

Settings
(
BaseSettings
):


api_key
:

str


db_url
:

str


class

Config
:


env_file

=

"
.env
"

settings

=

Settings
()

Now, when you run this code, Pydantic will automatically load the values ofapi_keyanddb_urlfrom the.envfile or environment variables.
These values will be accessible and validated according to the types defined in theSettingsmodel.
Just great!

## MkDocs

I useMkDocsfor documentation and static generation of the website for the project.7I’m not a designer, so I prefer to just copy an aesthetically pleasing design from another similar open-source project and make some simple modifications to the CSS (like changing fonts and colors).

## FastAPI

I useFastAPIfor building APIs.
It has been a game changer for me, it allows for easy creation of RESTful APIs with automatic validation, serialization, and documentation.
FastAPI is built on top of Starlette and Pydantic, which means it provides excellent performance and type safety.
It’s fast, easy to use, and integrates seamlessly with Pydantic for data validation.

## Dataclasses

Dataclassesis not a library but a Python feature that provides a way to define classes that are primarily used to store data.
They offer a simple syntax for creating classes that automatically generate special methods like__init__(),__repr__(), and__eq__().

This greatly reduces boilerplate when creating data containers.

Here’s an example:

1
2
3
4
5
6
7
8
9

from

dataclasses

import

dataclass

@dataclass

class

Point
:


x
:

int


y
:

int

p

=

Point
(
1
,

2
)

print
(
p
)

# Output: Point(x=1, y=2)

So goodbye boilerplate and cryptic code!

# Version Control

## GitHub Actions

I’m a fanboy ofGitHub Actions, especially for CI across different OSs.
I recommend using it for both API and UI pipelines.

A typical workflow forproject-apilooks like this:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

name
:

CI-API

on
:


push
:


branches
:


-

main


pull_request
:


branches
:


-

main

jobs
:


build-and-test
:


runs-on
:

ubuntu-latest


steps
:


-

name
:

Checkout code


uses
:

actions/checkout@v3


-

name
:

Build Docker image


run
:

docker build -t project-api:ci ./project-api


-

name
:

Run tests


run
:

docker run --rm project-api:ci pytest

Note that this workflow uses Docker to run the tests in an isolated environment.8You can change the OS by setting theruns-onparameter towindows-latestormacos-latest.

## Dependabot

Handling dependencies is a pain, butDependabotmakes it easier.
It automatically checks for outdated dependencies and creates pull requests to update them.

Here’s a sample configuration for Dependabot in the.github/dependabot.ymlfile:

1
2
3
4
5
6
7

version
:

2

updates
:

-

package-ecosystem
:

"
uv"


directory
:

"
/"


schedule
:


interval
:

"
weekly"

## Gitleaks

If there’s something that could hurt our reputation, it’s committing sensitive information, like API keys or passwords, directly to a repository.
Fortunately,Gitleakshelps prevent this from happening.
There’s just no reason not to use it.

## Pre-commit Hooks

I usepre-committo run checks and format code before committing.
It helps ensure that the code is always in a good state and follows the project’s coding standards.
For example, I use it to runruff-pre-commitandgitleaksbefore committing my code.

Here’s a sample.pre-commit-config.yamlfile that I use:

1
2
3
4
5
6
7
8
9
10
11
12

repos
:

repos
:


-

repo
:

https://github.com/astral-sh/ruff-pre-commit


rev
:

v0.12.3

# Ruff version.


hooks
:


-

id
:

ruff-check

# Run the linter.


args
:

[

--fix

]


-

id
:

ruff-format

# Run the formatter.


-

repo
:

https://github.com/gitleaks/gitleaks


rev
:

v8.27.2


hooks
:


-

id
:

gitleaks

# Infrastructure Management

## Make

Makeis a Swiss Army knife, a classic utility for automating tasks.
I use it to create simple shortcuts for common development commands.
Instead of remembering and typing out long CLI incantations to run tests, build Docker images, or start services, I define these tasks in aMakefile.
Then I just run commands likemake testormake infrastructure-up.

As you might have noticed, there is aMakefilein both theproject-apiand the globalprojectdirectories:

1. project/project-api/Makefile: For linting, testing, and running the API.
2. project/Makefile: For building and running the infrastructure (viadocker-compose).

Here’s an extremely simple example of theproject-apiMakefile:

1
2
3
4
5
6
7
8
9
10
11

DIR := . # project/project-api/Makefile

test:
 uv run pytest

format-fix:
 uv run ruff format $(DIR)
 uv run ruff check --select I --fix

lint-fix:
 uv run ruff check --fix

Now, if I want to run the tests, I just runmake test, and it executesuv run pytestin the current directory.

For the global project, I use the followingMakefile:

1
2
3
4
5
6
7
8

infrastructure-build:
 docker compose build

infrastructure-up:
 docker compose up --build -d

infrastructure-stop:
 docker compose stop

makeis a powerful tool that can help you automate almost anything in your development workflow.
Although the examples above are very simple, just imagine how you can add more complex tasks as needed.

## Docker

Dockeris a tool that allows you to package your application and its dependencies into a container,including everything needed to run: dependencies, system tools, code, and runtime OS.
When working locally, I useDocker Composeto connect all Docker images into the same network.
Like Docker for dependencies, Docker Compose allows encapsulating the whole application stack and separating it from the rest of your local environment.

To fully grasp this concept, let’s take a look at a simpledocker-compose.ymlfile:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

version
:

'
3.8'

services
:


project-api
:


build
:


context
:

./project-api


dockerfile
:

Dockerfile


ports
:


-

"
8000:8000"


volumes
:


-

./project-api:/app


environment
:


-

ENV_VAR=value


networks
:


-

project-network


project-ui
:


build
:


context
:

./project-ui


dockerfile
:

Dockerfile


ports
:


-

"
3000:3000"


networks
:


-

project-network

networks
:


project-network
:


driver
:

bridge

In this file, we define two services:project-apiandproject-ui.
Each service has its own build context (Dockerfile), ports, volumes, and environment variables.

Here’s a sampleDockerfilefor theproject-apiservice:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

FROM
 python:3.11-slim

# Install system dependencies

COPY
 --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR
 /app

COPY
 uv.lock pyproject.toml README.md ./

RUN
uv
sync

--frozen

--no-cache

# Bring in the actual application code

COPY
 src/app app/

COPY
 tools tools/

# Define a command to run the application

CMD
 ["/app/.venv/bin/fastapi", "run", "project/infrastructure/api.py", "--port", "8000", "--host", "0.0.0.0"]

As you can see, the Dockerfile starts from a Python base image, installs dependencies, copies the project files, and defines the command to run the FastAPI application.

This way, you can run the entire application stack with a single command:

docker compose up
--build

-d

# Footnotes

1. If you know me, you know I used to be mostly a Java/JavaScript/R kind of guy.↩
2. For example, todayJupyteris bundled by almost every major cloud provider as the de facto tool for interactive data science and scientific computing.↩
3. “Production-ready,” for me, means I can deploy the app to the cloud as-is, without needing to make a lot of infrastructure changes.↩
4. Don’t get me wrong, I understand there are cases where a multi-repo structure is necessary, like when multiple teams work on different parts of the project or when dependencies needs to be shared across projects.↩
5. I believe that aviding premature decomposition is a good idea. If a codebase is less than, say, 1/2 million LoC, then setting a network layer (like API calls) over it only would make maintenance a pain fornon-Amazonrational developers.↩
6. Thepyproject.tomlfile is similar topackage.jsonin Node.js orpom.xmlin Java.↩
7. By the way, I think every single project on GitHub should have its own website (it’s extremely easy viaGitHub Pages), so no excuses, sorry.↩
8. Using Docker for CI ensures parity with production environments, but it might add some cold-start overhead. You know… compromises, life is full of them.↩
