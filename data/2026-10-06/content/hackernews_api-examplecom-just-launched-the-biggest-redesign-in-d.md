---
title: Example.com Just Launched The Biggest Redesign In Decades | DebugBear
url: https://www.debugbear.com/blog/example-dot-com-redesign-history
site_name: hackernews_api
content_file: hackernews_api-examplecom-just-launched-the-biggest-redesign-in-d
fetched_at: '2026-10-06T17:04:36.648681'
original_url: https://www.debugbear.com/blog/example-dot-com-redesign-history
author: jgx0
date: '2026-10-05'
description: A look at the history of visual changes to example.com.
tags:
- hackernews
- trending
---

example.comis a reserved domain name set aside by the Internet Assigned Numbers Authority (IANA) for documentation purposes. It has been available as an example URL for developers and writers since the late nineties.

While the overall messaging of the page has been consistent over time, the visual appearance has received several major overhauls.

In this article, we take a look at the recent changes as well as the evolution ofexample.comover the last 20+ years.

Your browser does not support the video tag.

## What changed on 28 September 2026?​

Until 28 September 2026, example.com was a static English-language page. The redesign introduces multi-language support using JavaScript, showing the content in a new language every 5 seconds.

Example.com shows an explanation of the site's purpose in English, Arabic, Chinese, French, Russian and Spanish. This is the English-language message:

This domain is for use in documentation examples without needing permission. This is not a service, avoid relying on it for testing and monitoring purposes.

Along with introducing multi-language support, the JavaScript code also inserts an SVG book icon.

### How does the language transition animation work?​

The new site doesn't just replace the content when showing the next language. Instead, there's a gradual opacity transition.

The opacity animation itself just usestransition: opacity .4s;. But how is the character-by-character transition implemented?

Each character is wrapped in its ownspanelement, and eachspangets a slightly largerCSStransition-delaythan the one before it. That means each character's opacity animation happens at a slightly different time.

## More changes on 3 October 2026​

Example.com has now removed the animation and shows all languages right from the start:

## Statement from IANA​

IANA provided the following statement explaining the reasoning behind the recent changes:

The changes we make to the site from time-to-time are usually informed by a desire to either reduce the overall bandwidth demands of serving the site, or improve its utility. At its heart it is a placeholder for a site no-one should be accessing, but we have historically showed a message there to inform visitors about why the domain is registered and how they may use it.

As it tends to be heavily trafficked, the overall bandwidth is a key consideration, and to that end one of the changes we made this week was to split the page content into a more basic page, augmented by a separate Javascript file with additional content beyond that. Since most of the traffic to the site is automated it tends not to fetch the Javascript file, reducing overall data requirements.

The fundamental purpose of the domain is for use in documentation, such as illustrative examples you may find in instructions. We know that people may, for example, cut-and-paste a sample configuration file and forget to customize entries that contain an example domain, and we expect we get some incidental traffic from that. However, the domain isn't intended to be a general purpose endpoint for things like availability testing so we do not encourage that kind of usage. There is no requirement there is a HTTP service present on the host in order to fulfill its purpose, we just operate it as a courtesy.

## January 20, 2002: What did the earliest version look like?​

According toWikipedia, theexample.comwebsite launched on January 1, 1999. The earliest version available to view in the Wayback Machine is from January 20, 2002.

The earliest version of the website only featured a list of domain names reserved by the Internet Corporation for Assigned Names and Numbers (ICANN) and IANA.

In the .com, .net, and .org top-level domains (TLDs), various domain names are reserved. These names are reserved from initial registration, but to the extent they are already registered the existing registrant may renew them.

Structurally, the HTML used a table layout, with the ICANN logo positioned in the top left corner of the page.

The server headers show that the site used Apache 1.3.22 at this point.

## March 28, 2002: simplified messaging​

The first version of theexample.comwording we recognize today came 67 days after the first available screenshot:

You have reached this web page by typing "example.com", "example.net", or "example.org" into your web browser.

These domain names are reserved for use in documentation and are not available for registration.

## February 7, 2003: RFC 2606 citation added​

In February 2003, the content was amended to include a link toRFC 2606, the official document for reserved top-level and second-level domains, so visitors could find more information on the website's purpose.

There was also a small technical change around this time: the server was upgraded to Apache 1.3.27 on Red Hat Linux.

## July 30, 2010: .edu added to domain list​

The website then went unchanged for seven years. On July 30, 2010, a slight change was made:example.eduwas now pointed to the landing page, alongside the three previous domains.

## July 29, 2013: migration and landing page redesign​

From January 2011,example.comdidn't serve its own page. Instead, it redirected visitors to a page on IANA's website.

That changed on July 29, 2013, when the redirect was removed andexample.combegan serving its own page from the EdgeCastContent Delivery Network (CDN)instead of Apache, alongside a major redesign of the landing page. The new design used a rounded card with an<h1>reading 'Example Domain' and a new description of the website's purpose.

The viewable domain list was now gone, with a link to IANA's website for more information.

## October 17, 2019: font and copy changes​

A new update came six years after the biggest change in the website's history. The layout remained the same, but the font stack was modernized to include more fallback fonts for devices such as Macs, iPhones, and Windows PCs.

The copy was tweaked slightly, with 'is for use in illustrative examples' replacing 'established to be used' and 'in literature' replacing 'in examples'.

## January 15, 2025: infrastructure switch​

Almost twelve years after the switch from Apache to the EdgeCast CDN, another infrastructure change took place: theServerheader disappeared entirely. Theresponse headersalone don't reveal which platform was serving the page at this point.

A change of provider around this time isn't surprising. EdgeCast had been acquired from Yahoo by Limelight Networks in 2022 and rebranded as Edgio. Edgio then filed for Chapter 11 bankruptcy in late 2024, with Akamai acquiring select Edgio customer contracts.

## October 9, 2025: redesign​

Later in 2025, the page was redesigned. The card design was dropped, and the HTML was minified. The copy was changed to a more direct message, again linking to IANA's website, with the link text changed from 'More information...' to 'Learn more'.

## December 17, 2025: Cloudflare migration​

Less than a year after the previous switch, the infrastructure changed again: the site now serves fromCloudflare, as indicated by thecloudflareserver header andCF-RAYheader in the response. Whatever platform served the page after the January 2025 change, it has now been replaced with a Cloudflare-fronted setup.

## June 9, 2026: favicon and HTML tweaks​

The next update, on June 9, 2026, brought no visual changes. The only HTML changes on the page itself were a favicon tag being added and the<p>tags being closed. The page now includes an empty favicon:

<link rel="icon" href="data:," />

This avoids a lot of unnecessary requests, as otherwise browsers look for a favicon at/favicon.ico.

## Avoid relying on it for testing and monitoring purposes​

Example.com first introduced an "Avoid use in operations" message in 2025.

For developers, it's tempting to useexample.comto check if the network is working or test HTTP requests. The example server likely receives a lot of traffic through this.

However, as the page now clarifies, it's not a service you can rely on. When we look at ouruptime monitoringdata, we can see that every now and then the example.com server doesn't respond correctly.

Using infrastructure that your organization controls can be more reliable.

## Conclusion​

Looking at the visual timeline, we can see that changes toexample.comhappen sporadically. Sometimes a couple of small tweaks happen in back-to-back months. Other times the website remains untouched for periods of up to seven years.

We have beenmonitoring the pagefor several years in our public demo project. TheChrome UX Report (CrUX) datashows how page speed has changed over time.

To learn more about how your website is performing,sign upfor a free 14-day DebugBear trial.

## Monitor Page Speed & Core Web Vitals

### DebugBear monitoring includes:

* In-depth Page Speed Reports
* Automated Recommendations
* Real User Analytics Data
Start Free Trial
Go To App

## Get a monthly email with page speed tips