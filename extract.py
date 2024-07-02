import os
import zipfile
import shutil


def create_download_dir():
    download_dir = "data/downloads"

    if not os.path.exists(download_dir):
        os.makedirs(f"{download_dir}", exist_ok=True)
    
    return download_dir


def download_file(download_dir):
    zip_file_path = os.path.join(f"{download_dir}", 'orders.csv.zip')

    if os.path.exists(zip_file_path):
        print('file already exists')
    else:
        os.system(f'kaggle datasets download ankitbansal06/retail-orders -f orders.csv -p {download_dir}')

    return zip_file_path, download_dir
