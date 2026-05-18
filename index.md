---
layout: home
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家｜阅文集团SEO&GEO总顾问｜21年全域SEO实战经验

专注AI+SEO+GEO全域获客，帮助企业建立持续、稳定、低成本的自然流量获客能力。

📞 手机：13805186030（微信同号）

---

## 最新文章

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
  <div style="margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #eee;">
    <h3 style="margin:0 0 0.5rem 0;">
      <a href="{{ post.url }}" style="color:#2385bb; text-decoration:none;">{{ post.title }}</a>
    </h3>
    <p style="color:#666; font-size:0.9rem; margin:0 0 0.5rem 0;">发布于：{{ post.date | date: "%Y年%m月%d日" }}</p>
    <p style="color:#444; margin:0 0 0.5rem 0;">{{ post.excerpt | strip_html | truncate: 200 }}</p>
    <a href="{{ post.url }}" style="color:#2385bb; text-decoration:none; font-size:0.9rem;">阅读全文 →</a>
  </div>
  {% endfor %}
{% else %}
  <p>暂无文章，敬请期待...</p>
{% endif %}
