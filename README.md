# 去广告合集 · Shadowrocket All-in-One

把 [LOWERTOP/Shadowrocket-First](https://github.com/LOWERTOP/Shadowrocket-First) 及社区收录的去广告模块合并成一个 `.sgmodule`，一个文件导入即用。

**已排除**：哔哩哔哩增强、哔哩哔哩国际版。

## 安装

- 网页一键安装：<https://alexanderava.github.io/sr-adblock/>
- 模块地址（`shadowrocket://install?module=` 后面拼这个）：

```
https://raw.githubusercontent.com/Alexanderava/sr-adblock/main/AdBlock.sgmodule
```

- 或者直接下载 `AdBlock.sgmodule`，用 Shadowrocket 打开导入。

## 内容

| 文件 | 说明 |
|---|---|
| `AdBlock.sgmodule` | 合并后的模块，约 89 KB |
| `index.html` | 一键安装页（GitHub Pages） |

规模：20 个模块 + 1 套通用规则集 · 377 条规则 · 51 条 URL Rewrite · 18 条 Map Local · 126 条 jq · 31 个脚本 · 51 个 MITM 域名 · 31 个可调参数。

## 生效前提

1. 全局路由设为 **「配置」** 模式
2. 开启 **HTTPS 解密** 并信任证书，否则 jq / 脚本类模块无效
3. 部分 App 需清缓存或重装（微博、小红书、贴吧尤其明显）

## 自定义

模块内每段都带 `# ------- 模块名 -------` 横幅，删掉对应几行即可关闭某个 App。
通用规则集在文件末尾 `# ======= AntiAD` 之后，整段删除不影响其他模块。

## 来源与版权

所有规则、脚本、配色均来自原作者，此处仅做格式合并：

- LOWERTOP（铁柱）· 向晚 · 奶思 / fmz200 · iab0x00 · app2smile · xream / QingRex · Reukix · Maasea
- 脚本仍从各原作者仓库实时拉取，本仓库不含 JS 本体

合并为静态文件，不随上游自动更新；单个 App 失效时回原仓库取最新单模块替换对应段落即可。
