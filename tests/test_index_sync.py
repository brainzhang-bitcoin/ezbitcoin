import os
import re

def test_index_is_in_sync_with_readme():
    readme_path = "README.md"
    index_path = "docs/index.md"
    
    assert os.path.exists(readme_path), "README.md does not exist"
    assert os.path.exists(index_path), "docs/index.md does not exist"
    
    # docs/index.md must be a real file, not a symlink, so Zensical link rewriting works correctly
    assert not os.path.islink(index_path), "docs/index.md is a symlink, it should be a real file"
    
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
        
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
        
    # Expected index content is README.md content with `](docs/` replaced with `](`
    expected_content = re.sub(r'\]\(docs/', '](', readme_content)
    
    assert index_content == expected_content, (
        "docs/index.md is out of sync with README.md.\n"
        "Please run `python scripts/sync_index.py` to synchronize them."
    )
