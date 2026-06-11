---
title: 'GitHub - apache/burr: Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, trace, persist, and execute on your own infrastructure. · GitHub'
url: https://github.com/apache/burr
site_name: tldr
content_file: tldr-github-apacheburr-build-applications-that-make-dec
fetched_at: '2026-06-11T19:53:11.569736'
original_url: https://github.com/apache/burr
date: '2026-06-11'
description: Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, trace, persist, and execute on your own infrastructure. - apache/burr
tags:
- tldr
---

apache

 

/

burr

Public

* NotificationsYou must be signed in to change notification settings
* Fork163
* Star2.3k

 
 
 
 
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

931 Commits
931 Commits
.github
.github
 
 
burr
burr
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
telemetry/
ui
telemetry/
ui
 
 
tests
tests
 
 
website
website
 
 
.asf.yaml
.asf.yaml
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.htaccess
.htaccess
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.rat-excludes
.rat-excludes
 
 
.style.yapf
.style.yapf
 
 
CONTRIBUTING.rst
CONTRIBUTING.rst
 
 
DISCLAIMER
DISCLAIMER
 
 
LICENSE
LICENSE
 
 
LICENSE-wheel
LICENSE-wheel
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
burr_logo.png
burr_logo.png
 
 
burr_logo.svg
burr_logo.svg
 
 
chatbot.gif
chatbot.gif
 
 
pyproject.toml
pyproject.toml
 
 
setup.cfg
setup.cfg
 
 
View all files

## Repository files navigation

# Apache Burr (incubating)

Apache Burr (incubating) makes it easy to develop applications that make decisions (chatbots, agents, simulations, etc...) from simple python building blocks.

Apache Burr works well for any application that uses LLMs, and can integrate with any of your favorite frameworks. Burr includes a UI that can track/monitor/trace your system in real time, along with
pluggable persisters (e.g. for memory) to save & load application state.

Link todocumentation. Quick (<3min) video introhere.
Longervideo intro & walkthrough. Blog posthere. Join discord for help/questionshere.

## 🏃Quick start

Install frompypi:

pip install 
"
apache-burr[start]
"

(seethe docsif you're using poetry)

Then run the UI server:

burr

This will open up Burr's telemetry UI. It comes loaded with some default data so you can click around.
It also has a demo chat application to help demonstrate what the UI captures enabling you too see things changing in
real-time. Hit the "Demos" side bar on the left and selectchatbot. To chat it requires theOPENAI_API_KEYenvironment variable to be set, but you can still see how it works if you don't have an API key set.

Next, start coding / running examples:

git clone https://github.com/apache/burr 
&&
 
cd
 burr/examples/hello-world-counter
python application.py

You'll see the counter example running in the terminal, along with the trace being tracked in the UI.
See if you can find it.

For more details see thegetting started guide.

## 🔩 How does Apache Burr work?

With Apache Burr you express your application as a state machine (i.e. a graph/flowchart).
You can (and should!) use it for anything in which you have to manage state, track complex decisions, add human feedback, or dictate an idempotent, self-persisting workflow.

The core API is simple -- the Burr hello-world looks like this (plug in your own LLM, or copy fromthe docsforgpt-X)

from
 
burr
.
core
 
import
 
action
, 
State
, 
ApplicationBuilder

@
action
(
reads
=
[], 
writes
=
[
"prompt"
, 
"chat_history"
])

def
 
human_input
(
state
: 
State
, 
prompt
: 
str
) 
->
 
State
:
 
# your code -- write what you want here, for example

 
chat_item
 
=
 {
"role"
 : 
"user"
, 
"content"
 : 
prompt
}
 
return
 
state
.
update
(
prompt
=
prompt
).
append
(
chat_history
=
chat_item
)

@
action
(
reads
=
[
"chat_history"
], 
writes
=
[
"response"
, 
"chat_history"
])

def
 
ai_response
(
state
: 
State
) 
->
 
State
:
 
# query the LLM however you want (or don't use an LLM, up to you...)

 
response
 
=
 
_query_llm
(
state
[
"chat_history"
]) 
# Burr doesn't care how you use LLMs!

 
chat_item
 
=
 {
"role"
 : 
"system"
, 
"content"
 : 
response
}
 
return
 
state
.
update
(
response
=
content
).
append
(
chat_history
=
chat_item
)

app
 
=
 (
 
ApplicationBuilder
()
 .
with_actions
(
human_input
, 
ai_response
)
 .
with_transitions
(
 (
"human_input"
, 
"ai_response"
),
 (
"ai_response"
, 
"human_input"
)
 ).
with_state
(
chat_history
=
[])
 .
with_entrypoint
(
"human_input"
)
 .
build
()
)

*
_
, 
state
 
=
 
app
.
run
(
halt_after
=
[
"ai_response"
], 
inputs
=
{
"prompt"
: 
"Who was Aaron Burr, sir?"
})

print
(
"answer:"
, 
app
.
state
[
"response"
])

Apache Burr includes:

1. A (dependency-free) low-abstraction python library that enables you to build and manage state machines with simple python functions
2. A UI you can use view execution telemetry for introspection and debugging
3. A set of integrations to make it easier to persist state, connect to telemetry, and integrate with other systems

## 💻️ What can you do with Apache Burr?

Apache Burr can be used to power a variety of applications, including:

1. A simple gpt-like chatbot
2. A stateful RAG-based chatbot
3. An LLM-based adventure game
4. An interactive assistant for writing emails

As well as a variety of (non-LLM) use-cases, including a time-series forecastingsimulation,
andhyperparameter tuning.

And a lot more!

Using hooks and other integrations you can (a) integrate with any of your favorite vendors (LLM observability, storage, etc...), and
(b) build custom actions that delegate to your favorite libraries (likeApache Hamilton).

Apache Burr willnottell you how to build your models, how to query APIs, or how to manage your data. It will help you tie all these together
in a way that scales with your needs and makes following the logic of your system easy. Burr comes out of the box with a host of integrations
including tooling to build a UI in streamlit and watch your state machine execute.

## 🏗 Start building

See the documentation forgetting started, and follow the example.
Then read through some of the concepts and write your own application!

## 📃 Comparison against common frameworks

While Apache Burr is attempting something (somewhat) unique, there are a variety of tools that occupy similar spaces:

Criteria

Apache Burr

Langgraph

temporal

Langchain

Superagent

Apache Hamilton

Explicitly models a state machine

✅

✅

❌

❌

❌

❌

Framework-agnostic

✅

✅

✅

✅

❌

✅

Asynchronous event-based orchestration

❌

❌

✅

❌

❌

❌

Built for core web-service logic

✅

✅

❌

✅

✅

✅

Open-source user-interface for monitoring/tracing

✅

❌

❌

❌

❌

✅

Works with non-LLM use-cases

✅

❌

❌

❌

❌

✅

## 🌯 Why the name Burr?

Apache Burr is named afterAaron Burr, founding father, third VP of the United States, and murderer/arch-nemesis ofAlexander Hamilton.
What's the connection with (Apache) Hamilton? We imagine a world in which Burr and Hamilton lived in harmony and saw through their differences to better the union. Originally Apache Burr was built as aharnessto handle state between executions of Apache Hamilton DAGs (because DAGs don't have cycles),
but realized that it has a wide array of applications and decided to release it more broadly.

# Testimonials

"After evaluating several other obfuscating LLM frameworks, their elegant yet comprehensive state management solution proved to be the powerful answer to rolling out robots driven by AI decision-making."

Ashish GhoshCTO, Peanut Robotics

"Of course, you can use it [LangChain], but whether it's really production-ready and improves the time from 'code-to-prod' [...], we've been doing LLM apps for two years, and the answer is no [...] All these 'all-in-one' libs suffer from this [...]. Honestly, take a look at Burr. Thank me later."

Reddit user cyan2kLocalLlama, Subreddit

"Using Burr is a no-brainer if you want to build a modular AI application. It is so easy to build with, and I especially love their UI which makes debugging a piece of cake. And the always-ready-to-help team is the cherry on top."

IshitaFounder, Watto.ai

"I just came across Burr and I'm like WOW, this seems like you guys predicted this exact need when building this. No weird esoteric concepts just because it's AI."

Matthew RideoutStaff Software Engineer, Paxton AI

"Burr's state management part is really helpful for creating state snapshots and building debugging, replaying, and even evaluation cases around that."

Rinat GareevSenior Solutions Architect, Provectus

"I have been using Burr over the past few months, and compared to many agentic LLM platforms out there (e.g. LangChain, CrewAi, AutoGen, Agency Swarm, etc), Burr provides a more robust framework for designing complex behaviors."

Hadi NayebiCo-founder, CognitiveGraphs

"Moving from LangChain to Burr was a game-changer!

* Time-Saving: It took me just a few hours to get started with Burr, compared to the days and weeks I spent trying to navigate LangChain.
* Cleaner Implementation: With Burr, I could finally have a cleaner, more sophisticated, and stable implementation. No more wrestling with complex codebases.
* Team Adoption: I pitched Burr to my teammates, and we pivoted our entire codebase to it. It's been a smooth ride ever since."

Aditya K.DS Architect, TaskHuman

## 🛣 Roadmap

While Apache Burr is stable and well-tested, we have quite a few tools/features on our roadmap!

1. FastAPI integration + hosted deployment -- make it really easy to get Apache Burr in an app in production without thinking about REST APIs
2. Various efficiency/usability improvements for the core library (seeplanned capabilitiesfor more details). This includes:First-class support for retries + exception managementMore integration with popular frameworks (LCEL, LLamaIndex, Apache Hamilton, etc...)Capturing & surfacing extra metadata, e.g. annotations for particular point in time, that you can then pull out for fine-tuning, etc.Improvements to the pydantic-based typing system
3. First-class support for retries + exception management
4. More integration with popular frameworks (LCEL, LLamaIndex, Apache Hamilton, etc...)
5. Capturing & surfacing extra metadata, e.g. annotations for particular point in time, that you can then pull out for fine-tuning, etc.
6. Improvements to the pydantic-based typing system
7. Tooling for hosted execution of state machines, integrating with your infrastructure (Ray, modal, FastAPI + EC2, etc...)
8. Additional storage integrations. More integrations with technologies like MySQL, S3, etc. so you can run Apache Burr on top of what you have available.

If you want to avoid self-hosting the above solutions we're building Burr Cloud. To let us know you're interested
sign upherefor the waitlist to get access.

## 🤲 Contributing

We welcome contributors! To get started on developing, see thedeveloper-facing docs.

## 👪 Contributors

### Code contributions

Users who have contributed core functionality, integrations, or examples.

* Elijah ben Izzy
* Stefan Krawczyk
* Joseph Booth
* Nandani Thakur
* Thierry Jean
* Hamza Farhan
* Abdul Rafay
* Margaret Lange

### Bug hunters/special mentions

Users who have contributed small docs fixes, design suggestions, and found bugs

* Luke Chadwick
* Evans
* Sasmitha Manathunga

# 📑 License

Apache Burr is released under the Apache 2.0 License. SeeLICENSEfor details.

# 🌎 Community

## 👨‍💻 Contributing

We're very supportive of changes by new contributors, big or small! Make sure to discuss potential changes by creating an issue or commenting on an existing one before opening a pull request. Good first contributions include creating an example or an integration with your favorite Python library!

To contribute, checkout ourcontributing guidelines, ourdeveloper setup guide, and ourCode of Conduct.

## About

Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, trace, persist, and execute on your own infrastructure.

burr.apache.org/

### Topics

 state-management

 ai

 state-machine

 graphs

 visibility

 persistent-data-structure

 hacktoberfest

 chatbot-framework

 dags

 burr

 mlops

 llms

 generative-ai

 llmops

### Resources

 Readme

 

### License

 Apache-2.0, Apache-2.0 licenses found
 

### Licenses found

Apache-2.0

LICENSE

 

Apache-2.0

LICENSE-wheel

 

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

2.3k

 stars
 

### Watchers

13

 watching
 

### Forks

163

 forks
 

 Report repository

 

## Releases73

Apache Burr 0.42.0-incubating

 Latest

 

May 10, 2026

 

+ 72 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python63.0%
* TypeScript34.4%
* HCL1.0%
* CSS0.5%
* Jinja0.3%
* Shell0.3%
* Other0.5%