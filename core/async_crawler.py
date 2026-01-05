import aiohttp
import asyncio
from urllib.parse import urljoin
from bs4 import BeautifulSoup


async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except:
        return ""


async def crawl_async(base_url, limit=20):
    urls = set([base_url])
    visited = set()

    async with aiohttp.ClientSession() as session:
        while urls and len(visited) < limit:
            url = urls.pop()
            visited.add(url)

            html = await fetch(session, url)
            soup = BeautifulSoup(html, "html.parser")

            for link in soup.find_all("a", href=True):
                new_url = urljoin(base_url, link["href"])
                if base_url in new_url and new_url not in visited:
                    urls.add(new_url)

    return list(visited)


def crawl(base_url):
    print("[*] Async crawling target...")
    return asyncio.run(crawl_async(base_url))
