---
title: 'GitHub - open-metadata/OpenMetadata: OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. · GitHub'
url: https://github.com/open-metadata/OpenMetadata
site_name: github
content_file: github-github-open-metadataopenmetadata-openmetadata-is-a
fetched_at: '2026-04-22T20:04:28.171633'
original_url: https://github.com/open-metadata/OpenMetadata
author: open-metadata
description: OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. - open-metadata/OpenMetadata
---

open-metadata

 

/

OpenMetadata

Public

* NotificationsYou must be signed in to change notification settings
* Fork2k
* Star12.1k

 
 
 
 
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

16,179 Commits
16,179 Commits
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
bin
bin
 
 
bootstrap
bootstrap
 
 
common
common
 
 
conf
conf
 
 
docker
docker
 
 
docs
docs
 
 
examples/
python-sdk/
data-quality
examples/
python-sdk/
data-quality
 
 
ingestion
ingestion
 
 
openmetadata-airflow-apis
openmetadata-airflow-apis
 
 
openmetadata-clients
openmetadata-clients
 
 
openmetadata-dist
openmetadata-dist
 
 
openmetadata-integration-tests
openmetadata-integration-tests
 
 
openmetadata-k8s-operator
openmetadata-k8s-operator
 
 
openmetadata-mcp
openmetadata-mcp
 
 
openmetadata-sdk
openmetadata-sdk
 
 
openmetadata-service
openmetadata-service
 
 
openmetadata-shaded-deps
openmetadata-shaded-deps
 
 
openmetadata-spec
openmetadata-spec
 
 
openmetadata-ui-core-components
openmetadata-ui-core-components
 
 
openmetadata-ui
openmetadata-ui
 
 
perf-tests
perf-tests
 
 
scripts
scripts
 
 
skills
skills
 
 
.dockerignore
.dockerignore
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.nojekyll
.nojekyll
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.pylintrc
.pylintrc
 
 
.snyk
.snyk
 
 
APPLICATION.md
APPLICATION.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DEVELOPER.md
DEVELOPER.md
 
 
INCIDENT_RESPONSE.md
INCIDENT_RESPONSE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
THREAT_MODEL.md
THREAT_MODEL.md
 
 
generate_ts.sh
generate_ts.sh
 
 
package.json
package.json
 
 
pom.xml
pom.xml
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

Empower your Data Journey with OpenMetadata

## What is OpenMetadata?

OpenMetadatais a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column-level lineage, and seamless team collaboration. It is one of the fastest-growing open-source projects with a vibrant community and adoption by a diverse set of companies in a variety of industry verticals. Based on Open Metadata Standards and APIs, supporting connectors to a wide range of data services, OpenMetadata enables end-to-end metadata management, giving you the freedom to unlock the value of your data assets.

Contents:

* Features
* Try our Sandbox
* Install & Run
* Roadmap
* Documentation and Support
* Contributors

OpenMetadata Consists of Four Main Components:

* Metadata Schemas: These are the core definitions and vocabulary for metadata based on common abstractions and types. They also allow for custom extensions and properties to suit different use cases and domains.
* Metadata Store: This is the central repository for storing and managing the metadata graph, which connects data assets, users, and tool-generated metadata in a unified way.
* Metadata APIs: These are the interfaces for producing and consuming metadata, built on top of the metadata schemas. They enable seamless integration of user interfaces and tools, systems, and services with the metadata store.
* Ingestion Framework: This is a pluggable framework for ingesting metadata from various sources and tools to the metadata store. It supports about 84+ connectors for data warehouses, databases, dashboard services, messaging services, pipeline services, and more.

## Key Features of OpenMetadata

Data Discovery: Find and explore all your data assets in a single place using various strategies, such as keyword search, data associations, and advanced queries. You can search across tables, topics, dashboards, pipelines, and services.

Data Collaboration: Communicate, converse, and cooperate with other users and teams on data assets. You can get event notifications, send alerts, add announcements, create tasks, and use conversation threads.

Data Quality and Profiler: Measure and monitor the quality withno-codeto build trust in your data. You can define and run data quality tests, group them into test suites, and view the results in an interactive dashboard. With powerful collaboration, make data quality a shared responsibility in your organization.

Data Governance: Enforce data policies and standards across your organization. You can define data domains and data products, assign owners and stakeholders, and classify data assets using tags and terms. Use powerful automation features to auto-classify your data.

Data Insights and KPIs: Use reports and platform analytics to understand how your organization's data is doing. Data Insights provides a single-pane view of all the key metrics to reflect the state of your data best. Define the Key Performance Indicators (KPIs) and set goals within OpenMetadata to work towards better documentation, ownership, and tiering. Alerts can be set against the KPIs to be received on a specified schedule.

Data Lineage: Track and visualize the origin and transformation of your data assets end-to-end. You can view column-level lineage, filter queries, and edit lineage manually using a no-code editor.

Data Documentation: Document your data assets and metadata entities using rich text, images, and links. You can also add comments and annotations and generate data dictionaries and data catalogs.

Data Observability: Monitor the health and performance of your data assets and pipelines. You can view metrics such as data freshness, data volume, data quality, and data latency. You can also set up alerts and notifications for any anomalies or failures.

Data Security: Secure your data and metadata using various authentication and authorization mechanisms. You can integrate with different identity providers for single sign-on and define roles and policies for access control.

Webhooks: Integrate with external applications and services using webhooks. You can register URLs to receive metadata event notifications and integrate with Slack, Microsoft Teams, and Google Chat.

Connectors: Ingest metadata from various sources and tools using connectors. OpenMetadata supports about 84+ connectors for data warehouses, databases, dashboard services, messaging services, pipeline services, and more.

## Try our Sandbox

Take a look and play with sample data athttp://sandbox.open-metadata.org

## Install and Run OpenMetadata

Get up and running in a few minutes. See the OpenMetadata documentation forinstallation instructions.

## Documentation and Support

We're here to help and make OpenMetadata even better! Check outOpenMetadata documentationfor a complete description of OpenMetadata's features. Join ourSlack Communityto get in touch with us if you want to chat, need help, or discuss new feature requirements.

## Contributors

We ❤️ all contributions, big and small! Check out ourCONTRIBUTINGguide to get started, and let us know how we can help.

Don't want to miss anything? Give the project a ⭐ 🚀

A HUGE THANK YOU to all our supporters!

## Stargazers

## License

OpenMetadata is released underApache License, Version 2.0

## About

OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

open-metadata.org

### Topics

 metadata

 data-validation

 mcp

 data-catalog

 data-discovery

 hacktoberfest

 data-quality-checks

 data-quality

 data-profiling

 metadata-management

 dataengineering

 dataquality

 data-governance

 data-lineage

 data-contracts

 data-observability

 datadiscovery

 data-collaboration

 mcp-server

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

12.1k

 stars
 

### Watchers

54

 watching
 

### Forks

2k

 forks
 

 Report repository

 

## Releases205

1.12.6-release

 Latest

 

Apr 22, 2026

 

+ 204 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript43.3%
* Java34.2%
* Python20.5%
* Less1.2%
* Shell0.4%
* CSS0.2%
* Other0.2%