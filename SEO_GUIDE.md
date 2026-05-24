# SEO优化指南

**龙虾复盘网站搜索引擎优化配置**

---

## 🎯 已完成的SEO优化

### 1. Meta标签优化
- **Title**: 每个页面都有独特的标题
- **Description**: 描述页面内容，搜索引擎显示
- **Keywords**: 关键词标签（虽然权重降低，但仍有用）
- **Author**: 作者信息

### 2. Open Graph标签（社交分享）
- 分享到微信、微博、Twitter时显示预览
- 包含标题、描述、图片预览

### 3. 技术文件
- **robots.txt**: 指导搜索引擎爬取规则
- **sitemap.xml**: 网站地图，帮助搜索引擎发现页面

---

## 📋 部署后需要做的SEO工作

### 1. 更新URL占位符（重要！）

部署后需要修改以下文件中的URL：

#### index.html
```html
<!-- 找到这行 -->
<meta property="og:url" content="https://YOUR_USERNAME.github.io/stock-review-website/">

<!-- 改为 -->
<meta property="og:url" content="https://你的用户名.github.io/stock-review-website/">
```

#### robots.txt
```
Sitemap: https://YOUR_USERNAME.github.io/stock-review-website/sitemap.xml
改为：https://你的用户名.github.io/stock-review-website/sitemap.xml
```

#### sitemap.xml
所有URL都要改为你的实际GitHub Pages地址。

---

### 2. 添加网站图标（Favicon）

创建 `favicon.png` 文件（推荐尺寸：32x32或64x64像素）

**方法A：使用在线工具**
- 访问 https://favicon.io/emoji-favicons/
- 选择🦞龙虾emoji
- 下载PNG文件
- 放到网站根目录

**方法B：自己设计**
- 用Photoshop/GIMP等工具设计
- 导出为PNG格式
- 命名为 `favicon.png`

---

### 3. 添加网站Logo（Open Graph图片）

创建 `logo.png` 文件（推荐尺寸：1200x630像素）

用于社交分享时显示的预览图片，可以是：
- 龙虾复盘的Logo设计
- 公众号封面图
- 或者任何代表网站的图片

---

### 4. 提交到搜索引擎

#### 百度搜索
1. 访问 https://ziyuan.baidu.com/
2. 注册账号
3. 添加网站并验证
4. 提交sitemap.xml
5. 等待收录（通常1-7天）

#### Google搜索
1. 访问 https://search.google.com/search-console
2. 添加网站属性
3. 验证所有权（推荐使用HTML文件验证）
4. 提交sitemap.xml
5. 等待收录（通常几小时到几天）

---

### 5. 添加网站统计

#### 百度统计
1. 访问 https://tongji.baidu.com/
2. 注册账号
3. 创建站点
4. 获取统计代码
5. 在index.html的`</body>`前添加：
```html
<!-- 百度统计代码 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?你的统计ID";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
```

#### Google Analytics
1. 访问 https://analytics.google.com/
2. 创建账号和属性
3. 获取跟踪ID
4. 在index.html的`<head>`中添加：
```html
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=你的跟踪ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '你的跟踪ID');
</script>
```

---

## 🔧 SEO自动化脚本

创建一个脚本自动更新sitemap.xml：

```python
#!/usr/bin/env python3
# update_sitemap.py - 自动更新sitemap.xml

from pathlib import Path
from datetime import datetime

# 网站目录
WEBSITE_DIR = Path('C:/Users/ZhuanZ（无密码）/.qclaw/workspace-xiaochao/website')
REPORTS_DIR = WEBSITE_DIR / 'reports'

# 获取所有报告
reports = sorted(REPORTS_DIR.glob('*.html'), reverse=True)

# 生成sitemap
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://YOUR_USERNAME.github.io/stock-review-website/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    
    <url>
        <loc>https://YOUR_USERNAME.github.io/stock-review-website/reports.html</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    
    <url>
        <loc>https://YOUR_USERNAME.github.io/stock-review-website/about.html</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
'''.format(today=datetime.now().strftime('%Y-%m-%d'))

# 添加报告URL
for report in reports:
    date = report.stem  # 2026-05-24
    sitemap += f'''
    <url>
        <loc>https://YOUR_USERNAME.github.io/stock-review-website/reports/{date}.html</loc>
        <lastmod>{date}</lastmod>
        <changefreq>yearly</changefreq>
        <priority>0.7</priority>
    </url>
'''

sitemap += '</urlset>'

# 写入文件
with open(WEBSITE_DIR / 'sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

print('✅ sitemap.xml已更新')
```

---

## 📊 SEO检查清单

部署后检查以下项目：

- [ ] 所有URL占位符已替换
- [ ] favicon.png已创建
- [ ] logo.png已创建（可选）
- [ ] robots.txt已更新
- [ ] sitemap.xml已更新
- [ ] 提交到百度搜索（可选）
- [ ] 提交到Google搜索（可选）
- [ ] 添加网站统计（可选）

---

## 🎯 SEO最佳实践

### 内容质量
- 每日更新复盘报告
- 保持内容原创性
- 提供有价值的信息

### 网站速度
- 使用GitHub Pages（速度快）
- 图片压缩优化
- CSS/JS文件已优化

### 移动友好
- 响应式设计已实现
- 手机和电脑都能良好显示
- 符合Google移动优先索引

### 内部链接
- 页面之间相互链接
- 报告之间可以跳转
- 导航清晰明了

---

**SEO优化完成日期**: 2026-05-24
**维护者**: 小默默