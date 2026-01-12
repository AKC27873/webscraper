import asyncio
import click
from core.crawler import crawl
from core.writer import write_json
from plugins import emails, text # You can add more here.


PLUGINS = {
    "emails": emails.extract,
    "text": text.extract,
}

@click.command()
@click.argument("url")
@click.option("--depth", default=1, show_default=True)

@click.option(
        "--out",
        required=True,
        type=click.Path(dir_okay=False, writable=True),
        help="JSON out file"
)

def main(url, depth, out):
    async def run():
        pages = []
        results = await crawl(url, depth)
        for page_url, html in results:
            page_data = {
                "url": page_url,
                "plugins": {}
            }
            
            for name, extractor in PLUGINS.items():
                try:
                    page_data["plugins"][name] = extractor(html)
                except Exception as e:
                    page_data["plugins"][name] = {"error": str(e)}

            pages.append(page_data)
        write_json(url, depth, pages, out)
        print(f"Saved {len(pages)} pages -> {out}")
    asyncio.run(run())
if __name__ == "__main__":
    main()
