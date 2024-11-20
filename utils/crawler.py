import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else 'No description found'
        
        headers = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        
        links = [a['href'] for a in soup.find_all('a', href=True)]
        broken_links = []
        for link in links:
            full_url = urljoin(url, link)
            link_response = requests.head(full_url, allow_redirects=True)
            if link_response.status_code != 200:
                broken_links.append(full_url)

        duplicate_content = set([p for p in paragraphs if paragraphs.count(p) > 1])

        robots_url = urljoin(url, '/robots.txt')
        robots_response = requests.get(robots_url)
        robots_content = robots_response.text if robots_response.status_code == 200 else 'No robots.txt found'

        sitemap_url = urljoin(url, '/sitemap.xml')
        sitemap_response = requests.get(sitemap_url)
        sitemap_content = sitemap_response.text if sitemap_response.status_code == 200 else 'No sitemap found'

        return {
            'title': title,
            'description': description_content,
            'headers': headers,
            'paragraphs': paragraphs,
            'broken_links': broken_links,
            'duplicate_content': list(duplicate_content),
            'robots_content': robots_content,
            'sitemap_content': sitemap_content
        }
    else:
        return None
