# Design Spec: Reorganize Documents into "External" (番外篇) Section

## Goal
Reorganize documentation files by grouping external/recommended blog posts and miscellaneous articles under a new top-level section called "External" (番外篇). This improves the logical flow of "Beginners" (新手指南) and "Technical" (技术核心) sections.

## Proposed Changes

### 1. File Movements
Move the following files into the newly created `docs/external/` directory:
- `docs/beginners/bitcoin-past-present-future.md` -> `docs/external/bitcoin-past-present-future.md`
- `docs/beginners/ancient-miners-move-bitcoins.md` -> `docs/external/ancient-miners-move-bitcoins.md`
- `docs/beginners/how-us-government-seizes-bitcoins.md` -> `docs/external/how-us-government-seizes-bitcoins.md`
- `docs/beginners/ten-lines-of-code-challenge-financial-system.md` -> `docs/external/ten-lines-of-code-challenge-financial-system.md`
- `docs/beginners/the-book-of-satoshi-reading-notes.md` -> `docs/external/the-book-of-satoshi-reading-notes.md`
- `docs/beginners/the-internet-of-money-reading-notes.md` -> `docs/external/the-internet-of-money-reading-notes.md`
- `docs/technical/cryptography/bitcoin-private-key-collision-ideas.md` -> `docs/external/bitcoin-private-key-collision-ideas.md`
- `docs/technical/networking/ideal-bitcoin-full-node-implementation.md` -> `docs/external/ideal-bitcoin-full-node-implementation.md`

### 2. Add Entry Page
Create `docs/external.md` as the entry page:
- Title: `# 比特币番外篇`
- Content: Contains brief introductions and links to all the moved articles.

### 3. Update Site Navigation
Update `zensical.toml` to:
- Create a new top-level nav item `"番外篇"` mapping to the moved files and `external.md`.
- Remove these 8 articles from `"新手指南"` and `"技术核心"` sections.

### 4. Link Updating
- Update `README.md` and sync it to `docs/index.md` (removing `docs/` prefix in `index.md`).
- Update references in `docs/beginners.md`, `docs/technical.md`, and any other markdown files in the repository.
