#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从奶思的 QX rewrite.snippet 提取域名规则，生成 Shadowrocket 规则集（.list）。

用法：
    python3 gen_rules.py <源 URL> <输出文件>

由 GitHub Actions 定时运行，把最新规则写进 rules/naisi.list。
"""

import os
import re
import sys
import urllib.request

SRC_DEFAULT = "https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/rewrite/rewrite.snippet"
OUT_DEFAULT = "rules/naisi.list"

HOST_MAP = {
    "host-suffix": "DOMAIN-SUFFIX",
    "host": "DOMAIN",
    "host-keyword": "DOMAIN-KEYWORD",
    "ip-cidr": "IP-CIDR",
    "ip6-cidr": "IP-CIDR6",
}


def fetch(url):
    # 本地路径直接读，便于离线/自测
    if os.path.exists(url):
        return open(url, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(url, headers={"User-Agent": "ruleset-sync/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else SRC_DEFAULT
    out = sys.argv[2] if len(sys.argv) > 2 else OUT_DEFAULT

    text = fetch(src)
    rules, seen = [], set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(";") or line.startswith("#"):
            continue
        m = re.match(
            r"^(host-suffix|host|host-keyword|ip-cidr|ip6-cidr)\s*,\s*([^,]+?)\s*,\s*(\S+)\s*$",
            line, re.I,
        )
        if not m:
            continue
        kind, value, policy = m.group(1).lower(), m.group(2).strip(), m.group(3).strip()
        if policy.lower() != "reject":
            continue
        rule = "%s,%s,REJECT" % (HOST_MAP[kind], value)
        if rule not in seen:
            seen.add(rule)
            rules.append(rule)

    header = [
        "# 奶思（fmz200）730 App 广告域名规则集",
        "# 源：https://github.com/fmz200/wool_scripts",
        "# 由 GitHub Actions 自动同步，请勿手动编辑",
        "# 规则数：%d" % len(rules),
        "",
    ]

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(header + rules) + "\n")

    print("已生成 %s，%d 条规则" % (out, len(rules)))


if __name__ == "__main__":
    main()
