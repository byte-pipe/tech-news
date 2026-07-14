---
title: 'GitHub - AIEraDev/Clypra: A modern video editor built with Tauri, React, and TypeScript. Focus on building free capabilities of premium capcut functionalities · GitHub'
url: https://github.com/AIEraDev/Clypra
site_name: github
content_file: github-github-aieradevclypra-a-modern-video-editor-built
fetched_at: '2026-07-14T11:32:40.875700'
original_url: https://github.com/AIEraDev/Clypra
author: AIEraDev
description: A modern video editor built with Tauri, React, and TypeScript. Focus on building free capabilities of premium capcut functionalities - AIEraDev/Clypra
---

AIEraDev

 

/

Clypra

Public

* NotificationsYou must be signed in to change notification settings
* Fork270
* Star2.4k

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,026 Commits
1,026 Commits
.github
.github
 
 
.vscode
.vscode
 
 
android
android
 
 
ios
ios
 
 
public
public
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLA.md
CLA.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
FAQ.md
FAQ.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
capacitor.config.ts
capacitor.config.ts
 
 
components.json
components.json
 
 
index.html
index.html
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

# Clypra

Professional video editing—free and open source forever.

A modern video editor built on Tauri v2, React 19, and Rust. Hardware-accelerated processing, cross-platform (desktop + mobile), with optional AI-powered features.

 
 
 

Features•Architecture•Installation•Development•Contributing•Open Core

## Overview

Clypra is afree, open-source video editor(MIT License) with professional-grade features. The core editor, effects engine, and all UI components are free forever—no watermarks, no feature limits, no subscriptions required.

Want AI superpowers? OptionalPro featuresadd natural language editing, auto-captions, smart reframing, and more.

### Target Platforms

* Desktop: macOS (Apple Silicon & Intel), Windows, Linux
* Mobile: iOS (via Capacitor), Android (via Capacitor)

## Features

### Core Editing

* Multi-format media import: MP4, MOV, WebM, MKV, M4V, AVI (video); MP3, WAV, AAC (audio); JPG, PNG, WebP (image)
* Frame-accurate trimming: Precise timeline control with millisecond accuracy
* Multi-track timeline: Professional timeline interface with ruler and visual feedback
* Undo/redo system: 100-level history stack with command pattern architecture

### Professional Audio

* High-fidelity waveforms: Peak + RMS visualization with mirrored display (technical details)
* Audio synchronization: Frame-accurate AV sync during playback and export
* Volume control: Per-clip volume adjustment with real-time preview

### Visual Features

* Filmstrip thumbnails: Hardware-accelerated thumbnail generation with adaptive density
* Text overlays: Custom fonts, styles, and animations for titles and captions
* Preview canvas: Real-time compositing with transform controls

### Performance

* Hardware acceleration: Native GPU decode via FFmpeg (VideoToolbox/D3D11VA/VAAPI)
* Decoder prewarming: Sub-10ms first-frame latency through predictive decoder initialization
* Parallel processing: Web worker pool for thumbnail generation (2-4× faster rendering)
* Efficient caching: LRU-based decoder pool with 20 concurrent decoders
* Real-time monitoring: 30+ performance metrics tracked across video pipeline

### Project Management

* Persistent projects: SQLite-backed project storage with auto-save
* Media library: Centralized asset management with metadata caching
* Export pipeline: FFmpeg-based export with codec selection (H.264, H.265, ProRes)

## Architecture

Clypra is architected as anative desktop and mobile applicationwith clear separation between frontend UI and backend processing.

### Technology Stack

Frontend

* React 19 with TypeScript (strict mode)
* Zustand for state management (separated stores by domain)
* Vite for build tooling and hot module replacement

Backend

* Rust with Tauri v2 for native platform integration
* FFmpeg (via ffmpeg-next) for video/audio processing
* Hardware acceleration: VideoToolbox (macOS), D3D11VA (Windows), VAAPI (Linux)
* DashMap for concurrent data structures

Mobile

* Capacitor for iOS/Android deployment
* Native bridge for platform-specific features

### Design Principles

1. Native Performance: Rust FFmpeg backend eliminates browser constraints
2. Desktop-First Architecture: Optimized for desktop-class workflows, portable to mobile
3. Hardware Acceleration: Direct GPU access through native FFmpeg hardware decoders
4. Efficient IPC: Tauri commands optimized for minimal serialization overhead
5. Zero Browser Dependencies: No WebCodecs, MSE, or web-specific APIs

### Video Pipeline Architecture

┌─────────────────────────────────────────────────────────────┐
│ Frontend (React/TS) │
│ ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐ │
│ │ Timeline UI │ │ Preview Canvas│ │ Filmstrip Cache │ │
│ └──────┬───────┘ └──────┬────────┘ └────────┬────────┘ │
│ │ │ │ │
│ └─────────────────┴─────────────────────┘ │
│ │ │
│ Tauri IPC Layer │
│ │ │
└───────────────────────────┼─────────────────────────────────┘
 │
┌───────────────────────────┼─────────────────────────────────┐
│ Backend (Rust/FFmpeg) │
│ ┌─────────────────┴──────────────────┐ │
│ │ Decoder Pool (LRU, size=20) │ │
│ │ ┌──────────────────────────────┐ │ │
│ │ │ Hardware Decoder Context │ │ │
│ │ │ (VideoToolbox/D3D11/VAAPI) │ │ │
│ │ └──────────────────────────────┘ │ │
│ └─────────────┬────────────────────┬─┘ │
│ │ │ │
│ ┌─────────────▼────────┐ ┌────────▼──────────┐ │
│ │ Frame Decoder │ │ Export Pipeline │ │
│ │ (seek + decode) │ │ (encode + mux) │ │
│ └──────────────────────┘ └───────────────────┘ │
└─────────────────────────────────────────────────────────────┘

### Key Optimizations

Decoder Prewarming

* Decoders initialized on project load (eliminates 50-100ms cold start)
* Concurrent prewarming (4 decoders at a time)
* First-frame latency: 5-10ms (vs 50-100ms without prewarming)

Thumbnail Generation

* Web worker pool (CPU cores - 1, max 4)
* Zero-copy ImageBitmap transfer via Transferable
* 60% reduction in main thread CPU during scroll

Batch Processing

* Atlas-based thumbnail storage (reduces IPC overhead by 90%)
* Streaming decode with channel-based delivery
* Concurrent frame decode (up to 20 videos simultaneously)

Sequential Decode Optimization

* Smart seeking: forward decode within GOP boundaries (avoids redundant seeks)
* Sequential hit tracking: detects scrubbing patterns
* 70% reduction in seek operations during timeline navigation

For detailed performance metrics and optimization roadmap, seePERFORMANCE-DESKTOP-ROADMAP.md.

## Installation

### Binary Releases

Pre-built binaries are available for all supported platforms. Download from thelatest release.

#### macOS

Recommended: Homebrew Installation

brew install AIEraDev/tap/clypra

This method automatically handles Gatekeeper authorization and updates.

Alternative: Direct Download

1. DownloadClypra-universal.dmgfrom releases
2. Open the DMG and drag Clypra to/Applications
3. Right-click the app icon and select "Open" to authorize first launch

Supported: macOS 11+ (Big Sur and later), both Apple Silicon and Intel

#### Windows

1. DownloadClypra-x64.msifrom releases
2. Run the installer
3. If Windows SmartScreen blocks execution, click "More Info" → "Run Anyway"

Supported: Windows 10 (version 1809+) and Windows 11

#### Linux

1. DownloadClypra-x86_64.AppImagefrom releases
2. Make executable:chmod +x Clypra-x86_64.AppImage
3. Run:./Clypra-x86_64.AppImage

Supported: Ubuntu 20.04+, Fedora 35+, Debian 11+, and derivatives

## Development

### Prerequisites

Required

* Node.js 18+ with npm
* Rust 1.70+ (install viarustup)
* FFmpeg 6.0+ with development libraries

Platform-Specific

* macOS: Xcode Command Line Tools (xcode-select --install)
* Windows: Visual Studio 2019+ with C++ desktop development tools
* Linux: Build essentials, webkit2gtk, libayatana-appindicator

### FFmpeg Installation

macOS

brew install ffmpeg

Ubuntu/Debian

sudo apt install ffmpeg libavcodec-dev libavformat-dev libavutil-dev libswscale-dev

Windows (Chocolatey)

choco install ffmpeg

Windows (Manual)

1. Download fromffmpeg.org/download.html
2. Extract toC:\ffmpeg
3. AddC:\ffmpeg\binto system PATH

### Build from Source

#
 Clone repository

git clone https://github.com/AIEraDev/clypra.git

cd
 clypra

#
 Install dependencies

npm install

#
 Configure environment

cp .env.example .env

#
 Edit .env and add your Clypra API key (required for text effects)

#
 Development mode with hot reload

npm run tauri dev

#
 Production build

npm run build
npm run tauri build

### Development Architecture

The codebase is organized by domain with clear separation of concerns:

src/
├── components/ # React components
│ ├── editor/ # Core editor UI (Timeline, Preview, Filmstrip)
│ ├── screens/ # Full-screen views (Launch, Settings)
│ └── ui/ # Reusable UI primitives (Modals, Icons, Buttons)
├── store/ # Zustand state stores (by domain)
│ ├── timelineStore.ts # Timeline structure (tracks, clips, gaps)
│ ├── playbackStore.ts # Playback state and AV sync
│ ├── projectStore.ts # Project metadata and media assets
│ └── ... # uiStore, settingsStore, historyStore
├── core/ # Core engine logic
│ ├── runtime/ # ProjectSession and lifecycle management
│ ├── scheduler/ # Frame scheduler for preview rendering
│ ├── resources/ # PreviewMediaPool (video/audio elements)
│ ├── render/ # Canvas rasterization and compositing
│ └── timeline/ # Timeline calculations and utilities
├── lib/ # Shared utilities
│ ├── platform/ # Tauri IPC wrappers
│ ├── monitoring/ # Performance monitoring
│ ├── workers/ # Web worker pool
│ └── ... # Audio, video, filmstrip utilities
├── hooks/ # Custom React hooks
├── types/ # TypeScript type definitions
└── App.tsx # Application entry point

src-tauri/
├── src/
│ ├── commands/ # Tauri command handlers
│ │ ├── thumbnail.rs # Video decode commands
│ │ ├── export.rs # Export pipeline
│ │ └── ...
│ ├── thumbnail_engine/# FFmpeg decoder pool
│ │ ├── decoder.rs # Hardware-accelerated decoder
│ │ ├── cache.rs # LRU caching
│ │ └── ...
│ └── lib.rs # Tauri application setup
└── Cargo.toml # Rust dependencies

### API Configuration

Clypra uses the Clypra API for text effects and templates. To enable these features:

1. Copy.env.exampleto.env:cp .env.example .env
2. Add your API key to.env:VITE_CLYPRA_API_KEY=your_api_key_here
3. Important: Never commit.envto version control (already in.gitignore)

The API provides:

* Text effects library with customizable styles
* Canvas-based text templates with WebM video previews
* Google Fonts integration

### Testing

#
 Run all tests

npm 
test

#
 Run Rust tests

cd
 src-tauri 
&&
 cargo 
test

#
 Run specific test suite

npm 
test
 -- src/lib/__tests__/timelineUtils.test.ts

#
 Run with coverage

npm 
test
 -- --coverage

### Code Quality

#
 TypeScript type checking

npx tsc --noEmit

#
 Rust linting

cd
 src-tauri 
&&
 cargo clippy -- -D warnings

#
 Format code

npm run format

cd
 src-tauri 
&&
 cargo fmt

## Project Structure

### State Management Architecture

Clypra uses Zustand with domain-separated stores to maintain clear ownership boundaries:

* timelineStore: Timeline structure (tracks, clips, transitions, gaps)
* playbackStore: Playback state, playhead position, AV sync
* projectStore: Project metadata, media assets, persistence
* historyStore: Undo/redo command stack
* uiStore: UI state (modals, selections, drag state)
* settingsStore: User preferences and application settings

Each store owns its domain and exposes actions. Cross-store communication happens through explicit calls, not shared mutable state.

### Video Processing Pipeline

1. Import: FFmpeg probe extracts metadata (duration, dimensions, codec)
2. Thumbnail: Rust decoder generates filmstrip tiles (L0-L3 density tiers)
3. Preview: HTMLVideoElement (live playback) or Canvas (composited frames)
4. Export: Frame scheduler → RGBA frames → FFmpeg encoder → MP4/MOV

### Performance Monitoring

The application includes comprehensive performance monitoring:

* Decoder metrics: Cache hits, evictions, decode latency
* Export metrics: Frame write time, fps, total duration
* Render metrics: Layer rendering time, canvas pool efficiency
* Cache metrics: Filmstrip cache hit rate, memory usage

Access metrics in development viawindow.__performanceMonitor.

## Contributing

We welcome contributions! Please seeCONTRIBUTING.mdfor guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Make your changes with tests
4. Ensure all tests pass (npm test && cd src-tauri && cargo test)
5. Commit with conventional commits (feat:,fix:,docs:, etc.)
6. Push to your fork and open a Pull Request

### Code Style

* TypeScript: Strict mode enabled, ESLint + Prettier
* Rust:cargo fmt+cargo clippy(no warnings)
* Commits: Conventional commits format
* Documentation: JSDoc for public APIs, inline comments for complex logic

## License

This project is licensed under the MIT License - see theLICENSEfile for details.

### FFmpeg Licensing

Clypra uses FFmpeg for video processing. FFmpeg is licensed under:

* LGPL 2.1+ (default build)
* GPL 2+ (if built with GPL-only components)

Binary releases include FFmpeg under LGPL. If you build with GPL components, ensure GPL compliance.

## Acknowledgments

* Tauri: Cross-platform native application framework
* FFmpeg: Video/audio processing engine
* React: UI framework
* shadcn/ui: Component library foundation

## Support

* Issues:GitHub Issues
* Discussions:GitHub Discussions
* Documentation:Project Wiki

## Open Core Model

Clypra uses anOpen Corebusiness model:

### Free & Open Source (MIT License)

✅Core Video Editor- Multi-track timeline, frame-accurate editing, hardware-accelerated processing✅Effects Engine- Professional video effects, transitions, filters (via@clypra-studio/engine)✅Audio Tools- Waveform visualization, volume control, AV sync✅Export Pipeline- H.264, H.265, ProRes export with FFmpeg✅Text Overlays- Custom fonts, styles, and animations✅All UI Components- Full source code, no proprietary dependencies

No watermarks. No feature limits. No subscriptions. Forever.

### Pro Features (AI Layer)

🎯Natural Language Editing- "Remove all pauses", "Add captions", "Make this shorter"🎯Auto-Captioning- Transcription with speaker detection and customizable styles🎯Smart Reframe- Auto-crop for Instagram Stories, TikTok, YouTube Shorts🎯Scene Detection- AI-powered scene splitting and B-roll suggestions🎯Audio Enhancement- Noise removal, EQ, compression🎯Voice Cloning- Match narrator voice across clips (coming soon)🎯Multi-language Dubbing- Translate and dub with lip sync (coming soon)

Pricing: Free tier (100 AI calls/month) • Pro ($10/month, unlimited) • Enterprise (custom)

Learn more about Pro features →

### Why Open Core?

We believe professional video editing should be free and accessible to everyone. Open source ensures:

* Transparency- You can audit every line of code
* Ownership- Your edits, your data, your workflow
* Community- Contributions from creators worldwide
* Longevity- The editor can't be shut down or paywalled

The Pro AI features fund full-time development on the open source core. Everyone wins.

## Roadmap

SeePERFORMANCE-DESKTOP-ROADMAP.mdfor upcoming performance improvements.

Planned features:

* Mobile app release (iOS/Android via Capacitor)
* Advanced color grading
* Multi-camera editing
* Plugin system for extensions
* GPU-accelerated effects rendering

Pro Roadmap(AI features):

* Natural language commands (Q3 2026)
* Auto-captioning (Q3 2026)
* Smart reframe (Q4 2026)
* Voice cloning (Q1 2027)
* Multi-language dubbing (Q2 2027)

## About

A modern video editor built with Tauri, React, and TypeScript. Focus on building free capabilities of premium capcut functionalities

clypra.abdulkabirmusa.com

### Topics

 video-editor

 clypra

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.4k

 stars
 

### Watchers

9

 watching
 

### Forks

270

 forks
 

 Report repository

 

## Releases5

Clypra v1.1.1

 Latest

 

Jul 13, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript91.4%
* Rust7.3%
* CSS0.4%
* Shell0.3%
* JavaScript0.3%
* Swift0.1%
* Other0.2%