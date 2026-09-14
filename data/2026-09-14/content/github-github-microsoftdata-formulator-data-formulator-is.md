---
title: 'GitHub - microsoft/data-formulator: 🪄 Data Formulator is an interactive AI-powered data analysis system makes it easy to connect, explore and visualize data. · GitHub'
url: https://github.com/microsoft/data-formulator
site_name: github
content_file: github-github-microsoftdata-formulator-data-formulator-is
fetched_at: '2026-09-14T16:47:19.083830'
original_url: https://github.com/microsoft/data-formulator
author: microsoft
description: 🪄 Data Formulator is an interactive AI-powered data analysis system makes it easy to connect, explore and visualize data. - microsoft/data-formulator
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 microsoft

 

/

data-formulator

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.7k
* Star17.2k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,435 Commits
1,435 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude
.claude
 
 
.cursor
.cursor
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
docs
docs
 
 
examples/
plugins
examples/
plugins
 
 
loops/
model-evaluation
loops/
model-evaluation
 
 
packaging
packaging
 
 
public
public
 
 
py-src/
data_formulator
py-src/
data_formulator
 
 
src
src
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.template
.env.template
 
 
.gitignore
.gitignore
 
 
.python-version
.python-version
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODESPACES.md
CODESPACES.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.js
eslint.config.js
 
 
index.html
index.html
 
 
local_server.bat
local_server.bat
 
 
local_server.sh
local_server.sh
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
pytest.ini
pytest.ini
 
 
requirements.txt
requirements.txt
 
 
tsconfig.json
tsconfig.json
 
 
uv.lock
uv.lock
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

# Data Formulator: AI-powered Data Visualization

🪄 Explore data with visualizations, powered by AI agents.

  
 

 
 
 
 
 
 
 
 

## Why Data Formulator?

Working with data is hard for two simple reasons:

1. Data lives everywhere.Connecting agents to files, databases,
warehouses, and BI tools takes time. It is even harder when agents start
answering before the relationships between data sources are clear.
2. Questions evolve as you explore.Each answer can lead to follow-up
questions, comparisons, and new directions. A long chat history makes it
hard to see where you are and how you got there.

Data Formulator provides one visual workspace for exploring and analyzing data:

1. Data connectorsgive agents a common way to connect to different data
sources and maintains a data memory to remember the relationships between them.
2. Data Threadslet you branch into different questions, compare paths,
and use visualizations to discover deeper insights without losing context.

Data.Formulator-0.7-1080p.mp4

Tip

Love the charts?They're built onFlint. It's an open-source visualization language that compiles compact chart specs into polished visualizations.

## News 🔥🔥🔥

[08-15-2026]Data Formulator 0.8 beta 1(0.8.0b1) introduces:

* One unified flow:load data, ask questions, review results, and branch in the Data Thread.
* More data sources:use files, local folders, databases, and platforms such as Databricks.
* Better charts:explore more Flint-powered charts, recommendations, themes, and styling tools.

Preview withpip install --pre data_formulator==0.8.0b1oruvx data_formulator@0.8.0b1.
Install the latest stable release (0.7) withpip install data_formulatoror run instantly withuvx data_formulator.

See thechangelogfor release details.

## Previous Updates

Here are milestones that lead to the current design:

* v0.7(05-28-2026): Turn ANY data into insights in five steps — connect governed data sources, load via agents, explore with the unifiedDataAgent+ Data Thread, refine 30+ chart types (semantic chart engine powered byFlint) with a style-refinement agent, and share as reports. Plus persistent sessions & workspaces and a multilingual (English/Chinese) UI.
* v0.6(Demo): Real-time insights from live data — connect to URLs and databases with automatic refresh
* uv support: Faster installation withuv—uvx data_formulatororuv pip install data_formulator
* v0.5.1(Demo): Community data loaders, US Map & Pie Chart, editable reports, snappier UI
* v0.5: Vibe with your data, in control — agent mode, data extraction, reports
* v0.2.2(Demo): Goal-driven exploration with agent recommendations and performance improvements
* v0.2.1.3/4(Readme|Demo): External data loaders (MySQL, PostgreSQL, MSSQL, Azure Data Explorer, S3, Azure Blob)
* v0.2(Demos): Large data support with DuckDB integration
* v0.1.7(Demos): Dataset anchoring for cleaner workflows
* v0.1.6(Demo): Multi-table support with automatic joins
* Model Support: OpenAI, Azure, Ollama, Anthropic viaLiteLLM(feedback)
* Python Package: Easy local installation (try it)
* Visualization Challenges: Test your skills (challenges)
* Data Extraction: Parse data from images and text (demo)
* Initial Release:Blog|Video

## Overview

Data Formulatoris a Microsoft Research project for data exploration with visualizations powered by AI agents. It combinesUI interactionswithnatural languageso analysts can communicate intent, branch into alternative analyses, and share results — starting from any data format (screenshot, text, CSV, or database).

## Get Started

Play with Data Formulator with one of the following options.

### Desktop downloads

CI builds self-contained Windows and macOS applications for pull requests and
every update tomain. Download the latest archives from theArtifactssection of the most recentdesktop builds workflow.
Workflow artifacts are retained for 30 days. Tagged builds are also attached
as permanent downloads to the correspondingGitHub Release.

Extract the archive, then launch Data Formulator using the instructions for
your operating system:

* Windows:RunData Formulator.exe. If Microsoft Defender SmartScreen
appears, selectMore info, verify that you downloaded the archive from
this repository, and then selectRun anyway.
* macOS:MoveData Formulator.apptoApplications. The first time you
open it, macOS may report that Apple could not verify the app. OpenSystem Settings → Privacy & Security, scroll toSecurity, and selectOpen Anywayfor Data Formulator. Confirm by selectingOpenwhen
prompted.

Warning

These are automated preview builds and are not currently code-signed or
notarized. Only bypass the operating-system warning when the archive was
downloaded directly from this repository's workflow artifacts or releases.

* Option 1: Install via uv (recommended)uvis an extremely fast Python package manager. If you have uv installed, you can run Data Formulator directly without any setup:uvx data_formulatorRunuvx data_formulator --helpto see all available options, such as custom port, sandboxing mode, and data storage location.
* Option 2: Install via pipUse pip for installation (recommend: install it in a virtual environment).pip install data_formulator#installpython -m data_formulator#runData Formulator will be automatically opened in the browser athttp://localhost:5567.
* Option 3: Run with Dockerdocker compose up --buildOpenhttp://localhost:5567in your browser. To stop, pressCtrl+Cor rundocker compose down.
* Option 4: Working as developerYou can build Data Formulator locally and develop your own version. Check out details inDEVELOPMENT.md.

## Using Data Formulator

Start with the data you already have: upload CSV, TSV, Excel, JSON, screenshots,
or text; connect to databases and data platforms; or ask the analyst to find and
load the data you need. The analyst can discover sources, clarify your request,
propose a loading plan, and let you review the data before adding it to the
workspace.

Continue the conversation in theData Thread. Ask questions in
natural language and follow the reasoning through explanations, tables, and
editable charts in one history. Refine a result directly, branch from any
earlier step to explore an alternative, or delegate the next investigation to
the analyst. When the analysis is ready, compose the results into a report to
share.

data-formulator-tutorial.mp4

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visithttps://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted theMicrosoft Open Source Code of Conduct.
For more information see theCode of Conduct FAQor contactopencode@microsoft.comwith any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must followMicrosoft's Trademark & Brand Guidelines.
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.