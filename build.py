import os
import markdown
import frontmatter
from datetime import datetime

# 配置
POSTS_PER_PAGE = 10
SITE_TITLE = "君财有道-知识星球"
SITE_DESCRIPTION = "前阿里巴巴SEO专家 | 阅文集团SEO&GEO总顾问 | 21年全域流量实战经验"
CONTACT = "📞 手机：13805186030（微信同号）"

print("🚀 开始构建博客...")

# 读取模板
with open("templates/index.html", "r", encoding="utf-8") as f:
    index_template = f.read()
with open("templates/post.html", "r", encoding="utf-8") as f:
    post_template = f.read()

# 创建输出目录
os.makedirs("public", exist_ok=True)
os.makedirs("public/posts", exist_ok=True)

# 读取所有文章
posts = []
for filename in os.listdir("_posts"):
    if filename.endswith(".md"):
        try:
            print(f"📄 处理文章：{filename}")
            post = frontmatter.load(f"_posts/{filename}")
            
            date_str = filename[:10]
            post_date = datetime.strptime(date_str, "%Y-%m-%d")
            url = f"/posts/{filename[:-3]}.html"
            
            if "title" not in post:
                post["title"] = filename[11:-3]
            
            posts.append({
                "title": post["title"],
                "date": post_date,
                "date_str": post_date.strftime("%Y年%m月%d日"),
                "url": url,
                "content": markdown.markdown(post.content, extensions=["tables", "fenced_code"])
            })
        except Exception as e:
            print(f"⚠️  跳过文章 {filename}：{e}")
            continue

print(f"✅ 共找到 {len(posts)} 篇文章")
posts.sort(key=lambda x: x["date"], reverse=True)

# 生成文章页面
for post in posts:
    try:
        html = post_template.replace("{site_title}", SITE_TITLE)
        html = html.replace("{title}", post["title"])
        html = html.replace("{date}", post["date_str"])
        html = html.replace("{content}", post["content"])
        
        with open(f"public{post['url']}", "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(f"⚠️  生成文章失败 {post['title']}：{e}")
        continue

# 生成分页
total_pages = (len(posts) + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE
print(f"📑 共生成 {total_pages} 个分页")

for page_num in range(1, total_pages + 1):
    start = (page_num - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    page_posts = posts[start:end]
    
    # 生成文章列表
    posts_html = ""
    for post in page_posts:
        excerpt = post['content'].replace("<p>", "").replace("</p>", "")[:200] + "..."
        posts_html += f"""
        <div class="post-item">
            <h4><a href="{post['url']}">{post['title']}</a></h4>
            <div class="post-date">{post['date_str']}</div>
            <div class="post-excerpt">{excerpt}</div>
            <a href="{post['url']}" class="read-more">阅读全文 →</a>
        </div>
        """
    
    # 生成分页导航
    pagination_html = ""
    if total_pages > 1:
        pagination_html = '<div style="text-align: center; margin-top: 40px;">'
        if page_num > 1:
            prev_url = "/" if page_num == 2 else f"/page{page_num-1}.html"
            pagination_html += f'<a href="{prev_url}" style="margin: 0 10px; padding: 8px 16px; background: #2385bb; color: white; text-decoration: none; border-radius: 4px;">上一页</a>'
        pagination_html += f'<span style="margin: 0 15px; font-weight: bold;">第 {page_num} 页 / 共 {total_pages} 页</span>'
        if page_num < total_pages:
            pagination_html += f'<a href="/page{page_num+1}.html" style="margin: 0 10px; padding: 8px 16px; background: #2385bb; color: white; text-decoration: none; border-radius: 4px;">下一页</a>'
        pagination_html += '</div>'
    
    # 生成首页
    html = index_template.replace("{site_title}", SITE_TITLE)
    html = html.replace("{site_description}", SITE_DESCRIPTION)
    html = html.replace("{contact}", CONTACT)
    html = html.replace("{posts}", posts_html)
    html = html.replace("{pagination}", pagination_html)
    
    if page_num == 1:
        with open("public/index.html", "w", encoding="utf-8") as f:
            f.write(html)
    else:
        with open(f"public/page{page_num}.html", "w", encoding="utf-8") as f:
            f.write(html)

print("\n🎉 博客构建完成！")
