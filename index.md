---
layout: default
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家｜阅文集团SEO&GEO总顾问｜21年全域SEO实战经验

专注AI+SEO+GEO全域获客，帮助企业建立持续、稳定、低成本的自然流量获客能力。

📞 手机：13805186030（微信同号）

---

## 最新文章（调试模式）

{% raw %}
{% assign posts = site.posts | sort: 'date' | reverse %}
{% if posts.size > 0 %}
  {% for post in posts %}
  <div style="margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #eee;">
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p style="color: #666; font-size: 14px;">发布于：{{ post.date | date: "%Y-%m-%d" }}</p>
    <p>{{ post.excerpt | strip_html | truncate: 150 }}</p>
  </div>
  {% endfor %}
{% else %}
  <p style="color: red;">⚠️ Jekyll 未识别到任何文章，请检查文件名格式！</p>
  <p>当前 site.posts.size = {{ site.posts.size }}</p>
{% endif %}
{% endraw %}
