---
title: Medium
url: https://blog.argoproj.io/argo-rollouts-1-10-release-candidate-24c9edc69abe
site_name: tldr
content_file: tldr-medium
fetched_at: '2026-07-23T11:39:25.984065'
original_url: https://blog.argoproj.io/argo-rollouts-1-10-release-candidate-24c9edc69abe
author: Kostis Kapelonis
date: '2026-07-23'
published_date: '2026-07-16T16:10:42.297Z'
description: Argo Rollouts 1.10 Release Candidate We’re excited to announce the release candidate for Argo Rollouts 1.10! This release includes contributions from 46 contributors and includes 98 commits …
tags:
- tldr
---

DevOps
Kubernetes
Gitops
Progressive Delivery
Argo Rollouts

# Argo Rollouts 1.10 Release Candidate

Kostis Kapelonis
6 min read
·
6 days ago

--

Listen

Share

Press enter or click to view image in full size

We’re excited to announce the release candidate for Argo Rollouts 1.10! This release includes contributions from 46 contributors and includes 98 commits, covering more reliable rollout reconciliation, safer Job-based analysis, better Istio reliability, expanded plugin support, and reduced controller resource usage. If you are still using Traefik v2, there is also a potential breaking change.

You can check out thefull CHANGELOGfor the complete list of changes, and grab the RC from thev1.10.0-rc1 release page.

## More Reliable Rollout Reconciliation

This release fixes a class of bugs where the controller could briefly act on outdated information about a Rollout, occasionally causing it to miss or override an action a user had just taken, like unpausing, aborting, or promoting a rollout while a deployment was already in progress. Rollouts now respond more consistently and predictably to manual actions, even under concurrent changes. We know that there are several more improvements that can be done in this area, so stay tuned.

Thanks toZach Aller(Intuit) andAlexandre Gaudreault(Intuit) for this work.

## Detect failed Jobs faster

If you use Kubernetes Jobs to run analysis, this release fixes a case where a job that never actually finished because it failed to even start would be incorrectly reported asSuccessful. That could let a bad rollout continue even though the analysis never really passed. These cases (image not found or not pulled) are now correctly reported asInconclusiveinstead.

metrics:
 - name: job-metric
 provider:
 job:
 spec:
 activeDeadlineSeconds: 10 # generically bounds how long a hung job can run before it's reported Inconclusive
 template:
 spec:
 containers:
 - name: my-job
 image: wrong-image-name:any
 restartPolicy: Never

This is the first step in a larger effort to improve the Job metric provider. We want to make the Job metric as powerful as the other metric providers (even reporting inconclusive on its own) so expect more improvements there in future releases.

Thanks toKostis Kapelonis(Octopus Deploy) andShetaya(Procore) for this work.

## Istio Traffic-Routing Reliability

If you use Istio to split traffic between canary and stable versions, this release fixes several timing issues that could cause brief live traffic errors during canary rollouts and rollbacks including one where a fast rollback could briefly send far more traffic to a canary than it was scaled to handle. Canary progression and rollbacks should now be noticeably more reliable under Istio. Again, we know that lots of Argo Rollouts users employ Istio, and this is an area that is constantly getting new fixes and updates.

Thanks toAndrew J. Brownfor this work.

## Breaking Change: Traefik Now Defaults to v3

Argo Rollouts now assumesTraefik v3by default. If you are already running Traefik v3, no action is needed.

If you’re still onTraefik v2, youMUSTtell the controller to use the older API version before upgrading, or it won’t be able to talk to your Traefik resources:

--traefik-api-group=traefik.containo.us
--traefik-api-version=traefik.containo.us/v1alpha1

Thanks toidurgakalyanfor this update.

## New Notification Channels: Microsoft Teams and Nats.io

Rollout and analysis notifications can now be sent toMicrosoft Teams, using its modern Workflows connector, and toNats.ioin addition to the channels already supported (Slack, email etc.). If you’re currently notifying Teams via the older Office 365 Connectors integration, this is also the recommended upgrade path, since Microsoft is retiring that integration in 2026.

data:
 service.teams-workflows: |
 recipientUrls:
 my-channel: https://api.powerautomate.com/webhook/<your-webhook-id>

This change is part of the upstream integration from thenotification engine(also used in Argo CD).

## Traffic-Routing Plugins Catch Up to Built-In Providers

Two capabilities that were previously only available with the built-in ALB and Istio traffic routers now also work with any traffic-routing plugin, like theGateway API plugin:

* Ping-pong services, whichallow zero-downtimerollouts for long-lived connections (like gRPC or database connections) that can’t tolerate a mid-request cutover.
* Traffic mirroring, which sendsa copy of live trafficto the canary for testing, without it affecting real users or counting toward canary analysis.

Note that this change only unblocks plugins for implementing the mechanism. Plugins must also add the respective capabilities in code for the feature to be usable. There is alreadyan open PR for ping/pongin the Gateway API plugin.

## GetKostis Kapelonis’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe
Subscribe

Remember me for faster sign in

Thanks toYehor Boikofor the ping-pong support andKostis Kapelonis(Octopus Deploy) for the mirroring support.

## Datadog: Configurable Request Timeout

Datadog analysis queries previously had a fixed 10-second timeout, which meant a query that was simply slow could fail an analysis. You can now raise (or lower) this timeout per metric:

provider:
 datadog:
 requestTimeout: 30s # default is 10sdatadog:

Thanks toGabriel Ferraté(Datadog) for this one.

## Lower Controller Memory and CPU Usage

The controller now uses noticeably less memory and CPU, especially on large clusters. This comes from two changes: it no longer keeps track of Kubernetes objects it doesn’t actually need, and it reads objects from its internal cache more efficiently. If you run Argo Rollouts on a large cluster or scrape it frequently with Prometheus, you should see a real drop in resource usage.

Thanks toWilliam Van Hevelingen(Acquia) andNiels Stevens(OneSignal) for this work.

## Aligning With Argo CD

As sibling projects under the Argo umbrella, Argo Rollouts and Argo CD often solve the same problems twice. This release brings a few things over from Argo CD directly, so both projects stay closer in how they’re built and maintained:

* Switched the dashboard UI topnpm.The UI build now uses pnpm instead of yarn, matching the same move Argo CD already made, resulting in faster installs and less disk usage for anyone building the UI from source.
* Smarter CI for documentation-only changes.A PR that only touches documentation no longer triggers the full build/test/e2e suite, cutting down turnaround time for doc contributions.
* A cherry-pick bot.Backporting a merged fix to an older release branch now happens automatically via a bot, instead of requiring a manual cherry-pick.

Thanks toKeith Chong(Red Hat),Kevin Joe Harris(LTM), andKostis Kapelonis(Octopus Deploy) for this work.

## Other Improvements

* Dashboard:added a page-size selector, so you can view more rollouts per page in the table view. Thanks toGregor Heine.
* Dashboard:the full container image name is now visible while editing a rollout, instead of being cut off. Thanks toKarl Lyons(Shaped AI).
* GitOps:fixed an issue where Argo CD could incorrectly report a rollout as “out of sync” when a certain optional field was left unset in Git. Thanks toZach Aller(Intuit).
* Build system:teams maintaining a private fork of Argo Rollouts can now build and publish images to their own container registry, rather than having everything hard-coded to the project’s registry. Thanks toKostis Kapelonis(Octopus Deploy).
* Traffic routing:fixed a bug where rollouts using a custom traffic-weight scale (instead of the standard 0–100%) could fail to send any traffic to the canary at all. Thanks toFumingZhang.
* Blue-green analysis:fixed a bug where analysis could be canceled and the rollout promoted early if pods briefly dropped out during normal cluster activity, even though nothing was actually wrong. Thanks toJesse Suen(Akuity).
* CRDs:kubectl explain now shows proper field descriptions for Rollouts again, after a change had accidentally stripped them out. Thanks tojaspreet-skillz.
* Controller:removed a misconfigured health check that was adding unnecessary load on busy clusters. Thanks toPeter Jiang(Intuit).

## Bug Fixes

Beyond the fixes above, this release includes 18 additional smaller bug fixes across traffic routing, analysis, metric providers, the dashboard, and the controller. See thefull CHANGELOGfor the complete list.

## Summary

As always, a huge thank you to everyone who contributed code, documentation, bug reports, and reviews to this release. If you are also building any kind of plugin for Argo Rollouts (metric, traffic, step) we would love to know about it!

Photo bychris robertonUnsplash