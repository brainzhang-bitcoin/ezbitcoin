import os
from urllib.parse import urlparse, unquote

URL_MAP = {
    "mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de": "docs/beginners/how-us-government-seizes-bitcoins.md",
    "yuan-gu-kuang-gong-zhuan-yi-8mo-mei-bi-te-bi": "docs/beginners/ancient-miners-move-bitcoins.md",
    "shi-xing-dai-ma-dian-fu-shi-jie-jin-rong-ti-xi": "docs/beginners/ten-lines-of-code-challenge-financial-system.md",
    "is-craig-wright-real-satoshi-nakamoto-2": "docs/beginners/is-craig-wright-real-satoshi-part2.md",
    "the-internet-of-money-du-shu-bi-ji": "docs/beginners/the-internet-of-money-reading-notes.md",
    "the-book-of-satoshi-du-shu-bi-ji": "docs/beginners/the-book-of-satoshi-reading-notes.md",
    "bi-te-bi-de-guo-qu-,xian-zai-he-wei-lai": "docs/beginners/bitcoin-past-present-future.md",
    "happy-10th-birthday-bitcoin": "docs/beginners/happy-10th-birthday-bitcoin.md",
    "lnd-low-rescan-speed-for-startup": "docs/technical/lightning/lnd-low-rescan-speed-startup.md",
    "how-to-close-lightning-channels-by-lnd-cli": "docs/technical/lightning/how-to-close-lightning-channels-by-lnd-cli.md",
    "hello-lightning-network-3": "docs/technical/lightning/hello-lightning-network-part3.md",
    "hello-lightning-network-2": "docs/technical/lightning/hello-lightning-network-part2.md",
    "hello-lightning-network-1": "docs/technical/lightning/hello-lightning-network-part1.md",
    "bi-te-bi-de-jiao-yi-7": "docs/technical/lightning/hello-lightning-network-part0.md",
    "setup-lightning-node-cheat-sheet": "docs/technical/lightning/setup-lightning-node-cheat-sheet.md",
    "eltoo-shan-dian-he-chi-xian-qi-yue-geng-xin-ji-zhi": "docs/technical/lightning/eltoo-lightning-offchain-contracts.md",
    "shan-dian-wang-luo-man-man-cheng-chang": "docs/technical/lightning/lightning-network-gradual-growth.md",
    "how-to-set-systemd-startup-script-for-bitcoind": "docs/technical/networking/how-to-set-systemd-startup-script-for-bitcoind.md",
    "li-xiang-zhong-de-bi-te-bi-quan-jie-dian-shi-xian": "docs/technical/networking/ideal-bitcoin-full-node-implementation.md",
    "bi-te-bi-de-blockchain-2": "docs/technical/blockchain/bitcoin-blockchain-part2.md",
    "bi-te-bi-de-blockchain-1": "docs/technical/blockchain/bitcoin-blockchain-part1.md",
    "[?]-chong-ti-gao-bi-te-bi-si-yao-peng-zhuang-ji-lu-de-si-lu": "docs/technical/cryptography/bitcoin-private-key-collision-ideas.md",
    "bi-te-bi-de-jiao-yi-6": "docs/technical/transaction/bitcoin-transaction-part6.md",
    "bi-te-bi-de-jiao-yi-5": "docs/technical/transaction/bitcoin-transaction-part5.md",
}

def get_local_path_for_blog_url(url: str) -> str | None:
    path = urlparse(url).path
    parts = [p for p in path.split("/") if p]
    if not parts:
        return None
    slug = unquote(parts[-1])
    return URL_MAP.get(slug)

def get_relative_link(source_filepath: str, target_filepath: str) -> str:
    source_dir = os.path.dirname(source_filepath)
    rel = os.path.relpath(target_filepath, source_dir)
    return rel.replace("\\", "/")
