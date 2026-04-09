---
title: Announcing AnalogJS 2.0 ⚡️ - DEV Community
url: https://dev.to/analogjs/announcing-analogjs-20-348d
date: 2025-11-03
site: devto
model: llama3.2:1b
summarized_at: 2025-11-10T11:23:52.893396
screenshot: devto-announcing-analogjs-2-0-dev-community.png
---

# Announcing AnalogJS 2.0 ⚡️ - DEV Community

## Introducing AnalogJS 2.0 ⚡️
AnalogJS, the meta-framework built on top of Angular, is now available with its second major release.

## Key Features (⭐️)
- First-class support for Vite ecosystem services
- Filesystem-based routing
- Markdown and blog features
- API/server routes
- Hybrid SSR/SSG with sitemap and RSS feed support
- Supports Angular CLI/Nx workspaces
- Server and deployment capabilities

## New Features Include:
- Content resources for displaying content lists and files
- Smaller install bundle size optimizations
- Vite ecosystem upgrades

## Notable Changes:

### Content Resources
ContentResources are used to display content lists and files.
```js
import {
  Component,
} from '@angular/core';

@Component({
  selector: 'blog-posts',
  imports: [
    PostsComponent {},
    Post {}
  ],
  template: `
    @defer(hydrate on hover) {
      <posts [posts]="postsResource.value()"></posts>
    }
  `,
})
export class Blog {
  readonly postsResource = contentFilesResource(Post);
}
```
### Markdown Component
The new Markdown component is integrated with Angular's latest primitives for reactivity.
```js
import { Component } from '@angular/core';
import MarkdownComponent from './markdown';

@Component({
  selector: 'post',
  template: `
    <div class="flex flex-grow justify-center min-h-screen">
      <article class="w-screen max-w-4xl p-8">
        <h2 class="text-gray-600 text-2xl">{{ post.attributes.title }}</h2>

        <span class="font-light text-sm">
          {{ post.attributes.publishedDate }} - {{ post.content }} min read
        </span>

        <analog-markdown [content]="post.content"></analog-markdown>
      </article>
    </div>
  `,
})
export class Post {
}
```
### RouteMeta and Resolvers
Route meta is updated to include post metadata.
```js
import { RouteMeta } from '@analogjs/router';
import postMetaResolver, postTitleResolver from './resolvers';

const routeMeta: RouteMeta = {
  title: postTitleResolver,
  meta: postMetaResolver,
};
```
### Smaller Install Bundle Size Optimizations

The entire AnalogJS library has been optimized to reduce installation bundle size.
```js
// Removed unnecessary code and minified the result
```

## Conclusion
