import os
import sys
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from blog_router import get_local_path_for_blog_url
from blog_transformer import transform_blog_html_to_markdown

def scrape_blog() -> bool:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    
    category_url = "https://brainz.fun/blog/categories/blockchain/"
    print(f"Fetching category page: {category_url}")
    try:
        resp = session.get(category_url, timeout=15)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
    except Exception as e:
        print(f"Error fetching category page: {e}")
        return False
        
    soup = BeautifulSoup(resp.text, "lxml")
    article_links = []
    
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/blog/" in href:
            absolute_url = urljoin(category_url, href)
            # Filter by matching URL slugs
            local_target = get_local_path_for_blog_url(absolute_url)
            if local_target and absolute_url not in article_links:
                article_links.append(absolute_url)
                
    print(f"Found {len(article_links)} matching articles to import.")
    os.makedirs("docs/images", exist_ok=True)
    
    failed_articles = 0
    
    for i, url in enumerate(article_links, 1):
        md_file_path = get_local_path_for_blog_url(url)
        print(f"[{i}/{len(article_links)}] Processing {url} -> {md_file_path}")
        
        # Rate limit sleep
        time.sleep(random.uniform(0.2, 0.5))
        
        try:
            art_resp = session.get(url, timeout=15)
            art_resp.raise_for_status()
            art_resp.encoding = 'utf-8'
        except Exception as e:
            print(f"  Failed to fetch: {e}")
            failed_articles += 1
            continue
            
        os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
        md_content, images = transform_blog_html_to_markdown(art_resp.text, md_file_path)
        
        # Download images
        for img in images:
            img_dest = os.path.join("docs/images", img["local_filename"])
            if os.path.exists(img_dest):
                continue
                
            time.sleep(random.uniform(0.1, 0.3))
            try:
                img_resp = session.get(img["src_url"], timeout=15)
                img_resp.raise_for_status()
                with open(img_dest, "wb") as f:
                    f.write(img_resp.content)
                print(f"    Downloaded image: {img['local_filename']}")
            except Exception as e:
                print(f"    Failed to download image {img['src_url']}: {e}")
                
        # Write Markdown file
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
    if failed_articles > 0:
        print(f"Blog import completed with {failed_articles} failures.")
        return False
        
    print("Blog import completed successfully!")
    return True

if __name__ == "__main__":
    success = scrape_blog()
    if not success:
        sys.exit(1)
