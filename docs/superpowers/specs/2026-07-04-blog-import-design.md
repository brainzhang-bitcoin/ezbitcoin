# Design Spec: Import Bitcoin Blog Posts from brainz.fun

This specification outlines the design for importing specific Bitcoin and Lightning-related blog posts from `https://brainz.fun/blog/categories/blockchain/` into the local `docs/` repository structure.

## 1. Scope & Mapping Rules

Only Bitcoin and Lightning Network-related articles are extracted. The Chinese pinyin slugs are mapped to standard English filenames.

### Target Mapping Table:

- **docs/beginners/**
  - `mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de` -> `how-us-government-seizes-bitcoins.md`
  - `yuan-gu-kuang-gong-zhuan-yi-8mo-mei-bi-te-bi` -> `ancient-miners-move-bitcoins.md`
  - `shi-xing-dai-ma-dian-fu-shi-jie-jin-rong-ti-xi` -> `ten-lines-of-code-challenge-financial-system.md`
  - `is-craig-wright-real-satoshi-nakamoto-2` -> `is-craig-wright-real-satoshi-part2.md`
  - `the-internet-of-money-du-shu-bi-ji` -> `the-internet-of-money-reading-notes.md`
  - `the-book-of-satoshi-du-shu-bi-ji` -> `the-book-of-satoshi-reading-notes.md`
  - `bi-te-bi-de-guo-qu-xian-zai-he-wei-lai` -> `bitcoin-past-present-future.md`
  - `happy-10th-birthday-bitcoin` -> `happy-10th-birthday-bitcoin.md`

- **docs/technical/lightning/** (New Directory)
  - `lnd-low-rescan-speed-for-startup` -> `lnd-low-rescan-speed-startup.md`
  - `how-to-close-lightning-channels-by-lnd-cli` -> `how-to-close-lightning-channels-by-lnd-cli.md`
  - `hello-lightning-network-3` -> `hello-lightning-network-part3.md`
  - `hello-lightning-network-2` -> `hello-lightning-network-part2.md`
  - `hello-lightning-network-1` -> `hello-lightning-network-part1.md`
  - `hello-lightning-network-0` -> `hello-lightning-network-part0.md`
  - `setup-lightning-node-cheat-sheet` -> `setup-lightning-node-cheat-sheet.md`
  - `eltoo-shan-dian-he-chi-xian-qi-yue-geng-xin-ji-zhi` -> `eltoo-lightning-offchain-contracts.md`
  - `shan-dian-wang-luo-man-man-cheng-chang` -> `lightning-network-gradual-growth.md`

- **docs/technical/networking/**
  - `how-to-set-systemd-startup-script-for-bitcoind` -> `how-to-set-systemd-startup-script-for-bitcoind.md`
  - `li-xiang-zhong-de-bi-te-bi-quan-jie-dian-shi-xian` -> `ideal-bitcoin-full-node-implementation.md`

- **docs/technical/blockchain/**
  - `bi-te-bi-de-blockchain-2` -> `bitcoin-blockchain-part2.md`
  - `bi-te-bi-de-blockchain-1` -> `bitcoin-blockchain-part1.md`

- **docs/technical/cryptography/**
  - `yi-chong-ti-gao-bi-te-bi-si-yao-peng-zhuang-ji-lu-de-si-lu` -> `bitcoin-private-key-collision-ideas.md`

- **docs/technical/transaction/**
  - `bi-te-bi-de-jiao-yi-6` -> `bitcoin-transaction-part6.md`
  - `bi-te-bi-de-jiao-yi-5` -> `bitcoin-transaction-part5.md`

## 2. Scraping and Cleaning Logic

1. **Content Extraction**: Target `<article role="article">` or `<div class="entry-content">`. Remove sharing elements (`div.sharing`), comments (`#disqus_thread`), and footer tags.
2. **Format Conversion**: Convert HTML to Markdown (retaining original Chinese text).
3. **Image Isolation**: Download images to `docs/images/` with a `blog_` filename prefix and resolve relative paths based on target directory depth (e.g. `../../images/` or `../../../images/`).
4. **Internal Link Rewriting**: Intercept any `href` link matching `/blog/\d{4}/\d{2}/\d{2}/<slug>/` and rewrite it to point to the correct local markdown file.
