---
layout: home
title: 君财有道-知识星球
---

# 欢迎来到君财有道-知识星球

前阿里巴巴SEO专家｜阅文集团SEO&GEO总顾问｜21年全域SEO实战经验

专注AI+SEO+GEO全域获客，帮助企业建立持续、稳定、低成本的自然流量获客能力。

{{ site.author.bio }}

---

## 最新文章

{% for post in paginator.posts %}
### [{{ post.title }}]({{ post.url }})
**发布日期：{{ post.date | date: "%Y年%m月%d日" }}**

{{ post.excerpt }}

[阅读全文 →]({{ post.url }})

---
{% endfor %}

<!-- 分页导航 -->
{% if paginator.total_pages > 1 %}
<div style="text-align: center; margin-top: 40px; padding: 20px; border-top: 1px solid #eee;">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" style="margin: 0 10px; padding: 8px 16px; background: #2385bb; color: white; text-decoration: none; border-radius: 4px;">上一页</a>
  {% endif %}

  <span style="margin: 0 15px; font-weight: bold;">第 {{ paginator.page }} 页 / 共 {{ paginator.total_pages }} 页</span>

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" style="margin: 0 10px; padding: 8px 16px; background: #2385bb; color: white; text-decoration: none; border-radius: 4px;">下一页</a>
  {% endif %}
</div>
{% endif %}
