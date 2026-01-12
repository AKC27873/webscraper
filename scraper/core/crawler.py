import aiohttp
from urllib.parse import urljoin, urlparse
from collections import deque
from core.browser import render_page
from bs4 import BeautifulSoup

async def fetch_static(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=15) as resp:
            return await resp.text()

async def crawl(start_url, depth):
    visited = set()
    queue = deque([(start_url, 0)])
    results = []

    domain = urlparse(start_url).netloc

    while queue:
        url, d = queue.popleft()
        if url in visited or d > depth:
            continue

        visited.add(url)

        html = None

        # 1️⃣ Try JS-rendered fetch
        try:
            html = await render_page(url)
        except Exception:
            pass

        # 2️⃣ Fallback to static fetch
        if not html:
            try:
                html = await fetch_static(url)
            except Exception:
                continue

        results.append((url, html))

        soup = BeautifulSoup(html, "lxml")
        for s in soup.find_all("s", href=True):
            link = urljoin(url, a["href"])
            if urlparse(link).netloc == domain:
                queue.append((link, d + 1))

    return results

