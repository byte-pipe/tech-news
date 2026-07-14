---
title: Your ‘App’ Could Have Been a Webpage (so I fixed it for you…) – Dan Q
url: https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/
date: 2026-07-11
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:48:46.257341
---

# Your ‘App’ Could Have Been a Webpage (so I fixed it for you…) – Dan Q

# Summary of “Your ‘App’ Could Have Been a Webpage (so I fixed it for you…) – Dan Q”

## Why the app feels wrong  
- The Travelbound app is essentially static text, images, and PDF links that could be delivered as a simple webpage.  
- It adds two undesirable features:  
  1. Sends Google‑account tracking data back to the developers.  
  2. Shows “inspirations” advertisements for other trips.  
- A webpage would be:  
  - Copy‑pastable, printable, saveable, bookmarkable, searchable, device‑agnostic, and potentially more accessible.  

## Intercepting the app’s traffic  
1. Created a rooted Android Virtual Device (AVD) in Android Studio.  
2. Installed Magisk and configured it to grant `su` access automatically.  
3. Ran HTTP Toolkit, which installed a fake VPN to proxy the device’s traffic.  
4. Installed the Travelbound app from the Play Store and limited the proxy to that app.  
5. Discovered that the app builds a URL like `https://travelbound.api.vamoos.com/api/itineraries/{username}-{password}` and receives a JSON payload containing:  
   - Itinerary legs  
   - “Inspirations” advertisement entries  
   - References to images and other files  
6. Noted that S3 image URLs have short expirations, forcing periodic JSON refetches.  

## Turning the data into a better webpage  
- Wrote a Ruby script scheduled via cron to fetch the JSON and generate an HTML page.  
- Omitted the “inspirations” section and listed only:  
  1. Itinerary items  
  2. Files not referenced by inspirations (e.g., PDF download links)  
- Hosted the page behind the same password given to the tour group and embedded the raw JSON in `<details>` elements for future inspection.  
- Result: a ~0.05 MB page (plus optional images) versus a 43 MB app that can grow to 124 MB, with no tracking or ads and full web‑standard features.  

## Critique of “app culture”  
- Publishing HTML content as an app adds cost (store fees, development, maintenance) and reduces accessibility.  
- The app’s content is already HTML delivered over HTTP, so a webpage would be the natural medium.  
- Some use cases truly need native apps, but Travelbound is not one of them.  
- Users now have a clear choice: a bulky, tracked app or a lightweight, ad‑free webpage.  

## Key footnote takeaways (condensed)  
- Rooting the device was necessary to bypass certificate pinning for man‑in‑the‑middle interception.  
- The shared username/password is used by the whole tour group; security considerations appear minimal.  
- Images are cached locally by the app in an inefficient way, leading to large storage use.  
- Accessibility is likely worse in the app than in the simple web version.  

## Community reactions  
- 👍 137 👎 5 🤔 4 📵 11   (emoji‑only voting)