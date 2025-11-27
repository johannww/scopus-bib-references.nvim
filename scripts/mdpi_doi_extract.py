import requests
import re, requests

def extract_doi(url):
    m = re.search(r"mdpi\.com/([^/]+)/([^/]+)/([^/]+)/([^/?#]+)", url)
    if not m:
        return None

    issn, volume, issue, article = m.groups()

    # build Crossref URL with parameters directly in the URL
    crossref_url = (
        f"https://api.crossref.org/works?"
        f"query={url.split('https://www.mdpi.com/')[1]}"
    )

    r = requests.get(crossref_url, timeout=10)
    items = r.json().get("message", {}).get("items", [])
    for item in items:
        if item["URL"].find(f"{volume}{issue}{article}") != -1:
            return item.get("DOI")
    return None
