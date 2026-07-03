---
title: v3.0.0 · immich-app/immich · Discussion #29439 · GitHub
url: https://github.com/immich-app/immich/discussions/29439
date: 2026-07-02
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-03T11:57:52.555800
---

# v3.0.0 · immich-app/immich · Discussion #29439 · GitHub

**Immich v3.0.0 Released**

* **Breaking Changes:**
	+ Updates API endpoints for compatibility with third-party tools.
	+ Drops support for pgvecto.rs library.
	+ Migration guide available at <https://docs.immich.app/install/upgrading#migrating-to-vectorchord>
* **Release Details:**

**Update Method:**

1. Update `IMMICH_VERSION` in your `.envfile` from version 2 to v3.
2. Run the usual update commands:
   ```bash
docker compose pull 
&&
 docker compose up -d
```

**Features and Improvements:**

* Mobile non-destructive editing for images and other media with improvements like background backup and slideshow feature.
* Workflows, including preview functionality.
* Background backup improvements.
* Recently added page on the Immich website.
* Integrity checks feature implementation.
* Enhancements to video editing, transcription (HLS real-time video transcoding), web player for video online streaming, new photo viewer on the mobile app gallery and Open Photo in the Android Mobile App gallery.
* OCR engine optimization.

**Changelog:**

The Immich Team is excited about this release of v3.0.0, which includes several breaking changes that improve developer experience with our product. For more information visit the <https://docs.immich.app/install/upgrading> page for migration guides and detailed changelogs and explanations.