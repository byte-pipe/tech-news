import os
import re
import requests
from datetime import datetime
from typing import List, Tuple

def find_broken_links() -> List[Tuple[str, str]]:
    """Find broken links in today's scraped data."""
    data_dir = 'data'
    today = datetime.now().strftime('%Y-%m-%d')
    today_dir = os.path.join(data_dir, today)

    if not os.path.exists(today_dir):
        return []

    url_pattern = re.compile(r'https?://[^\s<>]+')
    broken_links = []

    for file in os.listdir(today_dir):
        if not file.endswith('.md'):
            continue
        with open(os.path.join(today_dir, file), 'r') as f:
            content = f.read()
            urls = url_pattern.findall(content)
            for url in urls:
                try:
                    response = requests.head(url, allow_redirects=True, timeout=5)
                    if response.status_code >= 400:
                        broken_links.append((url, f'status: {response.status_code}'))
                except Exception as e:
                    broken_links.append((url, f'connection failed: {str(e)}'))

    return broken_links

def main():
    broken_links = find_broken_links()
    if broken_links:
        print('Found broken links:')
        for url, reason in broken_links:
            print(f'- {url} ({reason})')
        exit(1)
    else:
        print('No broken links found')
        exit(0)

if __name__ == '__main__':
    main()