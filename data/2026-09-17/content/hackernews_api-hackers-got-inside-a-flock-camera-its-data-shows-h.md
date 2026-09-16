---
title: Hackers Got Inside a Flock Camera. Its Data Shows How the System Really Works | WIRED
url: https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/
site_name: hackernews_api
content_file: hackernews_api-hackers-got-inside-a-flock-camera-its-data-shows-h
fetched_at: '2026-09-17T03:38:25.932058'
original_url: https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/
author: Dhruv Mehrotra
date: '2026-09-16'
published_date: '2026-09-16T10:30:00.000Z'
description: A hacker collective pulled down a Flock camera and dumped its data. The files included thousands of videos and logs showing that the device captured 1.6 million images of 50,000 vehicles in 21 days.
tags:
- hackernews
- trending
---

Save Story
Save this story
Save Story
Save this story

Hackers ripped downaFlock cameraabove a roadway, made a near-complete copy of the data stored inside it, and shared the files with404 Mediaand WIRED, revealing in new detail how exactly Flock Safety’s cameras track the movements ofboth vehicles and people. The hackers say they are also publishing details on how they managed to obtain the software, in the hopes that other people may copy them.

The breach provides an unprecedented look inside a system that Flock has described as protected byon-device encryption. The hackers were able to copy the camera’s storage and recover an encryption key stored on the device, which unlocked videos of thousands of vehicle detections. The hackers shared the material with 404 Media and the transparency nonprofitDistributed Denial of Secrets, which shared the data with WIRED. 404 Media and WIRED then analyzed those files as part of a joint investigation.

While much of the automatic license plate reader’s most sensitive storage remained encrypted and inaccessible, the joint analysis of the recovered data shows that software running on the device explicitly detects people as well as vehicles, license plates, and bicycles. The camera can produce dozens of images of a single passing vehicle and, according to several weeks of recovered logs, generated more than a million images. Its computer-vision software also sometimes isolated bumper stickers and other graphics, including, in one case, an American flag patch on a motorcyclist’s saddlebag.

The act of removing the camera and dumping its software shows that some people are not content with just destroying or removing the cameras. Across the country, multiple people have been arrested for allegedly tampering with or otherwise sabotaging Flock’s cameras. In response, some towns have announced that they are going to stop using Flock’s cameras altogether, and in one case, a police department evenmade a fake, 3D-printed Flock camera casein order to bait potential vandals.

“Why just destroy them when we can reverse engineer them and find the secrets of those spying on us?” one of the hackers, from a collective calling itself stegan0gram, said in an interview. “We liberated hardware in the field, disarmed them, and proceeded with reverse engineering of the cameras and associated solar equipment.”

Flock’s cameras photograph passing vehicles and send the images and other data to the company’s servers. There, Flock’s system presumably reads the license plate and can identify characteristics such as the vehicle’s color, make, and model. Flock then makes these time-stamped records searchable by whichever local agency owns or has access to the cameras. But in many cases, Flock’s system also allows other police departments from all over the country to search those cameras too, as part of the company’s national network. In Alpharetta, Georgia, for example,WIRED foundthat records from the city’s Flock cameras were accessible to more than 2,000 agencies, including police departments, colleges, airports, and, inexplicably, the Office of Inspector General for the federal General Services Administration.

This national network has been a selling point for Flock but also a deep source of controversy.404 Media revealedthat local cops were performing lookups in the national network on behalf of Immigration and Customs Enforcement, including in areas that banned working with immigration authorities ortransferring license plate dataout of state.404 Media also revealedthat a cop in Texas searched Flock cameras nationwide for a woman who self-administered an abortion. Those stories, among others, triggered a national conversation about whether people want Flock cameras, or automatic license plate readers more generally, in their communities.

And in the case of stegan0gram, the answer is clearly no.

The hackers said they were able to access the Android system on the camera and found two partitions—sections of its hard drive, essentially. A few of these were unencrypted, the hackers said, including one called “vendor” and another called “media.” The latter contained an encryption key that unlocked another part, which contained much of the media—the videos and stills—the camera took.

In early 2025, security researcher Jon “GainSec” Gainesreverse engineereda Flock license-plate reader and documented flaws that could be used to gain root-level access. After Gainesdisclosed his findings,the company acknowledgedthe findings but downplayed their severity, writing that the flaws required physical access to the device and that even someone who gained access to a camera “would still not be able to gain access to footage,” because images remained on the device only briefly after being transmitted to the cloud.

404 Media and WIRED analyzed the camera’s contents. The device’s processor is similar to those used in midrange smartphones, and it runs about 20 Flock-built apps that handle everything from detecting motion and taking pictures to classifying objects, uploading data, and receiving remote updates.

According to the code, when something moves into view, the camera takes a rapid series of photos. A typical passing vehicle generated about 28 images, though some produced more than 100. The camera uses different exposures to capture both the license plate and the wider scene, then scans the images, selects and crops useful frames, and sends them with other data to Flock over the cellular network. The camera itself does not appear to read the plate or identify the vehicle’s make, model, and color. That appears to happen on Flock’s servers.

According to our analysis, the camera’s logs recorded about 21 days of activity across several periods. During those windows, the device photographed roughly 50,200 vehicles and generated about 1.6 million images. On a typical day, it logged around 3,300 vehicles, with a high of 4,454. Those figures would vary considerably depending on where a camera is installed and how much traffic passes in front of it. The camera was almost certainly operating outside those periods, but older logs had been overwritten or were no longer recoverable from the device.

The software running on the camera explicitly detects people, somethingwhich is typically overlookedin discussions around Flock cameras. When it spots a person, it records where they appear in the image and how confident it is in the detection.

To test what the software could actually see, WIRED extracted the models from the camera’s files and ran them against test images and footage recovered from the device. The models readily detected people, including a selfie of a reporter. WIRED then ran them across 27,321 short videoclips stored on the camera. The clips were MP4 files, each about one to two seconds long, recorded at 1,024 by 768 pixels without audio. They were separate from the rapid bursts of higher-resolution still images the camera also takes as vehicles pass. The models detected people in 11 of the clips, all of them riding motorcycles. The small number is likely due to the camera’s position above a roadway, pointed down at passing traffic where pedestrians were unlikely to appear.

The tests also showed how broadly the camera’s license plate detector could interpret what it saw. In some cases it mistook bumper stickers, dealership frames, and other graphics for license plates and cropped them out as if they were plates. In one video of a passing motorcycle, the detector cropped an American flag patch on the rider’s saddlebag as if it were a plate.

Flock insists its cameras do not perform face recognition. WIRED and 404 Media found no evidence of any face-recognition capabilities in the camera’s software beyond ones included by default in the Android operating system. Those capabilities did not appear to be enabled or in active use.

In August,WIRED obtainedfrontend code for Flock’s police software, now called OS Investigate and previously known as Nightshift, and reconstructed portions of the tool. That software showed how Flock can use the records generated by its cameras, along with police files and commercial data, to identify drivers, surface vehicles that repeatedly travel together, and search for people based on patterns of movement. The data provides a view of the other end of a system.

A Flock spokesperson said in a statement: “The unauthorized removal and tampering of a Flock camera is illegal.” When asked specifically about the encryption key stored on the camera, the company added, “Flock takes security seriously and maintains a publicVulnerability Disclosure Policyfor security researchers to report potential vulnerabilities directly to us. We received no report through that process, and based on the limited information provided, we do not have enough detail to assess the claims being made. If the individuals identified legitimate vulnerabilities, we encourage them to submit their technical findings through our vulnerability reporting process so our security team can review them and take any appropriate action.”

One of the hackers said, “Being investigated is a legit concern and something we are trying to avoid. I'm sure our actions have attracted some attention as it is, but we are careful and try to keep a low profile.”

Noel Pichardo, a former Pawtucket, Rhode Island, police officer who becamean outspoken critic of Flockafter challenging his department’s use of the cameras, says he understands the activists’ frustration but worries that sabotaging devices could ultimately strengthen the case for them. “I think that type of vigilantism will only crystallize the police and the state at large in their belief that this tool is necessary,” Pichardo says. “The longer the state continues to ignore the groanings of their constituents who are against this type of surveillance, the more this will happen.”

The camera’s logs also show the camera struggling with storage. Its logs recorded more than 27,000 “no space left on device” errors while trying to save full-resolution images, along with tens of thousands of related errors, crashes, and reboots. At the same time, about every two minutes, code checked that the camera was still running and logged the message, “Who’s a good boy?!” More than 12,000 of those messages appear in the recovered logs.

When the camera did restart, another service left a final message in the logs: “A reboot was requested! ¡Adiós, Amigos!”

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:WIRED'smost ambitious, future-defining stories
* AI slop backlashis actually having an impact
* Big Story:The cop whotook on Flock
* The rise ofthe 1am job interview
* Watch:I stole a car by hacking this hidden device
Dhruv Mehrotra
 is an investigative data reporter at WIRED, where he uses technology to find, build, and analyze datasets for accountability journalism. His reporting has examined surveillance, policing, data brokers, platforms, and the government agencies and companies that use them.
Before joining WIRED, he worked at Bloomberg News, the Center for ... 
Read More
Senior Correspondent, Investigations
* bluesky
* X
Joseph Cox
 is an award-winning investigative journalist focused on generating impact. His work has triggered hundreds of millions of dollars worth of fines, shut down tech companies, and much more. ... 
Read More
404 Media co-owner and journalist

Topics
Flock
Police
privacy
surveillance
cameras
data
hackers
cybersecurity
security
Flock Has a Powerful New AI Tool for Police. We Got Its Code
Flock’s surveillance cameras have already sparked outrage. WIRED reconstructed its next-generation AI system, already in use by some police, to confirm it goes much further than tracking license plates.
Dhruv Mehrotra
Reverse-Lookup Service Exposed Millions of Photos of People’s Faces
The people-search tool ClarityCheck says its reverse image search service is “private and secure”—but it left a database containing more than 9 million image files exposed.
Lily Hay Newman
How an Atlanta Suburb Ended Up Sharing Flock Data With More Than 2,000 Organizations
Alpharetta, Georgia, cops share data with thousands of Flock users, ranging from federal agencies to a fish and wildlife commission. The reasons why show how vast—and invasive—the network has become.
Caroline Haskins
Lawmakers Want States to Crack Down on Flock Cameras—or Pay the Price
A new bipartisan effort in Congress to rein in automated license plate readers takes a page from the national drinking age: Comply, or risk losing federal highway funding.
Paresh Dave
OpenAI Agents Hacked Another Website
Plus: Tens of millions of US and Canadian drivers’ licenses go up for sale on the dark web, the US military finally tries to tackle the risk online ad data poses to troops, and more.
Lily Hay Newman
This Is Flock’s AI Search Tool for Cops
WIRED rebuilt Flock’s latest search tool from code the company sends to a police officer’s browser. Its AI can keep watch across multiple cameras for anyone fitting a written description.
Dell Cameron
ZuckOff Is a Free App That Sees Meta Glasses Before They See You
You can’t always tell if someone is recording you with their smart glasses, but your phone can help.
Megan Tomos 
Meta Failed to Catch Hundreds of AI Child Abuse Ads. Some Included Images of Real Kids
Images of real children—including a member of a European royal family—were used to create some of the 350 ads containing child sexual abuse. Lawmakers say they plan to investigate.
Matt Burgess
From Hacks to Bioweapons, Claude Misuse Is Now Everywhere
Plus: The US disrupts the internet’s biggest black market, a Conti ransomware hacker gets prison time, Meta fails to stop AI-generated videos of child abuse.
Andy Greenberg
San Francisco Orders Meta to Stop ‘Allowing’ AI Child Abuse Ads
The City Attorney’s Office has asked Meta to explain how the harmful ads repeatedly ran on Facebook and Instagram. The company claims the ads are not under the city’s jurisdiction.
Matt Burgess
‘I Felt Super Violated’: Men Wearing Meta Glasses on Dates Is an Instant Red Flag
As anxieties over surveillance tech grow, unsuspecting singles are sharing stories of being covertly filmed on dates by Meta smart glasses.
Jason Parham
Meta Ran Ads for an App That Promised to Nudify Female Politicians
One advertisement featured a pornographic video with a deepfake closely resembling a prominent US politician. Apple removed the app from the App Store after an inquiry from WIRED.
Vittoria Elliott