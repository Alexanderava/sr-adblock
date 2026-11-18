# 去广告合集 · Shadowrocket All-in-One

把 [LOWERTOP/Shadowrocket-First](https://github.com/LOWERTOP/Shadowrocket-First) 及社区收录的去广告模块合并成一个 `.sgmodule`，一个文件导入即用。

**未合并**：无（社区主要模块已全部纳入）。

## 安装

- 网页一键安装：<https://alexanderava.github.io/sr-adblock/>
- 模块地址（`shadowrocket://install?module=` 后面拼这个）：

```
https://raw.githubusercontent.com/Alexanderava/sr-adblock/main/AdBlock.sgmodule
```

- 或者直接下载 `AdBlock.sgmodule`，用 Shadowrocket 打开导入。

## 去掉了哪些广告

| App / 站点 | 具体去掉的内容 |
|---|---|
| 微博 | 开屏 · 热搜榜推广 · 超话推广 · 评论区广告 · 转发区广告 · 详情页广告 · 发现页推广 · 每日弹窗 · 顶部 tab 分组推广 · 信息收集埋点 |
| 微博轻享版 | 热搜词 · 搜索发现 · 「我的」页冗余入口 |
| 百度贴吧 | 开屏广告 · 信息流广告 · 推荐页视频贴（可关）· 广告域名 DNS 查询 |
| 哔哩哔哩 | 开屏广告 · 首页/动态/搜索广场推广位 · 会员购与付费推广素材 · 直播带货卡片 · 游戏中心大卡 · 置顶评论广告 · 播放结束页推荐 · 青少年模式提示 · P2P 上传（可关）· 空降助手（可关） |
| 哔哩哔哩国际版（白B） | 热搜 · 搜索发现 · 「我的」页冗余入口与卡片 |
| 小红书 | 开屏 · 信息流 · 搜索广告 · 广告素材引导 · 营销盒子触发 · 图片与视频水印 · 秒针归因 · 埋点上报 · QUIC 强制走 TCP |
| 滴滴出行 | 开屏 · 首页推荐位 · 底栏推广 · 「我的」福利/金融/更多服务卡片 · 优惠商城 · 活动 feeds · 行程中广告组件 |
| 携程 | 开屏 · 首页弹窗 · 信息流 / Banner · 广告埋点 ma-adx · TCP 网关（可切） |
| 瑞幸咖啡 | 开屏广告 · 点单弹窗 · 首页营销位 · 养成日历 · 礼品卡推荐 · 广告图片资源 |
| 特来电 | 开屏聚合 · 广告 SDK · 广告位接口 · 商城轮播 · PLUS 促销 · 券包售卖 · 福利群二维码 · 友盟/Bugly/字节埋点 |
| 高德地图 | 开屏 · 首页 Banner · 搜索热词与提示词 · 附近点评推广卡 · 天气页增值位 · AI 推荐位 · 广告图片 CDN · 埋点 |
| 彩云天气 | 首页推广卡 · 搜索推荐 · 弹窗与浮层 · 活动位 · SVIP 推荐 · 广告统计域名 |
| 一汽大众 | 开屏展位 · 首页 Banner 与浮标 · 权益卡 · 内容推荐流 · 活动广场 · 搜索提示词 |
| 红果短剧 | 阅读页广告 · 广告位接口 · 广告视频资源 · 信息流推广 |
| 包子漫画（网页版） | 页面元素级广告 · 安装 App 横幅 |
| 小蚁摄像机 | 广告接口 · 配置下发广告位 |
| 德施曼 | 多盟广告网络 · 广告点击归因 · Talk-Plus 广告 SDK · 行为追踪 · 友盟/个推上报 · Shopee 打点 |
| 浩辰 CAD 看图王 | 广告连接（纯规则，无需解密） |
| Qing | 开屏广告 · 火山引擎 APMPlus 遥测 · MobTech 隐私追踪 · HTTPDNS（另有 6 项本地解锁，默认关） |
| YouTube | 视频广告 · 首页与搜索推广 · Shorts/上传/选段按钮（可关）· 画中画 · YouTube Music 广告 |
| Spotify | 首页广告 · 播放页广告 · 会员配置解锁 · 歌词补全与翻译 |
| Reddit | 推广帖 · 详情页广告 · NSFW 提示 · 自动翻译 |
| SDGun 社区 | 开屏广告 · 轮播广告 |
| Pinterest | 首页推广帖 · 相关推荐推广帖 |
| Talkatone | AdMob / InMobi / Criteo / Smaato / AppLovin / Amazon 广告系统 |
| Discord | 历史消息自动翻译（Google 翻译）· 双语对照 · 可调条目数与目标语言 · 阻断 UDP 443 |
| GitHub 资源加速 | RAW 资源 302 到 jsDelivr CDN · 可选 cdn / fastly / gcore 节点 |
| GitHub 私库访问 | 按用户名自动注入 PAT Token · 支持 4 个账号 · 私密仓库 raw / gist · 默认未启用 |
| GitHub 限制解除 | 解除 zh-CN 语言限制 · 缓解 429 Too Many Requests |
| 苹果助手 | App Store 下载走金山 CDN · 系统升级走 cdn-apple · 可换网宿 / 阿里 CDN |
| AWAvenue 秋风广告规则 | 998 条精确域名级广告封锁，覆盖各家 App 内置广告 SDK、统计与归因域名 |
| AntiAD 通用兜底 | 淘宝 · 贴吧 · 微博 · 微信公众号 · 字节穿山甲 · 腾讯广点通 · 友盟 · 快手 · Viber · 各类广告联盟与统计上报 |

## 规模

28 个模块 + 2 套通用规则集 · 1394 条规则 · 62 条 URL Rewrite · 27 条 Map Local · 137 条 jq · 39 个脚本 · 75 个 MITM 域名 · 59 个可调参数 · 4 条 Host 映射 · 约 171 KB。

规则顺序：具体 App 模块 → AWAvenue 通用规则（998 条）→ AntiAD 自用规则（兜底）。首条匹配生效，所以前面模块的 DIRECT 白名单不会被后面的通用 REJECT 覆盖。

## 生效前提

1. 全局路由设为 **「配置」** 模式
2. 开启 **HTTPS 解密** 并信任证书，否则 jq / 脚本类模块无效
3. 部分 App 需清缓存或重装（微博、小红书、贴吧尤其明显）
4. **哔哩哔哩额外要求**：Shadowrocket ≥ 2.2.81(3096)，并在设置里开启 **HTTP/2 MITM**；低版本请删除哔哩哔哩对应的段落（搜 `哔哩哔哩增强`），或在 `[MITM]` 里排除解密 `-grpc.biliapi.net`
5. **GitHub 加速与私库互斥**：加速模块会把 RAW 请求 302 到 jsDelivr，导致私库的 Token 注入失效。用私库请删掉「GitHub 资源加速」那两行 URL Rewrite；用加速则保持默认、不开私库开关
6. **AWAvenue 覆盖面广**：998 条精确域名封锁，个别 App 可能出现图片不加载或登录异常 —— 搜 `AWAvenue` 删掉整段再试

## 自定义

模块内每段都带 `# ------- 模块名 -------` 横幅，删掉对应几行即可关闭某个 App。
通用规则集在文件末尾 `# ======= AntiAD` 之后，整段删除不影响其他模块。

## 来源与版权

所有规则、脚本均来自原作者，此处仅做格式合并：

- LOWERTOP（铁柱）· 向晚 · 奶思 / fmz200 · iab0x00 · app2smile · xream / QingRex · Reukix · Maasea · kokoryh · TG-Twilight
- 脚本仍从各原作者仓库实时拉取，本仓库不含 JS 本体

合并为静态文件，不随上游自动更新；单个 App 失效时回原仓库取最新单模块替换对应段落即可。
