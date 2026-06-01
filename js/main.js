// 配置信息
const CONFIG = {
    // GitHub仓库信息（用于Gitalk评论）
    // 配置步骤: https://github.com/settings/developers → New OAuth App
    //   Application name: 龙虾复盘
    //   Homepage URL: https://StocksClaw.github.io/stock-review-website/
    //   Callback URL: https://StocksClaw.github.io/stock-review-website/
    // 创建后填入 clientID 和 clientSecret
    github: {
        owner: 'StocksClaw',
        repo: 'stock-review-website',
        clientID: '',      // 待虎哥配置
        clientSecret: ''   // 待虎哥配置
    },
    // 报告文件列表（手动维护或自动生成）
    reports: [{
            date: '2026-06-01',
            title: '龙虾复盘 | 2026.06.01 周一 退潮',
            file: 'reports/2026-06-01.html',
            sentiment: '退潮',
            position: '空仓'
        },
        {
            date: '2026-05-29',
            title: '龙虾复盘 | 2026.05.29 周五 分歧',
            file: 'reports/2026-05-29.html',
            sentiment: '分歧',
            position: '1~2成试错'
        },
        {
            date: '2026-05-28',
            title: '龙虾复盘 | 2026.05.28 周四 试盘',
            file: 'reports/2026-05-28.html',
            sentiment: '试盘',
            position: '2~3成试错'
        },
        {
            date: '2026-05-26',
            title: '龙虾复盘 | 2026.05.26 周二 退潮',
            file: 'reports/2026-05-26.html',
            sentiment: '退潮',
            position: '清仓'
        },
        {
            date: '2026-05-25',
            title: '龙虾复盘 | 2026.05.25 周一 弱修复',
            file: 'reports/2026-05-25.html',
            sentiment: '弱修复',
            position: '1~2成试错'
        },
        {
            date: '2026-05-22',
            title: '龙虾复盘 | 2026.05.22 周五 主升',
            file: 'reports/2026-05-24.html',
            sentiment: '主升',
            position: '3~5成'
        }
    ]
};

// 加载最新报告
async function loadLatestReport() {
    const latest = CONFIG.reports[0];
    
    // 更新页面信息
    document.getElementById('report-title').textContent = latest.title;
    document.getElementById('report-date').textContent = latest.date;
    document.getElementById('sentiment-tag').textContent = '情绪：' + latest.sentiment;
    document.getElementById('position-tag').textContent = '仓位：' + latest.position;
    document.getElementById('update-time').textContent = new Date().toLocaleString('zh-CN');
    
    // 加载报告内容
    try {
        const response = await fetch(latest.file);
        if (response.ok) {
            const html = await response.text();
            document.getElementById('report-content').innerHTML = html;
            document.getElementById('report-content').classList.remove('loading');
            
            // 初始化评论系统
            initGitalk(latest.date);
        } else {
            throw new Error('报告文件不存在 (' + response.status + ')');
        }
    } catch (error) {
        document.getElementById('report-content').innerHTML =
            '<div style="text-align:center; padding:50px; color:#999;">' +
            '<h3>📊 报告加载失败</h3>' +
            '<p>原因：' + error.message + '</p>' +
            '<p>请稍后刷新页面重试</p>' +
            '</div>';
    }
}

// 初始化Gitalk评论系统
function initGitalk(reportId) {
    // 评论系统未配置时跳过
    if (!CONFIG.github.clientID || !CONFIG.github.clientSecret) {
        document.getElementById('gitalk-container').innerHTML =
            '<p style="text-align:center;color:#999;padding:20px;">💬 评论系统配置中，敬请期待...</p>';
        return;
    }
    try {
        var gitalk = new Gitalk({
            clientID: CONFIG.github.clientID,
            clientSecret: CONFIG.github.clientSecret,
            repo: CONFIG.github.repo,
            owner: CONFIG.github.owner,
            admin: [CONFIG.github.owner],
            id: reportId,
            distractionFreeMode: false,
            title: '复盘报告 ' + reportId,
            body: '自动创建于 ' + new Date().toLocaleString('zh-CN'),
            labels: ['复盘报告', reportId]
        });
        gitalk.render('gitalk-container');
    } catch (error) {
        console.error('Gitalk初始化失败:', error);
        document.getElementById('gitalk-container').innerHTML =
            '<p style="text-align:center;color:#999;padding:20px;">💬 评论系统配置中，敬请期待...</p>';
    }
}

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    loadLatestReport();
});
