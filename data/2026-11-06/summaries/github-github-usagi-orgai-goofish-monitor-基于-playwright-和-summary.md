---
title: GitHub - Usagi-org/ai-goofish-monitor: 基于 Playwright 和AI实现的闲鱼多任务实时/定时监控与智能分析系统，配备了功能完善的后台管理UI。帮助用户从闲鱼海量商品中，找到心仪产品。 · GitHub
url: https://github.com/Usagi-org/ai-goofish-monitor
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:38.970848
---

# GitHub - Usagi-org/ai-goofish-monitor: 基于 Playwright 和AI实现的闲鱼多任务实时/定时监控与智能分析系统，配备了功能完善的后台管理UI。帮助用户从闲鱼海量商品中，找到心仪产品。 · GitHub

# 闲鱼智能监控系统概览

## 项目概述
- 基于 Playwright 与 AI 的闲鱼多任务实时监控系统
- 提供完整的 Web 可视化管理界面
- 支持自然语言创建任务、深度商品分析、结果导出等功能

## 核心特性
- Web 可视化管理：任务、账号、AI Prompt、日志、结果浏览
- AI 驱动：自然语言任务创建，多模态模型商品分析
- 多任务并发：关键词、价格、筛选条件、AI Prompt 可独立配置
- 高级筛选：包邮、新发布时间、三级地区（省/市/区）过滤
- 实时通知：ntfy.sh、企业微信、Bark、Telegram、Webhook 等
- 定时调度：Cron 表达式配置周期任务
- 账号与代理轮换：多账号管理、任务绑定、代理池轮换与失败重试
- Docker 部署：一键容器化，内置 Chromium，无需宿主机额外浏览器

## Docker 部署（推荐）
1. 克隆仓库并复制 `.env.example` 为 `.env`，填写配置项  
   ```bash
   git clone https://github.com/Usagi-org/ai-goofish-monitor
   cd ai-goofish-monitor
   cp .env.example .env
   vim .env   # 填写必要配置
   ```
2. 启动容器  
   ```bash
   docker compose up -d
   docker compose logs -f app
   ```
3. 如需加速镜像下载，可使用国内加速仓库并重新打标签后启动  
   ```bash
   docker pull ghcr.nju.edu.cn/usagi-org/ai-goofish:latest
   docker tag ghcr.nju.edu.cn/usagi-org/ai-goofish:latest ghcr.io/usagi-org/ai-goofish:latest
   docker compose up -d
   ```
- 默认 Web UI 地址：`http://127.0.0.1:8000`
- 持久化目录：`data/`（SQLite 主库）、`state/`（登录态）、`prompts/`、`logs/`、`images/` 等

## 数据存储与迁移
- 主存储使用 SQLite，默认路径 `data/app.sqlite3`（可通过 `APP_DATABASE_FILE` 环境变量自定义）
- 启动时自动建库建表，并尝试从旧的 `config.json`、`jsonl/`、`price_history/` 导入历史数据
- 图片等二进制文件仍保存在文件系统目录 `images/`，任务结束后默认清理

## 最少配置项
| 变量 | 说明 | 必填 |
|------|------|------|
| OPENAI_API_KEY | AI 模型 API Key | 是 |
| OPENAI_BASE_URL | OpenAI 兼容接口地址 | 是 |
| OPENAI_MODEL_NAME | 支持图片输入的模型名称 | 是 |
| WEB_USERNAME / WEB_PASSWORD | Web UI 登录账号密码（默认 admin/admin123） | 否 |

## 使用指南
1. 访问 `http://127.0.0.1:8000` 并使用默认或自定义账号登录  
2. 在「闲鱼账号管理」中导入 Chrome 扩展导出的登录态 JSON，文件保存至 `state/`  
3. 在「任务管理」创建任务并绑定账号，支持 AI 任务或关键词规则两种模式  
4. 任务运行后可在「结果查看」页面查询、导出 SQLite 中的记录；日志页面帮助排查登录态失效、风控、AI 调用等问题  

### 任务管理要点
- AI 任务提交后会生成后台 Job，前端弹出进度窗口  
- 关键词任务直接创建，无需 AI 生成标准  
- 区域筛选采用省/市/区三级选择器，可显著缩小结果集  

## 开发者指南
- 环境要求：Python 3.10+、Node.js + npm（建议 v20.18.3）、Playwright CLI 与 Chromium  
- 一键启动脚本 `start.sh` 会检查前置条件、安装依赖、构建前端并启动后端  
- 手动启动：  
  - 后端：`python -m src.app` 或 `uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload`  
  - 前端：`cd web-ui && npm install && npm run dev`  
- 测试：`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest`  

## 配置说明（常用项）
- **AI 与运行时**：`OPENAI_API_KEY`、`OPENAI_BASE_URL`、`OPENAI_MODEL_NAME`、`PROXY_URL`、`RUN_HEADLESS`、`SERVER_PORT`、`LOGIN_IS_EDGE`、`PCURL_TO_MOBILE`  
- **通知渠道**：`NTFY_TOPIC_URL`、`GOTIFY_URL/TOKEN`、`BARK_URL`、`WX_BOT_URL`、`TELEGRAM_BOT_TOKEN/CHAT_ID/API_BASE_URL`、`WEBHOOK_*`  
- **代理轮换与失败保护**：`PROXY_ROTATION_ENABLED`、`PROXY_ROTATION_MODE`、`PROXY_POOL`、`PROXY_ROTATION_RETRY_LIMIT`、`PROXY_BLACKLIST_TTL`、`TASK_FAILURE_THRESHOLD`、`TASK_FAILURE_PAUSE_SECONDS`、`TASK_FAILURE_GUARD_PATH`  

## 工作流程概览
1. 启动监控任务 → 选择账号/代理  
2. 执行商品搜索 → 发现新商品则抓取详情、卖家信息、下载图片  
3. 调用 AI 进行分析 → AI 推荐则发送通知，否则保存记录  
4. 若未发现新商品则翻页或等待继续搜索  
5. 触发风控/异常时自动进行账号或代理轮换并重试  

## 常见问题
- **AI 任务创建为何不立即完成？**  
  AI 模式先生成分析标准，采用后台 Job 方式避免表单卡死。  
- **区域筛选默认建议留空？**  
  区域筛选会显著减少结果，适用于只关注特定地区的场景。  
- **前端构建产物缺失怎么办？**  
  执行 `./start.sh` 或在 `web-ui/` 目录手动 `npm run build`，确保 `dist/` 已复制到根目录。  
- **缺少 Playwright 或浏览器提示？**  
  按脚本提示安装 Playwright CLI 与 Chromium，或确保系统已安装 Chrome/Edge。  

## 致谢
- 参考项目：`superboyyy/xianyu_spider`  
- 感谢 LinuxDo 社区及贡献者 `@jooooody`、ClaudeCode、Gemini、Codex 等模型工具的支持  

## 注意事项
- 请遵守闲鱼用户协议和 robots.txt，避免高频请求导致账号被限制  
- 本项目仅供学习、技术研究使用，禁止用于非法用途  
- 项目采用 MIT 许可证，按“现状”提供，不提供任何形式的担保  
- 作者及贡献者对因使用本软件导致的任何直接或间接损失不承担责任  

---  
如需进一步了解，请查阅仓库根目录下的 `README.md`、`DISCLAIMER.md` 与 `LICENSE`。