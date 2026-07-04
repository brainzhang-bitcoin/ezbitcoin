import os
import re
from pathlib import Path

def sanitize_filename(url: str) -> str:
    # Extract path portion and replace slashes and special chars with underscores
    if "learnmeabitcoin.com/" in url:
        path = url.split("learnmeabitcoin.com/")[-1]
    elif "brainz.fun/" in url:
        path = url.split("brainz.fun/")[-1]
        path = path.replace("images/blog/", "")
    else:
        from urllib.parse import urlparse
        path = urlparse(url).path

    path = path.replace("images/", "").replace("assets/", "")
    sanitized = re.sub(r"[^a-zA-Z0-9\.\-_]", "_", path)
    return sanitized.strip("_")

def get_relative_img_path(md_file_path: str, image_name: str) -> str:
    # Count directories between docs/ and target markdown file
    normalized = md_file_path.replace("\\", "/")
    parts = Path(normalized).parts
    # Format: docs/dir1/dir2/file.md -> parts has len 4 (docs, dir1, dir2, file.md)
    # The image path is always in docs/images/.
    # Number of up-steps is len(parts) - 2
    steps = len(parts) - 2
    prefix = "../" * steps if steps > 0 else ""
    return f"{prefix}images/{image_name}"

