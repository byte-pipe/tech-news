---
title: 'GitHub - kelseyhightower/kubernetes-the-hard-way: Bootstrap Kubernetes the hard way. No scripts. · GitHub'
url: https://github.com/kelseyhightower/kubernetes-the-hard-way
site_name: github
content_file: github-github-kelseyhightowerkubernetes-the-hard-way-boot
fetched_at: '2026-09-25T15:44:39.826728'
original_url: https://github.com/kelseyhightower/kubernetes-the-hard-way
author: kelseyhightower
description: Bootstrap Kubernetes the hard way. No scripts. Contribute to kelseyhightower/kubernetes-the-hard-way development by creating an account on GitHub.
---

kelseyhightower

 

/

kubernetes-the-hard-way

Public

* NotificationsYou must be signed in to change notification settings
* Fork15.9k
* Star50.1k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

296 Commits
296 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
configs
configs
 
 
docs
docs
 
 
units
units
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
COPYRIGHT.md
COPYRIGHT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ca.conf
ca.conf
 
 
downloads-amd64.txt
downloads-amd64.txt
 
 
downloads-arm64.txt
downloads-arm64.txt
 
 
View all files

## Repository files navigation

# Kubernetes The Hard Way

This tutorial walks you through setting up Kubernetes the hard way. This guide is not for someone looking for a fully automated tool to bring up a Kubernetes cluster. Kubernetes The Hard Way is optimized for learning, which means taking the long route to ensure you understand each task required to bootstrap a Kubernetes cluster.

The results of this tutorial should not be viewed as production ready, and may receive limited support from the community, but don't let that stop you from learning!

## Copyright

This work is licensed under aCreative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

## Target Audience

The target audience for this tutorial is someone who wants to understand the fundamentals of Kubernetes and how the core components fit together.

## Cluster Details

Kubernetes The Hard Way guides you through bootstrapping a basic Kubernetes cluster with all control plane components running on a single node, and two worker nodes, which is enough to learn the core concepts.

Component versions:

* kubernetesv1.32.x
* containerdv2.1.x
* cniv1.6.x
* etcdv3.6.x

## Labs

This tutorial requires four (4) ARM64 or AMD64 based virtual or physical machines connected to the same network.

* Prerequisites
* Setting up the Jumpbox
* Provisioning Compute Resources
* Provisioning the CA and Generating TLS Certificates
* Generating Kubernetes Configuration Files for Authentication
* Generating the Data Encryption Config and Key
* Bootstrapping the etcd Cluster
* Bootstrapping the Kubernetes Control Plane
* Bootstrapping the Kubernetes Worker Nodes
* Configuring kubectl for Remote Access
* Provisioning Pod Network Routes
* Smoke Test
* Cleaning Up