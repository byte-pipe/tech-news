---
title: 'GitHub - meshery/meshery: Meshery, the cloud native manager · GitHub'
url: https://github.com/meshery/meshery
site_name: github
content_file: github-github-mesherymeshery-meshery-the-cloud-native-man
fetched_at: '2026-06-14T19:34:04.840339'
original_url: https://github.com/meshery/meshery
author: meshery
description: Meshery, the cloud native manager. Contribute to meshery/meshery development by creating an account on GitHub.
---

meshery

 

/

meshery

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.4k
* Star10.4k

 
 
 
 
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

56,770 Commits
56,770 Commits
.agents
.agents
 
 
.github
.github
 
 
docs
docs
 
 
install
install
 
 
mesheryctl
mesheryctl
 
 
policies/
wasm
policies/
wasm
 
 
provider-ui
provider-ui
 
 
server
server
 
 
ui
ui
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitpod.yml
.gitpod.yml
 
 
ADOPTERS.md
ADOPTERS.md
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CNAME
CNAME
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY-INSIGHTS.yml
SECURITY-INSIGHTS.yml
 
 
SECURITY.md
SECURITY.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

##### If you like Meshery, please★this repository to show your support! 🤩

MESHERY IS A CLOUD NATIVE COMPUTING FOUNDATION PROJECT

A self-service engineering platform,Meshery, is the open source, cloud native manager that enables the design and management of all Kubernetes-based infrastructure and applications (multi-cloud). As an extensible platform, Meshery offers visual and collaborative GitOps, freeing you from the chains of YAML while managing Kubernetes multi-cluster deployments.

Try Meshery in your browser using theCloud Native Playground(teaser video)

 

# Functionality

## Infrastructure Lifecycle Management

Meshery manages the configuration, deployment, and operation of your Cloud services and Kubernetes clusters while supporting hundreds of different types of cloud native infrastructure integrations. Meshery supports380+ integrations.

Find infrastructure configuration patterns in Meshery'scatalog of curated design templatesfilled with configuration best practices.

### Multiple Kubernetes Clusters and Multiple Clouds

Meshery provides a single pane of glass to manage multiple Kubernetes clusters across any infrastructure, including various cloud providers. Meshery enables consistent configuration, operation, and observability across your entire Kubernetes landscape.

#### Dry-run your deployments

Meshery leverages Kubernetes' built-in dry-run capabilities to allow you to simulate deployments without actually applying the changes to your cluster. This enables you to:

* Validate configurations: Ensure your deployment specifications (e.g., YAML manifests, Helm charts, Meshery Designs) are syntactically correct and will be accepted by the Kubernetes API server.
* Identify potential issues: Detect errors in your configurations, such as invalid resource definitions, missing fields, or API version mismatches, before they impact your live environment.
* Preview changes: Understand the objects that Kubernetes would create or modify during a real deployment.
* Integrate with CI/CD: Incorporate dry-run as a step in your continuous integration and continuous delivery pipelines to automate pre-deployment checks and prevent faulty deployments.

By providing this dry-run functionality, Meshery helps you increase the reliability and stability of your Kubernetes deployments by catching potential problems early in the development and deployment process.

### Visually and collaboratively manage your infrastructure

Using a GitOps-centric approach, visually and collaboratively design and manage your infrastructure and microservices. Meshery intelligently infers the manner in which each resourceinterrelateswith each other. Meshery supports a broad variety of built-in relationships between components, which you can use to create your own custom relationships.

#### Context-Aware Policies For Applications

Leverage built-in relationships to enforce configuration best practices consistently from code to Kubernetes. Configure your infrastructure with confidence without needing to know or write Open Policy Agent's Rego query language.

## Workspaces: Your team's Google Drive for cloud native projects

Workspaces let you organize your work and serve as the central point of collaboration for you and your teams and a point of access control to Environments and their resources.

#### Manage your connections with Environments

Environmentsmake it easier for you to manage, share, and work with a collection of resources as a group, instead of dealing with all your Connections and Credentials on an individual basis.

#### See changes to your infra before you merge

Get snapshots of your infrastructure directly in your PRs. Preview your deployment, view changes pull request-to-pull request and get infrastructure snapshots within your PRs by connecting Meshery to your GitHub repositories.

## Platform Engineering with Meshery's Extension Points

Extend Meshery as your self-service engineering platform by taking advantage of itsvast set of extensibility features, including gRPC adapters, hot-loadable React packages and Golang plugins, subscriptions on NATS topics, and consumableandextendable API interfaces via REST and GraphQL. The great number of extension points in Meshery make it ideal as the foundation of your internal developer platform.

#### Access the Cloud Native Patterns for Kubernetes

Design and manage all of your cloud native infrastructure using the design configurator in Meshery or start from a template using the patterns from thecatalog.

Meshery offers robust capabilities for managing multiple tenants within a shared Kubernetes infrastructure. Meshery provides the tools and integrations necessary to create a secure, isolated, and manageable multi-tenant environments, allowing multiple teams or organizations with granular control over their role-based access controls.

Meshery's "multi-player" functionality refers to its collaborative features that enable multiple users to interact with and manage cloud native infrastructure simultaneously. This is primarily facilitated through Meshery extensions.

## Performance Management

Meshery offers load generation and performance characterization to help you assess and optimize the performance of your applications and infrastructure.

Create and reuse performance profiles for consistent characterization of the configuration of your infrastructure in context of how it performs.

#### Manage the performance of your infrastructure and its workloads

Baseline and track your cloud native performance from release to release.

* Use performance profiles to track the historical performance of your workloads.
* Track your application performance from version to version.
* Understand behavioral differences between cloud native network functions.
* Compare performance across infrastructure deployments.

#### Load Generation and Microservice Performance Characterization

* Load Generation:Meshery uses the Fortio load generator to drive performance tests, with a pluggable load generator interface for extensibility.
* Configurable Performance Profiles:Meshery provides a highly configurable set of load profiles with tunable facets, enabling users to generate TCP, gRPC, and HTTP load. You can customize parameters such as duration, concurrent threads, concurrent generators, and load generator type.
* Statistical Analysis:Meshery performs statistical analysis on the results of performance tests, presenting data in the form of histograms with latency buckets. Understand the distribution of response times and identify potential bottlenecks.
* Comparison of Test Results:Meshery enables you to compare the difference in request performance (latency and throughput) between independent performance tests. Save your load test configurations as Performance Profiles, making it easy to rerun tests with the same settings and track performance variations over time.
* Kubernetes Cluster and Workload Metrics:Meshery connects to one or more Prometheus servers to gather both cluster and application metrics. Meshery also integrates with Grafana, allowing you to import your existing dashboards and visualize performance data.

In an effort to produce infrastructure agnostic tooling, Meshery uses theCloud Native Performancespecification as a common format to capture and measure your infrastructure's performance against a universal cloud native performance index. Meshery participates in advancing cloud native infrastructure adoption through the standardization of APIs. Meshery enables you to measure the value provided by Docker, Kubernetes, or other cloud native infrastructure in the context of the overhead incurred.

## Get Started with Meshery

### Using `mesheryctl`

Meshery runs as a set of containers inside or outside of your Kubernetes clusters.

curl -L https://meshery.io/install | bash -

Use thequick startguide.

See all supported platforms

See thegetting startedsection to quickly deploy Meshery on any of these supported platforms:

Platform

Supported?

 
Docker

✔️

    
 
Docker - Docker App

✔️

    
 
Docker - Docker Extension

✔️

 
Kubernetes

✔️

    
 
Kubernetes - AKS

✔️

    
 
Kubernetes - Docker Desktop

✔️

    
 
Kubernetes - EKS

✔️

    
 
Kubernetes - GKE

✔️

    
 
Kubernetes - Helm

✔️

    
 
Kubernetes - kind

✔️

    
 
Kubernetes - Minikube

✔️

    
 
Kubernetes - OpenShift

✔️

    
 
Kubernetes - Rancher

✔️

 
Linux

✔️

 
Mac

✔️

    
 
Mac - Homebrew

✔️

 
Windows

✔️

    
 
Scoop

✔️

    
 
WSL2

✔️

 Raspberry Pi

In Progress

Meshery documentationoffers thorough installation guides for your platform of choice.

 

 

## Join the Meshery community

Our projects are community-built and welcome collaboration. 👍 Be sure to see theContributor Journey MapandCommunity Handbookfor a tour of resources available to you. Jump into communitySlackordiscussion forumto participate.

### Find your MeshMate

MeshMates are experienced Meshery community members, who will help you learn your way around, discover live projects, and expand your community network. Connect with a MeshMate today!

Learn more about theMeshMatesprogram.

✔️Joinany or all of the weekly meetings oncommunity calendar.✔️Watchcommunitymeeting recordings.✔️Fill-inamember formand gain access to community resources.✔️Discussin thecommunity forum.✔️Explore morein thecommunity handbook.

Not sure where to start?Grab an open issue with thehelp-wanted label.

 

## Contributing

Please do! We're a warm and welcoming community of open source contributors. Please join. All types of contributions are welcome. Be sure to read theContributor Guidesfor a tour of resources available to you and how to get started.

Naming conventions.This repository adheres to the canonical camelCase-wire identifier-naming contract shared across the Meshery ecosystem. See theidentifier-naming contributor guideinmeshery/schemasfor the full reader-friendly directory (26-row naming table with before/after and do/don't examples). Repo-specific mandates live inAGENTS.md § Identifier Naming Conventions.

 

### Stargazers

If you like Meshery, please★star this repository to show your support! 🤩

### License

This repository and site are available as open-source under the terms of theApache 2.0 License.

#### Software Bill of Materials (SBOM)

Meshery'sSoftware Bill of Materials(SBOM) is available as a build artifact.

## About

Meshery, the cloud native manager

meshery.io

### Topics

 visualization

 docker

 kubernetes

 golang

 reactjs

 cncf

 webassembly

 opa

 infrastructure-as-code

 cloud-native

 gsoc

 kubernetes-operator

 control-plane

 hacktoberfest

 gitops

 platform-engineering

 meshery

 management-plane

 internal-developer-platform

 kanvas

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

10.4k

 stars
 

### Watchers

59

 watching
 

### Forks

3.4k

 forks
 

 Report repository

 

## Releases821

Meshery v1.0.43

 Latest

 

Jun 13, 2026

 

+ 820 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript43.3%
* Go36.5%
* JavaScript16.6%
* Open Policy Agent1.3%
* Shell0.9%
* Makefile0.4%
* Other1.0%