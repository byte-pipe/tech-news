import os
from datetime import datetime

def validate_data():
    """Validate the scraped data for today."""
    # Get project root directory (three levels up from this script)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    data_dir = os.path.join(project_root, 'data')
    today = datetime.now().strftime('%Y-%m-%d')
    today_dir = os.path.join(data_dir, today)

    if not os.path.exists(today_dir):
        print('No data directory found for today')
        return False

    files = os.listdir(today_dir)
    if not files:
        print('No files found in today\'s directory')
        return False

    for file in files:
        if not file.endswith('.md'):
            continue
        with open(os.path.join(today_dir, file), 'r') as f:
            content = f.read()
            if len(content.strip()) < 10:
                print(f'File {file} seems empty or too small')
                return False

    return True

if __name__ == '__main__':
    exit(0 if validate_data() else 1)