import os
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, value in attrs:
                if attr == "href":
                    self.links.append(value)

def check_links():
    html_root = "html"
    broken_links = []
    
    for root, dirs, files in os.walk(html_root):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                parser = LinkExtractor()
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    parser.feed(content)
                
                for link in parser.links:
                    # Skip external links and javascript
                    if link.startswith("http") or link.startswith("mailto:") or link.startswith("javascript:"):
                        continue
                    # Skip fragment-only links
                    if link.startswith("#"):
                        continue
                    
                    # Resolve relative path
                    target_path = urljoin(file_path, link)
                    # Normalize and remove fragments
                    target_path = urlparse(target_path).path
                    
                    if not os.path.exists(target_path):
                        broken_links.append(f"In {file_path}: Broken link to {link}")

    if not broken_links:
        print("All internal links are working correctly.")
    else:
        print("Broken links found:")
        for bl in broken_links:
            print(bl)

if __name__ == "__main__":
    check_links()
