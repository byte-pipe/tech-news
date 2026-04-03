---
title: "Don't Get Distracted"
url: https://calebhearth.com/dont-get-distracted
date: 2026-02-10
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-10T11:03:50.137905
---

# Don't Get Distracted

# Don't Get Distracted

This article recounts the author's experience working on a software project for the Department of Defense (DOD) during an internship. Initially, the author was excited by the opportunity and the technical challenge of building a tool to locate WiFi signals using phone sensors. The project involved collecting geolocation data and WiFi signal strength to predict the location of access points using algorithms based on the Free Space Path Loss equation, R^2 error measurement, and Gaussian estimation. These calculations were optimized for speed using a dictionary of latitude/longitude pairs.

## Key Points:

* **Initial Enthusiasm:** The author accepted an internship with a high salary, viewing it as a great opportunity to support the military, influenced by family connections.
* **Project Description:** The team was developing a tool to find WiFi signals by analyzing changes in signal strength as a phone moved. This involved combining geolocation data with WiFi signal strength readings.
* **Technical Details:** The software utilized algorithms like R^2 and Gaussian estimation, combined with a probability matrix to determine WiFi signal locations in 2D space, including altitude.
* **Optimization Efforts:** The author contributed to optimizing the code, such as implementing a dictionary to avoid redundant distance calculations, significantly improving performance.
* **Accuracy Limitations:** The accuracy of the location finding was around 45 feet, which is significant given typical WiFi range.
* **Genetic Algorithm Implementation:** A Genetic Algorithm was employed to fine-tune the parameters of the Gaussian estimation, using the actual location data as a fitness function to optimize the accuracy of the predictions.
* **Hidden Purpose:** The author explicitly warns the reader not to be distracted by the technical details, emphasizing that the software was ultimately designed for a harmful purpose – to kill people. The article highlights the ethical implications of the author's work without their initial knowledge.
* **Team Dynamics:** The author describes the team as a mix of experienced and less experienced individuals, with their own areas of expertise complementing the author's software engineering skills.
