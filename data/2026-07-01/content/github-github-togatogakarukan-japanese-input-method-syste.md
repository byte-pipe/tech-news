---
title: 'GitHub - togatoga/karukan: Japanese Input Method System for Linux, macOS, Neural Kana-Kanji Conversion Engine · GitHub'
url: https://github.com/togatoga/karukan
site_name: github
content_file: github-github-togatogakarukan-japanese-input-method-syste
fetched_at: '2026-07-01T12:04:46.206914'
original_url: https://github.com/togatoga/karukan
author: togatoga
description: Japanese Input Method System for Linux, macOS, Neural Kana-Kanji Conversion Engine - togatoga/karukan
---

togatoga

 

/

karukan

Public

* NotificationsYou must be signed in to change notification settings
* Fork29
* Star525

 
 
 
 
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

26 Commits
26 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
images
images
 
 
karukan-cli
karukan-cli
 
 
karukan-engine
karukan-engine
 
 
karukan-fcitx5
karukan-fcitx5
 
 
karukan-im
karukan-im
 
 
karukan-macos
karukan-macos
 
 
scripts
scripts
 
 
tests/
integration
tests/
integration
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
THIRD_PARTY_LICENSES
THIRD_PARTY_LICENSES
 
 
icon.png
icon.png
 
 
View all files

## Repository files navigation

# Karukan

Linux・macOS向け日本語入力システム — ニューラルかな漢字変換エンジン

## プロジェクト構成

クレート

説明

karukan-fcitx5

Linux向けIMEフロントエンド — fcitx5アドオン + C FFI

karukan-macos

macOS向けIMEフロントエンド — Swift/InputMethodKit

karukan-im

共有IMEエンジン — ステートマシン、ローマ字変換、karukan-imserver(macOS向けJSON-RPCサーバー)

karukan-engine

コアライブラリ — ローマ字→ひらがな変換 + llama.cppによるニューラルかな漢字変換

karukan-cli

CLIツール・サーバー — 辞書ビルド、Sudachi辞書生成、辞書ビューア、AJIMEE-Bench、HTTPサーバー

## 特徴

* ニューラルかな漢字変換: GPT-2ベースのモデルをllama.cppで推論し、高度な日本語変換
* ライブ変換: 入力と同時に変換結果をリアルタイム表示。Spaceを押さずに変換が進む（Ctrl+Shift+LでON/OFF）
* コンテキスト対応: 周辺テキストを考慮した日本語変換
* 変換学習: ユーザーが選択した変換結果を記憶し、次回以降の変換で優先表示。予測変換（前方一致）にも対応し、入力途中でも学習済みの候補を提示
* システム辞書:SudachiDictの辞書データからシステム辞書を構築
* 候補リライター (Mozcから移植): 半角カタカナ、英字の大文字小文字・全角半角、記号の関連候補、数字の各種表記（漢数字・大字・ローマ数字・丸数字・16/8/2進数）を自動生成。各候補にはMozc由来の注釈（「半角カタカナ」「16進数」など）が付く
* 絵文字入力: かな読み（ぴえん→ 🥺、きんにく→ 💪）と Slack 風:triggerクエリ（:smile→ 😄、:halo→ 😇）の両方をサポート

Note:初回起動時にHugging Faceからモデルをダウンロードするため、初回の変換開始までに時間がかかります。2回目以降はダウンロード済みのモデルが使用されます。

## インストール

* Linux (fcitx5):karukan-fcitx5 の READMEを参照
* macOS:karukan-macos の READMEを参照

## ライセンス

MIT OR Apache-2.0 のデュアルライセンスで提供しています。

* MIT License
* Apache License 2.0

karukan-engine/data/配下にはMozc（Google製日本語入力システム）から派生したデータを含み、こちらはBSD 3-Clause Licenseのもとで配布されています。各派生ファイルの由来およびMozcの著作権表記はTHIRD_PARTY_LICENSESを参照してください。

## About

Japanese Input Method System for Linux, macOS, Neural Kana-Kanji Conversion Engine

### Topics

 nlp

 macos

 linux

 rust

 natural-language-processing

 inputmethod

 ime

 input-method

 japanese

 fcitx5

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

525

 stars
 

### Watchers

5

 watching
 

### Forks

29

 forks
 

 Report repository

 

## Releases1

v0.1.0

 Latest

 

Feb 23, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust81.3%
* Swift6.9%
* Python3.0%
* JavaScript2.7%
* C++1.7%
* CSS1.3%
* Other3.1%