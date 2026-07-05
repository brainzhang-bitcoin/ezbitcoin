#!/usr/bin/env python3
import os
import re

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(project_root, "README.md")
    index_path = os.path.join(project_root, "docs/index.md")
    
    print(f"Reading from {readme_path}...")
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
        
    expected_content = re.sub(r'\]\(docs/', '](', readme_content)
    
    if os.path.exists(index_path):
        if os.path.islink(index_path):
            print(f"Removing symlink {index_path}...")
            os.unlink(index_path)
        else:
            print(f"Overwriting existing file {index_path}...")
    else:
        print(f"Creating file {index_path}...")
        
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(expected_content)
        
    print("Synchronization complete!")

if __name__ == "__main__":
    main()
