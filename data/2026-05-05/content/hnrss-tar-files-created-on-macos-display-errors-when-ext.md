---
title: Tar Files Created on macOS Display Errors When Extracting on Linux
url: https://aruljohn.com/blog/macos-created-tar-files-linux-errors/
site_name: hnrss
content_file: hnrss-tar-files-created-on-macos-display-errors-when-ext
fetched_at: '2026-05-05T00:51:46.208523'
original_url: https://aruljohn.com/blog/macos-created-tar-files-linux-errors/
author: Arul John
date: '2026-04-30'
published_date: '2024-12-06T04:10:28+00:00'
description: tar.gz files seem to include extra files starting with ._. When these are extracted on Linux, a bunch of errors are displayed.
tags:
- hackernews
- hnrss
---

# Tar Files Created on macOS Display Errors When Extracting on Linux

Published December 06, 2024

Home
 → 
Articles
 → 
Tech
 💻

I use my MacBook as my development machine and Debian / Ubuntu / Red Hat Linux at work and on this website. I occasionally create tarballs, or tar.gz and tgz files on Mac, which are then deployed on Linux servers. When I untar the tar.gz file on the Linux server, it may throw errors or warnings.

Table of Contents
* Creating tar files
* SCP to Linux server
* Extract or untar pix.tar.gz
* Warnings and errors when extracting tar.gz or tgz files
* Why does it have those extra files?
* Solution 1: Use--no-xattrswhile creating the tar
* Solution 2: Use--disable-copyfilewhile creating the tar
* Solution 3: Install and use gnu-tar instead of bsdtar
* Conclusion

## Creating tar files

I create tar.gz files the regular way. For example, if I want to create a tar.gz file of a directorypixcontaining pictures.

tar -cvzf pix.tar.gz pix

That command will create a tar gzipped filepix.tar.gz.

## SCP to Linux server

I will scp this tar.gz tomyserver.tldasuserand under the/tmpdirectory

scp pix.tar.gz user@myserver.tld:/tmp/

## Extract or untar pix.tar.gz

Now, I will extract this gzipped tar file on the Linux server.

cd /tmp
tar -xzvf pix.tar.gz 

Output (snippet):

...
pix/TODO/._IMG_3110.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3110.jpeg
pix/TODO/._IMG_3113.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3113.jpeg
pix/TODO/._IMG_3115.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3115.jpeg
pix/TODO/._IMG_3114.jpeg
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'
pix/TODO/IMG_3114.jpeg
...

## Warnings and errors when extracting tar.gz or tgz files

As we can see, the tar file contained several new files starting with._. These appear to be duplicates of existing files.

You may or may not see errors and warnings when extracting files that were tarred on macOS.

On one occasion, I saw warnings like this:

tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemTextContentLanguage'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseVersion'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseLabels'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseConfidences'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'

Another time, I got these warnings:

tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.lastuseddate#PS'

And then, this:

tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemTextContentLanguage'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseVersion'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseLabels'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemKeyphraseConfidences'

## Why does it have those extra files?

For some reason, the default BSD tar program on macOS seems to create and add these new files. There are two ways to get create a clean tar file.

## Solution 1: Use--no-xattrswhile creating the tar

While creating the tar file, you can add the attribute--no-xattrs. Doing this will prevent the extra files from getting added.

Previously, we did this:

tar -cvzf pix.tar.gz pix

Now, we will do this:

tar -cvzf --no-xattrs pix.tar.gz pix

This is the simplest way.

Now, SCP it to your Linux server and untar / gunzip it. You should not find the extra files or any errors or warnings.

tar -xzvf pix.tar.gz

## Solution 2: Use--disable-copyfilewhile creating the tar

Similar to the previous solution, in this case, we will use the--disable-copyfileoption.

tar -cvzf --disable-copyfile pix.tar.gz pix

Now, SCP the pix.tar.gz file to your Linux server and extract it. You should not find the extra files or any errors or warnings.

tar -xzvf pix.tar.gz

## Solution 3: Install and use gnu-tar instead of bsdtar

This is more of a permanent solution, in that you don't have to remember to type the extra optional arguments.

On your macOS, run this command to verify that you are using bsdtar. You should get something like this.

$ tar --version
bsdtar 3.5.3 - libarchive 3.5.3 zlib/1.2.12 liblzma/5.4.3 bz2lib/1.0.8 

Check in which directory bsdtar is installed:

$ which tar
/usr/bin/tar

### Install gnu-tar

Now, install gnu-tar using Homebrew.

$ brew install gnu-tar

After a few minute, gnu-tar will be installed in your macOS. It will get installed in this location:

/usr/local/opt/gnu-tar/libexec/gnubin/tar

### Verify gnu-tar installation

You can verify gnu-tar by running this:

$ /usr/local/opt/gnu-tar/libexec/gnubin/tar --version
tar (GNU tar) 1.35
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by John Gilmore and Jay Fenlason.

### Make gnu-tar your default tar

Now, you can make that your default by setting the path to gnu-tar earlier than bsdtar in your~/.bash_profilefile.

Edit your~/.bash_profilefile.

If you are using a Mac with an Intel processor, add this line:

export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"

If you are using a Mac with an Apple Silicon M1, M2, M3 or M4 processor, add this line:

export PATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"

Save and quit your editor and restart your Terminal session.

### Check that gnu-tar is default tar, and tar again

Test and see iftar --versionreturns GNU tar instead of BSD tar.

$ tar --version
tar (GNU tar) 1.35
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by John Gilmore and Jay Fenlason.

If you get a similar response, then recreate the tar file the regular way.

tar -cvzf pix.tar.gz pix

SCP it to your Linux server and untar / gunzip it. You should not find the extra files or any errors or warnings.

## Conclusion

I hope the steps in this blog post worked for you. This post will be updated whenever there is anything relevant. Feel free tocontact meif you have any questions or suggestions.

macos
 
linux
 
tar
 
gz
 
extract

## Related Posts

* How to Create Large Files in Linux and macOS 1GB 10GB 100GB 1TB
* How to Install OpenJDK Java 8 on MacOS using Homebrew in 2025
* How to Add HTTP Referer to Curl Commands
* How to Read a File Line by Line in Linux
* Create a File of Specific Size in Linux
* How to Change the Modification Date and Time of a File in Linux
* How to install Windows 7 on VirtualBox
* How to Hack Your Linksys WRT54G Wireless-G Router With DD-WRT Firmware
* How to Set Up and Secure Your Linode Server
* jq Command for JSON Processing with Practical Examples

If you have any questions, please contact me atarulbOsutkNiqlzziyties@gNqmaizl.bkcom. You can also post questions in ourFacebook group. Thank you.

Disclaimer: Our website is supported by our users. We sometimes earn affiliate links when you click through the affiliate links on our website.

Last Updated: December 06, 2024.     This post was originally written on December 05, 2024.

← Previous PostHow to Get Rid of PHP mb_convert_encoding() Deprecation Error

Next Post →How to Use Python list.sort() and sorted() Functions