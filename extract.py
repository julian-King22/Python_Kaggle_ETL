import os
import zipfile
import shutil


def create_download_dir():
    download_dir = "data/downloads"

    if not os.path.exists(download_dir):
        os.makedirs(f"{download_dir}", exist_ok=True)
    
    return download_dir

