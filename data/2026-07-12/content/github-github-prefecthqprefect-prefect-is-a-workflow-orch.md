---
title: 'GitHub - PrefectHQ/prefect: Prefect is a workflow orchestration framework for building resilient data pipelines in Python. · GitHub'
url: https://github.com/PrefectHQ/prefect
site_name: github
content_file: github-github-prefecthqprefect-prefect-is-a-workflow-orch
fetched_at: '2026-07-12T11:27:16.407269'
original_url: https://github.com/PrefectHQ/prefect
author: PrefectHQ
description: Prefect is a workflow orchestration framework for building resilient data pipelines in Python. - PrefectHQ/prefect
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 PrefectHQ

 

/

prefect

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.4k
* Star23k

 
 
 
 
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

21,759 Commits
21,759 Commits
.claude
.claude
 
 
.github
.github
 
 
benches
benches
 
 
client
client
 
 
compat-tests @ 3c5ec01
compat-tests @ 3c5ec01
 
 
docs
docs
 
 
examples
examples
 
 
integration-tests
integration-tests
 
 
load_testing
load_testing
 
 
plans
plans
 
 
schemas
schemas
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
ui-v2
ui-v2
 
 
ui
ui
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.nvmrc
.nvmrc
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.prefectignore
.prefectignore
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.sqlite-builder
Dockerfile.sqlite-builder
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
hatch_build.py
hatch_build.py
 
 
justfile
justfile
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Installation·Quickstart·Build workflows·Deploy workflows·Prefect Cloud

# Prefect

Prefect is a workflow orchestration framework for building data pipelines in Python.
It's the simplest way to elevate a script into a production workflow.
With Prefect, you can build resilient, dynamic data pipelines that react to the world around them and recover from unexpected changes.

With just a few lines of code, data teams can confidently automate any data process with features such as scheduling, caching, retries, and event-based automations.

Workflow activity is tracked and can be monitored with a self-hostedPrefect serverinstance or managedPrefect Clouddashboard.

Tip

Prefect flows can handle retries, dependencies, and even complex branching logic

Check our docsor see the example below to learn more!

## Getting started

Prefect requires Python 3.10+. Toinstall the latest version of Prefect, run one of the following commands:

pip install -U prefect

uv add prefect

Then create and run a Python file that uses Prefectflowandtaskdecorators to orchestrate and observe your workflow - in this case, a simple script that fetches the number of GitHub stars from a repository:

from
 
prefect
 
import
 
flow
, 
task

import
 
httpx

@
task
(
log_prints
=
True
)

def
 
get_stars
(
repo
: 
str
):
 
url
 
=
 
f"https://api.github.com/repos/
{
repo
}
"

 
count
 
=
 
httpx
.
get
(
url
).
json
()[
"stargazers_count"
]
 
print
(
f"
{
repo
}
 has 
{
count
}
 stars!"
)

@
flow
(
name
=
"GitHub Stars"
)

def
 
github_stars
(
repos
: 
list
[
str
]):
 
for
 
repo
 
in
 
repos
:
 
get_stars
(
repo
)

# run the flow!

if
 
__name__
 
==
 
"__main__"
:
 
github_stars
([
"PrefectHQ/prefect"
])

Fire up a Prefect server and open the UI athttp://localhost:4200to see what happened:

prefect server start

To run your workflow on a schedule, turn it into a deployment and schedule it to run every minute by changing the last line of your script to the following:

if
 
__name__
 
==
 
"__main__"
:
 
github_stars
.
serve
(
 
name
=
"first-deployment"
,
 
cron
=
"* * * * *"
,
 
parameters
=
{
"repos"
: [
"PrefectHQ/prefect"
]}
 )

You now have a process running locally that is looking for scheduled deployments!
Additionally you can run your workflow manually from the UI or CLI. You can even run deployments in response toevents.

Tip

Where to go next - check out ourdocumentationto learn more about:

* Deploying flows to production environments
* Adding error handling and retries
* Integrating with your existing tools
* Setting up team collaboration features

## Prefect Cloud

Prefect Cloud provides workflow orchestration for the modern data enterprise. By automating over 200 million data tasks monthly, Prefect empowers diverse organizations — from Fortune 50 leaders such as Progressive Insurance to innovative disruptors such as Cash App — to increase engineering productivity, reduce pipeline errors, and cut data workflow compute costs.

Read more about Prefect Cloudhereor sign up totry it for yourself.

## prefect-client

If your use case is geared towards communicating with Prefect Cloud or a remote Prefect server, check out ourprefect-client. It is a lighter-weight option for accessing client-side functionality in the Prefect SDK and is ideal for use in ephemeral execution environments.

## Connect & Contribute

Join a thriving community of over 25,000 practitioners who solve data challenges with Prefect. Prefect's community is built on collaboration, technical innovation, and continuous improvement.

### Community Resources

🌐Explore the Documentation- Comprehensive guides and API references💬Join the Slack Community- Connect with thousands of practitioners🤝Contribute to Prefect- Help shape the future of the project🔌Support or create a new Prefect integration- Extend Prefect's capabilities📋Tail the Dev Log- Prefect's open source development blog

### Stay Informed

📥Subscribe to our Newsletter- Get the latest Prefect news and updates📣XandBluesky- Latest updates and announcements📺YouTube- Video tutorials and webinars📱LinkedIn- Professional networking and company news

Your contributions, questions, and ideas make Prefect better every day. Whether you're reporting bugs, suggesting features, or improving documentation, your input is invaluable to the Prefect community.

## About

Prefect is a workflow orchestration framework for building resilient data pipelines in Python.

prefect.io

### Topics

 python

 infrastructure

 workflow

 data-science

 data

 automation

 pipeline

 workflow-engine

 orchestration

 data-engineering

 observability

 prefect

 data-ops

 ml-ops

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

23k

 stars
 

### Watchers

197

 watching
 

### Forks

2.4k

 forks
 

 Report repository

 

## Releases858

3.7.8 - The flush must go on

 Latest

 

Jul 9, 2026

 

+ 857 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Used by8k

 + 7,957
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python79.6%
* TypeScript19.6%
* Vue0.4%
* CSS0.2%
* Just0.1%
* Jinja0.1%