---
title: How to prepare for the Bitnami Changes coming soon
url: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon
site_name: hackernews_api
fetched_at: '2025-08-29T10:02:08.557176'
original_url: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon
author: zdkaster
date: '2025-08-28'
published_date: '2025-08-18T18:14:48.027Z'
description: The Deletion of Docker.io/Bitnami
tags:
- hackernews
- trending
---

# Blog Viewer

## How to prepare for the Bitnami Changes coming soon

#### ByBeltran Rueda Borregoposted10 days ago


   


Recommend

##### Update

After evaluating the impact and community feedback, the Bitnami team has postponed the deletion of the Bitnami public catalog (docker.io/bitnami) untilSeptember 29thto give users more time to adapt to the upcoming changes.To raise awareness before the registry deletion, we will run a series ofbrownoutsover the coming weeks. During each brownout, a set of 10 container images fromdocker.io/bitnamiwill be temporarily unavailable for 24 hours. The scheduled brownouts are:

* August 28, 08:00 UTC → August 29, 08:00 UTCSeptember 2, 08:00 UTC → September 3, 08:00 UTCSeptember 17, 08:00 UTC → September 18, 08:00 UTC
* August 28, 08:00 UTC → August 29, 08:00 UTC
* September 2, 08:00 UTC → September 3, 08:00 UTC
* September 17, 08:00 UTC → September 18, 08:00 UTC

The list of affected applications will be published on the day of each brownout via our usual channels.As previously announced, since August 28th, we have not published new Bitnami container images or Helm charts to Docker Hub in OCI format. The source code for containers and Helm charts remains available on GitHub under the Apache 2.0 license.

### What's changing?

Starting August 28th, Bitnami will be archiving its OCI registry of charts and images to a new location, Bitnami Legacy, to make room for the new secure, hardened images that will eventually reside in the main Bitnami registry. Users who are currently pulling these images will need to update their pipelines, internal mirrors, and Kubernetes clusters to pull from a new location before that time. A couple of options users have:

1. Switch toBitnami Secure Images
2. Switch to the Bitnami Legacy Registry

To retain existing functionality and maintain continuity of systems relying on Bitnami, we recommend switching to Bitnami Secure Images. In addition to a less disruptive transition, BSI helps strengthen your security and compliance posture by adopting the higher-quality images offered as part of BSI.

### Switching to Bitnami Secure Images (BSI)

While some BSI images will be free, they are only for use in development/testing purposes, and a commercial subscription is recommended for access to the entire catalog, as well as stable tags, long-term support versions, and more.

Though a BSI subscription provides customers with the entire Bitnami Debian-based image catalog (which will continue to receive updates), we recommend users upgrade and start using the hardened Photon Linux-based images instead. These are designed to be replacement images for any of the Debian images and work with the same Helm charts.

The Photon images provide many other benefits not previously available to users of Debian images, including:

* Drastically reduced CVE count (e.g., 100+ CVEs to in some cases 0)
* VEX statements for easier triage, along withKnown Exploitable Vulnerabilities(KEV) andEPSSscores
* A self-service UI/API with powerful reporting and metadata capabilities
* More advanced Helm charts are not available on Docker Hub, such as Bitnami’s “distroless charts” which offer an 83% smaller attack surface (by MB).
* Support for customizing the images built by our secureSLSA 3software factory
* Images and Helm charts are delivered to a private and secure OCI registry dedicated to each customer instead of relying on a public registry with rate limits like Docker Hub.
* Access to over 90 VM Images in OVA format
* Enterprise support for packaging and installation issues

### Switching to Bitnami Legacy Registry

Another option for users of Bitnami today is to switch to the historic archive registry called Bitnami Legacy. This is unsupported software that is being made available, at users' own risk, while they make plans for alternatives. As such, this is a temporary solution, and we do not plan to keep this registry around for long. It will quickly begin to accumulate vulnerabilities that are not patched and atrophy as any software frozen in time does. If this is your choice,we strongly recommend copying the images you are using to your own registry; again, this should be considered a temporary solution.While we think there are many better options to make before the August 28th change, this is an option of last resort for those who need more time.

### Why is it a good time to consider upgrading your security and compliance for open source?

So why do all the work now to change what’s maybe been working and update the type of open source images you use? We get it, no one likes change. But the reality is the landscape of open source is changing all around us. For example, from 2019-2023, the number of malicious packages discovered has risen to more than 245,000 according to Sonatype. That’s 2x all the previous years combined. The implication is that bad actors are finding increasing opportunities to exploit open source software that is running in every major software organization around the world. Meanwhile, with the growth of AI and MCP models, open source consumption is only going to increase. So the risk profile tides are quickly rising around us, and having a better boat to be prepared for the impacts of this change is the only responsible response.

In addition, theCyber Resilience Act in the EUcreates an impending obligation for many organizations doing business there to provide guarantees about the open source software they use in their organization. It could soon be a liability to use open source that doesn’t have the required documentation to prove it’s been sourced from a safe place and hasn’t been tampered with.

This is why the launch of Bitnami Secure Images is so timely. BSI is making it easier than ever for organizations to responsibly prepare for what the future of open source software in our modern world looks like. As with many things, what started out simple has become increasingly complex and requires more care to navigate. Furthermore, BSI has one of the lowest TCOs in the industry, enabling more organizations than ever before to afford cutting-edge supply chain security. BSI is effectively democratizing security and compliance for open source so that it doesn’t require million-dollar contracts from vendors with sky-high valuations.

### What are Competitors trying to claim about Bitnami?

It’s also a great time for the competition to try and steer the narrative about Bitnami. Some have claimed that Bitnami is “pulling their free container images and Helm charts from public access”. However, if we look a little more closely at the changes Bitnami has announced, this statement is inaccurate. For one, Bitnami Helm charts continue to be an open source project, under Apache 2, freely available to the public on GitHub.

Second, what is actually changing is the built OCI artifacts. Essentially, Bitnami has been the Jenkins of the internet for many years, but this has become unsustainable. Operating a build pipeline and OCI registry for the general public is very expensive. Just ask those same competitors throwing shade at Bitnami why they have never offered to make their charts or images publicly available at the same scale Bitnami has?

So users can continue to freely access the Helm chart source (as well as the Debian images). However, in order to sustain and support the dedicated team of engineers who maintain and build new charts and images, a subscription will be required if an organization needs the images and charts built and hosted in an OCI registry for them. And to reiterate the above again, organizations that choose this path are simultaneously upgrading their security posture and improving their OSS strategy.

### How do the changes on August 28th work?

The changes to the Bitnami repo are slated to begin on Aug 28th. They will not all be at once. Over a multi-week period, the images will be cleaned up from the registry to make room for the new ones. This is being done gradually to minimize the disruptions. However, we can’t be precise about which image will be removed at what time due to the complexity of the 84TB of OCI content that the engineering team will be dealing with. Therefore, it’s best to assume starting Aug 28th, every image used in a key business function should be addressed with an alternate registry.

We’re making room in the mainline Bitnami registry so we can populate it with the free tier of Bitnami Secure Images. These hardened Photon have the same names as the Debian images, so they can’t occupy the same registry. And we want new adopters of Bitnami to start with the secure images going forward, as we believe this is the future of open-source software on the internet. Inthis FAQ,you can find more information about all the details of the upcoming changes.

#bitnami#Security#helm


 0 comments



 22 views


## Permalink

https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon
