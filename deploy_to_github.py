#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键部署网站到GitHub Pages
功能：
1. 初始化Git仓库
2. 添加远程仓库
3. 提交所有文件
4. 推送到GitHub
"""

import os
import sys
import subprocess
from pathlib import Path

# 修复Windows GBK终端编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 网站目录
WEBSITE_DIR = Path(r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website')

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or WEBSITE_DIR,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, '', str(e)

def check_git():
    """检查Git是否已安装"""
    success, stdout, stderr = run_command('git --version')
    if success and 'git version' in stdout.lower():
        print(f"✅ Git已安装: {stdout.strip()}")
        return True
    else:
        print("❌ Git未安装，请先安装Git")
        print("下载地址: https://git-scm.com/download/win")
        return False

def init_git():
    """初始化Git仓库"""
    git_dir = WEBSITE_DIR / '.git'
    if git_dir.exists():
        print("✅ Git仓库已存在")
        return True
    
    success, stdout, stderr = run_command('git init')
    if success:
        print("✅ Git仓库初始化成功")
        return True
    else:
        print(f"❌ Git初始化失败: {stderr}")
        return False

def add_remote(username, repo_name):
    """添加远程仓库"""
    # 先检查是否已有remote
    success, stdout, stderr = run_command('git remote -v')
    if 'origin' in stdout:
        print("✅ 远程仓库已配置")
        return True
    
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    success, stdout, stderr = run_command(f'git remote add origin {remote_url}')
    
    if success or 'already exists' in stderr.lower():
        print(f"✅ 远程仓库已添加: {remote_url}")
        return True
    else:
        print(f"❌ 添加远程仓库失败: {stderr}")
        return False

def commit_files():
    """提交所有文件"""
    # 添加所有文件
    success, stdout, stderr = run_command('git add .')
    if not success:
        print(f"❌ git add 失败: {stderr}")
        return False
    
    # 检查是否有改动
    success, stdout, stderr = run_command('git status --porcelain')
    if not stdout.strip():
        print("ℹ️  没有需要提交的改动")
        return True
    
    # 提交
    success, stdout, stderr = run_command('git commit -m "Update website"')
    if success or 'nothing to commit' in stdout.lower():
        print("✅ 文件已提交")
        return True
    else:
        print(f"❌ 提交失败: {stderr}")
        return False

def push_to_github():
    """推送到GitHub"""
    # 先检查当前分支
    success, stdout, stderr = run_command('git branch --show-current')
    branch = stdout.strip() if success else 'main'
    
    # 如果是新仓库，可能需要设置上游分支
    success, stdout, stderr = run_command(f'git push -u origin {branch}')
    
    if success:
        print(f"✅ 已推送到GitHub ({branch}分支)")
        return True
    else:
        if 'no upstream branch' in stderr.lower():
            # 尝试设置上游分支
            success, stdout, stderr = run_command(f'git push --set-upstream origin {branch}')
            if success:
                print(f"✅ 已推送到GitHub ({branch}分支)")
                return True
        
        print(f"❌ 推送失败: {stderr}")
        if 'authentication failed' in stderr.lower() or 'permission denied' in stderr.lower():
            print("\n💡 解决方法:")
            print("   1. 检查GitHub用户名和仓库权限")
            print("   2. 使用SSH密钥或Personal Access Token")
            print("   3. 或使用GitHub Desktop: https://desktop.github.com/")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🦞 龙虾复盘网站 - GitHub部署助手")
    print("=" * 60)
    print()
    
    # 检查Git
    if not check_git():
        return False
    
    print("\n📋 部署步骤:")
    print("   1. 在GitHub创建仓库（如果还没有）")
    print("   2. 输入GitHub用户名和仓库名")
    print("   3. 自动推送代码")
    print()
    
    # 获取GitHub信息
    username = input("👤 GitHub用户名: ").strip()
    if not username:
        print("❌ 用户名不能为空")
        return False
    
    repo_name = input("📦 仓库名 (默认: stock-review-website): ").strip()
    if not repo_name:
        repo_name = 'stock-review-website'
    
    print(f"\n🎯 目标仓库: https://github.com/{username}/{repo_name}")
    print()
    
    # 确认
    confirm = input("确认部署？(y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ 已取消")
        return False
    
    print("\n" + "=" * 60)
    print("开始部署...")
    print("=" * 60)
    
    # 步骤1：初始化Git
    print("\n[1/4] 初始化Git仓库...")
    if not init_git():
        return False
    
    # 步骤2：添加远程仓库
    print("\n[2/4] 添加远程仓库...")
    if not add_remote(username, repo_name):
        return False
    
    # 步骤3：提交文件
    print("\n[3/4] 提交文件...")
    if not commit_files():
        return False
    
    # 步骤4：推送到GitHub
    print("\n[4/4] 推送到GitHub...")
    if not push_to_github():
        return False
    
    # 成功提示
    print("\n" + "=" * 60)
    print("✅ 部署成功！")
    print("=" * 60)
    print(f"\n🌐 网站地址: https://{username}.github.io/{repo_name}/")
    print(f"📊 GitHub仓库: https://github.com/{username}/{repo_name}")
    print("\n📝 下一步:")
    print("   1. 访问仓库设置启用GitHub Pages")
    print(f"      → https://github.com/{username}/{repo_name}/settings/pages")
    print("   2. Source选择 'main' 分支，点击Save")
    print("   3. 等待1-2分钟部署完成")
    print(f"   4. 访问 https://{username}.github.io/{repo_name}/")
    
    return True

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ 已取消")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
