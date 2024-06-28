# photo_loader.py

import os
import glob
from google_images_search import GoogleImagesSearch

# Initialize Google Images Search with dev key and cx
gis = GoogleImagesSearch(os.getenv("GCS_DEVELOPER_KEY"), os.getenv("GCS_CX"))

# Function to search and download images
def search_and_download_images(query, n):
    _search_params = {
        'q': query,
        'num': n,
        'fileType': 'jpg|gif|png',
    }
    try:
        gis.search(search_params=_search_params, path_to_dir='./images/')
        filenames = [f for f in os.listdir('./images/') if os.path.isfile(os.path.join('./images/', f))]
        return filenames
    except Exception as e:
        print(e)

# Function to empty the images folder
def empty_images_folder():
    folder_path = "./images/"
    file_list = glob.glob(os.path.join(folder_path, "*"))
    for file_path in file_list:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
