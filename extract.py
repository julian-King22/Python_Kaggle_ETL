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

def extract_file(zip_file_path, download_dir):
    dataset_dir = "data"
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(f'{dataset_dir}/orders.zip')
            print(f"Downloaded and extracted to: {dataset_dir}")
    except:
        print("Failed to download the file.")
    finally:
        shutil.rmtree(f"{download_dir}")


if __name__ == "__main__":
    data_folder = create_download_dir()
    file_path, download_dir = download_file(data_folder)
    extract_file(file_path, download_dir)