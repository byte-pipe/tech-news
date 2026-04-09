---
title: Forgejo v12.0 is available — Forgejo
url: https://forgejo.org/2025-07-release-v12-0/
site_name: lobsters
fetched_at: '2025-07-18T23:07:55.760232'
original_url: https://forgejo.org/2025-07-release-v12-0/
date: '2025-07-18'
description: ☶
tags: release, vcs
---

Forgejo v12.0was released on 17 July 2025. You will find a short selection of the changes it introduces below and acomplete list in the release notes.

Adedicated test instanceis available to try it out. Before upgrading it isstrongly recommendedto make a full backup as explained in theupgrade guideand carefully readall breaking changesfrom therelease notes. If in doubt, do not hesitate to ask for helpon the Fediverse, orin the chat room.

This release marks the Forgejo v7.0 LTS series as End of Life. Forgejo v11.0 was published three months ago and will be supported until15 July 2026, when Forgejo v16.0 is published. Admins of Forgejo instances with version v7.0 are recommended to upgrade to v11.0 as soon as possible as only it and v12.0 will receive security patches from now on.

## Summary

User researchanddesignis where Forgejo User eXperience (UX) and User Interface (UI) are discussed and improved. It is not about mimicking other forges but observing what users do and improve accordingly. For instance:

* Most Forgejo user have visited their profile page at least once and some may use it as their landing page. It is in constant need for improvement while minimizing the impact on habits that users developed over time. Theredesign of the user profilewas done in that spirit. It adds more actions while also making better use of the available space.
* There are a number of hidden features in Forgejo that only few people actually use because their UX is not good enough. The ability to review pull requests one commit at a time was among them and itwas made easier to discover and more convenient to use.
* Forgejo Actions may be used to schedule jobs that run daily, just like cron. But failures could got unnoticed for a long time, waiting for a user to visit the actions page. By adding an option to the workflow,an email notification can now be sentwhen a job fails.

In large part because Forgejo is used at scale by Codeberg, performance issues are discovered that are not easily detected on smaller instances. For instance, each open pull request is checked for conflict every time a new commit is pushed to the target branch, blocking the ability to merge them. ThisI/O intensive and time consuming step is optimized, saving resources and allowing faster merges.

Forgejo security features rely on a mixture OpenPGP and SSH. Since SSH is more widely known, Forgejo is gradually implementing alternatives using SSH for tasks that previously required OpenPGP. In this release it is now possible to use SSH instead of OpenPGP forinstance signing.

Excessive crawling is a recurring chore for all Forgejo instances, large and small. Arobots.txtfileis included by default to reduce the impact of crawlers by letting them know which URLs should be avoided.

### Improved UX for per-commit reviews

When a pull request has a well organized series of commit, it may be convenient for the reviewer to focus on each of them individually instead of using the larger diff that shows all of them at once. It is already possible in Forgejo but it is also one of the lesser known features, in part because it was inconvenient to use and discover.This was improved as follows:

* The new next (“Next”) and previous (“Prev”) buttons can be used to navigate the list of commits which is more convenient than using the pull down menu.
* The review button (“Finish Review”) can be accessed from the per-commit review page instead of being inactive.
* The links in the pull request pages (conversation and list of commits) lead to the per-commit review page instead of the commit display page. Unless they were made redundant by a force push.
* The commit message is now displayed in the per-commit review page so the reviewer does not need to navigate away to find it.

## Keeping forks in sync

If you have a fork and want to keep it synchronized with upstream, thenew sync fork featureprovides a way to do that. It also indicates whether your fork is behind and/or ahead and by how many commits.

## glTF viewer

If you open aglTF modelin Forgejo, you willnow be able to preview this modelin the Forgejo UI without having to download the model and open it in an external tool. Support for previewing other 3D formatsis an open issue.

## Forgejo Actions email notifications on failure

If a workflow fails,a mail will be sentprovided the workflow containsenable-email-notifications: true. The recipient depends on the context:

* Pull requests: the user who opened the pull request.
* Push: the user who pushed the commit.
* Scheduled: the user who owns the repository or the contact email of the organization.
* Dispatch: the user who triggered the dispatch.

## UI and UX improvements

* If you try to create a repository and you have hit the limit on the amount of repositories you are allowed to create, it isnow clearer which limityou hit.
* The size and dimensions constraints of the custom avatar isnow shown in the UI. You no longer have to find out about this requirement after failing to upload an avatar.
* Pasting images into the comment editorwill now show that image in the ‘dropzone’.
* Theuser profile has been redesigned. The most notable change is that actions have been moved to a dropdown and several new actions were added.
* The ‘Write’/‘Preview’ switch has beenreworked to use the new switch element.
* Themigration screen was redesignedto make it more usable and make better use of the available screen space.

### Automatically refreshing workflows

Endlessly staring at many workflows in the ‘Actions’ tab to see if they pass is a favorite activity of many developers. Forgejo nowrefreshes the status of these workflows every 30 secondsso you no longer have to open each workflow in a new tab or wear out yourF5key.

### Localized relative time

In many places of the Forgejo UI you will find relative time, the logic of this component was provided bygithub/relative-time-element. Forgejo encountered two issues with this library: it was not possible to localize the relative time and there arecases that it does not show the correct relative time. This library is now replaced by Forgejo’s own implementation (1,2) that allows for localized relative time and uses a simpler approach to calculating relative time that does not run into the same bugs the previous library did.

## Faster conflict checking

Due to Forgejo’s nature it relies a lot on Git commands to perform its job in a efficient manner. Forgejo stores repositories asbare repositoriesand this means that it is not always possible to use commands that require aworking tree. For certain operations a temporary clone is created for the sole purpose of using such Git operations. For large repositories this can end up causing a lot of I/O. One of such example was pull request conflict checking, whichwas reported by a userto cause I/O loads proportional to the amount of open pull requests. Upon re-examining available git commandsgit merge-tree --write-treeallows for conflict checking to happen without requiring a working tree. If Forgejo is run with a Git version greater or equal than 2.38you will enjoy this improved performance.

## API changes

* Two new API endpoints were addedto retrieve actions runs of a repository and retrieve specific runs by their ID.
* A new API endpoint was addedthat is able to retrieve multiples blobs at once. This endpoint was added to helpget support for Forgejo in Sveltia CMS.
* Endpoints that return the metadata of a filenow also returns when the last commit was committed. This changehelps GitNex with showing this informationin directory listings of a repository, similar how Forgejo shows that information.
* It is now possible tolists packages and retrieve info about a package without a token if the profile is public. This is public information and was not required to be guarded behind a token check.

## Redirecting fediverse handles

Forgejo willnow transform fediverse handles(ex.@forgejo@floss.socialand!forgejo@programming.dev) into links tohttps://fedirect.toolforge.org, a website hosted byWikimedia, to redirect fediverse handles to their respective URLs via Webfinger. Forgejo is working on implementing properfederated mentionsthat will also notify users on other federated services, which the redirection does not do.

## Tabs indentations in the comment editor

If you have typed comments and tried to useTabyou have noticed that it does nothing, this is frustrating especially if you try to type lists. Tab handling isnow implemented in Forgejoto do indentations. A lot of time has been spent to make sure it is accessible and works in a consistent and expected behavior to addressconcerns raised last yearin a previous implementation.

## Relaxing the requirements on email addresses

In response to a security reportGitea restricted the allowed syntax of email addresses in early 2022and some email addresses could not be used despite being conformant to the RFC. This change hasnow been revertedand the security issue that would allow for command injection was fixed, thus removing the need for strict requirements on the syntax of email addresses.

## Instance signing with SSH

Commits that are created by Forgejo (e.g. file edits and merge commits) can be signed by the Forgejo instance via a GPG key.
It is now also possible to insteaduse SSH signing, it has the unique capability of being done by a TPM viaan ssh-agent.
In addition theinstance signing documentationwas reworded to use clearer language and be easier to read for instance admins.

## Removing deprecated API authentication methods

The API has several authentication methods,two of them are now removedafter being deprecated in 2023. The two methods would look in the URL query for theaccess_tokenandtokenparameter. Passing authentication via the URL is not secure and can lead to them being logged and thus being exposed. It is now fully removed and there’s no option to enable these methods again.

## Default robots.txt

Forgejo instances have in the last several months beenhit hard by all sorts of new crawlers. One of the easiest way that crawlers disrupt Forgejo instances is by navigating to expensive to serve endpoints, creating many repo archives and filling disk space or getting lost in trying many different issue filters. Forgejonow serves a strong restrictive robots.txt, if norobots.txtis set. This should help with reducing the impact of crawlers that respectrobots.txtby not navigating to endpoints that can disrupt Forgejo instances.

## Forgejo build time optimization

The build process compresses the frontend assets viagzipinto the Forgejo binary withvfsgenso that Forgejo can serve these assets. The build process nowcompresses the frontend assets with Zstd, which is 4x faster than gzip. As an added benefit, assets are now served viaZstdwith a fallback to on-the-flygzipfor browsers that do not supportZstd. It also resulted in reducing the Forgejo binary by 2 MiB.

One of Forgejo’s dependencies, specificallygo-rpmutils, contained a dependency that is aCGOwrapper aroundZstd’s reference library. Although Forgejo’s did not use this CGO dependency, Go unconditionally compiled it and it took almost as long as compiling the CGO SQLite3 driver. Forgejonow has a fork of go-rpmutilswithout this CGO dependency, resulting in a shorter build time of Forgejo.

## xorm EngineGroup connections for optimized database query routing and load balancing

Withthis addition, read-only queries are automatically routed to database read-replicas in a load-balanced way, keeping theprimaryfree for writes.Multiple load balancing policiescan be selected.

Note: This requires a HA database setup with multiple nodes (at least 3) and only works with Postgres or MySQL.

## Reducing the usage of Fomantic.

Forgejo usesFomantic-UIfor historical reasons. In many cases it is not needed, does not provide good accessibility and lock components behind a javascript requirement that could also have been implemented via CSS and semantic HTML. In this release, there are two changes that reduce the use of Fomantic.

* The module that dims the entire page and displays a modalhas been replaced with Forgejo’s own dimming module. This allows browser testing to happen and avoid regressions.
* Fomantic-UI comes with a lot of CSS, Forgejo does not use all this CSS.Unused font size classes were removed. This reduces the size of the compiled CSS file and ensures that we do not accidentally depend on it in the future.

## Container images based on Alpine 3.22

Thev12 container imagesarebuiltfrom the latestAlpine 3.22 patch release. It includes:

* Git 2.49.1
* GnuPG 2.4.7
* SQLite 3.49.2
* OpenSSH 10.0

## Release schedule and Long Term Support

Thetime based release schedulewas established to publish a release every three months. Patch releases will be published more frequently, depending on the severity of the bug or security fixes they contain.

Version
Release date
End Of Life
11.0 (LTS)
16 April 2025
16 July 2026
12.0
17 July 2025
16 October 2025
13.0
16 October 2025
15 January 2026

### 12.0-test daily releases

Releases are built daily from the latest changes found in thev12.0/forgejodevelopment branch. They are deployed to thehttps://v12.next.forgejo.orginstance for manual verification in case a bug fix is of particular interest ahead of the next patch release. It can also be installed locally with:

* OCI images:rootandrootless
* Binaries

Their names are staying the same but they are replaced by new builds every day.

## Get Forgejo v12.0

See thedownload pagefor instructions on how to install Forgejo, and read therelease notesfor more information.

### Upgrading

Carefully read thebreaking bug fixessection of the release notes.

The actual upgrade process is as simple as replacing the binary or container image
with the correspondingForgejo binaryorcontainer image.
If you’re using the container images, you can use the12.0tagto stay up to date with the latest12.0.Ypatch release automatically.

Make sure to check theForgejo upgrade
documentationfor
recommendations on how to properly backup your instance before the
upgrade.

### Contribute to Forgejo

If you have any feedback or suggestions for Forgejo do not hold back, it is also your project.
Open an issue inthe issue trackerfor feature requests or bug reports, reach outon the Fediverse,
or drop intothe Matrix space(main chat room) and say hi!

### Donate

Forgejo is proud to befunded transparently. Additionally, it accept donationsthrough Liberapay. It is also possible todonate to Codeberg e.V.in case the Liberapay option does not work out for you, and part of the funding is used tocompensate for work on Forgejo.

However, the Liberapay team allows for money to go directly to developers without a round-trip to Codeberg. Additionally, Liberapay allows for a steady and reliable funding stream next to other options, a crucial aspect for the project. The distribution of funds through Liberapay istransparently controlled using the decision-making process, and Forgejo contributors are encouraged to consider applying to benefit from this funding opportunity.

Thank you for using Forgejo and considering a donation, in case your financial situation allows you to.
