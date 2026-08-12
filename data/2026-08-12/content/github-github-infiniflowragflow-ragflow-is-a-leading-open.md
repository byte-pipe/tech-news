---
title: 'GitHub - infiniflow/ragflow: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs · GitHub'
url: https://github.com/infiniflow/ragflow
site_name: github
content_file: github-github-infiniflowragflow-ragflow-is-a-leading-open
fetched_at: '2026-08-12T11:44:14.352040'
original_url: https://github.com/infiniflow/ragflow
author: infiniflow
description: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs - infiniflow/ragflow
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 infiniflow

 

/

ragflow

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.3k
* Star87.4k

 
 
 
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

8,248 Commits
8,248 Commits
.agents
.agents
 
 
.github
.github
 
 
admin
admin
 
 
agent
agent
 
 
api
api
 
 
bin
bin
 
 
cmd
cmd
 
 
common
common
 
 
conf
conf
 
 
deepdoc
deepdoc
 
 
docker
docker
 
 
docs
docs
 
 
example
example
 
 
helm
helm
 
 
internal
internal
 
 
mcp
mcp
 
 
memory
memory
 
 
rag
rag
 
 
ragflow_deps
ragflow_deps
 
 
sdk/
python
sdk/
python
 
 
test
test
 
 
tools
tools
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.rooignore
.rooignore
 
 
.trivyignore
.trivyignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.scratch.oc9
Dockerfile.scratch.oc9
 
 
Dockerfile_base
Dockerfile_base
 
 
Dockerfile_deepdoc_oss
Dockerfile_deepdoc_oss
 
 
Dockerfile_tei
Dockerfile_tei
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_ar.md
README_ar.md
 
 
README_fr.md
README_fr.md
 
 
README_id.md
README_id.md
 
 
README_ja.md
README_ja.md
 
 
README_ko.md
README_ko.md
 
 
README_pt_br.md
README_pt_br.md
 
 
README_ru.md
README_ru.md
 
 
README_tr.md
README_tr.md
 
 
README_tzh.md
README_tzh.md
 
 
README_zh.md
README_zh.md
 
 
SECURITY.md
SECURITY.md
 
 
build.sh
build.sh
 
 
codecov.yml
codecov.yml
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
lefthook.yml
lefthook.yml
 
 
pyproject.toml
pyproject.toml
 
 
run_go_tests.sh
run_go_tests.sh
 
 
run_tests.py
run_tests.py
 
 
show_env.sh
show_env.sh
 
 
test.py
test.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

#### Cloud|Documentation|Roadmap|Discord

📕 Table of Contents

* 💡What is RAGFlow?
* 🎮Get Started
* 🔥Latest Updates
* 🌟Key Features
* 🔎System Architecture
* 🎬Self-Hosting
* 🔧Configurations
* 🔧Build a Docker Image
* 🔨Launch Service from Source for Development
* 📚Documentation
* 📜Roadmap
* 🏄Community
* 🙌Contributing

## 💡 What is RAGFlow?

RAGFlowis a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs. It offers a streamlined RAG workflow adaptable to enterprises of any scale. Powered by a convergedcontext engineand pre-built agent templates, RAGFlow enables developers to transform complex data into high-fidelity, production-ready AI systems with exceptional efficiency and precision.

## 🎮 Get Started

Try our cloud service athttps://cloud.ragflow.io.

## 🔥 Latest Updates

* 2026-06-15 Support multiple chat channels such as Feishu, Discord, Telegram, Line, etc.
* 2026-04-24 Supports DeepSeek v4.
* 2026-03-24RAGFlow Skill on OpenClaw— Provides an official skill for accessing RAGFlow datasets via OpenClaw.
* 2025-12-26 Supports 'Memory' for AI agent.
* 2025-11-19 Supports Gemini 3 Pro.
* 2025-11-12 Supports data synchronization from Confluence, S3, Notion, Discord, Google Drive.
* 2025-10-23 Supports MinerU & Docling as document parsing methods.
* 2025-10-15 Supports orchestrable ingestion pipeline.
* 2025-08-08 Supports OpenAI's latest GPT-5 series models.
* 2025-08-01 Supports agentic workflow and MCP.
* 2025-05-23 Adds a Python/JavaScript code executor component to Agent.
* 2025-03-19 Supports using a multi-modal model to make sense of images within PDF or DOCX files.

## 🎉 Stay Tuned

⭐️ Star our repository to stay up-to-date with exciting new features and improvements! Get instant notifications for new
releases! 🌟

## 🌟 Key Features

### 🍭"Quality in, quality out"

* Deep document understanding-based knowledge extraction from unstructured data with complicated
formats.
* Finds "needle in a data haystack" of literally unlimited tokens.

### 🍱Template-based chunking

* Intelligent and explainable.
* Plenty of template options to choose from.

### 🌱Grounded citations with reduced hallucinations

* Visualization of text chunking to allow human intervention.
* Quick view of the key references and traceable citations to support grounded answers.

### 🍔Compatibility with heterogeneous data sources

* Supports Word, Slides, Excel, TXT, images, scanned copies, structured data, web pages, and more.

### 🛀Automated and effortless RAG workflow

* Streamlined RAG orchestration catered to both personal and large businesses.
* Configurable LLMs as well as embedding models.
* Multiple recall paired with fused re-ranking.
* Intuitive APIs for seamless integration with business.

## 🔎 System Architecture

## 🎬 Self-Hosting

### 📝 Prerequisites

* CPU >= 4 cores
* RAM >= 16 GB
* Disk >= 50 GB
* Docker >= 24.0.0 & Docker Compose >= v2.26.1
* Python >= 3.13
* gVisor: Required only if you intend to use the code executor (sandbox) feature of RAGFlow.

Tip

If you have not installed Docker on your local machine (Windows, Mac, or Linux), seeInstall Docker Engine.

### 🚀 Start up the server

1. Ensurevm.max_map_count>= 262144:To check the value ofvm.max_map_count:sysctl vm.max_map_countResetvm.max_map_countto a value at least 262144 if it is not.#In this case, we set it to 262144:sudo sysctl -w vm.max_map_count=262144This change will be reset after a system reboot. To ensure your change remains permanent, add or update thevm.max_map_countvalue in/etc/sysctl.confaccordingly:vm.max_map_count=262144
2. Clone the repo:git clone https://github.com/infiniflow/ragflow.git
3. Start up the server using the pre-built Docker images:

Caution

All Docker images are built for x86 platforms. We don't currently offer Docker images for ARM64.
If you are on an ARM64 platform, followthis guideto build a Docker image compatible with your system.

The command below downloads thev0.26.4edition of the RAGFlow Docker image. See the following table for descriptions of different RAGFlow editions. To download a RAGFlow edition different fromv0.26.4, update theRAGFLOW_IMAGEvariable accordingly indocker/.envbefore usingdocker composeto start the server.

 
cd
 ragflow/docker

 git checkout v0.26.4
 
#
 Optional: use a stable tag (see releases: https://github.com/infiniflow/ragflow/releases)

 
#
 This step ensures the **entrypoint.sh** file in the code matches the Docker image version.

 
#
 Use CPU for DeepDoc tasks:

 docker compose -f docker-compose.yml up -d

 
#
 To use GPU to accelerate DeepDoc tasks:

 
#
 sed -i '1i DEVICE=gpu' .env

 
#
 docker compose -f docker-compose.yml up -d

Note: Prior tov0.22.0, we provided both images with embedding models and slim images without embedding models. Details as follows:

RAGFlow image tag

Image size (GB)

Has embedding models?

Stable?

v0.21.1

≈9

✔️

Stable release

v0.21.1-slim

≈2

❌

Stable release

Starting withv0.22.0, we ship only the slim edition and no longer append the-slimsuffix to the image tag.

1. Check the server status after having the server up and running:docker logs -f docker-ragflow-cpu-1The following output confirms a successful launch of the system:____ ___ ______ ______ __
 / __\/|/ ____// ____// /____ _ __
 / /_/ // /||/ / __ / /_ / // __\||/|/ /
 / _, _// ___|/ /_/ // __/ / // /_/ /||/|/ /
 /_/|_|/_/|_|\____//_/ /_/\____/|__/|__/*Running on all addresses (0.0.0.0)If you skip this confirmation step and directly log in to RAGFlow, your browser may prompt anetwork abnormalerror because, at that moment, your RAGFlow may not be fully initialized.
2. In your web browser, enter the IP address of your server and log in to RAGFlow.With the default settings, you only need to enterhttp://IP_OF_YOUR_MACHINE(sansport number) as the default
HTTP serving port80can be omitted when using the default configurations.
3. Inservice_conf.yaml.template, select the desired LLM factory inuser_default_llmand update
theAPI_KEYfield with the corresponding API key.Seellm_api_key_setupfor more information.The show is on!

## 🔧 Configurations

When it comes to system configurations, you will need to manage the following files:

* .env: Keeps the fundamental setups for the system, such asSVR_HTTP_PORT,MYSQL_PASSWORD, andMINIO_PASSWORD.
* service_conf.yaml.template: Configures the back-end services. The environment variables in this file will be automatically populated when the Docker container starts. Any environment variables set within the Docker container will be available for use, allowing you to customize service behavior based on the deployment environment.
* docker-compose.yml: The system relies ondocker-compose.ymlto start up.

The./docker/READMEfile provides a detailed description of the environment settings and service
configurations which can be used as${ENV_VARS}in theservice_conf.yaml.templatefile.

To update the default HTTP serving port (80), go todocker-compose.ymland change80:80to<YOUR_SERVING_PORT>:80.

Updates to the above configurations require a reboot of all containers to take effect:

docker compose -f docker-compose.yml up -d

### Switch doc engine from Elasticsearch to Infinity

RAGFlow uses Elasticsearch by default for storing full text and vectors. To switch toInfinity, follow these steps:

1. Stop all running containers:docker compose -f docker/docker-compose.yml down -v

Warning

-vwill delete the docker container volumes, and the existing data will be cleared.

1. SetDOC_ENGINEindocker/.envtoinfinity.
2. Start the containers:docker compose -f docker/docker-compose.yml up -d

Warning

Switching to Infinity on a Linux/arm64 machine is not yet officially supported.

## 🔧 Build a Docker Image

This image is approximately 2 GB in size and relies on external LLM and embedding services.

git clone https://github.com/infiniflow/ragflow.git

cd
 ragflow/
docker build --platform linux/amd64 -f Dockerfile -t infiniflow/ragflow:nightly 
.

Or if you are behind a proxy, you can pass proxy arguments:

docker build --platform linux/amd64 \
 --build-arg http_proxy=http://YOUR_PROXY:PORT \
 --build-arg https_proxy=http://YOUR_PROXY:PORT \
 -f Dockerfile -t infiniflow/ragflow:nightly 
.

## 🔨 Launch Service from Source for Development

Important

After cloning the repository for the first time, rungit config --local --unset core.hooksPath,uv tool install lefthookandlefthook installonce from the repo root to enable local Git hooks.

1. Installuv, or skip this step if it is already installed:pipx install uv
2. Clone the source code and install Python dependencies:git clone https://github.com/infiniflow/ragflow.gitcdragflow/
uv sync --python 3.13#install RAGFlow dependent python modulesuv run python3 ragflow_deps/download_deps.py
git config --local --unset core.hooksPath
uv tool install lefthook
lefthook install
3. Launch the dependent services (MinIO, Elasticsearch, Redis, and MySQL) using Docker Compose:docker compose -f docker/docker-compose-base.yml up -dAdd the following line to/etc/hoststo resolve all hosts specified indocker/.envto127.0.0.1:127.0.0.1 es01 infinity mysql minio redis sandbox-executor-manager
4. If you cannot access HuggingFace, set theHF_ENDPOINTenvironment variable to use a mirror site:exportHF_ENDPOINT=https://hf-mirror.com
5. If your operating system does not have jemalloc, please install it as follows:#Ubuntusudo apt-get install libjemalloc-dev#CentOSsudo yum install jemalloc#OpenSUSEsudo zypper install jemalloc#macOSbrew install jemalloc
6. Launch backend service:source.venv/bin/activateexportPYTHONPATH=$(pwd)bash docker/launch_backend_service.sh
7. Install frontend dependencies:cdweb
npm install
8. Launch frontend service:npm run devThe following output confirms a successful launch of the system:
9. Stop RAGFlow front-end and back-end service after development is complete:pkill -f"ragflow_server.py|task_executor.py"

## 📚 Documentation

* Quickstart
* Configuration
* Release notes
* User guides
* Developer guides
* References
* FAQs

## 📜 Roadmap

See theRAGFlow Roadmap 2026

## 🏄 Community

* Discord
* X
* GitHub Discussions

## 🙌 Contributing

RAGFlow flourishes via open-source collaboration. In this spirit, we embrace diverse contributions from the community.
If you would like to be a part, review ourContribution Guidelinesfirst.