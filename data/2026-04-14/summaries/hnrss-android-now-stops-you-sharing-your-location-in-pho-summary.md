---
title: Android now stops you sharing your location in photos – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/
date: 2026-04-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-14T06:05:30.974901
---

# Android now stops you sharing your location in photos – Terence Eden’s Blog

# Summary of “Android now stops you sharing your location in photos”

## Problem Overview
- The author runs **OpenBenches**, a site that relies on EXIF geolocation data embedded in photos of memorial benches.
- Recent changes in Android prevent browsers from accessing that EXIF location data when users upload photos.

## Technical Changes on Android
- **Original method**: `<input type="file" accept="image/jpeg">` opened the photo picker and preserved EXIF data.
- **First change**: Google forced the use of a generic file picker (`<input type="file">`), which allowed any file type but still passed EXIF data.
- **Second change**: The generic file picker also stopped passing EXIF data, breaking the workflow.
- Progressive Web Apps, Bluetooth/QuickShare, and email sharing now strip location information as well.
- The only reliable way left is to copy the photo via USB to a computer and upload it through a desktop browser.

## Stated Reasons from Google
- **Privacy concerns**: Users may unintentionally share precise location data (e.g., photos of children, jewelry, etc.).
- Google argues that most social platforms already strip location data automatically, reducing risk.

## Impact on OpenBenches
- Users can no longer simply select a photo on their phone and have the bench’s location auto‑filled.
- The site would need to ask users to manually enter coordinates or develop native mobile apps to request the special permission for reading EXIF geotags.

## Potential Workarounds Discussed
- A pop‑up permission prompt (“This website wants to see the location of your photos…”) – but concerns about prompt fatigue and unclear wording.
- Developing native Android (and possibly iOS) applications to obtain the necessary permission.
- Using zip files to preserve EXIF when sharing via apps that strip metadata (as mentioned in a comment).

## Community Reactions (selected comments)
- **Andrea Grandi**: Similar project; reluctant to build an Android client because of this limitation.
- **Josh Reimer**: Supports the privacy change; prefers that random websites cannot read location data.
- **Alex Kirk / Nick Fitzsimons**: Suggest using the Geolocation API at upload time, but note it gives the upload location, not the capture location.
- **Roel van der Plank**: Works around stripping by zipping the image before sharing.
- Others express frustration with lack of advance notice and call for a toggle or override.

## Author’s Outlook
- No clear solution yet; hopes for a browser‑level permission mechanism or community‑driven workaround.
- Invites comments from anyone who has found a method to retain full EXIF data in Android web uploads.
