from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from urllib.parse import urljoin, urlparse
from image_manager import sanitize_filename, get_relative_img_path

class CustomConverter(MarkdownConverter):
    def convert_img(self, el, text, *args, **kwargs):
        src = el.get('src', '')
        alt = el.get('alt', '')
        style = el.get('style', '')
        width = el.get('width', '')
        height = el.get('height', '')
        
        # Keep as HTML img tag if it's an SVG, has 'icon' in the URL, or has size attributes
        is_icon = src.endswith('.svg') or 'icon' in src.lower() or 'logo' in src.lower() or style or width or height
        
        if is_icon:
            attrs = []
            if src:
                attrs.append(f'src="{src}"')
            if alt:
                attrs.append(f'alt="{alt}"')
            if width:
                attrs.append(f'width="{width}"')
            if height:
                attrs.append(f'height="{height}"')
            if style:
                attrs.append(f'style="{style}"')
            else:
                # Default style for icons without explicit styling
                if src.endswith('.svg') or 'icon' in src.lower():
                    attrs.append('style="width: 24px; height: 24px;"')
            return f'<img {" ".join(attrs)} />'
            
        return super().convert_img(el, text, *args, **kwargs)



def transform_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(html_content, "lxml")
    
    # Locate article body. learnmeabitcoin content usually sits in <main> or class "content" or id "content"
    content_area = soup.find("article") or soup.find(id="content") or soup.find(class_="content")
    if not content_area:
        content_area = soup.find("body") or soup
        
    # Strip unnecessary elements (e.g., pagination buttons, navigation, scripts)
    for tag in content_area.find_all(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
        
    for tag in content_area.find_all(class_=["clipboard-code", "copy", "copied", "failed"]):
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

    # Convert cleaned HTML to markdown using CustomConverter
    converter = CustomConverter(heading_style="ATX")
    markdown_content = converter.convert(str(content_area))
    return markdown_content.strip(), images_to_download


