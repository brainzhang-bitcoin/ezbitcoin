from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import MarkdownConverter
from blog_router import get_local_path_for_blog_url, get_relative_link
from image_manager import sanitize_filename, get_relative_img_path

class BlogConverter(MarkdownConverter):
    pass

def transform_blog_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(html_content, "lxml")
    content_area = soup.find("article") or soup.find(class_="entry-content")
    if not content_area:
        content_area = soup.find("body") or soup

    # Decompose sharing, disqus, and meta elements
    for tag in content_area.find_all(class_=["sharing", "meta"]):
        tag.decompose()
    disqus = content_area.find(id="disqus_thread")
    if disqus:
        disqus.decompose()

    # Process images and rewrite sources
    images_to_download = []
    base_url = "https://brainz.fun/"

    for img in content_area.find_all("img"):
        src = img.get("src")
        if src:
            absolute_img_url = urljoin(base_url, src)
            # Prefix filename with blog_
            orig_filename = sanitize_filename(absolute_img_url)
            local_filename = f"blog_{orig_filename}"
            relative_path = get_relative_img_path(md_filepath, local_filename)
            
            img["src"] = relative_path
            images_to_download.append({
                "src_url": absolute_img_url,
                "local_filename": local_filename
            })

    # Rewrite internal links
    for a in content_area.find_all("a", href=True):
        href = a["href"]
        parsed = urlparse(href)
        # Check if internal blog link
        if "/blog/" in href:
            local_target = get_local_path_for_blog_url(href)
            if local_target:
                rel_href = get_relative_link(md_filepath, local_target)
                if parsed.fragment:
                    rel_href += f"#{parsed.fragment}"
                a["href"] = rel_href

    converter = BlogConverter(heading_style="ATX")
    markdown_content = converter.convert(str(content_area))
    return markdown_content.strip(), images_to_download
