---
title: I Followed the n8n AWS Docs and It Broke at the First Command - DEV Community
url: https://dev.to/aws-builders/i-followed-the-n8n-aws-docs-and-it-broke-at-the-first-command-4e1k
site_name: devto
content_file: devto-i-followed-the-n8n-aws-docs-and-it-broke-at-the-fi
fetched_at: '2026-09-30T22:50:58.374424'
original_url: https://dev.to/aws-builders/i-followed-the-n8n-aws-docs-and-it-broke-at-the-first-command-4e1k
author: Sarvar Nadaf
date: '2026-09-25'
description: The one command that breaks n8n self-hosting on Amazon Linux 2023, why it happens, and the full paste-ready Docker Compose setup that gets you from a bare EC2 box to your first login. Tagged with aws, n8n, docker, devops.
tags: '#aws, #n8n, #docker, #devops'
---

Includes a full paste-ready Compose fix

You SSH into a fresh EC2 box, runsudo dnf install -y docker, then the very next command from the guide you're following:

docker compose up 
-d

Enter fullscreen mode

Exit fullscreen mode

And it dies:

docker: 
'compose'
 is not a docker command.

Enter fullscreen mode

Exit fullscreen mode

I hit this on camera. Followed the steps, watched n8n never come up, and spent a few minutes convinced I'd broken something. I hadn't. Almost every "self-host n8n on AWS" tutorial has this exact hole in it, because the authors tested on Ubuntu or a VPS where Docker installs differently. On Amazon Linux 2023, the default AMI for EC2, the command they tell you to run gives you half of what you need.

This post is the fix, and the full path from a bare EC2 instance to your first n8n login. Two containers, one paste-ready compose file, no reverse proxy yet (that's the hardening step, and it's its own article). By the end you have n8n on Postgres running on a box you own.

## The gotcha, up front

On Amazon Linux 2023:

sudo 
dnf 
install
 
-y
 docker

Enter fullscreen mode

Exit fullscreen mode

installs the Dockerengine. It does not install theCompose v2 plugin. They're separate now. Compose stopped being a standalonedocker-composebinary years ago and became a plugin that lives under Docker's CLI, anddnf's docker package doesn't bundle it. So the engine runs fine,docker runworks, and thendocker composethrows'compose' is not a docker commandbecause the plugin isn't there.

On Ubuntu you'd installdocker.ioplusdocker-compose-pluginfrom Docker's apt repo and never notice. On AL2023 the plugin is on you. Here's the whole install, plugin included:

sudo 
dnf 
install
 
-y
 docker

sudo mkdir
 
-p
 /usr/local/lib/docker/cli-plugins

sudo 
curl 
-fsSL
 
\

 https://github.com/docker/compose/releases/download/v2.29.7/docker-compose-linux-x86_64 
\

 
-o
 /usr/local/lib/docker/cli-plugins/docker-compose

sudo chmod
 +x /usr/local/lib/docker/cli-plugins/docker-compose

sudo 
systemctl 
enable
 
--now
 docker

Enter fullscreen mode

Exit fullscreen mode

That third command is the one the other guides skip: it drops Docker's official Compose plugin binary into the directory the CLI actually looks in. Now both answer:

sudo 
docker 
--version

# Docker version 25.0.14, build 0bab007

sudo 
docker compose version

# Docker Compose version v2.29.7

Enter fullscreen mode

Exit fullscreen mode

Two version banners is how you know the box is actually ready. If you only check the first one, you find out the plugin is missing atdocker compose up, which is the worst time to find out.

One catch on the download URL: it ends inx86_64, which is right for at3(Intel) box. If you launched a Graviton/ARM instance (t4gand friends), grab theaarch64binary instead by swapping the filename todocker-compose-linux-aarch64. The wrong architecture installs cleanly and then fails with an exec-format error the moment you run it, which sends you hunting in the wrong place. Pick the binary that matches your instance. Andv2.29.7is just the version I pinned here; checkDocker's releasesand use the current one if you'd rather not lag.

## Launch the box first

Before any of that, you need the instance:

* AMI:Amazon Linux 2023.
* Size:t3.smallor larger. n8n plus Postgres want about 2 GB of RAM. Skipt2.microandt3.micro(1 GB) unless you like watching containers get OOM-killed mid-run.
* Security Group:SSH (22) from your IP only. For this private first test you can open 5678 to your IP only too. Do not open 5678 to0.0.0.0/0. An open n8n editor on the public internet is an editor anyone can find and claim.
* SSH in:ssh -i your-key.pem ec2-user@<PUBLIC_IP>

Everything below runs on that box asec2-user.

## Why bother self-hosting at all

n8n is a credential aggregator. One instance can hold your Stripe key, your database password, your Slack token, your Google OAuth, all in one place. On n8n Cloud that pile lives on someone else's server, priced per seat, capped on executions. Self-hosting moves it onto a box inside your own AWS account: no seat fees, no execution caps, your data stays home, and you pick the version.

The trade is honest. You now own the patching, the backups, and the security. This article gets it running. The hardening article (next in the series) closes the door behind it.

## The stack: two containers

That's the whole thing.

* n8nruns the editor and the workflow engine.
* Postgresstores workflows and executions so they survive a restart.

Not SQLite. n8n defaults to SQLite, which is fine for a five-minute look, but it handles concurrent executions poorly and migrating off it later is an afternoon you won't enjoy. Start on Postgres.

Clone the repo so you have the compose file on the box:

git clone https://github.com/simplynadaf/self-host-n8n-on-ec2.git

cd 
self-host-n8n-on-ec2/compose

Enter fullscreen mode

Exit fullscreen mode

Here's the compose file:

services
:

 
n8n
:

 
image
:
 
n8nio/n8n:1.123.64

 
restart
:
 
unless-stopped

 
ports
:

 
-
 
"
5678:5678"

 
environment
:

 
-
 
N8N_SECURE_COOKIE=false

 
-
 
N8N_DIAGNOSTICS_ENABLED=false

 
-
 
N8N_PERSONALIZATION_ENABLED=false

 
-
 
N8N_ENCRYPTION_KEY=change-me-to-a-long-random-string-please

 
-
 
DB_TYPE=postgresdb

 
-
 
DB_POSTGRESDB_HOST=postgres

 
-
 
DB_POSTGRESDB_DATABASE=n8n

 
-
 
DB_POSTGRESDB_USER=n8n

 
-
 
DB_POSTGRESDB_PASSWORD=change-me-strong-db-password

 
depends_on
:

 
-
 
postgres

 
postgres
:

 
image
:
 
postgres:16-alpine

 
restart
:
 
unless-stopped

 
environment
:

 
-
 
POSTGRES_DB=n8n

 
-
 
POSTGRES_USER=n8n

 
-
 
POSTGRES_PASSWORD=change-me-strong-db-password

 
volumes
:

 
-
 
pg_data:/var/lib/postgresql/data

volumes
:

 
pg_data
:

Enter fullscreen mode

Exit fullscreen mode

Three lines decide whether this works.

The image is pinned to1.123.64, notlatest.Pinning makes the build reproducible, and this version patches a real issue: CVE-2026-65589, an info-disclosure bug where credentials passed as custom headers in LLM sub-nodes could land in execution records. Runlatestand you're one silent restart away from a version you didn't choose.

N8N_ENCRYPTION_KEYencrypts every credential n8n stores.Set a real 32-plus character random string and save it somewhere safe right now. Lose it and every saved credential is unrecoverable. A restored backup without this key is a database full of workflows whose logins can't be decrypted.

The DB password appears twice(DB_POSTGRESDB_PASSWORDin the n8n service,POSTGRES_PASSWORDin postgres) and the two values must match. If they don't, n8n can't reach its own database and the container just restarts in a loop while you wonder why the editor never loads.

## Bring it up

Edit the two passwords and the encryption key, then:

sudo 
docker compose up 
-d

sudo 
docker compose ps

Enter fullscreen mode

Exit fullscreen mode

First run pulls both images and starts them. Give it twenty to forty seconds, then check n8n is answering:

curl 
-s
 
-o
 /dev/null 
-w
 
'n8n -> HTTP %{http_code}\n'
 http://localhost:5678

# n8n -> HTTP 200

Enter fullscreen mode

Exit fullscreen mode

200means n8n is up and serving. Once Compose was actually installed, this came back green on the first try.

## First login

Openhttp://<PUBLIC_IP>:5678in a browser. A fresh instance shows the setup wizard. Create your owner account with an email and a strong password, submit, and you land on the canvas.

Do this immediately after the box comes up, not tomorrow. The first account created on a fresh n8n becomes theowner, and until someone submits that form, it's open to whoever reaches it first. On a private Security Group that's only you. It's still a habit worth keeping.

One line in the compose file explains itself here:N8N_SECURE_COOKIE=false. That's only so first login works over plain HTTP on a raw IP while testing. It's a development shortcut, not a keeper. In production n8n sits behind HTTPS and this setting goes away.

## Before this goes anywhere near the internet

The compose here publishes port 5678 directly. That's fine for a private test where the Security Group only lets your IP in, but it falls apart on the open internet, where certificate transparency logs announce every new HTTPS host within minutes and scanners find fresh boxes fast.

Before you point a domain at this or widen the Security Group:

1. Keep n8n patched (1.123.64 or newer).
2. Stop publishing 5678. Useexposeso it's only reachable inside the Docker network.
3. Put Caddy in front for automatic TLS, and restrict the editor to your admin IP. Leave only/webhook/*public.
4. Move the encryption key and DB password into AWS Secrets Manager, read through a least-privilege IAM role.
5. Security Group: allow 22 (your IP), 80, 443. Never 5678 to0.0.0.0/0.

That whole checklist is the hardening article in this series. If this box is going public, that's your next read.

## Stop and start without losing data

Your data lives in thepg_datavolume, so you can stop the stack safely:

sudo 
docker compose down 
# stop, keep the data

sudo 
docker compose up 
-d
 
# start again

Enter fullscreen mode

Exit fullscreen mode

downstops the containers and keeps the volume, so your workflows and account are still there on the nextup. To also wipe the data, that'sdown -v, and only when you mean it.

## What you have now

* n8n running on an EC2 box you control, backed by Postgres.
* A pinned, patched image instead of a movinglatesttarget.
* An encryption key you actually set and saved.
* A clear line for what to do before this faces the internet.

And you know the one thing most AWS n8n guides get wrong: on Amazon Linux 2023, installing Docker does not install Compose, and the fix is onecurlinto the plugin directory.

## Where the series goes

* Get it running(this one): bare EC2 to first login, past the Compose gotcha.
* Harden it:TLS, closed editor port, Secrets Manager, least-privilege IAM.
* Give it a brain:wire this same n8n to Amazon Bedrock and build a real AI agent on the canvas, model running in your account, no OpenAI key anywhere.

The compose file, the install and verify scripts, and the full setup notes are in the repo:github.com/simplynadaf/self-host-n8n-on-ec2.

Follow me for more on AWS architecture, DevOps, and AI Infrastructure:Portfolio|LinkedIn|Dev.to|YouTube|Email|AWS Builder Center|X

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse