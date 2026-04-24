---
title: 360-degree cameras have a new superpower | The Verge
url: https://www.theverge.com/tech/914730/splatica-gaussian-splats-insta360-antigravity
site_name: newsfeed
content_file: newsfeed-360-degree-cameras-have-a-new-superpower-the-verge
fetched_at: '2026-04-24T19:51:31.850720'
original_url: https://www.theverge.com/tech/914730/splatica-gaussian-splats-insta360-antigravity
author: Sean Hollister
date: '2026-04-24'
published_date: '2026-04-24T15:30:00+00:00'
description: The Verge tries Splatica, which uses Insta360 cameras, Antigravity drones, and Gaussian splats to help creators easily reconstruct real-world scenes in 3D.
tags:
- the-verge
- cameras
- drones
- gadgets
---

* Tech
* Gadgets
* News

# 360-degree cameras have a new superpower

Insta360 cameras and Antigravity drones can use Gaussian splats to digitize little chunks of the world.

Insta360 cameras and Antigravity drones can use Gaussian splats to digitize little chunks of the world.

by
 
 
Sean Hollister
Apr 24, 2026, 3:30 PM UTC
* Link
* Share
* Gift
Image by Vjeran Pavic / The Verge
Sean Hollister
 
is a senior editor and founding member of The Verge who covers gadgets, games, and toys. He spent 15 years editing the likes of CNET, Gizmodo, and Engadget.

Imagine Google Street View, except you can walk around like it’s a video game. Now imagine you don’t need to wait for Google to come film because it’s completely DIY. Insta360, the leading maker of 360-degree cameras, is now partnered with a 12-person UK startupcalled Splaticato help creators do just that.

Last January,we wrote about Gaussian splatting, the tech that promises to someday let anyone digitally re-create chunks of the real world in photorealistic 3D. But Splatica is making it surprisingly easy to harness splatstoday— with nothing more than an off-the-shelf consumer 360-degree camera and a subscription service that handles everything else.

This is not a video. This is a 3D digital re-creation of my backyard that I can explore like a video game level.
 
Video by Sean Hollister / The Verge

When I say “surprisingly easy,” I mean it — this is all I had to do:

* Change two settings on an off-the-shelf Insta360 camera or Antigravity drone
* Record a video while walking (or flying) around the area
* Sign up for a Splatica account and upload the video
* Wait a day for a miniature 3D world to appear in my web browser

I tried it with both anInsta360 X5 cameraand anAntigravity A1, and you can check out my results below. While they’re definitely not perfect — splats can often look a bit ethereal, like you’re stepping into a CG painting — I’m already convinced some creators and businesses will buy 360-degree cameras for this purpose alone. Insta360 cofounder Max Richter tells me the company’s cameras were already in demand for real estate virtual tours, construction progress reports, and facility inspections — if I were a real-estate agent, I’d buy one for this feature right now.

Here’s my Antigravity A1 capture ofa giant play structurein my local park (use the WASD keys on a keyboard to fly and a mouse to steer, or drag the onscreen controls on a phone):

▶

Tap to load Splatica

And thebeat-up basketball hoopat another park down the road. Splatica automatically edits out most people in the scene, so the park’s a little emptier than it was in reality.

▶

Tap to load Splatica

If you tap the path button in the upper-right-hand corner, underneath “SD” and “HD,” you should see the exact winding path I took with each camera (and the Insta360 X5’s selfie stick) to create these results.

When I simplycircle around the hoop once, as you can see below, it doesn’t look nearly as good. Splatica can only re-create what your camera sees, so you need to film from every place you might want to “stand” in the virtual world.

▶

Tap to load Splatica

Below, I tried to simulate a basic bridge inspection at the same park,focusing on one pillarunderneath the BART commuter rail. I’m not sure it has enough detail to satisfy real surveyors or safety inspectors — perhaps that’s because the drone’s overzealous obstacle avoidance kept pausing my flight.

▶

Tap to load Splatica

But when I spent over five minutes capturing my own backyard with the X5, the results were so expansive my wife and I didn’t feel quite feel comfortable sharing the whole scan. Instead, check out how Splatica re-created all the objects in my backyard by generating a 3D point cloud:

You can summon point clouds for any Splatica scene by pressing X on a desktop keyboard, by the way.

All of these scans can be downloaded in PLY and USDZ format and associated with real-world measurements: Splatica cofounder Andrey Shelomentsev tells me there’s typically a one percent error every 100 centimeters, “good enough for surveying and some rough exploration of the space,” and says measurements can be more accurate by placing some markers around an area.

This actually isn’t the first time I’ve tried to 3D scan my backyard: in 2021,I did it with a Skydio self-flying drone. But back then, Skydio was charging $2,999 per year for the feature, not including a drone or a service to stitch the photos together, while Splatica claims its service does it all autonomously with a normal 360-degree video.

Splatica’s own sample scenes are even more interesting than mine, particularly now that it’s trying to prove companies can use its service to train robots before deploying them for real in factories around the world. Here’s theImecar Elektronik factoryin Antalya, Türkiye:

▶

Tap to load Splatica

And for something completely different, here’spart of the Leighton Housein London:

▶

Tap to load Splatica

How is this possible just by walking around with a camera? Shelomentsev tells me his company’s built a proprietary version of SLAM (the Simultaneous Localization and Mapping techniquethat lets all kinds of robots, self-driving cars, and VR headsets know their position in 3D space) specifically designed to create accurate point clouds from 360-degree video. You can think of point clouds as the “bones” of 3D objects that then get painted with color.

And while Splatica says it can work with any 360-degree camera, it helps that Insta360 and Antigravity’s cameras put all kinds of extra metadata into the video files themselves. “The files carry everything we need: lens distortion parameters, shutter speed, accelerometer and gyroscope data, and GPS — streamed from the Insta360 mobile app directly to the camera during capture,” Splatica CEO and cofounder Eugene Nikolskii tellsThe Verge.

Above: Corridor Crew visually explains how splats work.

The Insta360/Splatica combo does have its limitations. If you zoom into any of my embedded or linked examples to see fine details, you’ll probably see slightly translucent blobs of color rather than legible textures — that’s how splats are made, after all. Traditional high-res photogrammetry might do a better job if surfaces are what you care about most.

But that isn’t stopping Insta360, Antigravity, and Splatica from launching a marketing campaigncalled Project Eternal, which the companies are touting as a “global initiative” to preserve cultural landmarks for future generations. It’s offering prizes for the best Gaussian splats, 1,000 free Splatica uploads (first-come first served), and a pilot project to scan Pompeii and the stunningCivita di Bagnoregioin Italy. They’re also “inviting creators worldwide” to scan sites like Roman theaters and Korea’s Jeju Island.

(The companies wouldn’t tell us how much they’re investing in Project Eternal, and admitted they’re not helping creators secure permits for those locations — but Splatica claims it’ll maintain public access indefinitely to any scene submitted to its “Open Heritage Dataset,” and the company’s got adecent privacy policythat makes it clear your content belongs to you.)

Beyond that, Insta360’s Richter says his company already has enterprise customers piloting 3D reconstruction and digital twin workflows in the construction and facilities management realms, and hopes to provide richer data from the camera to 3D reconstruction services and make the process more seamless.

Right now, the biggest barrier to entry with Splatica might be that the service isn’t cheap. The company charges anywhere between 18 cents and 25 cents per second of processed video, and you have to pay a monthly subscription too. The company’s currently experimenting with pricing — last week it was $70, $200, or $385 per month depending on how big a scan you need, while this week the same tiers are $50, $150, and $300.

But if you want to give it a try, you might still be able to get one of the 1,000 free slots. Splatica says it’s waiving its subscription fee for those first 1,000 users, who should each be able to turn around 10 minutes of 360-degree footage into little 3D worlds. You can also explore over 100 additional splats inSplatica’s public gallery.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Sean Hollister
* Cameras
* Drones
* Gadgets
* Hands-on
* News
* Report
* Reviews
* Tech

## Most Popular

Most Popular
1. You’re about to feel the AI money squeeze
2. Microsoft brings Xbox back, scraps Microsoft Gaming
3. Leak reveals new Xbox Game Pass ‘Starter Edition’ that’s part of Discord Nitro
4. THE PEOPLE DO NOT YEARN FOR AUTOMATIONVideo
5. Anthropic’s Mythos breach was humiliating

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our
 
Terms
 and 
Privacy Notice
. 
This site is protected by reCAPTCHA and the Google
 
Privacy Policy
 
and
 
Terms of Service
 
apply.
Advertiser Content From

This is the title for the native ad

## More inTech

Google’s handsome Pixel Watch 4 is on sale for $40 off in both size configurations
The RAM shortage could get even worse if Samsung labor protests cut production
Tesla’s Cybercab goes into production — so why is Musk tapping the brakes?
AirPods, Touch Bars, and the rest of Tim Cook’s legacy
The Trump phone still isn’t real
A new Republican privacy bill could be ‘worse than no standard at all’
Google’s handsome Pixel Watch 4 is on sale for $40 off in both size configurations
Brandon Widder
Two hours ago
The RAM shortage could get even worse if Samsung labor protests cut production
Stevie Bonifield
Two hours ago
Tesla’s Cybercab goes into production — so why is Musk tapping the brakes?
Andrew J. Hawkins
3:17 PM UTC
AirPods, Touch Bars, and the rest of Tim Cook’s legacy
David Pierce
2:43 PM UTC
The Trump phone still isn’t real
Dominic Preston
2:00 PM UTC
A new Republican privacy bill could be ‘worse than no standard at all’
Lauren Feiner
1:00 PM UTC
Advertiser Content From

This is the title for the native ad

## Top Stories

12:00 PM UTC
Elon Musk and Sam Altman’s courtroom brawl could burn it all down
2:00 PM UTC
I don’t think Gwyneth Paltrow knows what a peptide is
2:00 PM UTC
The Trump phone still isn’t real
3:17 PM UTC
Tesla’s Cybercab goes into production — so why is Musk tapping the brakes?
Apr 23
You’re about to feel the AI money squeeze
4 minutes ago
The person who allegedly leaked Paramount’s new Avatar movie has been arrested