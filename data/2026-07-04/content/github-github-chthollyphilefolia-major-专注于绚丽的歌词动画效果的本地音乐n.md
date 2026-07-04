---
title: 'GitHub - chthollyphile/folia-major: 专注于绚丽的歌词动画效果的本地音乐/navidrome/第三方网易云播放器 · GitHub'
url: https://github.com/chthollyphile/folia-major
site_name: github
content_file: github-github-chthollyphilefolia-major-专注于绚丽的歌词动画效果的本地音乐n
fetched_at: '2026-07-04T11:32:36.677473'
original_url: https://github.com/chthollyphile/folia-major
author: chthollyphile
description: 专注于绚丽的歌词动画效果的本地音乐/navidrome/第三方网易云播放器. Contribute to chthollyphile/folia-major development by creating an account on GitHub.
---

chthollyphile

 

/

folia-major

Public

* NotificationsYou must be signed in to change notification settings
* Fork58
* Star915

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

814 Commits
814 Commits
.gemini
.gemini
 
 
.github
.github
 
 
api
api
 
 
assets
assets
 
 
build
build
 
 
docs
docs
 
 
electron
electron
 
 
img
img
 
 
packaging
packaging
 
 
public
public
 
 
shared
shared
 
 
skills
skills
 
 
src
src
 
 
test
test
 
 
worker
worker
 
 
.all-contributorsrc
.all-contributorsrc
 
 
.editorconfig
.editorconfig
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
benchmark_chorus.js
benchmark_chorus.js
 
 
index.html
index.html
 
 
metadata.json
metadata.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
postcss.config.js
postcss.config.js
 
 
stage-client.html
stage-client.html
 
 
tailwind.config.js
tailwind.config.js
 
 
tsconfig.json
tsconfig.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
wrangler.jsonc
wrangler.jsonc
 
 
View all files

## Repository files navigation

# Folia

Lyrics Reimagined // 辞曲新境

桌面版下载·Vercel 部署·使用指南·技术说明

## 项目简介

Folia是一个以全屏沉浸式歌词播放为核心的在线音乐播放器，支持网易云，navidrome和本地音乐库，通过智能歌词匹配，AI生成配色主题，以及多种全屏歌词动画为用户提供独特的听歌体验。

如果你希望直接开箱即用，马上体验，推荐直接使用基于Electron的 windows/ macOS/ Linux 桌面端版本。

如果希望能够在移动设备上使用，或在浏览器上体验云端多平台，可以选择一键部署到 Vercel的 Web 版本，或自行部署到其他支持 Node.js 的平台。

## 展示

### 演示视频

folia-demo2.mp4

2025-11-30.23-36-58.mp4

### 主题预览

浮名

流光

心象

云阶

群唱

倾诉

不同的歌词动画具有不同的排版氛围和可调参数，让全屏歌词拥有如同文字PV般的丰富视觉效果，同时又能兼顾响应式布局，自动适配不同窗口尺寸。

## 核心能力

模块

说明

在线搜索与播放

搜索歌曲、歌手或专辑后即可播放，并自动加载相关封面与歌词。

本地音乐支持

可导入本地音频文件，在本地安全保存索引信息，不上传文件内容。

智能歌词匹配

本地歌曲可自动匹配在线歌词与封面，也支持手动修正匹配结果。

LRC 文件识别

自动加载同目录同名 
.lrc
 歌词文件，或歌词文件内嵌lrc歌词。适配 LDDC 生成的增强型逐字歌词格式

Now Playing 接入

支持通过本机 
Now Playing
 服务接入外部播放器的歌曲、时间轴与歌词信息，并驱动 Folia 的舞台视图与全屏歌词渲染。

AI 主题生成

基于歌曲情绪与歌词内容生成沉浸式背景与视觉参数。

多端体验

提供 Web 部署方式，同时支持桌面端打包分发。

## 桌面端下载

桌面版内置前后端运行环境，适合希望即装即用的用户。最新版本请前往Releases 页面。

Linux 包、Wayland / Hyprland 遥控窗和桌面端细节见技术与开发说明。

## 文档与开发

更完整的使用说明请访问Folia Guide。

部署、环境变量、本地开发、Stage API、常用脚本和技术栈见技术与开发说明。

如果你希望快速上线 Web 版本，请阅读Vercel 一键部署指南来创建项目

## 本地音乐与匹配说明

使用本地音乐时，Folia 会优先尝试从以下来源补全信息：

1. 音频文件自身元数据
2. 同目录同名歌词文件
3. 在线匹配结果

如果自动匹配不准确，可以在播放界面的右侧面板进入“本地”选项卡，手动搜索并指定更合适的歌词、封面或元数据来源。你也可以选择只使用本地信息，关闭在线匹配结果。

## 贡献者

Thanks goes to these wonderful people. Issue reports, bug reports, ideas, docs, design, tests, and code are all counted through theall-contributorsspec.

冬霧
💻

zhao_alpha
🐛

hz1ang
🐛
 
🤔

steadyoak
🐛
 
🤔

POINTER
🐛
 
🤔

Yuki-3939
🤔

MewsCat
🐛
 
🤔

tumuyan
🐛
 
🤔
 
💻

948720857
🐛

谦君
🤔

suheandzl
🐛

Enkianssus
🤔

不会飞的麻将
🤔

streamstack-cn
🤔

白影White
🤔

IXnAh1L
🐛

EGOIST
🐛

yanfd
🐛

Tony Smith
💻

## 法律与免责声明

本项目在 AI 的广泛协助下开发，因此仍可能存在细微或不易察觉的问题。若给你带来不便，敬请理解。

本项目主要用于展示播放动效、界面设计与相关工程实现。应用中涉及的在线音乐流媒体、歌词、专辑封面及其他内容，其版权均归对应权利人所有。

本仓库及其源代码仅供个人学习、技术交流与非营利测试使用。请勿将其用于商业盈利用途。若因对在线资源的传播、加工或再分发而引发版权纠纷或其他责任，均由使用者自行承担，项目开发者不承担相关责任。

请始终尊重数字版权，并在条件允许时通过官方平台支持正版音乐。

## 致谢

特别感谢以下项目和资源：

* chenmozhijin/LDDC
* NeteaseCloudMusicApiEnhanced
* chenglou/pretext

本项目接入了Apple Music-like Lyrics TTML 逐词歌词库以提供高质量的歌词文件，感谢此歌词库的作者和贡献者们。

## 许可证

本项目基于AGPL-3.0许可证开源。

## About

专注于绚丽的歌词动画效果的本地音乐/navidrome/第三方网易云播放器

folia-site.vercel.app/

### Topics

 react

 music

 player

 typescript

 music-player

 pwa

 ai

 netease-music

 vercel-deployment

 navidrome-client

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

915

 stars
 

### Watchers

1

 watching
 

### Forks

58

 forks
 

 Report repository

 

## Releases101

v0.5.21

 Latest

 

Jul 3, 2026

 

+ 100 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript93.5%
* JavaScript5.0%
* Other1.5%