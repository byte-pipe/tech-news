---
title: 'GitHub - frappe/erpnext: Free and Open Source Enterprise Resource Planning (ERP) · GitHub'
url: https://github.com/frappe/erpnext
site_name: github
content_file: github-github-frappeerpnext-free-and-open-source-enterpri
fetched_at: '2026-05-19T12:04:00.549535'
original_url: https://github.com/frappe/erpnext
author: frappe
description: Free and Open Source Enterprise Resource Planning (ERP) - frappe/erpnext
---

frappe

 

/

erpnext

Public

* NotificationsYou must be signed in to change notification settings
* Fork11.3k
* Star34.1k

 
 
 
 
develop
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

57,959 Commits
57,959 Commits
.github
.github
 
 
banking
banking
 
 
erpnext
erpnext
 
 
frappe-semgrep-rules
frappe-semgrep-rules
 
 
semgrep
semgrep
 
 
.coderabbit.yml
.coderabbit.yml
 
 
.editorconfig
.editorconfig
 
 
.eslintrc
.eslintrc
 
 
.flake8
.flake8
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.mergify.yml
.mergify.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.releaserc
.releaserc
 
 
.semgrepignore
.semgrepignore
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TRADEMARK_POLICY.md
TRADEMARK_POLICY.md
 
 
attributions.md
attributions.md
 
 
babel_extractors.csv
babel_extractors.csv
 
 
codecov.yml
codecov.yml
 
 
commitlint.config.js
commitlint.config.js
 
 
crowdin.yml
crowdin.yml
 
 
license.txt
license.txt
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
sider.yml
sider.yml
 
 
sponsors.md
sponsors.md
 
 
transaction-deletion-import-logic-summary.md
transaction-deletion-import-logic-summary.md
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

## ERPNext

Powerful, Intuitive and Open-Source ERP

Live Demo

	-
	
Website

	-
	
Documentation

## ERPNext

100% Open-Source ERP System to help you run your business.

### Motivation

Running a business is a complex task - handling invoices, tracking stock, managing personnel, and other daily operations. In a market where software is sold separately to manage each of these tasks, ERPNext does all of the above and more, for free.

### Key Features

* Accounting: All the tools you need to manage cash flow in one place, right from recording transactions to summarizing and analyzing financial reports.
* Order Management: Track inventory levels, replenish stock, and manage sales orders, customers, suppliers, shipments, deliverables, and order fulfillment.
* Manufacturing: Simplifies the production cycle, helps track material consumption, exhibits capacity planning, handles subcontracting, and more!
* Asset Management: From purchase to disposal, IT infrastructure to equipment. Covers every branch of your organization, all in one centralized system.
* Projects: Deliver both internal and external projects on time, budget and profitability. Track tasks, timesheets, and issues by project.

More

### Under the Hood

* Frappe Framework: A full-stack web application framework written in Python and JavaScript. The framework provides a robust foundation for building web applications, including a database abstraction layer, user authentication, and a REST API.
* Frappe UI: A Vue-based UI library, to provide a modern user interface. The Frappe UI library provides a variety of components that can be used to build single-page applications on top of the Frappe Framework.

## Production Setup

### Managed Hosting

You can tryFrappe Cloud, a simple, user-friendly, and sophisticatedopen-sourceplatform to host Frappe applications reliably and securely.

It handles installation, setup, upgrades, monitoring, maintenance, and support of your Frappe deployments. It is a fully featured developer platform with an ability to manage and control multiple Frappe deployments.

### Self-Hosted

#### Docker

SeeFrappe Docker Documentationfor full documentation & FAQ on Docker setup

#### Prerequisites

* Docker
* Docker Compose v2
* git

For Docker basics and best practices refer to Docker'sdocumentation

### Try on your environment

⚠️Disposable demo only

This setup is intended for quick evaluation. Expect to throw the environment away.You will not be able to install custom apps to this setup. For production deployments, custom configurations, and detailed explanations, see the full documentation.

First clone the repo:

git clone https://github.com/frappe/frappe_docker

cd
 frappe_docker

Then run:

docker compose -f pwd.yml up -d

Wait for a couple of minutes for ERPNext site to be created or check thecreate-sitecontainer logs before opening browser on port8080. (username:Administrator, password:admin)

SeeFrappe Dockerfor ARM based docker setup

## Development Setup

### Manual Install

The Easy Way: our install script for bench will install all dependencies (e.g. MariaDB). Seehttps://github.com/frappe/benchfor more details.

New passwords will be created for the ERPNext "Administrator" user, the MariaDB root user, and the Frappe user (the script displays the passwords and saves them to ~/frappe_passwords.txt).

### Local

To setup the repository locally follow the steps mentioned below:

1. Setup bench by following theInstallation Stepsand start the serverbench start
2. In a separate terminal window, run the following commands:# Create a new site
bench new-site erpnext.localhost
3. Get the ERPNext app and install it# Get the ERPNext app
bench get-app https://github.com/frappe/erpnext

# Install the app
bench --site erpnext.localhost install-app erpnext
4. Open the URLhttp://erpnext.localhost:8000/appin your browser, you should see the app running

## Learning and Community

1. Frappe School- Learn Frappe Framework and ERPNext from the various courses by the maintainers or from the community.
2. Official documentation- Extensive documentation for ERPNext.
3. Discussion Forum- Engage with the community of ERPNext users and service providers.
4. Telegram Group- Get instant help from huge community of users.

## Contributing

1. Issue Guidelines
2. Report Security Vulnerabilities
3. Pull Request Requirements
4. Translations

## Logo and Trademark Policy

Please read ourLogo and Trademark Policy.

## About

Free and Open Source Enterprise Resource Planning (ERP)

frappe.io/erpnext

### Topics

 support

 python

 distribution

 erp

 accounting

 crm

 healthcare

 project-management

 manufacturing

 frappe

 erpnext

 procurement

 retail

 point-of-sale

 hrms

 asset-management

### Resources

 Readme

 

### License

 GPL-3.0 license
 

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

34.1k

 stars
 

### Watchers

669

 watching
 

### Forks

11.3k

 forks
 

 Report repository

 

## Releases1,737

v16.18.3

 Latest

 

May 14, 2026

 

+ 1,736 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python76.6%
* JavaScript15.5%
* TypeScript5.4%
* HTML1.9%
* Other0.6%