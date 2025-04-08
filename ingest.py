# -----CONNECT MILVUS-----

from milv import database

# ----- GET URLS -----

from extract_url import get_sitemap_urls

SITEMAP_URL = "https://www.kitchener.ca/sitemap.xml"

urls = get_sitemap_urls(SITEMAP_URL)
print(f"Found {len(urls)} URLs")
print(urls[:5])  # Print first 5 URLs


# ----- EXTRACT CONTENT -----

from extract_content import fetch_website_contents

max_pages = 5

print(f"Extracting {max_pages} from {len(urls)}")


website_data = fetch_website_contents(urls, max_pages=max_pages, delay=1.0, preview_length=500)

print(f"Extracted {len(website_data)} from {len(urls)}")


