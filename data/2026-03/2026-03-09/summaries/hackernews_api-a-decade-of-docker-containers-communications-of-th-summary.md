---
title: A Decade of Docker Containers – Communications of the ACM
url: https://cacm.acm.org/research/a-decade-of-docker-containers/
date: 2026-03-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-09T07:26:40.357946
---

# A Decade of Docker Containers – Communications of the ACM

# A Decade of Docker Containers – Communications of the ACM

## Overview
- Docker streamlines three stages of application development: building an image (`docker build`), distributing it (`docker push`), and running isolated instances (`docker run`).  
- Developers create images from a Dockerfile alongside source code or reuse published images, enabling cross‑language and cross‑stack packaging.  
- Since its 2013 release, Docker has been adopted in diverse domains (e.g., scientific simulations, streaming services, space‑borne software) and consistently ranks among the most desired and used tools on Stack Overflow.  
- Docker Hub and other registries host over 14 million images and serve more than 11 billion pulls per month.

## Technical Foundations
- Docker addresses the long‑standing challenge of building and deploying microservices written in heterogeneous languages.  
- It has become the de‑facto standard for managing cloud‑native applications on multi‑tenant platforms such as Kubernetes and raises the bar for reproducible scientific research.  
- The system builds on decades of OS research, originally leveraging Linux primitives and later extending support to macOS and Windows without sacrificing usability.  
- Future work focuses on adapting Docker to AI‑driven workloads and heterogeneous hardware (e.g., GPUs, FPGAs).

## Typical Workflow
- Developers write a Dockerfile using familiar shell syntax extended with Docker directives (e.g., `FROM`, `COPY`, `RUN`, `EXPOSE`, `CMD`).  
- Example for a Python web app:
  ```dockerfile
  FROM python:3
  COPY requirements.txt /app/requirements.txt
  WORKDIR /app
  RUN pip install -r requirements.txt
  COPY . /app
  EXPOSE 80
  CMD ["python", "app.py"]
  ```
- Commands:
  - `docker build -t <repo>/<image> .` creates the image.  
  - `docker push <repo>/<image>` uploads it to a registry.  
  - `docker run -v data:/app/data -p 80:80 <repo>/<image>` runs the container with volume and port bindings.  
- The workflow has remained stable since 2013; GitHub contains over 3.4 million Dockerfiles in public repositories.

## Under‑the‑Hood Mechanisms
- Traditional OS kernels share memory, files, and IPC resources, leading to conflicts when multiple applications require different library versions or network ports.  
- Virtual machines isolate applications completely but are heavyweight, duplicating kernels, filesystems, caches, and networking stacks.  
- Early Unix solutions (e.g., `chroot`) provided separate root filesystems but could not combine multiple application filesystems or resolve network clashes.  
- Docker employs Linux **namespaces** to give each process an isolated view of resources (files, network, PID, etc.).  
  - A process sees a remapped filesystem (e.g., `/etc/passwd` from its own namespace) while the underlying kernel handles the redirection transparently.  
  - Namespaces apply at the point of resource opening; subsequent operations use standard kernel descriptors, preserving performance.  

## Impact and Adoption
- Docker’s lightweight isolation enables rapid iteration, versioned distribution, and conflict‑free coexistence of diverse applications on the same host.  
- Its ecosystem (Dockerfile, Docker Hub, CLI) has become integral to modern software engineering, supporting millions of developers and billions of deployments worldwide.