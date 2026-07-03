import os

def test_translation_integrity():
    # Helper to check if any translation broke standard link structures
    import re
    link_pattern = re.compile(r"\[([^]]*)\]\(([^)]*)\)")
    
    docs_dir = "docs"
    for root, dirs, files in os.walk(docs_dir):
        if "superpowers" in root or "images" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Ensure no Chinese characters are in URLs
                for match in link_pattern.finditer(content):
                    url = match.group(2)
                    # Check if url contains Chinese characters
                    assert not re.search(r"[\u4e00-\u9fa5]", url), f"URL contains Chinese characters: {url} in {path}"
