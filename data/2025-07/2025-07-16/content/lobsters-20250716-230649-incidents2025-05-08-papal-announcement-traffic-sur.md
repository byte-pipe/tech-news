---
title: Incidents/2025-05-08 Papal announcement traffic surge - Wikitech
url: https://wikitech.wikimedia.org/wiki/Incidents/2025-05-08_Papal_announcement_traffic_surge
site_name: lobsters
fetched_at: '2025-07-16T23:06:49.310580'
original_url: https://wikitech.wikimedia.org/wiki/Incidents/2025-05-08_Papal_announcement_traffic_surge
date: '2025-07-16'
tags: devops
---

From Wikitech

<
Incidents

document status:draft

## Summary

Incident metadata (see
Incident Scorecard
)

Incident ID

2025-05-08 Papal announcement traffic surge

Start

2025-05-08 17:16

Task

End

2025-05-08 17:30

People paged

Responder count

Coordinators

taavi, cdanis

Affected metrics/SLOs

Traffic SLO?

Impact

For a duration of about 10 minutes, some European users received error messages or very slow page load times.

https://grafana.wikimedia.org/goto/GRHGOusNR?orgId=1

The announcement of the election of a new Pope is an event that has a reputation for causing sudden traffic surges against news sites, which then cause user-visible outages during peak demand -- Wikipediaincluded.

* Readership reaching up to800kreq/s(more than 6x usual traffic), sustaining at ~500k req/sCDN egress bandwidth peaked at 134 gigabit/sec (more than 2x usual)
* CDN egress bandwidth peaked at 134 gigabit/sec (more than 2x usual)
* This breaks our previous all-time traffic record by more than 2xPrevious record was ~300kreq/s (at the time, 2x usual traffic), from 8 September 2022, when the death of Queen Elizabeth II was announced https://grafana.wikimedia.org/goto/bfAtojxHR
* Previous record was ~300kreq/s (at the time, 2x usual traffic), from 8 September 2022, when the death of Queen Elizabeth II was announced https://grafana.wikimedia.org/goto/bfAtojxHR
* User-facing impacts were minimal, and much better than feared:Some(?) European users received error pages or very slow loading speeds for a duration of about 10 minutes while our esams (Amsterdam) datacenter was overloadedMany editors encountered edit conflicts, although this is largely unavoidable in breaking news eventsSome users of on-wiki search received errorsIn the past, papal election announcements have caused extended outages across all wikis, for causes similar to theMichael Jackson effect.
* Some(?) European users received error pages or very slow loading speeds for a duration of about 10 minutes while our esams (Amsterdam) datacenter was overloaded
* Many editors encountered edit conflicts, although this is largely unavoidable in breaking news events
* Some users of on-wiki search received errors
* In the past, papal election announcements have caused extended outages across all wikis, for causes similar to theMichael Jackson effect.
* Mitigations made at the time:Some traffic fromesams(Amsterdam) was temporarilyrebalancedtodrmrs(Marseille)
* Some traffic fromesams(Amsterdam) was temporarilyrebalancedtodrmrs(Marseille)

## Conclusions

### What went well?

In essence: lots of engineering work over the past few years allowed us to remain online during this event.

Below is a list in approximate order of significance for handling this traffic surge, or for handling future exceptional load events.

* We builtdrmrs, our datacenter site in Marseilles.  Without drmrs taking half the European load during the event, esams would certainly have failed – and that would give us the unpleasant decision between being hard-down for all of Europe until traffic relented, or risking potentially turning the European outage into a globally-cascading one, if we had attempted to distribute European load among the remaining global datacenters.
* We wrote and have been deployingLiberica, our state-of-the-art load balancer, which includesKatran's scalable data plane.  During the event, our legacyIPVSload balancers in esams reported processing over 1 million packets per second and sustaining more than 5 million simultaneous connections – both of which we know to be at or beyond the architectural limits of IPVS as we use it.  We believe that IPVS is the component that overloaded and caused user-visible issues for esams traffic, which emphasizes the importance of continuing the liberica deployment and adopting Katran. Since this event, liberica/Katran has demonstrated handling over 6Mpps without any issues or degradation:https://grafana.wikimedia.org/goto/mWo5vuyNR
* We builtmagru, our datacenter site in São Paulo.  Even though it presently handles traffic for only some of South America, magru traffic peaked at 90krps during the event – one eighth of global CDN traffic.  Without magru, this traffic would have hit a mix of codfw and eqiad, potentially causing an overload there as well.
* Migration of the MediaWikiapp layer toKubernetes, in particular the change to using a larger number of instances with a smaller number of PHP-FPM workers per instance, allowed the app layer to sustain higher worker utilization without major user impact.  On bare metal, we could only reach 60% utilization of  PHP workers before starting to encounter serious latency degradation – so 60-65% was effectively our 'redline' utilization.  But on Kubernetes this isn't the case: utilization in eqiad peaked at 75% on mw-web and even exceeded 80% for a sustained period on mw-api-ext, without a serious latency hit.  In addition, although we did not do so here, Kubernetes also allows us to easily add app-layer capacity when needed in response to increased load.
* We implementedMediaWiki Multi-DC, giving us extra capacity and resilience for read-only requests, even once the CDN edge cache is out of the picture.  At the time, our secondary dc (codfw) was handling about 5k rps, or between 1/3rd to 1/4th of the total global appserver traffic, which gave headroom for eqiad to absorb a +33% increase in load when the name was announced.
* Request coalescinginside our CDN edges saved us about 2krps of traffic to the MediaWiki app layer.  Without this, the peak of the event would have increased app layer load by an additional 15% of its normal traffic.  With request coalescing, the event "only" increased app layer load by ~33% of its normal traffic.
* Ongoing MediaWiki performance cleanupsreduced lock contention, improved efficiency of DB queries, and removed bottlenecks before we run into them.  Some examples of this work are epics likeT302623andT322528, but there are many others.

(Please do note the differences above between CDN traffic and appserver traffic -- one appserver request is much more expensive than one CDN request.)

### What went poorly?

* The announcement was during the European early evening, which is usually when the daily peak in traffic occurs.

### Where did we get lucky?

* The announcement was during the European early evening, which is during business hours for most of the WMF SRE team and other technical staff.

## Timeline

All times in UTC.

Time

Event

16:08

<volans>
 habemus papam (a new pope has been elected, expect traffic spikes)

16:10

The Wikipedian who changed Jimmy Carter's page from "is" to "was" edits the Pope infobox to TBA, edit description "white smoke"

16:12

Traffic becomes slightly elevated above normal levels, and continues to rise for the next hour

17:14

Announcement of new Pope begins'

17:15

Slight
dip
 in traffic (as people stop hitting F5 and start watching live feeds)

17:16

<Emperor>
 we got a shout-out from the Vatican feed

17:19

FIRING:
 ProbeDown: Service text-https:443 has failed probes (http_text-https_ip4) @ esams

OUTAGE BEGINS

17:21

taavi becomes IC

17:21

Traffic peaks at 725k req/s

17:22

Decision to hold the MediaWiki train

17:23

Traffic from DE and PL is moved from esams to drmrs via GeoIP

link

17:24

FIRING
: NELHigh: Elevated Network Error Logging events (tcp.timed_out) #page

17:25

FIRING
: [2x] PoolcounterFullQueues: Full queues for poolcounter1006:9106 poolcounter

17:27

Varnish rolling upgrade in eqsin is stopped, to be resumed later

17:29

RESOLVED
: [2x] ProbeDown: Service text-https:443 has failed probes
OUTAGE ENDS

17:30

RESOLVED
: [2x] PoolcounterFullQueues: Full queues resolved for poolcounter1006:9106

17:32

<inflatador> re: cirrus, getting more pool counter rejections but on a downward trend
link

17:34

RESOLVED
: NELHigh: Elevated Network Error Logging events (tcp.timed_out)

17:36

Traffic from PL is moved back to esams

link

17:40

<jynus>
 save failures are high, but there are conflicts — not much to be done

17:42

Grafana upgrade is postponed due to ongoing incident

17:44

Discussion about what to do with the train

17:56

cdanis becomes IC

18:00

Traffic falls to ~315k req/s (still 175% of usual daily peak)

18:14

<cdanis>
 Edit conflict rate is 2–3x normal, otherwise healthy; train is unblocked

18:14

Incident declared resolved

## Detection

Automated monitoring detected the esams outage. However, many humans were already watching very closely.

## Links to relevant documentation

* Michael Jackson effect

## Actionables

* …

## Scorecard

Incident Engagement ScoreCard

Question

Answer

(yes/no)

Notes

People

Were the people responding to this incident sufficiently different than the previous five incidents?

Were the people who responded prepared enough to respond effectively

Were fewer than five people paged?

Were pages routed to the correct sub-team(s)?

Were pages routed to online (business hours) engineers?  
Answer “no” if engineers were paged after business hours.

Process

Was the "Incident status" section atop the Google Doc kept up-to-date during the incident?

Was a public wikimediastatus.net entry created?

Is there a phabricator task for the incident?

Are the documented action items assigned?

Is this incident sufficiently different from earlier incidents so as not to be a repeat occurrence?

Tooling

To the best of your knowledge was the open task queue free of any tasks that would have prevented this incident?
Answer “no” if there are open tasks that would prevent this incident or make mitigation easier if implemented.

Were the people responding able to communicate effectively during the incident with the existing tooling?

Did existing monitoring notify the initial responders?

Were the engineering tools that were to be used during the incident, available and in service?

Were the steps taken to mitigate guided by an existing runbook?

Total score (count of all “yes” answers above)

Retrieved from "
https://wikitech.wikimedia.org/w/index.php?title=Incidents/2025-05-08_Papal_announcement_traffic_surge&oldid=2324006
"

Categories
:
* Incident documentation
* Incident documentation drafts
