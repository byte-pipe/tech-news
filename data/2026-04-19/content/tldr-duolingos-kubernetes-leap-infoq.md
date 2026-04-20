---
title: Duolingo's Kubernetes Leap - InfoQ
url: https://www.infoq.com/presentations/duolingo-eks-kubernetes/
site_name: tldr
content_file: tldr-duolingos-kubernetes-leap-infoq
fetched_at: '2026-04-19T19:41:00.618678'
original_url: https://www.infoq.com/presentations/duolingo-eks-kubernetes/
date: '2026-04-19'
description: Franka Passing explains Duolingo's migration from AWS ECS to EKS, discussing how they built a foundation with Argo CD and Karpenter to enable blue-green deployments for 128M+ active users.
tags:
- tldr
---

InfoQ HomepagePresentationsDuolingo's Kubernetes Leap

 DevOps


Shipping Faster, Breaking More: Rethinking Delivery Systems in the Age of AI (Webinar May 28th)

# Duolingo's Kubernetes Leap

View Presentation

* Vertical
* Horizontal
* Full

Speed:

* 1x
* 1.25x
* 1.5x
* 2x

Download

* Slides

43:06

## Summary

Franka Passing discusses the architectural shift of Duolingo’s 500+ backend services to Kubernetes. She explains the move toward GitOps with Argo CD, the transition to IPv6-only pods, and the "cellular architecture" used to isolate environments. She shares "reports from the trenches" on managing developer trust, navigating AWS rate limits, and productionizing early adopter services.

## Bio

Franka Passing is a Senior Platform Engineer at Duolingo. She has previously worked in platform and security engineering at organizations such as Mapbox, Klarna and others. She is a seasoned conference speaker and tech community organizer at the feminist Hackspace Heart of Code in Berlin.

## About the conference

InfoQ Dev Summit Munich software development conference focuses on the critical software challenges senior dev teams face today. Gain valuable real-world technical insights from 20+ senior software developers, connect with speakers and peers, and enjoy social events.

### INFOQ EVENTS

* May 12th, 2026, 1:30 PM EDT#### Designing Data Layers for Agentic AI: Patterns for State, Memory, and Coordination at ScalePresented by: Karthik Ranganathan - Co-CEO & Co-Founder at YugabyteDB, and Aditi Gupta - Snr. GenAI/ML Specialist Solutions Architect | GTM Data and AI at AWS

* May 21st, 2026, 12 PM EDT#### Portable by Design: Data Mobility & Recovery Patterns for Multi-Cloud SystemsPresented by: Liore Shai - Solutions Architect at Eon

* May 28th, 2026, 1 PM EDT#### Shipping Faster, Breaking More: Rethinking Delivery Systems in the Age of AIPresented by: Eric Minick - Sr. Director of DevOps Solutions at Harness, and Aaron Newcomb - Senior Product Marketing Manager at Harness

## Transcript

Franka Passing: I'm here to talk about Duolingo's Kubernetes leap. My name is Franka. I'm a senior platform engineer at Duolingo. I've been at Duolingo over just about three years now, and previously have worked in infrastructure, platform, and also security roles. For the last year at Duolingo, I've been working on this project that we're about to really dive into.

Duolingo is a language learning app. Duolingo's mission is to build the best education in the world and make it universally accessible. To give you an idea of the scale that we're looking at, Duolingo currently has over 128 million monthly active users, and we have over 250 courses that you can learn on the app. We have a lot of different languages going from Spanish, Navajo, Japanese. Actually, I've met a bunch of you on this conference already over the past year who told me they're learning Spanish on Duolingo, so that seems to be the popular language at InfoQ.

On the engineering side, we have over 400 engineers and more than 500 backend services, just to give you an idea of the scale of this migration that we're going to be looking at today. I already spoiled, used the word migration. I think that's the more boring, but the term that we're used to instead of Kubernetes leap. This is really the story of what I want to get into today. Firstly, why we migrated, building the foundation. We're going to look at concretely what does it look like for one of our services to be migrated onto the platform. This story is very much a report from the trenches. We are very much still in the middle of this migration. I thought about, is it too early to give a talk about it? Maybe it is. I thought there would still be some valuable lessons already just from the initial story of making this decision to migrate and the work that we've done over the past year to build out the foundation and migrate our early adopter services. That's what we're going to be looking at.

## The Decision to Migrate to K8s

Why did we make this decision to migrate to Kubernetes? As you all know, with any of these kinds of major infrastructure changes, there's a lot of cost investment that you're putting into it. You're investing a lot of time, engineering cost, infrastructure cost, and also training your users or product engineers to actually get familiar with the new platform. That's going to take them some time and it might even slow them down a little bit in their work. That's an additional cost. You want to be really clear on any of these, why you're making this decision, and be able to clearly communicate it to yourself and to your users. Why did we move to Kubernetes? To answer that question, it might help you to understand what we were doing before we made that choice.

Previously, the 500-plus backend services that I mentioned at the beginning are running on AWS ECS. We have some workloads that are running on different infrastructure, but for the mass majority, they're on ECS. That's what I'm going to be focusing on. We're going to be moving from ECS to EKS. ECS is AWS's container orchestration solution. It's a managed solution. It's very simple and straightforward to use. We've been actually super happy with ECS over the past year, and it served our needs very well. Now as we've grown to a much bigger scale, as I mentioned, Kubernetes just offers a much more feature-rich ecosystem and open-source platform, as well as specific features that ECS does not give us.

Kubernetes, obviously, has been the industry standard for container orchestration for the past decade. It's open source. It gives you multi-cloud support, so it makes it easier if there ever is interest in moving to a different cloud or standing up workloads in different environments. It's very feature-rich. This ecosystem here, obviously, we don't want to be using all of these tools and that would probably be a terrible idea, but there are a lot of open-source tools such as Argo CD, Karpenter, just to name a few that fit very specific needs that we found we have. It's still a managed service, so I'm going to be using EKS and Kubernetes interchangeably throughout the presentation since we opted to use AWS's managed Kubernetes offering on their platform.

## The Migration Taskforce

Before we got into what the actual migration work looked like, I just want to give you an idea of the team that was working on this so that you have an idea of how many people, of those 500 engineers, is it a 100 people team? Obviously not. We were six or seven people over the past year, made of one PM, a technical lead, two platform engineers, I'm one of them. Then we had a cast of rotating representatives from other platform teams such as observability, security, CI/CD, depending on what kind of topic was interesting at the time and what they could help us with, integrate into their existing platforms. When I talk about product or the customers of this platform, I'm talking about the 30-plus product engineering teams we have that own those 500 backend services. These are really the users or customers of our platform. As you know, they're working on product, they're trying to ship the app, but those are our customers for the new platform. Speaking of the product teams, this is actually a slide that we shared with them last year to get them on board as we started doing the advocacy work of what the new platform would look like. It's also been our guiding light throughout the migrations.

Firstly, we will do most of the work. Obviously, the product teams are still responsible for managing, operating their services, but we really wanted to be able to take away most of this migration workflows for them and also be able to therefore ensure that it happens in a timely manner. If that means building really great documentation, building automation tools, building the things they need to actually migrate, that's what we'll do. VIP support, so for every service that's being migrated, there's going to be a partner from our EKS team that's going to be partnering with that service team to help them answer questions, give experiences, or even do some of the grunt work throughout the migration.

Finally, product has control. We really wanted to reassure product teams that we would be happy to work with their timelines on these migrations. We wanted to target those people who are really excited and wanted to migrate first, first, and then give those who have specific deadlines or who don't currently have the space to do this because they're working on a specific feature, give them the option to migrate at a later time.

## Project Phases

There are three major phases that the project has been in so far to bring us to today. Those are the three phases that I'm going to be looking at throughout this talk. The first phase, the second half of 2024, that's when we built the foundation of the project. This means spinning up all of the initial tooling, deployment tooling, observability, actually standing up some clusters and starting to test those clusters with our test services. The second phase, which was at the first half of this year, was basically productionizing and sending up our early adopter services on those existing clusters. Part three, there's obviously further parts that will come here as we go into general adoption, but currently at the moment, we are working on migrating our most critical services and further automating those migration rollouts.

## Phase 1 - Building the Foundation Clusters, Ready for Prod (B/G Deploys)

First, I want to talk about building the foundation of the platform. Obviously, when I say this took six months, from the second half of last year, there was time before that that folks spent to actually research what tools we wanted to use, do some prototyping and also do advocacy within the organization to propose that we want to do this decision. That's the shadow phase that is not captured here, but that's the thing with any bigger project. Let's jump into our foundation. When we were looking at our platform before the migration, one of the bigger issues we were seeing with our existing platforms was basically deployments. With our lot of services, people were seeing issues with slow deployments and also issues with stage environments, where we had static stage environments that were not available to use when you needed them. These are our two North Star features for the Kubernetes migration that we wanted to achieve and have shipped with Argo CD.

Firstly, blue-green deployments. Blue-green deployments, it's basically, you're able to stand up a new version of your service, send traffic to that new deployment and observe metrics such as latency, error rates, and so on, and then casually switch over to serve full traffic on that feature. Ephemeral dev deployments, another feature, is the ability to stand up an ephemeral deployment or an ephemeral environment. For example, you make a PR, you push a button, and then you get a full service from that PR stood up, which later can be cleaned up after your PR is merged. That especially was a highly requested feature because we were seeing developers, even with this service which already has 10 stage environments, which is a lot, still being stuck on that. You might say ECS has blue-green deployments. It does actually have blue-green deployments now, but still Argo CD gives us more flexibility.

I mentioned before, we decided to use Argo CD for our deployment agent. It's a declarative tool that uses GitOps. Basically, what that means is the configuration that is in GitHub or in your Git, whatever Git you're using, is the thing that will be applied into your actual environment. As a team who has been using things like infrastructure as code for a long time, this made a lot of sense for us. We really wanted to be able to use that. Also, Argo CD offers these custom, flexible deployment strategies. We've mentioned blue-green deployments, but we also have the option to use rolling updates, which is the default on ECS, as well as more custom things like phased canary, where you send canary traffic to a specific service for a while, and other options. We leverage the GitOps bridge, which is the component that syncs from GitHub into the actual Argo CD deployment.

Blue-green rollouts, as I said, this was one of the most requested features and one of the things we wanted to get right from the beginning. This was actually very straightforward to set up with Argo CD. It's been very cool to see that you can analyze these rollouts on custom metrics. For a lot of the services, they use the default, which is latency and 5xx. You can then pause or proceed with deployment. Also, Argo CD, we have set it up to post notifications to Slack on the deployment. Although we previously on ECS had canary services, where developers had the option to deploy to a canary service and then roll back, oftentimes the canary, which was hardcoded to receive only 1% of traffic, was not enough to actually show any symptoms, such as latencies or error rates. Here you also have the advantage that previously you would deploy to a canary deployment and then a human would need to look at the dashboard and make that call of whether the latency looks a little bit higher, but maybe it's a Java service, it's going to come down once it warms up. Here you actually have those checks in the platform automated, so you can also go away and Argo CD will manage that rollout for you.

Cellular architecture. This is another design decision that we made on our Argo CD deployment. In Markus' talk about AWS's sovereign cloud, he talked a lot about AWS partitions. This is a little bit what inspired this idea. Essentially, we have tenants for our Kubernetes deployments that contain multiple clusters, but each tenant is an isolated environment. In each tenant — this is a little bit complicated to understand at first, also took me a while to wrap my head around it — we have different environments, so dev, stage, and prod.

What this gives us is the flexibility to really roll out changes to a specific tenant or one cell, as it could be called as well, without impacting the other services in production. This also means that we're able to test changes to the platform without ever impacting our actual customers, as in the product engineers. They might have what they see as dev and stage clusters in our Duolingo main tenant, but from our perspective as the platform owners, all the actual code that gets pushed to that main tenant has already been tested in our separate EKS dev and stage environments or tenants where the product developers don't have access to.

Another thing, related to this, but just took us a while to figure out was, when you have Argo CD, how do you actually set up the repository? We landed on this structure. The interesting part is the tenants thing in the middle, where basically you have the service manifests split up by tenants and by services, by environments. This gives you the ability to set default values. For example, all services in the stage tenant have less memory or whatever defaults that you want to set there.

Stepping away from Argo CD and deployments, we had that set up. We had our clusters. Technically this comes first, but as you're setting up the foundation, you also need to build out the network architecture. Networking is always challenging, especially when you build out a totally new platform, you also have the ability to make changes that you might not be able to do in your existing environment. We decided to use IPv6 for our Kubernetes pods. This was for multiple reasons. First of all, IPv6 is the future, and we had the chance here to basically bring our platform to a more future-proof setup by enabling IPv6 on the clusters from the get-go. At the same time, with our scale and our existing network infrastructure, continuing with IPv4, there might have been concerns of running out of IPv4 addresses, especially with Kubernetes, where each pod gets assigned the IP address, and IPv6 would make sure we do not run into that issue.

Once we made that decision, what this means is that every pod has an IPv6 address. However, our VPC, we needed to be dual-stack since we still want to be able to make connections to IPv4 hosts, and specifically also talk to services in our old infrastructure, which was IPv4-based. We made a dual-stack VPC, which basically means the VPC supports both address schemes. There we were able to leverage the AWS VPC CNI plugin. That is great. I'm really glad that we were able to leverage IPv6, but we also ran into some challenges with the setup. First of all, application updates. As I mentioned at the very beginning, we're moving from one container orchestration platform to another container orchestration platform.

In an ideal world, you might think that you're able to take your existing container from ECS, lift it, shift it, and just put it on EKS. Up until now, this was exactly the case. We were able to use our existing Docker containers and deploy them onto EKS. IPv6 changed this. This was the first change where we actually needed to make code-level changes so that the services could run on Kubernetes. This is because a lot of the web services frameworks that we were using, you actually need to configure it to allow IPv6 connections coming into the service.

For example, on your Python Flask app or your Java whatever app, you need to actually go into the configuration and say, update the address screen to allow incoming IPv6 connections. It's not a big deal, but it did add some complexity because, like I said, suddenly we're actually changing application code as well. This is in every single repo that we're touching. NAT costs was another issue. If you've worked with managed NAT gateways on AWS, you know that they can be expensive. We were hoping to get around this issue with IPv6 because egress traffic on IPv6 is actually free going through an egress-only internet gateway.

However, we found that some of our services actually call back to a lot of IPv4-only hosts. We ended up still being charged more for NAT costs. Finally, IPv6 support on AWS services and also on just public services at this current point in time is not where we would like it to be. We were a little bit blind going into this, assuming that IPv6 is more supported than it is. We found that a lot of, for example, AWS services do not yet offer IPv6 endpoints. It is changing. Actually, just two weeks ago, they announced that DynamoDB now offers IPv6, which is a big win for us. This is still work in progress.

Another big topic as you build out a new platform foundation is observability. This was really important to us from the beginning because even with our very first adopter service, we wanted to make sure that service owners had all the metrics and traces and just all the information they can to be able to be confident that their service is performing well on the new platform. We use a variety of tools, Honeycomb for traces, Sentry for bug tracking, PagerDuty for alarms, and various AWS integrations such as CloudWatch. We had to build out integrations with all of these tools to be able to work on Kubernetes. This was done with the help of our observability team, which joined the rotation for a while.

Some of the challenges we ran into with observability, the first one was, I got a page, is it from ECS or from EKS? As I'll share later, for most of the services that are being migrated, there's a period of time where some percentage of traffic is going to ECS and some percentage of traffic is going to EKS. It was not immediately clear, which was not an issue we expected, when a user would get paged, that they would know, this is from the new EKS service versus this is from the old service. There was a little bit of confusion that we initially introduced to our users about this.

One thing that helped there was just to add identifying tags and attributes that this is coming from Kubernetes, this is coming from this prod cluster, just to give folks more information. For example, here in the corner, you can see we added the Kubernetes cluster name tag to our Honeycomb traces. Another challenge was just to maintain the interfaces developers were already used to, while shipping new features. Some alarms made more sense on EKS or on ECS. There was a constant balance that we wanted to take of taking advantage of the new platform and adjusting alarms in a way that makes sense on the new platform, while not introducing any unnecessary friction or change to the developers that causes more confusion.

Service templates. Another thing that we focused on in this initial building the foundation stage is basically make right templates that make it more easy for us to continue shipping more services as we go on. There were two types of templates that we worked with. Firstly, Helm charts. Helm charts are basically a way to write Kubernetes manifests, but being able to use features like templating so you can set default values for services. We built two different Helm charts. They're based on the same default, but they have some different settings. One is just a web service and another one is a worker, which is very similar to a web service, but does not have an HTTP ingress. We also use KEDA for queue-based scheduling on the worker so that you're able to deploy a worker who can read messages from a queue and scale based on the messages in that queue. Those Helm charts were what on ECS we were using Terraform modules for. On ECS, we had Terraform modules that will let you configure things like memory, CPU, and the other attributes on a service.

All of that configuration now moved into the Helm charts. That is a new technology we had to get used to. That said, we still had some Terraform for our EKS services that we needed to create as well. This was mainly to manage interaction with AWS permissions. For example, if you have a bunch of databases, some S3 buckets in your AWS role, we still needed to be able to give permission specific to that service, and that part is being done in Terraform. We do leverage EKS Pod Identity for access management, and those roles are being created in Terraform. The Terraform also syncs environment variables and secrets. One tip that I can give from this initial building the foundation phase is to lean on the provider support.

In our case, AWS were very helpful since we were moving from one of their products to another product. Obviously, depending on your relationship or support level you're on. In our case, we were able to get workshops from them before we started going on this journey, just to get everyone on the same page, get some training for the team. The best practices documentation has been really helpful. Then we also have monthly check-ins with our account managers to be able to make sure we're on the right track and ask them specific questions about some of the networking stuff, for example.

## Phase 2 - Productionizing Pilot Services, Migration Testing, and Iteration

Now we have our foundation, we have our Argo CD clusters, platforms, and we have a couple of test services deployed onto those clusters. Now we're going to move into the next phase, which coincided around the start of this year, where we actually start deploying pilot services to the platform, do migration testing. Of course, also continue iterating on the platform. I want to talk you through what does it look like for one of our backend services, step-by-step, to actually go from being on ECS to be deployed on EKS. I call this service owl-service. It's not its real name, but let's go with it. I want to introduce owl-service to you. How did we pick this service?

First of all, partner teams. We have one of our teams, the core architecture team, that is close. It's one of our sister teams. We partnered with them to basically ask them if they're interested in being some of our early adopters and start deploying their services on EKS. Luckily, they were very interested. We basically sat down with this team and said, of your services, let's go through the list and see which is a handful of services that we want to migrate early on, which are some that we want to do later on. Owl-service was the second production service that we deployed on EKS. The first service was a Java service.

Now, with owl-service, we wanted a Python service to be able to make sure that with our early adopter services, we're covering already a wide range of languages and platforms, and so we get a better feel for how different services are doing on the platform. It was medium critically, so it doesn't take down the app if it goes down, but it does impact our users, whereas our very first production service was non-critical. We just wanted to have a safe choice. With this service, we wanted to give us a bit more of a challenge and also get more information again.

Now that we have our owl-service, we're actually going to deploy it. As I mentioned before, we still have some Terraform that we're actually using. At Duolingo, we have our platform teams that maintain a library of shared Terraform modules. For almost any resource that you would want to stand up on AWS, we have a module that you can use to do that. We basically created a new EKS service module that, like I said, mainly manages AWS permissions. This is very stripped down from our previous ECS module, where that module contained practically the whole ECS service. There's also a separate module that we created for observability, and that creates some of the default alarms, as well as dashboards and log groups and so on. You can see here, as inputs, it just takes the environment that you want to deploy it on, product, service. These are used for tags. We use default tags on Terraform, and some environment variables.

Once we have the Terraform in place, the next step, as I mentioned, is the Argo CD manifest. This is a new concept for us in the Kubernetes world, where you basically have this manifest file that defines what service looks like, what resources it requires, and so on. Previously, that was managed in Terraform, now this information has moved into this manifest file. This is the actual manifest file for the owl-service. I just blacked out the ECR repository. Basically, you can configure memory, CPU, and so on. This is also based on a Duolingo service Helm chart, so there are also defaults for all of those values.

Additionally, to the memory and CPU reservations, you also define scaling behavior and those deployment strategies that I mentioned earlier. Argo CD, do you want to use a blue-green deployment? Do you want to use a rolling update? That would be defined in this file as well. Additionally, to these actual files, which contain the actual configuration, we're also later on building automation on top of these files so that developers don't need to actually go in and edit this file in GitHub, but can use a job to say, I want to scale my service to a higher number, and so on.

Once we have Terraform and the Argo CD part, we basically have a service running on Kubernetes, if everything went well, which is great news. At that point, we basically do service validation. With the help of the actual owning teams who know their service best, we go in and check what the health of the service is. This is also where our observability metrics come in handy. Looking at metrics, traces, logs, we're able to just see how the service is running. Is it heavy on the platform? We can also do things like just checking the routes and comparing the responses to the still-running ECS service. You could just, for example, curl or send some requests to both services with the same parameters, compare the responses, which hopefully are the same. You can also do some basic load testing. This we focused on more in the beginning when we were still less confident with the platform, but just send some load to the service, see how it behaves, how the scaling behavior is done.

The service validation was quite a manual process at the beginning, but as we migrate more services, this has become more automated. After we've done the actual validation, which, like I said, kind of a manual thing, we can move into canary testing. For canary testing, what we did is just to send a small percent of production traffic to that service over first a short period of time and later longer. It might be starting with 10 minutes, observing metrics, maybe an hour, maybe a day. We would monitor service health over that day. During that time, we would also compare the latency, error rates, again, to the ECS service. This was really helpful this whole time that we had the ECS service almost as a control value to compare to. For example, here you can see this service failed its canary test because it had quite high latency and 4xx ELB errors. We had to stop canary testing, go back, fix some issues, and then redeploy the service.

How did we control the rollout? We actually used weighted DNS records to send traffic to the new services. This gave us the flexibility to just send a number of traffic to the new services at any point and also to revert if needed. One of the challenges that we ran into was that DNS can be slow. If you're going to revert really quickly, it might not be the right choice. Although we did find that we were able to stop DNS caching by redeploying upstream services and to clear those caches.

In general, the weighted routing has worked really well for us. We've also been able to observe service behavior over a longer period using the strategy. Letting the service sit at 50-50% traffic, for example, so you can observe how memory behaves after two or three days, and so on. A service for us is completed for now if it's running 99% of its traffic on EKS. We actually decided to keep the ECS services running for a bit longer while we still finish building the platform to give us the option to revert back to ECS if needed. We still wanted to keep those ECS services warm and also being deployed to, so we would deploy to both services in parallel.

I talked a lot about what the technical preparation looks like during this process of migrating one service. Obviously, there's also a human aspect. As I mentioned for these early adopter services, we worked with one of our sister teams. We worked pretty closely to make sure that they are up to speed on the platform. Specifically, we did training with this team. We talked them through the platform. Also kept them in the loop as the migration process was going. We created some documentation and runbooks with checklists that were being updated as we went, so that everyone could see what the current status of the migration was. Of course, there were also some challenges in this phase, or in the phase that we're still now where we're going from early adopters to general adopters.

One of those challenges, I call it recency bias. It's basically this bias where something new comes in and then you blame every issue on the new thing. Something is wrong with my service, it must be because it's on Kubernetes. This kind of thinking can lead to paper cuts which can really add up and erode trust in the new platform. Obviously, out of 10 times it could be that one or two times that the issue is actually related to the new platform. Also, oftentimes, it might just be because someone shipped bad code or there's an upstream vendor issue going on, and so on. What has helped there is really, again, focusing on observability tools.

If you have the observability tools in place to say, no, we can actually see this issue is coming from this other problem, that's really helpful. Training, again, like I said, to make sure that people are actually used to the new platform. Even in the case of an incident, remember where to go for the new dashboards, where to see the documentation, and so on. Communication, and I actually really liked in the Skyscanner talk where they said, show, don't tell. This is also something that we've been doing, even if the issue ends up not being related to our platform, but we got paged, still jump in and help the team with whatever incident they have going on. Just showing presence and helping them build that confidence on the new platform.

Another challenge that we've run into is rate limits. As we slowly add more services, I feel like we are constantly discovering new rate limits, which can be frustrating, but it is what it is. The EKS Pod Identity agent API was one where we got rate limiting, where pods failed to assume the EKS Pod Identity role. Then recently we also had an issue where we got rate limiting from the AMP, the managed Prometheus platform on AWS. It's been really interesting to see with these limits as we roll out services that, for example, with the Prometheus issue, we had a service rolled out to 50% for a couple of days. It was going fine. We rolled it out to 70%.

At our scale, suddenly just that percentage change was enough to hit those rate limits. What worked there was actually doing the slow rollout so we can see those issues early when they come in. Then, easily revertible, so being able to roll back the traffic if we need to, so that we can adjust the limit in the meantime.

Another thing that's helping here is migrate large scale services sooner than later. Now as we finish this early adopter phase, we're actually focused on the 10 most critical services that we run on the platform. The most critical are also the most scaled services. Migrating those early is helping us to find all of those little rate limits. Escalation, so what I mentioned earlier about working closely with AWS, keeping them in the loop on our migration, has also helped with these kinds of rate limits when they come from AWS, so that our TAMs are in the know about where we are in the migration and are able to have the right context and pass that on so we can be helped with our rate limit.

## Phase 3 - Beyond Kubernetes, the Steady-State Platform

We're still in the early or early to mid-phases. Maybe I'll be back to tell you how general adoption went. Beyond Kubernetes is our steady-state platform. One of the big wins we hit this quarter was, all new services that are created are on EKS from the start. That's a really good stopgap to make sure you're not going backwards in your migration effort.

## Recap

We talked about the why and having strong reasons for this migration. Only start a project like this if you have a strong need from your users or your customers, in our case the product who really wanted those deployment strategies. Building a strong foundation, so focusing on observability, security, and those deployment features really early on helped us to build a strong foundation that we're now still iterating on. Migration stories, so finding those early adopters who are very excited actually about Kubernetes and about being some of the first services on the platform, and then iterating our migration process as we go has been really helpful as well.

## Questions and Answers

Participant 1: One question is regarding the reasons, again, you mentioned that you were quite happy with ECS, but then eventually decided to start this migration. If you could name top two or three maybe technical reasons for this migration. Also, second question would be regarding distributed tracing, how you manage it or did it on ECS, for example, through X-Ray or somehow in a different way, and then how you handle it during this migration phase.

Franka Passing: The first question about the why. ECS was great for us in terms of a more simple, more managed platform, but we really wanted to take advantage of the richer ecosystem, for example, with Karpenter. We're heavy users of Spot on AWS as well, and Karpenter makes that much easier. Then the more custom deployment features on Argo CD was another really strong reason as we were seeing some deployment issues on ECS. Just from the technical features, I think those are the top two.

Then the other question about tracing. I'm not super deep into the observability stack, but we use OTel Collectors running on both our ECS and EKS infrastructures that goes into Prometheus. Then from there, we give our users access to Honeycomb to actually be able to look at those traces and use them for analyzing their issues.

 

See morepresentations with transcripts

 

Recorded at:

Apr 06, 2026

by

* Franka Passing

#### This content is in theDevOpstopic

##### Related Topics:

* DevOps
* InfoQ Dev Summit Munich 2025
* InfoQ Dev Summit
* Kubernetes
* Transcripts
* Containers
* QCon Software Development Conference
* Case Study
* Cloud Computing
* InfoQ

* #### Related Editorial
* #### Popular across InfoQ##### Anthropic Releases Claude Mythos Preview with Cybersecurity Capabilities but Withholds Public Access##### Anthropic Introduces Agent-Based Code Review for Claude Code##### Claude Code Used to Find Remotely Exploitable Linux Kernel Vulnerability Hidden for 23 Years##### Java News Roundup: JDK 27 Release Schedule, Hibernate, LangChain4j, Keycloak, Helidon, Junie CLI##### Cloudflare Launches Code Mode MCP Server to Optimize Token Usage for AI Agents##### How SBOMs and Engineering Discipline Can Help You Avoid Trivy’s Compromise
* ##### Anthropic Releases Claude Mythos Preview with Cybersecurity Capabilities but Withholds Public Access
* ##### Anthropic Introduces Agent-Based Code Review for Claude Code
* ##### Claude Code Used to Find Remotely Exploitable Linux Kernel Vulnerability Hidden for 23 Years
* ##### Java News Roundup: JDK 27 Release Schedule, Hibernate, LangChain4j, Keycloak, Helidon, Junie CLI
* ##### Cloudflare Launches Code Mode MCP Server to Optimize Token Usage for AI Agents
* ##### How SBOMs and Engineering Discipline Can Help You Avoid Trivy’s Compromise
