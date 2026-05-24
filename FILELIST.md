# 🦞 龙虾复盘网站 - 文件清单

**最后更新**: 2026-05-24 18:25
**版本**: v1.0

---

## 📂 网站文件结构

```
website/
├── 📄 index.html              # 首页（展示最新复盘）
├── 📄 reports.html            # 历史归档页
├── 📄 about.html              # 关于页面
│
├── 📁 css/
│   └── 📄 style.css          # 样式文件（响应式设计）
│
├── 📁 js/
│   └── 📄 main.js            # 核心脚本（报告加载+Gitalk）
│
├── 📁 reports/               # 复盘报告目录
│   └── 📄 2026-05-24.html    # 今日报告
│
├── 🛠️ tools.py               # 工具集入口（交互式菜单）
├── 🛠️ auto_update_report.py  # 自动更新报告
├── 🛠️ deploy_to_github.py    # GitHub部署助手
├── 🛠️ check_config.py        # Gitalk配置检查
├── 📄 .gitignore             # Git忽略规则
│
├── 📖 README.md              # 完整配置文档
├── 📖 QUICKSTART.md          # 快速启动指南
├── 📖 FILELIST.md            # 本文件
│
└── 🖱️ 启动工具.bat           # 双击启动工具集（Windows）
```

---

## 📊 文件大小统计

| 文件类型 | 数量 | 总大小 |
|---------|------|--------|
| HTML页面 | 3个 | 8.5 KB |
| 样式表 | 1个 | 3.1 KB |
| JavaScript | 1个 | 3.2 KB |
| 复盘报告 | 1个 | 51.6 KB |
| Python工具 | 4个 | 20.9 KB |
| 文档 | 3个 | 13.2 KB |
| **总计** | **13个** | **~100 KB** |

---

## 🎯 核心功能清单

### ✅ 已完成功能
- [x] 首页展示最新复盘报告
- [x] 历史报告归档页面
- [x] 关于页面（项目介绍）
- [x] 响应式设计（手机/电脑）
- [x] 渐变主题样式
- [x] 自动化更新脚本
- [x] GitHub部署助手
- [x] Gitalk配置检查工具
- [x] 交互式工具集菜单
- [x] 完整使用文档

### ⏳ 待配置功能（需虎哥操作）
- [ ] Gitalk评论系统（需GitHub App）
- [ ] GitHub Pages部署（需创建仓库）
- [ ] 自定义域名（可选）

---

## 🚀 快速开始

### 方法1：双击启动（推荐新手）
```
双击运行：启动工具.bat
```

### 方法2：命令行启动
```powershell
cd "C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website"
python tools.py
```

### 方法3：直接运行单个工具
```powershell
# 更新报告
python auto_update_report.py

# 部署到GitHub
python deploy_to_github.py

# 检查配置
python check_config.py

# 启动本地服务器
python -m http.server 8000
```

---

## 📋 日常使用流程

### 每日更新复盘报告
```
1. 运行 publish_review_v30_full.py 生成报告
2. 运行 auto_update_report.py 更新网站
3. 推送到GitHub（如已部署）
```

### 首次部署到公网
```
1. 创建GitHub仓库
2. 运行 deploy_to_github.py
3. 启用GitHub Pages
4. 创建GitHub App配置Gitalk
5. 运行 check_config.py 验证配置
```

---

## 🔧 工具说明

### tools.py - 工具集入口
交互式菜单，提供所有工具的统一入口。

### auto_update_report.py - 自动更新报告
- 读取 `_last_report.html`
- 复制到 `reports/YYYY-MM-DD.html`
- 更新 `js/main.js` 和 `reports.html`
- 提取报告信息（日期、标题、情绪、仓位）

### deploy_to_github.py - GitHub部署助手
- 检查Git环境
- 初始化Git仓库
- 添加远程仓库
- 提交并推送代码
- 显示部署成功提示

### check_config.py - Gitalk配置检查
- 验证 `js/main.js` 配置
- 检查必需字段是否填写
- 显示GitHub App创建指南
- 提供修复建议

---

## 🌐 网站访问地址

### 本地测试
```
http://localhost:8000
```

### GitHub Pages（部署后）
```
https://YOUR_USERNAME.github.io/stock-review-website/
```

---

## 📝 配置文件位置

### Gitalk评论配置
```
js/main.js → CONFIG.github 对象
```

### 样式主题配置
```
css/style.css → 第5行渐变色
```

### 报告列表配置
```
js/main.js → CONFIG.reports 数组
```

---

## ⚠️ 注意事项

1. **Gitalk配置**：必须创建GitHub App并安装到仓库
2. **GitHub Pages**：部署后需在仓库设置中启用
3. **报告更新**：每次生成新报告后需运行更新脚本
4. **Git推送**：修改配置后需重新提交到GitHub

---

## 🆘 常见问题

### Q: 评论区显示"Not Found"
A: 检查Gitalk配置，运行 `check_config.py` 验证

### Q: 报告加载失败
A: 使用本地服务器测试，不要直接打开HTML文件

### Q: 推送到GitHub失败
A: 检查Git安装和GitHub权限，使用Personal Access Token

### Q: 样式不生效
A: 清除浏览器缓存，检查CSS文件路径

---

**文档维护**: 小超超 & 小默默
**联系方式**: 微信公众号「龙虾复盘」
