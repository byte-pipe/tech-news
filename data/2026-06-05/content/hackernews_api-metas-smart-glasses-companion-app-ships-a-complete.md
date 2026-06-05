---
title: Meta's smart glasses companion app ships a complete, dormant face-recognition pipeline on a stock account.
url: https://www.buchodi.com/meta-glasses-facial-recognition/
site_name: hackernews_api
content_file: hackernews_api-metas-smart-glasses-companion-app-ships-a-complete
fetched_at: '2026-06-05T19:36:40.614707'
original_url: https://www.buchodi.com/meta-glasses-facial-recognition/
author: buchodi
date: '2026-06-04'
published_date: '2026-06-04T17:09:58.000Z'
description: Meta's ships facial recognition on smart glasses
tags:
- hackernews
- trending
---

Stella is the companion app for Meta's smart glasses. Inspecting version273.0.0.21of the Android build (com.facebook.stella), I found the entire computational and storage stack for on-device facial recognition: three face models, a local database schema, a cosine-similarity vector index dimensioned to match the models, a write path that stages biometric records to disk, a fully wired notification surface, and a user-facing "Connections" widget.

I want to be precise about what that does and does not mean, because the gap between the two is important.

What I can demonstrate:the machinery is present, it is wired together. Several facial extraction and facial fingerprinting models are present and I was able run the recognition pipeline end-to-end on a test image and it detected a face, generate a 2048-dimension biometric embedding, searched a local index, and on a match fired an Android notification stating to the user "Person Recognized".To get the pipeline to run I invoked its existing handler directly with a test photo.

What I cannot demonstrate:that any of this is active for ordinary users. On a stock, unenrolled account the user-facing UI does not appear, and the screen the recognition notification deep-links to is missing from the build. I also did not observe Meta server-pushing identity data to the relevant database on my test account.

So this is not "Meta is secretly identifying the people you look at." It is: the complete apparatus to do exactly that is sitting on the device, assembled and functional, gated by Meta.

All findings below are reproducible againstcom.facebook.stellav273.0.0.21.

## Three face-recognition models ship on the device (~100 MB)

Three ExecuTorch (.pte) models arrive on the device via NMLML, Meta's asset-delivery system, downloaded from Meta.

Asset name (Meta's naming)

File

Size

Function

android_facerec_scrfd

SCRFD.pte

3.4 MB

Detects faces in an image

android_facerec_kps_aligner

KPSAligner.pte

117 KB

Crops and aligns each detected face

android_facerec_sface

SFace.pte

96 MB

Converts a face into a 2048-number embedding (the biometric fingerprint)

These map onto open-source architectures, the same model families that other apps and academic projects already use:

* SCRFDSample and Computation Redistribution for Efficient Face Detection(InsightFace, ICLR 2022). Reference implementation:github.com/deepinsight/insightface.
* SFaceSigmoid-Constrained Hypersphere Loss for Face Recognition(Zhong et al., 2021). Reference:github.com/zhongyy/SFace
* KPSAlignerkeypoint-based alignment, standard practice since 2015 (MTCNN, dlib, InsightFace).

Meta's SFace variant seems to be scaled larger than the public reference (96 MB vs. ~40 MB; 2048-dimension output vs. the reference's 128–512).Worth stating plainly:shipping detection and embedding models is not, by itself, evidence of recognition. Plenty of apps run on-device face detection for framing or autofocus.

## A cosine-similarity face index, dimensioned exactly to the on-device fingerprinter

The recognition pipeline that actually runs and reads into this database:

/data/user/0/com.facebook.stella/files/rldrive/person_profiles/objects.db

This lives underRLDrive, Meta's cross-device sync framework, in aperson_profilesnamespace designed to be populated remotely. I didnotdirectly observe Meta pushing data toperson_profilesspecifically on my test account. I want to be clear that I'm describing the channel's existence, not an observed transmission.

The schema:

CREATE TABLE person (
 nodeid INTEGER PRIMARY KEY,
 name TEXT, 
 uri TEXT, 
 blob BLOB,
 deleted INTEGER,
 version BLOB
);

CREATE TABLE face (
 nodeid INTEGER PRIMARY KEY,
 mediaPath TEXT, -- the face_id used in the deep link
 personUri TEXT, -- soft reference back to person.uri
 blob BLOB,
 deleted INTEGER,
 uri TEXT,
 version BLOB
);

CREATE VIRTUAL TABLE face_mediaPath_vec
 USING vec0(mediaPath float[2048] distance_metric=cosine);
 -- 2048-float biometric fingerprint per face, cosine-distance search
 -- (uses the sqlite-vec extension)

Eachfacerow points at apersonviapersonUri. Eachface.mediaPathis the primary key intoface_mediaPath_vec, which stores the 2048-number embedding. Recognition is a cosine-similarity query against that index, followed by a join intoperson.namefor the notification text.

A few things line up:

* vec0is the open-sourcesqlite-vecextension, which turns SQLite into a vector-similarity engine.
* The dimensionfloat[2048]is the exact output shape of the SFace embedder shipped on the app.
* Thecosinemetric is the standard choice for comparing face embeddings.

The schema permits multiplefacerows perpersonUri(noUNIQUEconstraint), but whether a production deployment uses one-to-one or one-to-many is not visible from a non-enrolled device.

End-to-end test confirms both branches and isolates where writes go.I SHA-256-snapshotted and row-counted the database, then ran the full recognition pipeline twice: once against an empty index (no-match), once against an index pre-loaded with a single embedding (match):

* No match(emptyface_mediaPath_vec): one(uuid.jpg, uuid.emb)pair was written toNameTagsPending/. No notification.
* Match: an Android notification fired through the productionnametags_recognitionchannel - title"Person recognized", body"Recognized Michel Foucault". Nothing was added toNameTagsPending/.

## Unrecognized faces are staged to disk: crop plus fingerprint inNameTagsPending/

When the device sees a face that the local index does not match, Stella writes it to:

/data/user/0/com.facebook.stella/files/NameTagsPending/

Each unrecognized face produces a pair of files named with a fresh UUID:

* a.jpg— the cropped, aligned face, the output of SCRFD + KPSAligner; and
* an.emb— the 2048-number SFace fingerprint.

The directory is mode0700and survives reboots. Writes happenonlyon the no-match branch; matched faces go to a notification and leave no on-disk trace.

I verified the embedding's structure directly:

File: NameTagsPending/1566ab46-[...].emb
Size: 8,192 bytes (2048 × float32, big-endian)
L2 norm: 0.999999 ← canonical L2-normalized face embedding
Min/max: −0.092110 / +0.098950
Mean: +0.000292

Together,(uuid.jpg, uuid.emb)is a complete, indexable biometric record of one face — the same shape and encoding the cosine index inperson_profiles/objects.dbis built to match against.

The nameNameTagsPendingmost literal reading is "faces pending a name" — biometrically encoded, awaiting a label. I'll note the structural fact and let it carry its own weight: a face image and its fingerprint, stored side by side in plaintext, mode0700, surviving reboots, is precisely the dataset you would assemble if you intended to retroactively identify faces once a label arrives.

The original photo 
the pipeline received as input (1970 portrait of Michel Foucault by Jerry Bauer, 1970, 318×418 px JPEG, 28 KB) Public domain, via 
Wikimedia Commons
.
The cropped face Stella's pipeline produced 
and wrote to NameTagsPending/. Output of SCRFD (detector) + KPSAligner (aligner). 83×118 px RGB JPEG, 4,396 bytes 

## The notification surface is fully wired

Stella defines a dedicated Android notification channel

NotificationChannel{
 id = "nametags_recognition"
 name = "NameTags recognition"
 description = "Notifications for recognized NameTags connections"
 importance = IMPORTANCE_HIGH (heads-up + sound + badge)
 sound = system notification sound
}

The notification template is hardcoded in the recognition handler. Title is always"Person recognized"; body is always"Recognized " + name, wherenamecomes from thepersontable inperson_profiles/objects.db:

NotificationCompat.Builder(ctx, "nametags_recognition")
 .setContentTitle("Person recognized")
 .setContentText("Recognized " + matched_name)
 .setAutoCancel(true)
 .setContentIntent(
 PendingIntent.getActivity(
 ctx,
 matched_name.hashCode(),
 Intent.ACTION_VIEW with
 Uri "fb-viewapp://name_tags?face_id=" + face_id,
 FLAG_IMMUTABLE | FLAG_UPDATE_CURRENT))
 .build()

NotificationManagerCompat.notify(matched_name.hashCode(), notification)

The notification is tappable: itscontentIntentis a deep link of the formfb-viewapp://name_tags?face_id=<face_id>, a Meta-authored URL scheme meant to open a person-profile screen inside Stella.

One honest caveat: in v273,I could not find that destination screen. Tapping the notification routes Stella to its default tab, because the target Compose destination is absent from the navigation graph. The notification fires; the screen it points at isn't built into this release.

## A user-facing "Connections" entry point exists in the APK

Stella v273 contains a widget rendering a card under a section header titled"Connections", with the text"See your connections"/"Remember the people you met and make new connections."Both strings are hardcoded literals in the APK not server-pushed.

On a stock, unenrolled account, the card doesnot appearon the Glasses tab at all. It became visible during testing. In normal use, a user would not see this.

## What this adds up to

1. The full on-device face-recognition stack: detection, alignment, embedding, vector index, storage, write path, and notification surface is present and assembled in Stella v273.
2. It is functional. Run end-to-end, it recognizes a known face and names it in a notification, and it stages unknown faces (crop + fingerprint) to disk.
3. The index dimension, embedding shape, and storage schema are mutually consistent, this is a coherent system, not stray dead code.
4. The pieces a user would actually touch: the "Connections" card and the profile screen the notification opens are either absent from the build or buried deeper.
5. The database the live pipeline uses sits in a sync namespace Meta populates server-side, alongside other namespaces it already populates, but I did not observe a push to the face namespace on my account.

What I amnotclaiming: that Meta is identifying strangers for users today, that enrollment data is flowing, or that any of this is enabled in production.

What's hard to wave away: building, shipping, and wiring this much apparatus down to an 2048-dimension facial fingerprinting and a hardcoded "Person recognized" notification, is an engineering investment. Capability that doesn't ship by accident. Whether and when it goes into production is Meta's to answer.

This research is published alongside reporting in WIRED.