---
layout: default
title: 君财有道-知识星球
description: 前阿里巴巴SEO专家 | 阅文集团SEO&GEO总顾问 | 21年全域流量实战经验，专注SEO优化、GEO优化与AI搜索流量增长。
keywords: [SEO优化, GEO优化, 全域流量, SEO专家, AI搜索优化, 知识星球]
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家 | 阅文集团SEO&GEO总顾问 | 21年全域SEO实战经验

📞 手机：13805186030（微信同号）

---

## 最新文章

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
    <div style="margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid #eee;">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p style="color:#666;">发布于：{{ post.date | date: "%Y年%m月%d日" }}</p>
      <div>{{ post.excerpt }}</div>
      <a href="{{ post.url | relative_url }}">阅读全文 →</a>
    </div>
  {% endfor %}
{% else %}
  <p>暂无文章，敬请期待...</p>
{% endif %}
