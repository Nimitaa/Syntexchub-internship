from scanner.crawler import crawl
from scanner.injector import submit_form
from scanner.detector import is_vulnerable
from scanner.reporter import save_report

base_url = "http://testphp.vulnweb.com"

# Load payloads
with open("payloads/xss_payloads.txt") as f:
    payloads = f.read().splitlines()

to_visit = [base_url]
visited = set()
vulnerabilities = []

while to_visit:
    url = to_visit.pop()

    if url in visited:
        continue
    visited.add(url)

    urls, forms = crawl(url, base_url)

    for form in forms:
        for payload in payloads:
            response = submit_form(form, url, payload)

            if is_vulnerable(response, payload):
                print(f"[VULNERABLE] {url}")

                vulnerabilities.append({
                    "url": url,
                    "payload": payload
                })

    to_visit.extend(urls)

save_report(vulnerabilities)
