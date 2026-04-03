---
title: 'TIL: Docker log rotation | nicole@web'
url: https://ntietz.com/blog/til-docker-log-rotation/
site_name: lobsters
content_file: lobsters-til-docker-log-rotation-nicoleweb
fetched_at: '2026-02-18T06:00:33.138052'
original_url: https://ntietz.com/blog/til-docker-log-rotation/
date: '2026-02-18'
tags: devops
---

# TIL: Docker log rotation

Monday, February 16, 2026

Last week[1], when I went to publish my blog post, I ran into a surprising error: I was out of disk space. My server is used only for hosting a couple of small static sites, so I was surprised. None of the content is very large, why is the disk full?

A little investigation found the culprit. Starting from/and then drilling in usingdu -h -d 1 .showed me that a Docker folder was using most of the server's 25 GB disk. None of my container images are very large, so I checked in side and found a few log files that were larger than 10 GB each.

It turns out, Docker doesn't automatically rotate log files! As long as a container exists, the logs will keep growing for it. This means even if you stop a container and start it again, the logs are still there and getting bigger. I'd not thought about this before, but it turns out that when my blog is seeing heavy traffic, the logs can grow in order of megabytes per hour. And that really adds up over time.

* * *

First I did a quick check of how the logs are configured to start with. You can see the log configuration by usingdocker inspect.

$ docker inspect --format
=
'{{.HostConfig.LogConfig}}'
 my-poor-container

{json-file map
[]
}

And my container's logging was totally unconfigured! That explained a lot.

Now the fix is pretty quick. Thedocsshow us an example that works well enough here./etc/docker/daemon.jsondidn't exist yet, so I created it and added this log configuration in.

{


"log-driver"
:
"json-file"
,


"log-opts"
: {


"max-size"
:
"100m"
,


"max-file"
:
"3"

 }

}

The original example had10mfor log files, but I want a little more than that. I have the disk space, and I'd like longer to investigate logs before they are truncated away.

After setting that up, I restarted the docker daemon by callingsystemctl restart docker. But logs don't rotate yet, no! The docs told us that this applies fornewcontainers after Docker is restarted, but not for existing containers. So the final step was to stop and remove any containers I wanted rotation to work on, then recreate them.

After that, a quick check, and we've got log rotation.

$ docker inspect --format
=
'{{.HostConfig.LogConfig}}'
 my-happy-container

{json-file map
[
max
-
file:3 max
-
size:100m
]
}

* * *

Don't be like me, don't forget to rotate your logs!

Or, do forget. Focus on the things you enjoy, and do just enough of the other things to make it work. You can always hire someone else to solve some of the annoying, tedious, or difficult problems for you. (Hi.Hire me!)

1. This is another "today I learned" post that happened previously, so at this point it should be "last week I learned" or "recently I learned", but you know what, I don't make the rules[2].↩
2. Okay, I do make the rules on this site.↩

If you're looking for help on a software project, please considerworking with me!

Please share this post, and subscribe to thenewsletterorRSS feed.
 You can emailmy personal emailwith any comments or questions.

Want to become a better programmer?Join the Recurse Center!Want to hire great programmers?Hire via Recurse Center!
