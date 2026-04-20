---
title: 'GitHub - goharbor/harbor: An open source trusted cloud native registry project that stores, signs, and scans content. · GitHub'
url: https://github.com/goharbor/harbor
site_name: github
content_file: github-github-goharborharbor-an-open-source-trusted-cloud
fetched_at: '2026-04-08T11:23:33.678524'
original_url: https://github.com/goharbor/harbor
author: goharbor
description: An open source trusted cloud native registry project that stores, signs, and scans content. - goharbor/harbor
---

goharbor



/

harbor

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.2k
* Star28k




 
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

12,622 Commits
12,622 Commits
.github
.github
 
 
api/
v2.0
api/
v2.0
 
 
contrib
contrib
 
 
docs
docs
 
 
icons
icons
 
 
make
make
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.buildbaselog
.buildbaselog
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmessage
.gitmessage
 
 
.spectral.yaml
.spectral.yaml
 
 
ADOPTERS.md
ADOPTERS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
OWNERS.md
OWNERS.md
 
 
README.md
README.md
 
 
RELEASES.md
RELEASES.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
VERSION
VERSION
 
 
codecov.yml
codecov.yml
 
 
View all files

## Repository files navigation

# Harbor

Community Meeting

The Harbor Project holds bi-weekly community calls in two different timezones. To join the community calls or to watch previous meeting notes and recordings, please visit the
meeting schedule
.



Note: Themainbranch may be in anunstable or even broken stateduring development.
Please usereleasesinstead of themainbranch in order to get a stable set of binaries.

Harbor is an open source trusted cloud native registry project that stores, signs, and scans content. Harbor extends the open source Docker Distribution by adding the functionalities usually required by users such as security, identity and management. Having a registry closer to the build and run environment can improve the image transfer efficiency. Harbor supports replication of images between registries, and also offers advanced security features such as user management, access control and activity auditing.

Harbor is hosted by theCloud Native Computing Foundation(CNCF). If you are an organization that wants to help shape the evolution of cloud native technologies, consider joining the CNCF. For details about who is involved and how Harbor plays a role, read the CNCFannouncement.

## Features

* Cloud native registry: With support for both container images andHelmcharts, Harbor serves as registry for cloud native environments like container runtimes and orchestration platforms.
* Role based access control: Users access different repositories through 'projects' and a user can have different permission for images or Helm charts under a project.
* Policy based replication: Images and charts can be replicated (synchronized) between multiple registry instances based on policies with using filters (repository, tag and label). Harbor automatically retries a replication if it encounters any errors. This can be used to assist loadbalancing, achieve high availability, and facilitate multi-datacenter deployments in hybrid and multi-cloud scenarios.
* Vulnerability Scanning: Harbor scans images regularly for vulnerabilities and has policy checks to prevent vulnerable images from being deployed.
* LDAP/AD support: Harbor integrates with existing enterprise LDAP/AD for user authentication and management, and supports importing LDAP groups into Harbor that can then be given permissions to specific projects.
* OIDC support: Harbor leverages OpenID Connect (OIDC) to verify the identity of users authenticated by an external authorization server or identity provider. Single sign-on can be enabled to log into the Harbor portal.
* Image deletion & garbage collection: System administrators can run garbage collection jobs so that images (dangling manifests and unreferenced blobs) can be deleted and their space can be freed up periodically.
* Notary: Support signing container images using Docker Content Trust (leveraging Notary) for guaranteeing authenticity and provenance. In addition, policies that prevent unsigned images from being deployed can also be activated.
* Graphical user portal: User can easily browse, search repositories and manage projects.
* Auditing: All the operations to the repositories are tracked through logs.
* RESTful API: RESTful APIs are provided to facilitate administrative operations, and are easy to use for integration with external systems. An embedded Swagger UI is available for exploring and testing the API.
* Easy deployment: Harbor can be deployed via Docker compose as well Helm Chart, and a Harbor Operator was added recently as well.

## Architecture

For learning the architecture design of Harbor, check the documentArchitecture Overview of Harbor.

## API

* Harbor RESTful API: The APIs for most administrative operations of Harbor and can be used to perform integrations with Harbor programmatically.Part 1:New or changed APIs
* Part 1:New or changed APIs

## Install & Run

System requirements:

On a Linux host:docker 20.10.10-ce+ and docker-compose 1.18.0+ .

Download binaries ofHarbor releaseand followInstallation & Configuration Guideto install Harbor.

If you want to deploy Harbor on Kubernetes, please use theHarbor chart.

Refer to thedocumentationfor more details on how to use Harbor.

### Verifying Release Signatures

Starting with v2.15.0, Harbor release artifacts are cryptographically signed using Cosign to ensure authenticity and integrity.

Download the installers and signature bundles from the Harbor releases page.

#### Quick Verification

#
 Install Cosign (v2.0+)

brew install sigstore/tap/cosign

#
 Verify signature

cosign verify-blob \
 --bundle harbor-offline-installer-v2.15.0.tgz.sigstore.json \
 --certificate-oidc-issuer https://token.actions.githubusercontent.com \
 --certificate-identity-regexp
'
^https://github.com/goharbor/harbor/.github/workflows/publish_release.yml@refs/tags/v.*$
'
 \
 harbor-offline-installer-v2.15.0.tgz

* Expected output:Verified OK
* Full verification guide:docs/signature-verification.md

## OCI Distribution Conformance Tests

Check the OCI distribution conformance testsreportof Harbor.

## Compatibility

Thecompatibility listdocument provides compatibility information for the Harbor components.

* Replication adapters
* OIDC adapters
* Scanner adapters

## Community

* Twitter:@project_harbor
* User Group:Join Harbor user email group:harbor-users@lists.cncf.ioto get update of Harbor's news, features, releases, or to provide suggestion and feedback.
* Developer Group:Join Harbor developer group:harbor-dev@lists.cncf.iofor discussion on Harbor development and contribution.
* Slack:Join Harbor's community for discussion and ask questions:Cloud Native Computing Foundation, channel:#harborand#harbor-dev

## Demos

* Live Demo- A demo environment with the latest Harbor stable build installed. For additional information please refer tothis page.
* Video Demos- Demos for Harbor features and continuously updated.

## Partners and Users

For a list of users, please refer toADOPTERS.md.

## Security

### Security Audit

A third party security audit was performed by Cure53 in October 2019. You can see the full reporthere.

### Reporting security vulnerabilities

If you've found a security related issue, a vulnerability, or a potential vulnerability in Harbor please let theHarbor Security Teamknow with the details of the vulnerability. We'll send a confirmation
email to acknowledge your report, and we'll send an additional email when we've identified the issue
positively or negatively.

For further details please see our completesecurity release process.

## License

Harbor is available under theApache 2 license.

This project uses open source components which have additional licensing terms. The official docker images and licensing terms for these open source components can be found at the following locations:

* Photon OS 1.0:docker image,license

## Fossa Status

## About

An open source trusted cloud native registry project that stores, signs, and scans content.

goharbor.io

### Topics

 docker

 kubernetes

 registry

 containers

 helm

 container

 cncf

 container-management

 cloud-native

 hacktoberfest

 container-registry

 cncf-project

### Resources

 Readme



### License

 Apache-2.0 license


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

28k

 stars


### Watchers

518

 watching


### Forks

5.2k

 forks


 Report repository



## Releases351

v2.15.0

 Latest



Mar 20, 2026



+ 350 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Go52.9%
* TypeScript21.6%
* HTML8.0%
* Python5.5%
* RobotFramework5.1%
* Jinja3.9%
* Other3.0%
