---
title: 'GitHub - apache/superset: Apache Superset is a Data Visualization and Data Exploration Platform · GitHub'
url: https://github.com/apache/superset
site_name: github
content_file: github-github-apachesuperset-apache-superset-is-a-data-vi
fetched_at: '2026-03-28T11:10:45.444020'
original_url: https://github.com/apache/superset
author: apache
description: Apache Superset is a Data Visualization and Data Exploration Platform - apache/superset
---

apache

 

/

superset

Public

* NotificationsYou must be signed in to change notification settings
* Fork16.9k
* Star71.2k

 
 
 
 
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

19,330 Commits
19,330 Commits
.claude
.claude
 
 
.cursor/
rules
.cursor/
rules
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
ASF
ASF
 
 
CHANGELOG
CHANGELOG
 
 
RELEASING
RELEASING
 
 
RESOURCES
RESOURCES
 
 
docker
docker
 
 
docs
docs
 
 
helm/
superset
helm/
superset
 
 
requirements
requirements
 
 
scripts
scripts
 
 
superset-core
superset-core
 
 
superset-embedded-sdk
superset-embedded-sdk
 
 
superset-extensions-cli
superset-extensions-cli
 
 
superset-frontend
superset-frontend
 
 
superset-websocket
superset-websocket
 
 
superset
superset
 
 
tests
tests
 
 
.asf.yaml
.asf.yaml
 
 
.codecov.yml
.codecov.yml
 
 
.coveragerc
.coveragerc
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.envrc.example
.envrc.example
 
 
.flaskenv
.flaskenv
 
 
.fossa.yml
.fossa.yml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.markdownlint.json
.markdownlint.json
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.pylintrc
.pylintrc
 
 
.rat-excludes
.rat-excludes
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GEMINI.md
GEMINI.md
 
 
GPT.md
GPT.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE.txt
LICENSE.txt
 
 
MANIFEST.in
MANIFEST.in
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
UPDATING.md
UPDATING.md
 
 
docker-compose-image-tag.yml
docker-compose-image-tag.yml
 
 
docker-compose-light.yml
docker-compose-light.yml
 
 
docker-compose-non-dev.yml
docker-compose-non-dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
dockerize.Dockerfile
dockerize.Dockerfile
 
 
lintconf.yaml
lintconf.yaml
 
 
pyproject.toml
pyproject.toml
 
 
pytest.ini
pytest.ini
 
 
setup.py
setup.py
 
 
superset_text.yml
superset_text.yml
 
 
View all files

## Repository files navigation

# Superset

A modern, enterprise-ready business intelligence web application.

### Documentation

* User Guide— For analysts and business users. Explore data, build charts, create dashboards, and connect databases.
* Administrator Guide— Install, configure, and operate Superset. Covers security, scaling, and database drivers.
* Developer Guide— Contribute to Superset or build on its REST API and extension framework.

Why Superset?|Supported Databases|Release Notes|Get Involved|Resources|Organizations Using Superset

## Why Superset?

Superset is a modern data exploration and data visualization platform. Superset can replace or augment proprietary business intelligence tools for many teams. Superset integrates well with a variety of data sources.

Superset provides:

* Ano-code interfacefor building charts quickly
* A powerful, web-basedSQL Editorfor advanced querying
* Alightweight semantic layerfor quickly defining custom dimensions and metrics
* Out of the box support fornearly any SQLdatabase or data engine
* A wide array ofbeautiful visualizationsto showcase your data, ranging from simple bar charts to geospatial visualizations
* Lightweight, configurablecaching layerto help ease database load
* Highly extensiblesecurity roles and authenticationoptions
* AnAPIfor programmatic customization
* Acloud-native architecturedesigned from the ground up for scale

## Screenshots & Gifs

Video Overview

superset-video-1080p.webm

Large Gallery of Visualizations

Craft Beautiful, Dynamic Dashboards

No-Code Chart Builder

Powerful SQL Editor

## Supported Databases

Superset can query data from any SQL-speaking datastore or data engine (Presto, Trino, Athena,and more) that has a Python DB-API driver and a SQLAlchemy dialect.

Here are some of the major database solutions that are supported:

  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 
  
 

A more comprehensive list of supported databasesalong with the configuration instructions can be foundhere.

Want to add support for your datastore or data engine? Read morehereabout the technical requirements.

## Installation and Configuration

Try out Superset'squickstartguide or learn aboutthe options for production deployments.

## Get Involved

* Ask and answer questions onStackOverflowusing theapache-supersettag
* Join our community's Slackand please read ourSlack Community Guidelines
* Join our dev@superset.apache.org Mailing list. To join, simply send an email todev-subscribe@superset.apache.org
* If you want to help troubleshoot GitHub Issues involving the numerous database drivers that Superset supports, please consider adding your name and the databases you have access to on theSuperset Database Familiarity Rolodex
* Join Superset's Town Hall andOperational Modelrecurring meetings. Meeting info is available on theSuperset Community Calendar

## Contributor Guide

Interested in contributing? Check out ourDeveloper Guideto find resources around contributing along with a detailed guide on
how to set up a development environment.

## Resources

* Superset "In the Wild"- see who's using Superset, andadd your organizationto the list!
* Feature Flags- the status of Superset's Feature Flags.
* Standard Roles- How RBAC permissions map to roles.
* Superset Wiki- Tons of additional community resources: best practices, community content and other information.
* Superset SIPs- The status of Superset's SIPs (Superset Improvement Proposals) for both consensus and implementation status.

Understanding the Superset Points of View

* The Case for Dataset-Centric Visualization
* Understanding the Superset Semantic Layer
* Getting Started with SupersetSuperset in 2 Minutes using Docker ComposeInstalling Database DriversBuilding New Database ConnectorsCreate Your First DashboardComprehensive Tutorial for Contributing Code to Apache Superset
* Superset in 2 Minutes using Docker Compose
* Installing Database Drivers
* Building New Database Connectors
* Create Your First Dashboard
* Comprehensive Tutorial for Contributing Code to Apache Superset
* Resources to master Superset by Preset
* Deploying SupersetOfficial Docker imageHelm Chart
* Official Docker image
* Helm Chart
* Recordings of PastSuperset Community EventsMixed Time Series ChartsHow the Bing Team Customized Superset for the Internal Self-Serve Data & Analytics PlatformLive Demo: Visualizing MongoDB and Pinot Data using TrinoIntroduction to the Superset APIBuilding a Database Connector for Superset
* Mixed Time Series Charts
* How the Bing Team Customized Superset for the Internal Self-Serve Data & Analytics Platform
* Live Demo: Visualizing MongoDB and Pinot Data using Trino
* Introduction to the Superset API
* Building a Database Connector for Superset
* VisualizationsCreating Viz PluginsManaging and Deploying Custom Viz PluginsWhy Apache Superset is Betting on Apache ECharts
* Creating Viz Plugins
* Managing and Deploying Custom Viz Plugins
* Why Apache Superset is Betting on Apache ECharts
* Superset API

## Repo Activity

## About

Apache Superset is a Data Visualization and Data Exploration Platform

superset.apache.org/

### Topics

 react

 python

 flask

 data-science

 bi

 analytics

 superset

 apache

 data-visualization

 data-engineering

 business-intelligence

 data-viz

 data-analytics

 data-analysis

 sql-editor

 asf

 business-analytics

 apache-superset

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

71.2k

 stars
 

### Watchers

1.5k

 watching
 

### Forks

16.9k

 forks
 

 Report repository

 

## Releases244

6.0.0

 Latest

 

Dec 18, 2025

 

+ 243 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript50.7%
* Python38.4%
* Jupyter Notebook6.4%
* HTML3.6%
* JavaScript0.6%
* Shell0.3%