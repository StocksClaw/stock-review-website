# 🦞 龙虾复盘网站 - 快速启动指南

## ✅ 网站已创建完成！

### 📁 文件位置
```
C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website\
```

### 🚀 本地测试

**方法1：启动本地服务器**
```powershell
cd "C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website"
python -m http.server 8000
```
然后浏览器访问：http://localhost:8000

**方法2：直接打开（可能受CORS限制）**
```powershell
start "C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website\index.html"
```

---

## 📊 每日更新复盘报告

运行自动化脚本：
```powershell
cd "C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website"
python auto_update_report.py
```

**功能**：
1. 自动读取 `_last_report.html`
2. 复制到 `reports/YYYY-MM-DD.html`
3. 更新 `js/main.js` 配置
4. 更新 `reports.html` 列表

---

## 🌐 部署到GitHub Pages（公网访问）

### 步骤1：创建GitHub仓库

1. 访问 https://github.com/new
2. 仓库名：`stock-review-website`（或自定义）
3. 设为 Public
4. 点击 "Create repository"

### 步骤2：推送代码

```powershell
cd "C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website"

# 初始化Git仓库
git init

# 添加远程仓库（替换YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/stock-review-website.git

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: 龙虾复盘网站"

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 步骤3：启用GitHub Pages

1. 访问仓库设置：https://github.com/YOUR_USERNAME/stock-review-website/settings/pages
2. Source 选择：`main` 分支
3. 点击 Save
4. 等待1-2分钟部署完成

**公网访问地址**：
```
https://YOUR_USERNAME.github.io/stock-review-website/
```

---

## 💬 配置Gitalk评论系统

### 步骤1：创建GitHub App

1. 访问：https://github.com/settings/apps/new
2. 填写信息：
   - **App name**: `stock-review-gitalk`（或自定义）
   - **Homepage URL**: `https://YOUR_USERNAME.github.io/stock-review-website/`
   - **Callback URL**: `https://YOUR_USERNAME.github.io/stock-review-website/`
   - **Webhook**: 取消勾选
3. Permissions设置：
   - Repository permissions → Issues: Read & write
   - Repository permissions → Contents: Read-only
4. 点击 "Create GitHub App"
5. 记录 **Client ID**
6. 点击 "Generate a new client secret"，记录 **Client Secret**

### 步骤2：安装App到仓库

1. 访问：https://github.com/apps/YOUR_APP_NAME/installations/new
2. 选择你的仓库
3. 点击 Install

### 步骤3：修改配置文件

编辑 `js/main.js`：
```javascript
const CONFIG = {
    github: {
        owner: 'YOUR_GITHUB_USERNAME',  // 你的用户名
        repo: 'stock-review-website',    // 仓库名
        clientID: 'YOUR_CLIENT_ID',      // 填入Client ID
        clientSecret: 'YOUR_CLIENT_SECRET' // 填入Client Secret
    },
    ...
};
```

### 步骤4：提交更改

```powershell
git add js/main.js
git commit -m "Configure Gitalk"
git push
```

---

## 🎨 自定义主题颜色

编辑 `css/style.css`，修改第5行的渐变色：

**当前（紫色）**：
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

**蓝色主题**：
```css
background: linear-gradient(135deg, #2193b0 0%, #6dd5ed 100%);
```

**红色主题**：
```css
background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
```

---

## 🔧 常见问题

### Q1: 报告加载失败
**原因**：文件路径错误或CORS限制

**解决**：使用本地服务器测试（`python -m http.server 8000`）

### Q2: 评论区显示"Not Found"
**原因**：Gitalk配置错误或未安装App

**解决**：
1. 检查 `js/main.js` 配置
2. 确保GitHub App已安装到仓库
3. 确保仓库已启用Issues（Settings → Features → Issues）

### Q3: 样式不生效
**原因**：CSS文件未加载

**解决**：检查文件路径，确保 `css/style.css` 存在

---

## 📝 自动化集成（可选）

在复盘脚本 `publish_review_v30_full.py` 的最后添加：

```python
# 自动更新网站
import subprocess
subprocess.run([
    'python',
    r'C:\Users\ZhuanZ（无密码）\.qclaw\workspace-xiaochao\website\auto_update_report.py'
])
```

这样每次生成复盘报告后会自动更新网站。

---

## 📞 需要帮助？

查看完整文档：`README.md`

或联系：小超超 & 小默默
