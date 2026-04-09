---
title: Google flags Immich sites as dangerous | Immich Blog
url: https://immich.app/blog/google-flags-immich-as-dangerous
date: 2025-10-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-24T11:40:03.878894
screenshot: hackernews_api-google-flags-immich-sites-as-dangerous-immich-blog.png
---

# Google flags Immich sites as dangerous | Immich Blog

**Google flags Immich sites as dangerous**

* October 20, 2025
* By Jason Rasmussen

**Background:** Google offers a service called Safe Browsing, which tries to determine if a site is running malware, unwanted software, or performing social engineering. The service works with browsers like Chrome & Firefox.

**What happens if a site is marked as dangerous?**

* Most browsers use the Safe Browsing service to mark sites as potentially harmful.
* Only users who click on the "visit this safe site" link will see this warning and be able to view the site without any issues.
* If someone clicks on the link, they may be forced to download unwanted software or reveal personal information.

**Being flagged**

* Some Immich domains started receiving warnings due to their content being marked as potentially harmful by the Safe Browsing service.
* The issue affected both public sites and internal test environments like the Search Console account.
* Users could access their sites again after creating a Google account and requesting a review of the affected site through Google Search Console.

**Affected URLs**

* Specific website pages attempted to trick users into installing unwanted software or revealing personal information (e.g. login details).
* Notably, some URLs contained links that would force users to download browser extensions like Pupjuicer or Jumplink.
