# tangly1024.com

## 简介
由Flask驱动的博客系统
## 功能说明
[ ] 集成后台管理
[ ] SEO优化
[ ] 支持评论系统
[ ] 支持第三方云存储
[ ] 支持Markdown编辑

## 技术选型
- Flask
- Python
- Markdown renderer：Marko
- Markdown editor：Simple MDE
- Picture preview: Photoswipe
- 后台管理 待定

## 项目结构
- backend (flask后端项目：提供API接口，服务端渲染的页面)
    - common 通用模块工具类
    - modules 业务模块
       - blog 博客模块
        - views.py (页面跳转，接口)
       - auth 账号权限模块
        - views.py (页面跳转，接口)
    - static 静态资源
    - templates html模板
    
    
- frontend
    vue搭建的分离前端项目：无需SEO优化的页面，例如后台管理




## 待完成
    [] 响应式导航栏
        https://www.jianshu.com/p/abaf426f4bdc