---
title: Code and Cake - Docker is weird
url: https://codeandcake.dev/posts/2026-10-22-docker-is-weird
date: 2026-10-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-23T15:41:53.261714
---

# Code and Cake - Docker is weird

## What is Docker?

Docker is a container runtime that allows you to package, ship, and run applications in containers.

## Key points about Docker

* Containers are not just processes; they have their own kernel and memory layout.
* Containers don't have access to the host's kernel and memory; instead, they have their own isolated world.
* Images are not real but rather folders where Docker puts an image.
* Containers can have their own networking configuration.

## Weird things about Docker

* Containers are not real in the sense that the kernel is still running the process.
* Docker uses Linux features like cgroups and namespaces to control container resources and network behavior.
* Images can be run from a different user and group than the container's user and group.
* Go is not a suitable language for a container runtime due to its thread-safety issues.

## Strange quirks of Docker's runc

* runc is written in Go and is the core of the container runtime.
* runc needs to make specific Linux syscalls that are not natively supported in Go.
* runc cannot fork; it needs to use a special command-line argument to approximate a fork.

## Why Docker has challenges

* Containers require root privileges to run; Docker usually uses root to manage the daemon.
* Networking in containers needs to be reimplemented in/userspace.

## Learning Docker is fun

* Writing your own Docker tool can help you understand the technology.

## Key takeaways

Docker is a complex system that provides unique benefits and challenges. By understanding its quirks and design choices, you can better use Docker to package, ship, and run applications.
* Containers are not just processes but have their own kernel and memory layout.
* Docker images are not real but rather folders with access control and networking features.
* runc is the core of the container runtime, but it cannot fork or use traditional Linux syscalls.