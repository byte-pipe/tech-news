---
title: AI is making the nice version worth building · Jamie Lord
url: https://lord.technology/2026/09/14/ai-is-making-the-nice-version-worth-building.html
date: 2026-09-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:39:31.184587
---

# AI is making the nice version worth building · Jamie Lord

# AI is making the nice version worth building

## Main argument
- The cost of building separate native implementations for iOS and Android has traditionally kept many “nice‑to‑have” improvements in the backlog.  
- AI‑driven coding agents lower the effort required to create and maintain distinct implementations, making native rewrites more affordable.  
- When the implementation cost drops below the value of the user‑experience improvement, native development becomes a viable choice again.

## Evidence from industry
- **Shopify** migrated its mobile apps from React Native back to Swift/Kotlin in about twelve weeks; startup time fell 23 % on iOS and 50 % on Android, and the Android binary shrank by 109 MB.  
- **Apple** highlighted Notion’s migration to SwiftUI, showing that native investment can be justified when the long‑term benefits outweigh the initial cost.  
- AI tools accelerated the React Native development process, demonstrating that both cross‑platform and native paths benefit from reduced coding effort.

## Practical implications for teams
- The decision to reuse code versus build native features can now be tested quickly: rebuild a problematic flow, measure performance on real devices, and compare against maintenance overhead.  
- Smaller internal tools that previously failed cost estimates (e.g., a mobile companion for a 12‑person warehouse team) become feasible when AI cuts development and support expenses.  
- Teams can allocate saved time to polish existing experiences—fixing tablet layouts, improving launch speed on older phones—rather than only chasing headline features.

## Strategic considerations
- Shared libraries remain valuable for core business rules (order cancellation, permission checks, error handling) to ensure consistency across platforms.  
- As implementation cost declines, explicit product specifications, API contracts, and behavioral tests gain importance for defining what must be shared versus what can differ.  
- A testable, CLI‑driven architecture, as described by Shopify, lets agents exercise behavior without waiting for UI simulation, further speeding iteration.

## Takeaway
- AI is shifting the balance between cross‑platform convenience and native quality.  
- By making separate implementations cheaper, AI enables teams to revisit “nice‑to‑have” ideas, deliver better user experiences, and invest development effort where it truly adds value.