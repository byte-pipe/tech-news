---
title: 'GitHub - elastic/elasticsearch: Free and Open Source, Distributed, RESTful Search Engine · GitHub'
url: https://github.com/elastic/elasticsearch
site_name: github
content_file: github-github-elasticelasticsearch-free-and-open-source-d
fetched_at: '2026-07-03T11:49:33.043341'
original_url: https://github.com/elastic/elasticsearch
author: elastic
description: Free and Open Source, Distributed, RESTful Search Engine - elastic/elasticsearch
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 elastic

 

/

elasticsearch

Public

* NotificationsYou must be signed in to change notification settings
* Fork25.9k
* Star77.2k

 
 
 
 
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

102,317 Commits
102,317 Commits
.buildkite
.buildkite
 
 
.ci
.ci
 
 
.github
.github
 
 
.idea
.idea
 
 
benchmarks
benchmarks
 
 
build-conventions
build-conventions
 
 
build-tools-internal
build-tools-internal
 
 
build-tools
build-tools
 
 
client
client
 
 
dev-tools
dev-tools
 
 
distribution
distribution
 
 
docs
docs
 
 
gradle
gradle
 
 
libs
libs
 
 
licenses
licenses
 
 
modules
modules
 
 
plugins
plugins
 
 
qa
qa
 
 
rest-api-spec
rest-api-spec
 
 
server
server
 
 
test
test
 
 
x-pack
x-pack
 
 
.backportrc.json
.backportrc.json
 
 
.dir-locals.el
.dir-locals.el
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
BUILDING.md
BUILDING.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.txt
LICENSE.txt
 
 
NOTICE.txt
NOTICE.txt
 
 
README.asciidoc
README.asciidoc
 
 
REST_API_COMPATIBILITY.md
REST_API_COMPATIBILITY.md
 
 
TESTING.asciidoc
TESTING.asciidoc
 
 
TRACING.md
TRACING.md
 
 
Vagrantfile
Vagrantfile
 
 
branches.json
branches.json
 
 
build.gradle
build.gradle
 
 
buildkite_pr_stats_esql.ndjson
buildkite_pr_stats_esql.ndjson
 
 
catalog-info.yaml
catalog-info.yaml
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
muted-tests.yml
muted-tests.yml
 
 
renovate.json
renovate.json
 
 
settings.gradle
settings.gradle
 
 
updatecli-compose.yaml
updatecli-compose.yaml
 
 
View all files

## Repository files navigation

# Elasticsearch

Elasticsearch is a distributed search and analytics engine, scalable data store and vector database optimized for speed and relevance on production-scale workloads. Elasticsearch is the foundation of Elastic’s open Stack platform. Search in near real-time over massive datasets, perform vector searches, integrate with generative AI applications, and much more.

Use cases enabled by Elasticsearch include:

* Retrieval Augmented Generation (RAG)
* Vector search
* Full-text search
* Logs
* Metrics
* Application performance monitoring (APM)
* Security logs

... and more!

To learn more about Elasticsearch’s features and capabilities, see ourproduct page.

To access information onmachine learning innovationsand the latestLucene contributions from Elastic, more information can be found inSearch Labs.

## Get started

The simplest way to set up Elasticsearch is to create a managed deployment withElasticsearch Service on Elastic
Cloud.

If you prefer to install and manage Elasticsearch yourself, you can download
the latest version fromelastic.co/downloads/elasticsearch.

### Run Elasticsearch locally

Warning

DO NOT USE THESE INSTRUCTIONS FOR PRODUCTION DEPLOYMENTS.

This setup is intended for local development and testing only.

Quickly set up Elasticsearch and Kibana in Docker for local development or testing, using thestart-localscript.

ℹ️ For more detailed information about thestart-localsetup, refer to theREADME on GitHub.

#### Prerequisites

* If you don’t have Docker installed,download and install Docker Desktopfor your operating system.
* If you’re using Microsoft Windows, then installWindows Subsystem for Linux (WSL).

#### Trial license

This setup comes with a one-month trial license that includes all Elastic features.

After the trial period, the license reverts toFree and open - Basic.
Refer toElastic subscriptionsfor more information.

#### Runstart-local

To set up Elasticsearch and Kibana locally, run thestart-localscript:

curl -fsSL https://elastic.co/start-local 
|
 sh

This script creates anelastic-start-localfolder containing configuration files and starts both Elasticsearch and Kibana using Docker.

After running the script, you can access Elastic services at the following endpoints:

* Elasticsearch:http://localhost:9200
* Kibana:http://localhost:5601

The script generates a random password for theelasticuser, which is displayed at the end of the installation and stored in the.envfile.

Caution

This setup is for local testing only. HTTPS is disabled, and Basic authentication is used for Elasticsearch. For security, Elasticsearch and Kibana are accessible only throughlocalhost.

#### API access

An API key for Elasticsearch is generated and stored in the.envfile asES_LOCAL_API_KEY.
Use this key to connect to Elasticsearch with aprogramming language clientor theREST API.

From theelastic-start-localfolder, check the connection to Elasticsearch usingcurl:

source
 .env
curl 
$ES_LOCAL_URL
 -H 
"
Authorization: ApiKey 
${ES_LOCAL_API_KEY}
"

To use the password for theelasticuser, set and export theES_LOCAL_PASSWORDenvironment variable. For example:

source
 .env

export
 ES_LOCAL_PASSWORD

### Send requests to Elasticsearch

You send data and other requests to Elasticsearch through REST APIs.
You can interact with Elasticsearch using any client that sends HTTP requests,
such as theElasticsearch
language clientsandcurl.

#### Using curl

Here’s an example curl command to create a new Elasticsearch index, using basic auth:

curl -u elastic:
$ES_LOCAL_PASSWORD
 \
 -X PUT \
 http://localhost:9200/my-new-index \
 -H 
'
Content-Type: application/json
'

#### Using a language client

To connect to your local dev Elasticsearch cluster with a language client, you can use basic authentication with theelasticusername and the password stored in theES_LOCAL_PASSWORDenvironment variable.

You’ll use the following connection details:

* Elasticsearch endpoint:http://localhost:9200
* Username:elastic
* Password:$ES_LOCAL_PASSWORD(Value you set in the environment variable)

For example, to connect with the Pythonelasticsearchclient:

import
 
os

from
 
elasticsearch
 
import
 
Elasticsearch

username
 
=
 
'elastic'

password
 
=
 
os
.
getenv
(
'ES_LOCAL_PASSWORD'
) 
# Value you set in the environment variable

client
 
=
 
Elasticsearch
(
 
"http://localhost:9200"
,
 
basic_auth
=
(
username
, 
password
)
)

print
(
client
.
info
())

#### Using the Dev Tools Console

Kibana’s developer console provides an easy way to experiment and test requests.
To access the console, open Kibana, then go toManagement>Dev Tools.

Add data

You index data into Elasticsearch by sending JSON objects (documents) through the REST APIs.
Whether you have structured or unstructured text, numerical data, or geospatial data,
Elasticsearch efficiently stores and indexes it in a way that supports fast searches.

For timestamped data such as logs and metrics, you typically add documents to a
data stream made up of multiple auto-generated backing indices.

To add a single document to an index, submit an HTTP post request that targets the index.

POST /customer/_doc/1
{
 "firstname": "Jennifer",
 "lastname": "Walters"
}

This request automatically creates thecustomerindex if it doesn’t exist,
adds a new document that has an ID of 1, and
stores and indexes thefirstnameandlastnamefields.

The new document is available immediately from any node in the cluster.
You can retrieve it with a GET request that specifies its document ID:

GET /customer/_doc/1

To add multiple documents in one request, use the_bulkAPI.
Bulk data must be newline-delimited JSON (NDJSON).
Each line must end in a newline character (\n), including the last line.

PUT customer/_bulk
{ "create": { } }
{ "firstname": "Monica","lastname":"Rambeau"}
{ "create": { } }
{ "firstname": "Carol","lastname":"Danvers"}
{ "create": { } }
{ "firstname": "Wanda","lastname":"Maximoff"}
{ "create": { } }
{ "firstname": "Jennifer","lastname":"Takeda"}

Search

Indexed documents are available for search in near real-time.
The following search matches all customers with a first name ofJenniferin thecustomerindex.

GET customer/_search
{
 "query" : {
 "match" : { "firstname": "Jennifer" }
 }
}

Explore

You can use Discover in Kibana to interactively search and filter your data.
From there, you can start creating visualizations and building and sharing dashboards.

To get started, create adata viewthat connects to one or more Elasticsearch indices,
data streams, or index aliases.

1. Go toManagement > Stack Management > Kibana > Data Views.
2. SelectCreate data view.
3. Enter a name for the data view and a pattern that matches one or more indices,
such ascustomer.
4. SelectSave data view to Kibana.

To start exploring, go toAnalytics > Discover.

## Upgrade

To upgrade from an earlier version of Elasticsearch, see theElasticsearch upgrade
documentation.

## Build from source

Elasticsearch usesGradlefor its build system.

To build a distribution for your local OS and print its output location upon
completion, run:

./gradlew localDistro

To build a distribution for another platform, run the related command:

./gradlew :distribution:archives:linux-tar:assemble
./gradlew :distribution:archives:darwin-tar:assemble
./gradlew :distribution:archives:windows-zip:assemble

Distributions are output todistribution/archives.

To run the test suite, seeTESTING.

## Documentation

For the complete Elasticsearch documentation visitelastic.co.

For information about our documentation processes, see thedocs README.

## Examples and guides

Theelasticsearch-labsrepo contains executable Python notebooks, sample apps, and resources to test out Elasticsearch for vector search, hybrid search and generative AI use cases.

## Contribute

For contribution guidelines, seeCONTRIBUTING.

## Questions? Problems? Suggestions?

* To report a bug or request a feature, create aGitHub Issue. Please
ensure someone else hasn’t created an issue for the same topic.
* Need help using Elasticsearch? Reach out on theElastic ForumorSlack. A
fellow community member or Elastic engineer will be happy to help you out.

## About

Free and Open Source, Distributed, RESTful Search Engine

www.elastic.co/products/elasticsearch

### Topics

 java

 search-engine

 elasticsearch

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

77.2k

 stars
 

### Watchers

2.6k

 watching
 

### Forks

25.9k

 forks
 

 Report repository

 

## Releases253

Elasticsearch 9.4.3

 Latest

 

Jun 30, 2026

 

+ 252 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Java99.2%
* Groovy0.3%
* StringTemplate0.1%
* C++0.1%
* TypeScript0.1%
* Rust0.1%
* Other0.1%