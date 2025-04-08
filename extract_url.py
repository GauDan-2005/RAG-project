import requests
import xml.etree.ElementTree as ET

def get_sitemap_urls(sitemap_url):
    """
    Fetches all URLs from a given sitemap URL.

    Args:
        sitemap_url (str): The URL of the sitemap.

    Returns:
        list: A list of URLs found in the sitemap.
    """
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        urls = [url.text for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        return urls
    return []

# sitemap -->all the urls website
