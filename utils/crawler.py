import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        
        # Limit the description to a maximum of 150 characters
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'][:150] + '...' if description else 'No description found'
        
        # Limit the number of headers collected to a maximum of 5
        headers = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])][:5]
        
        # Remove paragraphs entirely
        paragraphs = []  # Exclude paragraphs to reduce text

        links = [a['href'] for a in soup.find_all('a', href=True)]
        broken_links = []
        for link in links:
            full_url = urljoin(url, link)
            try:
                link_response = requests.head(full_url, allow_redirects=True)
                link_response.raise_for_status()  # Raise an error for bad responses
            except requests.exceptions.RequestException as e:
                broken_links.append(full_url)
                print(f"Broken link found: {full_url} - Error: {e}")

        # Remove duplicate content collection
        duplicate_content = []  # Exclude duplicate content

        # Construct robots.txt URL
        robots_url = urljoin(url, '/robots.txt')
        print(f"Fetching robots.txt from: {robots_url}")  # Debugging line
        robots_response = requests.get(robots_url)
        robots_content = robots_response.text if robots_response.status_code == 200 else 'No robots.txt found'

        # Construct sitemap.xml URL
        sitemap_url = urljoin(url, '/sitemap.xml')
        print(f"Fetching sitemap.xml from: {sitemap_url}")  # Debugging line
        sitemap_response = requests.get(sitemap_url)
        sitemap_content = sitemap_response.text if sitemap_response.status_code == 200 else 'No sitemap found'

        return {
            'title': title,
            'description': description_content,
            'headers': headers,
            'paragraphs': paragraphs,  # No paragraphs collected
            'broken_links': broken_links,
            'duplicate_content': duplicate_content,  # No duplicate content collected
            'robots_content': robots_content,
            'sitemap_content': sitemap_content
        }
    else:
        return None
