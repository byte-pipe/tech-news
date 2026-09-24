---
title: 🦄 Sharing DEV Followers Count on Github Profile 🦄 - DEV Community
url: https://dev.to/annavi11arrea1/sharing-dev-followers-count-on-github-profile-bj3
date: 2026-09-23
site: devto
model: llama3.2:1b
summarized_at: 2026-09-24T15:46:11.930583
---

# 🦄 Sharing DEV Followers Count on Github Profile 🦄 - DEV Community

**Sharing DEV Follower Count on Github: A Devolved Project**

#### Key Points

* Created a small project to fix a recurring issue with Github Actions: failed to update follow-count on GitHub due to a leftover comment.
* Tweaked API call, commented out unused code, and added a new Github Actions file to achieve the update.
* Successfully ran the updated file, achieving first successful run #343.

#### YAML File Contents

* Updated development team followers count using `DEVTO Followers Count` script.
* Set up GitHub Actions workflow using `dev.to Followers Count` job.

#### Steps

* Checkout repository using `actions/checkout@v4`.
* Set up Node.js environment with specific version.
* Run the `update_script.js` to update followers count.
* Commit the updated `README.md` file.
* Push the updated changes using `git push`.

#### Important Notes

* Environment variables are used to secure access to API keys.
* Specify tags in `README.md` file to include output of followers count.
* Github Actions auto-pushes the updated job run.

#### Conclusion

The author successfully developed a small project to fix the issue of tracking Github Actions failing to update followers count, introducing DEV.to followers count. By improving the existing API request and commenting out unused code, they were able to achieve success without hardcoding API keys. Key features included environment variable security and auto-pushed updates.