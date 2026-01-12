{pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  name = "webscraper";
  
  buildInputs = with pkgs; [
    python312
    python312Packages.aiohttp
    python312Packages.beautifulsoup4
    python312Packages.lxml
    python312Packages.click
    python312Packages.rich
    python312Packages.playwright

    # Runtime tools
    nodejs
    tor
    sqlite
  ];

  shellhook = '' 
    export PLAYWRIGHT_BROWSERS_PATH=0
    echo "Installing Playwright browsers..."
    playwright install chromium
    echo "WebIntel dev shell ready"

  '';
}
