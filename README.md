# WebScraper


## Using Nix 
```nix
nix develop
```

## Not using nix

```bash
pip install aiohttp playwright beautifulsoup4 lxml click rich
playwright install chromium
```

# Usage

## Basic Usage

```bash
python cli.py https://example.com --out output.json
```

## Adding crawl depth

```bash
python cli.py https://example.com --depth 2 --out output.json
```

## Output Format

```json
{
  "target": "https://example.com",
  "depth": 1,
  "timestamp": "2026-01-12T16:28:31.979151",
  "pages": [
    {
      "url":"https://example.com",
      "plugins": {
        "text": "Example Domain",
        "emails": []
      }
    }
  ]
}
```


