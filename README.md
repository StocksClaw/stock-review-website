# 🦞 龙虾复盘网站

A股超短线复盘报告发布平台 - 静态网站Demo

## 📁 项目结构

```
website/
├── index.html          # 首页（展示最新复盘）
├── reports.html        # 历史归档页
├── about.html          # 关于页面
├── css/
│   └── style.css      # 样式文件
├── js/
│   └── main.js        # 核心JavaScript
├── reports/           # 复盘报告HTML文件
│   ├── 2026-05-22.html
│   └── ...
└── README.md          # 本文件
```

## 🚀 快速开始

### 1. 本地测试

直接用浏览器打开 `index.html` 即可。

**注意**：由于浏览器的CORS策略，直接打开HTML文件可能无法加载报告。建议使用本地服务器：

```bash
# Python 3
cd website
python -m http.server 8000

# 然后访问 http://localhost:8000
```

### 2. 配置Gitalk评论系统

Gitalk基于GitHub Issues，需要以下配置：

#### 步骤1 - 创建GitHub仓库

1. 在GitHub创建新仓库（如 `stock-review-website`）
2. 将整个 `website/` 目录推送到仓库
3. 在仓库设置中启用GitHub Pages

#### 步骤2 - 创建GitHub App

1. 访问 https://github.com/settings/apps
2. 点击"New GitHub App"
3. 填写信息：
   - **App name**: `stock-review-gitalk`
   - **Homepage URL**: `https://你的用户名.github.io/stock-review-website/`
   - **Callback URL**: `https://你的用户名.github.io/stock-review-website/`
   - **Webhook**: 取消勾选（不需要）
   - **Permissions**:
     - Repository permissions → Issues: Read & write
     - Repository permissions → Contents: Read-only
   - **Where can this app be installed?**: Choose "Any account"
4. 点击"Create GitHub App"
5. 记录 `Client ID` 和生成 `Client Secret`

#### 步骤3 - 修改配置文件

编辑 `js/main.js`，替换以下占位符：

```javascript
const CONFIG = {
    github: {
        owner: 'YOUR_GITHUB_USERNAME',  // 你的GitHub用户名
        repo: 'stock-review-website',    // 你的仓库名
        clientID: 'YOUR_CLIENT_ID',      // 从GitHub App获取
        clientSecret: 'YOUR_CLIENT_SECRET' // 从GitHub App获取
    },
    ...
};
```

### 3. 部署到GitHub Pages

```bash
# 1. 克隆你的仓库
git clone https://github.com/你的用户名/stock-review-website.git
cd stock-review-website

# 2. 将website目录内容复制到仓库
cp -r path/to/website/* .

# 3. 提交并推送
git add .
git commit -m "Initial commit"
git push origin main

# 4. 启用GitHub Pages
# 访问仓库 → Settings → Pages → Source选择main分支 → Save
```

访问 `https://你的用户名.github.io/stock-review-website/` 查看网站。

## 📊 添加新复盘报告

### 方法1：手动添加

1. 将 `_last_report.html` 重命名为 `YYYY-MM-DD.html`（如 `2026-05-22.html`）
2. 复制到 `website/reports/` 目录
3. 编辑 `js/main.js`，在 `CONFIG.reports` 数组中添加新报告信息：

```javascript
reports: [
    {
        date: '2026-05-22',
        title: '龙虾复盘 | 2026.05.22 周五 主升',
        file: 'reports/2026-05-22.html',
        sentiment: '主升',
        position: '2~3成轻仓'
    },
    // 添加更多...
]
```

4. 编辑 `reports.html`，添加新的报告链接

### 方法2：自动化脚本（推荐）

创建一个Python脚本自动完成上述步骤：

```python
# auto_update_website.py
import shutil
from datetime import datetime

# 源文件
src = r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\_last_report.html'

# 目标文件（用日期命名）
today = datetime.now().strftime('%Y-%m-%d')
dst = fr'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website\reports\{today}.html'

# 复制文件
shutil.copy(src, dst)
print(f'报告已复制到: {dst}')

# TODO: 自动更新 js/main.js 和 reports.html
```

## 🎨 自定义样式

编辑 `css/style.css` 修改颜色、字体、布局等。

**主题色**（当前为紫色渐变）：
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

修改为其他颜色，如蓝色：
```css
background: linear-gradient(135deg, #2193b0 0%, #6dd5ed 100%);
```

## 🔧 故障排除

### 问题1：评论区显示"Not Found"

**原因**：Gitalk配置错误 或 GitHub App未正确安装

**解决**：
1. 检查 `js/main.js` 中的配置是否正确
2. 确保GitHub App已安装到仓库（访问 https://github.com/apps/你的App名称/installations/new）
3. 确保仓库已启用Issues功能

### 问题2：报告加载失败

**原因**：文件路径错误或CORS限制

**解决**：
1. 检查 `CONFIG.reports[x].file` 路径是否正确
2. 使用本地服务器测试（不要用 `file://` 协议直接打开）

### 问题3：样式错乱

**原因**：CSS文件未正确加载

**解决**：
1. 检查浏览器控制台是否有404错误
2. 确保 `style.css` 路径正确

## 📝 待优化功能

- [ ] 自动生成历史报告列表（从 `reports/` 目录读取）
- [ ] 搜索功能（按日期/关键词搜索报告）
- [ ] RSS订阅（自动推送新报告）
- [ ] PWA支持（可安装到手机桌面）
- [ ] 暗黑模式
- [ ] 多语言支持

## 📞 联系方式

- 微信公众号：龙虾复盘
- GitHub：https://github.com/你的用户名/stock-review-website

---

**Made with ❤️ by 小超超 & 小默默**
