---
title: Ubiquiti Launches UniFi OS Server for Self-Hosting — LazyAdmin
url: https://lazyadmin.nl/home-network/unifi-os-server/
site_name: hackernews
fetched_at: '2025-08-02T01:05:45.060706'
original_url: https://lazyadmin.nl/home-network/unifi-os-server/
author: Rudy Mens
date: '2025-08-02'
published_date: '2025-07-31T17:12:54+00:00'
---

Ubiquiti just released UniFi OS Server in Early Access, allowing you to self-host the complete UniFi network stack on your own hardware. Initially, it will support UniFi Network and Innerspace.

Besides UniFi Network and InnerSpace, you can also run UniFi Identity on UniFi OS Server, which was not possible with the self-hosted UniFi Network server, for example.

In this article

Toggle

Let’s take a look at how to install and configure UniFi OS Server.

## Requirements

The currently known requirements for UniFi OS Server are:

* Storage:Minimum: 20GB of free disk space.
* Windows: WSL (Windows Subsystem for Linux) version 2.
* Linux: Podman 4.3.1 or higher.
* Ports used:3478, 5005, 5514, 6789, 8080, 8444, 8880, 8881, 8882, 9543, 10003, 11443.

### Download links

Windows (arm64)Windows (x64)macOSmacOS (Intel)Linux (arm64)Linux (x64)

## Installing UniFi OS Server

Currently, I have only tested the installation on a Windows machine. I will maybe try to install it next week on a Linux-based VPS. So for the Windows installation, just download the setup file, click next, and wait for the initial installation to complete.

After the initial installation, it will take a couple of minutes to set up the WSL environment, and it will also take a moment to start up the UniFi OS Server setup.

When the server is done booting up, you can enter a name for your server. Next, we need to log in with our Ubiquiti account. This way, we can manage the server just like we normally do through unifi.ui.com.

You can also proceed without an Ubiquiti account, but then you won’t be able to manage the server remotely, no MFA, no notifications, no cloud backup, and you also won’t be able to useTeleportandSite Magic VPN.

After signing in, you will have the option to import an existing network if you already have a self-hosted UniFi Network installation on the same machine. Another option you will get is to restore a backup from one of your UniFi Consoles.

UniFi OS Server comes pre-installed with UniFi Network. This means you only need toconfigure your network, and you are good to go.

The current version of UniFi OS Server also supports InnerSpace. If you want to use that, simply go to Settings > Control Plane and install InnerSpace.

### Starting/Stopping the Server

When you close the interface of UOS, the server will remain active in the background, which is great. But when you want to stop the actual server, you will need to go to your system tray, right-click the UniFi icon, and hit exit. This way, the server will actually shut down.

To start it, simply open the app from your start menu. A known bug at the moment is that after UOS is started, it will show a message that UniFi Network is offline. This only takes a few seconds until it’s up and running as well.

If UOS is running, you can also access it directly in your browser through https://localhost:11443.

## Installing UOS on Debian

As said, I have not installed it on Linux myself, but to get you started, to install UniFi OS Server on Debian, you can use the following commands: install all required dependencies

# src: Mirano Verhoef
# Go into root
su -

# Install all required dependencies
apt update ; apt upgrade ; apt install podman -y ; cd ~ ; mkdir 4.2.23 ; cd 4.2.23 ; wget https://fw-download.ubnt.com/data/unifi-os-server/8b93-linux-x64-4.2.23-158fa00b-6b2c-4cd8-94ea-e92bc4a81369.23-x64 ; chmod +x 8b93-linux-x64-4.2.23-158fa00b-6b2c-4cd8-94ea-e92bc4a81369.23-x64 ; ./8b93-linux-x64-4.2.23-158fa00b-6b2c-4cd8-94ea-e92bc4a81369.23-x64 install

### SSL Cert when using Linux

If you are running UniFi OS on Linux, then you can install a Let’s Encrypt SSL certificate using the following script from Mirano Verhoef:MiranoVerhoef/UniFi-OS-Server-SSL-Import: Import for new Unifi OS Server

## Wrapping Up

It’s great to see that we can run UniFi OS Server in a self-hosted environment. I think we are all waiting and hoping that Ubiquiti will also add UniFi Protect to UOS.

Hope you liked this article. If you have any questions, drop a comment below.

## You may also like the following articles

Jun 18, 2025

### How to set up UniFi Site-to-Site VPN

Jun 17, 2025

### UniFi Protect 6.0 Update – What you need to know

Jun 3, 2025

### How to Install an Access Point – Complete Guide
