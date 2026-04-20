---
title: MinIO Is Dead, Long Live MinIO · Vonng
url: https://blog.vonng.com/en/db/minio-resurrect/
date: 2026-02-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-01T10:17:14.728814
---

# MinIO Is Dead, Long Live MinIO · Vonng

# MinIO Is Dead, Long Live MinIO

## The Death Certificate
- On 3 Dec 2025 MinIO announced “maintenance mode”; on 12 Feb 2026 the repository was marked “no longer maintained” and archived.
- The project, with 60 k stars and >1 billion Docker pulls, became read‑only: no PRs, issues, or contributions accepted.
- Timeline of the wind‑down:
  - May 2021 – license changed from Apache 2.0 to AGPL v3.
  - Jul 2022 – legal action against Nutanix (license enforcement).
  - Mar 2023 – legal action against Weka (license enforcement).
  - May 2025 – admin console removed from Community Edition.
  - Oct 2025 – binary/Docker distribution stopped.
  - Dec 2025 – “maintenance mode” announced.
  - Feb 2026 – repo archived, project officially ended.

## Why Open‑Source Survives
- AGPL is irrevocable; once code is released under it, the community retains the right to fork and maintain it.
- MinIO’s abandonment cannot revoke the license, allowing a community‑driven resurrection.

## What I Did
- **Background**: Maintainer of Pigsty (a PostgreSQL distribution) and former operator of a large MinIO deployment (≈25 PB) in China.
- **Fork**: Created `swapminio/minioforpgsty/minio` with CVE‑patched binaries ready since Dec 2025.

### 1. Restored the Admin Console
- Reverted the `minio/console` submodule to the pre‑May 2025 version, bringing back full user management, bucket policies, lifecycle management, etc.
- No reverse engineering required; the code was still present in the history.

### 2. Rebuilt Binary Distribution
- Published Docker images (`pgsty/minio`) on Docker Hub.
- Built RPM and DEB packages matching the original specifications.
- Set up an automated CI/CD pipeline on GitHub for continuous, reproducible builds.
- Provided easy installation via the `pig` package manager and a ready‑to‑use APT/DNF repo.

### 3. Restored Community Edition Documentation
- Forked `minio/docs`, fixed broken links, reinstated console documentation, and hosted it under the same CC‑BY‑4.0 license.

## Commitments and Principles
- **No new features** – focus on supply‑chain stability and CVE fixes.
- **Production‑ready builds** – binaries are dog‑fooded in Pigsty for months; any breakage is fixed promptly.
- **Bug tracking and CVE handling** – issues can be reported on `pgsty/minio`; support is best‑effort, not a commercial SLA.
- **Trademark considerations** – will address trademark issues if they arise, but they do not impede the fork’s functionality.

## How to Use the Revived MinIO
- Docker: `docker pull pgsty/minio` (replace `swapminio/minioforpgsty/minio` in existing setups).
- Linux packages: download RPM/DEB from the GitHub releases page or install via `pig`:
  ```bash
  curl https://repo.pigsty.io/pig | bash
  pig repo add infra -u
  pig install minio
  ```
- Documentation: available at the forked docs site, identical in content to the original Community Edition.
