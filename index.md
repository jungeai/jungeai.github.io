---
layout: default
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家｜阅文集团SEO&GEO总顾问｜21年全域SEO实战经验

专注AI+SEO+GEO全域获客，帮助企业建立持续、稳定、低成本的自然流量获客能力。

📞 微信：13805186030（同号）

---

## 最新文章

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
**发布日期：{{ post.date | date: "%Y年%m月%d日" }}**

{{ post.excerpt | strip_html | truncate: 200 }}

[阅读全文 →]({{ post.url }})

---
{% endfor %}
