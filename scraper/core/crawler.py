import aiohttp
import asyncio 
from urllib.parse import urljoin, urlparse
from collections import deque
from core.browser import render_page

async def crawl(start_url, depth):
    visited = set()
    queue = deque([(start_url, 0)])
    results = []
    
    while queue:
        url, d = queue.popleft()
        if url in visited or d > depth:
            continue
        visited.add(url)

        try:
            html = await render_page(url)
        except Exception:
            continue
        
        results.append((url, html))

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "lxml")
        domain = urlparse(start_url).netloc

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            if urlparse(link).netloc == domain:
                queue.append((link, d + 1))
    return results
