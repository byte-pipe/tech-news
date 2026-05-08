---
title: ClojureScript - 1.12.145 Release
url: https://clojurescript.org/news/2026-05-07-release
site_name: hackernews_api
content_file: hackernews_api-clojurescript-112145-release
fetched_at: '2026-05-09T07:54:04.572419'
original_url: https://clojurescript.org/news/2026-05-07-release
author: Borkdude
date: '2026-05-08'
description: ClojureScript Gets Async/Await
tags:
- hackernews
- trending
---

(refer-global :only '[Promise])

(defn ^:async foo [n]
 (let [x (await (Promise/resolve 10))
 y (let [y (await (Promise/resolve 20))]
 (inc y))
 ;; not async
 f (fn [] 20)]
 (+ n x y (f))))