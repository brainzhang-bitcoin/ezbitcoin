import os
import json

def get_groups():
    docs_dir = "docs"
    groups = {
        "group_1": [],
        "group_2": [],
        "group_3": [],
        "group_4": []
    }
    
    # Walk docs recursively
    for root, dirs, files in os.walk(docs_dir):
        # Exclude superpowers/ specs/plans
        if "superpowers" in root or "images" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.relpath(os.path.join(root, file))
                
                # Assign to groups
                if "beginners" in file_path:
                    groups["group_1"].append(file_path)
                elif any(p in file_path for p in ["block/", "blockchain/", "cryptography/", "general/"]) or file_path == "docs/technical.md":
                    groups["group_2"].append(file_path)
                elif any(p in file_path for p in ["keys/", "transaction/"]):
                    groups["group_3"].append(file_path)
                elif any(p in file_path for p in ["script/", "mining/", "networking/", "upgrades/"]):
                    groups["group_4"].append(file_path)
                    
    return groups

if __name__ == "__main__":
    groups = get_groups()
    with open("groups.json", "w") as f:
        json.dump(groups, f, indent=2)
    print("Groups generated in groups.json")
