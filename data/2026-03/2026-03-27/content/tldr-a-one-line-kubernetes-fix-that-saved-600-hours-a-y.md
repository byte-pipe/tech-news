---
title: A one-line Kubernetes fix that saved 600 hours a year
url: https://blog.cloudflare.com/one-line-kubernetes-fix-saved-600-hours-a-year/
site_name: tldr
content_file: tldr-a-one-line-kubernetes-fix-that-saved-600-hours-a-y
fetched_at: '2026-03-27T19:20:59.861847'
original_url: https://blog.cloudflare.com/one-line-kubernetes-fix-saved-600-hours-a-year/
date: '2026-03-27'
published_date: 2026-03-26T13:00+00:00
description: When we investigated why our Atlantis instance took 30 minutes to restart, we discovered a bottleneck in how Kubernetes handles volume permissions. By adjusting the fsGroupChangePolicy, we reduced restart times to 30 seconds.
tags:
- tldr
---

# A one-line Kubernetes fix that saved 600 hours a year

2026-03-26

* Braxton Schafer
4 min read

Every time we restarted Atlantis, the tool we use to plan and apply Terraform changes, we’d be stuck for 30 minutes waiting for it to come back up. No plans, no applies, no infrastructure changes for any repository managed by Atlantis. With roughly 100 restarts a month for credential rotations and onboarding, that added up to over50 hours of blocked engineering time every month, and paged the on-call engineer every time.

This was ultimately caused by a safe default in Kubernetes that had silently become a bottleneck as the persistent volume used by Atlantis grew to millions of files. Here’s how we tracked it down and fixed it with a one-line change.

### Mysteriously slow restarts

We manage dozens of Terraform projects with GitLab merge requests (MRs) usingAtlantis, which handles planning and applying. It enforces locking to ensure that only one MR can modify a project at a time.

It runs on Kubernetes as a singleton StatefulSet and relies on a Kubernetes PersistentVolume (PV) to keep track of repository state on disk. Whenever a Terraform project needs to be onboarded or offboarded, or credentials used by Terraform are updated, we have to restart Atlantis to pick up those changes — a process that can take 30 minutes.

The slow restart was apparent when we recently ran out of inodes on the persistent storage used by Atlantis, forcing us to restart it to resize the volume. Inodes are consumed by each file and directory entry on disk, and the number available to a filesystem is determined by parameters passed when creating it. The Ceph persistent storage implementation provided by our Kubernetes platform does not expose a way to pass flags tomkfs, so we’re at the mercy of default values: growing the filesystem is the only way to grow available inodes, and restarting a PV requires a pod restart.

We talked about extending the alert window, but that would just mask the problem and delay our response to actual issues. Instead, we decided to investigate exactly why it was taking so long.

### Bad behavior

When we were asked to do a rolling restart of Atlantis to pick up a change to the secrets it uses, we would runkubectl rollout restart statefulset atlantis, which would gracefully terminate the existing Atlantis pod before spinning up a new one. The new pod would appear almost immediately, but looking at it would show:

$ kubectl get pod atlantis-0
atlantis-0 0/1 
Init:0/1 0 30m

...so what gives? Naturally, the first thing to check would be events for that pod. It's waiting around for an init container to run, so maybe the pod events would illuminate why?

$ kubectl events --for=pod/atlantis-0
LAST SEEN TYPE REASON OBJECT MESSAGE
30m Normal Killing Pod/atlantis-0 Stopping container atlantis-server
30m Normal Scheduled Pod/atlantis-0 Successfully assigned atlantis/atlantis-0 to 36com1167.cfops.net
22s Normal Pulling Pod/atlantis-0 Pulling image "oci.example.com/git-sync/master:v4.1.0"
22s Normal Pulled Pod/atlantis-0 Successfully pulled image "oci.example.com/git-sync/master:v4.1.0" in 632ms (632ms including waiting). Image size: 58518579 bytes.

That looks almost normal... but what's taking so long between scheduling the pod and actually starting to pull the image for the init container? Unfortunately that was all the data we had to go on from Kubernetes itself. But surely therehadto be something more that can tell us why it's taking so long to actually start running the pod.

### Going deeper

In Kubernetes, a component calledkubeletthat runs on each node is responsible for coordinating pod creation, mounting persistent volumes, and many other things. From my time on our Kubernetes team, I know thatkubeletruns as a systemd service and so its logs should be available to us in Kibana. Since the pod has been scheduled, we know the host name we're interested in, and the log messages fromkubeletinclude the associated object, so we could filter foratlantisto narrow down the log messages to anything we found interesting.

We were able to observe the Atlantis PV being mounted shortly after the pod was scheduled. We also observed all the secret volumes mount without issue. However, there was still a big unexplained gap in the logs. We saw:

[operation_generator.go:664] "MountVolume.MountDevice succeeded for volume \"pvc-94b75052-8d70-4c67-993a-9238613f3b99\" (UniqueName: \"kubernetes.io/csi/rook-ceph-nvme.rbd.csi.ceph.com^0001-000e-rook-ceph-nvme-0000000000000002-a6163184-670f-422b-a135-a1246dba4695\") pod \"atlantis-0\" (UID: \"83089f13-2d9b-46ed-a4d3-cba885f9f48a\") device mount path \"/state/var/lib/kubelet/plugins/kubernetes.io/csi/rook-ceph-nvme.rbd.csi.ceph.com/d42dcb508f87fa241a49c4f589c03d80de2f720a87e36932aedc4c07840e2dfc/globalmount\"" pod="atlantis/atlantis-0"
[pod_workers.go:1298] "Error syncing pod, skipping" err="unmounted volumes=[atlantis-storage], unattached volumes=[], failed to process volumes=[]: context deadline exceeded" pod="atlantis/atlantis-0" podUID="83089f13-2d9b-46ed-a4d3-cba885f9f48a"
[util.go:30] "No sandbox for pod can be found. Need to start a new one" pod="atlantis/atlantis-0"

The last two messages looped several times until eventually we observed the pod actually start up properly.

Sokubeletthinks that the pod is otherwise ready to go, but it's not starting it and something's timing out.

### The missing piece

The lowest-level logs we had on the pod didn't show us what's going on. What else do we have to look at? Well, the last message before it hangs is the PV being mounted onto the node. Ordinarily, if the PV has issues mounting (e.g. due to still being stuck mounted on another node), that will bubble up as an event. But something's still going on here, and the only thing we have left to drill down on is the PV itself. So I plug that into Kibana, since the PV name is unique enough to make a good search term... and immediately something jumps out:

[volume_linux.go:49] Setting volume ownership for /state/var/lib/kubelet/pods/83089f13-2d9b-46ed-a4d3-cba885f9f48a/volumes/kubernetes.io~csi/pvc-94b75052-8d70-4c67-993a-9238613f3b99/mount and fsGroup set. If the volume has a lot of files then setting volume ownership could be slow, see https://github.com/kubernetes/kubernetes/issues/69699

Remember how I said at the beginning we'd just run out of inodes? In other words, we have alotof files on this PV. When the PV is mounted,kubeletis runningchgrp -Rto recursively change the group on every file and folder across this filesystem. No wonder it was taking so long — that's a ton of entries to traverse even on fast flash storage!

The pod'sspec.securityContextincludedfsGroup: 1, which ensures that processes running under GID 1 can access files on the volume. Atlantis runs as a non-root user, so without this setting it wouldn’t have permission to read or write to the PV. The way Kubernetes enforces this is by recursively updating ownership on the entire PVevery time it's mounted.

### The fix

Fixing this was heroically...boring. Since version 1.20, Kubernetes has supported an additional field onpod.spec.securityContextcalledfsGroupChangePolicy. This field defaults toAlways, which leads to the exact behavior we see here. It has another option,OnRootMismatch, to only change permissions if the root directory of the PV doesn't have the right permissions. If you don’t know exactly how files are created on your PV, do not setfsGroupChangePolicy:OnRootMismatch. We checked to make sure that nothing should be changing the group on anything in the PV, and then set that field:

spec:
 template:
 spec:
 securityContext:
 fsGroupChangePolicy: OnRootMismatch

Now, it takes about 30 seconds to restart Atlantis, down from the 30 minutes it was when we started.

Default Kubernetes settings are sensible for small volumes, but they can become bottlenecks as data grows. For us, this one-line change tofsGroupChangePolicyreclaimed nearly 50 hours of blocked engineering time per month. This was time our teams had been spending waiting for infrastructure changes to go through, and time that our on-call engineers had been spending responding to false alarms. That’s roughly 600 hours a year returned to productive work, from a fix that took longer to diagnose than deploy.

Safe defaults in Kubernetes are designed for small, simple workloads. But as you scale, they can slowly become bottlenecks. If you’re running workloads with large persistent volumes, it’s worth checking whether recursive permission changes like this are silently eating your restart time. Audit yoursecurityContextsettings, especiallyfsGroupandfsGroupChangePolicy.OnRootMismatchhas been available since v1.20.

Not every fix is heroic or complex, and it’s usually worth asking “why does the system behave this way?”

If debugging infrastructure problems at scale sounds interesting,we’re hiring. Come join us on theCloudflare Communityor ourDiscordto talk shop.

Cloudflare's connectivity cloud protects 
entire corporate networks
, helps customers build 
Internet-scale applications efficiently
, accelerates any 
website or Internet application
, 
wards off DDoS attacks
, keeps 
hackers at bay
, and can help you on 
your journey to Zero Trust
.
Visit 
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet, 
start here
. If you're looking for a new career direction, check out 
our open positions
.
 
 
Kubernetes
Terraform
Platform Engineering
Infrastructure
SRE