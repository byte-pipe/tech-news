---
title: GitHub - google/copybara: Copybara: A tool for transforming and moving code between repositories. · GitHub
url: https://github.com/google/copybara
date: 2026-06-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-01T20:01:03.971489
---

# GitHub - google/copybara: Copybara: A tool for transforming and moving code between repositories. · GitHub

# Copybara – Code Transformation and Migration Tool

## Overview
- Copybara is an open‑source tool originally developed at Google for transforming and moving code between repositories.  
- It is designed to keep multiple repositories (e.g., confidential and public) in sync while designating a single authoritative source of truth.  
- The tool is stateless: state is stored in the destination repository as a label in the commit message, allowing concurrent use by many users or services.

## Core Features
- **Repository Types**: Primary support for Git; experimental read support for Mercurial.  
- **Stateless Operation**: No external state store; all needed information is embedded in commit metadata.  
- **Bidirectional Sync**: Can import code from confidential to public repos, from public to confidential, or merge changes from a non‑authoritative repo into the authoritative one.  
- **Extensible Architecture**: Custom origins and destinations can be added for new VCS types or specialized workflows.  
- **Transformations**: Built‑in transformations (e.g., `replace`, `move`) and the ability to define custom file glob patterns.

## Typical Use Cases
- Synchronizing a private repository with a public mirror.  
- One‑time migration of a codebase to a new repository.  
- Propagating contributions made in a public fork back to the internal repository, handling merge conflicts automatically.  

## Example Workflow
```sky
core.workflow(
  name = "default",
  origin = git.github_origin(
      url = "https://github.com/google/copybara.git",
      ref = "master"),
  destination = git.destination(
      url = "file:///tmp/foo"),
  destination_files = glob(["third_party/copybara/**"],
                           exclude = ["README_INTERNAL.txt"]),
  authoring = authoring.pass_thru("Default email <default@default.com>"),
  transformations = [
    core.replace(
        before = "//third_party/bazel/bashunit",
        after  = "//another/path:bashunit",
        paths  = glob(["**/BUILD"])),
    core.move("", "third_party/copybara")
  ],
)
```
Running the workflow:
```bash
mkdir /tmp/foo && cd /tmp/foo && git init --bare
copybara copy.bara.sky
```

## Getting Started

### Pre‑built Snapshot Releases
- Weekly snapshot binaries are available on the GitHub releases page.  
- No guarantee of manual testing or compatibility; use at your own risk.

### Building from Source
1. Install **JDK 11** and **Bazel**.  
2. Clone the repository: `git clone https://github.com/google/copybara.git`.  
3. Build the uber‑jar: `bazel build //java/com/google/copybara:copybara_deploy.jar`.  
4. Run tests (optional): `bazel test //...` (skip tests requiring external tools if not needed).

### System Packages
- Arch Linux users can install via AUR: `aur/copybara-git`.

## Integration with Bazel

### Using Pre‑built Copybara in a Bazel Workspace
1. Ensure Java Runtime 21+ is used (`--java_runtime_version=remotejdk_21`).  
2. Download the release jar with `http_jar` in `WORKSPACE` or `MODULE.bazel`.  
3. Declare a `java_binary` target for Copybara.  
4. Run with Bazel: `bazel run //tools:copybara -- migrate copy.bara.sky`.

### Adding Copybara as an External Repository
```python
http_archive(
    name = "com_github_google_copybara",
    sha256 = "{{ sha256sum }}",
    strip_prefix = "copybara-{{ commit }}",
    url = "https://github.com/google/copybara/archive/{{ commit }}.zip",
)

load("@com_github_google_copybara//:repositories.bzl", "copybara_repositories")
copybara_repositories()

load("@com_github_google_copybara//:repositories.maven.bzl", "copybara_maven_repositories")
copybara_maven_repositories()
```

## Development Tips
- IntelliJ users can configure the Bazel plugin with the following directories and targets:  
  - Directories: `copybara/integration`, `java/com/google/copybara`, `javatests/com/google/copybara`, `third_party`.  
  - Targets: `//copybara/integration/...`, `//java/com/google/copybara/...`, `//javatests/com/google/copybara/...`, `//third_party/...`.  
- Configuration files (e.g., `.bara.sky` workflows) can reside anywhere; storing them in version control is recommended.  

## License & Contributions
- Licensed under the Apache License 2.0.  
- Contributions are welcomed; see `CONTRIBUTING.md` for guidelines.