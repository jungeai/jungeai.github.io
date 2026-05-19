---
layout: default
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家 | 阅文集团SEO&GEO总顾问 | 21年全域流量实战经验

📞 手机：13805186030（微信同号）

---

## 最新文章

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
发布于：{{ post.date | date: "%Y年%m月%d日" }}

{{ post.excerpt | strip_html | truncate: 150 }}

[阅读全文 →]({{ post.url }})
  {% endfor %}
{% else %}
  暂无文章，敬请期待...
{% endif %}
