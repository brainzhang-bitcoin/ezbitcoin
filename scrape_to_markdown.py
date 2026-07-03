import os
import time
import random
import requests
from sitemap_parser import extract_urls
from content_transformer import transform_html_to_markdown

def main():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    
    # 1. Fetch and Parse Sitemap
    print("Fetching Sitemap...")
    try:
        sitemap_resp = session.get("https://learnmeabitcoin.com/sitemap", timeout=15)
        sitemap_resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return
        
    urls = extract_urls(sitemap_resp.text)
    print(f"Found {len(urls)} matching urls.")
    
    # Ensure local directory structure
    os.makedirs("docs/images", exist_ok=True)
    
    # 2. Scrape each URL
    for i, url in enumerate(urls, 1):
        # Determine output file path
        path_suffix = url.split("learnmeabitcoin.com/")[-1]
        md_file_path = f"docs/{path_suffix.strip('/')}.md"
        
        print(f"[{i}/{len(urls)}] Processing {url} -> {md_file_path}")
        
        # Check if already processed
        if os.path.exists(md_file_path):
            print(f"  Skipped (already exists)")
            continue
            
        # Get content
        try:
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"  Failed to fetch: {e}")
            continue
            
        os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
        
        # Transform content
        md_content, images = transform_html_to_markdown(resp.text, md_file_path)
        
        # Download images
        for img in images:
            img_dest = os.path.join("docs/images", img["local_filename"])
            if os.path.exists(img_dest):
                continue
            
            # Rate limiting sleep before fetching image
            time.sleep(random.uniform(0.1, 0.3))
            try:
                img_resp = session.get(img["src_url"], timeout=15)
                img_resp.raise_for_status()
                with open(img_dest, "wb") as f:
                    f.write(img_resp.content)
                print(f"    Downloaded image: {img['local_filename']}")
            except Exception as e:
                print(f"    Failed to download image {img['src_url']}: {e}")
                
        # Write Markdown
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        # Sleep to be polite
        time.sleep(random.uniform(0.2, 0.5))

if __name__ == "__main__":
    main()
