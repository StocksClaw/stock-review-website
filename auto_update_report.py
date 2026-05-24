#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新网站复盘报告
功能：
1. 将 _last_report.html 复制到 reports/ 目录（用日期命名）
2. 更新 js/main.js 中的报告列表
3. 更新 reports.html 中的报告链接
"""

import os
import sys
import re
import shutil
from datetime import datetime
from pathlib import Path

# 修复Windows GBK终端编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 配置路径
WEBSITE_DIR = Path(r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website')
SRC_REPORT = Path(r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\_last_report.html')
REPORTS_DIR = WEBSITE_DIR / 'reports'
JS_FILE = WEBSITE_DIR / 'js' / 'main.js'
REPORTS_HTML = WEBSITE_DIR / 'reports.html'

def get_report_info(html_content):
    """从HTML内容中提取报告信息"""
    info = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'title': f'龙虾复盘 | {datetime.now().strftime("%Y.%m.%d")} 周五',
        'sentiment': '未知',
        'position': '未知'
    }
    
    # 提取日期
    date_match = re.search(r'(\d{4})\.(\d{2})\.(\d{2})', html_content)
    if date_match:
        info['date'] = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
        info['title'] = f"龙虾复盘 | {date_match.group(1)}.{date_match.group(2)}.{date_match.group(3)}"
    
    # 提取标题（从<title>或<h1>标签）
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
    if title_match:
        info['title'] = title_match.group(1).strip()
    
    # 提取情绪周期
    sentiment_match = re.search(r'情绪周期[：:]\s*([^\s<]+)', html_content)
    if sentiment_match:
        info['sentiment'] = sentiment_match.group(1).strip()
    
    # 提取仓位建议
    position_match = re.search(r'仓位[建议：:]*\s*([^\s<]+)', html_content)
    if position_match:
        info['position'] = position_match.group(1).strip()
    
    return info

def update_js_config(report_info):
    """更新 js/main.js 中的报告列表"""
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 构建新的报告项
    new_report = (
        "{\n"
        "            date: '" + report_info['date'] + "',\n"
        "            title: '" + report_info['title'] + "',\n"
        "            file: 'reports/" + report_info['date'] + ".html',\n"
        "            sentiment: '" + report_info['sentiment'] + "',\n"
        "            position: '" + report_info['position'] + "'\n"
        "        }"
    )
    
    # 查找 reports 数组的位置
    reports_match = re.search(r'reports:\s*\[([^\]]*)\]', content, re.DOTALL)
    if reports_match:
        # 在数组开头插入新报告
        old_reports = reports_match.group(1).strip()
        if old_reports:
            new_reports = f"{new_report},\n        {old_reports}"
        else:
            new_reports = new_report
        
        # 替换
        content = content[:reports_match.start(1)] + new_reports + content[reports_match.end(1):]
        
        with open(JS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已更新 js/main.js")
        return True
    else:
        print("❌ 未找到 reports 数组")
        return False

def update_reports_html(report_info):
    """更新 reports.html 中的报告列表"""
    with open(REPORTS_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 构建新的报告项HTML
    new_item = (
        '<div class="report-item" onclick="location.href=\'index.html\'">\n'
        '                    <div class="report-item-header">\n'
        '                        <h3>' + report_info['title'] + '</h3>\n'
        '                        <time>' + report_info['date'] + '</time>\n'
        '                    </div>\n'
        '                    <div class="report-item-meta">\n'
        '                        <span class="tag">情绪：' + report_info['sentiment'] + '</span>\n'
        '                        <span class="tag">仓位：' + report_info['position'] + '</span>\n'
        '                    </div>\n'
        '                </div>'
    )
    
    # 查找 reports-list div
    list_match = re.search(r'<div class="reports-list"[^>]*>(.*?)</div>', content, re.DOTALL)
    if list_match:
        # 在列表开头插入新报告
        old_list = list_match.group(1)
        # 移除旧的"即将上线"占位符
        if '即将上线' in old_list:
            old_list = re.sub(r'<div class="report-item"[^>]*style="opacity[^"]*"[^>]*>.*?</div>', '', old_list, flags=re.DOTALL)
        
        new_list = f"{new_item}\n                {old_list.strip()}"
        content = content[:list_match.start(1)] + new_list + content[list_match.end(1):]
        
        with open(REPORTS_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 已更新 reports.html")
        return True
    else:
        print("❌ 未找到 reports-list")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("🦞 龙虾复盘网站 - 自动更新脚本")
    print("=" * 50)
    
    # 检查源文件
    if not SRC_REPORT.exists():
        print(f"❌ 源文件不存在: {SRC_REPORT}")
        return False
    
    # 读取HTML内容
    with open(SRC_REPORT, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 提取报告信息
    report_info = get_report_info(html_content)
    print(f"\n📅 报告日期: {report_info['date']}")
    print(f"📝 报告标题: {report_info['title']}")
    print(f"😊 情绪周期: {report_info['sentiment']}")
    print(f"💰 仓位建议: {report_info['position']}")
    
    # 目标文件路径
    dst_report = REPORTS_DIR / f"{report_info['date']}.html"
    
    # 检查是否已存在
    if dst_report.exists():
        print(f"\n⚠️  报告已存在: {dst_report}")
        choice = input("是否覆盖？(y/n): ").strip().lower()
        if choice != 'y':
            print("❌ 已取消")
            return False
    
    # 复制报告文件
    shutil.copy(SRC_REPORT, dst_report)
    print(f"✅ 已复制报告到: {dst_report}")
    
    # 更新JS配置
    if not update_js_config(report_info):
        return False
    
    # 更新HTML报告列表
    if not update_reports_html(report_info):
        return False
    
    print("\n" + "=" * 50)
    print("✅ 网站更新完成！")
    print("=" * 50)
    print(f"\n📂 报告文件: {dst_report}")
    print(f"📊 配置文件: {JS_FILE}")
    print(f"📋 列表页面: {REPORTS_HTML}")
    print(f"\n💡 下一步:")
    print(f"   1. 本地测试: cd website && python -m http.server 8000")
    print(f"   2. 推送到GitHub: git add . && git commit -m 'Add report {report_info['date']}' && git push")
    
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
