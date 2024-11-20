import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else 'No description found'
        
        headers = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        
        return {
            'title': title,
            'description': description_content,
            'headers': headers,
            'paragraphs': paragraphs
        }
    else:
        return None
