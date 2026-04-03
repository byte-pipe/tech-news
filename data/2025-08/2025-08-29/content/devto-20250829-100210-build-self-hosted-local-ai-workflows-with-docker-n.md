---
title: Build self-hosted local AI workflows with Docker, n8n, Ollama, and ngrok - DEV Community
url: https://dev.to/ngrok/build-self-hosted-local-ai-workflows-with-docker-n8n-ollama-and-ngrok-40jh
site_name: devto
fetched_at: '2025-08-29T10:02:10.150981'
original_url: https://dev.to/ngrok/build-self-hosted-local-ai-workflows-with-docker-n8n-ollama-and-ngrok-40jh
author: Joel Hans
date: '2025-08-26'
description: Workflow automation is one of those things that often works best when you host it yourself. Why?... Tagged with docker, ai, automation, devops.
tags: '#docker, #ai, #automation, #devops'
---

Workflow automation is one of those things that often works best when you host it yourself. Why? Because the tools you chain together usually require (sensitive) internal data, self-hosting lets you keep full control while also keeping costs down. That goes doubly so for AI-driven workflow automation—who knows what might happen to sensitive data once it's passed onto the "black boxes" of popular AI efforts.

That said, it's easy for any self-hosting effort to get caught up in deployment and security red tape. How are you going to deploy and maintain it? Are youreallygoing to port forward and doxx your IP to the world? A VPN works for sharing with colleagues, but what about external APIs or receiving webhooks?

For the first question, that's why Docker exists in the first place. Docker Desktop, in particular, makes deploying AI workflows ridiculously easy.

For everything else, there's ngrok's gateways and our new Docker Desktop extension, which makes sharing your AI workflow automations easy to configure (less waiting on IT) and security-first (no more getting scolded by the network folks).

In this quick guide, I'll walk you through two gateways you can ship here to get the job done.

1. The three-click gateway
2. The secure (but still simple) gateway

Big fan of video? Click the big red button to get a short-and-sweet edition of this setup—but read the rest for all the details.

## The self-hosted AI workflow architecture

1. ngrok* [ngrok](https://ngrok.com] is a flexible, globally distributed gateway that helps you share apps, APIs, devices, or entire networks with the world... and then lock them down exactly as you need with configurable policies written in YAML. It started long ago as "online in one line," but now covers advanced API gateway features in ways that remain simple to configure and maintain.
* ngrok will receive, authenticate (if you let it), and forward all the traffic to your self-hosted AI workflows.
2. Docker* Docker(Engine) helps you download and deploy software packaged in lightweight, isolated containers.
* Docker Desktopsimplifies the developer experience around starting and running containerized software by replacing thedockerCLI with a GUI for macOS, Windows, and Linux, while still exposing all the nuances "under the hood."
3. n8n* With a hugely popularopen-source repo, n8n is a workflow automation platform with a visual builder and tons of integrations with both remote and local software like LLMs.
4. Ollama* Open-source developer tooling, mostly on the CLI but with a small desktop GUI as well, to help you download, manage, and self-host LLMs.
* gpt-ossis a newopen-weight modelthat was, according to OpenAI, "designed for powerful reasoning, agentic tasks, and versatile developer use cases." You could also pickDeepSeek-R1,Gemma 3, or anything else fromOllama's library.
5. Your local compute* The beauty of self-hosting is that it works with any system whose resources and uptime you want to spare—that could be the laptop you use for work, a cluster of Raspberry Pis in the closet, or a VM in the cloud.

This architecture is also an infinitely repeatable pattern. Just replace n8n and Ollama with the containerized services you need to run, and you're off to the races with far more control and less cost than relying solely on a platform as a service (PaaS) provider.

## What you'll need

Start withDocker Desktopinstalled andsign up for a free ngrok accountif you don't already have one.

I also recommend youreserve a static subdomain(likeyour-ai-workflow.ngrok.apporbring your custom domainto ngrok so we can handle certificates on your behalf. You can create random and purely ephemeral public URLs with ngrok, but it's not particularly useful long-term.

I'll refer to that as$NGROK_DOMAINfrom here on out.

## Set up your self-hosted AI workflow

All this happens directly within Docker Desktop—nice and tidy.

### Ollama

Click onDocker Hub,search forOllama, clickRun. Give it a name like ollama (wild, I know) and the default host port of 11434.

ClickExecto enter the containers CLI and pull a model like gpt-oss:

ollama pull gpt-oss

Enter fullscreen mode

Exit fullscreen mode

### n8n

Just as you did with Ollama, findn8nand run it.

I highly recommend these optional settings:

* Container name:n8n(just... because)‍
* Host port:5678(defaults are good)‍
* Volumes:n8n_data//home/.node.n8n(to create a volume for n8n that's separate from the container itself)‍
* Environment variables:N8N_EDITOR_BASE_URL /$NGROK_DOMAIN(to let n8n know it's not being hosted onlocalhostforever)If you really want to use a random ngrok URL, then you can leave this blank.
* If you really want to use a random ngrok URL, then you can leave this blank.

When you clickRun, Docker Desktop drops into the container's logs. Your editor won'tquite yetbe available via$NGROK_DOMAIN, but it will be soon.

All done running new containers.

### ngrok's Docker Desktop extension

Here's thedirect link, or you can clickExtensions -> Manage -> Browseand search for ngrok there.

Once installed, clickOpen. You'll need your ngrok authtoken, which you cancopy from the dashboardand paste into Docker Desktop.

Next up: sharing your containers on the public internet.

## The three-click gateway

1. The+icon next to your n8n container to create a new endpoint. Leave the defaultPublicsetting, but if you have an$NGROK_DOMAIN, drop that in as the URL.
2. Next Step.
3. Skip and Create Endpoint. This completely ignores the incredible power ofTraffic Policy(more on that soon), but I did promise you three clicks.

You'll have a public endpoint and URL for your n8n instance that you or others can access from anywhere.

As some ngrokkers like to say (when not"doglabbing" ngrok):It's just that shrimple.

## The secure (but still simple) gateway

A bundle of security-conscious neurons might've jumped to life at the phrase just above:you or others can access from anywhere. It's actually quite scary to have a self-hosted service available on the public internet—you never quite know what anyone is up to, and even though n8n comes with user management built-in, someone could still hammer the login page into oblivion trying an automated attack against common username:password patterns.hunter2, anyone?

Authentication is one place where ngrok shines as a gateway to your self-hosted services. AndTraffic Policyis a configuration language that gives you complete control over how traffic gets to your apps—or if it should get there at all.

In Docker Desktop, click those three dots next to your endpoint, thenEdit Endpoint. Scroll down a bit for theTraffic Policyinput and paste in this policy.

on_http_request
:


-

actions
:


-

type
:

oauth


config
:


provider
:

google


-

expressions
:


-

"
!actions.ngrok.oauth.identity.email.endsWith('@example.com')"


actions
:


-

type
:

custom-response


config
:


body
:

Hey, no n8n for you ${actions.ngrok.oauth.identity.name}!


status_code
:

400

Enter fullscreen mode

Exit fullscreen mode

What's happening here?This policy forces every request to log in with Google-provided OAuth. If the Google account used to log indoesn'tend with@example.com(replace with your organization's domain), ngrok rejects the request before it gets anywhere near your self-hosted AI.

You now have ngrok working as a gateway that 1) handles your public URL/domain, 2) routes traffic into your Docker containers, and 3) authenticates said traffic before it ever gets close to your local compute.

### Side quest: Expose the Ollama API directly (and securely)

Let's say you're self-hosting this self-hosted AI stack on behalf of your organization, and one of your developers wants to hit the Ollama API directly instead of through n8n and some workflow.

The same process works here, too: Start a new endpoint, give it an ngrok URL (if you have another to spare), and add another policy to authenticate that API traffic before it hits your network. Because it's an API, which assumescurland machine-to-machine (M2M) communication, OAuth isn't going to cut work, but you can also choose fromIP restrictions,JWT validation, or even a "secret" header value that you filter against with an expression, like"'averysecretvalue' in req.headers['x-super-secret-token']".

IP restrictions might require a little more maintenance over time if folks are traveling or have dynamic IPs, but theyareinfallible—just replace the IPs inallowwith the ones you want to give access to the Ollama API.

on_http_request
:


-

actions
:


-

type
:

restrict-ips


config
:


enforce
:

true


allow
:


-

1.1.1.1/32


-

1.2.3.4/32

Enter fullscreen mode

Exit fullscreen mode

## What's next?

Of course, this leaves you with the task of still building out all your automations with n8n, Ollama, and whatever else you want to connect together. Here are some things you might consider:

* Replace Cursor-generated AI overviews of PRs with ones generated by your LLM.
* Create a custom chatbot based on internal documentation in Notion or elsewhere.
* Give developers an AI coding agent to build with while also still keeping a tight hold of your data.

There's also plenty more to dig into with ngrok within our Docker Desktop extension to make your gateway even more production-grade:

* Endpoint Pooling: If you have multiple Ollama containers across different servers or laptops, you can check theEndpoint Poolingtoggle in ngrok's Docker Desktop extension to automatically load balance between them. Just make sure you put them on the same public URL so your ngrok gateway knows what to do.
* More Traffic Policyfor advanced gateways: If you have other self-hosted services you want to put behind a single gateway and URL+path combinations likeinternal.example.com/n8nandinternal.example.com/something-else, consider the"front door" patternormultiplexing.
* Observability: Click the three dots in Docker Desktop and thenView inTraffic Inspectorto see real-time logs about all the requests and responses flowing through your system.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
