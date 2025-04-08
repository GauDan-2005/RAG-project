from bs4 import BeautifulSoup
import time
import requests


def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all relevant elements in the order they appear on the page
            content_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a'])
            
            # Extract text from the elements
            full_text = ' '.join([element.get_text() for element in content_elements])
            
            return full_text.strip()
        else:
            print(f"Failed to fetch {url} - Status Code:", response.status_code)
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


import time
from typing import Dict, List

def fetch_website_contents(urls: List[str], 
                          max_pages: int = 5, 
                          delay: float = 1.0, 
                          preview_length: int = 500) -> Dict[str, str]:
    """
    Fetches content from multiple web pages with rate limiting and preview display.
    
    Args:
        urls: List of URLs to fetch content from
        max_pages: Maximum number of pages to fetch (default: 5)
        delay: Delay between requests in seconds (default: 1.0)
        preview_length: Number of characters to show in preview (default: 500)
    
    Returns:
        Dictionary with URLs as keys and page content as values
    """
    website_data = {}
    
    for url in urls[:max_pages]:
        try:
            print(f"Fetching content from: {url}")
            content = fetch_page_content(url)  # Assuming this function exists
            website_data[url] = content
            
            # Print preview
            print("\nSample Extracted Content:")
            print(f"URL: {url}")
            print(content[:preview_length])
            print("\n" + "=" * 80 + "\n")
            
            time.sleep(delay)
            
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            website_data[url] = None
    
    return website_data
