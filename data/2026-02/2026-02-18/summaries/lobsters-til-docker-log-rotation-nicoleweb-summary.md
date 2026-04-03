---
title: TIL: Docker log rotation | nicole@web
url: https://ntietz.com/blog/til-docker-log-rotation/
date: 2026-02-18
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-18T06:01:48.940550
---

# TIL: Docker log rotation | nicole@web

# TIL: Docker Log Rotation

* The author unexpectedly ran out of disk space on their server, which was primarily used for hosting static websites.
* Investigation revealed that Docker containers were consuming most of the 25 GB disk space due to large, unrotated log files.
* Docker does not automatically rotate log files; as long as a container is running, logs continue to grow. This can lead to significant disk space consumption over time, especially with high traffic.
* The author checked the Docker container's log configuration using `docker inspect` and found it was entirely unconfigured.
* To fix this, the author created or modified the `/etc/docker/daemon.json` file to include a log driver ("json-file") with options for a maximum file size (100m) and a maximum number of files (3).
* After restarting the Docker daemon (`systemctl restart docker`), the author realized the configuration applies to new containers only. Existing containers needed to be stopped and recreated for the log rotation to take effect.
* Verification after recreation showed the log rotation was working as expected.
* The author emphasizes the importance of configuring log rotation in Docker to prevent disk space issues.
* The author humorously suggests outsourcing tedious tasks like log rotation and promotes their services.
* The post includes links to the author's newsletter, RSS feed, personal email, and resources for programmers and hiring.
