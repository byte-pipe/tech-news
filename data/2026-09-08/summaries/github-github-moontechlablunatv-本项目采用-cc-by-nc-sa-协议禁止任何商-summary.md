---
title: GitHub - MoonTechLab/LunaTV: 本项目采用 CC BY-NC-SA 协议，禁止任何商业化行为，任何衍生项目必须保留本项目地址并以相同协议开源 · GitHub
url: https://github.com/MoonTechLab/LunaTV
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:31:30.198471
---

# GitHub - MoonTechLab/LunaTV: 本项目采用 CC BY-NC-SA 协议，禁止任何商业化行为，任何衍生项目必须保留本项目地址并以相同协议开源 · GitHub

# MoonTV 项目概览

## 功能特性
- 多源聚合搜索：一次搜索返回全部资源结果  
- 丰富详情页：展示剧集列表、演员、年份、简介等信息  
- 流畅在线播放：集成 HLS.js 与 ArtPlayer  
- 收藏与继续观看：支持 Kvrocks、Redis、Upstash 存储，多端同步进度  
- PWA：离线缓存，可安装到桌面或移动主屏，提供原生体验  
- 响应式布局：桌面侧边栏 + 移动底部导航，自适应各种屏幕尺寸  
- 智能去广告（实验性）：自动跳过视频中的切片广告  

> 注意：部署后项目为空壳，无内置播放源和直播源，需要自行收集。

## 技术栈
- 前端框架：Next.js 14（App Router）  
- UI 与样式：Tailwind CSS 3  
- 语言：TypeScript 4  
- 播放器：ArtPlayer、HLS.js  
- 代码质量：ESLint、Prettier、Jest  
- 部署方式：Docker  

## 部署方式

### Docker 部署（通用）
项目仅支持 Docker 或基于 Docker 的平台部署。

### Zeabur 一键部署（推荐）
1. 添加 Kvrocks 服务（端口 6666，持久化卷路径 `/var/lib/kvrocks/db`）。  
2. 添加 LunaTV 服务（镜像 `ghcr.io/moontechlab/lunatv:latest`，端口 3000）。  
3. 配置环境变量（管理员账号、存储类型、Kvrocks 连接 URL 等）。  
4. 部署完成后在 Zeabur 为 LunaTV 服务设置访问域名（可生成免费域名或绑定自定义域名）。  
5. 如需更新镜像，手动重启服务即可拉取最新 `latest` 标签。

### 存储选项

| 存储方式 | 说明 | 示例 docker-compose 片段 |
|----------|------|---------------------------|
| Kvrocks（推荐） | 高性能键值数据库，持久化安全 | `NEXT_PUBLIC_STORAGE_TYPE=kvrocks`<br>`KVROCKS_URL=redis://moontv-kvrocks:6666` |
| Redis | 本地 Redis，存在数据丢失风险，需开启持久化 | `NEXT_PUBLIC_STORAGE_TYPE=redis`<br>`REDIS_URL=redis://moontv-redis:6379` |
| Upstash | 云端 Redis，即付即用 | `NEXT_PUBLIC_STORAGE_TYPE=upstash`<br>`UPSTASH_URL=HTTPS_ENDPOINT`<br>`UPSTASH_TOKEN=TOKEN` |

## 配置文件
部署完成后需在管理后台填写 JSON 配置文件，例如：

```json
{
  "cache_time": 7200,
  "api_site": {
    "dyttzy": {
      "api": "http://xxx.com/api.php/provide/vod",
      "name": "示例资源",
      "detail": "http://xxx.com"
    }
    // …更多站点
  },
  "custom_category": [
    {
      "name": "华语",
      "type": "movie",
      "query": "华语"
    }
  ]
}
```

- `cache_time`：接口缓存时间（秒）。  
- `api_site`：键为唯一标识，`api` 为资源站提供的 vodJSON API 根地址，`name` 为前端显示名称，`detail`（可选）用于爬取无法通过 API 获取的剧集详情。  
- `custom_category`：自定义分类，`type` 支持 `movie`（电影）或 `tv`（电视剧），`query` 为豆瓣搜索关键词。  

项目兼容标准的苹果 CMS V10 API 格式。

## 订阅
将完整的配置文件进行 base58 编码并提供 HTTP 服务，即可生成订阅链接，供 MoonTV 后台或 Helios 使用。

## 自动更新
可使用 `watchtower`、`dockge`、`komodo` 等 Docker 自动更新工具，或在 Zeabur 手动重启服务以拉取最新镜像。

## 环境变量

| 变量 | 必填 | 说明 | 示例 |
|------|------|------|------|
| USERNAME | 是 | 站长账号 | admin |
| PASSWORD | 是 | 站长密码 | your_secure_password |
| SITE_BASE | 否 | 站点 URL（如 `https://example.com`） |  |
| NEXT_PUBLIC_SITE_NAME | 否 | 站点名称 | MoonTV |
| ANNOUNCEMENT | 否 | 站点公告文字 | 本网站仅提供影视信息搜索服务，所有内容均来自第三方网站… |
| NEXT_PUBLIC_STORAGE_TYPE | 是 | 播放记录/收藏的存储方式（redis、kvrocks、upstash） | kvrocks |
| KVROCKS_URL | 否 | Kvrocks 连接 URL | redis://apachekvrocks:6666 |
| REDIS_URL | 否 | Redis 连接 URL | redis://moontv-redis:6379 |
| UPSTASH_URL | 否 | Upstash Redis HTTPS ENDPOINT | https://… |
| UPSTASH_TOKEN | 否 | Upstash 访问 Token | your_token |
| NEXT_PUBLIC_SEARCH_MAX_PAGE | 否 | 搜索接口最大页数（1-50） | 5 |
| NEXT_PUBLIC_DOUBAN_PROXY_TYPE | 否 | 豆瓣数据源请求方式 | direct |
| NEXT_PUBLIC_DOUBAN_PROXY | 否 | 自定义豆瓣数据代理 URL 前缀 |  |
| NEXT_PUBLIC_DOUBAN_IMAGE_PROXY_TYPE | 否 | 豆瓣图片代理类型 | direct |

## 注意事项
- 项目采用 **CC BY-NC-SA** 协议，禁止任何商业化行为，衍生项目必须保留原项目地址并使用相同协议开源。  
- 请勿在 B 站、小红书、微信公众号、抖音、今日头条或其他中国大陆社交平台发布视频或文章宣传本项目。  
- 部署后需自行收集并配置播放源与直播源。  
- 如使用 Redis，请务必开启持久化以防数据丢失。