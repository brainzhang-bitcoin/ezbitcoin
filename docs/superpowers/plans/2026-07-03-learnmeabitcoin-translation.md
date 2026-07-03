# Learn Me A Bitcoin Translation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Translate all scraped markdown files in `docs/` from English to Chinese, directly overwriting the source files, utilizing parallel translation subagents.

**Architecture:** Split the codebase docs into 4 Group lists, dispatch a subagent for each group running in parallel, verify translation completeness, and check syntax integrity.

**Tech Stack:** AI translation subagents (inheriting session model), file editing.

## Global Constraints
- Target folder: `docs/`
- Target language: Chinese (Simplified)
- Terminology rule: Keep `UTXO`, `SegWit`, `Taproot`, `WIF`, `Bech32`, `Base58`, `PSBT`, `ECDSA`, `Schnorr`, `VarInt`, `Opcode`, `Coinbase`, `Nonce`, `Merkle Root`, `HD Wallets`, `txid`, `wtxid`, `vout` untranslated.
- Do not modify markdown layout, link paths, or code block contents.

---

### Task 1: Generate Group Lists and Initial Verification Test

**Files:**
- Create: `translate_groups.py`
- Create: `tests/test_translation.py`

**Interfaces:**
- Consumes: None
- Produces: JSON grouped files lists, verification test structure.

- [ ] **Step 1: Write translate_groups.py**

```python
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
```

- [ ] **Step 2: Generate groups.json file**

Run: `python translate_groups.py`
Expected: File `groups.json` is created with list of files for each group.

- [ ] **Step 3: Create tests/test_translation.py**

```python
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
```

- [ ] **Step 4: Run test to verify environment**

Run: `pytest tests/test_translation.py -v`
Expected: PASS (since no files are translated yet)

- [ ] **Step 5: Commit**

```bash
git add translate_groups.py tests/test_translation.py
git commit -m "feat: setup translation grouping and verification test"
```

---

### Task 2: Translate Group 1 (Beginners)

**Files:**
- Modify: `docs/beginners.md` and all files listed in `groups.json` -> `group_1`

**Interfaces:**
- Consumes: `groups.json`
- Produces: Translated Chinese markdown files for Group 1.

- [ ] **Step 1: Dispatch translation subagent for Group 1**
Prompt: Translate Group 1 files listed under `group_1` in `groups.json` directly overwriting the original files using standard translation prompt.

- [ ] **Step 2: Verify Group 1 files translated**
Check that files like `docs/beginners.md` and `docs/beginners/wallets.md` contain Chinese text and preserve technical terms.

- [ ] **Step 3: Commit**

```bash
git add docs/beginners.md docs/beginners/
git commit -m "feat: translate beginners guide docs to Chinese"
```

---

### Task 3: Translate Group 2 (Technical Core & Basics)

**Files:**
- Modify: `docs/technical.md` and all files listed under `group_2` in `groups.json`

**Interfaces:**
- Consumes: `groups.json`
- Produces: Translated Chinese markdown files for Group 2.

- [ ] **Step 1: Dispatch translation subagent for Group 2**
Prompt: Translate Group 2 files listed under `group_2` in `groups.json` directly overwriting the original files using standard translation prompt.

- [ ] **Step 2: Verify Group 2 files translated**
Check that files like `docs/technical/general/hexadecimal.md` contain Chinese text and code blocks are unchanged.

- [ ] **Step 3: Commit**

```bash
git add docs/technical.md docs/technical/block/ docs/technical/blockchain/ docs/technical/cryptography/ docs/technical/general/
git commit -m "feat: translate technical core docs to Chinese"
```

---

### Task 4: Translate Group 3 (Technical Keys & Transaction)

**Files:**
- Modify: All files listed under `group_3` in `groups.json`

**Interfaces:**
- Consumes: `groups.json`
- Produces: Translated Chinese markdown files for Group 3.

- [ ] **Step 1: Dispatch translation subagent for Group 3**
Prompt: Translate Group 3 files listed under `group_3` in `groups.json` directly overwriting the original files using standard translation prompt.

- [ ] **Step 2: Verify Group 3 files translated**
Check that files like `docs/technical/keys/hd-wallets.md` contain Chinese text and preserve terms.

- [ ] **Step 3: Commit**

```bash
git add docs/technical/keys/ docs/technical/transaction/
git commit -m "feat: translate keys and transactions docs to Chinese"
```

---

### Task 5: Translate Group 4 (Technical Scripts, Mining, Networking)

**Files:**
- Modify: All files listed under `group_4` in `groups.json`

**Interfaces:**
- Consumes: `groups.json`
- Produces: Translated Chinese markdown files for Group 4.

- [ ] **Step 1: Dispatch translation subagent for Group 4**
Prompt: Translate Group 4 files listed under `group_4` in `groups.json` directly overwriting the original files using standard translation prompt.

- [ ] **Step 2: Verify Group 4 files translated**
Check that files like `docs/technical/script/p2tr.md` contain Chinese text and preserve terms.

- [ ] **Step 3: Commit**

```bash
git add docs/technical/script/ docs/technical/mining/ docs/technical/networking/ docs/technical/upgrades/
git commit -m "feat: translate script, mining, networking, upgrades docs to Chinese"
```

---

### Task 6: Final Validation

**Files:**
- Modify: None

**Interfaces:**
- Consumes: None
- Produces: All tests verified.

- [ ] **Step 1: Run pytest to verify all links and Markdown formats are valid**

Run: `pytest tests/test_translation.py -v`
Expected: PASS

- [ ] **Step 2: Cleanup temporary groups.json and translate_groups.py**

Run: `rm -f groups.json translate_groups.py`
Expected: Clean directory.

- [ ] **Step 3: Commit final check**

```bash
git add .
git commit -m "chore: cleanup temporary translation helper files and complete translation verify"
```
