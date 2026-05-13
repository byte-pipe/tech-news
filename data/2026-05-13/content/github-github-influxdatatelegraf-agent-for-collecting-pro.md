---
title: 'GitHub - influxdata/telegraf: Agent for collecting, processing, aggregating, and writing metrics, logs, and other arbitrary data. · GitHub'
url: https://github.com/influxdata/telegraf
site_name: github
content_file: github-github-influxdatatelegraf-agent-for-collecting-pro
fetched_at: '2026-05-13T11:46:09.388893'
original_url: https://github.com/influxdata/telegraf
author: influxdata
description: Agent for collecting, processing, aggregating, and writing metrics, logs, and other arbitrary data. - influxdata/telegraf
---

influxdata

 

/

telegraf

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.8k
* Star16.9k

 
 
 
 
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

10,951 Commits
10,951 Commits
.circleci
.circleci
 
 
.github
.github
 
 
agent
agent
 
 
assets
assets
 
 
cmd/
telegraf
cmd/
telegraf
 
 
config
config
 
 
docs
docs
 
 
etc/
logrotate.d
etc/
logrotate.d
 
 
filter
filter
 
 
internal
internal
 
 
logger
logger
 
 
metric
metric
 
 
migrations
migrations
 
 
models
models
 
 
persister
persister
 
 
plugins
plugins
 
 
scripts
scripts
 
 
selfstat
selfstat
 
 
testutil
testutil
 
 
tools
tools
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.markdownlint.jsonc
.markdownlint.jsonc
 
 
.markdownlintignore
.markdownlintignore
 
 
CHANGELOG-1.13.md
CHANGELOG-1.13.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
EXTERNAL_PLUGINS.md
EXTERNAL_PLUGINS.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
accumulator.go
accumulator.go
 
 
aggregator.go
aggregator.go
 
 
build_version.txt
build_version.txt
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
info.plist
info.plist
 
 
input.go
input.go
 
 
logger.go
logger.go
 
 
metric.go
metric.go
 
 
output.go
output.go
 
 
parser.go
parser.go
 
 
plugin.go
plugin.go
 
 
processor.go
processor.go
 
 
secretstore.go
secretstore.go
 
 
serializer.go
serializer.go
 
 
View all files

## Repository files navigation

# Telegraf

Telegraf is an agent for collecting, processing, aggregating, and writing
metrics, logs, and other arbitrary data.

* Offers a comprehensive suite of over 300 plugins, covering a wide range of
functionalities including system monitoring, cloud services, and message
passing
* Enables the integration of user-defined code to collect, transform, and
transmit data efficiently
* Compiles into a standalone static binary without any external dependencies,
ensuring a streamlined deployment process
* Utilizes TOML for configuration, providing a user-friendly and unambiguous
setup experience
* Developed with contributions from a diverse community of over 1,200
contributors

Users can choose plugins from a wide range of topics, including but not limited
to:

* Devices:OPC UA,Modbus
* Logs:File,Tail,Directory Monitor
* Messaging:AMQP,Kafka,MQTT
* Monitoring:OpenTelemetry,Prometheus
* Networking:Cisco TelemetryMDT,gNMI
* System monitoring:CPU,Memory,Disk,Network,SMART,Docker,Nvidia SMI, etc.
* Universal:Exec,HTTP,HTTP Listener,SNMP,SQL
* Windows:Event Log,Management Instrumentation,Performance Counters

## 🔨 Installation

For binary builds, Docker images, RPM & DEB packages, and other builds of
Telegraf, please see theinstall guide.

See thereleases documentationfor details on versioning
and when releases are made.

## 💻 Usage

Users define a TOML configuration with the plugins and settings they wish to
use, then pass that configuration to Telegraf. The Telegraf agent then
collects data from inputs at each interval and sends data to outputs at each
flush interval.

For a basic walkthrough seequick start.

## 📖 Documentation

For a full list of documentation including tutorials, reference and other
material, start with the/docs directory.

Additionally, each plugin has its own README that includes details about how to
configure, use, and sometimes debug or troubleshoot. Look under the/plugins directoryfor specific plugins.

Here are some commonly used documents:

* Changelog
* Configuration
* FAQ
* Releases
* Security

## ❤️ Contribute

We love our community of over 1,200 contributors! Many of the plugins included
in Telegraf were originally contributed by community members. Check out
ourcontributing guideif you are interested in helping out.
Also, join us on ourCommunity SlackorCommunity Forumsif you have questions or
comments for our engineering teams.

If you are completely new to Telegraf and InfluxDB, you can also enroll for free
atInfluxDB universityto take courses
to learn more.

## ℹ️ Support

Please use theCommunity SlackorCommunity Forumsif you have questions or
comments for our engineering teams. GitHub issues are limited to actual issues
and feature requests only.

## 📜 License

## About

Agent for collecting, processing, aggregating, and writing metrics, logs, and other arbitrary data.

influxdata.com/telegraf

### Topics

 golang

 mqtt

 json

 kafka

 monitoring

 influxdb

 time-series

 metrics

 logs

 modbus

 telegraf

 xpath

 telemetry-collection

 t

 hacktoberfest

 windows-eventlog

 opcua

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

16.9k

 stars
 

### Watchers

293

 watching
 

### Forks

5.8k

 forks
 

 Report repository

 

## Releases214

v1.38.4

 Latest

 

May 11, 2026

 

+ 213 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go99.5%
* Shell0.3%
* Makefile0.1%
* Ragel0.1%
* Python0.0%
* Ruby0.0%