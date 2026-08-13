---
title: What’s new in Flutter 3.47 | The Flutter Blog
url: https://flutter.dev/blog/whats-new-in-flutter-3-47
date: 2026-08-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-14T06:01:21.352847
---

# What’s new in Flutter 3.47 | The Flutter Blog

# What’s new in Flutter 3.47

## Choose your own UI adventure
- Material and Cupertino widgets are now released as standalone packages (`material_ui` and `cupertino_ui`) at version 1.0 on pub.dev.  
- Decoupling lets the design systems ship bug fixes and new components on a weekly cadence, independent of the quarterly Flutter SDK releases.  
- Benefits:
  - Use the latest widget styles without upgrading the whole SDK.  
  - Faster contribution and release cycles.  
  - Foundation for a style‑neutral core widget catalog and custom design systems.  
- Migration:
  - Run `dart fix --apply --code=migrate_design_widgets` to update imports automatically.  
  - If `pubspec.yaml` is not updated, add the packages manually with `flutter pub add material_ui` (and `cupertino_ui` if needed) and rerun the fix command.  
- Compatibility bridge:
  - `MaterialUiCompatibilityBridge` allows apps to work with the new packages even when some dependencies still use the legacy core imports.  
- Localization:
  - `flutter_localizations` is unbundled; localization delegates now live in the respective standalone packages.  
  - Import `package:material_ui/material_ui.dart` and use `GlobalMaterialLocalizations.delegates`, which now includes Cupertino and widget delegates.  
- Contribution:
  - The freeze on core library contributions is lifted; weekly releases and community contributions are now open for both packages.

## Prepping for the next wave of Apple updates
- Minimum OS versions increased:
  - iOS 15 (up from 13)  
  - macOS 12 (up from 10.15)  
- Xcode 27 / iOS 27 / macOS 27 support:
  - UIScene lifecycle is mandatory; Flutter CLI migrates most apps automatically, but manual migration is required for custom native code or plugins.  
- Intel Mac support is being phased out:
  - Automated tests on Intel hardware disabled.  
  - CLI warns on Intel builds; warnings will become errors later.  
  - Enable ARM64‑only macOS builds with `flutter config --enable-macos-arm64-only`.  
- Swift Package Manager (SwiftPM) progress:
  - 92 of the top 100 iOS plugins have migrated to SwiftPM.  
  - CocoaPods is now in maintenance mode; unmigrated plugins will lose functionality and pub.dev scores.  
  - Re‑enable SwiftPM with `flutter config --enable-swift-package-manager`.  
- Build‑time improvements contributed by community member `lukemmtt` through early filtering of unnecessary SwiftPM schemes.

## Setting course for Wasm by default
- Ongoing work to make WebAssembly the default target for Flutter web, aiming for native‑like performance in browsers.  
- Developers are encouraged to test web apps with the upcoming Wasm defaults.