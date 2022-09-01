import shutil
import requests


def download_image(url: str, local_path: str):
    response = requests.get(url, stream=True)
    with open(local_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
