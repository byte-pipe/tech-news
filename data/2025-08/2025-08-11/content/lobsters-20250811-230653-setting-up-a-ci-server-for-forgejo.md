---
title: Setting up a CI server for Forgejo
url: https://robey.lag.net/2025/08/10/forgejo-ci.html
site_name: lobsters
fetched_at: '2025-08-11T23:06:53.294172'
original_url: https://robey.lag.net/2025/08/10/forgejo-ci.html
date: '2025-08-11'
tags: devops, testing
---

I recently got CI working with my personal forgejo instance, and thought I would share how I did it. It’s not that hard, but has a few confusing quirks, and all the tutorials I found online were wrong, outdated, or both. They also tend to include a few pages of steps you don’t really need for a small instance.

Background:Forgejois a “software forge” – a way to host git & jujutsu code repos for you, your friends, or your team. It’s part of the “small communities” decentralization movement, and is a good replacement for things like Github or Launchpad. CI means “continual integration” which just means “build server” like Jenkins, TeamCity, or Tinderbox. It’s totally possible to host your own code and CI on 1 or 2 servers, virtual or home lab.

How it works: The build server runs some kind of Linux container manager. I chosepodman, a command-line tool that’s compatible with Docker, but much smaller & simpler, and doesn’t have to run as root. A separate service calledforgejo-runnerauthenticates with your forgejo server, receives build requests, runs them on the container, and sends back logs and artifacts.

Forgejo recommends putting the build server on a different machine than the forge, because both pieces of software can run hot, and the build server will be literally running new Linux VMs to do builds. For security, you probably want to treat the build machine as disposable: don’t give it access to anything besides your forge, and rebuild it from scratch if it behaves suspiciously. (I haven’t had any trouble here. This is just general good advice.)

I chose Alpine as the Linux install for the build machine. It’s a good thin distribution for servers, where you don’t need any bells and whistles or a full desktop. The first time I tried it, I was pleasantly surprised that the display oftoponly showed my servers, not pages and pages of systemd and random “support” daemons. It also has packages for podman and forgejo-runner, which greatly simplifies the CI install.

## Install Alpine

If you already have an Alpine 3.22 VM ready, you can skip this part. Otherwise, install a fresh Alpine image, and do the bare minimum:

# setup-alpine

* Make sure to create a user account for yourself and add your SSH key.
* Add your user account to/etc/sudoersunderroot.
* Make sure you can login as your new user, from a new ssh connection, andsudo echo hito make sure you can sudo.
* Turn off ssh password auth. I don’t understand why this defaults on for virtual machine images.Edit/etc/ssh/sshd_config, find thePasswordAuthenticationline, and change the value toNo.
* Edit/etc/ssh/sshd_config, find thePasswordAuthenticationline, and change the value toNo.

If you’re picky like me, now is also your chance to install some of your favorite tools:

# apk add less lsof

Now upgrade it to at least 3.22, if it’s not already. That’s the minimum version to get forgejo-runner.

* Edit/etc/apk/repositoriesChange the version number to3.22on every line.
* Change the version number to3.22on every line.

# apk update
# apk add --upgrade apk-tools
# apk upgrade --available

This should be pretty fast. Then reboot into the new, fresh-smelling 3.22:

# reboot

From now on, you’ll be logging into this machine as yourself (the username you added above), not root, and using “sudo” to do things that require root permission.

## Install podman & runner

Podman and forgejo-runner can be installed at the same time, but they need extra dependencies. Some are obvious (git), others are needed to create virtual file systems and network interfaces.

# apk add nodejs npm rsync git iptables podman forgejo-runner slirp4netns fuse
# rc-update add cgroups
# rc-service cgroups start
# modprobe tun
# echo tun >>/etc/modules
# echo forgejo-runner:100000:9999 >>/etc/subuid
# echo forgejo-runner:100000:9999 >>/etc/subgid

If you aren’t already using tmpfs, you need to set that up too. Podman has a panic attack if it sees old files in/tmpafter a reboot:

# echo "tmpfs /tmp tmpfs nodev,nosuid,size=1G 0 0" >> /etc/fstab
# mount /tmp

At this point, you should be able to run a test image with podman – as your normal user account! – to prove it’s installed correctly.

$ podman run --rm hello-world

We need to do a little bootstrapping to make sure the environment is set up correctly before starting the daemons. Runner creates its own user (forgejo-runner) and we want podman to run as the same user. Runner will create this user’s home folder the first time it starts, but it expects podman to be running already, and podman will crash if it can’t reach the same home folder. Easy to untangle, though.

# forgejo-runner generate-config > /etc/forgejo-runner/config.yaml
# mkdir /var/lib/forgejo-runner
# chown forgejo-runner:forgejo-runner /var/lib/forgejo-runner

Runner and podman communicate through a unix socket. Podman’s default location for this socket is undiscoverable, so tell them to look in/tmp.

* Edit/etc/conf.d/podmanand change these lines:podman_uri="unix:///tmp/podman.sock"podman_user="forgejo-runner"
* podman_uri="unix:///tmp/podman.sock"
* podman_user="forgejo-runner"
* Edit/etc/forgejo-runner/config.yamland change this line inside thecontainersection at the end:docker_host: "unix:///tmp/podman.sock"
* docker_host: "unix:///tmp/podman.sock"

Also, the startup script for forgejo-runner has a bug. It can’t start at boot time until podman is running, but they forget to add a dependency.

* Edit/etc/init.d/forgejo-runnerand add this line insidedepend():need podman
* need podman

That makes thedepend()function look like:

depend() {
 need net
 need podman
 use dns logger
}

Nowrebootto make sure all the new config is loaded (especially the changes to/etc/subuidand/etc/subgid).

## Start the podman & runner services

# rc-update add podman
# rc-service podman start
# rc-service podman status

As your normal user, double-check that the runner can talk to podman, and register it with your forgejo server:

$ doas -u forgejo-runner podman run --rm alpine echo "It works!"
$ cd /var/lib/forgejo-runner && doas -u forgejo-runner forgejo-runner register

It will ask for your forgejo server’s url, and then a token. There are a few kinds of tokens, but the simplest kind is the “site” token which gives access to every project on your server. That’s in the upper right corner under “Site administration” -> “Actions” -> “Runners” -> “Create new runner”.

After that, you should see the config in/var/lib/forgejo-runner/.runneras JSON. You can change the label here if you like, but I figured “docker” is already a pretty good description of what’s going on.

Now you can start up the runner:

# rc-update add forgejo-runner
# rc-service forgejo-runner start
# rc-service forgejo-runner status

Back on your forgejo server, reloading the “Runners” admin page should show your new runner as idle. You did it!

As a last step, you may need to “activate” actions for your project(s). That’s a separate checkbox in the project’s “Settings” page, under “Units” -> “Overview”.

## How do I use this?

Forgejo runners seem to be based on a Github feature called “Github Actions”. They’re so heavily based on it that they use the same build file structure, use Github’s name in many of the field names and environment variables, and require a lot of ceremony that’s overkill for a team build server.

Describe a build by committing a special file into your repo in a.forgejo/workflows/folder. This file must be YAML. Inside, you declare which runner to use (usually “docker” unless you changed it), which docker base image to start from, and a set of steps/commands. Optionally, you can set which branches trigger the build when pushed. Here’s a simple example:

# .forgejo/workflows/build.yaml

---
name: build
"on":
 push: "*"
jobs:
 build:
 runs-on: docker
 container:
 image: "rust:alpine"
 steps:
 - run: apk add nodejs npm git
 - uses: actions/checkout@v4
 - run: "./ci.sh"

This calls the build “build”, starts it on a push to any branch, starts with therust:alpinebase docker image, and runs the shell scriptci.shto do the actual build.

Two tricky bits to catch here: You have to add theuses:line to ask explicitly for your code to be cloned into the image – without that, you get an empty folder. And before that, you need to install nodejs & git in the image, because the “plugin” that handles that is written in typescript, and will fallback to downloading your code over an API if it can’t find git installed. This looks like a bunch of cruft “borrowed” from Github, which hasn’t bothered anyone enough to get fixed yet.

As soon as you push this file to your forgejo repo, you can go watch your build in the “Actions” tab. Congrats!
