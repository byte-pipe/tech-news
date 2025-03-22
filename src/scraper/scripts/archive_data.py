import os
import shutil
from datetime import datetime, timedelta

def archive_old_data(days_to_keep: int = 30):
    """Archive data directories older than specified days."""
    data_dir = 'data'
    archive_dir = os.path.join(data_dir, 'archive')

    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    cutoff_date = datetime.now() - timedelta(days=days_to_keep)

    for dir_name in os.listdir(data_dir):
        if dir_name == 'archive':
            continue

        try:
            dir_date = datetime.strptime(dir_name, '%Y-%m-%d')
            if dir_date < cutoff_date:
                source = os.path.join(data_dir, dir_name)
                target = os.path.join(archive_dir, dir_name)
                shutil.move(source, target)
                print(f'Archived {dir_name}')
        except ValueError:
            continue

def main():
    try:
        archive_old_data()
        print('Data archiving completed successfully')
        exit(0)
    except Exception as e:
        print(f'Error during archiving: {str(e)}')
        exit(1)

if __name__ == '__main__':
    main()