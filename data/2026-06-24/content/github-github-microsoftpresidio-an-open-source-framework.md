---
title: 'GitHub - microsoft/presidio: An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines. · GitHub'
url: https://github.com/microsoft/presidio
site_name: github
content_file: github-github-microsoftpresidio-an-open-source-framework
fetched_at: '2026-06-24T11:56:50.371971'
original_url: https://github.com/microsoft/presidio
author: microsoft
description: An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines. - microsoft/presidio
---

microsoft

 

/

presidio

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star9.5k

 
 
 
 
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

1,545 Commits
1,545 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
docs
docs
 
 
e2e-tests
e2e-tests
 
 
overrides
overrides
 
 
presidio-analyzer
presidio-analyzer
 
 
presidio-anonymizer
presidio-anonymizer
 
 
presidio-cli
presidio-cli
 
 
presidio-image-redactor
presidio-image-redactor
 
 
presidio-structured
presidio-structured
 
 
presidio
presidio
 
 
.env
.env
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT
CODE_OF_CONDUCT
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.MD
README.MD
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
docker-compose-image.yml
docker-compose-image.yml
 
 
docker-compose-text.yml
docker-compose-text.yml
 
 
docker-compose-transformers.yml
docker-compose-transformers.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Presidio - Data Protection and De-identification SDK

Context aware, pluggable and customizable PII de-identification service for text and images.

Component

Downloads

Coverage

Presidio Analyzer

Presidio Anonymizer

Presidio Image-Redactor

Presidio Structured

## What is Presidio

Presidio(Origin from Latin praesidium ‘protection, garrison’)helps to ensure sensitive data is properly managed and governed. It provides fastidentificationandanonymizationmodules for private entities in text such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers, financial data and more.

### 📘Full documentation

### ❓Frequently Asked Questions

### 💭Demo

### 🛫Examples

### Goals

* Allow organizations to preserve privacy in a simpler way by democratizing de-identification technologies and introducing transparency in decisions.
* Embrace extensibility and customizability to a specific business need.
* Facilitate both fully automated and semi-automated PII de-identification flows on multiple platforms.

### Main features

1. Predefinedorcustom PII recognizersleveragingNamed Entity Recognition,regular expressions,rule based logicandchecksumwith relevant context in multiple languages.
2. Options for connecting to external PII detection models.
3. Multiple usage options,from Python or PySpark workloads through Docker to Kubernetes.
4. Customizabilityin PII identification and de-identification.
5. Module forredacting PII text in images(standard image types and DICOM medical images).

⚠️Presidio can help identify sensitive/PII data in un/structured text. However, because it is using automated detection mechanisms, there is no guarantee that Presidio will find all sensitive information. Consequently, additional systems and protections should be employed.

## Installing Presidio

1. Using pip
2. Using Docker
3. From source
4. Migrating from V1 to V2

## Running Presidio

1. Getting started
2. Setting up a development environment
3. PII de-identification in text
4. PII de-identification in images
5. Usage samples and example deployments

## Support

* Before you submit an issue, please go over thedocumentation.
* For general discussions, please use theGitHub repo's discussion board.
* If you have a usage question, found a bug or have a suggestion for improvement, please file aGitHub issue.
* For other matters, please emailpresidio@microsoft.com.

## Contributing

For details on contributing to this repository, see thecontributing guide.

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visithttps://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted theMicrosoft Open Source Code of Conduct.
For more information see theCode of Conduct FAQor
contactopencode@microsoft.comwith any additional questions or comments.

## Contributors

## About

An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data. Supports NLP, pattern matching, and customizable pipelines.

microsoft.github.io/presidio

### Topics

 python

 nlp

 privacy

 transformers

 spacy

 named-entity-recognition

 data-privacy

 phi

 sensitive-data

 anonymization

 pii

 data-anonymization

 de-identification

 data-masking

 personally-identifiable-information

 data-obfuscation

 guardrails

 pii-detection

 data-redaction

 image-redactor

### Resources

 Readme

 

### License

 MIT license
 

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

9.5k

 stars
 

### Watchers

90

 watching
 

### Forks

1.2k

 forks
 

 Report repository

 

## Releases47

Release 2.2.362

 Latest

 

Mar 18, 2026

 

+ 46 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.5%
* Other0.5%