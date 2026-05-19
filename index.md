---
layout: default
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家 | 阅文集团SEO&GEO总顾问 | 21年全域SEO实战经验

专注AI+SEO+GEO全域获客，帮助企业建立持续、稳定、低成本的自然流量获客能力。

📞 手机：13805186030（微信同号）

---

## 最新文章

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
    <div style="margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid #eee;">
      <h2 style="margin: 0 0 10px 0; font-size: 22px;">
        <a href="{{ post.url | relative_url }}" style="color:#2385bb; text-decoration:none;">{{ post.title }}</a>
      </h2>
      <p style="color:#999; font-size:14px; margin:0 0 10px 0;">发布日期：{{ post.date | date: "%Y年%m月%d日" }}</p>
      <p style="color:#444; line-height:1.6;">
        {% if post.excerpt %}
          {{ post.excerpt | strip_html | truncate: 200 }}
        {% else %}
          {{ post.content | strip_html | truncate: 200 }}
        {% endif %}
      </p>
      <a href="{{ post.url | relative_url }}" style="color:#2385bb; text-decoration:none;">阅读全文 →</a>
    </div>
  {% endfor %}
{% else %}
  <p>暂无文章，敬请期待...</p>
{% endif %}
