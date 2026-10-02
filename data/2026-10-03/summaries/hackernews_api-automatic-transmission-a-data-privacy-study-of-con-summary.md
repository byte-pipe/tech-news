---
title: Automatic Transmission — a data-privacy study of connected vehicles
url: https://automatictransmission.khoury.northeastern.edu/index.html
date: 2026-10-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-03T03:07:35.067831
---

# Automatic Transmission — a data-privacy study of connected vehicles

# Automatic Transmission — a data‑privacy study of connected vehicles

## Research Questions
- What personal consumer data do connected vehicles and their companion mobile apps transmit?  
- Who receives that personal consumer data?  
- What is the manufacturer response to these findings?

## Methods
- Tested 21 U.S. market vehicles and 30 companion mobile apps from October 2024 to August 2025.  
- **Vehicle testing**:  
  - Created a custom Wi‑Fi access point on a Raspberry Pi and captured traffic with tcpdump.  
  - Conducted idle, active, and driving tests (5–45 mph).  
  - Blocked cellular signals for 11 EVs using a car‑sized Faraday tent (≈93 dB attenuation) to see if traffic rerouted to Wi‑Fi.  
- **App testing**:  
  - Used iPhone 8 (iOS 16.6), iPhone X (iOS 16.7.11), and iPhone 13 (iOS 18.5.0).  
  - Deleted non‑essential apps, installed each vehicle app individually, and recorded interactions with iOS screen recording.  
  - Captured and decrypted network traffic via mitmproxy with custom root certificates.  
  - Followed a standardized interaction flow: accept all permission requests, log in with existing credentials, exercise all app functions (e.g., locate vehicle, view service data, remote actions), and verify vehicle responses.

## Vehicle Dataset
- Estimated procurement cost: > $1.2 M (enabled by Consumer Reports partnership).  
- Sample includes models from GM, Stellantis, Fisker, Ford, Honda, Land Rover, Lexus, Toyota, Subaru, Lucid, Mercedes‑Benz, Nissan, Rivian, Tesla, Volvo, and others.  
- Tests recorded for each vehicle: driving, idle, in‑tent (cellular blocked), and cellular‑only where applicable.  
- Note: not exhaustive of all U.S. manufacturers; results represent a snapshot in time.

## Findings
- **Wi‑Fi transmissions**: 19 of 21 vehicles contacted at least one third‑party domain, many known for advertising and tracking.  
- **App transmissions**: 7 of 30 companion apps sent sensitive identifiers (VIN, email, phone number, precise location) to advertising/tracking third parties.  
- **PII aggregation**: Multiple PII elements sent to the same third party enable detailed consumer profiling.  
- **Impact of companion apps**: Pairing an app roughly doubled a vehicle’s exposure to advertising/tracking entities; some vehicles added 20 + new third parties.  
- **Manufacturer disclosures**:  
  - Responses largely shifted responsibility to consumers, citing lack of user‑choice mechanisms.  
  - Owners face limited options: accept data‑sharing terms, disable connected features, or abandon the vehicle.  
  - Honda was an exception, having revised its practices to stop sending precise geolocation to tracking third parties.

## Conclusion
- Connected vehicles routinely communicate with a broad ecosystem that includes first‑party manufacturer services and third‑party advertising/tracking services.  
- Network behavior varies even among models from the same manufacturer, complicating systematic privacy assessments.  
- The study highlights a significant visibility gap for consumers and a need for clearer consent mechanisms and regulatory oversight.