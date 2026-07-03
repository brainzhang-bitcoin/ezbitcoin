from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse
from image_manager import sanitize_filename, get_relative_img_path

def transform_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(html_content, "lxml")
    
    # Locate article body. learnmeabitcoin content usually sits in <main> or class "content" or id "content"
    content_area = soup.find("article") or soup.find(id="content") or soup.find(class_="content")
    if not content_area:
        content_area = soup.find("body") or soup
        
    # Strip unnecessary elements (e.g., pagination buttons, navigation, scripts)
    for tag in content_area.find_all(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
        
    # Process images and rewrite sources
    images_to_download = []
    base_url = "https://learnmeabitcoin.com/"
    
    for img in content_area.find_all("img"):
        src = img.get("src")
        if src:
            absolute_img_url = urljoin(base_url, src)
            local_filename = sanitize_filename(absolute_img_url)
            relative_path = get_relative_img_path(md_filepath, local_filename)
            
            img["src"] = relative_path
            images_to_download.append({
                "src_url": absolute_img_url,
                "local_filename": local_filename
            })
            
    # Rewrite target links (e.g. /beginners/wallets/ -> /docs/beginners/wallets.md)
    for a in content_area.find_all("a", href=True):
        href = a["href"]
        parsed = urlparse(href)
        # Check if it points to the target directories
        path = parsed.path.strip("/")
        if path.startswith("beginners") or path.startswith("technical"):
            new_href = f"/docs/{path}.md"
            if parsed.fragment:
                new_href += f"#{parsed.fragment}"
            a["href"] = new_href

    # Convert cleaned HTML to markdown
    markdown_content = md(str(content_area), heading_style="ATX")
    return markdown_content.strip(), images_to_download

