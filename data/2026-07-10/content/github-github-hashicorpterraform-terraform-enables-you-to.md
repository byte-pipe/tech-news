---
title: 'GitHub - hashicorp/terraform: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. · GitHub'
url: https://github.com/hashicorp/terraform
site_name: github
content_file: github-github-hashicorpterraform-terraform-enables-you-to
fetched_at: '2026-07-10T12:02:02.770327'
original_url: https://github.com/hashicorp/terraform
author: hashicorp
description: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. - hashicorp/terraform
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 hashicorp

 

/

terraform

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.7k
* Star49k

 
 
 
 
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

35,649 Commits
35,649 Commits
.changes
.changes
 
 
.github
.github
 
 
.release
.release
 
 
docs
docs
 
 
internal
internal
 
 
scripts
scripts
 
 
testing/
equivalence-tests
testing/
equivalence-tests
 
 
tools
tools
 
 
version
version
 
 
website
website
 
 
.changie.yaml
.changie.yaml
 
 
.copywrite.hcl
.copywrite.hcl
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.go-version
.go-version
 
 
.tfdev
.tfdev
 
 
BUGPROCESS.md
BUGPROCESS.md
 
 
BUILDING.md
BUILDING.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODEOWNERS
CODEOWNERS
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build.Dockerfile
build.Dockerfile
 
 
catalog-info.yaml
catalog-info.yaml
 
 
checkpoint.go
checkpoint.go
 
 
commands.go
commands.go
 
 
experiments.go
experiments.go
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
help.go
help.go
 
 
main.go
main.go
 
 
main_test.go
main_test.go
 
 
provider_source.go
provider_source.go
 
 
signal_unix.go
signal_unix.go
 
 
signal_windows.go
signal_windows.go
 
 
staticcheck.conf
staticcheck.conf
 
 
telemetry.go
telemetry.go
 
 
telemetry_test.go
telemetry_test.go
 
 
version.go
version.go
 
 
working_dir.go
working_dir.go
 
 
View all files

## Repository files navigation

# Terraform

* Website:https://developer.hashicorp.com/terraform
* Forums:HashiCorp Discuss
* Documentation:https://developer.hashicorp.com/terraform/docs
* Tutorials:HashiCorp's Learn Platform
* Certification Exam:HashiCorp Certified: Terraform Associate

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

The key features of Terraform are:

* Infrastructure as Code: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.
* Execution Plans: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.
* Resource Graph: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.
* Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.

For more information, refer to theWhat is Terraform?page on the Terraform website.

## Getting Started & Documentation

Documentation is available on theTerraform website:

* Introduction
* Documentation

If you're new to Terraform and want to get started creating infrastructure, please check out ourGetting Started guideson HashiCorp's learning platform. There are alsoadditional guidesto continue your learning.

Show off your Terraform knowledge by passing a certification exam. Visit thecertification pagefor information about exams and findstudy materialson HashiCorp's learning platform.

## Developing Terraform

This repository contains only Terraform core, which includes the command line interface and the main graph engine. Providers are implemented as plugins, and Terraform can automatically download providers that are published onthe Terraform Registry. HashiCorp develops some providers, and others are developed by other organizations. For more information, refer toPlugin development.

* To learn more about compiling Terraform and contributing suggested changes, refer tothe contributing guide.
* To learn more about how we handle bug reports, refer to thebug triage guide.
* To learn how to contribute to the Terraform documentation, refer to theWeb Unified Docs repository.

## License

Business Source License 1.1

## About

Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

developer.hashicorp.com/terraform

### Topics

 cloud

 graph

 terraform

 cloud-management

 infrastructure-as-code

### Resources

 Readme

 

### License

 View license
 

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

49k

 stars
 

### Watchers

1.3k

 watching
 

### Forks

10.7k

 forks
 

 Report repository

 

## Releases429

v1.15.8

 Latest

 

Jul 8, 2026

 

+ 428 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go99.7%
* Other0.3%