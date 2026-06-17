---
title: 'Volkswagen App: Page 3 - GrapheneOS Discussion Forum'
url: https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3
site_name: hnrss
content_file: hnrss-volkswagen-app-page-3-grapheneos-discussion-forum
fetched_at: '2026-06-17T19:45:49.653351'
original_url: https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3
date: '2026-06-17'
description: GrapheneOS discussion forum
tags:
- hackernews
- hnrss
---

Loading...

 This site is best viewed in a modern browser with JavaScript enabled.
 

 Something went wrong while trying to load the full version of this site. Try hard-refreshing this page to fix the error.
 

# Volkswagen App

### tux_

Do you really need a car app? You should be aware that modern cars carry a cellular modem and report extensive telemetry to the manufacturer, dealer, and possibly third parties. Cars can also be effectively remote controlled because of it. By connecting a phone to the car, you are just adding another exfiltration mechanism, and are allowing data to be exfiltrated even if you disabled or removed the cellular modem from the car.

### aaron94

BebefI mean the "Exploit protection compability mode" at "App Info" of the app.

### Maritime4165

The myVW app is still working for me again as of yesterday. I'd be glad to share any details that could help. All I can say is that I always ran the app in my Owner profile, once I realized it does work without play svcs (I ignored the error message and didn't care about the lack of a location map - but I did have a text based proximity location). Just to recap my steps to restore the app's functionality (besides location):

1). I deleted the Aurora store version of the app2). Installed a fresh version directly from the play store (that didn't work at first and crashed upon opening)3). Noticed my device had a GOS update pushed to it and completed that process4). Enabled Play services before launching the app5). Logged into the app, including the app pin, and confirmed the app was working as previously6). Exited the app and disabled G play svcs7). Launched the app again and had no issues getting to the home screen that showed my doors were locked, climate off, and the approximate location

Again, please lmk if I can provide any additional info that could help.

### iswrong

As reported above, it worked fine for me (with the Contacts access enabled in Play Services for syncing not to get stuck). Until they logged me out today and now there is no way to log in again.

### Postman

No chance anymore also for My SEAT. I tried Play Services with Google Account and this compatibility mode - nothing helps. Currently it shows "under maintenance" again, but the main reason is this new integrity check. We can only hope that VW changes their policy back to better compatibility. Older Android versions have been also cut off.For SEAT Mii these remote services via App are free of charge for 10 years, so it hurts not so much as having paid for this and now it is unusable.

### Overcook0708

Wrote an email to SEAT.

Please all consider writing as well, it did help for some other apps

### iswrong

Overcook0708Yep, also worth writing a review for their app in the Play Store, there are a couple of reviews that mention this issue already.

### Schiglip

I can only confirm the issue.It did work on GrapheneOS without anything Google up to a few weeks ago.It doesn't work anymore, not even with Google Play install and Google Play Services enabled. (I didn't try checking the contact permission etc). GOS reports that "Volkswagen used the Pay Integrity API"I contactedconnect-support@volkswagen.de(the address that I was suggested in reply to my Google Play review).For context, in my country, only one bank uses the "Play Integrity API". And even that bank does it in a way that that banking app still works with Google Play and Google Play Services.

### Schiglip

SchiglipI meant "Volkswagen used the Play Integrity API". Play, not Pay.

### iswrong

 

Hello XYZ,

Thank you for contacting Volkswagen Digital Services.

Please note that the use of the Volkswagen app is only supported on iOS devices and Android devices with supported operating system versions.

On devices on which alternative operating systems (so-called custom ROMs, e.g. GrapheneOS, LineageOS, or similar solutions) are installed, limitations or a lack of functionality of the Volkswagen app may occur. These systems are not part of the supported application environment of Volkswagen AG for the Volkswagen app, which is why we unfortunately cannot offer technical support in such cases.

The reason for this is that the Volkswagen app relies on security-relevant system components and certified Android standards to ensure reliable and secure use of our digital services.

Of course, we will be happy to assist you with any questions regarding the use of our official applications and services.

If you have any further questions about our digital services, please reply directly to this email. Further contact options can be found underhttps://contact.volkswagen.com. When calling, please mention your case number CASE_NUMBER so that we can help you as quickly as possible.

We wish you a safe journey with your Volkswagen MODEL at all times.

Best regards,Your Volkswagen Team

🫠

### foobar2026

iswrongI got the same text from VW support.

They also told me to check if my device is proofed as "play protect certified". For this you must go to the Play Store > Profile icon > Settings > About and then you can see that your graphene os device ist NOT certified.There exist a google play help site where the steps are described (https://support.google.com/googleplay/answer/7165974?hl=en#zippy=) as well as a funny advice what you should do when your device is not certified. Spoiler: You must flash the original, manufacturer-signed Android build that came pre-installed on your device.

For me the next step would be to complain at the european commission. I told this issue Google AI and it wrote me a very good complaint letter (I like the ironies), where there is mentioned the violation of EU Data Act, Violation of Interoperability & Digital Fairness.

### Taijian

Yeah, I got that same one. Wrote a reply re "security" when allowing Android 10 but banning GOS. Also let them know my next car could just as easily be a BMW, cause THEIR app does work on my phone.:shrug:

### xtti_f777

I don't know if it's related, but since v1.1.5, the MyHyundai app isn't working anymore. It crashes right upon startup. However, it's working on my other phones.

### rawrick

foobar2026I can only encourage people to do so, although I am not a fan of such "car apps" on my device.

« Previous Page