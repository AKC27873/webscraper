from bs4 import BeautifulSoup

def extract(html):
    soup = BeautifulSoup(html, "lxml")
    return " ".join(soup.stripped_strings)

