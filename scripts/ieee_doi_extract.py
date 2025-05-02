import requests
from bs4 import BeautifulSoup

def extract_doi(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(response.text)
        # exit(1)
        doi = response.text.split('doi":"')[1].split('"')[0]
        if doi:
            return doi
        # script_tags = soup.find_all('script')
        # print(len(script_tags))
        # for script_tag in script_tags:
        #     script_test = script_tag.text
        #     if 'xplGlobal.document.metadata' in script_test:
                # doi = script_test.split('doi":"')[1].split('"')[0]
                # if doi:
                #     return doi
        print("No script tag containing metadata found on this page.")
        exit(1)
    except Exception as e:
        return f"An error occurred: {str(e)}"

