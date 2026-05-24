#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gitalk配置检查工具
验证GitHub App配置是否正确
"""

import os
import sys
import re
import json
from pathlib import Path

# 修复Windows GBK终端编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

WEBSITE_DIR = Path(r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website')
JS_FILE = WEBSITE_DIR / 'js' / 'main.js'

def check_js_config():
    """检查js/main.js中的配置"""
    print("📋 检查Gitalk配置...\n")
    
    if not JS_FILE.exists():
        print("❌ 文件不存在: js/main.js")
        return False
    
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查owner
    owner_match = re.search(r"owner:\s*'([^']+)'", content)
    if owner_match:
        owner = owner_match.group(1)
        if owner == 'YOUR_GITHUB_USERNAME':
            issues.append("❌ owner: 需要替换为你的GitHub用户名")
        else:
            print(f"✅ owner: {owner}")
    else:
        issues.append("❌ 未找到 owner 配置")
    
    # 检查repo
    repo_match = re.search(r"repo:\s*'([^']+)'", content)
    if repo_match:
        repo = repo_match.group(1)
        if repo == 'stock-review-website':
            print(f"⚠️  repo: {repo} (请确认仓库名是否正确)")
        else:
            print(f"✅ repo: {repo}")
    else:
        issues.append("❌ 未找到 repo 配置")
    
    # 检查clientID
    client_id_match = re.search(r"clientID:\s*'([^']+)'", content)
    if client_id_match:
        client_id = client_id_match.group(1)
        if client_id == 'YOUR_CLIENT_ID':
            issues.append("❌ clientID: 需要替换为GitHub App的Client ID")
        else:
            print(f"✅ clientID: {client_id[:20]}...")
    else:
        issues.append("❌ 未找到 clientID 配置")
    
    # 检查clientSecret
    secret_match = re.search(r"clientSecret:\s*'([^']+)'", content)
    if secret_match:
        secret = secret_match.group(1)
        if secret == 'YOUR_CLIENT_SECRET':
            issues.append("❌ clientSecret: 需要替换为GitHub App的Client Secret")
        else:
            print(f"✅ clientSecret: {secret[:10]}...")
    else:
        issues.append("❌ 未找到 clientSecret 配置")
    
    # 检查报告列表
    reports_match = re.search(r'reports:\s*\[([^\]]+)\]', content, re.DOTALL)
    if reports_match:
        reports_text = reports_match.group(1)
        report_count = reports_text.count('date:')
        print(f"\n📊 报告列表: {report_count} 个报告")
        
        # 提取第一个报告的日期
        first_date_match = re.search(r"date:\s*'([^']+)'", reports_text)
        if first_date_match:
            print(f"   最新报告: {first_date_match.group(1)}")
    else:
        issues.append("❌ 未找到 reports 配置")
    
    # 输出问题
    if issues:
        print("\n⚠️  需要修复的问题:")
        for issue in issues:
            print(f"   {issue}")
        
        print("\n📝 修复步骤:")
        print("   1. 访问 https://github.com/settings/apps")
        print("   2. 点击你创建的GitHub App")
        print("   3. 复制 Client ID")
        print("   4. 点击 'Generate a new client secret' 生成 Client Secret")
        print("   5. 编辑 js/main.js，替换以下占位符:")
        print("      - YOUR_GITHUB_USERNAME → 你的GitHub用户名")
        print("      - YOUR_CLIENT_ID → GitHub App的Client ID")
        print("      - YOUR_CLIENT_SECRET → GitHub App的Client Secret")
        
        return False
    else:
        print("\n✅ 配置检查通过！")
        return True

def check_github_app_instructions():
    """显示GitHub App创建指南"""
    print("\n" + "=" * 70)
    print("📖 GitHub App 创建指南")
    print("=" * 70)
    print()
    print("步骤1: 创建GitHub App")
    print("-" * 70)
    print("1. 访问: https://github.com/settings/apps/new")
    print("2. 填写信息:")
    print("   - App name: stock-review-gitalk (或自定义)")
    print("   - Homepage URL: https://YOUR_USERNAME.github.io/stock-review-website/")
    print("   - Callback URL: https://YOUR_USERNAME.github.io/stock-review-website/")
    print("   - Webhook: 取消勾选 'Active'")
    print()
    print("3. 设置权限 (Repository permissions):")
    print("   - Issues: Read & write")
    print("   - Contents: Read-only")
    print()
    print("4. 选择 'Any account' (允许安装到任何账户)")
    print("5. 点击 'Create GitHub App'")
    print()
    print("步骤2: 获取凭证")
    print("-" * 70)
    print("1. 在App页面找到 'Client ID'，复制它")
    print("2. 点击 'Generate a new client secret'")
    print("3. 立即复制 Client Secret（只显示一次）")
    print()
    print("步骤3: 安装App到仓库")
    print("-" * 70)
    print("1. 访问: https://github.com/apps/YOUR_APP_NAME/installations/new")
    print("2. 选择你的仓库")
    print("3. 点击 'Install'")
    print()
    print("步骤4: 更新配置文件")
    print("-" * 70)
    print("编辑 js/main.js，填入你的信息:")
    print("""
const CONFIG = {
    github: {
        owner: '你的GitHub用户名',
        repo: 'stock-review-website',
        clientID: '你的Client ID',
        clientSecret: '你的Client Secret'
    },
    ...
};
""")
    print("=" * 70)

def main():
    """主函数"""
    print("=" * 70)
    print("🦞 龙虾复盘网站 - Gitalk配置检查工具")
    print("=" * 70)
    print()
    
    # 检查配置
    config_ok = check_js_config()
    
    # 显示指南
    if not config_ok:
        check_github_app_instructions()
    
    print("\n💡 提示:")
    print("   - 修改 js/main.js 后需要重新提交到GitHub")
    print("   - Gitalk首次使用需要用户登录GitHub账号")
    print("   - 评论会保存在GitHub Issues中")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ 已取消")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
