import requests
from urllib.parse import urljoin

def submit_form(form, url, payload):
    action = form.get("action")
    method = form.get("method", "get").lower()
    target_url = urljoin(url, action)

    inputs = form.find_all("input")
    data = {}

    for input_tag in inputs:
        name = input_tag.get("name")
        if name:
            data[name] = payload

    if method == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)
