---
title: GitHub - localsend/localsend: An open-source cross-platform alternative to AirDrop · GitHub
url: https://github.com/localsend/localsend
date: 2026-04-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-29T06:02:38.245720
---

# GitHub - localsend/localsend: An open-source cross-platform alternative to AirDrop · GitHub

# LocalSend – Open‑source cross‑platform alternative to AirDrop

## Overview
- Free, open‑source app for securely sharing files and messages over a local network.  
- No internet connection or third‑party servers required.  
- Communicates via a REST API protected by HTTPS; TLS certificates are generated on‑the‑fly for each device.

## Platforms & Compatibility
- **Android:** version 5.0 and above.  
- **iOS:** version 12.0 and above.  
- **macOS:** version 11 (Big Sur) and above (legacy support via OpenCore Legacy Patcher).  
- **Windows:** version 10 and above (last Windows 7 support in v1.15.4).  
- **Linux:** requires `xdg-desktop-portal` (GNOME) or `xdg-desktop-portal-gtk/kde` (KDE).  

## Download Options
- **Windows:** EXE installer, Winget, Scoop, Chocolatey, portable ZIP.  
- **macOS:** DMG, Homebrew, App Store.  
- **Linux:** AppImage, DEB, Snap, Flathub, AUR, Nixpkgs.  
- **Android:** Play Store, F‑Droid, APK.  
- **iOS:** App Store.  
- **Fire OS:** Amazon Appstore.  
- *Note:* The app does not have an auto‑update mechanism; using official distribution channels is recommended.

## Setup & Network Requirements
- Usually works out of the box.  
- If sending/receiving fails, adjust firewall:
  - Allow inbound TCP/UDP on port 53317.  
  - Allow outbound TCP/UDP on any port.  
- Disable AP isolation on the router (often disabled by default).  
- Windows: set network profile to “private”.  
- macOS/iOS: enable “Local Network” permission in Privacy settings.

## Portable Mode & Hidden Start
- **Portable mode (v1.13.0+):** create an empty `settings.json` file in the same directory as the executable; settings are stored there instead of the default location.  
- **Start hidden (v1.15.0+):** launch with `--hidden` flag (e.g., `localsend_app.exe --hidden`).  
- In v1.14.0 and earlier, the app starts hidden when the `autostart` flag is set and hidden mode is enabled.

## How It Works
- Devices exchange data over HTTPS using a locally generated TLS/SSL certificate.  
- All communication stays within the local network, ensuring speed and privacy.

## Getting Started (Building from Source)
1. Install Flutter (use the version specified in `.fvmrc` or manage with `fvm`).  
2. Install Rust.  
3. Clone the LocalSend repository.  
4. Navigate to the project directory.  
5. Run `flutter pub get` to fetch dependencies.  
6. Run `flutter run` to launch the app or use platform‑specific build commands.

## Contributing
- **Translation:** use Weblate or edit JSON files in `app/assets/i18n`. Files ending with `_missing_translations_<locale>.json` or `strings_<locale>.i18n.json` hold translatable strings.  
- **Bug fixes:** submit a pull request with a clear description of the issue and the fix.  
- **Improvements:** open an issue first to discuss the proposed change.  
- Detailed guidelines are in `CONTRIBUTING.md`.

## Troubleshooting
| Issue | Affected Platform(s) | Suggested Solution |
|-------|-----------------------|---------------------|
| Device not visible | Any | Disable AP isolation on router. |
| Device not visible | Windows (receiver) | Set network as “private”. |
| Device not visible | macOS, iOS (receiver) | Toggle “Local Network” permission in Privacy settings. |
| Slow transfer speed | Any | Use 5 GHz Wi‑Fi; disable encryption on both devices. |
| Slow transfer speed | Android | Known issue (see `flutter-cavalry/saf_stream#4`). |

## Building for Each Platform (maintainer commands)
- **Android:** `flutter build apk` (traditional) or `flutter build appbundle` (Google Play).  
- **iOS:** `flutter build ipa`.  
- **macOS:** `flutter build macos`.  
- **Windows:** `flutter build windows`; for MSIX packages use `flutter pub run msix:create` (store‑ready with `--store`).  
- **Linux:** `flutter build linux`; create AppImage with `appimage-builder --recipe AppImageBuilder.yml`; Snap instructions are in `localsend/snap/README.md`.

## License & Credits
- Licensed under Apache‑2.0.  
- Community: 4.3 k forks, 79.7 k stars, 309 watchers.  
- Contributions welcomed from developers, translators, and users.