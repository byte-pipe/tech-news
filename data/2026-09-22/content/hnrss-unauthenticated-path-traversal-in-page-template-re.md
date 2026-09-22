---
title: Unauthenticated path traversal in page-template resolution leading to conditional RCE · Advisory · WordPress/wordpress-develop · GitHub
url: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
site_name: hnrss
content_file: hnrss-unauthenticated-path-traversal-in-page-template-re
fetched_at: '2026-09-22T21:49:26.899270'
original_url: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
date: '2026-09-22'
description: GitHub is where people build software. More than 150 million people use GitHub to discover, fork, and contribute to over 420 million projects.
tags:
- hackernews
- hnrss
---

WordPress

 

/

wordpress-develop

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.7k
* Star3.4k

# Unauthenticated path traversal in page-template resolution leading to conditional RCE

 Critical

johnbillion

 published
 
GHSA-7hp8-65ch-5whp

Sep 22, 2026

## Software

WordPress
 

## Affected versions

7.1.0 - 7.1.1

7.0.0 - 7.0.5

6.9.0 - 6.9.8

6.8.0 - 6.8.9

6.7.0 - 6.7.8

6.6.0 - 6.6.8

6.5.0 - 6.5.11

6.4.0 - 6.4.11

6.3.0 - 6.3.11

6.2.0 - 6.2.12

6.1.0 - 6.1.13

6.0.0 - 6.0.15

5.9.0 - 5.9.17

5.8.0 - 5.8.16

5.7.0 - 5.7.18

5.6.0 - 5.6.20

5.5.0 - 5.5.21

5.4.0 - 5.4.22

5.3.0 - 5.3.24

5.2.0 - 5.2.27

5.1.0 - 5.1.25

5.0.0 - 5.0.28

4.9.0 - 4.9.32

4.8.0 - 4.8.31

4.7.0 - 4.7.36

## Patched versions

7.1.2

7.0.6

6.9.9

6.8.10

6.7.9

6.6.9

6.5.12

6.4.12

6.3.12

6.2.13

6.1.14

6.0.16

5.9.18

5.8.17

5.7.19

5.6.21

5.5.22

5.4.23

5.3.25

5.2.28

5.1.26

5.0.29

4.9.33

4.8.32

4.7.37

## Description

An unauthenticated attacker can makeget_page_template()page-template resolution include a chosen readable local.phpfile outside the active theme directories. If relevant pre-conditions for both the server environment and the active theme are met, this can lead to RCE.

The pre-conditions are:

* The active child or parent theme contains a top-level directory whose name starts withpage-(e.g.page-templates). This affects the legacy Twenty Twelve and Twenty Fourteen themes, as well as some popular third party themes such as Neve, Hestia, and Sydney.
* A chosen local.phptarget file exists on the server and is readable by the web server account. The well knownpearcmd.phpPEAR→RCE transition can be used for this whenregister_argc_argvis set toOn. The officialphpimage for Docker is affected, and the default cPanel configuration is affected when PHP prior to 8.5 is in use.

WordPress 7.1.2 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed byRobert Ressl.