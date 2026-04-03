---
title: (Almost) Every infrastructure decision I endorse or regret after 4 years running infrastructure at a startup · Jack's home on the web
url: https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/
site_name: hnrss
content_file: hnrss-almost-every-infrastructure-decision-i-endorse-or
fetched_at: '2026-02-20T11:15:16.999267'
original_url: https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/
author: Jack Lindamood
date: '2026-02-17'
published_date: '2024-02-01T13:59:47-08:00'
description: Assortment of technology startup infrastructure recommendations
tags:
- hackernews
- hnrss
---

Image from UnSplash

I’ve led infrastructure at astartupfor the past 4 years that has had
to scale quickly. From the beginning I made some core decisions that the
company has had to stick to, for better or worse, these past four years. This post
will list some of the major decisions made and if I endorse them for your
startup, or if I regret them and advise you to pick something else.

## AWSLink to heading

### Picking AWS over Google CloudLink to heading

🟩Endorse

Early on, we were using both GCP and AWS. During that time, I had
no idea who my “account manager” was for Google Cloud, while at the same
time I had regular cadence meetings with our AWS account manager. There is a feel
that Google lives on robots and automation, while Amazon lives with a customer focus.
This support has helped us when evaluating new AWS services. Besides support, AWS has done a great job around stability
and minimizing backwards incompatible API changes.

There was a time when Google Cloud was the choice for Kubernetes clusters, especially
when there was ambiguity around if AWS would invest in EKS overECS. Now though, with
all the extra Kubernetes integrations around AWS services (external-dns, external-secrets, etc),
this is not much of any issue anymore.

### EKSLink to heading

🟩Endorse

Unless you’re penny-pinching (and your time is free), there’s no reason to run your own
control plane rather than use EKS. The main advantage of using an alternative in AWS, like ECS,
is the deep integration into AWS services. Luckily, Kubernetes has caught up in many ways: for example,
using external-dns to integrate with Route53.

### EKSmanaged addonsLink to heading

🟧Regret

We started with EKS managed addons because I thought it was the “right” way to use EKS. Unfortunately, we always
ran into a situation where we needed to customize the installation itself. Maybe the CPU requests, the image tag,
or some configmap. We’ve since switched to using helm charts for what were add-ons and things are running much better
with promotions that fit similar to our existing GitOps pipelines.

### RDSLink to heading

🟩Endorse

Data is the most critical part of your infrastructure. You lose your network: that’s downtime. You
lose your data: that’s a company ending event. The markup cost of using RDS (or any managed database)
is worth it.

### Redis ElastiCacheLink to heading

🟩Endorse

Redis has worked very well as a cache and general use product. It’s fast, the API is simple and
well documented, and the implementation is battle tested. Unlike other cache options, like
Memcached, Redis has a lot of features that make it useful for more than just caching. It’s a
great swiss army knife of “do fast data thing”.

Part of me is unsure what the state of Redis is for Cloud Providers, but I feel it’s so widely used by AWS customers
that AWS will continue to support it well.

### ECRLink to heading

🟩Endorse

We originally hosted onquay.io. It was a hot mess of stability problems. Since moving to ECR,
things have been much more stable. The deeper permission integrations with EKS nodes or dev servers has also been a
big plus.

### AWS VPNLink to heading

🟩Endorse

There are Zero Trust VPN alternatives from companies like CloudFlare. I’m sure these products work
well, but a VPN is just so dead simple to setup and understand (“simplicity is preferable” is my mantra). We use
Okta to manage our VPN access and it’s been a great experience.

### AWSpremium supportLink to heading

🟧Regret

It’s super expensive: almost (if not more) than the cost of another engineer. I think if we had very little
in house knowledge of AWS, it would be worth it.

### Control Tower Account Factory for TerraformLink to heading

🟩Endorse

Before integrating AFT, using control tower was a pain mostly because it was very difficult to automate. We’ve since
integrated AFT into our stack and spinning up accounts has worked well since. Another thing AFT makes easier is
standardizing tags for our accounts. For example, our production accounts have a tag that we can then use to make
peering decisions. Tags work better than organizations for us because the decision of “what properties describe
this account” isn’t always a tree structure.

## ProcessLink to heading

### Automating post-mortem process with a slack botLink to heading

🟩Endorse

Everyone is busy. It can feel like you’re the “bad guy” reminding people to fill out the post-mortem. Making a robot
be the bad guy had been great. It streamlines the process by nudging people to follow the SEV and post-mortem procedure.

It doesn’t have to be too complex to start. Just the basics of “It’s been an hour of no messages. Someone post an update” or
“It’s been a day with no calendar invite. Someone schedule the post-mortem meeting” can go a long ways.

## Using pager duty’s incidenttemplatesLink to heading

🟩Endorse

Why reinvent the wheel? PagerDuty publishes a template of what to do during an incident. We’ve customized it a bit,
which is where the flexibility of Notion comes in handy, but it’s been a great starting point.

### Reviewing pager duty tickets on a regular cadenceLink to heading

🟩Endorse

Alerting for a company goes like this:

1. There are no alerts at all. We need alerts.
2. We have alerts. There are too many alerts, so we ignore them.
3. We’ve prioritized the alerts. Now only the critical ones wake me up.
4. We ignore the non-critical alerts.

We have a two tiered alerting setup: critical and non-critical. Critical alerts wake people up. Non-critical alerts
are expected to ping the on-call async (email). The problem is that non-critical alerts are often ignored. To resolve
this, we have regular (usually every 2 weeks) PagerDuty review meetings where we go over all our alerts. For the critical
alerts, we discuss if it should stay critical. Then, we iterate the non-critical alerts (usually picking a few each meeting)
and discuss what we can do to clear those out as well (usually tweaking the threshold or creating some automation).

### Monthly cost tracking meetingsLink to heading

🟩Endorse

Early on, I set up a monthly meeting to go over all of our SaaS cost (AWS, DataDog, etc). Previously, this was just
something reviewed from a finance perspective, but it’s hard for them to answer general questions around “does this cost
number seem right”. During these meetings, usually attended by both finance and engineering, we go over every software
related bill we get and do a gut check of “does this cost sound right”. We dive into the numbers of each of the high bills
and try to break them down.

For example, with AWS we group items by tag and separate them by account. These two dimensions, combined with the general
service name (EC2, RDS, etc) gives us a good idea of where the major cost drivers are. Some things we do with this data
are go deeper into spot instance usage or which accounts contribute to networking costs the most. But don’t stop at
just AWS: go into all the major spend sinks your company has.

### Managing post mortems in datadog or pager dutyLink to heading

🟥Regret

Everyone should do post-mortems. BothDataDogand PagerDuty have integrations to manage writing post-mortems and we tried
each.
Unfortunately, they both make it hard to customize the post-mortem process. Given how powerful wiki-ish tools
like Notion are, I think it’s better to use a tool like that to manage post-mortems.

### Not using Function as a Service(FaaS) moreLink to heading

🟥Regret

There are no great FaaS options for running GPU workloads, which is why we could never go fully FaaS. However,
many CPU workloads could be FaaS (lambda, etc). The biggest counter-point people bring up is the cost. They’ll
say something like “This EC2 instance type running 24/7 at full load is way less expensive than a Lambda running”.
This is true, but it’s also a false comparison. Nobody runs a service at 100% CPU utilization and
moves on with their life. It’s always on some scaler that says “Never reach 100%. At 70% scale up another”. And it’s
always unclear when to scale back down, instead it’s a heuristic of “If we’ve been at 10% for 10 minutes, scale down”.
Then, people assume spot instances when they aren’t always on market.

Another hidden benefit of Lambda is that it’s very easy to track costs with high accuracy. When deploying services
in Kubernetes, cost can get hidden behind other per node objects or other services running on the same node.

### GitOpsLink to heading

🟩Endorse

GitOps has so far scaled pretty well and we use it for many parts of our infrastructure: services,
terraform, and config to name a few. The main downside is that pipeline oriented workflows give
a clear picture of “here is the box that means you did a commit and here are arrows that go from
that box to the end of the pipeline”. With GitOps we’ve had to invest in tooling to help people answer
questions like “I did a commit: why isn’t it deployed yet”.

Even still, the flexibility of GitOps has been a huge win and I strongly recommend it for your company.

### Prioritizing team efficiency over external demandsLink to heading

🟩Endorse

Most likely, your company is not selling the infrastructure itself, but another product. This puts pressure on the
team to deliver features and not scale your own workload. But just like airplanes tell you to put your own mask on
first, you need to make sure your team is efficient. With rare exception, I have never regretted prioritizing
taking time to write some automation or documentation.

### Multiple applications sharing a databaseLink to heading

🟥Regret

Like most tech debt, we didn’tmakethis decision, we just did notnotmake this decision. Eventually, someone
wants the product to do a new thing and makes a new table. This feels good because there are now foreign keys between
the two tables. But sinceeverythingis owned bysomeoneand thatsomeoneis a row in a table, you’ve got
foreign keys between all objects in the entire stack.

Since the database is used byeveryone, it becomes cared for byno one. Startups don’t have the luxury of a DBA,
and everything owned byno oneis owned byinfrastructureeventually.

The biggest problem with a shared database are:

* Crud accumulates in the database, and it’s unclear if it can be deleted.
* When there are performance issues, infrastructure (without deep product knowledge) has to debug the database and figure out who to redirect to
* Database users can push bad code that does bad things to the database. These bad things may PagerDuty alert the
infrastructure team (since they own the database). It feels bad to wake up one team for another team’s issue. With application owned databases,
the application team is the first responder.

All that said, I’m not against stacks that want to share a single database either. Just be aware of the tradeoffs above
and have a good story for how you’ll manage them.

## SaaSLink to heading

### Not adopting an identity platform early onLink to heading

🟥Regret

I stuck with Google Workspace at the start, using it to create groups for employees as a way to assign permissions. It just isn’t flexible enough.
In retrospect, I wish we had picked upOktamuch sooner. It’s worked very well, has integrations for almost everything,
and solves a lot of compliance/security aspects. Just lean into an identity solution early on and only accept SaaS
vendors that integrate with it.

### NotionLink to heading

🟩Endorse

Every company needs a place to put documentation. Notion has been a great choice and worked much easier than things
I’ve used in the past (Wikis, Google Docs, Confluence, etc). Their Database concept for page organization has also
allowed me to create pretty sophisticated organizations of pages.

### SlackLink to heading

🟩Endorse

Thank god I don’t have to use HipChat anymore. Slack is great as a default communication tool, but to reduce stress
and noise I recommend:

* Using threads to condense communication
* Communicating expectations that people may not respond quickly to messages
* Discourage private messages and encourage public channels.

### Moving offJIRAontolinearLink to heading

🟩Endorse

Not even close. JIRA is so bloated I’m worried running it in an AI company it would just turn fully sentient. When
I’m using Linear, I will often think “I wonder if I can do X” and then I’ll try and I can!

### Not usingTerraform CloudLink to heading

🟩No Regrets

Early on, I tried to migrate our terraform to Terraform Cloud. The biggest downside was that I couldn’t justify the
cost. I’ve since moved us toAtlantis, and it has worked well enough. Where atlantis
falls short, we’ve written a bit of automation in our CI/CD pipelines to make up for it.

### GitHub actionsfor CI/CDLink to heading

🟧Endorse-ish

We, like most companies, host our code on GitHub. While originally using CircleCI, we’ve switched
to Github actions for CI/CD. The marketplace of actions available to use for your workflows is
large and the syntax is easy to read. The main downside of Github actions is their support
for self-hosted workflows is very limited. We’re using EKS andactions-runner-controllerfor our self-hosted runners
hosted in EKS, but the integration is often buggy (but nothing we cannot work around).
I hope GitHub takes Kuberentes self-hosting more seriously in the future.

### DatadogLink to heading

🟥Regret

Datadog is a great product, but it’s expensive. More than just expensive, I’m worried
their cost model is especially bad for Kubernetes clusters and for AI companies. Kubernetes
clusters are most cost-effective when you can rapidly spin up and down many nodes, as well
as use spot instances. Datadog’s pricing model is based on the number of instances you
have and that means even if we have no more than 10 instances up at once, if we spin up
and down 20 instances in that hour, we pay for 20 instances. Similarly, AI companies
tend to use GPUs heavily. While a CPU node could have dozens of services running at once,
spreading the per node Datadog cost between many use cases, a GPU node is likely to have
only one service using it, making the perserviceDatadog cost much higher.

### PagerdutyLink to heading

🟩Endorse

Pagerduty is a great product and well priced. We’ve never regretted picking it.

## SoftwareLink to heading

### Schema migration by DiffLink to heading

🟧Endorse-ish

Schema management is hard no matter how you do it, mostly because of how scary it is. Data is important and a bad
schema migration can delete data. Of all the scary ways to solve this hard problem, I’ve been very happy with the idea
of checking in the entire schema into git and then using atoolto generate
the SQL to sync the database to the schema.

## Ubuntu for dev serversLink to heading

🟩Endorse

Originally I tried making the dev servers the same base OS that our Kubernetes nodes ran on, thinking this would make
the development environment closer to prod. In retrospect, the effort isn’t worth it. I’m happy we are sticking
with Ubuntu for development servers. It’s a well-supported OS and has most of the packages we need.

### AppSmithLink to heading

🟩Endorse

We frequently need to automate some process for an internal engineer: restart/promote/diagnose/etc. It’s easy enough
for us to make APIs to solve these problems, but it’s a bit annoying debugging someone’s specific installation of a
CLI/os/dependencies/etc. Being able to make a simple UI for engineers to interact with our scripts is very useful.

We self-host our AppSmith. It works … well enough. Of course there are things we would change, but it is enough
for the “free” price point. I originally explored deeper integration withretool, but I couldn’t justify the price
point for what, at the time, was just a few integrations.

### helmLink to heading

🟩Endorse

Helm v2 got a bad reputation (for good reason), but helm v3 has worked … well enough. There are still issues
with deploying CRDs and educating developers on why their helm chart did not deploy correctly. Overall, however,
helm works well enough as a way to package and deploy versioned Kubernetes objetcs and the Go templating language
is difficult to debug, but powerful.

### helm charts in ECR(oci)Link to heading

🟩Endorse

Originally our helm charts were hosted inside S3 and downloaded with a plugin. The main downsides were needing to install
a custom helm plugin and manually managing lifecycles. We’ve since switched to OCI stored helm charts and haven’t
had any issues with this setup.

### bazelLink to heading

🟧Unsure

To be fair, a lot of smart people like bazel, so I’m sure it’s not abadchoice to make.

When deploying Go services, bazel personally feels like overkill. I think Bazel is a great choice if your last company
used bazel, and you feel home sick. Otherwise, we have a build system that only a few engineers can dive deeply into,
compared to GitHub Actions, where it seems everyone knows how to get their hands dirty.

### Not using opentelemetryearlyLink to heading

🟥Regret

We started off sending metrics directly to DataDog using DataDog’s API. This has made it very hard to rip them out.

Open telemetry wasn’t as mature 4 years ago, but it’s gotten much better. I think the metrics telemetry is still
a bit immature, but the tracing is great. I recommend using it from the start for any company.

### PickingrenovatebotoverdependabotLink to heading

🟩Endorse

I honestly wish we had thought about “keep your dependencies up to date” sooner. When you wait on this too long,
you end up with versions so old the upgrade process is long and inevitably buggy. Renovatebot has worked well with
the flexibility to customize it to your needs. The biggest, and it’s pretty big, downside is that it’s VERY complicated
to setup and debug. I guess it’s the best of all the bad options.

### KubernetesLink to heading

🟩Endorse

You needsomethingto host your long running services. Kuberentes is a popular choice and it’s worked well for us.
The Kubernetes community has done a great job integrating AWS services (like load balancers, DNS, etc) into the
Kubernetes ecosystem. The biggest downside with any flexible system is that there are a lot of ways to use it, and
any system with a lot of ways to use has a lot of ways to use wrong.

any system with a lot of ways to use has a lot of ways to use wrong

* Jack Lindamood

### Buying our own IPsLink to heading

🟩Endorse

If you work with external partners, you’ll frequently need to publish a whitelist of your IPs for them. Unfortunately,
you may later develop more systems that need their own IPs. Buying your own IP block is a great way to avoid this by
giving the external partner a larger CIDR block to whitelist.

### PickingFluxfor k8s GitOpsLink to heading

🟩No Regrets

An early GitOps choice for Kubernetes was to decide between ArgoCD and Flux: I went with Flux (v1
at the time). It’s worked very well. We’re currently using Flux 2. The only downside is we’ve had to make our
own tooling to help people understand the state of their deployments.

I hear great things about ArgoCD, so I’m sure if you picked that you’re also safe.

### Karpenterfor node managementLink to heading

🟩Endorse

If you’re using EKS (and not fully on Fargate), you should be using Karpenter. 100% full stop. We’ve used other autoscalers,
including the default Kubernetes autoscaler andSpotInst. Between them all, Karpenter has
been the most reliable and the most cost-effective.

### UsingSealedSecretsto manage k8s secretsLink to heading

🟥Regret

My original thought was to push secret management to something GitOps styled. The two main drawbacks of using
sealed-secrets were:

* It was more complicated for less infra knowledgeable developers to create/update secrets
* We lost all the existing automations that AWS has around rotating secrets (for example)

### UsingExternalSecretsto manage k8s secretsLink to heading

🟩Endorse

ExternalSecrets has worked very well to sync AWS -> Kubernetes secrets. The process is simple for developers to
understand and lets us take advantage of terraform as a way to easily create/update the secrets inside AWS, as well
as give users a UI to use to create/update the secrets.

### UsingExternalDNSto manage DNSLink to heading

🟩Endorse

ExternalDNS is a great product. It syncs our Kubernetes -> Route53 DNS entries and has given us very little
problems in the past 4 years.

### Usingcert-managerto manage SSL certificatesLink to heading

🟩Endorse

Very intuitive to configure and has worked well with no issues. Highly recommend using it to create your Let’s Encrypt
certificates for Kubernetes. The only downside is we sometimes have ANCIENT (SaaS problems am I right?) tech stack
customers that don’t trust Let’s Encrypt, and you need to go get a paid cert for those.

### Bottlerocketfor EKSLink to heading

🟥Regret

Our EKS cluster used to run on Bottlerocket. The main downside was we frequently ran into networking CSI issues
and debugging the bottlerocket images were much harder than debugging the standard EKS AMIs. Using theEKS optimizedAMIs for our nodes has given us no problems, and we still have a backdoor to debug the node itself when there are
strange networking issues.

### PickingTerraformoverCloudformationLink to heading

🟩Endorse

Using Infrastructure as Code is a must for any company. Being in AWS, the two
main choices are Cloudformation and Terraform. I’ve used both and don’t
regret sticking with Terraform. It’s been easy to extend for other SaaS providers
(like Pagerduty), the syntax is easier to read than CloudFormation, and hasn’t been
a blocker or slowdown for us.

### Not using more code-ish IaC solutions (Pulumi,CDK, etc)Link to heading

🟩No Regrets

While Terraform and CloudFormation are data files (HCL and YAML/JSON) that describe
your infrastructure, solutions like Pulumi or CDK allow you to write code that
does the same. Code is of course powerful, but I’ve found the restrictive nature of
Terraform’s HCL to be a benefit with reduced complexity. It’s not that it’s
impossible to write complex Terraform: it’s just that it’s more obvious when it’s
happening.

Some of these solutions, like Pulumi, were invented many years ago while
Terraform lacked a lot of the features it has today. Newer versions of Terraform
have integrated a lot of the features that we can use to reduce complexity. We instead
use a middleground that generates basic skeletons of our Terraform code for parts we want to abstract away.

### Not using a network mesh (istio/linkerd/etc)Link to heading

🟩No regrets

Network meshes are really cool and a lot of smart people tend to endorse them, so I’m
convinced they are fine ideas. Unfortunately, I think companies underestimate the
complexity of things. My general infrastructure advice is “less is better”.

### Nginxload balancer for EKS ingressLink to heading

🟩No Regrets

Nginx is old, it’s stable, and it’s battle tested.

## homebrewfor company scriptsLink to heading

🟩Endorse

Your company will likely need a way to distribute scripts and binaries for your engineers to use. Homebrew has workedwell enoughfor both linux and Mac users as a way to distribute scripts and binaries.

## Gofor servicesLink to heading

🟩Endorse

Go has been easy for new engineers to pick up and is a great choice overall. For non-GPU services that are mostly network
IO bound, Go should be your default language choice.
