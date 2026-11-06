---
title: GitHub - JiaFeiMiao-K-Cat/DiscImageStudio · GitHub
url: https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:58.937824
---

# GitHub - JiaFeiMiao-K-Cat/DiscImageStudio · GitHub

# Disc Image Studio 项目概览

## 项目简介
- 多平台光盘盘面图像生成与刻录工具，可在 CD、DVD 与单层蓝光（BD‑R）光盘上刻出肉眼可见的图案。  
- 将普通图片转换为符合光盘物理层约束的数据，支持导出 ISO、RAW、WAV+CUE 等格式。

## 主要功能
- **光盘数据生成**  
  - CD：导出带格式头的 WAV 音轨及 CUE，兼容 cdrecord、ImgBurn 等；亦可导出 RAW 音轨。  
  - DVD：导出 ISO 镜像。  
  - 蓝光：支持单层 BD‑R（25 GB），可生成纯绘图或 UDF 2.01 文件系统。  
  - 随盘文件：在设计页直接选择文件夹及内外圈位置，导出页可调节。  
  - 灰度方案与抖动工具：提供 CD、DVD 的二阶黑白灰度及独立 PNG 抖动处理程序。  
  - 盘片预设：内置多品牌光盘参数，支持用户自定义贡献。  

- **辅助标定**  
  - 粗标定、边界标定、精细标定三阶段流程，通过盘面照片估计半径与轨距，提升图案直线度。  

- **刻录**  
  - 导出完整 ISO/RAW 文件后手动刻录。  
  - 实验性即时流式刻录：边生成边写入 CD、DVD、BD‑R（仅单层），不保存完整镜像。  

## 快速入门
- **Windows**：下载 `win-x64.exe` 直接运行。  
- **Linux/macOS**：下载对应 CPU 架构的 CLI 包，解压后运行 `./disc-image-studio --help`（自带 .NET 运行时）。  
- 步骤：  
  1. 新建工程（选择 CD、DVD 或蓝光，指定输出位置）。  
  2. 设计盘面：导入图片，使用图层排版，调节抖动、伽马、亮度、灰阶档位。  
  3. 预览与导出：在预览页核对投影，导出 ISO/RAW/WAV+CUE，或使用即时刻录写入空白盘片（仅用于可报废的测试介质）。

## 系统要求
- 桌面版：Windows 10 2004 及以上或 Windows 11。  
- 构建环境：.NET 10 SDK（`global.json` 锁定 10.0.x），Release EXE 已包含运行时。  
- 即时刻录需 Windows 识别的 CD/DVD/BD 刻录机和空白盘片，BD‑R 必须支持顺序写入。

## 构建与运行
```bash
dotnet build DiscImageStudio.slnx -c Release
dotnet run --project src/DiscImageStudio.App -c Release
```
- 回归检查：运行 `DvdImageSolver`、`DiscImageStudio.ArchitectureTests` 等自测命令。  
- 发布流程详见 `RELEASING.md`（CI、MSIX 打包、签名等）。

## 命令行工具
- 支持 Linux（glibc）x64/arm64、macOS（Intel/Apple Silicon）等平台。  
- 常用子命令示例：  
  - `cd-generate`：生成 WAV+CUE 或 CD 数据盘 ISO。  
  - `dvd-generate`（`solve`）：快速纹理映射生成 DVD 镜像。  
  - `bd-generate`：生成完整 BD‑R ISO 并输出 sidecar JSON。  
  - `calibrate`、`simulate`、`selftest` 等用于标定、仿真与回归测试。  

## 源码结构
- `src/DiscImageStudio.Cli/`：跨平台 CLI 入口。  
- `src/DiscImageStudio.Core/`、`Imaging/`、`Burning/` 等：核心模块、图像预处理、Windows IMAPI2 刻录层。  
- `src/DiscImageStudio.App/`：WPF GUI。  
- `src/DvdImageSolver/`：独立 DVD 编码/求解引擎。  
- `tests/`、`packaging/`、`tools/`、`docs/`：测试、打包脚本、辅助工具、文档。

## 文档与标准
- 关键文档：`ARCHITECTURE.md`、`DVD_ENGINE.md`、`ADDING_BLURAY.md`、`CALIBRATION_TUTORIAL.md` 等。  
- 参考标准：ECMA‑394（CD‑R）、ECMA‑267/359（DVD‑R）、ISO/IEC 30190:2021（BD‑R）以及 CD‑ROM ECMA‑130。

## 使用安全与隐私
- 不安装驱动或服务，使用 Windows 自带的 IMAPI2。  
- 实验性即时刻录仅建议在可报废的测试介质上使用，可能导致盘片报废。  
- 项目不联网、不收集遥测，详见 `PRIVACY.md`。  
- 安全问题请通过 GitHub 私密报告渠道披露。

## 贡献与许可证
- 欢迎提交 Issue 与 Pull Request，贡献指南位于 `CONTRIBUTING.md`。  
- 采用 GNU GPL v3.0 或更高版本（GPL‑3.0‑or‑later），部分代码来源于 CDImage 项目并保持兼容授权。  

## 致谢
- 感谢 arduino**celentano** 的 CDImage 项目提供的 CD 交织实现与盘面绘图思路，为本项目奠定重要基础。