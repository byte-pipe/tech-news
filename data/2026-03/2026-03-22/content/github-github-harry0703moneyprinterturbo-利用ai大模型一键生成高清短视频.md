---
title: 'GitHub - harry0703/MoneyPrinterTurbo: 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. · GitHub'
url: https://github.com/harry0703/MoneyPrinterTurbo
site_name: github
content_file: github-github-harry0703moneyprinterturbo-利用ai大模型一键生成高清短视频
fetched_at: '2026-03-22T11:09:43.149380'
original_url: https://github.com/harry0703/MoneyPrinterTurbo
author: harry0703
description: 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. - harry0703/MoneyPrinterTurbo
---

harry0703



/

MoneyPrinterTurbo

Public

* NotificationsYou must be signed in to change notification settings
* Fork7.2k
* Star50.6k




 
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

484 Commits
484 Commits
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
app
app
 
 
docs
docs
 
 
resource
resource
 
 
test
test
 
 
webui
webui
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README-en.md
README-en.md
 
 
README.md
README.md
 
 
config.example.toml
config.example.toml
 
 
docker-compose.yml
docker-compose.yml
 
 
main.py
main.py
 
 
requirements.txt
requirements.txt
 
 
webui.bat
webui.bat
 
 
webui.sh
webui.sh
 
 
View all files

## Repository files navigation

# MoneyPrinterTurbo 💸

### 简体中文 |English

只需提供一个视频
主题
 或
关键词
 ，就可以全自动生成视频文案、视频素材、视频字幕、视频背景音乐，然后合成一个高清的短视频。

#### Web界面

#### API界面

## 特别感谢 🙏

由于该项目的部署和使用，对于一些小白用户来说，还是有一定的门槛，在此特别感谢录咖（AI智能 多媒体服务平台）网站基于该项目，提供的免费AI视频生成器服务，可以不用部署，直接在线使用，非常方便。

* 中文版：https://reccloud.cn
* 英文版：https://reccloud.com

## 感谢赞助 🙏

感谢佐糖https://picwish.cn对该项目的支持和赞助，使得该项目能够持续的更新和维护。

佐糖专注于图像处理领域，提供丰富的图像处理工具，将复杂操作极致简化，真正实现让图像处理更简单。

## 功能特性 🎯

* 完整的MVC架构，代码结构清晰，易于维护，支持API和Web界面
* 支持视频文案AI自动生成，也可以自定义文案
* 支持多种高清视频尺寸竖屏 9:16，1080x1920横屏 16:9，1920x1080
* 竖屏 9:16，1080x1920
* 横屏 16:9，1920x1080
* 支持批量视频生成，可以一次生成多个视频，然后选择一个最满意的
* 支持视频片段时长设置，方便调节素材切换频率
* 支持中文和英文视频文案
* 支持多种语音合成，可实时试听效果
* 支持字幕生成，可以调整字体、位置、颜色、大小，同时支持字幕描边设置
* 支持背景音乐，随机或者指定音乐文件，可设置背景音乐音量
* 视频素材来源高清，而且无版权，也可以使用自己的本地素材
* 支持OpenAI、Moonshot、Azure、gpt4free、one-api、通义千问、Google Gemini、Ollama、DeepSeek、文心一言,Pollinations、ModelScope等多种模型接入中国用户建议使用DeepSeek或Moonshot作为大模型提供商（国内可直接访问，不需要VPN。注册就送额度，基本够用）
* 中国用户建议使用DeepSeek或Moonshot作为大模型提供商（国内可直接访问，不需要VPN。注册就送额度，基本够用）

### 后期计划 📅

* GPT-SoVITS 配音支持
* 优化语音合成，利用大模型，使其合成的声音，更加自然，情绪更加丰富
* 增加视频转场效果，使其看起来更加的流畅
* 增加更多视频素材来源，优化视频素材和文案的匹配度
* 增加视频长度选项：短、中、长
* 支持更多的语音合成服务商，比如 OpenAI TTS
* 自动上传到YouTube平台

## 视频演示 📺

### 竖屏 9:16

▶️
 《如何增加生活的乐趣》

▶️
 《金钱的作用》
更真实的合成声音

▶️
 《生命的意义是什么》

demo-portrait-1.mp4

default.mp4

demo-portrait-2.mp4

### 横屏 16:9

▶️
《生命的意义是什么》

▶️
《为什么要运动》

demo-landscape.mp4

demo-landscape-2.mp4

## 配置要求 📦

* 建议最低 CPU4核或以上，内存4G或以上，显卡非必须
* Windows 10 或 MacOS 11.0 以上系统

## 快速开始 🚀

### 在 Google Colab 中运行

免去本地环境配置，点击直接在 Google Colab 中快速体验 MoneyPrinterTurbo

### Windows一键启动包

下载一键启动包，解压直接使用（路径不要有中文、特殊字符、空格）

* 百度网盘（v1.2.6）:https://pan.baidu.com/s/1wg0UaIyXpO3SqIpaq790SQ?pwd=sbqx提取码: sbqx
* Google Drive (v1.2.6):https://drive.google.com/file/d/1HsbzfT7XunkrCrHw5ncUjFX8XX4zAuUh/view?usp=sharing

下载后，建议先双击执行update.bat更新到最新代码，然后双击start.bat启动

启动后，会自动打开浏览器（如果打开是空白，建议换成Chrome或者Edge打开）

## 安装部署 📥

### 前提条件

* 尽量不要使用中文路径，避免出现一些无法预料的问题
* 请确保你的网络是正常的，VPN需要打开全局流量模式

#### ① 克隆代码

git clone https://github.com/harry0703/MoneyPrinterTurbo.git

#### ② 修改配置文件（可选，建议启动后也可以在 WebUI 里面配置）

* 将config.example.toml文件复制一份，命名为config.toml
* 按照config.toml文件中的说明，配置好pexels_api_keys和llm_provider，并根据 llm_provider 对应的服务商，配置相关的
API Key

### Docker部署 🐳

#### ① 启动Docker

如果未安装 Docker，请先安装https://www.docker.com/products/docker-desktop/

如果是Windows系统，请参考微软的文档：

1. https://learn.microsoft.com/zh-cn/windows/wsl/install
2. https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-containers

cd
 MoneyPrinterTurbo
docker-compose up

注意：最新版的docker安装时会自动以插件的形式安装docker compose，启动命令调整为docker compose up

#### ② 访问Web界面

打开浏览器，访问http://0.0.0.0:8501

#### ③ 访问API文档

打开浏览器，访问http://0.0.0.0:8080/docs或者http://0.0.0.0:8080/redoc

### 手动部署 📦

视频教程

* 完整的使用演示：https://v.douyin.com/iFhnwsKY/
* 如何在Windows上部署：https://v.douyin.com/iFyjoW3M

#### ① 创建虚拟环境

建议使用conda创建 python 虚拟环境

git clone https://github.com/harry0703/MoneyPrinterTurbo.git

cd
 MoneyPrinterTurbo
conda create -n MoneyPrinterTurbo python=3.11
conda activate MoneyPrinterTurbo
pip install -r requirements.txt

#### ② 安装好 ImageMagick

* Windows:下载https://imagemagick.org/script/download.php选择Windows版本，切记一定要选择静态库版本，比如
ImageMagick-7.1.1-32-Q16-x64-static.exe安装下载好的 ImageMagick，注意不要修改安装路径修改配置文件 config.toml中的imagemagick_path为你的实际安装路径
* 下载https://imagemagick.org/script/download.php选择Windows版本，切记一定要选择静态库版本，比如
ImageMagick-7.1.1-32-Q16-x64-static.exe
* 安装下载好的 ImageMagick，注意不要修改安装路径
* 修改配置文件 config.toml中的imagemagick_path为你的实际安装路径
* MacOS:brew install imagemagick
* Ubuntusudo apt-get install imagemagick
* CentOSsudo yum install ImageMagick

#### ③ 启动Web界面 🌐

注意需要到 MoneyPrinterTurbo 项目根目录下执行以下命令

###### Windows

webui.bat

###### MacOS or Linux

sh webui.sh

启动后，会自动打开浏览器（如果打开是空白，建议换成Chrome或者Edge打开）

#### ④ 启动API服务 🚀

python main.py

启动后，可以查看API文档http://127.0.0.1:8080/docs或者http://127.0.0.1:8080/redoc直接在线调试接口，快速体验。

## 语音合成 🗣

所有支持的声音列表，可以查看：声音列表

2024-04-16 v1.1.2 新增了9种Azure的语音合成声音，需要配置API KEY，该声音合成的更加真实。

## 字幕生成 📜

当前支持2种字幕生成方式：

* edge: 生成速度快，性能更好，对电脑配置没有要求，但是质量可能不稳定
* whisper: 生成速度慢，性能较差，对电脑配置有一定要求，但是质量更可靠。

可以修改config.toml配置文件中的subtitle_provider进行切换

建议使用edge模式，如果生成的字幕质量不好，再切换到whisper模式

注意：

1. whisper 模式下需要到 HuggingFace 下载一个模型文件，大约 3GB 左右，请确保网络通畅
2. 如果留空，表示不生成字幕。

由于国内无法访问 HuggingFace，可以使用以下方法下载whisper-large-v3的模型文件

下载地址：

* 百度网盘:https://pan.baidu.com/s/11h3Q6tsDtjQKTjUu3sc5cA?pwd=xjs9
* 夸克网盘：https://pan.quark.cn/s/3ee3d991d64b

模型下载后解压，整个目录放到.\MoneyPrinterTurbo\models里面，
最终的文件路径应该是这样:.\MoneyPrinterTurbo\models\whisper-large-v3

MoneyPrinterTurbo
 ├─models
 │ └─whisper-large-v3
 │ config.json
 │ model.bin
 │ preprocessor_config.json
 │ tokenizer.json
 │ vocabulary.json

## 背景音乐 🎵

用于视频的背景音乐，位于项目的resource/songs目录下。

当前项目里面放了一些默认的音乐，来自于 YouTube 视频，如有侵权，请删除。

## 字幕字体 🅰

用于视频字幕的渲染，位于项目的resource/fonts目录下，你也可以放进去自己的字体。

## 常见问题 🤔

### ❓RuntimeError: No ffmpeg exe could be found

通常情况下，ffmpeg 会被自动下载，并且会被自动检测到。
但是如果你的环境有问题，无法自动下载，可能会遇到如下错误：

RuntimeError: No ffmpeg exe could be found.
Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.

此时你可以从https://www.gyan.dev/ffmpeg/builds/下载ffmpeg，解压后，设置ffmpeg_path为你的实际安装路径即可。

[
app
]

#
 请根据你的实际路径设置，注意 Windows 路径分隔符为 \\

ffmpeg_path
 =
"
C:
\\
Users
\\
harry
\\
Downloads
\\
ffmpeg.exe
"

### ❓ImageMagick的安全策略阻止了与临时文件@/tmp/tmpur5hyyto.txt相关的操作

可以在ImageMagick的配置文件policy.xml中找到这些策略。
这个文件通常位于 /etc/ImageMagick-X/ 或 ImageMagick 安装目录的类似位置。
修改包含pattern="@"的条目，将rights="none"更改为rights="read|write"以允许对文件的读写操作。

### ❓OSError: [Errno 24] Too many open files

这个问题是由于系统打开文件数限制导致的，可以通过修改系统的文件打开数限制来解决。

查看当前限制

ulimit
 -n

如果过低，可以调高一些，比如

ulimit
 -n 10240

### ❓Whisper 模型下载失败，出现如下错误

LocalEntryNotfoundEror: Cannot find an appropriate cached snapshotfolderfor the specified revision on the local disk and
outgoing trafic has been disabled.
To enablerepo look-ups and downloads online, pass 'local files only=False' as input.

或者

An error occured while synchronizing the model Systran/faster-whisper-large-v3 from the Hugging Face Hub:
An error happened while trying to locate the files on the Hub and we cannot find the appropriate snapshot folder for the
specified revision on the local disk. Please check your internet connection and try again.
Trying to load the model directly from the local cache, if it exists.

解决方法：点击查看如何从网盘手动下载模型

## 反馈建议 📢

* 可以提交issue或者pull request。

## 许可证 📝

点击查看LICENSE文件

## Star History

## About

利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM.

### Topics

 python

 automation

 ai

 moviepy

 shortvideo

 tiktok

 chatgpt

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

50.6k

 stars


### Watchers

365

 watching


### Forks

7.2k

 forks


 Report repository



## Releases9

v1.2.6

 Latest



May 10, 2025



+ 8 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python97.8%
* Dockerfile1.6%
* Other0.6%
