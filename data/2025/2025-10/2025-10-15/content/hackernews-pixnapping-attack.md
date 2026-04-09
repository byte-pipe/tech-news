---
title: Pixnapping Attack
url: https://www.pixnapping.com/
site_name: hackernews
fetched_at: '2025-10-15T19:08:14.046261'
original_url: https://www.pixnapping.com/
author: kevcampb
date: '2025-10-15'
---

* Paper
* Q&A

Pixnapping is a new class of attacks that allows a malicious Android app to stealthily leak information displayed by other Android apps or arbitrary websites.
Pixnapping exploits Android APIs and a hardware side channel that affects nearly all modern Android devices.
We have demonstrated Pixnapping attacks on Google and Samsung phones and end-to-end recovery of sensitive data from websites including Gmail and Google Accounts and apps including Signal, Google Authenticator, Venmo, and Google Maps.
Notably, our attack against Google Authenticator allows any malicious app to steal 2FA codes in under 30 seconds while hiding the attack from the user.

## Demo video

Your browser does not support the video tag.

## Research paper

The Pixnapping paper will appear in the 32nd ACM Conference on Computer and Communications Security (Taipei, Taiwan; October 13-17, 2025) with the following title:

* Pixnapping: Bringing Pixel Stealing out of the Stone Age

You can download apreprintof the paper and cite it via thisBibTeX citation.

The paper is the result of a collaboration between the following researchers:

* Alan Wang(University of California, Berkeley)
* Pranav Gopalkrishnan(University of Washington)
* Yingchen Wang(University of California, Berkeley)
* Christopher Fletcher(University of California, Berkeley)
* Hovav Shacham(University of California, San Diego)
* David Kohlbrenner(University of Washington)
* Riccardo Paccagnella(Carnegie Mellon University)

## Questions and answers

### What devices are affected?

We instantiated Pixnapping on five devices running Android versions 13 to 16 (up until build id BP3A.250905.014): Google Pixel 6, Google Pixel 7, Google Pixel 8, Google Pixel 9, and Samsung Galaxy S25.

We have not confirmed if Android devices from other vendors are affected by Pixnapping.
However, the core mechanisms enabling the attack are typically available in all Android devices.

### What are the attack requirements?

Any running Android app can mount this attack, even if it does not have any Android permissions (i.e., no permissions are specified in its manifest file).

### What information does the attack steal?

Anything that is visible when the target app is opened can be stolen by the malicious app using Pixnapping.
Chat messages, 2FA codes, email messages, etc. are all vulnerable since they are visible.

If an app has secret information that isnotvisible (e.g., it has a secret key that is stored but never shown on the screen), that information cannot be stolen by Pixnapping.

### Is Pixnapping being used in the wild?

We do not know.

### I am a user. How can I protect myself?

Make sure to install Android patches as soon as they become available.

### I am an app developer. How do I protect my users?

We are not aware of mitigation strategies to protect apps against Pixnapping.
If you have any insights into mitigations, please let us know and we will update this section.

### How does Pixnapping work?

The three steps a malicious app can use to mount a Pixnapping attack are:

1. Invoking a target app (e.g., Google Authenticator) to cause sensitive information to be submitted for rendering.
This step is described in Section 3.1 ofthe paper.
2. Inducing graphical operations on individual sensitive pixels rendered by the target app (e.g., the pixels that are part of the screen region where a 2FA character is known to be rendered by Google Authenticator).
This step is described in Section 3.2 ofthe paper.
3. Using a side channel (e.g.,GPU.zip) to steal the pixels operated on during Step 2, one pixel at a time.
This step is described in Section 3.3 ofthe paper.

Steps 2 and 3 are repeated for as many pixels as needed to run OCR over the recovered pixels and recover the original content.
Conceptually, it is as if the malicious app was taking a screenshot of screen contents it should not have access to.

### What Android APIs does Pixnapping exploit?

Pixnapping forces sensitive pixels into the rendering pipeline and overlays semi-transparent activities on top of those pixels via Android intents.
To induce graphical operations on these pixels, our instantiations use Android’s window blur API.
To measure rendering time, our instantiations use VSync callbacks.
For a more detailed explanation, we refer tothe paper.

### Does Google plan to patch these APIs?

Google has attempted to patch Pixnappingby limiting the number of activities an app can invoke blur on.
However, we discovered a workaround to make Pixnapping work despite this patch.
The workaround is still under embargo.

### What hardware side channel does Pixnapping exploit?

Pixnapping relies on theGPU.zipside channel to leak pixels.

### Do GPU vendors plan to patch the hardware side channel?

As of October 2025, no GPU vendor has committed to patching GPU.zip.

### Is there an assigned CVE for Pixnapping?

Yes. Pixnapping is tracked underCVE-2025-48561in the Common Vulnerabilities and Exposures (CVE) system.

### Are other operating systems affected by Pixnapping?

Android is vulnerable to Pixnapping because it allows an app to:

1. Send another app’s activities to the Android rendering pipeline (e.g., with intents).
2. Induce graphical operations (e.g., blur) on pixels displayed by another app’s activities.
3. Measure the pixel color-dependent side effects of graphical operations.

We have not investigated the applicability of these properties on other platforms yet.

### What is the app list bypass vulnerability?

It is another vulnerability we discovered that an app can use to determine if any other app is installed on the phone.
This information can be used to profile users.
Note that unlike prior app list bypass tricks (e.g.,[1]and[2]), nothing needs to be specified in the malicious app’s manifest file to exploit our app list bypass vulnerability.
For a more detailed explanation, we refer to Section 3.1 ofthe paper.

### Does Google plan to patch the app list bypass vulnerability?

As of October 2025, Google has not committed to patching our app list bypass vulnerability.
They resolved our report as “Won’t fix (Infeasible)”.

### Can I use the logo?

Yes. The Pixnapping logo is free to use under aCC0license.

* Download logo:SVG,PNG
* Download logo with text:SVG,PNG

### Did you release the source code of Pixnapping?

We will release the source code at this link once patches become available:https://github.com/TAC-UCB/pixnapping

## Timeline and news

October 13, 2025

 Google told
The Register
 that they will be issuing an additional patch for Pixnapping in the December Android security bulletin


September 19, 2025

 We disclosed to Samsung that Google's patch was insufficient to protect Samsung devices (from our original attack with no workaround)


September 11, 2025

 Google rated our workaround as
High Severity

September 8, 2025

 We disclosed our workaround to Google


September 4, 2025

 We became aware of the patch and later discovered a workaround to re-enable
Pixnapping

September 2, 2025

 Google released a patch for
Pixnapping
 (
release
;
acknowledgement
)


July 25, 2025

 Google assigned
Pixnapping

CVE-2025-48561

May 5, 2025

 Google rated our
app list bypass
 as
Low Severity
 and resolved the report as
Won't Fix (Infeasible)

April 23, 2025

 We separately disclosed our
app list bypass
 vulnerability (Section 3.1 of
the paper
) to Google


April 14, 2025

 Google rated
Pixnapping
 as
High Severity

February 24, 2025

 We disclosed
Pixnapping
 to Google
