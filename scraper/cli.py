import asyncio
import click
from core.crawler import crawl
from core.storage import init_db
from plugins import emails, text

@click.command()
@click.argument("url")
@click.option("--depth", default=1)

def main(url, depth):
    async def run():
        db = await init_db()
        pages = await crawl(url, depth)

        for page_url, html in pages:
            content = text.extract(html)
            await db.execute(
                "INSERT OR REPLACE INTO pages VALUES (?, ?)",
                (page_url, content)
            )

        await db.commit()
        print(f"Scraped {len(pages)} pages")
    asyncio.run(run())
if __name__ == "__main__":
    main()
