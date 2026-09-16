---
title: We wanted to use Baseten for inference. We ended up with admin access to Baseten GitHub repos - Strix
url: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
site_name: hackernews_api
content_file: hackernews_api-we-wanted-to-use-baseten-for-inference-we-ended-up
fetched_at: '2026-09-16T15:21:42.370283'
original_url: https://www.strix.ai/blog/baseten-harbor-github-pat-takeover
author: Strix
date: '2026-09-15'
description: We gave Strix a domain. In 25 minutes, it found a live token with admin access to Baseten's product, deployment, and CLI repos in a public Docker image.
tags:
- hackernews
- trending
---

September 1st, 2026

# We wanted to use Baseten for inference. We ended up with admin access to Baseten GitHub repos

Alex Schapiro

We were about to trust Baseten with our own and our customers’ data. So to be safe, we ran Strix to ensure they were secure first. About 25 minutes later, it had a live GitHub token with repository-level admin rights on internal Baseten repos.

We buildStrix, an autonomous hacking agent, which of course means we need (cheap and fast) inference. We were exploring our options, and Baseten is one of the obvious choices. It's a great product, they're valued at$13 billion, and a lot of serious companies depend on them.

But... we're a security company. Before we give a third party our data, models, or code, we scan them. We would much rather find a problem and help get it fixed before we start depending on that service (we do this with almost all of our vendors and have a high rate of finding serious issues).

So... we pointed Strix at*.baseten.coand let it run without credentials or source code.

It came back with an active GitHub personal access token forbasetenbot. That token hadadmin and push access to Baseten's main product repo, the GitOps repo that drives their clusters, and their Homebrew tap, plus read/write access to other private repositories including specific repos per customers.

The image build dated toMarch 2023, and the token still worked when we found it in July 2026.

But before we get into the details, let's give some kudos to Baseten's security team. They confirmed the issue as critical, locked down the registry project, and rotated the token by the next afternoon. They were professional and very quick to deal with it (which is often not the case in these situations).

## How Strix actually found it

Strix starts the way any good pentest does: recon. Many times the most severe vulnerability on your infra may be on a service on a subdomain you forgot about (which is why we always recommend black box testing alongside testing with code access)! So Strix enumerated hosts, looked through certificate logs, mapped the full surface. Eventually, it found a Harbor registry atgcp-us-east4-zlw.registry.baseten.co.

Harbor stores container images and groups repositories into projects. One of these projects was public. Without any token or auth, Strix could list repositories, obtain anonymous pull tokens, and download the actual image manifests and blobs. That included an image calledbaseten/baseten-app.

At this point, it would be easy to report an exposed registry and move on. But companies do intentionally publish images, and Strix never wants to report a false positive. The important question is what impact the images being exposed have.

Strix decided to pull an image and see what was inside. Here's that part of the run as it appears in Strix (yes, the agent's own writing sounds like AI, for obvious reasons):

Harbor Exposure Impact Review
Thinking

If those Harbor projects are not meant to be public, this is a real exposure, not metadata noise. The chain is what matters: enumerate public projects, read artifact metadata, mint an anonymousservice/tokenscoped torepository:baseten/baseten-app:pull, pull the manifest, then fetch the blob through a signed storage redirect. That proves real anonymous pull access. The way to make triage take it seriously is to prove one thing from a pulled image: proprietary code, internal binaries, hardcoded credentials, or internal hostnames.

The first promising hit was a pair of AWS keys inbaseten/baseten-app. Strix tried a read-onlysts:GetCallerIdentitycall, which tells you what account a credential belongs to. The response wasInvalidClientTokenId.

That key was dead, so Strix kept looking.

## Then, a token that actually worked

It pulled the layers, ranTruffleHog(shout out to our open-source security friends!), and inspected the image config directly. And there it was: a classic GitHub personal access token, sitting inhistory[].created_by.

I am not a Docker runtime expert, but luckily Strix is (thanks to it having pretty much all of human knowledge at its disposal). So it knew that that field records how a build step was created. In this case, it contained aRUNcommand with the value ofGITHUB_TOKENexpanded directly into it.

Strix used the token for a read-onlyGET /userrequest to GitHub and…VOILÀ.200, with the account namebasetenbot.

The token in the Docker build history, followed by GitHub identifying it as basetenbot. The credential is redacted.
 
Open image for full size.

Notice where the token was found. As I learned, a Docker image has filesystem layers, but it also has a config containing information about the image and its build history. That config is downloadable along with the image. Cleaning up a credential file doesn't help if the build history still contains another copy of the token.

And this one still worked more than three years later.

## Okay, what can basetenbot do?

A live token is interesting, but obviously the permissions matter. This token could have 0 permissions and thus 0 impact. So Strix checked the account and its organization membership. GitHub returnedX-OAuth-Scopes: repo, and the account belonged tobasetenlabs.

GitHub returned repo scope for basetenbot and listed basetenlabs as its organization.
 
Open image for full size.

Then it checked the individual repository permissions, again using read-only requests:

Repository
Access
basetenlabs/b***
admin: true
, 
push: true
basetenlabs/f***
admin: true
, 
push: true
basetenlabs/h***
admin: true
, 
push: true
basetenlabs/r***
Private, read/write
basetenlabs/b***
Private, read/write
basetenlabs/t***
Private, read/write
basetenlabs/b***
Private, read/write

This is an insane amount of access to leave in a publicly downloadable image.

At that point, we had enough to report and be confident this was not a false positive. We didn't clone the customer repo, push anything, or change any configuration. We stopped there and wrote the disclosure email immediately.

## How does a token end up there?

The build history was timestamped. The step containing the token ran onMarch 3, 2023. This was an old build credential that still had all of that access when we tested it in July 2026.

The underlying mistake is pretty familiar. A build needed to fetch private dependencies from GitHub, so somebody passed a token in as a build argument. The relevant pattern looked like this:

1
ARG
 GITHUB_TOKEN
2
RUN
 GITHUB_TOKEN=
${GITHUB_TOKEN}
 bash -c 
'\
3
 if [[ "${GITHUB_TOKEN}" != "" ]]; then \
4
 git config --global --add \
5
 url."https://${GITHUB_TOKEN}@github.com/".insteadOf "git@github.com:"; \
6
 fi'

I can see how someone ends up writing this. You need a private dependency, you pass in the token, Git authenticates, and the build works. But Docker can record that build argument in the image's metadata and history. In this case, it recorded the actual token value. Dockerexplicitly warns about this.

There is also a second problem with this pattern:git config --globalwrites the authenticated URL into Git's configuration file. Even if you change how the token gets into the build, you still need to avoid saving it into the image.

The fix is to use aBuildKit secret mountand temporary authentication that doesn't persist the credential. Then inspect both the image's layers and its history. And revoke the old token! Changing the Dockerfile doesn't do anything about an image that someone already downloaded.

## What Strix did on its own

Baseten has a responsive security team and alreadyuses AI security tooling. Still, this token from a 2023 build had admin access to their product and deployment repos when we found it.

It's easy to focus on the application and the source repositories, and forget about an old container image. Even if you scan the image's files, you still need to check its build history.

What I like about this scan is that Strix kept following the finding. It found a registry, checked whether it could actually pull an image, tested a credential and found it was dead, found another credential in the build history, and checked what that one could access.

We hadn't told it to look for Harbor or given it any hints about a token.It worked through the whole thing autonomously in about 25 minutes.

This is why we're building Strix. AI-powered attacks have been getting super scary in the past few weeks, and we believe the only way to defend yourself is to constantly be hacking yourself to find these issues (because there will always be issues) before the bad guys do.

## Disclosure

Baseten handled this well. The timeline was:

* July 13, 11:10 PM:I reported the livebasetenbottoken, the public Harbor project, and the repository permissions.
* July 14, morning:Baseten made the Harbor project private. I flagged that the token itself still worked.
* July 14, 4:34 PM:Anton from Baseten Security confirmed the issue as critical and said they had made the Harbor project private and rotated the token. He also asked us to securely delete the images we'd pulled.
* July 14, 5:05 PM:We confirmed deletion and sent over two lower-severity findings from the same scan.
* July 17:Baseten closed out the remaining findings.
* September:We let Baseten know we planned to disclose the finding publicly and sent them a draft of this post.

They also sent us some T-shirts and sweatshirts as a thank-you for finding this critical bug.

## Go check your old images

If you run containers and use GitHub, this is worth checking in your own infrastructure:

1. See what someone can pull without logging in, including old tags and projects you haven't thought about in a while.
2. Read the build history withdocker history --no-trunc, or inspect the config blob'shistory[].created_byfields. Check the layers too.
3. Get secrets out of build arguments. Use secret mounts, and make sure the commands consuming those secrets don't write them back into the image.
4. Check what your build tokens can actually do. Fetching a dependency needs read access to that dependency. Giving that token admin on your product and deployment repos makes a leak much worse. Limit the permissions and give it an expiry.

And run something like Strix against your own systems. This whole scan started because we wanted to use an inference provider. We gave it a domain and got back a critical vulnerability that Baseten could act on the next morning.

AI attackers can follow these same paths. If an agent can find a live admin token in an old image in 25 minutes, you want yours to find it first.

Try Strix →
 
Book a demo →
Copy link