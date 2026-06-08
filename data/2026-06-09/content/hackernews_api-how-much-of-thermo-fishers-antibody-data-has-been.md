---
title: How much of Thermo Fisher’s antibody data has been manipulated? – Reese Richardson
url: https://reeserichardson.blog/2026/05/28/how-much-of-thermo-fishers-antibody-data-has-been-manipulated/
site_name: hackernews_api
content_file: hackernews_api-how-much-of-thermo-fishers-antibody-data-has-been
fetched_at: '2026-06-09T06:46:58.664295'
original_url: https://reeserichardson.blog/2026/05/28/how-much-of-thermo-fishers-antibody-data-has-been-manipulated/
author: mhrmsn
date: '2026-06-08'
published_date: '2026-05-28T17:11:37+00:00'
description: We've documented more than 450 instances of apparent data manipulation in Thermo's catalog
tags:
- hackernews
- trending
---

Research Integrity

## How much of Thermo Fisher’s antibody data has been manipulated?

Published by

Reese Richardson

on

May 28, 2026

[ TL;DR: As of 3 June 2026, we have identified more than 450 images bearing signs of manipulation in verification data advertised by Thermo Fisher Scientific in its online primary antibodies catalog (+1 by Abcam). See the full repository of problematic images, curated by myself and Sholto David, here:Zenodo – Problematic images in vendor antibody verification dataYou are welcome to contribute new findings atthis Google form.This blog post was original posted on 28 May 2026 and has not been edited to update counts since that date. There is an update covering Thermo Fisher’s response at the bottom of this post. ]

A week and a half ago, while looking for trustworthy data demonstrating a cell line’s deficiency in the protein p53,Sholto Davidcame across the following image of a Western blot in Thermo Fisher Scientific’s online antibodies catalog:

A Western blot presented as “Advanced Verification” data for an 
anti-p53 monoclonal antibody
.

This image is supposed to demonstrate thatthe antibody being soldworks as intended. It is labeled as“Advanced Verification”data on Thermo Fisher’s site and its caption implies that the data was produced internally (other images in the catalog that have not been produced internally are labeled under “Published Figures”).

This Western blot appears to be fabricated.As annotated by Sholto, several of the bands in the image are identical after flipping and rotation:

The bands labeled 1 through 4 are all identical to one another after a vertical flip, a horizontal flip or a 180 degree rotation.

Shortly after,Johan Duchênenoticeda similarly suspicious imageof another anti-p53 antibody in Thermo Fisher’s catalog. I decided to go looking myself andquickly turned upten more suspicious images on eight other antibody products offered by Thermo Fisher.

Sholto and I have now documented more than 100 images provided as verification data in Thermo Fisher’s antibody catalog that have apparently been manipulated. You can see all of them atthis Zenodo repository, which we’ll try to update regularly. This repository also contains a handful of instances that are less suggestive of manipulation, but the data is still problematic (e.g., the same image being presented as verification data for two different antibodies).

Here are some highlights:

Some images are similar to the example that started this excursion and also feature bands that are unusually similar to one another.

Many images, if you adjust the contrast, feature conspicuous “brushstrokes”, suggesting that part of the image has been painted over in a program like Photoshop.

Other images feature repetitive blocks of background noise, suggesting that parts of the image were copy-pasted over each other. They might also feature sudden unexpected discontinuities in the pattern of background noise.

In one instance, I thought I had stumbled across another one of these instances of duplicated blocks of background noise…

…only to discover that dozens of antibodies for sale from Thermo Fisher present a verification Western blot that features this exact background pattern, just with minimal edits such that the single band is positioned where one would expect to see the protein of interest.

A slideshow of contrast-adjusted Western blots all featuring “background pattern A”. 

At the time of writing, we’ve documented 50 instances of this background pattern appearing in verification data on Thermo Fisher’s site, but this is far from an exhaustive list. “Similar image” searches using Google Lens, Bing Images or DuckDuckGo betray hundreds more that we have yet to document.

Antibodies are near-ubiquitous but notoriously fickle laboratory reagents in biomedical research. For many applications, it is absolutely crucial that the antibodies that you use are selective (i.e., the antibody binds strongly to the target protein) and specific (i.e., the antibody binds to the protein of interest and little else). Commercially-available antibodies often fail to meet these criteria. Members ofYCharOS, an independent antibody validation initiative,estimated in 2024that “more than 50% of all antibodies failed in one or more applications”. Antibodies that don’t work as intended can delay experiments by weeks and non-specific antibodies are a massive source of irreproducibility in the biomedical literature. To learn more, check out Johan’sSeptember 2025 talkin which he details his experience with a study published using a non-specific antibody.

Antibody vendors like Thermo Fisher (probably the largest laboratory reagent supplier in the world) put verification data in their catalogs to demonstrate to scientists that the product works as intended. While signs of manipulation in this verification data don’t necessarily imply that the antibodies in question don’t work as advertised, without reliable verification data available, scientists will have no way of knowing until they have actually purchased the antibody. And antibodies are not cheap; at Thermo Fisher, a single vial containing a 0.1 mL aliquot of antibody solution typically costs 400 to 500 USD.

We createdour repositoryof problematic images in vendor antibody catalogs A) to raise awareness among working biomedical scientists that the antibody verification data they see in a vendor’s catalog may be unreliable and B) to encourage others to look for and report problematic vendor-provided antibody verification data (not limited to just Thermo Fisher). If you spot anything, feel free to fill out thisGoogle formso that it might be added to the spreadsheet and repository.

A parting message:always validate your antibodies!

UPDATE 8 June 2026:Thermo Fisher hasreleased a galling 15-point responseto our observations. The most important part (in my assessment) is quoted below (emphasis mine):

6. Did Thermo Fisher manipulate or fabricate antibody data?No.The Company fully stands by the data and underlying science. At Thermo Fisher Scientific, as the world leader in serving science, scientific integrity is a core value. The Company takes antibody validation, specificity and accurate product documentation seriously, and is committed to the transparent and ethical generation, analysis and presentation of scientific data.In the process of preparing antibody images for publication on its website, some images may have been adjusted to clarify for presentation purposes– not to alter or misrepresent the underlying experimental results. Thermo Fisher recognizes, however, that image adjustments of any kind can raise questions about data integrity, which is why moving forward, where an original image is not present or available, the Company will ensure that website users are informed thatantibody images may have been optimized for presentation and clarity on the website.

The phrase “antibody images may have been optimized for presentation and clarity on the website” is repeated on this FAQ page six times. I encourage readers to peruse the images collected in ourZenodo repositoryand decide what could and could not charitably be described as “optimization for presentation and clarity”.

### Share this:

* Share on X (Opens in new window)X
* Share on Facebook (Opens in new window)Facebook
* More
* Print (Opens in new window)Print
* Email a link to a friend (Opens in new window)Email
* Share on LinkedIn (Opens in new window)LinkedIn
* Share on Reddit (Opens in new window)Reddit
* Share on Tumblr (Opens in new window)Tumblr
* Share on Pinterest (Opens in new window)Pinterest
* Share on Telegram (Opens in new window)Telegram
* Share on WhatsApp (Opens in new window)WhatsApp
* Share on Mastodon (Opens in new window)Mastodon
Like
 
Loading…