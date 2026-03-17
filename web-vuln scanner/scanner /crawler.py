import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def crawl(url, base_url):
    if url in visited:
        return []

    visited.add(url)
    print(f"[+] Crawling: {url}")

    urls = []
    forms = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if base_url in next_url:
                urls.append(next_url)

    except:
        pass

    return urls, forms
