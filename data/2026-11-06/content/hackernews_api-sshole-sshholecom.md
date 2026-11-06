---
title: '*sshole · sshhole.com'
url: https://sshhole.com
site_name: hackernews_api
content_file: hackernews_api-sshole-sshholecom
fetched_at: '2026-11-06T12:28:24.728888'
original_url: https://sshhole.com
author: josemrb
date: '2026-11-05'
description: openssh on musl linux has been letting people into password-less accounts since 2016.
tags:
- hackernews
- trending
---

tl;dr

## try it

one debian box, one alpine box. type stuff. it all runs right here in your browser, nothing gets sent anywhere

ozgun

256 × A

300 × A

clear

256
1024

0bytes

debian · glibc

crypt(pw, bob's salt)

alice's field

*

alpine · musl

crypt(pw, bob's salt)

alice's field

*

## are you affected?

* is your sshd running onmusl? (alpine, openwrt, buildroot, yocto)
* is itnot using pam? alpine'sopenssh-serverdoesn't by default, or maybe you setUsePAM no
* arepassword loginsstill on? they are by default
* is there an account with just*as its password? key-only users, ldap users, root on alpine
* and someotheraccount with a real password?
* then that*account takes any password between 257 and 1024 characters

on alpine's official aws and azure images that's the defaultalpineuser, and it has passwordlessdoas. so it's root

on debian, ubuntu, fedora or anything else with glibc? going through pam? dropbear? openbsd? you're fine

## what now

you

# update. openssh 10.6p2 fixes it.

$
 apk upgrade openssh

# can't update yet? turn password logins off.

$
 echo "PasswordAuthentication no" > /etc/ssh/sshd_config.d/00-no-passwords.conf

$
 rc-service sshd restart