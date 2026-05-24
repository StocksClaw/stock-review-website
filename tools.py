#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 龙虾复盘网站 - 工具集
一键管理网站的更新、部署、配置检查
"""

import os
import sys

# 修复Windows GBK终端编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def show_menu():
    """显示菜单"""
    print("=" * 60)
    print("🦞 龙虾复盘网站 - 工具集")
    print("=" * 60)
    print()
    print("可用工具:")
    print()
    print("  [1] 📊 更新报告")
    print("      → 将最新复盘报告添加到网站")
    print()
    print("  [2] 🚀 部署到GitHub")
    print("      → 一键推送代码到GitHub Pages")
    print()
    print("  [3] ⚙️  检查Gitalk配置")
    print("      → 验证评论系统配置是否正确")
    print()
    print("  [4] 🌐 启动本地服务器")
    print("      → 本地预览网站效果")
    print()
    print("  [5] 📖 查看帮助文档")
    print("      → 显示详细使用说明")
    print()
    print("  [0] 🚪 退出")
    print()
    print("=" * 60)

def run_tool(tool_num):
    """运行选中的工具"""
    if tool_num == '1':
        print("\n📊 启动报告更新工具...\n")
        os.system('python auto_update_report.py')
    
    elif tool_num == '2':
        print("\n🚀 启动GitHub部署工具...\n")
        os.system('python deploy_to_github.py')
    
    elif tool_num == '3':
        print("\n⚙️  启动配置检查工具...\n")
        os.system('python check_config.py')
    
    elif tool_num == '4':
        print("\n🌐 启动本地服务器...\n")
        print("服务地址: http://localhost:8000")
        print("按 Ctrl+C 停止服务器\n")
        os.system('python -m http.server 8000')
    
    elif tool_num == '5':
        print("\n📖 帮助文档\n")
        print("-" * 60)
        print("QUICKSTART.md - 快速启动指南")
        print("README.md     - 完整配置文档")
        print("-" * 60)
        print()
        print("查看方式:")
        print("  Windows: notepad QUICKSTART.md")
        print("  或直接用文本编辑器打开")
        print()
        print("本地测试:")
        print("  python -m http.server 8000")
        print("  浏览器访问 http://localhost:8000")
        print()
        print("部署流程:")
        print("  1. 创建GitHub仓库")
        print("  2. 运行工具 [2] 部署到GitHub")
        print("  3. 启用GitHub Pages")
        print("  4. 运行工具 [3] 配置Gitalk评论")
        print("-" * 60)
    
    elif tool_num == '0':
        print("\n👋 再见！\n")
        return False
    
    else:
        print("\n❌ 无效选项，请重新选择\n")
    
    return True

def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请选择工具 [0-5]: ").strip()
        
        if not run_tool(choice):
            break
        
        if choice != '0' and choice != '4':  # 4会阻塞在服务器
            input("\n按Enter键继续...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 再见！\n")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
