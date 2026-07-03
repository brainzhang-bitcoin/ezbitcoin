from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls(html_content: str) -> list[str]:
    soup = BeautifulSoup(html_content, "lxml")
    links = []
    base_url = "https://learnmeabitcoin.com/"
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if (
            href.startswith("/beginners/")
            or href.startswith("/technical/")
            or "learnmeabitcoin.com/beginners/" in href
            or "learnmeabitcoin.com/technical/" in href
        ):
            links.append(urljoin(base_url, href))
    return sorted(list(set(links)))
