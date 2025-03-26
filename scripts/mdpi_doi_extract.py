import requests
from bs4 import BeautifulSoup

def extract_doi(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        doi = soup.find("meta", {"name":"citation_doi"}).get("content")
        if doi:
            return doi
        else:
            print("No DOI found on MDPI page")
            exit(1)
    except Exception as e:
        return f"An error occurred: {str(e)}"
