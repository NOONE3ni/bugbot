import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def crawl(url):
    urls = set()

    # Always include the target itself
    urls.add(url)

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            urls.add(full_url)

    except Exception:
        pass

    return list(urls)
